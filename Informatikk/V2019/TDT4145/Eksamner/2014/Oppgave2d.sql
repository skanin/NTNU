SELECT City, COUNT(*) AS 'Antall Abonnenter'
FROM Subscriber WHERE ID IN (SELECT SubscriberID
							 FROM PhoneNumber)
GROUP BY City
ORDER BY COUNT(*) DESC;