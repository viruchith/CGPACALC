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
var eng=document.getElementById('eng');
var mat=document.getElementById('mat');
var phy=document.getElementById('phy');
var chem=document.getElementById('chem');
var em=document.getElementById('em');
var bee=document.getElementById('bee');
var wp=document.getElementById('wp');
var beel=document.getElementById('beel');


var gp1=grade(eng.value);
var gp2=grade(mat.value);
var gp3=grade(phy.value);
var gp4=grade(chem.value);
var gp5=grade(em.value);
var gp6=grade(bee.value);
var gp7=grade(wp.value);
var gp8=grade(beel.value);

var cgpa=(2*(gp8+gp1)+3*(gp3+gp4+gp5+gp6)+(gp7)+(4*gp2))/21;
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
