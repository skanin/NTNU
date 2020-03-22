SELECT film.title, AVG(skuespiller.faar) AS Average_age_movie
FROM film JOIN skuespillerifilm ON skuespillerifilm.filmID = film.filmID
JOIN skuespiller ON skuespiller.skuespillerID = skuespillerifilm.skuespillerID
GROUP BY film.filmID
HAVING Average_age_movie > 
(SELECT AVG(skuespiller.faar) FROM film JOIN skuespillerifilm ON skuespillerifilm.filmID = film.filmID
JOIN skuespiller ON skuespiller.skuespillerID = skuespillerifilm.skuespillerID);