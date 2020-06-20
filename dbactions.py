import psycopg2
from AppCredentials import Credentials as creds


connection = psycopg2.connect(user=creds.DB_USERNAME,
                            password=creds.DB_PASSWORD,
                            host="localhost",
                            port="5432",
                            database=creds.DB_NAME)
cursor = connection.cursor()

def dictFilter(details):
    for i in details.keys():
        if details[i]==None:
            details[i]=0.0
    return details

def fetchStudentPasswdHash(email):
    cursor.execute("""SELECT * FROM student_primary_credentials WHERE email_id = %s """,(email,))
    credentials=cursor.fetchone()
    try:
        admission_no=credentials[0]
        passwd_hash=credentials[2]
        return {"admission_no":admission_no,"passwd_hash":passwd_hash}

    except TypeError:

        return False

def fetchStudentDashboard(admnno):
    details={}
    cursor.execute("""SELECT admission_no,email_id,student_name,mobile_no,profile_pic FROM student_primary_credentials WHERE admission_no = %s """, (admnno,))
    result=cursor.fetchone()
    details["admission_no"]=result[0]
    details["email_id"]=result[1]
    details["student_name"]=result[2]
    details["mobile_no"] = result[3]
    details["profile_pic"]= result[4]
    return details

def changeStudentPassword(admnno,new_hash):
    cursor.execute("""UPDATE student_primary_credentials SET password=%s WHERE admission_no = %s""",(new_hash,admnno))
    connection.commit()
    return True

def fetchUserByEmail(mail):
    details={}
    cursor.execute("""SELECT admission_no,email_id FROM student_primary_credentials WHERE email_id = %s """, (mail,))
    credentials=cursor.fetchone()
    try:
        details["admission_no"]=credentials[0]
        details["email_id"]=credentials[1]
        return details
    except:
        return False



def userExists(admnno):
    details={}
    cursor.execute("""SELECT admission_no,email_id FROM student_primary_credentials WHERE admission_no = %s """, (admnno,))
    result=cursor.fetchone()
    try:
        admission_no=result[0]
        return admission_no
    except:
        return False

def fetchStudentPersonalInfo(admnno):
    details={}
    cursor.execute("""SELECT * FROM student_personal_info WHERE admission_no = %s """, (admnno,))
    result=cursor.fetchone()
    if result!=None:
        details["admission_no"]=result[0]
        details["first_name"]=result[1]
        details["last_name"]=result[2]
        details["DOB"]=result[3]
        details["height"]=result[4]
        details["weight"]=result[5]
        details["blood_group"]=result[6]
        details["identification_marks"]=result[7]
        details["permanent_address"]=result[8]
        details["communication_address"]=result[9]
        details["district"]=result[10]
        details["state"]=result[11]
        details["country"]=result[12]
        details["pincode"]=result[13]
        details["father_contact_number"]=result[14]
        details["mother_contact_number"]=result[15]
        details["student_mobile_number"]=result[16]
        details["languages"]=result[17]
        details["edit_permission"]=result[18]
        return details
    else:
        return False

def updateStudentPersonalInfo(details):
    cursor.execute("""UPDATE 
    student_personal_info
    SET  
    first_name=%s,
    last_name=%s,
    dob=%s,
    height=%s,
    weight=%s,
    blood_group=%s,
    identification_marks=%s,
    communication_address=%s,
    permanent_address=%s,
    district=%s,
    state=%s,
    country=%s,
    pincode=%s,
    father_contact_number=%s,
    mother_contact_number=%s,
    student_mobile_number=%s,
    languages=%s

     WHERE admission_no=%s;    
    """, (details["first_name"], details["last_name"], details["DOB"], details["height"], details["weight"], details["blood_group"], details["identification_marks"], details["communication_address"], details["permanent_address"], details["district"], details["state"],details["country"],details["pincode"],details["father_contact_number"],details["mother_contact_number"],details["student_mobile_number"],details["languages"],details["admission_no"]))
    connection.commit()

def insertStudentPersonalInfo(details):
    cursor.execute("""INSERT INTO 
    student_personal_info  
     (admission_no,
    first_name,
    last_name,
    dob,
    height,
    weight,
    blood_group,
    identification_marks,
    communication_address,
    permanent_address,
    district,
    state,
    country,
    pincode,
    father_contact_number,
    mother_contact_number,
    student_mobile_number,
    languages)
     VALUES
      (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    
    """, (details["admission_no"], details["first_name"], details["last_name"], details["DOB"], details["height"], details["weight"], details["blood_group"], details["identification_marks"], details["communication_address"], details["permanent_address"], details["district"], details["state"],details["country"],details["pincode"],details["father_contact_number"],details["mother_contact_number"],details["student_mobile_number"],details["languages"]))
    connection.commit()

def fetchStudentAcademicInfo(admnno):
    details={}
    cursor.execute("""SELECT * FROM student_academic_info WHERE admission_no = %s """, (admnno,))
    result=cursor.fetchone()
    if result!=None:
        details["admission_no"]=result[0]
        details["reg_no"]=result[1]
        details["school_name"]=result[2]
        details["school_place"]=result[3]
        details["school_board"]=result[4]
        details["school_medium"]=result[5]
        details["school_group"]=result[6]
        details["tenth_marks"]=result[7]
        details["twelveth_marks"]=result[8]
        details["religion"]=result[9]
        details["caste"] = result[10]
        details["community"]=result[11]
        details["semester_1_gpa"]=result[12]
        details["semester_2_gpa"]=result[13]
        details["semester_3_gpa"]=result[14]
        details["semester_4_gpa"]=result[15]
        details["semester_5_gpa"]=result[16]
        details["semester_6_gpa"]=result[17]
        details["semester_7_gpa"]=result[18]
        details["semester_8_gpa"] = result[19]
        details["edit_permission"]=result[20]
        dictFilter(details)
        return details
    else:
        return False

def insertStudentAcademicInfo(details):
    details=dictFilter(details=details)
    cursor.execute("""INSERT INTO 
        student_academic_info  
        (admission_no,
        reg_no,
        school_name,
        school_place,
        school_board,
        school_medium,
        school_group,
        tenth_std_marks,
        twelveth_std_marks,
        religion,
        caste,
        community,
        semester_1_gpa,
        semester_2_gpa,
        semester_3_gpa,
        semester_4_gpa,
        semester_5_gpa,
        semester_6_gpa,
        semester_7_gpa,
        semester_8_gpa
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        
        """, (details["admission_no"], details["reg_no"], details["school_name"], details["school_place"], details["school_board"], details["school_medium"], details["school_group"], details["tenth_marks"], details["twelveth_marks"], details["religion"], details["caste"], details["community"], details["semester_1_gpa"], details["semester_2_gpa"], details["semester_3_gpa"], details["semester_4_gpa"], details["semester_5_gpa"], details["semester_6_gpa"], details["semester_7_gpa"], details["semester_8_gpa"]))
    connection.commit()


def updateStudentAcademicInfo(details):
    details = dictFilter(details=details)
    cursor.execute("""UPDATE
        student_academic_info  
         SET
        reg_no=%s,
        school_name=%s,
        school_place=%s,
        school_board=%s,
        school_medium=%s,
        school_group=%s,
        tenth_std_marks=%s,
        twelveth_std_marks=%s,
        religion=%s,
        caste=%s,
        community=%s,
        semester_1_gpa=%s,
        semester_2_gpa=%s,
        semester_3_gpa=%s,
        semester_4_gpa=%s,
        semester_5_gpa=%s,
        semester_6_gpa=%s,
        semester_7_gpa=%s,
        semester_8_gpa=%s
        
        WHERE admission_no = %s ;
        
        """, (details["reg_no"], details["school_name"], details["school_place"], details["school_board"], details["school_medium"], details["school_group"], details["tenth_marks"], details["twelveth_marks"], details["religion"], details["caste"], details["community"], details["semester_1_gpa"], details["semester_2_gpa"], details["semester_3_gpa"], details["semester_4_gpa"], details["semester_5_gpa"], details["semester_6_gpa"], details["semester_7_gpa"], details["semester_8_gpa"],details["admission_no"]))
    connection.commit()

def updateImportantDocuments(admnno,doctype,filename):
    if doctype=="10th-mark-list":
      cursor.execute("""UPDATE student_documents SET tenth_marklist = %s WHERE admission_no = %s""",(filename,admnno))
    elif doctype=="12th-mark-list":
      cursor.execute("""UPDATE student_documents SET twelfth_marklist = %s WHERE admission_no = %s""",(filename,admnno))
    elif doctype=="birth-certificate":
      cursor.execute("""UPDATE student_documents SET birth_certificate = %s WHERE admission_no = %s""",(filename,admnno))
    elif doctype=="community-certificate":
      cursor.execute("""UPDATE student_documents SET community_certificate = %s WHERE admission_no = %s""",(filename,admnno))
    elif doctype=="passport-size-photo":
      cursor.execute("""UPDATE student_primary_credentials SET profile_pic = %s WHERE admission_no = %s""",(filename,admnno))
      cursor.execute("""UPDATE student_documents SET passport_size_photo = %s WHERE admission_no = %s""",(filename,admnno))
    elif doctype=="signature":
      cursor.execute("""UPDATE student_documents SET signature = %s WHERE admission_no = %s""", (filename, admnno))
    else:
        return False
    connection.commit()
    return True    

def getStudentDocuments(admnno):
    details={}
    cursor.execute("""SELECT tenth_marklist,twelfth_marklist,birth_certificate,community_certificate,passport_size_photo,signature FROM student_documents WHERE admission_no = %s """,(admnno,))
    result=cursor.fetchone()
    details["tenth-marklist"]=result[0]
    details["twelfth-marklist"]=result[1]
    details["birth-certificate"]=result[2]
    details["community-certificate"]=result[3]
    details["passport-size-photo"] = result[4]
    details["signature"]=result[5]
    return details

def insertStudentTalent(talent_id,admnno,title,description):
    cursor.execute("""INSERT INTO student_talents (talent_id,admission_no,title,description) VALUES (%s,%s,%s,%s)""",(talent_id,admnno,title,description))
    connection.commit()
    return True

def fetchStudentTalents(admnno):
    cursor.execute(""" SELECT talent_id,admission_no,title,description FROM student_talents WHERE admission_no = %s """,(admnno,))
    result=cursor.fetchall()
    return result

def deleteStudentTalent(admnno,talentid):
    cursor.execute(""" DELETE FROM student_talents WHERE talent_id = %s AND admission_no = %s """,(talentid,admnno))
    connection.commit()
    return True

def insertStudentAchievement(achievement_id,admnno,title,description):
    cursor.execute(""" INSERT INTO student_achievements (achievement_id,admission_no,title,description) VALUES (%s,%s,%s,%s) """,(achievement_id, admnno, title, description))
    connection.commit()
    return True

def fetchStudentAchievements(admnno):
    cursor.execute(""" SELECT achievement_id,admission_no,title,description FROM student_achievements WHERE admission_no = %s """,(admnno,))
    result=cursor.fetchall()
    return result

def deleteStudentAchievement(admnno,achievementid):
    cursor.execute(""" DELETE FROM student_achievements WHERE achievement_id = %s AND admission_no = %s """,(achievementid,admnno))
    connection.commit()
    return True

def insertStudentExtraCourse(courseid,admnno,title,link,semester,description):
    cursor.execute("""INSERT INTO student_extra_courses (course_id,admission_no,title,link,semester,description) VALUES (%s,%s,%s,%s,%s,%s)""",(courseid, admnno, title,link,semester, description))
    connection.commit()
    return True

def fetchStudentExtraCourses(admnno):
    cursor.execute(""" SELECT course_id,admission_no,title,link,semester,description FROM student_extra_courses WHERE admission_no = %s """,(admnno,))
    result=cursor.fetchall()
    return result

def deleteStudentExtraCourse(courseid,admnno):
    cursor.execute(""" DELETE FROM student_extra_courses WHERE course_id = %s  AND admission_no = %s""",(courseid,admnno))
    connection.commit()
    return True

def insertStudentActivitiy(actid,admnno,certtype,title,link,semester,description):
    cursor.execute("""INSERT INTO student_event_activities (certid,admission_no,cert_type,title,semester,link,description) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(actid, admnno,certtype, title,semester,link, description))
    connection.commit()
    return True

def fetchStudentActivities(admnno):
    cursor.execute(""" SELECT certid,admission_no,cert_type,title,link,semester,description FROM student_event_activities WHERE admission_no = %s """, (admnno,))
    result = cursor.fetchall()
    return result

def deleteStudentExtraActivity(admnno,actid):
    cursor.execute(""" DELETE FROM student_event_activities WHERE certid = %s AND admission_no = %s """,(actid,admnno))
    connection.commit()
    return True

def fetchStudentFamily(admnno):
    cursor.execute(""" SELECT * FROM student_family WHERE admission_no = %s """,(admnno,))
    result=cursor.fetchone()
    return result

def updateFamily(admnno,nomem,father_fname,father_lname,father_occupation,father_dob,mother_fname,mother_lname,mother_occupation,mother_dob,have_sibling,noofsiblings):
    cursor.execute(""" UPDATE student_family SET no_of_members=%s,father_fname=%s,father_lname=%s,father_occupation=%s,father_dob=%s,mother_fname=%s,mother_lname=%s,mother_occupation=%s,mother_dob=%s,has_siblings=%s,no_of_siblings=%s WHERE admission_no=%s""",(nomem,father_fname,father_lname,father_occupation,father_dob,mother_fname,mother_lname,mother_occupation,mother_dob,have_sibling,noofsiblings,admnno))
    connection.commit()
    return True

def fetchStudentSiblings(admnno):
    cursor.execute(""" SELECT * FROM student_siblings WHERE admission_no = %s ; """,(admnno,))
    result = cursor.fetchall()
    return result

def addSiblings(siblingid,admnno,relation,name,status,age,sona_associated,description):
    cursor.execute(""" INSERT INTO student_siblings (sibling_id,admission_no,relation,name,status,age,associated_with_sona,description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) """,(siblingid,admnno,relation,name,status,age,sona_associated,description))
    connection.commit()
    return True

def deleteSibling(id,admnno):
    cursor.execute(""" DELETE FROM student_siblings WHERE sibling_id = %s AND admission_no=%s """,(id,admnno))
    connection.commit()
    return True

def addClubActivity(id,admnno,cname,cposition,organisedorparticipated,description):
    cursor.execute(""" INSERT INTO student_clubs (id,admission_no,club_name,club_position,organised_participated,description) VALUES(%s,%s,%s,%s,%s,%s)  """,(id,admnno,cname,cposition,organisedorparticipated,description))
    connection.commit()
    return True

def fetchClubActivities(admnno):
    cursor.execute(""" SELECT * FROM student_clubs WHERE admission_no = %s """,(admnno,))
    result = cursor.fetchall()
    return result

def deleteClubActivity(admnno,id):
    cursor.execute(""" DELETE FROM student_clubs WHERE admission_no = %s AND id = %s """,(admnno,id))
    connection.commit()
    return True

def fetchFacultyCredentials(username):
    details={}
    cursor.execute("""SELECT username,password FROM faculty_credentials WHERE username = %s""",(username,))
    result=cursor.fetchone()
    if result!=None:
        details["username"]=result[0]
        details["password"]=result[1]
        return details  
    else:
      return False

def fetchAllStudents():
    cursor.execute(""" SELECT student_name,admission_no,mobile_no FROM student_primary_credentials """)
    result=cursor.fetchall()
    return result



