SELECT Grade, COUNT(*)
FROM Course JOIN Exam ON CID = CourseID
			JOIN ExamResult ON Eno = ExamNo
WHERE CCode = 'TDT4145' AND EDay = 1 AND Emonth = 6 AND Year = 2015
GROUP BY Grade
ORDER BY Grade ASC;
