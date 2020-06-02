function grade(g) {
    if (g === "O") {
        return 10;
    } else if (g === "A+") {
        return 9;
    } else if (g === "A") {
        return 8;
    } else if (g === "B+") {
        return 7;
    } else if (g === "B") {
        return 6;
    } else if (g === "U") {
        return 0;
    }
}

function validate() {
    var eng = document.getElementById('eng');
    var mat = document.getElementById('mat');
    var pyp = document.getElementById('pyp');
    var beee = document.getElementById('beee');
    var bem = document.getElementById('bem');
    var beeel = document.getElementById('beeel');
    var pcl = document.getElementById('pcl');
    var pypl = document.getElementById('pypl');



    console.log("Success");
    var gp1 = grade(eng.value);
    var gp2 = grade(mat.value);
    var gp3 = grade(pyp.value);
    var gp4 = grade(beee.value);
    var gp5 = grade(bem.value);
    var gp6 = grade(beeel.value);
    var gp7 = grade(pcl.value);
    var gp8 = grade(pypl.value);
    var cgpa = (4 * (gp2+gp5) + 3 * (gp1 +gp3+ gp4) + (1.5 * gp7) + gp6 + gp8) / 20.5;
    console.log(gp1, gp2, gp3, gp4, gp5, gp6, gp7);
    console.log(cgpa);
    document.getElementById("result").innerHTML = "GPA: " + cgpa.toFixed(2);


}

function bigImg(x) {
    x.style.fontSize = "23px";
}

function normalImg(x) {
    x.style.fontSize = "20px";
}
