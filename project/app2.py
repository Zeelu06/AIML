from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)
        return redirect("/")
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete_task(id):
    tasks.pop(id)
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_task(id):
    if request.method == "POST":
        tasks[id] = request.form["task"]
        return redirect("/")
    return render_template("update.html", task=tasks[id])

if __name__ == "__main__":
    app.run(debug=True)