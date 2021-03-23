import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__=="__main__":
    server_mail = "smtp.163.com" 
    server_port = 25
    server_user = 
    server_pwd = 
    sender = 
    receiver = 
    
    con = smtplib.SMTP(server_mail,server_port)
    con.login(server_user,server_pwd)

    msg = MIMEMultipart()
    subject = Header("SMTP subject","utf-8").encode()
    msg['Subject'] = subject
    msg['From'] = sender+" <"+sender+">"
    msg['To'] = receiver
    text = MIMEText("Hungry","plain","utf-8")
    msg.attach(text)

    con.sendmail(sender,receiver,msg.as_string())
    con.quit()

    '''
    SMTP协议要做什么
    https://blog.csdn.net/kerry0071/article/details/28604267#:~:text=%E9%80%9A%E5%B8%B8%E5%AE%83%E5%B7%A5%E4%BD%9C%E5%9C%A8%E4%B8%A4,Mail%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%BB%BA%E7%AB%8BSMTP%E8%BF%9E%E6%8E%A5%E3%80%82
    '''
    