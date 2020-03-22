--Oppgave 2c
SELECT PNumber
FROM Subscriber JOIN PhoneNumber on ID = SubscriberID
WHERE Address LIKE "Bluckhaugen %";

--Oppgave 2d
SELECT city, COUNT(*) as "Antall Abonnenter"
FROM Subscriber
GROUP BY city
ORDER BY COUNT(*) DESC;

--Oppgave 2e
UPDATE Subscriber
SET Address = "Bluckhaugen 99", PostalCode = 7046, city = Trondheim
WHERE ID = 100;

--Oppgave 2f
SELECT PNumber, ID, Name, Address
FROM Subscriber JOIN PhoneNumber ON ID = SubscriberID
WHERE PNumber NOT IN (SELECT PNumber
FROM PhoneNumber JOIN PhoneCall ON FromNo = PNumber
WHERE CYear = 2015)
ORDER BY ID ASC, PNumber ASC;