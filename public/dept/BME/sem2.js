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
    var chem = document.getElementById('chem');
    var eg = document.getElementById('eg');
    var bio = document.getElementById('bio');
    var ct = document.getElementById('ct');
    var wpl = document.getElementById('wpl');
    var pcl = document.getElementById('pcl');

    var gp1 = grade(eng.value);
    var gp2 = grade(mat.value);
    var gp3 = grade(chem.value);
    var gp4 = grade(eg.value);
    var gp5 = grade(bio.value);
    var gp6 = grade(ct.value);
    var gp7 = grade(wpl.value);
    var gp8 = grade(pcl.value);
    
    var gpa = (((gp1+gp3+gp8)*2)+((gp4+gp5+gp6)*3)+(gp2*4)+(gp7*1))/20
    document.getElementById("result").innerHTML = "GPA : " + gpa.toFixed(2);


}


function bigImg(x) {
    x.style.fontSize = "23px";
}

function normalImg(x) {
    x.style.fontSize = "20px";
}
