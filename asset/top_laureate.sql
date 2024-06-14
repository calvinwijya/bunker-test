WITH top_laureate AS (
    SELECT laureate_id, category, COUNT(*) AS total_awards
    FROM prize_laureates
    GROUP BY laureate_id, category
    ORDER BY total_awards DESC
    LIMIT 1
)
    
SELECT DISTINCT l.id, l.full_name, tl.total_awards, tl.category
FROM top_laureate tl
LEFT JOIN laureates l ON tl.laureate_id = l.id;