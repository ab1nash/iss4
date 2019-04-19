for(var name in students){
$("#select1").append("<option>"+name+"</option>");
}

$("#select1").click(function(){
var n = $('#select1').find(":selected").text();
$("#students-body").append("<tr>");
$("#students-body").append("<td>" +n+"</td>");
$("#students-body").append("<td>" +students[n][0]+"</td>");
$("#students-body").append("<td>" +students[n][1]+"</td>");
$("#students-body").append("<td>" +students[n][2]+"</td>");
$("#students-body").append("<td>" +students[n][3]+"</td>");
$("#students-body").append("<td>" +students[n][4]+"</td>");

var total=(students[n][0]+students[n][1]+students[n][2]+students[n][3]+students[n][4])/5;
if(total>90) var grade='A';
else if(total>80) var grade='B';
else if(total>70) var grade='C';
else if(total>60) var grade='D';
else var grade='E';

$("#students-body").append("<td>" +total+"</td>");
$("#students-body").append("<td>" +grade+"</td>");
$("#students-body").append("</tr>");

});