function validtest() {
   var quoteboxValue = document.forms["suggestForm"]["id_item"].value.toLowerCase();
   var sourceboxValue = document.forms["suggestForm"]["id_source"].value.toLowerCase();
   var nameboxValue = document.forms["suggestForm"]["id_name"].value.toLowerCase();
   var mailboxValue = document.forms["suggestForm"]["id_email"].value.toLowerCase();
   var validboxValue = document.forms["suggestForm"]["validateBox"].value.toLowerCase();

   if (quoteboxValue == "")
      {
         var strMessage = "You must enter a quote.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   else if (sourceboxValue == "")
      {
         var strMessage = "Enter the source of the quote.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   else if (nameboxValue == "")
      {
         var strMessage = "Please include your real name.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   else if (mailboxValue == "")
      {
         var strMessage = "Please give an email for us to follow up.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   else if (validboxValue != "blue")
      {
         var strMessage = "The validation word is incorrect.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   return true;
}
