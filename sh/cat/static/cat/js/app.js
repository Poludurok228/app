window.addEventListener('scroll', function() {
    var heroHeader = document.querySelector('.hero__header');
    var headerHeight = heroHeader.clientHeight * 2;

    if (window.scrollY > headerHeight) {
        heroHeader.classList.add('hero__header__active');
    } else {
        heroHeader.classList.remove('hero__header__active');
    }
});








window.addEventListener('scroll', () => {
  const stepItems = document.querySelectorAll('.step__item');

  stepItems.forEach((item, index) => {
    const scrollBarProgress = item.querySelector('.scroll__bar__proggres');
    const stepItemOffset = item.offsetTop;
    const stepItemHeight = item.clientHeight;
    const progressHeight = scrollBarProgress.clientHeight;
    const speedCoeff = 0.2; // коэффициент скорости изменения высоты

    let scrollPosition = window.scrollY;
    let startFromTop = stepItemOffset - window.innerHeight / 2;
    let bottomLimit = stepItemOffset + stepItemHeight - window.innerHeight / 2;

    if(scrollPosition > startFromTop && scrollPosition < bottomLimit) {
      let progress = ((scrollPosition - startFromTop) / (stepItemHeight - window.innerHeight / 2) * 100) * speedCoeff;
      scrollBarProgress.style.height = `${progress}%`;
    } else if(scrollPosition <= startFromTop) {
      scrollBarProgress.style.height = '0%';
    } else if(scrollPosition >= bottomLimit) {
      scrollBarProgress.style.height = '100%';
    }
  });
});







const heroMenuBtn = document.querySelector('.hero__menu__btn');
const mediaMenuBtn = document.querySelector('.media__menu__btn');
const mediaMenu = document.querySelector('.media__menu');

heroMenuBtn.addEventListener('click', () => {
  mediaMenu.classList.add('media__menu__active');
});

mediaMenuBtn.addEventListener('click', () => {
  mediaMenu.classList.remove('media__menu__active');
});








const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 0; // Изначально показываем первое изображение

imgBtns.forEach((imgItem, index) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = index;
        slideImage();
        imgBtns.forEach((item) => {
            item.parentElement.classList.remove('img-item-active');
        });
        imgItem.parentElement.classList.add('img-item-active');
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase').clientWidth;
    const gap = parseFloat(window.getComputedStyle(document.querySelector('.img-showcase')).gap);
    document.querySelector('.img-showcase').style.transform = `translateX(${-imgId * (displayWidth + gap)}px)`;
}

window.addEventListener('resize', slideImage);








const tabItems = document.querySelectorAll('.tab-item');
const tabPanes = document.querySelectorAll('.tab-pane');

tabItems.forEach((item) => {
    item.addEventListener('click', (event) => {
        const tabNum = item.getAttribute('data-tab');
        tabPanes.forEach((pane) => {
            if (pane.getAttribute('data-tab') === tabNum) {
                pane.classList.add('active');
            } else {
                pane.classList.remove('active');
            }
        });
        tabItems.forEach((i) => {
            i.classList.remove('active');
        });
        item.classList.add('active');
    });
});






document.addEventListener('DOMContentLoaded', function() {
    // Находим нужные элементы по классам
    var filterBtn = document.querySelector('.filterbtnjs');
    var filterMenu = document.querySelector('.filter__menu');
    var closeBtn = document.querySelector('.filter__menu__close__btn');

    // Обработчик события для открытия меню
    filterBtn.addEventListener('click', function() {
        filterMenu.style.left = '0%';
    });

    // Обработчик события для закрытия меню
    closeBtn.addEventListener('click', function() {
        filterMenu.style.left = '-100%';
    });
});





function validateRange(event) {
  // Определение родительского контейнера текущего ползунка
  const parent = event.target.closest('.block__filter__price');

  // Определение элементов для обновления внутри этого контейнера
  const minDisplay = parent.querySelector('.price-content div:nth-child(1) p');
  const maxDisplay = parent.querySelector('.price-content div:nth-child(2) p');

  // Получаем ссылки на ползунки минимума и максимума
  const minInput = parent.querySelector(".min-price, .min-power");
  const maxInput = parent.querySelector(".max-price, .max-power");

  // Получаем значения ползунков
  let minValue = parseInt(minInput.value);
  let maxValue = parseInt(maxInput.value);

  // Валидация значений
  if (minValue > maxValue) {
    let tempValue = maxValue;
    maxValue = minValue;
    minValue = tempValue;
  }

  // Обновление отображаемых значений
  minDisplay.innerHTML = minValue;
  maxDisplay.innerHTML = maxValue;
}

// Перебираем все элементы входа и добавляем обработчик события
const inputElements = document.querySelectorAll(".range-slider input");
inputElements.forEach((element) => {
  element.addEventListener("input", validateRange);
});





// Находим все элементы с классом h4_pointer
  const h4Elements = document.querySelectorAll('.h4_pointer');

  // Для каждого найденного элемента...
  h4Elements.forEach(function(h4) {
    // Добавляем обработчик события клика
    h4.addEventListener('click', function() {
      // Поиск родительского элемента с классом 'card' относительно текущего h4
      // Это предполагает, что .card всегда будет прямым или ближайшим родителем для h4
      let cardElement = h4.nextElementSibling;
      
      // Переключаем класс 'cardactive' для найденного .card элемента
      cardElement.classList.toggle('cardactive');
    });
  });













// Функция для добавления слушателей на label и span, чтобы переключать чекбокс
function attachListenersForLabelAndSpan(selector) {
    document.querySelectorAll(selector).forEach(container => {
        const input = container.querySelector('input[type="checkbox"]');
        if (!input) return; // Пропустить, если не найден input
        
        // Слушатель для label
        const label = container.querySelector('label');
        label && label.addEventListener('click', (e) => {
            // Предотвращаем дублирующее срабатывание для вложенных событий
            e.stopPropagation();
            input.checked = !input.checked;
            // Здесь можно добавить dispatchEvent, если нужно триггерить событие 'change' на input
        });
        
        // Слушатель для span
        const span = container.querySelector('.check_box');
        span && span.addEventListener('click', (e) => {
            // Предотвращаем дублирующее срабатывание для вложенных событий
            e.stopPropagation();
            input.checked = !input.checked;
            // Здесь можно добавить dispatchEvent, если нужно триггерить событие 'change' на input
        });
    });
}

// Применяем функцию для двух видов контейнеров
attachListenersForLabelAndSpan('.block__filter__brand__input__con');
attachListenersForLabelAndSpan('.block__filter__coin__input__con');