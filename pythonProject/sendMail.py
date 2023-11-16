import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPServerDisconnected


def sendEmail():
    try:
        # Setează detaliile de autentificare pentru serverul SMTP Yahoo
        email_address = 'danselegean@gmail.com'
        password = 'spin wyms jykc mkeq'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Adresa destinatarului
        to_address = 'adrian_dany15@yahoo.com'

        # Creează un obiect MIMEMultipart pentru mesaj
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_address
        msg['Subject'] = 'Alerta casa!'

        # Adaugă corpul mesajului
        body = 'UDA PLANTA.'
        msg.attach(MIMEText(body, 'plain'))

        # Conectează-te la serverul SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, password)

            # Trimite mesajul
            server.send_message(msg)

        print('Mesaj trimis cu succes!')
    except SMTPServerDisconnected as e:
        print(f"Conexiunea la server a fost întreruptă: {e}")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

#verificare
#sendEmail()