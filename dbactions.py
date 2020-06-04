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
    cursor.execute("""SELECT admission_no,email_id,student_name,mobile_no FROM student_primary_credentials WHERE admission_no = %s """, (admnno,))
    result=cursor.fetchone()
    details["admission_no"]=result[0]
    details["email_id"]=result[1]
    details["student_name"]=result[2]
    details["mobile_no"] = result[3]
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

