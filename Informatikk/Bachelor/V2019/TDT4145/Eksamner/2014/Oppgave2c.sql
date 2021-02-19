SELECT PNumber
FROM Subscriber JOIN PhoneNumber on ID = SubscriberID
WHERE Address LIKE "Buckhaugen%" AND City = "Trondheim";