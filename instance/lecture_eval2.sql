PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE student (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO student VALUES(1,'김재경','password1');
INSERT INTO student VALUES(2,'김채민','password2');
INSERT INTO student VALUES(3,'김서연','password3');
INSERT INTO student VALUES(4,'이유림','password4');
INSERT INTO student VALUES(5,'김민재','password5');
CREATE TABLE professor (
	id INTEGER NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO professor VALUES(1,'Professor Kim');
INSERT INTO professor VALUES(2,'Professor Choi');
CREATE TABLE lecture (
	id VARCHAR(30) NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO lecture VALUES('DB','Database');
INSERT INTO lecture VALUES('ML','Machine Learning');
INSERT INTO lecture VALUES('DS','Data Structure');
INSERT INTO lecture VALUES('AL','Algorithm');
INSERT INTO lecture VALUES('OS','Operating System');
CREATE TABLE professor_lecture (
	professor_id INTEGER NOT NULL, 
	lecture_id VARCHAR(30) NOT NULL, 
	PRIMARY KEY (professor_id, lecture_id), 
	FOREIGN KEY(professor_id) REFERENCES professor (i_