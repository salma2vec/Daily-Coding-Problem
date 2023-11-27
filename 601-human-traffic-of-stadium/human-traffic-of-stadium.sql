# Write your MySQL query statement below

WITH CTE AS (
		SELECT
			*,
			 id - ROW_NUMBER() OVER(ORDER BY visit_date) Diff
		FROM
			Stadium
		WHERE
			people >= 100
    )
,CTE2 AS (
	SELECT
		Diff,
		COUNT(Diff) AS DiffCounted
	FROM
		CTE
	GROUP BY 
		Diff
	HAVING COUNT(Diff) > 2
    )
SELECT
	id,
    visit_date,
    people
FROM
	CTE 
WHERE
	Diff IN (
		SELECT Diff FROM CTE2
    )
ORDER BY
	visit_date ASC