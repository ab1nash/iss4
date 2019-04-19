var l = 1;
var str = " ";
var counter;
var  str1  = " ";
 
function changeProfile() {
  l = l + 1;
  if(l > 5) {
    l = 1;
  }
  str = "../img/img"+l+".jpeg";
  document.getElementById("prof").src = str;
}

function like() {

    if(localStorage.getItem("save"))
     { 
     counter = localStorage.getItem("save");
      }
      else {
        counter=0;
      }
     counter++;
     localStorage.setItem("save", counter);
     // var count = localStorage.getItem("save");
     str1 = "Likes:"+counter;
     document.getElementById("counter1").innerHTML = str1;
}

var text = ["Code", "Travel", "be happy" , "play T.T"];
var count = 0;

function changeText() {
    document.getElementById("ani").innerHTML = text[count]
    count < 3 ? count++ : count = 0;
}
setInterval(changeText, 1500);

