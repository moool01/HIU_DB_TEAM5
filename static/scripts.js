// 강의 평가 폼 입력 검증
document.addEventListener("DOMContentLoaded", () => {
    const evaluationForm = document.querySelector("form");

//     if (evaluationForm) {
//         evaluationForm.addEventListener("submit", (event) => {
//             const rating = document.querySelector('input[name="rating"]');
//             const examCount = document.querySelector('input[name="exam_count"]');
//             const semester = document.querySelector('input[name="semester"]');

//             let valid = true;

//             // 평점 검증
//             if (rating.value < 1 || rating.value > 5 || rating.value === "") {
//                 alert("평점은 1에서 5 사이의 숫자를 입력해야 합니다.");
//                 valid = false;
//             }

//             // 시험 횟수 검증
//             if (examCount.value < 0 || examCount.value === "") {
//                 alert("시험 횟수는 0 이상의 숫자를 입력해야 합니다.");
//                 valid = false;
//             }

//             // 학기 입력 검증
//             if (semester.value.trim() === "") {
//                 alert("학기를 입력해 주세요 (예: 2023 Fall).");
//                 valid = false;
//             }

//             // 검증 실패 시 제출 방지
//             if (!valid) {
//                 event.preventDefault();
//             }
//         });
//     }
});

// 검색창 자동 포커스 기능
const searchInput = document.querySelector('input[name="query"]');
if (searchInput) {
    searchInput.addEventListener("focus", () => {
        searchInput.style.backgroundColor = "#f0f8ff";
    });

    searchInput.addEventListener("blur", () => {
        searchInput.style.backgroundColor = "white";
    });
}

// 검색 결과 항목 클릭 시 강조 효과
const searchItems = document.querySelectorAll(".search-container li a");
if (searchItems) {
    searchItems.forEach((item) => {
        item.addEventListener("mouseenter", () => {
            item.style.color = "#005BB5";
            item.style.fontWeight = "bold";
        });

        item.addEventListener("mouseleave", () => {
            item.style.color = "#0078D4";
            item.style.fontWeight = "normal";
        });
    });
}
// 별점 선택 시 점수 업데이트
document.querySelectorAll('.stars input').forEach((radio) => {
    radio.addEventListener('change', (e) => {
      // 선택된 별의 value 값 가져오기
      const rating = e.target.value;
      // 점수 표시 업데이트
      document.querySelector('.rating-value').textContent = `${rating}/5`;
    });
  });
  
document.addEventListener("DOMContentLoaded", () => {
    const stars = document.querySelectorAll(".stars input");
    const ratingValue = document.querySelector(".rating-value");

    stars.forEach((star) => {
        star.addEventListener("change", (e) => {
            const rating = e.target.value; // 선택된 별점의 value 가져오기
            ratingValue.textContent = `${rating}/5`; // 올바른 점수로 업데이트
        });
    });
});
