-- Exercise 1: Detailed Medal Analysis

-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. 
-- Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.

CREATE TEMPORARY TABLE competitor_medal_season AS
SELECT pr.person_id, p.full_name, g.season, COUNT(ce.medal_id) AS medal_count
FROM olympics.person_region pr
JOIN olympics.games_competitor gc ON pr.person_id = gc.person_id
JOIN olympics.games g ON gc.games_id = g.id
JOIN olympics.person p ON pr.person_id = p.id
JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
GROUP BY pr.person_id, p.full_name, g.season;


SELECT cms.full_name, cms.medal_count FROM  competitor_medal_season cms
GROUP BY cms.full_name, cms.medal_count HAVING (COUNT(DISTINCT cms.season) = 2 AND medal_count >0);

-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports,
-- and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.

CREATE TEMPORARY TABLE competitor_two_sports_medals AS
SELECT gc.person_id, COUNT( DISTINCT e.sport_id) AS sports_count, SUM(ce.medal_id) AS total_medals
FROM olympics.games_competitor gc
JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
JOIN olympics.event e ON e.id=ce.event_id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT person_id, total_medals FROM competitor_two_sports_medals
ORDER BY total_medals DESC LIMIT 3;

-- Exercise 2: Region and Competitor Performance

-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.

WITH competitor_medal_counts AS (
    SELECT gc.person_id, ce.event_id, pr.region_id, COUNT(ce.medal_id) AS medal_count
    FROM olympics.games_competitor gc
    JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
    JOIN olympics.person_region pr ON gc.person_id = pr.person_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY gc.person_id, ce.event_id, pr.region_id
)SELECT person_id, event_id, region_id, medal_count
INTO TEMPORARY TABLE max_medals_per_event
FROM competitor_medal_counts
WHERE medal_count = (
	SELECT MAX(medal_count)
	FROM competitor_medal_counts cmc
	WHERE cmc.person_id = competitor_medal_counts.person_id);

SELECT nr.region_name, SUM(mme.medal_count) AS total_medals
FROM max_medals_per_event mme
JOIN olympics.noc_region nr ON mme.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals.
-- Retrieve and display the contents of this table, including their full names and the number of games they participated in.

CREATE TEMPORARY TABLE competitors_no_medals AS 
SELECT gc.person_id,  p.full_name, COUNT(DISTINCT gc.games_id) AS games_participated
FROM olympics.games_competitor gc
JOIN olympics.person p ON gc.person_id = p.id
LEFT JOIN olympics.competitor_event ce ON gc.person_id = ce.competitor_id
WHERE ce.medal_id IS NULL
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3;

SELECT * FROM competitors_no_medals;
-- empty