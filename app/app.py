from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

account_sid = 'ACa65488664cae2390ed349a8e2c53d4fd'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

def download_image(media_url):
    # Implementar la lógica para descargar la imagen desde media_url y guardarla en el servidor
    # Devolver el nombre del archivo descargado
    pass

def convert_to_sticker(image_filename):
    # Implementar la lógica para convertir la imagen en sticker (PNG) y guardarla en el servidor
    # Devolver el nombre del archivo del sticker generado
    pass

def send_sticker(sticker_filename, recipient):
    # Implementar la lógica para enviar el sticker al número de teléfono del remitente
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='',
        to=f'whatsapp:{recipient}'
    )

    media_url = f"http://your-server-url/{sticker_filename}"
    message.media(media_url)

    print(message.sid)

if __name__ == "__main__":
    app.run(debug=True)
