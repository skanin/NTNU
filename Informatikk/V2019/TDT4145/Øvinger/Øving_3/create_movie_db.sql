USE film;

CREATE TABLE regissør(
		regissørID INTEGER NOT NULL,
        navn VARCHAR(255),
        CONSTRAINT regissør_PK PRIMARY KEY (regissørID)
);

CREATE TABLE film (
    filmID INTEGER NOT NULL,
    title VARCHAR(30),
    prodaar INTEGER,
    regissorID INTEGER NOT NULL,
    CONSTRAINT film_PK PRIMARY KEY (filmID),
    CONSTRAINT film_FK FOREIGN KEY (regissorID)
        REFERENCES regissør (regissørID),
    CONSTRAINT aarsjekk CHECK (prodaar < YEAR(GETDATE()))
);

CREATE TABLE sjanger (
		sjangerID INTEGER NOT NULL,
        navn VARCHAR(20) NOT NULL,
        beskrivelse VARCHAR(255),
        CONSTRAINT sjanger_PK PRIMARY KEY (sjangerID)
);

CREATE TABLE sjangerforfilm (
		filmID INTEGER NOT NULL,
        sjangerID INTEGER NOT NULL,
        CONSTRAINT sjangerforfilm_PK PRIMARY KEY (filmID, sjangerID),
        CONSTRAINT sjangerforfilm_FK1 FOREIGN KEY (filmID) REFERENCES film (filmID) ON DELETE CASCADE,
        CONSTRAINT sjangerforfilm_FK2 FOREIGN KEY (sjangerID) REFERENCES sjanger (sjangerID)
);

CREATE TABLE skuespiller (
		skuespillerID INTEGER NOT NULL,
        navn VARCHAR(255),
        faar INTEGER NOT NULL,
        CONSTRAINT skuespiller_PK PRIMARY KEY (skuespillerID),
        CONSTRAINT aarsjekk CHECK (faar < YEAR(getdate()))
);

CREATE TABLE skuespillerifIlm (
		filmID INTEGER NOT NULL,
        skuespillerID INTEGER NOT NULL,
        CONSTRAINT skuespillerifilm_PK PRIMARY KEY (filmID, skuespillerID),
        CONSTRAINT skuespillerifilm_FK1 FOREIGN KEY (filmID) REFERENCES film (filmID) ON DELETE CASCADE,
        CONSTRAINT skuespillerifilm_FK2 FOREIGN KEY (skuespillerID) REFERENCES skuespiller (skuespillerID)
);
