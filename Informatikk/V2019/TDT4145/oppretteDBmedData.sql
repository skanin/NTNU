CREATE TABLE Person (
   Pnr    INTEGER NOT NULL,
   Navn   VARCHAR(20),
   CONSTRAINT Person_PK PRIMARY KEY (Pnr));

CREATE TABLE Hund (
   Regnr    INTEGER NOT NULL,
   Navn     VARCHAR(30),
   Faar     INTEGER,
   Rase     VARCHAR(30),
   EierPnr INTEGER NOT NULL,
   CONSTRAINT Hund_PK PRIMARY KEY (Regnr),
   CONSTRAINT Hund_FK FOREIGN KEY (EierPnr) REFERENCES Person(Pnr),
   CONSTRAINT Alderssjekk CHECK (Faar > 1980));

CREATE TABLE BittAv (
   Pnr    INTEGER NOT NULL,
   Regnr  INTEGER NOT NULL,
   Antall INTEGER DEFAULT 0,
   CONSTRAINT BittAv_PK PRIMARY Key (Pnr, Regnr),
   CONSTRAINT BittAV_FK1 FOREIGN KEY (Pnr) REFERENCES Person(Pnr)
                                           ON DELETE CASCADE,
   CONSTRAINT BittAV_FK2 FOREIGN KEY (Regnr) REFERENCES Hund(Regnr)
                                             ON DELETE CASCADE,
   CONSTRAINT AntallSjekk CHECK (Antall > 0));

INSERT INTO Person VALUES (1, 'Olav');
INSERT INTO Person VALUES (2, 'Kari');
INSERT INTO Person VALUES (3, 'Anne');
INSERT INTO Person VALUES (4, 'Lisbeth');
INSERT INTO Person VALUES (5, 'Harald');
INSERT INTO Person VALUES (6, 'Liv');
INSERT INTO Person VALUES (7, 'Trude');
INSERT INTO Person VALUES (8, 'Per');
INSERT INTO Person VALUES (9, 'Kristin');
INSERT INTO Person VALUES (10, 'Christina');
INSERT INTO Person VALUES (11, 'Petter');
INSERT INTO Person VALUES (12, 'Liv');
INSERT INTO Person VALUES (13, 'Merete');

INSERT INTO Hund VALUES (1, 'King', 1992, 'Rottweiler', 1);
INSERT INTO Hund VALUES (2, 'Tarzan', 1993, 'Puddel', 3);
INSERT INTO Hund VALUES (3, 'Troll', 1995, 'Collie', 7);
INSERT INTO Hund VALUES (4, 'King', 1995, 'Schæfer', 6);
INSERT INTO Hund VALUES (5, 'Varg', 1995, 'Newfoundland', 1);
INSERT INTO Hund VALUES (6, 'Prins', 1994, 'Schæfer', 1);
INSERT INTO Hund VALUES (7, 'King', 1996, 'Puddel', 4);
INSERT INTO Hund VALUES (8, 'King', 1993, 'Rottweiler', 4);
INSERT INTO Hund VALUES (9, 'Tarzan', 1995, 'Doberman', 3);
INSERT INTO Hund VALUES (10, 'Troll', 1996, 'Puddel', 1);

INSERT INTO BittAv VALUES (2,2,5);
INSERT INTO BittAv VALUES (3,9,1);
INSERT INTO BittAv VALUES (4,9,1);
INSERT INTO BittAv VALUES (5,2,3);
INSERT INTO BittAv VALUES (5,4,2);
INSERT INTO BittAv VALUES (6,9,2);
INSERT INTO BittAv VALUES (8,5,2);
INSERT INTO BittAv VALUES (9,4,4);
INSERT INTO BittAv VALUES (11,5,1);
INSERT INTO BittAv VALUES (12,4,3);