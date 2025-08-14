import smtplib

meu_email = 'renato.asterio@hotmail.com'
senha = 'bvoyztbhpcptmqkm'

with smtplib.SMTP('smtp-mail.outlook.com', port=587) as connection:
    connection.starttls()
    connection.login(user=meu_email, password=senha)
    connection.sendmail(from_addr=meu_email, to_addrs='renato.asterio.ext@ultra.com.br', msg='Subject:Test\n\nOlá')