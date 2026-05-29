```javascript
const calculator = {
  displayValue: '0',
  firstOperand: null,
  operator: null,
  secondOperand: false
};

function updateDisplay() {
  const display = document.querySelector('.calculator-display');
  display.value = calculator.displayValue;
}

function inputDigit(digit) {
  const { displayValue, secondOperand } = calculator;

  if (secondOperand === true) {
    calculator.displayValue = digit;
    calculator.secondOperand = false;
  } else {
    calculator.displayValue = displayValue === '0' ? digit : displayValue + digit;
  }

  updateDisplay();
}

function inputDecimal() {
  const { displayValue } = calculator;

  if (displayValue.includes('.')) return;

  calculator.displayValue = displayValue + '.';
  updateDisplay();
}

function handleOperator(nextOperator) {
  const { firstOperand, displayValue, operator } = calculator;

  const value = parseFloat(displayValue);

  if (firstOperand === null) {
    calculator.firstOperand = value;
  } else if (operator) {
    const result = calculate(firstOperand, operator, value);

    calculator.displayValue = result.toString();
    calculator.firstOperand = result;
  }

  calculator.secondOperand = true;
  calculator.operator = nextOperator;
  updateDisplay();
}

function calculate(first, operator, second) {
  if (operator === '+') {
    return first + second;
  } else if (operator === '-') {
    return first - second;
  } else if (operator === '*') {
    return first * second;
  } else if (operator === '/') {
    if (second === 0) {
      throw new Error('Cannot divide by zero');
    }
    return first / second;
  }

  return second;
}

function resetCalculator() {
  calculator.displayValue = '0';
  calculator.firstOperand = null;
  calculator.operator = null;
  calculator.secondOperand = false;
  updateDisplay();
}

function deleteDigit() {
  const displayValue = calculator.displayValue;
  calculator.displayValue = displayValue.slice(0, -1);
  if (calculator.displayValue === '') {
    calculator.displayValue = '0';
  }
  updateDisplay();
}

const keys = document.querySelector('.calculator-keys');

keys.addEventListener('click', (event) => {
  const { target } = event;
  const { value } = target;

  if (!target.matches('button')) {
    return;
  }

  switch (value) {
    case '+':
    case '-':
    case '*':
    case '/':
      handleOperator(value);
      break;
    case '=':
      if (calculator.firstOperand !== null && calculator.operator !== null) {
        const result = calculate(calculator.firstOperand, calculator.operator, parseFloat(calculator.displayValue));
        calculator.displayValue = result.toString();
        calculator.firstOperand = null;
        calculator.operator = null;
        calculator.secondOperand = false;
      }
      break;
    case '.':
      inputDecimal();
      break;
    case 'all-clear':
      resetCalculator();
      break;
    case 'delete':
      deleteDigit();
      break;
    default:
      if (Number.isInteger(Number(value))) {
        inputDigit(value);
      }
  }

  updateDisplay();
});
```