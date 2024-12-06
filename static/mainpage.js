document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu-toggle');
  const sidebarMenu = document.getElementById('sidebar-menu');
  const loginButton = document.getElementById('login-button');
  const menuItems = document.querySelectorAll('.menu-item');
  const backgroundContainer = document.querySelector('.background-container');
  const prevButton = document.getElementById('prev-button');
  const nextButton = document.getElementById('next-button');

  // 배경 이미지 배열
  const backgrounds = [
    'background1.png',
    'background2.png',
    'background3.png'
  ];

  let currentBackgroundIndex = 0;

  // 배경 순환 함수
  const changeBackground = () => {
    backgroundContainer.style.backgroundImage = `url('${backgrounds[currentBackgroundIndex]}')`;
  };

  // 자동 배경 변경 (10초마다)
  setInterval(() => {
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
    changeBackground();
  }, 10000);

  // 좌측 화살표 버튼 클릭 시 배경 변경
  prevButton.addEventListener('click', () => {
    currentBackgroundIndex = (currentBackgroundIndex - 1 + backgrounds.length) % backgrounds.length;
    changeBackground();
  });

  // 우측 화살표 버튼 클릭 시 배경 변경
  nextButton.addEventListener('click', () => {
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
    changeBackground();
  });

  // 햄버거 메뉴 클릭 이벤트
  menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    sidebarMenu.classList.toggle('hidden');
    sidebarMenu.classList.toggle('visible');
  });

  // 로그인 버튼 클릭 이벤트
  loginButton.addEventListener('click', () => {
    window.location.href = 'login.html'; // 로그인 페이지로 이동
  });

  // 각 메뉴 버튼 클릭 시 페이지 이동
  menuItems.forEach((button, index) => {
    button.addEventListener('click', () => {
      let targetPage = '';

      // 메뉴에 따라 이동할 페이지 설정
      switch (index) {
        case 0:
          targetPage = 'search.html'; // 첫 번째 메뉴: 강의/교수님 검색
          break;
        case 1:
          targetPage = 'evaluation.html'; // 두 번째 메뉴: 강의 평가 작성
          break;
        case 2:
          targetPage = 'my-reviews.html'; // 세 번째 메뉴: 나의 평가 보기
          break;
        case 3:
          targetPage = 'help.html'; // 네 번째 메뉴: 도움말
          break;
        default:
          targetPage = 'index.html'; // 기본값으로 홈 화면
      }

      window.location.href = targetPage; // 설정된 페이지로 이동
    });
  });
});