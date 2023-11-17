from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from rembg import remove
from PIL import Image

app = Flask(__name__)

def remove_bg(img_source: str) -> Image:
    input_img = Image.open(img_source)
    output_img = remove(input_img)
    return output_img.save(img_source.replace(".jpg", "_output.png"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        removed_bg = remove_bg(secure_filename(f.filename))
        return redirect(url_for('create'), removed_bg)

if __name__ == "__main__":
    app.run(debug=True)


