import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email@gmail.com", "password")

message = "Subject: Malware Alert\n\nEICAR Detected!"
server.sendmail("email@gmail.com", "receiver@gmail.com", message)
server.quit()
