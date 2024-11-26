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
	FOREIGN KEY(professor_id) REFERENCES professor (id), 
	FOREIGN KEY(lecture_id) REFERENCES lecture (id)
);
INSERT INTO professor_lecture VALUES(1,'DB');
INSERT INTO professor_lecture VALUES(1,'AL');
INSERT INTO professor_lecture VALUES(2,'ML');
INSERT INTO professor_lecture VALUES(2,'AL');
INSERT INTO professor_lecture VALUES(1,'ML');
INSERT INTO professor_lecture VALUES(2,'OS');
CREATE TABLE summary (
	id INTEGER NOT NULL, 
	lecture_id VARCHAR(30) NOT NULL, 
	average_rating FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(lecture_id) REFERENCES lecture (id)
);
CREATE TABLE evaluation (
    id INTEGER NOT NULL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    lecture_id VARCHAR(30) NOT NULL,
    professor_id INTEGER NOT NULL,  -- 추가된 컬럼
    rating FLOAT NOT NULL,
    assignment_amount VARCHAR(20) NOT NULL,
    group_work VARCHAR(20) NOT NULL,
    grade_fairness VARCHAR(20) NOT NULL,
    attendance_type VARCHAR(50) NOT NULL,
    exam_count VARCHAR(50) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    review TEXT,
    FOREIGN KEY (student_id) REFERENCES student (id),
    FOREIGN KEY (lecture_id) REFERENCES lecture (id),
    FOREIGN KEY (professor_id) REFERENCES professor (id)
);
INSERT INTO evaluation VALUES(1,1,'DB',1,4.0,'많음','많음','보통','직접호명','두 번','2024년 2학기','교수님이 하시는 목소리가 잘 안들리지만 내용은 괜찮아요!');
INSERT INTO evaluation VALUES(2,1,'DB',1,4.0,'많음','많음','보통','직접호명','두 번','2024년 2학기','교수님이 하시는 목소리가 잘 안들리지만 내용은 괜찮아요!');
INSERT INTO evaluation VALUES(3,1,'ML',1,4.0,'보통','보통','관대함','지정좌석','네 번 이상','2022년 1학기','좋아요!');
INSERT INTO evaluation VALUES(4,5,'OS',2,5.0,'없음','없음','관대함','반영안함','없음','2023년 2학기',replace(replace('어머 이수업을 지금와서야 듣다니.. 참 완벽한 수업 이였어요\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(5,5,'OS',2,1.0,'많음','많음','깐깐함','지정좌석','네 번 이상','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(6,5,'OS',2,1.0,'많음','많음','깐깐함','직접호명','세 번','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(7,5,'OS',2,1.0,'많음','많음','깐깐함','전자출결','한 번','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(8,5,'OS',2,1.0,'많음','많음','깐깐함','전자출결','한 번','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(9,5,'OS',2,1.0,'많음','많음','깐깐함','전자출결','한 번','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
INSERT INTO evaluation VALUES(10,5,'OS',2,1.0,'많음','많음','깐깐함','전자출결','한 번','2023년 1학기',replace(replace('아 진짜 개 최악. 내 등록금과 시간이 개 아까움\r\n','\r',char(13)),'\n',char(10)));
DELETE FROM sqlite_sequence;
COMMIT;
