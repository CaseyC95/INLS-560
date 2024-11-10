# Python App for creating a Flask/SQLite Task list in HTML and CSS
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
        ''')
    print("Database initialized.")

# Fetch all tasks from the database
def get_tasks():
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
    return tasks

# Add a new task to the database
def add_task(title, description):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))

# Delete a task from the database
def delete_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        add_task(title, description)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
    