# 1148-article-views-i

SELECT DISTINCT(author_id) AS id
FROM Views 
WHERE author_id = viewer_id
ORDER BY author_id ASC;