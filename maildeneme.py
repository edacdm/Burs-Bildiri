import smtplib

def MailGonder():
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "your password"

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_email, password)
        print("Giriş Yapıldı.")

        body = "YÖK 100/2000 BURSU HAKKINDA YENİ BİR GELİŞME VAR !\nlink: https://yuzikibinbursu.yok.gov.tr/"
        subject = "BURS HABERİ"
        message = f'Subject: {subject}\n\n{body}'.encode('utf-8')
        smtp.sendmail(sender_email, receiver_email, message)

        print(f"{receiver_email} adresine mesajınız ulaştırıldı")
        smtp.quit()
