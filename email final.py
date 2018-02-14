import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
msg="hi"
server.starttls()
server.login('johnrohith1731999@gmail.com','password')
server.sendmail('johnrohith1731999@gmail.com','prateekkovalli7@gmail.com',msg)
