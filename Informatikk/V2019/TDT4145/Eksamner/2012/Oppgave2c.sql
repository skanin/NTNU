SELECT SID, Navn, FødselsÅr
FROM SkøyteLøper NATURAL JOIN Passeringer NATURAL JOIN SkøyteLøp
WHERE SID NOT IN (SELECT SID
				  FROM Passeringer NATURAL JOIN SkøyteLøp
				  WHERE Distanse = 5000
				  AND RundeTid >= 30)
AND Distanse = 5000;