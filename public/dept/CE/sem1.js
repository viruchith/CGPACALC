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
var eg=document.getElementById('eg');
var pcl=document.getElementById('pcl');
var wpl=document.getElementById('wpl');


console.log("Success");
var gp1=grade(eng.value);
var gp2=grade(mat.value);
var gp3=grade(phy.value);
var gp4=grade(chem.value);
var gp5=grade(eg.value);
var gp6=grade(pcl.value);
var gp7=grade(wpl.value);
var cgpa=(4*(gp2+gp3+gp4)+3*(gp1+gp5)+(1.5*gp6)+gp7)/20.5;
console.log(gp1,gp2,gp3,gp4,gp5,gp6,gp7);
console.log(cgpa);
 document.getElementById("result").innerHTML = "CGPA: "+cgpa.toFixed(2);


}
