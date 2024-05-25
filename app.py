from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Software Developer",
    "location": "Remote",
    "salary": "$80,000"
}, {
    "id": 2,
    "title": "Data Analyst",
    "location": "New York",
    "salary": "$70,000"
}, {
    "id": 3,
    "title": "UX Designer",
    "location": "San Francisco",
}, {
    "id": 4,
    "title": "Product Manager",
    "location": "Los Angeles",
    "salary": "$90,000"
}]


@app.route("/")
def hello_world():
  return render_template("home.html" , jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
