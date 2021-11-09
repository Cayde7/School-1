CREATE TABLE Bericht (TweetID BIGSERIAL NOT NULL, StationNaam varchar(255) NOT NULL, Naam varchar(32), Datum date NOT NULL, Inhoud varchar(140) NOT NULL, Geaccepteerd bool, ModeratorModeratorID int4, ModDatum date, ModTijd time, ModReden varchar(255), PRIMARY KEY (TweetID));
CREATE TABLE Moderator (ModeratorID SERIAL NOT NULL, Naam varchar(255) NOT NULL, PRIMARY KEY (ModeratorID));
CREATE TABLE Stations (StationNaam varchar(255) NOT NULL, PRIMARY KEY (StationNaam));
ALTER TABLE Bericht ADD CONSTRAINT FKBericht515760 FOREIGN KEY (ModeratorModeratorID) REFERENCES Moderator (ModeratorID);
ALTER TABLE Bericht ADD CONSTRAINT FKBericht241876 FOREIGN KEY (StationNaam) REFERENCES Stations (StationNaam);

