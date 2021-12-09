from flask import Flask, render_template, redirect, request
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # just show "Index" for now
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/user")
def users():
    # call the get all class method to get all users
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route("/create")
def create():
    return render_template("createUser.html")

@app.route("/create_user", methods=['POST'])
def createUser():
    # First we make a data dictionary from the request.form
    # coming from our template.
    # the keys in the data need to line up EXACTLY with the variables 
    # in our query string.

    data = {
        "fname" : request.form['fname'],
        "lname" : request.form['lname'],
        "email" : request.form['email']
    }
    User.save(data)
    return redirect("/user")

if __name__ == "__main__":
    app.run(debug=True)
