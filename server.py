from typing import List, Dict
from flask import Flask, render_template_string, request
import mysql.connector

app = Flask(__name__)

def fetch_students() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'student'  # Changed database name to 'student'
    }

    # Establishing connection
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Fetching data from the 'students' table
    cursor.execute('SELECT * FROM students')
    results = []
    for row in cursor.fetchall():
        student_dict = {
            'Student_ID': row[0],
            'Student_Name': row[1],
            'Student_Age':row[2],
            'Student_CGPA':row[3]
        }
        results.append(student_dict)

    # Closing cursor and connection
    cursor.close()
    connection.close()

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    students = []  # Initially, no data is fetched
    display_students = False

    if request.method == 'POST':
        # Fetching student data when the button is clicked
        students = fetch_students()
        display_students = True
    
    # Creating a table-like view using Jinja2 templating
    table_template = '''
    <html>
    <head>
        <title>Student Data</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-image: url("https://tse1.mm.bing.net/th/id/OIP.Gl_WMeW-v87pANMo5qLgRAHaEK?w=315&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #fff;
                text-align: center;
                margin-top: 20px;
            }
            table {
                border-collapse: collapse;
                width: 80%;
                background-color: transparent; /* Semi-transparent white background */
                margin: 20px auto;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                overflow: hidden;
                display: {% if display_students %}block{% else %}none{% endif %};  /* Show the table only when students are displayed */
            }
            th, td {
                padding: 12px 15px;
                text-align: left;
                border-bottom: 1px solid #ddd;
                color: #fff;
            }
            th {
                background-color: transparent;
                font-weight: bold;
            }
            tr:nth-child(even) {
                background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
            }
            tr:hover {
                background-color: rgba(255, 255, 255, 0.6); /* Semi-transparent white background on hover */
            }
            button {
                background-color: #4caf50;
                color: white;
                padding: 15px 30px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                margin: 20px auto;
                display: block;
                transition: background-color 0.3s ease;
                font-size: 16px;
                outline: none;
            }
            button:hover {
                background-color: #45a049;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Student Data</h1>
            <form method="POST">
                <button type="submit">Display</button> <!-- Changed button label to "Display" -->
            </form>
            <table>
                <thead>
                    <tr>
                        <th>Student ID</th>
                        <th>Student Name</th>
                        <th>Student Age</th>
                        <th>Student CGPA</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in students %}
                    <tr>
                        <td>{{ student.Student_ID }}</td>
                        <td>{{ student.Student_Name }}</td>
                        <td>{{ student.Student_Age }}</td>
                        <td>{{ student.Student_CGPA }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    '''
    
    # Rendering the template string with student data
    rendered_template = render_template_string(table_template, students=students, display_students=display_students)
    
    return rendered_template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
