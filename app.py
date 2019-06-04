from flask import Flask, request, send_file
import qrcode
from io import BytesIO

DATA_FIELD = 'data'
INPUT_FORM = f'''
<h1>String to QR-Code</h1>
<p>By Jan Macenka</p>
<h2>Input some text and hit submit:</h2>
<form action="/" method="POST">
<input name="{DATA_FIELD}">
<input type="submit">
</form>'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return INPUT_FORM
    elif request.method == 'POST':
        imgIO = BytesIO()
        input_data = request.form[DATA_FIELD]
        img = qrcode.make(input_data)
        img.save(imgIO, 'PNG', quality=70)
        imgIO.seek(0)
        return send_file(imgIO, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
