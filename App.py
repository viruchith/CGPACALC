from flask import Flask,render_template,request,flash,session,redirect,url_for
from flask_mail import Mail,Message
#from xlrw import Xlrw
from uservalidations import UserValidations
from dbactions import fetchStudentDashboard,userExists,fetchUserByEmail,insertStudentPersonalInfo,updateStudentPersonalInfo,insertStudentAcademicInfo,updateStudentAcademicInfo,updateImportantDocuments,getStudentDocuments,fetchStudentTalents,deleteStudentTalent,insertStudentTalent,fetchStudentAchievements,deleteStudentTalent,insertStudentAchievement,deleteStudentAchievement,insertStudentExtraCourse,fetchStudentExtraCourses,deleteStudentExtraCourse,insertStudentActivitiy,fetchStudentActivities,deleteStudentExtraActivity,fetchStudentFamily,updateFamily,fetchStudentSiblings,deleteSibling,addSiblings,fetchClubActivities,addClubActivity,deleteClubActivity,fetchAllStudents
import os

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
                sender="SONA CSE APP",
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
            return render_template("studentdashboard.html",name=details["student_name"],admnno=details["admission_no"],mail=details["email_id"],mob=details["mobile_no"],pic=details["profile_pic"])
        else:
            return "<h1>404 Page Not Found</h1>"
    else :
        return redirect(url_for("studentLogin"))


@app.route("/<username>/personal-info")
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


@app.route("/<username>/personal-info/edit",methods={'GET','POST'})
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
    elif "studentuser" not in session:
        return redirect(url_for("studentLogin"))
    else:
        return "<h1>The page was not found</h1>"

@app.route("/<username>/academic-info")
def academicInfoDisplay(username):
    details=uv.studentAcademicInfoExist(username)
    if "studentuser" in session and username==session["studentuser"]["admission_no"] and isinstance(details,dict):
        session["academic_info"]=details
        return render_template("student_academic_info_display.html",username=username,academic=details)
   
    elif "studentuser" in session and username == session["studentuser"]["admission_no"] and not details:
        session["academic_info"] = {"admission_no": "", "reg_no": "", "school_name": "", "school_place": "", "school_board": "", "school_medium": "", "school_group": "", "tenth_marks": "", "twelveth_marks": "","semester_1_gpa": 0.0, "semester_2_gpa": 0.0, "semester_3_gpa": 0.0, "semester_4_gpa": 0.0, "semester_5_gpa": 0.0, "semester_6_gpa": 0.0, "semester_7_gpa": 0.0, "semester_8_gpa": 0.0, "edit_permission": True}
        return redirect(url_for("academicInfoEdit",username=username))
    else:
        return "<h1>The page your'e looking for was not found ! </h1>"

@app.route("/<username>/academic-info/edit",methods=['GET','POST'])
def academicInfoEdit(username):
    details=session["academic_info"]
    if "studentuser" in session and username == session["studentuser"]["admission_no"] and details["edit_permission"]==True and details["admission_no"]=="":
        if request.method=="POST" :
            try:
                insertStudentAcademicInfo({"admission_no": username, "reg_no": request.form["reg_no"], "school_name": request.form["school_name"], "school_place": request.form["school_place"], "school_board": request.form["school_board"], "school_medium": request.form["school_medium"], "school_group": request.form["school_group"], "tenth_marks": request.form["tenth_marks"], "twelveth_marks": request.form["twelveth_marks"], "religion": request.form["religion"], "caste": request.form[
                                          "caste"], "community": request.form["community"], "semester_1_gpa": request.form["semester_1_gpa"], "semester_2_gpa": request.form["semester_2_gpa"], "semester_3_gpa": request.form["semester_3_gpa"], "semester_4_gpa": request.form["semester_4_gpa"], "semester_5_gpa": request.form["semester_5_gpa"], "semester_6_gpa": request.form["semester_6_gpa"], "semester_7_gpa": request.form["semester_7_gpa"], "semester_8_gpa": request.form["semester_8_gpa"]})
                flash("Details Submitted Successfully","success")
                return redirect(url_for("studentDashboard",username=username))
            except Exception as e:
                flash("Submission Error !","danger")
        return render_template("student_academic_info_edit.html",academic=details)
    elif "studentuser" in session and username == session["studentuser"]["admission_no"] and details["edit_permission"] == True and details["admission_no"] != "":
        if request.method=='POST' :
            try:
                updateStudentAcademicInfo({"admission_no": username, "reg_no": request.form["reg_no"], "school_name": request.form["school_name"], "school_place": request.form["school_place"], "school_board": request.form["school_board"], "school_medium": request.form["school_medium"], "school_group": request.form["school_group"], "tenth_marks": request.form["tenth_marks"], "twelveth_marks": request.form["twelveth_marks"],"religion":request.form["religion"],"caste":request.form["caste"],"community":request.form["community"], "semester_1_gpa": request.form["semester_1_gpa"], "semester_2_gpa": request.form["semester_2_gpa"], "semester_3_gpa": request.form["semester_3_gpa"], "semester_4_gpa": request.form["semester_4_gpa"], "semester_5_gpa": request.form["semester_5_gpa"], "semester_6_gpa": request.form["semester_6_gpa"], "semester_7_gpa": request.form["semester_7_gpa"], "semester_8_gpa": request.form["semester_8_gpa"]})
                flash("Details updated successfullly !","success")
                return redirect(url_for("studentDashboard",username=username))            
            except Exception as e:
                flash("Submission Error !","danger")
        return render_template("student_academic_info_edit.html",academic=details)
    elif "studentuser" not in session:
        return redirect(url_for("studentLogin"))
    else:
        return "<h1>The page was not found</h1>"

@app.route("/<username>/documents")
def documentsDisplay(username):
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        return render_template("student_document_display.html",username=username,doc=getStudentDocuments(admnno=username))
    else:
        return "<h1>Access Denied</h1>"

@app.route("/<username>/upload/<filetype>",methods=['GET','POST'])
def docSave(username,filetype):
    fileTypeList = ["10th-mark-list", "12th-mark-list", "birth-certificate","community-certificate", "passport-size-photo", "signature"]
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        if request.method=='POST':
            if filetype in fileTypeList:
                f=request.files["stuDoc"]
                _,ext=os.path.splitext(f.filename)
                docname=username+'-'+filetype+ext
                pic_path=os.path.join(app.root_path,f'static/{filetype}',docname)
                f.save(pic_path)
                updateImportantDocuments(username,filetype,docname)
                return redirect(url_for("documentsDisplay",username=username))
        return render_template("student_document_upload.html")
    else:
        return "<h1>Unauthorised Access</h1>"


@app.route("/<username>/extra-curricular",methods=['GET','POST'])
def studentExtraCurricular(username):
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        talents=fetchStudentTalents(admnno=username)
        achievements=fetchStudentAchievements(admnno=username)
        clubs=fetchClubActivities(admnno=username)
        if request.method=='POST' and "add-talent" in request.form:
            try:
                insertStudentTalent(talent_id=uv.generateId(username),admnno=username,title=request.form["talent-title"],description=request.form["talent-description"])
                return redirect(url_for("studentExtraCurricular",username=username))
            except:
                return "<h1>Submission Error</h1>"

        if request.method=='POST' and "add-achievement" in request.form:
            try:
                insertStudentAchievement(achievement_id=uv.generateId(username),admnno=username,title=request.form["achievement-title"],description=request.form["achievement-description"])
                return redirect(url_for("studentExtraCurricular",username=username))
            except:
                return "<h1>Submission Error</h1>"
        
        if request.method=='POST' and "add-club" in request.form : 
            try:
                addClubActivity(id=uv.generateId(username),admnno=username,cname=request.form["club-name"],cposition=request.form["club-position"],organisedorparticipated=request.form["club-part-org"],description=request.form["club-description"])
                return redirect(url_for("studentExtraCurricular",username=username))
            except Exception as e:
                return f"<h1>Submission Error : {e}</h1>"
        return render_template("student_extra_curricular.html",username=username,talentlist=talents,achievementlist=achievements,clubs=clubs)
    else:
        return "<h1>Unauthorised Access</h1>"



@app.route("/<username>/<category>/extra-curricular/<catid>/delete")
def deleteTalent(username,category,catid):
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        if category=="talent":
            try:
                deleteStudentTalent(talentid=catid,admnno=username)
            except:
                return "<h1>Invalid Request</h1>"
            return redirect(url_for("studentExtraCurricular",username=username))
        elif category=="achievement":
            try:
                deleteStudentAchievement(admnno=username,achievementid=catid)
            except:
                return "<h1>Invalid Request</h1>"
            return redirect(url_for("studentExtraCurricular",username=username))

        elif category=="club":
            try:
                deleteClubActivity(admnno=username,id=catid)
            except:
                return "<h1>Invalid Request</h1>"
            return redirect(url_for("studentExtraCurricular",username=username))

    else:
        return "<h1>Unauthorised Access</h1>"

@app.route("/<username>/certifications-and-events",methods=['GET','POST'])
def certificationsAndEvents(username):
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        courses=fetchStudentExtraCourses(admnno=username)
        activities=fetchStudentActivities(admnno=username)

        if request.method=='POST' and "add-course" in request.form:
                try:
                    insertStudentExtraCourse(courseid=uv.generateId(username),admnno=username,title=request.form["course-title"],link=request.form["course-link"],semester=request.form["course-semester"],description=request.form["course-description"])
                    return redirect(url_for("certificationsAndEvents",username=username))
                except:
                    return "<h1>Submission Error</h1>"

        if request.method=='POST' and "add-activity" in request.form:
                try:
                    insertStudentActivitiy(actid=uv.generateId(username), admnno=username,certtype=request.form["activity-certtype"], title=request.form["activity-title"], link=request.form["activity-link"], semester=request.form["activity-semester"], description=request.form["activity-description"])
                    return redirect(url_for("certificationsAndEvents",username=username))
                except:
                    return "<h1>Submission Error</h1>"

        return render_template("student_courses_and_activities.html",username=username,courselist=courses,activitylist=activities)

    else:
        return "<h1>Unauthorised Access</h1>"

@app.route("/<username>/certifications-and-events/<category>/delete/<id>")
def deleteCertificationAndEvent(username,category,id):
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        if category=="course":
            try:
                deleteStudentExtraCourse(admnno=username,courseid=id)
            except:
                return "<h1>Invalid Request</h1>"
            return redirect(url_for("certificationsAndEvents",username=username))
        elif category=="activity":
            try:
                deleteStudentExtraActivity(admnno=username,actid=id)
            except:
                return "<h1>Invalid Request</h1>"
            return redirect(url_for("certificationsAndEvents",username=username))

    else:
        return "<h1>Access Denied</h1>"

@app.route("/<username>/Family")
def studentFamilyDisplay(username):
    family=fetchStudentFamily(admnno=username)
    siblings=fetchStudentSiblings(admnno=username)
    if "studentuser" in session and username==session["studentuser"]["admission_no"] and family[1]!=None:
        return render_template("student_family_display.html",username=username,details=family,siblings=siblings)
    elif "studentuser" in session and username==session["studentuser"]["admission_no"] and family[1]==None:
        return redirect(url_for("studentFamilyEdit",username=username))
    else:
        return "<h1>Access Denied</h1>"


@app.route("/<username>/Family/edit", methods=['GET', 'POST'])
def studentFamilyEdit(username):
    details=fetchStudentFamily(admnno=username)
    siblings=fetchStudentSiblings(admnno=username)
    if "studentuser" in session and username==session["studentuser"]["admission_no"]:
        if "family-edit" in request.form and request.method =='POST':
            try:
                updateFamily(admnno=username, nomem=request.form["family-mem"], father_fname=request.form["father-fname"], father_lname=request.form["father-lname"], father_occupation=request.form["father-occupation"], father_dob=request.form["father-dob"],
                         mother_fname=request.form["mother-fname"], mother_lname=request.form["mother-lname"], mother_occupation=request.form["mother-occupation"], mother_dob=request.form["mother-dob"], have_sibling=request.form["have-sibling"], noofsiblings=request.form["no-of-siblings"])
            except:
                return "<h1>Submission Error !</h1>"
        if "add-sibling" in request.form and request.method == 'POST' :
            addSiblings(siblingid=uv.generateId(username),admnno=username,relation=request.form["sibling-relation"],name=request.form["sibling-name"],status=request.form["sibling-status"],age=request.form["sibling-age"],sona_associated=request.form["sibling-sona"],description=request.form["sibling-description"])
            return redirect(url_for("studentFamilyDisplay",username=username))
        return(render_template("student_family_edit.html",username=username,family=details,siblings=siblings))
    else:
        return "<h1>Access Denied</h1>"

@app.route("/<username>/family/sibling/<id>/delete")
def siblingDelete(username,id):
    if "studentuser" in session and username == session["studentuser"]["admission_no"]:
        try:
            deleteSibling(id=id,admnno=username)
        except:
            pass
        return redirect(url_for("studentFamilyEdit",username=username))
    else:
        return "<h1>Invalid request ! </h1>"

@app.route("/faculty",methods=['GET','POST'])
def facultylogin():
    if request.method=="POST" : 
        authenticate=uv.authenticateFaculty(username=request.form["username"],password=request.form["password"])
        if authenticate==True:
            session["facultylogin"]= True
            return "<h1>Success</h1>"
        else:
            flash(authenticate,"danger")
    return render_template("facultyLogin.html")


@app.route("/display/student/all")
def ddisplayAllStudents():
    return render_template("displayAll_students.html",students=fetchAllStudents())


@app.route("/display/student/<admnno>")
def displayStudent(admnno):
    return f"<h1>{admnno}"

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
