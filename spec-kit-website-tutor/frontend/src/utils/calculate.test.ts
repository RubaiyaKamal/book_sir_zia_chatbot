import { calculate, State } from './calculate';

describe('calculate', () => {
  let state: State;

  beforeEach(() => {
    state = { current: '0', prev: '', operation: '', display: '0' };
  });

  it('should handle number input', () => {
    state = calculate(state, '5');
    expect(state.current).toBe('5');
    expect(state.display).toBe('5');
  });

  it('should handle multiple number inputs', () => {
    state = calculate(state, '5');
    state = calculate(state, '3');
    expect(state.current).toBe('53');
    expect(state.display).toBe('53');
  });

  it('should handle decimal input', () => {
    state = calculate(state, '5');
    state = calculate(state, '.');
    state = calculate(state, '3');
    expect(state.current).toBe('5.3');
    expect(state.display).toBe('5.3');
  });

  it('should not allow multiple decimals', () => {
    state = calculate(state, '5.3');
    state = calculate(state, '.');
    expect(state.current).toBe('5.3');
  });

  it('should handle addition', () => {
    state = calculate(state, '5');
    state = calculate(state, '+');
    state = calculate(state, '3');
    state = calculate(state, '=');
    expect(state.display).toBe('8');
  });

  it('should handle subtraction', () => {
    state = calculate(state, '5');
    state = calculate(state, '-');
    state = calculate(state, '3');
    state = calculate(state, '=');
    expect(state.display).toBe('2');
  });

  it('should handle multiplication', () => {
    state = calculate(state, '5');
    state = calculate(state, '*');
    state = calculate(state, '3');
    state = calculate(state, '=');
    expect(state.display).toBe('15');
  });

  it('should handle division', () => {
    state = calculate(state, '6');
    state = calculate(state, '/');
    state = calculate(state, '3');
    state = calculate(state, '=');
    expect(state.display).toBe('2');
  });

  it('should handle division by zero', () => {
    state = calculate(state, '6');
    state = calculate(state, '/');
    state = calculate(state, '0');
    state = calculate(state, '=');
    expect(state.display).toBe('Error');
  });

  it('should handle percentage', () => {
    state = calculate(state, '5');
    state = calculate(state, '%');
    expect(state.display).toBe('0.05');
  });

  it('should handle square root', () => {
    state = calculate(state, '9');
    state = calculate(state, '√');
    expect(state.display).toBe('3');
  });

  it('should handle power', () => {
    state = calculate(state, '2');
    state = calculate(state, '^');
    state = calculate(state, '3');
    state = calculate(state, '=');
    expect(state.display).toBe('8');
  });

  it('should handle clear', () => {
    state = calculate(state, '5');
    state = calculate(state, '+');
    state = calculate(state, '3');
    state = calculate(state, 'AC');
    expect(state.current).toBe('0');
    expect(state.prev).toBe('');
    expect(state.operation).toBe('');
    expect(state.display).toBe('0');
  });

  it('should handle plus/minus', () => {
    state = calculate(state, '5');
    state = calculate(state, '+/-');
    expect(state.current).toBe('-5');
    expect(state.display).toBe('-5');
    state = calculate(state, '+/-');
    expect(state.current).toBe('5');
    expect(state.display).toBe('5');
  });
});
