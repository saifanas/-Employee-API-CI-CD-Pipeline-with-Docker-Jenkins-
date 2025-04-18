from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy database
employees = [
    {"id": 1, "name": "Alice", "position": "DevOps Engineer"},
    {"id": 2, "name": "Bob", "position": "Cloud Engineer"}
]

@app.route('/')
def home():
    return "Welcome to the Employee API!"

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    employees.append(data)
    return jsonify({"message": "Employee added", "employee": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
