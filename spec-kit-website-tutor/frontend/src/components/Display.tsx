import React from 'react';

interface DisplayProps {
  value: string;
}

const Display: React.FC<DisplayProps> = ({ value }) => {
  return (
    <div className="bg-gray-800 text-white text-5xl font-bold text-right p-4 rounded-t-lg break-all">
      {value}
    </div>
  );
};

export default Display;
