SELECT skuespiller.navn
FROM skuespiller JOIN skuespillerifilm ON skuespiller.skuespillerID = skuespillerifilm.skuespillerID
JOIN film ON film.filmID = skuespillerifilm.filmID
WHERE film.title = "Ace Ventura: Pet Detective" 
AND skuespiller.skuespillerID NOT IN (
SELECT skuespiller.skuespillerID
FROM skuespiller JOIN skuespillerifilm ON skuespiller.skuespillerID = skuespillerifilm.skuespillerID
JOIN film ON film.filmID = skuespillerifilm.filmID
WHERE film.title = "Ace Ventura: When Nature Calls"
);