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
var ecd=document.getElementById('ecd');
var mi=document.getElementById('mi');
var phyl=document.getElementById('phyl');
var ecdl=document.getElementById('ecdl');


var gp1=grade(eng.value);
var gp2=grade(mat.value);
var gp3=grade(phy.value);
var gp4=grade(ecd.value);
var gp5=grade(mi.value);
var gp6=grade(phyl.value);
var gp7=grade(ecdl.value);

var cgpa=((gp1*2)+4*(gp2+gp3+gp4)+1.5*(gp6+gp7)+(gp5*3))/20;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7);
console.log(cgpa);
 document.getElementById("result").innerHTML = "GPA : "+cgpa.toFixed(2);


}

function bigImg(x) {
  x.style.fontSize = "23px";
}

function normalImg(x) {
  x.style.fontSize = "20px";
}
