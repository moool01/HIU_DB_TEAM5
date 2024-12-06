from flask import Flask, flash, render_template, request, redirect, url_for,session,g
from models import db, Student, Professor, Lecture, Evaluation, Summary,Professor_lecture
from forms import EvaluationForm
import cx_Oracle,sys
from env import DATABASE

# Oracle Instant Client 초기화
if sys.platform == "darwin":  # macOS
    try:
        cx_Oracle.init_oracle_client(lib_dir="/opt/oracle/instantclient_23_3")
        print("Oracle Instant Client 초기화 성공 (macOS)")
    except cx_Oracle.DatabaseError as e:
        print("Oracle Instant Client 초기화 실패 (macOS):", e)
        exit()

elif sys.platform == "win32":  # Windows
    try:
        cx_Oracle.init_oracle_client(lib_dir="C:\\instantclient-basic-windows\\instantclient_23_6")
        print("Oracle Instant Client 초기화 성공 (Windows)")
    except cx_Oracle.DatabaseError as e:
        print("Oracle Instant Client 초기화 실패 (Windows):", e)
        exit()

else:
    try:
        print("Oracle Instant Client 초기화 성공 (linux)")
    except cx_Oracle.DatabaseError as e:
        print("Oracle Instant Client 초기화 실패 (linux):", e)
        exit()
        print("지원하지 않는 운영 체제입니다:", sys.platform)
        exit()

# 이후 코드 작성
app = Flask(__name__)
app.config.from_object(DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.before_request
def add_student_to_template():
    student_id = session.get('student_id')
    if student_id:
        student = Student.query.get(student_id)
        g.student = student  # g는 Flask의 전역 객체
    else:
        g.student = None

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user_id = request.form['userID']
        password = request.form['password']
        user = Student.query.filter_by(id=int(user_id), password=password).first()
        if user:
            session['student_id'] = user.id  # 세션에 사용자 ID 저장
            flash('로그인 성공!', 'success')
            return redirect(url_for('evaluate'))
        else:
            flash('로그인 실패: 아이디와 비밀번호를 확인하세요.', 'danger')
            return redirect(url_for('login'))
        
        return render_template('login.html')
@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'GET':
        return render_template('login2.html')
    elif request.method == 'POST':
        user_id = request.form['userID']
        password = request.form['password']
        user = Student.query.filter_by(id=int(user_id), password=password).first()
        if user:
            session['student_id'] = user.id  # 세션에 사용자 ID 저장
            flash('로그인 성공!', 'success')
            return redirect(url_for('evaluate'))
        else:
            flash('로그인 실패: 아이디와 비밀번호를 확인하세요.', 'danger')
            return redirect(url_for('login2'))
        
        return render_template('login.html')
@app.route('/my_evaluations')
def my_evaluations():
    student_id = session.get('student_id')
    if not student_id:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))

    student = Student.query.get(student_id)  # 현재 로그인한 사용자 정보 가져오기
    evaluations = Evaluation.query.filter_by(student_id=student_id).all()
    return render_template('evaluation_list.html', evaluations=evaluations, student=student)

@app.route('/edit/<int:evaluation_id>', methods=['GET', 'POST'])
def edit_evaluation(evaluation_id):
    student_id = session.get('student_id')
    if not student_id:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))

    evaluation = Evaluation.query.get_or_404(evaluation_id)
    if evaluation.student_id != student_id:
        flash('권한이 없습니다.', 'danger')
        return redirect(url_for('my_evaluations'))

    form = EvaluationForm(obj=evaluation)
    if form.validate_on_submit():
        evaluation.rating = form.rating.data
        evaluation.assignment_amount = form.assignment_amount.data
        evaluation.group_work = form.group_work.data
        evaluation.grade_fairness = form.grade_fairness.data
        evaluation.attendance_type = form.attendance_type.data
        evaluation.exam_count = form.exam_count.data
        evaluation.semester = form.semester.data
        evaluation.review = form.review.data
        db.session.commit()
        flash('평가가 성공적으로 수정되었습니다.', 'success')
        return redirect(url_for('my_evaluations'))

    return render_template('evaluation_form.html', form=form, edit_mode=True)

@app.route('/delete/<int:evaluation_id>', methods=['POST'])
def delete_evaluation(evaluation_id):
    student_id = session.get('student_id')
    if not student_id:
        flash('로그인이 필요합니다.', 'danger')
        return redirect(url_for('login'))

    evaluation = Evaluation.query.get_or_404(evaluation_id)
    if evaluation.student_id != student_id:
        flash('권한이 없습니다.', 'danger')
        return redirect(url_for('my_evaluations'))

    db.session.delete(evaluation)
    db.session.commit()
    flash('평가가 성공적으로 삭제되었습니다.', 'success')
    return redirect(url_for('my_evaluations'))

@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    form = EvaluationForm()
    student_id = session.get('student_id')
    student = Student.query.get(student_id)

    if form.validate_on_submit():
        # 강의 및 교수 정보 처리
        lecture_title = form.lecture_title.data.strip()
        professor_name = form.professor_name.data.strip()

        # 교수 찾기 또는 생성
        professor = Professor.query.filter_by(name=professor_name).first()
        if not professor:
            professor = Professor(name=professor_name)
            db.session.add(professor)
            db.session.commit()

        # 강의 찾기 또는 생성
        lecture = Lecture.query.filter_by(title=lecture_title).first()
        if not lecture:
            lecture = Lecture(title=lecture_title)
            db.session.add(lecture)
            db.session.commit()

        # 강의와 교수 연결 (Professor_lecture 테이블에 추가)
        if professor not in lecture.professors:
            lecture.professors.append(professor)  # 다대다 관계 추가
            db.session.commit()

        # 중복 평가 확인
        existing_evaluation = Evaluation.query.filter_by(
            student_id=student_id,
            lecture_id=lecture.id,
            professor_id=professor.id,
            semester=form.semester.data
        ).first()

        if existing_evaluation:
            # 이미 존재하는 경우
            flash("이미 해당 강의에 대해 평가를 등록하셨습니다. 다시 시도할 수 없습니다.", "warning")
        else:
            # 새 평가 생성
            evaluation = Evaluation(
                student_id=student_id,
                lecture_id=lecture.id,
                professor_id=professor.id,
                rating=form.rating.data,
                assignment_amount=form.assignment_amount.data,
                group_work=form.group_work.data,
                grade_fairness=form.grade_fairness.data,
                attendance_type=form.attendance_type.data,
                exam_count=form.exam_count.data,
                semester=form.semester.data,
                review=form.review.data
            )
            db.session.add(evaluation)
            db.session.commit()
            flash("평가가 성공적으로 등록되었습니다.", "success")
            # summary로 리디렉션
            return redirect(url_for('summary', lecture_id=lecture.id, professor_id=professor.id))

    # 기존 평가 존재 시, 동일 페이지로 유지
    evaluations = Evaluation.query.filter_by(student_id=student_id).all()
    return render_template('evaluation_form.html', form=form, student=student)



@app.route('/summary/<string:lecture_id>/<int:professor_id>')
def summary(lecture_id, professor_id):
    lecture = Lecture.query.get_or_404(lecture_id)
    professor = Professor.query.get_or_404(professor_id)
    student_id = session.get('student_id')
    student = Student.query.get(student_id)
    evaluations = Evaluation.query.filter_by(lecture_id=lecture_id, professor_id=professor_id).all()

    # 평균 별점 계산
    avg_rating = round(sum(e.rating for e in evaluations) / len(evaluations), 2) if evaluations else 0

    # 통계 초기화 및 집계
    stats = {
        "assignment_amount": {"많음": 0, "보통": 0, "없음": 0},
        "group_work": {"많음": 0, "보통": 0, "없음": 0},
        "grade_fairness": {"관대함": 0, "보통": 0, "깐깐함": 0},
        "attendance_type": {"직접호명": 0, "지정좌석": 0, "전자출결": 0, "반영안함": 0},
        "exam_count": {"네 번 이상": 0, "세 번": 0, "두 번": 0, "한 번": 0, "없음": 0},
    }

    for e in evaluations:
        stats["assignment_amount"][e.assignment_amount] += 1
        stats["group_work"][e.group_work] += 1
        stats["grade_fairness"][e.grade_fairness] += 1
        stats["attendance_type"][e.attendance_type] += 1
        stats["exam_count"][e.exam_count] += 1

    total = len(evaluations)

    percentages = {
        key: {k: round((v / total * 100), 1) if total > 0 else 0 for k, v in value.items()}
        for key, value in stats.items()
    }

    most_selected = {
        "attendance_type": max(stats["attendance_type"], key=stats["attendance_type"].get) if total > 0 else "없음",
        "exam_count": max(stats["exam_count"], key=stats["exam_count"].get) if total > 0 else "없음",
    }

    return render_template(
        'summary_page.html',
        page_title=f"Database ({professor.name}) 강의 평가 요약",
        student=student,
        lecture=lecture,
        professor=professor,
        avg_rating=avg_rating,
        evaluations=evaluations,
        percentages=percentages,
        most_selected=most_selected,
        total_reviews=total
    )

@app.route('/search', methods=['GET', 'POST'])
def search():
    student_id = session.get('student_id')
    student = Student.query.get(student_id)
    query = request.form.get('query', '').strip()

    if not query:
        flash('검색어를 입력하세요.', 'danger')
        return redirect(url_for('home'))

    # 강의와 교수의 모든 조합 반환
    lectures = (
        db.session.query(Lecture, Professor)
        .join(Professor_lecture, Professor_lecture.c.lecture_id == Lecture.id)
        .join(Professor, Professor_lecture.c.professor_id == Professor.id)
        .filter(
            Lecture.title.ilike(f"%{query}%") |
            Professor.name.ilike(f"%{query}%")
        )
        .distinct()
        .all()
    )   

    # 객체 그대로 전달
    results = [
        {"lecture": lecture, "professor": professor}
        for lecture, professor in lectures
    ]

    return render_template('search_page.html', results=results, student=student)

@app.route('/help')
def help():
    student_id = session.get('student_id')
    student = Student.query.get(student_id) if student_id else None
    return render_template('help.html', student=student)

@app.route('/search_main', methods=['GET', 'POST'])
def search_main():
    query = request.form.get('query', '').strip()  # 폼 데이터에서 검색어 가져오기
    student_id = session.get('student_id')
    student = Student.query.get(student_id) if student_id else None

    results = []
    if query:
        # 강의 및 교수 검색
        lectures = (
            db.session.query(Lecture, Professor)
            .join(Professor_lecture, Professor_lecture.c.lecture_id == Lecture.id)
            .join(Professor, Professor_lecture.c.professor_id == Professor.id)
            .filter(
                Lecture.title.ilike(f"%{query}%") |
                Professor.name.ilike(f"%{query}%")
            )
            .distinct()
            .all()
        )

        results = [
            {"lecture": lecture, "professor": professor}
            for lecture, professor in lectures
        ]

    return render_template('search_main.html', query=query, results=results, student=student)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # 데이터 추가
        if not Professor.query.first():
            professor1 = Professor(name="Dr. Choi Wooseok")
            professor2 = Professor(name="Dr. Lee Jaeho")

            lecture1 = Lecture(title="Computer Science")
            lecture2 = Lecture(title="Machine Learning")

            professor1.lectures.append(lecture1)
            professor1.lectures.append(lecture2)
            professor2.lectures.append(lecture1)

            db.session.add_all([professor1, professor2, lecture1, lecture2])
            db.session.commit()
    app.run(debug=True)
