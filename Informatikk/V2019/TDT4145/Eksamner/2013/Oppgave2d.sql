SELECT PhotoID, Title
FROM Photo
WHERE PhotoID NOT IN (SELECT PhotoID
					  FROM KeyWordPhoto);