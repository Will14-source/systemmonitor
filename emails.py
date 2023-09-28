import json
import smtplib
from email.message import EmailMessage


"""

Essa função estrutura o e-mail utilizando o módulo 'email' e espera receber 4 (quatro) argumentos;
Remetente , Destinatário, Assunto e Contéudo.

"""
def gerar_email(de, para, assunto, conteudo):

    email = EmailMessage()
    remetente = de
    destinatario = para

    email["From"] = remetente
    email["To"] = destinatario
    email["Subject"] = assunto
    email.set_content(conteudo, subtype= "html")
        
    return email

"""

Essa função é feita utilizando o módulo 'smtplib' que é responsável por enviar o e-mail 
que foi estruturado na função anterior, lembrando que ela usa o endereço de e-mail e senha do remetente
é usado um arquivo JSON para extrair essas informações.

"""
def enviar_email(email):

    with open("config.json") as email_conf:
        dados_email = json.load(email_conf)

    servidor_email = smtplib.SMTP_SSL("smtp.gmail.com")
    servidor_email.login(dados_email["remetente"], dados_email["senha"])
    servidor_email.send_message(email)
    servidor_email.quit()

