import React from "react";

const TypingIndicator = ({ isTyping }) => {
  if (!isTyping) return null;

  return (
    <div className="typing-indicator p-3 text-sm text-gray-500">
      Someone is typing...
    </div>
  );
};

export default TypingIndicator;
