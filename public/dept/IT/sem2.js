function grade(g) {
  if (g==="O"){
    return 10;
  }else if (g==="A+") {
    return 9;
  }else if (g==="A") {
    return 8;
  }else if (g==="B+") {
    return 7;
  }else if (g==="B") {
    return 6;
  }else if (g==="U") {
    return 0;
  }
}

function validate() {
var mat=document.getElementById('mat');
var eng=document.getElementById('eng');
var chem=document.getElementById('chem');
var eg=document.getElementById('eg');
var cp=document.getElementById('cp');
var ite=document.getElementById('ite');
var cpl=document.getElementById('cpl');
var cheml=document.getElementById('cheml');


var gp1=grade(mat.value);
var gp2=grade(eng.value);
var gp3=grade(chem.value);
var gp4=grade(eg.value);
var gp5=grade(cp.value);
var gp6=grade(ite.value);
var gp7=grade(cpl.value);
var gp8=grade(cheml.value);
var cgpa=(3*(gp2+gp3+gp4+gp5)+2*gp6+1.5*(gp7+gp8)+4*gp1)/21;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7,gp8);
console.log(cgpa);
 document.getElementById("result").innerHTML = "GPA : "+cgpa.toFixed(2);


}

function bigImg(x) {
  x.style.fontSize = "23px";
}

function normalImg(x) {
  x.style.fontSize = "20px";
}
