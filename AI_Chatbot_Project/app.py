from flask import Flask, render_template, request, jsonify, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "studentassistant"

USERNAME = "tejaswini"
PASSWORD = "4567"

tips = [
    "Solve 2 DSA problems today.",
    "Update your GitHub profile.",
    "Practice aptitude for 30 minutes.",
    "Build one project every month.",
    "Revise one GATE subject daily."
]

knowledge_base = {

    "ai": "Artificial Intelligence enables machines to mimic human intelligence.",

    "machine learning": "Machine Learning is a subset of AI that learns patterns from data.",

    "deep learning": "Deep Learning uses neural networks with many layers.",

    "python": "Python is widely used in AI, Data Science and Web Development.",

    "java": "Java is an object-oriented programming language.",

    "javascript": "JavaScript makes websites interactive.",

    "html": "HTML creates the structure of web pages.",

    "css": "CSS styles web pages.",

    "react": "React is a frontend JavaScript library.",

    "node": "Node.js allows JavaScript to run on servers.",

    "mongodb": "MongoDB is a NoSQL database.",

    "full stack": """Full Stack Roadmap:
1. HTML
2. CSS
3. JavaScript
4. React
5. Node.js
6. Express.js
7. MongoDB
8. Deployment""",

    "frontend": "Frontend uses HTML, CSS and JavaScript.",

    "backend": "Backend handles APIs, databases and business logic.",

    "dsa": "DSA stands for Data Structures and Algorithms.",

    "array": "Array stores multiple elements of the same type.",

    "linked list": "Linked List is a dynamic linear data structure.",

    "stack": "Stack follows LIFO principle.",

    "queue": "Queue follows FIFO principle.",

    "tree": "Tree is a hierarchical data structure.",

    "graph": "Graph consists of vertices and edges.",

    "gate": """GATE CSE Subjects:
DSA
OS
DBMS
CN
TOC
COA
Compiler Design
Aptitude""",

    "resume": "Keep resume concise and highlight projects and skills.",

    "placement": "Focus on DSA, Aptitude and Communication Skills.",

    "interview": "Practice coding, projects and HR questions.",

    "internship": "Build projects and maintain GitHub regularly.",

    "linkedin": "Keep your LinkedIn profile updated.",

    "github": "Upload projects with proper README files.",

    "docker": "Docker is a containerization platform.",

    "aws": "AWS is a cloud computing platform.",

    "hackathon": "Hackathons improve coding and teamwork skills.",

    "project": """Project Ideas:
1. Rule-Based Chatbot
2. Face Detection System
3. Movie Recommendation System
4. Image Caption Generator
5. Tic Tac Toe AI""",

    "study plan": """Daily Study Plan:
1 Hour DSA
1 Hour Full Stack
1 Hour GATE
30 Min Aptitude
30 Min Revision""",

    "motivate": "Success is the sum of small efforts repeated every day.",

    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
}


def chatbot_response(msg):

    msg = msg.lower()

    for key in knowledge_base:

        if key in msg:
            return knowledge_base[key]

    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you today?"

    if "time" in msg:
        return "Current Time: " + datetime.now().strftime("%H:%M:%S")

    if "date" in msg:
        return "Today's Date: " + datetime.now().strftime("%d-%m-%Y")

    if "bye" in msg:
        return "Goodbye! Have a nice day."

    return "Sorry, I don't understand that. Ask me about AI, Programming, DSA, GATE, Resume or Career."


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == USERNAME and password == PASSWORD:

        session["user"] = username

        return redirect("/chatbot")

    return "Invalid Username or Password"


@app.route("/chatbot")
def chatbot():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "chatbot.html",
        username=session["user"],
        tip=random.choice(tips),
        date=datetime.now().strftime("%d-%m-%Y"),
        time=datetime.now().strftime("%H:%M")
    )


@app.route("/get_response", methods=["POST"])
def get_response():

    data = request.get_json()

    message = data["message"]

    return jsonify({
        "response": chatbot_response(message)
    })


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)