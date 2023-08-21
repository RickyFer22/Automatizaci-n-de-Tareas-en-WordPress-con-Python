# **Envío de Correo Electrónico de Notificación**
# Autor: Ricardo Fernández
# Data Science-Data Analytics-Developer Python
# LinkedIn: [Perfil de LinkedIn](https://www.linkedin.com/in/ricardo-fern%C3%A1ndez00)
#
# Descripción:
# Este script automatiza el envío de un correo electrónico de notificación al finalizar la carga de productos desde un archivo CSV en WordPress.
# Utiliza el protocolo SMTP para conectarse a una cuenta de Gmail y enviar un correo electrónico con la hora y fecha de finalización.
#
# Advertencia:
# El uso de este script es responsabilidad del usuario. El autor no se hace responsable por problemas derivados de un uso indebido
# o mala ejecución del mismo.

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración de la conexión SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tu correo", "clave de google ")

# Creación del mensaje
msg = MIMEMultipart()
msg['From'] = "tucorreo@gmail.com"
msg['To'] = "correo de aviso "
msg['Subject'] = "Actualización de lista de precios"

# Obtención de la fecha y hora actuales
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Creación del cuerpo del mensaje
body = f"Su lista de precio ha sido actualizada en la tienda luzin.com.ar. Fecha y hora de actualización: {dt_string}"

msg.attach(MIMEText(body, 'plain'))

# Envío del correo electrónico
server.sendmail("admiluzin18@gmail.com", ["compras@luzin.com.ar", "ventas@luzin.com.ar"], msg.as_string())

# Cierre de la conexión SMTP
server.quit()
