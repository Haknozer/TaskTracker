
<h1>Task Tracker CLI</h1>
    <p>Task Tracker CLI is a simple command-line interface (CLI) application designed to help you manage your tasks efficiently. You can add, update, delete, and track the progress of your tasks, all from your terminal. The tasks are stored in a JSON file for easy retrieval and manipulation.</p>

  <h2>Features</h2>
    <ul>
        <li>Add new tasks</li>
        <li>Update existing tasks</li>
        <li>Delete tasks</li>
        <li>Mark tasks as "active" or "inactive"</li>
        <li>List all tasks, or filter by status (active,inactive,date)</li>
        <li>Task properties include a unique ID, description, status, and timestamps for creation and updates</li>
    </ul>

  <h2>Requirements</h2>
    <ul>
        <li>This project runs entirely from the command line.</li>
        <li>It stores tasks in a <code>tasks.json</code> file in the current directory.</li>
        <li>No external libraries or frameworks are used—only native modules for working with the filesystem and handling user inputs.</li>
    </ul>

  <h2>Task Properties</h2>
    <p>Each task has the following properties:</p>
    <ul>
        <li><strong>id</strong>: A unique identifier for the task</li>
        <li><strong>description</strong>: A short description of the task</li>
        <li><strong>status</strong>: The current status of the task (<code>todo</code>, <code>in-progress</code>, <code>done</code>)</li>
        <li><strong>createdAt</strong>: The timestamp when the task was created</li>
        <li><strong>updatedAt</strong>: The timestamp when the task was last updated</li>
    </ul>

  <h2>How to Use</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/haknozer/TaskTracker.git </code></pre>
        </li>
        <li>Run the task tracker using your terminal and pass the appropriate commands.</li>
    </ol>
    
<h3>Commands</h3>

<h4>Add a New Task</h4>
    <pre><code>1 and  "Your task description"
# Example:
1 "Buy groceries"</code></pre>
<h4>Update a Task</h4>
    <pre><code>8 &lt;task_id&gt; and "Updated task description"
# Example:
8 and "Buy groceries and cook dinner"
    </code></pre>

  <h4>Delete a Task</h4>
    <pre><code>3 &lt;task_id&gt;
# Example:
3 1
    </code></pre>

  <h4>Mark a Task as Done</h4>
    <pre><code>2 &lt;task_id&gt;
# Example:
2 1
    </code></pre>

  <h4>List All Tasks</h4>
    <pre><code>9
    </code></pre>

  <h2>JSON Structure</h2>
    <p>All tasks are stored in <code>tasks.json</code>. Below is an example of the structure:</p>
    <pre><code>[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": false,
    "createdAt": "10/20/24",
    "updatedAt": "10/21/24"
  },
  {
    "id": 2,
    "description": "Finish homework",
    "status": true,
    "createdAt": "10/25/24",
    "updatedAt": "10/26/24"
  }
]
    </code></pre>

  <h2>Error Handling</h2>
    <ul>
        <li><strong>TASK NOT FOUND</strong>: If the JSON file does not exist, the application will create one.</li>
    </ul>

  <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to submit a pull request or file an issue.</p>

https://roadmap.sh/projects/task-tracker
