from flask_mail import Mail,Message
from App import app
from AppCredentials import Credentials as creds
app.config.update(
    DEBUG=True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=creds.MAIL_ID,
    MAIL_PASSWORD=creds.MAIL_PASSWORD
)

mail=Mail(app)

def studentForgotPassword(mail,token):
    msg=Message("Forgot Password Request ! ",
    sender="sonacse2019to2023@gmail.com",
    recipients=[mail])
    msg.body=f'''To reset your password, please visit the following link :
    {url_for()}
    
    '''

