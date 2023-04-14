from flask import Flask, jsonify, request
import json

HOST = "localhost" # 127.0.0.1
PORT = 1234
DEBUG = True

app = Flask(__name__)

# make a route with a url following a /
@app.route("/first", methods=["GET"])
def firstRoute():
    return jsonify({"reposnse":"Route"})

@app.route("/newRoute", methods=["GET"])
def newRoute():
    return "Added a new route"

@app.route("/numberInspector", methods=["POST"])
def numberInspector():
    userInput = request.json["value"]
    if (type(userInput) == int):
        try:
            return getData(userInput)
        except KeyError:
            return create_data(userInput)
    else:
        return jsonify({"results": "the \"value\" should be an integer"}), 400
    

def create_data(value):
    data = load_data()
    data[value] = {
            "isEven" : value % 2 == 0,
            "square" : value**2,
            "cube" : value**3,
            "binary" : bin(value),
            "hex" : hex(value)
        }
    save_data(data)
    return data

def getData(value):
    data = load_data()
    return data[value]

def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
        return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

    
if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)