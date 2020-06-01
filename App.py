from flask import Flask,render_template,request,flash,session,redirect,url_for
from flask_mail import Mail,Message
#from xlrw import Xlrw
from uservalidations import UserValidations
from dbactions import fetchStudentDashboard,userExists,fetchUserByEmail,insertStudentPersonalInfo,updateStudentPersonalInfo



app = Flask(__name__, template_folder="/Users/ganesankoundappan/Projects/CSEwebApp/templates")
app.config["UPLOAD_FOLDER"] = "/Users/ganesankoundappan/Projects/CSEwebApp"

app.secret_key = '53a9396ce993a69d973fe88b1c0a4208183a9835f3054bf5424c4f0b43e0f466'

uv=UserValidations()
#batch creation
'''@app.route("/",methods=['GET','POST'])
def upload():
    return render_template("fileform.html")'''

from AppCredentials import Credentials as creds
app.config.update(
    DEBUG=True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=creds.MAIL_ID,
    MAIL_PASSWORD=creds.MAIL_PASSWORD
)

fmail=Mail(app)

def sendResetMail(mail,token):
    msg=Message("Forgot Password Request ! ",
    sender="sonacse2019to2023@gmail.com",
    recipients=[mail])
    msg.body=f'''To reset your password for Sona CSE SIMS, please visit the following link :
    http://127.0.0.1:5000{url_for('forgotPasswordReset',token=token)}

    If you did not initiate this request please ignore it.
    '''
    fmail.send(msg)

@app.route("/student",methods=['GET','POST'])
def studentLogin():
    if request.method=="POST":
        auth=uv.studentAuthenticate(request.form["email"],request.form["password"])
        if isinstance(auth,dict):
            session["studentuser"]={"admission_no":auth["admission_no"],"email_id":auth["email_id"]}
            return redirect(url_for("studentDashboard",username=auth["admission_no"]))
        else:
            flash(auth,"danger")
            return render_template("studentlogin.html")
    
    return render_template("studentlogin.html")


@app.route("/logout")
def logout():
    if "studentuser" in session:
        session.pop("studentuser",None)
        return redirect(url_for("studentLogin"))
    else:
        return redirect(url_for("studentLogin"))


@app.route("/<username>/dashboard")
def studentDashboard(username):
    if "studentuser" in session:
        if username==session["studentuser"]["admission_no"]:
            details=fetchStudentDashboard(session["studentuser"]["admission_no"])
            return render_template("studentdashboard.html",name=details["student_name"],admnno=details["admission_no"],mail=details["email_id"],mob=details["mobile_no"])
        else:
            return "<h1>404 Page Not Found</h1>"
    else :
        return redirect(url_for("studentLogin"))


@app.route("/<username>/personal_info")
def personalInfoDisplay(username):
    details=uv.studentPersonalInfoExist(username)
    if "studentuser" in session and username==session["studentuser"]["admission_no"] and isinstance(details,dict) :
        session["personal_info"]=details
        return render_template("student_personal_info_display.html",username=username,personal=details)
    elif "studentuser" in session and username == session["studentuser"]["admission_no"] and not details:
        session["personal_info"] = {"admission_no": "", "first_name": "", "last_name": "", "DOB": "", "height": "", "weight": "", "blood_group": "", "identification_marks": "", "communication_address": "", "permanent_address": "","district": "", "state": "", "country": "", "pincode": "", "father_contact_number": "", "mother_contact_number": "", "student_mobile_number": "", "languages": "", "edit_permission": True}
        return redirect(url_for("personalInfoEdit",username=username))
    else:
        return "<h1>The page you're looking for was not found </h1>"


@app.route("/<username>/personal_info/edit",methods={'GET','POST'})
def personalInfoEdit(username):
    details = session["personal_info"]
    if "studentuser" in session and username == session["studentuser"]["admission_no"] and details["edit_permission"]==True and details["admission_no"]=="":
        if request.method=="POST" :
            try:
                insertStudentPersonalInfo({"admission_no": username, "first_name": request.form["first_name"], "last_name": request.form["last_name"], "DOB":request.form["dob"],"height":request.form["height"],"weight":request.form["weight"], "blood_group": request.form["blood_group"], "identification_marks": request.form["identification_marks"], "communication_address": request.form["communication_address"], "permanent_address": request.form["permanent_address"], "district": request.form["district"], "state": request.form["state"], "country": request.form["country"],"pincode":request.form["pincode"], "state": request.form["state"], "father_contact_number": request.form["fathermob"], "mother_contact_number": request.form["mothermob"], "student_mobile_number": request.form["studentmob"],"languages":request.form["languages"]})
                flash("Details Submitted Successfully","success")
                return redirect(url_for("studentDashboard",username=username))
            except:
                flash("Submission Error !","danger")
        return render_template("student_personal_info_edit.html",personal=details)
    elif "studentuser" in session and username == session["studentuser"]["admission_no"] and details["edit_permission"] == True and details["admission_no"] != "":
        if request.method=='POST' :
            try:
                updateStudentPersonalInfo({"admission_no": username, "first_name": request.form["first_name"], "last_name": request.form["last_name"], "DOB":request.form["dob"],"height":request.form["height"],"weight":request.form["weight"], "blood_group": request.form["blood_group"], "identification_marks": request.form["identification_marks"], "communication_address": request.form["communication_address"], "permanent_address": request.form["permanent_address"], "district": request.form["district"], "state": request.form["state"], "country": request.form["country"],"pincode":request.form["pincode"], "state": request.form["state"], "father_contact_number": request.form["fathermob"], "mother_contact_number": request.form["mothermob"], "student_mobile_number": request.form["studentmob"],"languages":request.form["languages"]})
                flash("Details updated successfullly !","success")
                return redirect(url_for("studentDashboard",username=username))            
            except:
                flash("Submission Error !","danger")
        return render_template("student_personal_info_edit.html",personal=details)
        return render_template("student_personal_info_edit.html",personal=details)
    elif "studentuser" not in session:
        return redirect(url_for("studentLogin"))
    else:
        return "<h1>The page was not found</h1>"
    

@app.route("/<username>/ResetPassword",methods=['GET','POST'])
def passwordReset(username):
    if "studentuser" in session and request.method=="POST" and username==session["studentuser"]["admission_no"]:
        
        if request.form["newpassword"]==request.form["retypenewpassword"]:
            auth=uv.studentAuthenticate(session["studentuser"]["email_id"],request.form["oldpassword"])
            
            if isinstance(auth,dict):
                msg,cat=uv.studentPasswordReset(session["studentuser"]["admission_no"],request.form["newpassword"])
                flash(msg,cat)
                return redirect(url_for("studentDashboard",username=session["studentuser"]["admission_no"]))
            
            else:
                flash(auth,"danger")
                return render_template("studentpasswordreset.html")
       
        else:
            flash("Passwords don't Match !", "danger")
            return render_template("studentpasswordreset.html")

    elif "studentuser" in session and username==session["studentuser"]["admission_no"]:
        return render_template("studentpasswordreset.html")
    else:
        return redirect(url_for("studentLogin"))

@app.route("/ForgotPassword",methods=['GET','POST'])
def forgotPasswordRequest():
    if "studentuser" in session:
        return redirect(url_for("studentDashboard",username=session["studentuser"]["admission_no"]))
    if "studentuser" not in session and request.method=="POST":
            details=fetchUserByEmail(request.form["email"])
            if isinstance(details,dict):
                token=uv.studentGetResetToken(app.secret_key,details["admission_no"])
                sendResetMail(request.form["email"],token=token)
                flash('An email has been sent with instructions to reset your password.', 'info')
            else:
                flash("Email Does not exist","danger")
    return render_template("studentforgotpasswordrequest.html") 

@app.route("/ResetPassword/<token>",methods=['GET','POST'])
def forgotPasswordReset(token):
    if "studentuser" not in session and request.method=='POST':
        admission_no=uv.studentVerifyResetToken(app.secret_key,token)
        newpassword=request.form["newpassword"]
        retyped=request.form["retypenewpassword"]

        if retyped==newpassword:
            msg,cat=uv.studentPasswordReset(admission_no,newpassword)
            flash(msg,cat)
            return redirect(url_for('studentLogin'))
        else:
            flash("Passwords Don't Match!","danger")

    elif "studentuser" not in session:
        admission_no = uv.studentVerifyResetToken(app.secret_key, token)
        if admission_no!=None:
            return render_template("studentforgotpasswordreset.html")
        else:
            return "<h1>The Token is either Invalid or Expired !</h1>"

    if "studentuser" in session :
        return redirect(url_for("studentDashboard",username=session["studentuser"]["admission_no"]))
    return "<h1>The Token is either Invalid or Expired !</h1>"

#batch creation
'''@app.route("/process",methods=['GET','POST'])
def batchCreation():
    if request.method == "POST":
        f=request.files["xlfile"]
        f.save(f.filename)
        #obj=Xlrw(f.filename)
        #obj.passWrite(obj.passGen(obj.read()))
        return "<h1>Success</h1>"'''


if __name__ == "__main__":
    app.run(debug=True)
