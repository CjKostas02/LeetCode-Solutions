# Time:  O(nlogn)
# Space: O(n)

# line sweep
WITH events_cte AS (
    SELECT employee_id,
           start_time AS event_time,
           +1 as event_type
    FROM EmployeeShifts
    UNION ALL
    SELECT employee_id,
           end_time AS event_time,
           -1 as event_type
    FROM EmployeeShifts
    ORDER BY 1, 2, 3
), line_sweep_cte AS (
    SELECT employee_id,
           event_type,
           CASE WHEN @event_count = 0 THEN @start_time := event_time
                ELSE @start_time END AS start_time,
           @event_count := @event_count + event_type AS event_count,
           CASE WHEN @event_count = 0 THEN event_time
                ELSE @start_time END AS end_time
    FROM events_cte, (SELECT @event_count := 0, @start_time := 0) init
), result_cte AS (
    SELECT employee_id,
       SUM(event_count) AS overlapping_shifts
    FROM line_sweep_cte
    WHERE event_type = -1
    GROUP BY 1
    ORDER BY NULL
)

SELECT *
FROM result_cte
WHERE overlapping_shifts != 0
ORDER BY 1;

# Time:  O(n^2)
# Space: O(n^2)
WITH cte AS (
    SELECT e1.employee_id
    FROM EmployeeShifts e1
    INNER JOIN EmployeeShifts e2
        ON e1.employee_id = e2.employee_id
    WHERE e1.start_time < e2.start_time
      AND e1.end_time > e2.start_time
)

SELECT employee_id,
       COUNT(*) AS overlapping_shifts
FROM cte
GROUP BY 1
ORDER BY 1;
