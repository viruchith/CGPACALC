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
var chem=document.getElementById('chem');
var pyp=document.getElementById('pyp');
var eg=document.getElementById('eg');
var pypl=document.getElementById('pypl');
var cheml=document.getElementById('cheml');
var wpl=document.getElementById('wpl');


console.log("Success");
var gp1=grade(eng.value);
var gp2=grade(mat.value);
var gp3=grade(chem.value);
var gp4=grade(pyp.value);
var gp5=grade(eg.value);
var gp6=grade(pypl.value);
var gp7=grade(cheml.value);
var gp8=grade(wpl.value);

var cgpa=((gp1*2)+3*(gp3+gp4+gp5)+(gp6+gp8)+(gp2*4)+(gp7*1.5))/18.5;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7,gp8);
console.log(cgpa);
 document.getElementById("result").innerHTML = "CGPA: "+cgpa.toFixed(2);


}

function bigImg(x) {
  x.style.fontSize = "23px";
}

function normalImg(x) {
  x.style.fontSize = "20px";
}
