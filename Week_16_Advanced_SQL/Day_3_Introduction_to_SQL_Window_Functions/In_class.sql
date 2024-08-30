CREATE TABLE new_employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);

CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO new_employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200);

-- Demonstration 1: Combining RANK() and DENSE_RANK()

SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS sales_rank,
       DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS dense_sales_rank
FROM new_employees e
JOIN sales_data s ON e.employee_id = s.employee_id;

-- Demonstration 2: Using NTILE() for Quartile Distribution

SELECT employee_id, first_name, last_name, department_id, salary,
       NTILE(4) OVER (PARTITION BY department_id ORDER BY salary DESC) AS salary_quartile
FROM new_employees;

-- Demonstration 3: Advanced Running Total with PARTITION BY and ORDER BY

SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       SUM(s.sales) OVER (PARTITION BY e.department_id ORDER BY e.employee_id) AS running_total
FROM new_employees e
JOIN sales_data s ON e.employee_id = s.employee_id;

-- Exercise 1: Employee Salaries

-- 1. Task: Use the ROW_NUMBER() function to list employees in each department, ordered by their salary in descending order. Display the department, employee name, and their salary rank within the department.

SELECT 
    d.department_name,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.salary,
    ROW_NUMBER() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS salary_rank
FROM 
    new_employees e
JOIN 
    departments d ON e.department_id = d.department_id
ORDER BY 
    d.department_name, salary_rank;

-- 2. Task: Calculate the cumulative salary for employees in each department using the SUM() function with windowing.

SELECT 
    d.department_name,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.salary,
    SUM(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS cumulative_salary
FROM 
    new_employees e
JOIN 
    departments d ON e.department_id = d.department_id
ORDER BY 
    d.department_name, cumulative_salary DESC;

--Exercise 2: Sales Performance

-- 1. Task: Rank the sales performance of employees within each department using the DENSE_RANK() function. Display the department, employee name, and their sales rank.

SELECT 
    d.department_name,
    e.first_name || ' ' || e.last_name AS employee_name,
    e.sales_amount,  -- Assuming 'sales_amount' represents the sales performance metric
    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.sales_amount DESC) AS sales_rank
FROM 
    new_employees e
JOIN 
    departments d ON e.department_id = d.department_id
ORDER BY 
    d.department_name, sales_rank;

-- 2. Task: Calculate the total sales for each employee and the running total of sales across all employees using the SUM() function with windowing.
SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       SUM(s.sales) OVER (PARTITION BY e.department_id ORDER BY e.employee_id) AS running_total
FROM new_employees e
JOIN sales_data s ON e.employee_id = s.employee_id;

