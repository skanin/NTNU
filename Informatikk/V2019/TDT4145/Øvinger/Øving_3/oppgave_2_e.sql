SELECT DISTINCT  title FROM film JOIN regissør ON film.regissorID = regissør.regissørID JOIN skuespillerifIlm 
ON film.filmID = skuespillerifilm.filmID JOIN skuespiller ON skuespillerifilm.skuespillerID = skuespiller.skuespillerID
WHERE skuespiller.navn = regissør.navn;