import React from "react";
import MessageBubble from "./MessageBubble";

const ChatThread = ({ messages, currentUserId }) => {
  return (
    <div className="chat-thread p-4 overflow-y-scroll h-full">
      {messages.map((message) => (
        <MessageBubble
          key={message.id}
          message={message}
          isOwnMessage={message.senderId === currentUserId}
        />
      ))}
    </div>
  );
};

export default ChatThread;
