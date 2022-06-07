from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/upload')
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
