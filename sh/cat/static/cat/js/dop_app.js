let minValue2 = document.getElementById("min-power");
let maxValue2 = document.getElementById("max-power");

// Function to validate range and update the fill color on slider
function validateRange2() {
  let minPower = parseInt(document.querySelector(".min-power").value);
  let maxPower = parseInt(document.querySelector(".max-power").value);

  if (minPower > maxPower) {
    let tempValue = maxPower;
    maxPower = minPower;
    minPower = tempValue;
  }

  minValue2.textContent = minPower; // используем textContent для обновления текста
  maxValue2.textContent = maxPower;
}

// Выбираем оба элемента input
const inputElements2 = document.querySelectorAll(".min-power, .max-power");

// Добавляем обработчик события на каждый элемент
inputElements2.forEach((element) => {
  element.addEventListener("input", validateRange2); // Здесь используется событие "input"
});

// Первоначальный вызов функции для инициализации значений
validateRange2();