# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:09:51 2021

@author: MartinXD
"""

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email import encoders

def enviarCorreo(file, description):
    msg = MIMEMultipart("plain")
    msg["From"] = "bravomartin178@gmail.com"
    msg["To"] = "bravomartin178@gmail.com"
    msg["Subject"] = description
    
    adjunto = MIMEBase("application", "octect-stream")
    adjunto.set_payload(open(file, "rb").read())
    encoders.encode_base64(adjunto)
    adjunto.add_header("content-Disposition", 'attachment; filename="InfoPrice.xlsx"')
    msg.attach(adjunto)
    
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("bravomartin178@gmail.com", "avenged sevenfold")
    smtp.sendmail("bravomartin178@gmail.com", "bravomartin178@gmail.com", msg.as_string())
    smtp.quit()