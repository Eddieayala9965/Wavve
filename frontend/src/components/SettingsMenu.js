import React from "react";

const SettingsMenu = ({ onLogout, onThemeChange }) => {
  return (
    <div className="settings-menu p-4 bg-white shadow-lg rounded-lg w-64">
      <h3 className="text-lg font-semibold mb-4">Settings</h3>
      <div className="settings-item mb-4">
        <label className="text-sm font-medium block mb-2">Theme</label>
        <select
          onChange={(e) => onThemeChange(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="light">Light</option>
          <option value="dark">Dark</option>
          <option value="system">System Default</option>
        </select>
      </div>
      <button
        onClick={onLogout}
        className="w-full bg-red-500 text-white p-2 rounded-lg hover:bg-red-600"
      >
        Logout
      </button>
    </div>
  );
};

export default SettingsMenu;
