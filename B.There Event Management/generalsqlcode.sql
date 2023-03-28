CREATE TABLE events (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50),
    date DATE,
    host VARCHAR(50),
    description TEXT,
    PRIMARY KEY (id)
) engine=INNODB;

INSERT INTO events(id,name,date,host,description) VALUES
(1001,"Mecum Auction Indy","2021-05-14","Mecum Auto Auctions","Mecum Auctions are the largest and most prestigious auto auctions coming to Indianapolis soon!"),
(1002,"Fuelicious","2021-10-28","Artomobilia","A prestigious event at the Lucas Oil Estate"),
(1003,"World of Wheels","2022-05-25","Autorama","A massive travelling auto show coming to Indy soon!"),
(1004,"Caffeine and Chrome","2022-10-30","Gateway Classic Cars","A fantastic classic car show coming to Indy soon!");

CREATE TABLE attendees (
    id INT NOT NULL AUTO_INCREMENT,
    event_id INT,
    name VARCHAR(50),
    email VARCHAR(50),
    comment TINYTEXT,
    FOREIGN KEY (event_id) REFERENCES events(id),
    PRIMARY KEY(ID)
) engine=INNODB;

INSERT INTO attendees(id,event_id,name,email,comment) VALUES
(1001,1001,"Jake","jake123@gmail.com","Can't wait!"),
(1002,1001,"Mikayla","mik@iu.edu","This is gonna be sick"),
(1003,1002,"Robert","Robert26@yahoo.com","This is gonna be so fun!"),
(1004,1003,"Mikey","mikeboy25@gmail.com","Already packing my bags!"),
(1005,1004,"Tim","timmyman22@mail.com","I don't know why I signed up for this");