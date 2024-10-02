from flask import Flask, render_template
# 04069656965

app = Flask(__name__)




@app.route("/home")
def home(): 
    return render_template('index.html', data=   [1,2,3,"fdsfsdfsdfsd"])

@app.route("/")
def index():
    return render_template('index.html', data=   [1,2,3,"fdsfsdfsdfsd"])
app.run(debug=True)






 

