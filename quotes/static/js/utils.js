function validtest() {
   var quoteboxValue = document.forms["suggestForm"]["id_item"].value.toLowerCase();
   var validboxValue = document.forms["suggestForm"]["validateBox"].value.toLowerCase();    
   
   if (quoteboxValue == "")
      {
         var strMessage = "You must enter a quote.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   else if (validboxValue != "blue")
      {
         var strMessage = "Validation is incorrect.";
         document.getElementById('message').innerHTML = strMessage;
         return false;
      }
   return true;
}
