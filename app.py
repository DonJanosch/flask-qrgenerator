from flask import Flask, request, redirect, url_for, send_from_directory

import qrcode, os
from datetime import datetime

results_dir = './Result_Data/'
form_name = 'data'
input_form = f'<h1>String to QR-Code</h1><br><h2>By Jan Macenka</h2><br><p>Input some text and hit submit:</p><form action="/" method="POST"><input name="{form_name}"><input type="submit"></form>'

app =Flask(__name__, static_folder=results_dir)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return input_form
    elif request.method == 'POST':
        timestamp = datetime.now().strftime('%Y%m%d-%H_%M_%S')
        input_data = request.form[form_name]
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        file_name = f'{timestamp}_Sample.jpeg'
        file_path = f'{results_dir}{file_name}'
        img.save(file_path)
        return send_from_directory(results_dir, file_name)#, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
