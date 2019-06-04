from flask import Flask, request, send_file
import qrcode
from io import BytesIO

form_name = 'data'
input_form = f'<h1>String to QR-Code</h1><p>By Jan Macenka</p><br><h2>Input some text and hit submit:</h2><form action="/" method="POST"><input name="{form_name}"><input type="submit"></form>'

app =Flask(__name__)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return input_form
    elif request.method == 'POST':
        imgIO = BytesIO()
        input_data = request.form[form_name]
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",back_color="white")#(fill_color='#66e100',back_color="white") #use planemos colors => impacts scanner results negativgely, deactivated.
        return serve_pil_image(img)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=False)
