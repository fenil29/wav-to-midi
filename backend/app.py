from flask import Flask, render_template, request
import uuid
from handlers.handlers import Convert

app = Flask(__name__)

# prevent caching file for development


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def upload_file_page():
    return render_template('./upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    uploaded_file = request.files['file']
    file_name = str(uuid.uuid4())
    # file_name = str(uuid.uuid4()) + uploaded_file.filename
    if uploaded_file.filename != '':
        uploaded_file.save("./file_wav/" + file_name + ".wav")
    Convert.convert_file("./file_wav/" +file_name + ".wav", "./file_midi/" +file_name + ".mid")
    return 'file uploaded successfully'


if __name__ == "__main__":
    app.run()
