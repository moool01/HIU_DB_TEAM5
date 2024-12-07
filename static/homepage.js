document.addEventListener('DOMContentLoaded', () => {
  // DOM 요소 참조
  const menuToggle = document.getElementById('menu-toggle');
  const sidebarMenu = document.getElementById('sidebar-menu');
  const loginButton = document.getElementById('login-button');
  const prevButton = document.getElementById('prev-button');
  const nextButton = document.getElementById('next-button');
  const backgroundContainer = document.querySelector('.background-container');
  
  // data-backgrounds 속성에서 JSON 배열 가져오기
  const backgrounds = JSON.parse(document.body.getAttribute('data-backgrounds')) || [];
  let currentBackgroundIndex = 0;

  // 배경 변경 함수
  const changeBackground = () => {
    if (backgroundContainer && backgrounds.length > 0) {
      backgroundContainer.style.backgroundImage = `url('${backgrounds[currentBackgroundIndex]}')`;
    }
  };

  // 초기 배경 설정
  if (backgrounds.length > 0) {
    changeBackground();
  }

  // 배경 자동 순환
  let backgroundRotationInterval = setInterval(() => {
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
    changeBackground();
  }, 10000);

  // 배경 버튼 클릭 이벤트
  prevButton.addEventListener('click', () => {
    currentBackgroundIndex = (currentBackgroundIndex - 1 + backgrounds.length) % backgrounds.length;
    changeBackground();
  });

  nextButton.addEventListener('click', () => {
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
    changeBackground();
  });

  // 햄버거 메뉴 토글
  menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    sidebarMenu.classList.toggle('hidden');
    sidebarMenu.classList.toggle('visible');
  });

  // 로그인 버튼 클릭 이벤트
  const loginUrl = document.body.dataset.loginUrl;
  loginButton.addEventListener('click', () => {
    if (loginUrl) {
      window.location.href = loginUrl;
    }
  });
//메뉴 버튼 클릭 이벤트
  document.addEventListener('DOMContentLoaded', () => {
  const menuItems = document.querySelectorAll('.menu-item');

  menuItems.forEach(item => {
    item.addEventListener('click', (event) => {
      console.log(`${event.target.innerText} 메뉴를 클릭했습니다.`);
    });
  });
});
});
// 플래시 메시지 표시 함수
function showFlashMessage(message, category) {
  const container = document.getElementById("flash-message-container");

  // 팝업 알림 생성
  const flashMessage = document.createElement("div");
  flashMessage.className = `flash-popup ${category}`;
  flashMessage.innerHTML = `
      <span>${message}</span>
      <button class="close-btn" onclick="this.parentElement.remove();">×</button>
  `;

  // 컨테이너에 메시지 추가
  container.appendChild(flashMessage);

  // 3초 후 자동 삭제
  setTimeout(() => {
      flashMessage.remove();
  }, 3000);
}