import telepot

TOKEN = '1995282608:AAHgCF249xJdHInqfX97zBQ-zbliTTGSZoQ'
bot = telepot.Bot(TOKEN)
me = 668618297

def sender(title , description):
    bot.sendMessage(me, f"{title} \n {description}")


# import smtplib, ssl
#
# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# sender_email = "shziyo12@gmail.com"
# password = "914766109z"
#
# # Create a secure SSL context
# context = ssl.create_default_context()
#
# # Try to log in to server and send email
# def sender(article):
#     try:
#         server = smtplib.SMTP(smtp_server, port)
#         server.ehlo()  # Can be omitted
#         server.starttls(context=context)  # Secure the connection
#         server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, "rashidovabdurakhmon@gmail.com", article)
#     except Exception as e:
#         # Print any error messages to stdout
#         print(e)
#     finally:
#         server.quit()