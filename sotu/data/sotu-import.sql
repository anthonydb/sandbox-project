--------------------------------------------------------------

-- U.S. President speeches

-- Sources:
-- https://archive.org/details/State-of-the-Union-Addresses-1945-2006
-- http://www.presidency.ucsb.edu/ws/index.php
-- https://www.eisenhower.archives.gov/all_about_ike/speeches.html


-- The Django ORM generates this:

CREATE TABLE public.sotu_speech
(
    id integer NOT NULL DEFAULT nextval('sotu_speech_id_seq'::regclass),
    president character varying(100) COLLATE pg_catalog."default" NOT NULL,
    title character varying(250) COLLATE pg_catalog."default" NOT NULL,
    speech_date date NOT NULL,
    speech_text text COLLATE pg_catalog."default" NOT NULL,
    search_speech_text tsvector,
    CONSTRAINT sotu_speech_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Index: sotu_speech_search__e67881_gin

CREATE INDEX sotu_speech_search__e67881_gin
    ON public.sotu_speech USING gin
    (search_speech_text)
    TABLESPACE pg_default;

--------------
-- Import data

COPY sotu_speech (president, title, speech_date, speech_text)
FROM 'C:\YourDirectory\sotu-1946-1977.csv'
WITH (FORMAT CSV, DELIMITER '|', HEADER OFF, QUOTE '@');

SELECT * FROM president_speeches;

-- Converting speeches to tsvector in the search_speech_text column

UPDATE sotu_speech
SET search_speech_text = to_tsvector('english', speech_text);

----------------
-- Queries


-- Finding speeches containing the word "Vietnam"

SELECT president, speech_date
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('Vietnam')
ORDER BY speech_date;

-- Displaying search results with ts_headline()

SELECT president,
       speech_date,
       ts_headline(speech_text, to_tsquery('Vietnam'),
                   'StartSel = <,
                    StopSel = >,
                    MinWords=5,
                    MaxWords=7,
                    MaxFragments=1')
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('Vietnam');

-- Finding speeches with the word "transportation" but not "roads"

SELECT president,
       speech_date,
       ts_headline(speech_text, to_tsquery('transportation & !roads'),
                   'StartSel = <,
                    StopSel = >,
                    MinWords=5,
                    MaxWords=7,
                    MaxFragments=1')
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('transportation & !roads');

-- Find speeches where "defense" follows "military"

SELECT president,
       speech_date,
       ts_headline(speech_text, to_tsquery('military <-> defense'),
                   'StartSel = <,
                    StopSel = >,
                    MinWords=5,
                    MaxWords=7,
                    MaxFragments=1')
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('military <-> defense');

-- Bonus: Example with a distance of 2:
SELECT president,
       speech_date,
       ts_headline(speech_text, to_tsquery('military <2> defense'),
                   'StartSel = <,
                    StopSel = >,
                    MinWords=5,
                    MaxWords=7,
                    MaxFragments=2')
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('military <2> defense');

-- Scoring relevance with ts_rank()

SELECT president,
       speech_date,
       ts_rank(search_speech_text,
               to_tsquery('war & security & threat & enemy')) AS score
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('war & security & threat & enemy')
ORDER BY score DESC
LIMIT 5;

-- Normalizing ts_rank() by speech length

SELECT president,
       speech_date,
       ts_rank(search_speech_text,
               to_tsquery('war & security & threat & enemy'), 2)::numeric 
               AS score
FROM sotu_speech
WHERE search_speech_text @@ to_tsquery('war & security & threat & enemy')
ORDER BY score DESC
LIMIT 5;


