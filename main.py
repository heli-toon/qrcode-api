import io
from flask import Flask, request, make_response
import qrcode

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr():
    # Get the URL from the query string
    url = request.args.get('url')

    # Create the QR code image
    img = qrcode.make(url)

    # Save the QR code image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='png')
    buffer.seek(0)

    # Creating the response object
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'

    # Making the qr code image downloadable
    # response.headers['Content-Disposition'] = 'attachment; filename=qrcode'+f'{url}'+'.png'

    # Return response
    return response

if __name__ == '__main__':
    # Run app
    app.run()