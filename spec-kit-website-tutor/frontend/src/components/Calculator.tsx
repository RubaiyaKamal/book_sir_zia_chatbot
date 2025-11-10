"use client";

import React, { useState } from 'react';
import Display from './Display';
import Button from './Button';
import { calculate, State } from '../utils/calculate';

const Calculator: React.FC = () => {
  const [state, setState] = useState<State>({ current: '0', prev: '', operation: '', display: '0' });

  const handleButtonClick = (button: string) => {
    setState(calculate(state, button));
  };

  return (
    <div className="w-full max-w-md mx-auto shadow-lg rounded-lg bg-white dark:bg-black">
      <Display value={state.display} />
      <div className="grid grid-cols-4 gap-1 p-1">
        <Button label="AC" onClick={handleButtonClick} className="col-span-2 bg-red-400 dark:bg-red-600" />
        <Button label="+/-" onClick={handleButtonClick} className="bg-gray-400 dark:bg-gray-500" />
        <Button label="/" onClick={handleButtonClick} className="bg-orange-400 dark:bg-orange-600" />

        <Button label="7" onClick={handleButtonClick} />
        <Button label="8" onClick={handleButtonClick} />
        <Button label="9" onClick={handleButtonClick} />
        <Button label="*" onClick={handleButtonClick} className="bg-orange-400 dark:bg-orange-600" />

        <Button label="4" onClick={handleButtonClick} />
        <Button label="5" onClick={handleButtonClick} />
        <Button label="6" onClick={handleButtonClick} />
        <Button label="-" onClick={handleButtonClick} className="bg-orange-400 dark:bg-orange-600" />

        <Button label="1" onClick={handleButtonClick} />
        <Button label="2" onClick={handleButtonClick} />
        <Button label="3" onClick={handleButtonClick} />
        <Button label="+" onClick={handleButtonClick} className="bg-orange-400 dark:bg-orange-600" />

        <Button label="0" onClick={handleButtonClick} className="col-span-2" />
        <Button label="." onClick={handleButtonClick} />
        <Button label="=" onClick={handleButtonClick} className="bg-orange-400 dark:bg-orange-600" />

        <Button label="%" onClick={handleButtonClick} className="bg-gray-400 dark:bg-gray-500" />
        <Button label="√" onClick={handleButtonClick} className="bg-gray-400 dark:bg-gray-500" />
        <Button label="^" onClick={handleButtonClick} className="bg-gray-400 dark:bg-gray-500" />
      </div>
    </div>
  );
};

export default Calculator;
