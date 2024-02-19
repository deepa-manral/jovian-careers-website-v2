from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '100000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '200000'
}, {
    'id': 3,
    'title': 'Front-end Developer',
    'location': 'Dublin, Ireland',
}, {
    'id': 4,
    'title': 'Python Developer',
    'location': 'Dublin, Ireland',
    'salary': '£200000'
}]


@app.route('/')
def hello_jovian():
  return render_template('/home.html', jobs=JOBS)


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
