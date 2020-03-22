DROP TABLE IF EXISTS Regissør;
DROP TABLE IF EXISTS SjangerForFilm;
DROP TABLE IF EXISTS Sjanger;
DROP TABLE IF EXISTS Skuespiller;
DROP TABLE IF EXISTS SkuespillerIFilm;
DROP TABLE IF EXISTS Movie;



CREATE TABLE Regissør(
	RegissørID 	Integer NOT NULL,
	Navn 		VARCHAR(255) NOT NULL,

	PRIMARY KEY (RegissørID),
);

CREATE TABLE Skuespiller(
	SkuespillerID	Integer NOT NULL,
	Navn			VARCHAR(255) NOT NULL,
	Fødselsår		VARCHAR(10) NOT NULL,

	PRIMARY	KEY (SkuespillerID)
);

CREATE TABLE Sjanger(
	SjangerID	Integer NOT NULL,
	Navn		VARCHAR(255) NOT NULL,
	Beskrivelse	VARCHAR(255) NOT NULL,

	PRIMARY KEY (SjangerID)
);

CREATE TABLE Movie(
	MovieID			Integer NOT NULL,
	Title			VARCHAR(255) NOT NULL,
	Produksjonsår	Integer NOT NULL,
	RegissørID		Integer NOT NULL,

	PRIMARY KEY (MovieID),
	FOREIGN KEY (RegissørID) REFERENCES Regissør(RegissørID)
);

CREATE TABLE SjangerForFilm(
	SjangerID 	Integer NOT NULL,
	FilmID		Integer NOT NULL,

	FOREIGN KEY (FilmID) REFERENCES Movie(MovieID) ON DELETE CASCADE,
	FOREIGN KEY (SjangerID) REFERENCES Sjanger(SjangerID) ON DELETE CASCADE
);

CREATE TABLE SkuespillerIFilm(
	FilmID			Integer NOT NULL,
	SkuespillerID 	Integer NOT NULL,
	Rolle			VARCHAR(255) NOT NULL,

	FOREIGN KEY (FilmID) REFERENCES Movie(MovieID) ON DELETE CASCADE,
	FOREIGN KEY	(SkuespillerID) REFERENCES Skuespiller(SkuespillerID) ON DELETE CASCADE
);

