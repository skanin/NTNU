SELECT SubjectNo, Name, COUNT(*) AS 'Number of A'
FROM Exam NATURAL JOIN Subject NATURAL JOIN ExamRegistration
WHERE grade = 'A'
AND Year = 2014
GROUP BY SubjectNo, Name
ORDER BY COUNT(*) DESC;