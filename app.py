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


@app.route("/ask-image", methods=["POST"])
def ask_image():
    if request.method == "POST":
        image = request.files["prompt"]
        
        # query= request.json
        # user = query["user"]
        # user_id = user["id"]
        # user_token = user["token"]
        # user_mail = user["mail"]
        # prompt = query["prompt"]
        # image_name = str(uuid.uuid4()) + ".jpg"
        # image.save(os.path.join("images", image_name))
        # text = tesseract_it(image_name)
        # answer = run_query(user_token, text)
        # query_id = create_query(user_id, text, answer)
        # return json.dumps({"query_id": query_id,"answer":answer, "status":200})
    else:
        return json.dumps({"status":400})



@app.route("/ask-text", methods=["POST"])
def ask_text():
    if request.method == "POST":
        query= request.json
        user = query["user"]
        user_id = user["id"]
        user_token = user["token"]
        user_mail = user["mail"]
        prompt = query["prompt"]
        answer = run_query(user_token, prompt)
        query_id = create_query(user_id, prompt, answer)
        return json.dumps({"query_id": query_id,"answer":answer, "status":200})
    else:
        return json.dumps({"status":400})


@app.route("/login", methods=["POST"])
def login():
    mail= request.json["mail"]
    token = request.json["token"]   
    if request.method == "POST":
        user_id = create_user_if_not_exists(token, mail)
        return json.dumps({"user_id": user_id, "status":200})
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3131, debug=True)
