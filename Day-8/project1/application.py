import os

from flask import Flask, session, render_template, request,make_response,jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
    # raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

# @app.route("/")
# def index():
#     return "Project 1: TODO"

@app.route("/register",methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/hello",methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/api/addtask",methods=["POST"])
def addTask():

    try:

      request_data=request.get_json(silent=True)
      di=(request.data.decode())
      task=json.loads(di)
      # print(di)
      # print(di['task_name'])
      task_name = task['task_name']
      due_date = task['due_date']
      is_done=task['is_done']
      print(task_name+" "+due_date+" ")
      return make_response("Task Added", 200)
    except: 
      return make_response("some thing went wrong", 500)   

    #   books = search_book(s_type, value)
    #   if books :
    #     return make_response(jsonify(books), 200)
    #   else :
    #     return make_response("nothing found", 404)
    # except: 
    #   return make_response("some thing went wrong", 500)    


@app.route("/api/gettasks",methods=["GET"])
def getTasks():
	# tasks=['task1','20.05.2020',False]
	tasks={['data':'data']}
	# return jsonify(hello='hello')
	# return make_response("Task Added", 200)
	response = app.response_class(
        response=json.dumps(tasks),
        status=200,
        mimetype='application/json'
    )
	return response
