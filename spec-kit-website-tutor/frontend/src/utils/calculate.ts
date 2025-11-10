export type State = {
  current: string;
  prev: string;
  operation: string;
  display: string;
};

export const calculate = (state: State, button: string): State => {
  let { current, prev, operation, display } = state;

  const updateDisplay = (value: string) => {
    display = value;
  };

  const handleNumber = (num: string) => {
    if (current === '0' && num === '0') return;
    if (current.includes('.') && num === '.') return;
    if (operation && prev && !current) {
      current = num;
    } else {
      current = current === '0' ? num : current + num;
    }
    updateDisplay(current);
  };

  const handleOperation = (op: string) => {
    if (current && prev && operation) {
      handleEquals();
      prev = display;
      current = '';
      operation = op;
    } else {
      operation = op;
      if (current) {
        prev = current;
        current = '';
      }
    }
  };

  const handleEquals = () => {
    if (!operation || !prev) return;
    const a = parseFloat(prev);
    const b = parseFloat(current || prev);
    let result: number;
    switch (operation) {
      case '+':
        result = a + b;
        break;
      case '-':
        result = a - b;
        break;
      case '*':
        result = a * b;
        break;
      case '/':
        if (b === 0) {
          updateDisplay('Error');
          current = '';
          prev = '';
          operation = '';
          return;
        }
        result = a / b;
        break;
      case '^':
        result = Math.pow(a, b);
        break;
      default:
        return;
    }
    updateDisplay(result.toString());
    prev = result.toString();
    current = '';
    operation = '';
  };

  const handleAdvanced = (op: string) => {
    const num = parseFloat(current || prev);
    if (isNaN(num)) return;
    let result: number;
    switch (op) {
      case '%':
        result = num / 100;
        break;
      case '√':
        result = Math.sqrt(num);
        break;
      default:
        return;
    }
    updateDisplay(result.toString());
    current = result.toString();
  };

  const handleClear = () => {
    current = '0';
    prev = '';
    operation = '';
    updateDisplay('0');
  };

  const handlePlusMinus = () => {
    if (!current) return;
    current = (parseFloat(current) * -1).toString();
    updateDisplay(current);
  };

  if (!isNaN(parseInt(button)) || button === '.') {
    handleNumber(button);
  } else if (['+', '-', '*', '/', '^'].includes(button)) {
    handleOperation(button);
  } else if (button === '=') {
    handleEquals();
  } else if (['%', '√'].includes(button)) {
    handleAdvanced(button);
  } else if (button === 'AC') {
    handleClear();
  } else if (button === '+/-') {
    handlePlusMinus();
  }

  return { current, prev, operation, display };
};
