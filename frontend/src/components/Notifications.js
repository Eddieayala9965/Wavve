import React from "react";

const Notifications = ({ notifications, onClose }) => {
  return (
    <div className="notifications fixed top-0 right-0 m-4 w-80">
      {notifications.map((notification, index) => (
        <div
          key={index}
          className="notification bg-blue-500 text-white p-3 mb-2 rounded-lg shadow-lg flex justify-between items-center"
        >
          <span>{notification.message}</span>
          <button
            onClick={() => onClose(index)}
            className="text-sm text-white hover:underline"
          >
            Close
          </button>
        </div>
      ))}
    </div>
  );
};

export default Notifications;
