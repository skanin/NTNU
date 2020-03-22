DROP TABLE IF EXISTS BrukerApparat;
DROP TABLE IF EXISTS Apparat;
DROP TABLE IF EXISTS HarOvelse;
DROP TABLE IF EXISTS HarTime;
DROP TABLE IF EXISTS OvelseITreningsokt;
DROP TABLE IF EXISTS InngaarI;
DROP TABLE IF EXISTS OvelsesGruppe;
DROP TABLE IF EXISTS Gruppetime;
DROP TABLE IF EXISTS Ovelse;
DROP TABLE IF EXISTS Treningsokt;


CREATE TABLE Treningsokt (
	treningsoktID INTEGER NOT NULL,
    dato DATE NOT NULL,
    tidspunkt TIME NOT NULL,
    varighet INTEGER NOT NULL CHECK (varighet > 0),
    personligForm INTEGER CHECK (personligForm > 0 and personligForm < 11),
    notat VARCHAR(255),
    CONSTRAINT treningsokt_PK PRIMARY KEY (treningsoktID)
);

CREATE TABLE Ovelse (
	ovelseID INTEGER NOT NULL,
    navn VARCHAR(45) NOT NULL,
    beskrivelse VARCHAR(255),
    CONSTRAINT ovelse_PK PRIMARY KEY (ovelseID)
);

CREATE TABLE Apparat (
	apparatID INTEGER NOT NULL,
    navn VARCHAR(45) NOT NULL,
    beskrivelse VARCHAR(255) NOT NULL,
    CONSTRAINT apparat_PK PRIMARY KEY (apparatID)
);

CREATE TABLE OvelsesGruppe (
	ovelsesGruppeID INTEGER NOT NULL,
    kategori VARCHAR(45) NOT NULL,
    CONSTRAINT ovelsesGruppe_PK PRIMARY KEY (ovelsesGruppeID)
);

CREATE TABLE Gruppetime (
	gruppetimeID INTEGER NOT NULL,
    navn VARCHAR(45) NOT NULL,
    beskrivelse VARCHAR(255) NOT NULL,
    CONSTRAINT gruppetime_PK PRIMARY KEY (gruppetimeID)
);

CREATE TABLE OvelseITreningsokt (
	treningsoktID INTEGER NOT NULL,
    ovelseID INTEGER NOT NULL,
    prestasjon INTEGER CHECK(prestasjon > 0 and prestasjon < 11),
    CONSTRAINT OvelseITreningsokt_PK PRIMARY KEY (treningsoktID, ovelseID),
    CONSTRAINT OvelseITreningsokt_FK FOREIGN KEY (treningsoktID) 
		REFERENCES Treningsokt (treningsoktID) ON DELETE CASCADE,
	CONSTRAINT OvelseITreningsokt_FK2 FOREIGN KEY (ovelseID) 
		REFERENCES Ovelse (ovelseID) ON DELETE CASCADE
);

CREATE TABLE InngaarI (
	gruppeID INTEGER NOT NULL,
    ovelseID INTEGER NOT NULL,
    CONSTRAINT InngaarI_PK PRIMARY KEY (gruppeID, ovelseID),
    CONSTRAINT InngaarI_FK FOREIGN KEY (gruppeID) 
		REFERENCES OvelsesGruppe (ovelsesGruppeID) ON DELETE CASCADE,
	CONSTRAINT InngaarI_FK2 FOREIGN KEY (ovelseID) 
		REFERENCES Ovelse (ovelseID) ON DELETE CASCADE
);

CREATE TABLE BrukerApparat (
	apparatID INTEGER NOT NULL,
    ovelseID INTEGER NOT NULL,
    kilo INTEGER NOT NULL,
    sett INTEGER NOT NULL,
    CONSTRAINT BrukerApparat_PK PRIMARY KEY (apparatID, ovelseID),
    CONSTRAINT BrukerApparat_FK FOREIGN KEY (apparatID) 
		REFERENCES Apparat (apparatID) ON DELETE CASCADE,
	CONSTRAINT BrukerApparat_FK2 FOREIGN KEY (ovelseID) 
		REFERENCES Ovelse (ovelseID) ON DELETE CASCADE
);

CREATE TABLE HarTime (
	treningsoktID INTEGER NOT NULL,
    gruppetimeID INTEGER NOT NULL,
    prestasjon INTEGER,
    CONSTRAINT HarTime_PK PRIMARY KEY (treningsoktID, gruppetimeID),
    CONSTRAINT HarTime_FK FOREIGN KEY (treningsoktID) 
		REFERENCES Treningsokt (treningsoktID) ON DELETE CASCADE,
	CONSTRAINT HarTime_FK2 FOREIGN KEY (gruppetimeID) 
		REFERENCES Gruppetime (gruppetimeID) ON DELETE CASCADE
);

CREATE TABLE HarOvelse (
	ovelseID INTEGER NOT NULL,
    gruppetimeID INTEGER NOT NULL,
    prestasjon INTEGER,
    CONSTRAINT HarOvelse_PK PRIMARY KEY (ovelseID, gruppetimeID),
    CONSTRAINT HarOvelse_FK FOREIGN KEY (ovelseID) 
		REFERENCES Ovelse (ovelseID) ON DELETE CASCADE,
	CONSTRAINT HarOvelse_FK2 FOREIGN KEY (gruppetimeID) 
		REFERENCES Gruppetime (gruppetimeID) ON DELETE CASCADE
);