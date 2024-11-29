"use client";

import { useEffect } from "react";
import { useNotificationsStore } from "@/store/notificationsStore";

export default function Notifications() {
  const { notifications, fetchNotifications, clearNotification } =
    useNotificationsStore();

  useEffect(() => {
    // Fetch notifications when the component loads
    fetchNotifications();
  }, [fetchNotifications]);

  if (!notifications.length) {
    return (
      <div className="p-4 text-center">
        <p className="text-gray-500">No notifications at the moment.</p>
      </div>
    );
  }

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Notifications</h2>
      <ul className="space-y-4">
        {notifications.map((notification) => (
          <li
            key={notification.id}
            className="p-4 border rounded hover:shadow cursor-pointer flex justify-between items-center"
          >
            <div>
              <p className="text-gray-800">{notification.message}</p>
              <p className="text-sm text-gray-500">
                {new Date(notification.timestamp).toLocaleString()}
              </p>
            </div>
            <button
              className="ml-4 px-3 py-1 bg-red-500 text-white text-sm rounded hover:bg-red-600"
              onClick={() => clearNotification(notification.id)}
            >
              Clear
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
