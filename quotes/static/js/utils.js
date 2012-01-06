function validtest() {
   var boxValue = document.forms["suggestForm"]["validateBox"].value.toLowerCase();    
   if (boxValue != "blue")
      {
         alert("Incorrect");
         return false;
      }
}
