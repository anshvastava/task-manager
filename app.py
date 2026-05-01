from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

html = """
<h2>Personal Task Manager</h2>

<form method="POST">
    <input type="text" name="task" placeholder="Enter task" required>
    <button type="submit">Add Task</button>
</form>

<h3>Tasks:</h3>
<ul>
{% for task in tasks %}
    <li>{{ task }}</li>
{% endfor %}
</ul>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template_string(html, tasks=tasks)

app.run()