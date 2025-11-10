# Calculator Logic

This document specifies the logic for the calculator.

## Operations

The calculator supports the following operations:

### Basic Operations

- **Add:** `a + b`
- **Subtract:** `a - b`
- **Multiply:** `a * b`
- **Divide:** `a / b`

### Advanced Operations

- **Percentage:** `a %` (divides the number by 100)
- **Square Root:** `√a`
- **Power:** `a ^ b`

## Error Handling

The calculator handles the following error conditions:

- **Division by Zero:** If the user attempts to divide by zero, the calculator will display an "Error" message.
- **Invalid Input:** The calculator will prevent multiple decimal points in a single number.

## Implementation

The calculator logic is implemented in the `frontend/utils/calculate.ts` file. The `calculate` function takes the current state of the calculator and the button pressed as input, and returns the new state.
