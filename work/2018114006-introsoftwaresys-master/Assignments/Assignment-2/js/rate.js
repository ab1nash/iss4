var countera = 0;
var arr = [];
function sub() {
	var x = document.getElementById("frm");

  var name = "";
  var skill = "";
  var level = "";
  name += x.elements[0].value;	
  skill += x.elements[1].value;
  level += x.elements[2].value;

  
  	arr.push({
  		nm: name,
  		skill: skill,
  		level: level, 		
  	});

  	var count = countera;
  	countera++;
     
     
     
  
  	var tbl = document.getElementsByTagName("table")[0];
  
    var row = document.createElement("tr");
   
      
      var cell = document.createElement("td");
      cell.innerHTML = arr[count].nm;
      row.appendChild(cell);

      var cell = document.createElement("td");
      cell.innerHTML = arr[count].skill;
      row.appendChild(cell);

      var cell = document.createElement("td");
      cell.innerHTML = arr[count].level;
      row.appendChild(cell);
    
  tbl.appendChild(row);
  
  document.getElementById("frm").reset();

}

window.onscroll = function() {myFunction()}

var navbar = document.getElementById("navbar");

var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
} 

function hover(x) {
   
   var y = document.getElementById(x);
    x.style.color = 'red';
    
}

function hover1(x) {
   
   var y = document.getElementById(x);
    x.style.color = 'white';
    
}


