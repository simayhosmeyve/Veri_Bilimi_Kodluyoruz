#### test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.
#### Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.
#### Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.
#### Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

* CREATE TABLE employee(id INTEGER,name VARCHAR(50),birthday DATE,email VARCHAR(100));

*  'Mockaroo' servisi kullanılarak veriler rastgele oluşturuldu. 
insert into employee (id, name, birthday, email) values (1, 'Gretta', '5.7.2021', 'gtefft0@chronoengine.com');

insert into employee (id, name, birthday, email) values (2, 'Alexio', '4.12.2021', 'awinders1@privacy.gov.au');

insert into employee (id, name, birthday, email) values (3, 'Homer', '10.4.2021', 'hgreensall2@yale.edu');

insert into employee (id, name, birthday, email) values (4, 'Eudora', '9.1.2022', 'edawber3@google.nl');

insert into employee (id, name, birthday, email) values (5, 'Zsazsa', '1.3.2021', 'zlaugherane4@webmd.com');

insert into employee (id, name, birthday, email) values (6, 'Myca', '11.11.2021', 'mklicher5@cbsnews.com');

insert into employee (id, name, birthday, email) values (7, 'Querida', '28.2.2021', 'qdemougeot6@mapquest.com');

insert into employee (id, name, birthday, email) values (8, 'Tannie', '29.5.2021', 'truilton7@amazon.de');

insert into employee (id, name, birthday, email) values (9, 'Rori', '30.1.2021', 'rwollrauch8@mayoclinic.com');

insert into employee (id, name, birthday, email) values (10, 'Cleon', '11.11.2021', 'clynett9@mysql.com');

insert into employee (id, name, birthday, email) values (11, 'Jeanie', '8.7.2021', 'jmedcalfea@g.co');

insert into employee (id, name, birthday, email) values (12, 'Conny', '7.7.2021', 'ckretschmerb@livejournal.com');

insert into employee (id, name, birthday, email) values (13, 'Rebecka', '5.3.2021', 'rkendredc@tripadvisor.com');

insert into employee (id, name, birthday, email) values (14, 'Iolande', '25.2.2021', 'iyeuletd@over-blog.com');

insert into employee (id, name, birthday, email) values (15, 'Prent', '29.12.2021', 'pimriee@senate.gov');

insert into employee (id, name, birthday, email) values (16, 'Elisabetta', '24.12.2021', 'emaryonf@springer.com');

insert into employee (id, name, birthday, email) values (17, 'Brigit', '19.10.2021', 'bagostinig@foxnews.com');

insert into employee (id, name, birthday, email) values (18, 'Nisse', '25.1.2021', 'nholburnh@twitpic.com');

insert into employee (id, name, birthday, email) values (19, 'Neils', '10.6.2021', 'nbaroni@about.me');

insert into employee (id, name, birthday, email) values (20, 'Whitney', '8.3.2021', 'wdesimonij@dropbox.com');

insert into employee (id, name, birthday, email) values (21, 'Noellyn', '1.9.2021', 'nlannink@google.com');

insert into employee (id, name, birthday, email) values (22, 'Alane', '28.5.2021', 'aroastl@smugmug.com');

insert into employee (id, name, birthday, email) values (23, 'Georgena', '2.6.2021', 'gronaghanm@ezinearticles.com');

insert into employee (id, name, birthday, email) values (24, 'Janina', '6.1.2022', 'jmouldn@amazonaws.com');

insert into employee (id, name, birthday, email) values (25, 'Judie', '27.12.2021', 'jdevoteo@gov.uk');

insert into employee (id, name, birthday, email) values (26, 'Imojean', '7.5.2021', 'iuffp@intel.com');

insert into employee (id, name, birthday, email) values (27, 'Nikki', '9.3.2021', 'nkellsq@studiopress.com');

insert into employee (id, name, birthday, email) values (28, 'Leola', '29.7.2021', 'lmcquillanr@salon.com');

insert into employee (id, name, birthday, email) values (29, 'Karalee', '4.12.2021', 'kvanarsdales@ovh.net');

insert into employee (id, name, birthday, email) values (30, 'Sile', '26.1.2021', 'svatinit@pbs.org');

insert into employee (id, name, birthday, email) values (31, 'Tammy', '30.10.2021', 'thammentsu@jimdo.com');

insert into employee (id, name, birthday, email) values (32, 'D''arcy', '27.12.2021', 'dsemensv@sitemeter.com');

insert into employee (id, name, birthday, email) values (33, 'Emmerich', '18.5.2021', 'eyegorchenkovw@booking.com');

insert into employee (id, name, birthday, email) values (34, 'Drud', '7.8.2021', 'dobeex@github.io');

insert into employee (id, name, birthday, email) values (35, 'Darbee', '7.11.2021', 'dmacmurrayy@ft.com');

insert into employee (id, name, birthday, email) values (36, 'Devlin', '14.3.2021', 'daustwickz@eepurl.com');

insert into employee (id, name, birthday, email) values (37, 'Harriet', '10.7.2021', 'hetienne10@is.gd');

insert into employee (id, name, birthday, email) values (38, 'Matthew', '25.12.2021', 'mlivens11@canalblog.com');

insert into employee (id, name, birthday, email) values (39, 'Erny', '26.9.2021', 'epolak12@businesswire.com');

insert into employee (id, name, birthday, email) values (40, 'Dex', '11.11.2021', 'dgent13@kickstarter.com');

insert into employee (id, name, birthday, email) values (41, 'Brady', '6.12.2021', 'bjizhaki14@artisteer.com');

insert into employee (id, name, birthday, email) values (42, 'Julissa', '22.7.2021', 'jeisak15@globo.com');

insert into employee (id, name, birthday, email) values (43, 'Anton', '19.7.2021', 'askule16@altervista.org');

insert into employee (id, name, birthday, email) values (44, 'Keefe', '3.4.2021', 'kbrecknall17@soundcloud.com');

insert into employee (id, name, birthday, email) values (45, 'Xaviera', '26.4.2021', 'xkiessel18@sitemeter.com');

insert into employee (id, name, birthday, email) values (46, 'Nikolai', '18.3.2021', 'nperigoe19@goodreads.com');

insert into employee (id, name, birthday, email) values (47, 'Roseanna', '22.3.2021', 'rfogden1a@marriott.com');

insert into employee (id, name, birthday, email) values (48, 'Alric', '11.2.2021', 'abillingsly1b@google.co.uk');

insert into employee (id, name, birthday, email) values (49, 'Danya', '19.7.2021', 'dwheatcroft1c@t-online.de');

insert into employee (id, name, birthday, email) values (50, 'Hannie', '12.6.2021', 'hskacel1d@artisteer.com');

* UPDATE employee SET name = 'Amelie' WHERE id = 1;

UPDATE employee SET name = 'James' WHERE id = 2;

UPDATE employee SET email = 'hgreensall@yale.edu' WHERE id = 3;

UPDATE employee SET email = 'edawber@google.nl' WHERE id = 4;

UPDATE employee SET birthday = '1.4.2021' WHERE id = 5;

* DELETE FROM employee WHERE name = 'Dex';

DELETE FROM employee WHERE id = 9;

DELETE FROM employee WHERE id = 30;

DELETE FROM employee WHERE name = 'Myca' AND email = 'mklicher5@cbsnews.com';

DELETE FROM employee WHERE name = 'Rebecka' AND birthday = '5.3.2021';
