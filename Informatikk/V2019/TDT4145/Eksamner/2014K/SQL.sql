--Oppgave 2d
SELECT DISTINCT SubjectNo, Name
FROM Subject NATURAL JOIN Exam
WHERE Year = 2014
ORDER BY SubjectNo ASC;

--Oppgave 2e
SELECT SubjectNo, Name, COUNT(grade) AS "Number of A"
FROM Exam NATURAL JOIN ExamRegistration
WHERE grade = "A" AND SubjectNo in (SELECT SubjectNo
									FROM Exam
									WHERE Year = 2014)
GROUP BY SubjectNo, Name
HAVING grade = 'A'
ORDER BY COUNT(*) DESC;