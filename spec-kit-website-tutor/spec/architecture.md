# Project Architecture

This document outlines the architecture of the calculator web application.

## Directory Structure

The project is organized into the following directories:

- `frontend/`: Contains the Next.js 15 frontend application.
- `frontend/components/`: Reusable UI components for the calculator.
- `frontend/utils/`: Helper functions, including the calculator logic.
- `frontend/app/`: Main pages of the application, using the Next.js App Router.
- `spec/`: Contains the project specifications and documentation managed by SpecKit.
- `env/`: Python virtual environment setup for any potential backend or Python-based scripts.

## Frontend

The frontend is built with Next.js 15 and TypeScript. It uses Tailwind CSS for styling. The application is designed to be a Single Page Application (SPA) with all the calculator functionality on the main page.

### Components

- `Calculator.tsx`: The main component that assembles the calculator interface.
- `Display.tsx`: The screen of the calculator that shows the input and the result.
- `Button.tsx`: A reusable button component for the calculator keys.

### State Management

The calculator's state (current number, previous number, operation) is managed within the `Calculator.tsx` component using React hooks (`useState`).

## Backend

For this project, the calculator logic is implemented in TypeScript on the frontend. There is no separate backend server. The `env/` directory is set up for potential future use, such as adding features that might require a Python backend.
