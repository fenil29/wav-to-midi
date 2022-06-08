from flask import Flask, render_template, request, send_file
import uuid
import requests
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
        # print(uploaded_file.filename)
        file_name = uploaded_file.filename.split('.')[0]
        uploaded_file.save(file_name + ".wav")
    Convert.convert_file(file_name + ".wav", file_name + ".mid")
    return send_file(path_or_file=file_name + ".mid", mimetype="audio/midi", as_attachment=True)
    # return 'file uploaded successfully'


@app.route('/upload_wav_link', methods=['GET', 'POST'])
def upload_wav_link():
    url = request.form['wavLink']
    r = requests.get(url, allow_redirects=True)
    open('wav_file.wav', 'wb').write(r.content)
    Convert.convert_file("wav_file.wav", "wav_file.mid")
    return send_file(path_or_file="wav_file.mid", mimetype="audio/midi", as_attachment=True)


if __name__ == "__main__":
    app.run()
