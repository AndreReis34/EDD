import smtplib
import ssl
from email.message import EmailMessage

# Configurações
email_emissor = 'andre.reis@discente.ufopa.edu.br'
email_senha = 'andreaatr8943' # A senha de 16 caracteres do Google
email_receptor = '4ndr3.r3is@gmail.com'

# Estruturar a mensagem
mensagem = EmailMessage()
mensagem['Subject'] = 'Assunto do E-mail'
mensagem['From'] = email_emissor
mensagem['To'] = email_receptor
mensagem.set_content('Olá, este é um e-mail automático enviado com Python!')

# Conectar e enviar
contexto = ssl.create_default_context()
try:
    #TEM QUE TROCAR SERVIDOR DE EMAIL ANTES ENVIAR
    #SERVIDOR DO GMAIL = (smtp.gmail.com)
    with smtplib.SMTP_SSL('mail.ufopa.edu.br', 465, context=contexto) as smtp:
        smtp.login(email_emissor, email_senha)
        smtp.send_message(mensagem)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro: {e}")
