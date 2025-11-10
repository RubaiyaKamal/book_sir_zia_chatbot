import React from 'react';

interface ButtonProps {
  label: string;
  onClick: (label: string) => void;
  className?: string;
}

const Button: React.FC<ButtonProps> = ({ label, onClick, className }) => {
  return (
    <button
      onClick={() => onClick(label)}
      className={`bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-2xl font-bold rounded-lg ${className}`}>
      {label}
    </button>
  );
};

export default Button;
