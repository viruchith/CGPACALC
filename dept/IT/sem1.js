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
var pyp=document.getElementById('pyp');
var beee=document.getElementById('beee');
var pcl=document.getElementById('pcl');
var beeel=document.getElementById('beeel');
var pypl=document.getElementById('pypl');


console.log("Success");
var gp1=grade(eng.value);
var gp2=grade(mat.value);
var gp3=grade(phy.value);
var gp4=grade(pyp.value);
var gp5=grade(beee.value);
var gp6=grade(pcl.value);
var gp7=grade(beeel.value);
var gp8=grade(pypl.value);
var cgpa=(3*(gp3+gp4+gp5)+2*gp1+((gp6*1.5)+gp7+gp8)+4*gp2)/18.5;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7,gp8);
console.log(cgpa);
 document.getElementById("result").innerHTML = "CGPA: "+cgpa.toFixed(2);


}
