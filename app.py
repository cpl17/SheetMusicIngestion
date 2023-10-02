from flask import Flask,render_template,request,redirect
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)

#App Configurations
app.config['UPLOAD_FOLDER'] = 'current_upload'


ALLOWED_EXTENSIONS = ['jpg','png'] #If change, change the accept attribute in index.html


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload_image():

    #Run Checks
    if 'image' not in request.files:
        return "No file part"
    
    image_file = request.files['image']

    if image_file.filename == "":
        return "No selected file"

    if not allowed_file(image_file.filename):
        return "Invalid file format"
    
    #If checks passed, save image to uploads
    filename = secure_filename(image_file.filename)
    image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return redirect("/")




def allowed_file(filename):
    # Check if the file has a valid extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS