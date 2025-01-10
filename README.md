# QR CODE API

When ran the server listens for `GET` requests at `/qr` endpoint with a `url` parameter from the query string and uses the qrcode library to create a QR code image. It then saves the image to a buffer and creates a response object with the contents of the buffer. Finally, it returns the response object with the QR code image. It also automatically downloads it.

## Dependencies

Install the following
- flask
- qrcode

Windows 🪟
```bash
pip install flask qrcode
```
MacOS🍎 & Linux🐧
```bash
pip3 install flask qrcode
```

### How to make it work

- Run a server

Windows 🪟
```bash
python main.py
```
MacOS🍎 & Linux🐧
```bash
python3 main.py
```

- Make a get request to `/qr` endpoint with a `url` parameter, like below 👇. Paste in your browser search bar.

```bash
https://localhost:5000/qr?url=https://www.example.com

```
