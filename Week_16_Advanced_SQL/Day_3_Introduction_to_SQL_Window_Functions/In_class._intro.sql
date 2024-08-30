-- 1. The ROW_NUMBER() function assigns a unique number to each row within a partition of a result set, starting at 1 for the first row in each partition. Think of it as giving a unique serial number to each row.

SELECT employee_id, first_name, last_name,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
FROM employees;

-- Explanation:
-- ROW_NUMBER(): Assigns a unique sequential integer to rows within each partition.
-- PARTITION BY: Divides the rows by department.
-- ORDER BY: Orders rows within each partition by salary in descending order.

-- 2. The RANK() function assigns a rank to each row within a partition of a result set. If two rows have the same value, they receive the same rank, and the next rank(s) are skipped.

SELECT employee_id, first_name, last_name, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
FROM employees;

-- Explanation:
-- RANK(): Assigns ranks to rows within each partition, allowing ties.
-- PARTITION BY: Divides the rows by department.
-- ORDER BY: Orders rows within each partition by salary in descending order.

-- 3. The DENSE_RANK() function is similar to RANK(), but it does not skip any ranks after ties.

SELECT employee_id, first_name, last_name, salary,
       DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Explanation:
-- DENSE_RANK(): Assigns ranks to rows within each partition, without gaps.
-- PARTITION BY: Divides the rows by department.
-- ORDER BY: Orders rows within each partition by salary in descending order.

-- 4. The NTILE() function distributes rows into a specified number of approximately equal groups. It assigns a number to each row indicating the group to which it belongs.

SELECT employee_id, first_name, last_name, salary,
       NTILE(4) OVER (PARTITION BY department_id ORDER BY salary DESC) AS quartile
FROM employees;

-- Explanation:
-- NTILE(4): Divides rows into 4 groups.
-- PARTITION BY: Divides the rows by department.
-- ORDER BY: Orders rows within each partition by salary in descending order.

