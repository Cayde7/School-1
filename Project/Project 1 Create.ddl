CREATE TABLE Moderator (ModeratorID SERIAL NOT NULL, Naam varchar(255) NOT NULL, PRIMARY KEY (ModeratorID));
CREATE TABLE Stations (StationNaam varchar(255) NOT NULL, PRIMARY KEY (StationNaam));
CREATE TABLE Tweet (TweetID BIGSERIAL NOT NULL, StationNaam varchar(255) NOT NULL, Naam varchar(32), Datum date NOT NULL, Inhoud varchar(140) NOT NULL, Geaccepteerd bool, ModeratorID int4, ModDatum date, ModTijd time, ModReden varchar(255), PRIMARY KEY (TweetID));
ALTER TABLE Tweet ADD CONSTRAINT FKTweet155392 FOREIGN KEY (ModeratorID) REFERENCES Moderator (ModeratorID);
ALTER TABLE Tweet ADD CONSTRAINT FKTweet291268 FOREIGN KEY (StationNaam) REFERENCES Stations (StationNaam);

