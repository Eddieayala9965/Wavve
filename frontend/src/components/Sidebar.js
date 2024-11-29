import React from "react";

const Sidebar = ({ chats, onSelectChat, onSettings }) => {
  return (
    <div className="sidebar w-1/4 bg-gray-100 p-4 border-r border-gray-300">
      <h2 className="text-lg font-bold mb-4">Chats</h2>
      <div>
        {chats.map((chat) => (
          <div
            key={chat.id}
            className="p-2 hover:bg-gray-200 cursor-pointer"
            onClick={() => onSelectChat(chat.id)}
          >
            {chat.name}
          </div>
        ))}
      </div>
      <button
        onClick={onSettings}
        className="mt-4 p-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Settings
      </button>
    </div>
  );
};

export default Sidebar;
