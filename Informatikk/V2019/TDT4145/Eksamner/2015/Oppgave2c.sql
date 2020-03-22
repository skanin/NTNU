SELECT SNo, Name, Email
FROM Student WHERE NOT EXISTS(SELECT * 
							  FROM Student JOIN ExamRegistration
							  ON SNo = StudentNo
							  WHERE RYear = 2015);