from flask import Flask,render_template
from flask_pymongo import PyMongo
from routes.routes import blog_page

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/blog_db"
mongo=PyMongo(app)

app.register_blueprint(blog_page)

@app.route('/')
def index():
    return  render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)