from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'student'  # 테이블 이름 명시
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)

# 중간 테이블 정의 (다대다 관계)
Professor_lecture = db.Table(
    'professor_lecture',
    db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key=True),
    db.Column('lecture_id', db.String(30), db.ForeignKey('lecture.id'), primary_key=True)  # lecture_id를 String으로 수정
)

class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lectures = db.relationship('Lecture', secondary=Professor_lecture, back_populates='professors')

class Lecture(db.Model):
    __tablename__ = 'lecture'
    id = db.Column(db.String(30), primary_key=True)  # id를 String으로 수정
    title = db.Column(db.String(100), nullable=False)
    professors = db.relationship('Professor', secondary=Professor_lecture, back_populates='lectures')

class Evaluation(db.Model):
    __tablename__ = 'evaluation'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    lecture_id = db.Column(db.String(30), db.ForeignKey('lecture.id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    assignment_amount = db.Column(db.String(20), nullable=False)
    group_work = db.Column(db.String(20), nullable=False)
    grade_fairness = db.Column(db.String(20), nullable=False)
    attendance_type = db.Column(db.String(50), nullable=False)
    exam_count = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    review = db.Column(db.Text, nullable=True)

    # Add relationships
    lecture = db.relationship('Lecture', backref='evaluations', lazy=True)
    professor = db.relationship('Professor', backref='evaluations', lazy=True)

class Summary(db.Model):
    __tablename__ = 'summary'  # 테이블 이름 명시
    id = db.Column(db.Integer, primary_key=True)
    lecture_id = db.Column(db.String(30), db.ForeignKey('lecture.id'), nullable=False)  # lecture_id 타입 수정
    average_rating = db.Column(db.Float, nullable=False)
