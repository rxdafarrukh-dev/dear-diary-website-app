from flask import Flask, render_template, request, redirect, url_for, session

#create a Flask app 
app = Flask(__name__)
app.secret_key = "any-random-string-you-want"

#Password and username for login
users = {
    "admin": "password"
}

#Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None

    if request.method == "POST":
        entered_username = request.form["username"]
        entered_password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if entered_password != confirm_password:
            error = "Passwords do not match, try again"
        else:
           users[entered_username] = entered_password
           return redirect(url_for("login"))

    return render_template("signup.html", error=error)

#The login route 
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
   
    if request.method == "POST":
        entered_username = request.form["username"]
        entered_password = request.form["password"]

        if entered_username in users and users[entered_username] == entered_password:
            session["username"] = entered_username
            return redirect(url_for("main"))
        else:
            error = "Wrong username or password, try again"

    return render_template("login.html", error=error)

#main route after successful login
@app.route("/main")
def main():
    return render_template("main.html")

#logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

#Run the app
if __name__ == "__main__":
    app.run(debug=True)
    
    
