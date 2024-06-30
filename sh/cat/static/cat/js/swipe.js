const swiper1 = new Swiper('.swiper__hero', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,
  spaceBetween: 20,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination__hero',
  },

 
  autoplay: {
   delay: 10000,
 },

});

const swiper2 = new Swiper('.swiper__review', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,
  slidesPerView: 2.5,
  spaceBetween: 30,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },


});


const swiper3 = new Swiper('.swiper__review2', {
  // Optional parameters
  direction: 'horizontal',
  loop: false,
  slidesPerView: 1,
  spaceBetween: 30,

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },


});



const cursorDot = document.querySelector('[data-cursor-dott]');
const cursorScale = [...document.querySelectorAll('.cursor-scale')];

// Переменные для хранения координат мыши и курсора
let mouseX = 0;
let mouseY = 0;
let cursorX = 0;
let cursorY = 0;
const delay = 0.05; // Задержка следования

function animateCursor() {
  // Линейная интерполяция для плавного следования
  cursorX += (mouseX - cursorX) * delay;
  cursorY += (mouseY - cursorY) * delay;

  // Вычисляем размеры курсора для центрирования
  const centerX = cursorDot.offsetWidth / 2;
  const centerY = cursorDot.offsetHeight / 2;

  // Применяем стили к курсору
  cursorDot.style.left = `${cursorX - centerX}px`;
  cursorDot.style.top = `${cursorY - centerY}px`;

  // Рекурсивно вызываем animateCursor на следующем кадре анимации
  requestAnimationFrame(animateCursor);
}

// Запускаем анимацию
animateCursor();

// Обработчик события для mousemove
window.addEventListener('mousemove', (e) => {
  // Обновляем координаты мыши
  mouseX = e.clientX;
  mouseY = e.clientY;
});

const swiper4 = new Swiper('.asic__swiper', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  slidesPerView: 2.5,
  spaceBetween: 30,

  on: {
    touchMove(swiper, event) {
      // Вызываем функцию обновления координат мыши напрямую
      mouseX = event.clientX;
      mouseY = event.clientY;
    },
  },

});



// События наведения для элементов, на которые должен реагировать курсор
cursorScale.forEach(link => {
  link.addEventListener('mouseleave', () => {
    cursorDot.classList.remove('grow');
  });
  link.addEventListener('mousemove', () => {
    cursorDot.classList.add('grow');
  });
});



const swiper5 = new Swiper('.asic__swiper2', {
 direction: 'horizontal',
  loop: true,
  slidesPerView: 1.2,
  spaceBetween: 10,
  centeredSlides: true,


});