from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

sample = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
mydb = client["router"]
mycol = mydb["my_router_collection"]


@sample.route("/")
def main():
    items = list(mycol.find({}))
    return render_template("index.html", items=items)

@sample.route("/add", methods=["POST"])
def add_router():
    ip = request.form.get("ip", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()


    if ip and username and password:
    
        mycol.insert_one({"ip": ip, "username": username, "password": password})
    return redirect(url_for("main"))

@sample.route("/delete", methods=["POST"])
def delete_router():
    rid = request.form.get("id")
    try:
        mycol.delete_one({"_id": ObjectId(rid)})
        if 0 <= idx < len(data):
            data.pop(idx)
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)

