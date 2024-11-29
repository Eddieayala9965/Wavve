import React from "react";

const ChatList = ({ chats, onSelectChat }) => {
  return (
    <div className="chat-list">
      {chats.map((chat) => (
        <div
          key={chat.id}
          className="chat-item p-3 border-b border-gray-200 hover:bg-gray-100 cursor-pointer"
          onClick={() => onSelectChat(chat.id)}
        >
          <h3 className="font-bold">{chat.name}</h3>
          <p className="text-sm text-gray-500">
            {chat.lastMessage ? chat.lastMessage : "No messages yet"}
          </p>
        </div>
      ))}
    </div>
  );
};

export default ChatList;
