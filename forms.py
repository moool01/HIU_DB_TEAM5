from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class EvaluationForm(FlaskForm):
    lecture_title = SelectField(
        '과목명',
        choices=[
            ('', '과목을 선택해주세요'),
            ('Database', 'Database'),
            ('Machine Learning', 'Machine Learning'),
            ('Data Structure', 'Data Structure'),
            ('Algorithm', 'Algorithm'),
            ('Operating System', 'Operating System')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control"}  # CSS 클래스 유지
    )

    professor_name = SelectField(
        '교수명',
        choices=[
            ('', '교수님을 선택해주세요'),
            ('Professor Kim', 'Professor Kim'),
            ('Professor Choi', 'Professor Choi')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )

    rating = RadioField(
        '평점 (1-5)',
        choices=[
            ('1', '★ ☆ ☆ ☆ ☆'),
            ('2', '★ ★ ☆ ☆ ☆'),
            ('3', '★ ★ ★ ☆ ☆'),
            ('5', '★ ★ ★ ★ ★'),
            ('4', '★ ★ ★ ★ ☆'),
            ('5', '★ ★ ★ ★ ★')
        ],
        validators=[DataRequired()],
        render_kw={"class": "rating-options"}  # 새 CSS 클래스 반영
    )

    review = TextAreaField(
        '총평',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "이 강의에 대한 총평을 작성해주세요.",
            "rows": 5
        }
    )

    assignment_amount = RadioField(
        '과제 양',
        choices=[
            ('많음', '많음'),
            ('보통', '보통'),
            ('없음', '없음')
        ],
        validators=[DataRequired()],
        render_kw={"class": "inline-options"}
    )

    group_work = RadioField(
        '조모임 여부',
        choices=[
            ('많음', '많음'),
            ('보통', '보통'),
            ('없음', '없음')
        ],
        validators=[DataRequired()],
        render_kw={"class": "inline-options"}
    )

    grade_fairness = RadioField(
        '성적의 관대함',
        choices=[
            ('관대함', '관대함'),
            ('보통', '보통'),
            ('깐깐함', '깐깐함')
        ],
        validators=[DataRequired()],
        render_kw={"class": "inline-options"}
    )

    attendance_type = RadioField(
        '출석 방식',
        choices=[
            ('직접호명', '직접호명'),
            ('지정좌석', '지정좌석'),
            ('전자출결', '전자출결'),
            ('반영안함', '반영안함')
        ],
        validators=[DataRequired()],
        render_kw={"class": "inline-options"}
    )

    exam_count = RadioField(
        '시험 횟수',
        choices=[
            ('네 번 이상', '네 번 이상'),
            ('세 번', '세 번'),
            ('두 번', '두 번'),
            ('한 번', '한 번'),
            ('없음', '없음')
        ],
        validators=[DataRequired()],
        render_kw={"class": "inline-options"}
    )

    semester = SelectField(
        '수강학기 선택',
        choices=[
            ('', '수강학기를 선택해주세요'),
            ('2022년 1학기', '2022년 1학기'),
            ('2022년 2학기', '2022년 2학기'),
            ('2023년 1학기', '2023년 1학기'),
            ('2023년 2학기', '2023년 2학기'),
            ('2024년 1학기', '2024년 1학기'),
            ('2024년 2학기', '2024년 2학기')
        ],
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )

    submit = SubmitField(
        '제출',
        render_kw={"class": "btn btn-custom"}  # 커스텀 클래스 추가
    )
