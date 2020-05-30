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

        




