from flask import Flask, render_template, request
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
    if uploaded_file.filename != '':
        uploaded_file.save("./file/" + uploaded_file.filename)
    return 'file uploaded successfully'


if __name__ == "__main__":
    app.run()
