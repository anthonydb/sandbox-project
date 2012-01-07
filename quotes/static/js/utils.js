function validtest() {
   var boxValue = document.forms["suggestForm"]["validateBox"].value.toLowerCase();    
   if (boxValue != "blue")
      {
         var strMessage = "Validation is incorrect.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
}
