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
var phy=document.getElementById('phy');
var mat=document.getElementById('mat');
var pyp=document.getElementById('pyp');
var mp=document.getElementById('mp');
var eng=document.getElementById('eng');
var phyl=document.getElementById('phyl');
var pypl=document.getElementById('pypl');



console.log("Success");
var gp1=grade(phy.value);
var gp2=grade(mat.value);
var gp3=grade(pyp.value);
var gp4=grade(mp.value);
var gp5=grade(eng.value);
var gp6=grade(phyl.value);
var gp7=grade(pypl.value);

var cgpa=(3*(gp3+gp5)+(gp7)+(4*(gp1+gp2+gp4))+(gp6*1.5))/20.5;
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
