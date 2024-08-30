-- Exercise 1: Complex Subquery Analysis

-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.

SELECT m.medal_name, AVG(gc.age) AS average_age
FROM olympics.medal m
JOIN olympics.competitor_event ce ON m.id = ce.medal_id
JOIN olympics.games_competitor gc ON ce.competitor_id = gc.person_id
WHERE 
    EXISTS (
        SELECT 1 
        FROM olympics.competitor_event ce2 
        WHERE ce2.competitor_id = gc.person_id 
        AND ce2.medal_id = m.id
    )
GROUP BY m.medal_name;

-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

SELECT nr.region_name, COUNT(DISTINCT gc.person_id) AS unique_competitors
FROM olympics.person_region pr
JOIN olympics.noc_region nr ON pr.region_id = nr.id
JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
WHERE gc.person_id IN (
        SELECT ce2.competitor_id
        FROM olympics.competitor_event ce2
        GROUP BY ce2.competitor_id
        HAVING COUNT(DISTINCT ce2.event_id) > 3
    )
GROUP BY nr.region_name
ORDER BY unique_competitors DESC LIMIT 5;

-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

CREATE TEMPORARY TABLE competitor_medal_count AS
SELECT ce.competitor_id, COUNT(ce.medal_id) AS total_medals
FROM olympics.competitor_event ce WHERE ce.medal_id IS NOT NULL GROUP BY ce.competitor_id;

SELECT cmc.competitor_id, cmc.total_medals FROM competitor_medal_count cmc WHERE cmc.total_medals > 2;

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.

select * from competitor_medal_count where total_medals <1
-- We dont have competitors like this

DELETE FROM competitor_medal_count
WHERE competitor_id IN (
	SELECT cmc.competitor_id FROM competitor_medal_count cmc
    LEFT JOIN olympics.competitor_event ce ON cmc.competitor_id = ce.competitor_id
    WHERE ce.medal_id IS NULL);

-- Exercise 2: Advanced Data Manipulation and Optimization

-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

UPDATE olympics.person p 
	SET height =(
		SELECT AVG(p.height) FROM olympics.person p 
		JOIN olympics.person_region pr ON pr.person_id= p.id
		JOIN olympics.noc_region nr ON pr.region_id= nr.id)
WHERE p.height IS NULL OR p.height = 0;

SELECT * FROM olympics.person p WHERE height = 0

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.

-- Doesn`t work for me
SELECT gc.person_id, gc.games_id, COUNT(ce.event_id) AS total_events
FROM olympics.games_competitor gc
JOIN  olympics.competitor_event ce ON gc.person_id = ce.competitor_id AND gc.games_id = ce.event_id
WHERE gc.person_id IN (
        SELECT ce2.competitor_id FROM olympics.competitor_event ce2
        GROUP BY ce2.competitor_id, ce2.event_id
        HAVING COUNT(DISTINCT ce2.event_id) > 1)
GROUP BY 
    gc.person_id, gc.games_id;

-- !! Even this part gives 0 values !!
SELECT ce2.competitor_id FROM olympics.competitor_event ce2
        GROUP BY ce2.competitor_id, ce2.event_id
        HAVING COUNT(DISTINCT ce2.event_id) > 1

-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.
	
CREATE TEMPORARY TABLE avg_medals_per_region AS
SELECT region_id, nr.region_name, AVG(medal_count) AS avg_medals_per_competitor
FROM ( SELECT gc.person_id, pr.region_id,  COUNT(ce.medal_id) AS medal_count
FROM olympics.games_competitor gc
JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
JOIN olympics.person_region pr ON gc.person_id = pr.person_id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id, pr.region_id) subquery 
JOIN olympics.noc_region nr ON subquery.region_id = nr.id
GROUP BY region_id, nr.region_name;

SELECT region_name, avg_medals_per_competitor FROM avg_medals_per_region
WHERE avg_medals_per_competitor > (SELECT AVG(avg_medals_per_competitor) FROM avg_medals_per_region)

-- Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.

CREATE TEMPORARY TABLE season_participation AS
SELECT pr.person_id, p.full_name, g.season
FROM olympics.person_region pr
JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
JOIN olympics.games g ON gc.games_id = g.id
JOIN olympics.person p ON pr.person_id = p.id
GROUP BY pr.person_id, p.full_name, g.season;

SELECT csp.full_name FROM  season_participation csp
GROUP BY csp.full_name HAVING COUNT(DISTINCT csp.season) = 2;
