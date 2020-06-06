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
var phy=document.getElementById('phy');
var chem=document.getElementById('chem');
var bme=document.getElementById('bme');
var wfms=document.getElementById('wfms');
var eg=document.getElementById('eg');
var eng=document.getElementById('eng');
var wfmsl=document.getElementById('wfmsl');


var gp1=grade(mat.value);
var gp2=grade(phy.value);
var gp3=grade(chem.value);
var gp4=grade(bme.value);
var gp5=grade(wfms.value);
var gp6=grade(eg.value);
var gp7=grade(eng.value);
var gp8=grade(wfmsl.value);

var cgpa=((gp1*4)+3*(gp2+gp3+gp4+gp5)+(gp7+gp8)+(gp6*2))/20;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7,gp8);
console.log(cgpa);
 document.getElementById("result").innerHTML = "GPA: "+cgpa.toFixed(2);


}

function bigImg(x) {
  x.style.fontSize = "23px";
}

function normalImg(x) {
  x.style.fontSize = "20px";
}
