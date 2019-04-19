var fifthDay = function(){

var tom = new Date();
tom.setDate(tom.getDate() + 5);
var n = tom.getDay();
if(n===0)
console.log("Sunday");
if(n===1)
console.log("Monday");
if(n===2)
console.log("Tuesday");
if(n===3)
console.log("Wednesday");
if(n===4)
console.log("Thursday");
if(n===5)
console.log("friday");
if(n===6)
console.log("Saturday");

}

fifthDay();
