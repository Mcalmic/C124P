from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/hello")
def helloworld():
    return "hello world"

tasks = [
    {
        "id": 1,
        "name":"Bob",
        "contact": "Brother",
        "done": False,
    },
    {
        "id": 2,
        "name":"Dev",
        "contact": "Friend",
        "done": False,
    },
]
@app.route("/add-data", methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({"STATUS":"error", "message": "Please provide the data."})

    task = {
        "name": request.json["title"],
        "contact": request.json.get("description", ""),
        "done": False,
        "id": tasks[-1]["id"] + 1
    }

    tasks.append(task)

    return jsonify({
        "status": "success",
        "message": "Contact added successfully !"
    })
@app.route("/get-data")
def getdata():
    return jsonify({
        "data": tasks
    })

if __name__ == "__main__":
    app.run(debug = True)
