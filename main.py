from flask import Flask,render_template as render, request as req,redirect, url_for
from pymongo import MongoClient
import os
import time


client = MongoClient("mongodb+srv://jbxvi:Eight8nine9@cluster0.1beb8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['root']
collection = db['uploads']


app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

#home
@app.route('/', methods=["GET", "POST"])
def home():
    products = collection.find()
    search = req.form.get('search')


    #sort
    if req.form.get('new')=="new":
        products = collection.find().sort("date",-1)
        return render("home.html", products=products,message="")

    if req.form.get('new')=="low":
       products = collection.find().sort("price", 1)
       return render("home.html", products=products, message="")

    if req.form.get('new')=="new":
        products = collection.find().sort("pricwe",-1)
        return render("home.html", products=products,message="")
    #search
    if search!=None:
         products = collection.find({"title": search})
         if products==None:
             products1 = collection.find({"desciption"})
             if products1 ==None:
                 products2 = collection.find({"tags"})
                 if products2 ==None:
                     message = "no item match you search"
                     return render("home.html", products="", message="")
                 else:
                     products = products2
                     return render("home.html", products=products,message="")

    return render("home.html", products=products, message="")
#admin-upload
@app.route('/admin-upload', methods=["GET", "POST"])
def upload():
    if req.method == "POST":
        title = req.form.get('title')
        price = req.form.get('price')
        desciption = req.form.get("description")
        id = req.form.get('id')
        tags = req.form.get("tags")
        m = req.form.get('m')
        l = req.form.get('l')
        xl = req.form.get('xl')
        xxl = req.form.get('xxl')
        xxxl = req.form.get('xxxl')

        file = req.files['image']

        file.save(os.path.join(app.config['UPLOAD_PATH'], id + ".jpg"))
        image_path = f"/{app.config['UPLOAD_PATH']}/{id}.jpg"
        find = collection.find_one({"id": id})
        if find != None:
            return render("upload.html", message="Same ID already exists")
        else:
            t = time.localtime()
            current_time = time.strftime("%I:%M:%S:%p", t)
            current_date = time.strftime("%y:%m:%d")
            collection.insert_one({"title": title, "price": price,"image":image_path, "desciption":desciption, "id": id, "tags": tags
                                               , "m": m, "l": l, "xl": xl, "xxl": xxl, "xxxl": xxxl
                                               , "time": current_time, "date": current_date})
            return render("upload.html", message="successfully uploaded")

    return render('upload.html', message="")

#buy
@app.route('/buy', methods=['POST',"GET"])
def buy():

    id = req.form.get('buy')
    product = collection.find_one({"id":id})

    return render("buy.html", p=product, id=id, message="")

#remove
if __name__=="__main__":
    app.run(debug=True)