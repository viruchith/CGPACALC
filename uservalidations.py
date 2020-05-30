from dbactions import fetchStudentPasswdHash,changeStudentPassword,fetchStudentDashboard,userExists
from flask_bcrypt import Bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



bcrypt=Bcrypt()

class UserValidations:

    def studentAuthenticate(self,email,password):
        if fetchStudentPasswdHash(email):
            fetched=fetchStudentPasswdHash(email)
            hashed_passwd=fetched["passwd_hash"]
            admission_no=fetched["admission_no"]
            if bcrypt.check_password_hash(hashed_passwd,password):
                return fetchStudentDashboard(fetched["admission_no"])
            else:
                return "Invalid Password"                
        else:
            return "Email Does not exist ! "
    

    def studentPasswordReset(self,admission_no,new_passwd):
        hashed = bcrypt.generate_password_hash(new_passwd).decode('utf-8')
        if changeStudentPassword(admission_no,hashed):
            return ["Password Changed Successfully","success"]


    @staticmethod
    def studentGetResetToken(secretkey,admission_no,expire_sec=600):
        s=Serializer(secretkey,expire_sec)
        return s.dumps({"admission_no":admission_no}).decode('utf-8')
    
    @staticmethod
    def studentVerifyResetToken(secretkey,token):
        s=Serializer(secretkey)
        try:
            token_value=s.loads(token)["admission_no"]
            admission_no=userExists(token_value)
            if admission_no!=None:
                return admission_no 
        except:
            return None
        
        

#obj=UserValidations()

#obj.studentPasswordReset("19CSEBE163","dg3sCV")



    


        




