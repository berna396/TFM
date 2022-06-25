import smtplib

server = smtplib.SMTP('imap.gmail.com', 587)
server.starttls()
server.login('testalertingtfm@gmail.com', 'testalerting')
server.sendmail('testalertingTFM@gmail.com', 'testalertingTFM@gmail.com', 'prueba')