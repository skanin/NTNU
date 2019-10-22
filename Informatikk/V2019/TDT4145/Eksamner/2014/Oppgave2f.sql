SELECT PNumber, SubscriberID, Name, Address
FROM PhoneNumber JOIN Subscriber ON ID = SubscriberID
WHERE Pnumber NOT IN (SELECT FromNo
					  FROM PhoneCall
					  WHERE CYear = 2014)
ORDER BY SubscriberID ASC, PNumber ASC;