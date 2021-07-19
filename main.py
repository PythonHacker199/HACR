# HelloGuys
# welcome Hacker Python Channel
# today we will make a email bot
# Here we dont need a pypi pakage
import smtplib
sender =str(input("SENDER EMAIL:  "))
TEXT = str(input("TEXT: "))
server= smtplib.SMTP('smtp.gmail.com',587)
server.login('your email id','password of email')
server.sendmail('email',sender,TEXT)
# NOTE U MAY HAVE TO GIVE SOME PRIVILAGE TO WORK THIS CODE IN GOOGLE ACCOUNT
# OK THEN THANK U FOR WATCHING
# LIKE AND SUBSCRIBE