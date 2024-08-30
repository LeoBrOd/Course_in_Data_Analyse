CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location_id INT
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    city VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO departments (department_id, department_name, location_id) VALUES
(1, 'HR', 100),
(2, 'Finance', 200),
(3, 'IT', 300),
(4, 'Marketing', 400),
(5, 'Sales', 500);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO locations (location_id, city, country) VALUES
(100, 'New York', 'USA'),
(200, 'London', 'UK'),
(300, 'San Francisco', 'USA'),
(400, 'Berlin', 'Germany'),
(500, 'Paris', 'France');

-- Demonstration 1: Complex Subqueries
-- Using subqueries to find employees in departments with average salary above a certain threshold.

SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM employees e
WHERE e.department_id IN (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) > 70000
);

-- Demonstration 2: Subqueries with EXISTS
-- Using the EXISTS operator to find employees who work in locations with specific criteria.

SELECT first_name, last_name
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    JOIN locations l ON d.location_id = l.location_id
    WHERE e.department_id = d.department_id
    AND l.city = 'London'
);

-- Demonstration 3: Nested Subqueries in FROM Clause
-- Using nested subqueries to find top earners in each department.

SELECT d.department_name, e.first_name, e.last_name, e.salary
FROM (
    SELECT department_id, MAX(salary) AS max_salary
    FROM employees
    GROUP BY department_id
) m
JOIN employees e ON e.department_id = m.department_id AND e.salary = m.max_salary
JOIN departments d ON e.department_id = d.department_id;

--! doesn`t work in this file
-- Filtering Based on Subqueries
-- In a sales database, you might want to find salespeople who have made more than 10 sales in a specific month.

SELECT salesperson_id, first_name, last_name
FROM salespeople
WHERE salesperson_id IN (
    SELECT salesperson_id
    FROM sales
    WHERE sale_date BETWEEN '2024-05-01' AND '2024-05-31'
    GROUP BY salesperson_id
    HAVING COUNT(sale_id) > 10
);

--! doesn`t work in this file
-- Subqueries for Data Validation
-- Ensuring that all employees assigned to a project have valid email addresses

SELECT project_id, project_name
FROM projects
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    JOIN project_assignments pa ON e.employee_id = pa.employee_id
    WHERE pa.project_id = projects.project_id
    AND e.email IS NULL
);

-- Exercise 1: Advanced Single-row Subquery
-- Task: Find the employee details who have the highest salary in each department.

SELECT e.employee_id, e. first_name, e. last_name, e.department_id, e.salary 
FROM employees e 
WHERE e. salary = ( 
	SELECT MAX (e2. salary) 
	FROM employees e2 
	WHERE e2.department_id = e.department_id
);

-- Exercise 2: Complex Multiple-row Subquery
-- Task: List the employees who work in departments located in either New York or London.

SELECT e. employee_id, e. first_name, e. last_name, e.department_id, e.salary 
FROM employees e 
WHERE e. department_id IN ( 
	SELECT d.department_id 
	FROM departments d 
	JOIN locations l ON d.location_id = l.location_id
	WHERE l.city IN ( 'New York', 'London')
)

-- Exercise 3: Correlated Subquery for Performance Analysis
-- Task: Find employees whose salary is above the departmental average, but only for departments located in the USA.

SELECT e.employee_id, e.first_name, e.last_name, e.salary, e.department_id, l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.country = 'USA'
  AND e.salary > (
      SELECT AVG(e.salary)
      FROM employees e
      WHERE e.department_id = e.department_id
  );