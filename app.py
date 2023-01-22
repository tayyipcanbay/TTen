from flask import Flask, request, after_this_request
from tesseract_operations import tesseract_it
from database_operations import (
    create_user_if_not_exists,
    create_query,
    update_query_answer,
)
from gpt_request import run_query
import os
import json
import uuid

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        token = request.headers.get("token")
        print(token)
        f.save(f.filename)
        user_id = create_user_if_not_exists(token)
        query_text = tesseract_it(f.filename)
        os.remove(f.filename)
        query_id = create_query(user_id, query_text)
        answer, api_key = run_query(token, query_text)
        _query_id, success = update_query_answer(query_id, answer)
        if query_id == _query_id and success:
            return answer
        else:
            return "Error in request"
    else:
        return "Not a POST request"

@app.route("/login", methods=["POST"])
def login():
    mail= request.json["mail"]
    token = request.json["token"]   
    if request.method == "POST":
        user_id = create_user_if_not_exists(token, mail)
        return json.dumps({"user_id": user_id, "status":200})
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3131, debug=True)
