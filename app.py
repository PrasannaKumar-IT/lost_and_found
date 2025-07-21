from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from datetime import datetime
app=Flask(__name__)
app.config['SECRET_KEY'] = 'lost_found_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_and_found.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db=SQLAlchemy(app)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_type = db.Column(db.String(10), nullable=False)  
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
    contact_name = db.Column(db.String(50), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(120))

@app.route("/",methods=['GET'])
def home_page():
    item_type=request.args.get("type")
    if item_type in ['lost','found']:
        items=Item.query.filter_by(item_type=item_type).order_by(Item.date_reported.desc()).all()
    else:
        items=Item.query.order_by(Item.date_reported.desc()).all()
    return render_template("home.html",items=items)


@app.route("/report",methods=['GET','POST'])
def report_item():
    if request.method =='POST':
        item_name=request.form['item_name']
        item_type=request.form['item_type']
        description=request.form['description']
        location=request.form['location']
        contact_name=request.form['contact_name']
        contact_email=request.form['contact_email']
        image=request.files['image']
        image_filename=None

        if image and allowed_file(image.filename):
            filename=secure_filename(image.filename)
            image_filename=filename
            image.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        
        new_item=Item(
            item_name=item_name,
            item_type=item_type,
            description=description,
            location=location,
            contact_name=contact_name,
            contact_email=contact_email,
            image_filename=image_filename
            )
        
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for("report_item"))
    return render_template("report.html")

@app.route("/item/<int:item_id>")
def item_detail(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template("item_detail.html", item=item)

# Run the app
app.run(debug=True)




