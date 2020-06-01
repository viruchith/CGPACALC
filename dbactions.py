import psycopg2
from AppCredentials import Credentials as creds


connection = psycopg2.connect(user=creds.DB_USERNAME,
                            password=creds.DB_PASSWORD,
                            host="localhost",
                            port="5432",
                            database=creds.DB_NAME)
cursor = connection.cursor()

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








        




