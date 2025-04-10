from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Develop by Chandreshkumar Patel for Final Test of IDS."

@app.route('/company')
def company_name():
    return "Company: Wild Rydes"

@app.route('/developer')
def developer_name():
    return "Developer: Chandreshkumar Patel"

@app.route('/id')
def student_id():
    return "Student ID: 100925696"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
