 // <script type = "application/javascript">
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest
var data_file = "localhost:8000/getmarks";
var http_request = new XMLHttpRequest();
           

http_request.onreadystatechange = function(){

   if (http_request.readyState == 4  && http_request.status == 200){
      // Javascript function JSON.parse to parse JSON data
      var jsonObj = JSON.parse(http_request.responseText);

      // jsonObj variable now contains the data structure and can
      // be accessed quest, takes input 'letter', returns JSONas jsonObj.name and jsonObj.country
      for (var key in jsonObj) {
	  if(key[0]=="F");
	  {
	  	console.log(jsonObj[key]);
	  }
	}
   }
   console.log(http_request.readyState);
   
   console.log(http_request.status);
}

http_request.open("POST", data_file, true);
http_request.send();

      // </script>
