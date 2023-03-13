from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.app_context().push()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/applicants")
def applicants():
    return render_template("applicants.html")


@app.route("/student_details")
def student():
    return render_template("student_details.html")

@app.route("/job_profiles")
def jobs():
    return render_template("job_profiles.html")








if __name__ =="__main__":
    app.run(debug=True)