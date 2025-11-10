"use client";
import { useState } from "react";

export default function Calculator() {
  const [input, setInput] = useState("0");

  const handleClick = (value: string) => {
    if (value === "AC") return setInput("0");
    if (value === "=") {
      try {
        // eslint-disable-next-line no-eval
        setInput(eval(input.replace("×", "*").replace("÷", "/")).toString());
      } catch {
        setInput("Error");
      }
      return;
    }
    setInput((prev) => (prev === "0" ? value : prev + value));
  };

  const buttons = [
    "AC", "+", "/", "%", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "−",
    "1", "2", "3", "+",
    "0", ".", "=",
  ];

  return (
    <div className="flex items-center justify-center min-h-screen bg-pink-100">
      <div className="bg-pink-200 rounded-2xl shadow-2xl p-6 w-80 border-4 border-pink-300">
        <div className="bg-white rounded-lg p-4 mb-4 text-right text-3xl font-mono shadow-inner">
          {input}
        </div>
        <div className="grid grid-cols-4 gap-3">
          {buttons.map((btn) => (
            <button
              key={btn}
              onClick={() => handleClick(btn)}
              className={`py-3 rounded-xl text-xl font-semibold shadow ${
                btn === "="
                  ? "bg-pink-500 text-white hover:bg-pink-600"
                  : "bg-white hover:bg-pink-300"
              }`}
            >
              {btn}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
