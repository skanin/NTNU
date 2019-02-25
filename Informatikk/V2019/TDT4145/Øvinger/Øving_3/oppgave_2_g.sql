SELECT DISTINCT sjanger.navn, COUNT(film.filmID)
FROM sjangerforfilm JOIN film ON sjangerforfilm.filmID = film.filmID 
JOIN sjanger ON sjangerforfilm.sjangerID = sjanger.sjangerID
GROUP BY sjanger.navn; 