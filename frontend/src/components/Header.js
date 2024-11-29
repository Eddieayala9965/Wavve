import React from "react";

const Header = ({ chatName, onBack }) => {
  return (
    <div className="header bg-blue-500 text-white p-4 flex justify-between items-center">
      <button onClick={onBack} className="text-sm hover:underline">
        Back
      </button>
      <h2 className="text-lg font-bold">{chatName}</h2>
    </div>
  );
};

export default Header;
