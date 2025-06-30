from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Keep DB connection alive globally
conn = sqlite3.connect(':memory:', check_same_thread=False)
conn.row_factory = sqlite3.Row

# Initialize DB once
def init_db():
    cursor = conn.cursor()

    # Create tables
    cursor.execute('DROP TABLE IF EXISTS departments')
    cursor.execute('DROP TABLE IF EXISTS employees')

    cursor.execute('''
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            department_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            age INTEGER,
            salary INTEGER,
            department_id INTEGER,
            manager_id INTEGER,
            email TEXT,
            hire_date TEXT,
            position TEXT,
            status TEXT,
            country TEXT
        )
    ''')

    # Insert sample data
    cursor.executemany('INSERT INTO departments (id, department_name) VALUES (?, ?)', [
        (1, 'HR'), (2, 'IT'), (3, 'Finance')
    ])

    cursor.executemany('''
        INSERT INTO employees (id, first_name, age, salary, department_id, manager_id, email, hire_date, position, status, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        (101, 'Alice', 30, 70000, 1, None, 'alice@example.com', '2021-01-01', 'Analyst', 'Active', 'India'),
        (102, 'Bob', 45, 80000, 2, 101, 'bob@example.com', '2020-05-15', 'Manager', 'Active', 'USA'),
        (103, 'Charlie', 28, 60000, 2, 102, 'charlie@example.com', '2023-08-20', 'Developer', 'Inactive', 'India'),
        (104, 'David', 33, 50000, None, 103, None, '2022-11-10', 'HR Assistant', 'Cancelled', 'India')
    ])
    conn.commit()

# Initialize database
init_db()

queries = [
    ("1. Basic SELECT", "SELECT first_name, salary FROM employees"),
    ("2. WHERE Clause", "SELECT * FROM employees WHERE age > 30"),
    ("3. DISTINCT", "SELECT DISTINCT country FROM employees"),
    ("4. ORDER BY", "SELECT first_name, salary FROM employees ORDER BY salary DESC"),
    ("5. LIMIT", "SELECT * FROM employees LIMIT 2"),
    ("6. LIKE", "SELECT first_name FROM employees WHERE first_name LIKE 'A%'"),
    ("7. IN", "SELECT * FROM employees WHERE department_id IN (1, 2)"),
    ("8. BETWEEN", "SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2023-12-31'"),
    ("9. Top-N Queries", "SELECT first_name, salary FROM employees ORDER BY salary DESC LIMIT 3"),
    ("10. Pagination", "SELECT * FROM employees ORDER BY hire_date LIMIT 3 OFFSET 1"),
    
    ("11. COUNT", "SELECT COUNT(*) FROM employees WHERE department_id = 2"),
    ("12. SUM", "SELECT SUM(salary) FROM employees"),
    ("13. AVG", "SELECT AVG(salary) FROM employees WHERE department_id = 2"),
    ("14. MIN / MAX", "SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees"),
    ("15. GROUP BY", "SELECT department_id, COUNT(*) FROM employees GROUP BY department_id"),
    ("16. HAVING", "SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) > 60000"),
    ("17. STRING_AGG (grouped names)", "SELECT department_id, GROUP_CONCAT(first_name, ', ') AS names FROM employees GROUP BY department_id"),
    
    ("18. INNER JOIN", "SELECT e.first_name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id"),
    ("19. LEFT JOIN", "SELECT e.first_name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.id"),
    ("20. RIGHT JOIN (Simulated using LEFT JOIN)", "SELECT d.department_name, e.first_name FROM departments d LEFT JOIN employees e ON d.id = e.department_id"),
    ("21. SELF JOIN", "SELECT e1.first_name AS employee, e2.first_name AS manager FROM employees e1 JOIN employees e2 ON e1.manager_id = e2.id"),
    ("22. CROSS JOIN", "SELECT e.first_name, d.department_name FROM employees e CROSS JOIN departments d"),
    
    ("23. CASE Statement", "SELECT first_name, salary, CASE WHEN salary > 70000 THEN 'High' ELSE 'Standard' END AS salary_level FROM employees"),
    ("24. SUBQUERY", "SELECT * FROM employees WHERE department_id = (SELECT id FROM departments WHERE department_name = 'IT')"),
    
    ("25. WINDOW Function: RANK", "SELECT first_name, salary, department_id, RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank FROM employees"),
    ("26. ROW_NUMBER", "SELECT ROW_NUMBER() OVER (ORDER BY hire_date) AS row_num, first_name, hire_date FROM employees"),
    ("27. PARTITION BY + SUM", "SELECT department_id, first_name, salary, SUM(salary) OVER (PARTITION BY department_id) AS dept_total FROM employees"),
    
    ("28. WITH CTE", "WITH high_earners AS (SELECT * FROM employees WHERE salary > 60000) SELECT * FROM high_earners WHERE department_id = 2"),
    ("29. PIVOT (Simulated)", "SELECT department_id, SUM(CASE WHEN strftime('%Y', hire_date) = '2021' THEN salary END) AS salary_2021, SUM(CASE WHEN strftime('%Y', hire_date) = '2022' THEN salary END) AS salary_2022 FROM employees GROUP BY department_id"),
    
    ("30. UNION", "SELECT first_name FROM employees UNION SELECT department_name FROM departments"),
    
    ("31. INSERT", "INSERT INTO employees (id, first_name, age, salary, department_id, manager_id, email, hire_date, position, status, country) VALUES (105, 'Eva', 29, 65000, 1, 101, 'eva@example.com', '2024-01-10', 'HR Assistant', 'Active', 'India')"),
    ("32. BULK INSERT", "INSERT INTO departments (id, department_name) VALUES (4, 'Sales'), (5, 'Marketing')"),
    ("33. UPDATE", "UPDATE employees SET salary = salary * 1.10 WHERE department_id = 1"),
    ("34. DELETE", "DELETE FROM employees WHERE status = 'Cancelled' AND hire_date < '2022-01-01'"),
    
    ("35. TRANSACTION", "BEGIN TRANSACTION; UPDATE employees SET salary = salary - 1000 WHERE id = 101; UPDATE employees SET salary = salary + 1000 WHERE id = 102; COMMIT;"),
    
    ("36. CREATE TABLE", "CREATE TABLE projects (id INTEGER PRIMARY KEY, project_name TEXT, start_date TEXT)"),
    ("37. CREATE INDEX", "CREATE INDEX idx_email ON employees(email)"),
    ("38. CREATE VIEW", "CREATE VIEW active_employees AS SELECT * FROM employees WHERE status = 'Active'"),
    ("39. STORED PROCEDURE (Simulated)", "-- SQLite doesn't support SPs natively, but this would be valid in other DBs:\n-- CREATE PROCEDURE GetHighEarners()\n-- AS\n-- SELECT * FROM employees WHERE salary > 75000"),
    
    ("40. NULL Handling", "SELECT first_name FROM employees WHERE email IS NULL"),
    ("41. COALESCE", "SELECT first_name, COALESCE(email, 'No Email') AS contact_email FROM employees"),
    ("42. DATE Functions", "SELECT first_name, DATE(hire_date, '+5 days') AS adjusted_date FROM employees"),
    ("43. Duplicate Detection", "SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*) > 1")
]


@app.route("/", methods=["GET", "POST"])
def index():
    query_blocks = []

    for idx, (title, default_query) in enumerate(queries):
        result_html = ""
        query = request.form.get(f"query_{idx}", default_query)

        if request.method == "POST" and f"run_{idx}" in request.form:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                headers = [desc[0] for desc in cursor.description] if cursor.description else []

                result_html += "<table><tr>"
                for h in headers:
                    result_html += f"<th>{h}</th>"
                result_html += "</tr>"
                for row in rows:
                    result_html += "<tr>" + "".join(f"<td>{row[col]}</td>" for col in headers) + "</tr>"
                result_html += "</table>"

            except Exception as e:
                result_html = f"<div class='error'>Error: {e}</div>"

        query_blocks.append((idx, title, query, result_html))

    # Read HTML from file path
    with open("ui.html", "r", encoding="utf-8") as f:
        template = f.read()

    return render_template_string(template, query_blocks=query_blocks)

if __name__ == '__main__':
    app.run(debug=True)











# Django Code

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
import sqlite3
import os

# DB init once
conn = sqlite3.connect(':memory:', check_same_thread=False)
conn.row_factory = sqlite3.Row

def init_db():
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS departments')
    cursor.execute('DROP TABLE IF EXISTS employees')

    cursor.execute('CREATE TABLE departments (id INTEGER PRIMARY KEY, department_name TEXT)')
    cursor.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY, first_name TEXT, age INTEGER, salary INTEGER,
            department_id INTEGER, manager_id INTEGER, email TEXT,
            hire_date TEXT, position TEXT, status TEXT, country TEXT
        )
    ''')

    cursor.executemany('INSERT INTO departments (id, department_name) VALUES (?, ?)', [
        (1, 'HR'), (2, 'IT'), (3, 'Finance')
    ])

    cursor.executemany('''
        INSERT INTO employees
        (id, first_name, age, salary, department_id, manager_id, email,
         hire_date, position, status, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [
        (101, 'Alice', 30, 70000, 1, None, 'alice@example.com', '2021-01-01', 'Analyst', 'Active', 'India'),
        (102, 'Bob', 45, 80000, 2, 101, 'bob@example.com', '2020-05-15', 'Manager', 'Active', 'USA'),
        (103, 'Charlie', 28, 60000, 2, 102, 'charlie@example.com', '2023-08-20', 'Developer', 'Inactive', 'India'),
        (104, 'David', 33, 50000, None, 103, None, '2022-11-10', 'HR Assistant', 'Cancelled', 'India')
    ])
    conn.commit()

init_db()

queries = [
    ("1. Basic SELECT", "SELECT first_name, salary FROM employees"),
    ("2. WHERE Clause", "SELECT * FROM employees WHERE age > 30"),
    ("3. DISTINCT", "SELECT DISTINCT country FROM employees"),
    ("4. ORDER BY", "SELECT first_name, salary FROM employees ORDER BY salary DESC"),
    ("5. LIMIT", "SELECT * FROM employees LIMIT 2"),
    ("6. LIKE", "SELECT first_name FROM employees WHERE first_name LIKE 'A%'"),
    ("7. IN", "SELECT * FROM employees WHERE department_id IN (1, 2)"),
    ("8. BETWEEN", "SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2023-12-31'"),
    ("9. Top-N Queries", "SELECT first_name, salary FROM employees ORDER BY salary DESC LIMIT 3"),
    ("10. Pagination", "SELECT * FROM employees ORDER BY hire_date LIMIT 3 OFFSET 1"),
    
    ("11. COUNT", "SELECT COUNT(*) FROM employees WHERE department_id = 2"),
    ("12. SUM", "SELECT SUM(salary) FROM employees"),
    ("13. AVG", "SELECT AVG(salary) FROM employees WHERE department_id = 2"),
    ("14. MIN / MAX", "SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees"),
    ("15. GROUP BY", "SELECT department_id, COUNT(*) FROM employees GROUP BY department_id"),
    ("16. HAVING", "SELECT department_id, AVG(salary) FROM employees GROUP BY department_id HAVING AVG(salary) > 60000"),
    ("17. STRING_AGG (grouped names)", "SELECT department_id, GROUP_CONCAT(first_name, ', ') AS names FROM employees GROUP BY department_id"),
    
    ("18. INNER JOIN", "SELECT e.first_name, d.department_name FROM employees e INNER JOIN departments d ON e.department_id = d.id"),
    ("19. LEFT JOIN", "SELECT e.first_name, d.department_name FROM employees e LEFT JOIN departments d ON e.department_id = d.id"),
    ("20. RIGHT JOIN (Simulated using LEFT JOIN)", "SELECT d.department_name, e.first_name FROM departments d LEFT JOIN employees e ON d.id = e.department_id"),
    ("21. SELF JOIN", "SELECT e1.first_name AS employee, e2.first_name AS manager FROM employees e1 JOIN employees e2 ON e1.manager_id = e2.id"),
    ("22. CROSS JOIN", "SELECT e.first_name, d.department_name FROM employees e CROSS JOIN departments d"),
    
    ("23. CASE Statement", "SELECT first_name, salary, CASE WHEN salary > 70000 THEN 'High' ELSE 'Standard' END AS salary_level FROM employees"),
    ("24. SUBQUERY", "SELECT * FROM employees WHERE department_id = (SELECT id FROM departments WHERE department_name = 'IT')"),
    
    ("25. WINDOW Function: RANK", "SELECT first_name, salary, department_id, RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank FROM employees"),
    ("26. ROW_NUMBER", "SELECT ROW_NUMBER() OVER (ORDER BY hire_date) AS row_num, first_name, hire_date FROM employees"),
    ("27. PARTITION BY + SUM", "SELECT department_id, first_name, salary, SUM(salary) OVER (PARTITION BY department_id) AS dept_total FROM employees"),
    
    ("28. WITH CTE", "WITH high_earners AS (SELECT * FROM employees WHERE salary > 60000) SELECT * FROM high_earners WHERE department_id = 2"),
    ("29. PIVOT (Simulated)", "SELECT department_id, SUM(CASE WHEN strftime('%Y', hire_date) = '2021' THEN salary END) AS salary_2021, SUM(CASE WHEN strftime('%Y', hire_date) = '2022' THEN salary END) AS salary_2022 FROM employees GROUP BY department_id"),
    
    ("30. UNION", "SELECT first_name FROM employees UNION SELECT department_name FROM departments"),
    
    ("31. INSERT", "INSERT INTO employees (id, first_name, age, salary, department_id, manager_id, email, hire_date, position, status, country) VALUES (105, 'Eva', 29, 65000, 1, 101, 'eva@example.com', '2024-01-10', 'HR Assistant', 'Active', 'India')"),
    ("32. BULK INSERT", "INSERT INTO departments (id, department_name) VALUES (4, 'Sales'), (5, 'Marketing')"),
    ("33. UPDATE", "UPDATE employees SET salary = salary * 1.10 WHERE department_id = 1"),
    ("34. DELETE", "DELETE FROM employees WHERE status = 'Cancelled' AND hire_date < '2022-01-01'"),
    
    ("35. TRANSACTION", "BEGIN TRANSACTION; UPDATE employees SET salary = salary - 1000 WHERE id = 101; UPDATE employees SET salary = salary + 1000 WHERE id = 102; COMMIT;"),
    
    ("36. CREATE TABLE", "CREATE TABLE projects (id INTEGER PRIMARY KEY, project_name TEXT, start_date TEXT)"),
    ("37. CREATE INDEX", "CREATE INDEX idx_email ON employees(email)"),
    ("38. CREATE VIEW", "CREATE VIEW active_employees AS SELECT * FROM employees WHERE status = 'Active'"),
    ("39. STORED PROCEDURE (Simulated)", "-- SQLite doesn't support SPs natively, but this would be valid in other DBs:\n-- CREATE PROCEDURE GetHighEarners()\n-- AS\n-- SELECT * FROM employees WHERE salary > 75000"),
    
    ("40. NULL Handling", "SELECT first_name FROM employees WHERE email IS NULL"),
    ("41. COALESCE", "SELECT first_name, COALESCE(email, 'No Email') AS contact_email FROM employees"),
    ("42. DATE Functions", "SELECT first_name, DATE(hire_date, '+5 days') AS adjusted_date FROM employees"),
    ("43. Duplicate Detection", "SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*) > 1")
]

@csrf_exempt
def query_view(request):
    query_blocks = []

    for idx, (title, default_query) in enumerate(queries):
        result_html = ""
        query = request.POST.get(f"query_{idx}", default_query)

        if request.method == "POST" and f"run_{idx}" in request.POST:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                headers = [desc[0] for desc in cursor.description] if cursor.description else []

                result_html += "<table><tr>"
                for h in headers:
                    result_html += f"<th>{h}</th>"
                result_html += "</tr>"
                for row in rows:
                    result_html += "<tr>" + "".join(f"<td>{row[col]}</td>" for col in headers) + "</tr>"
                result_html += "</table>"
            except Exception as e:
                result_html = f"<div class='error'>Error: {e}</div>"

        query_blocks.append((idx, title, query, result_html))

    # Load template from file directly
    html_path = os.path.join(os.path.dirname(__file__), '..', 'ui.html')
    with open(html_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    context = Context({"query_blocks": query_blocks})
    return HttpResponse(template.render(context))
