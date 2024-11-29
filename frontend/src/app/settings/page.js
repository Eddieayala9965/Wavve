import React from "react";
import AccountSettings from "./account";
import ThemeSettings from "./theme";

const SettingsPage = () => {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Settings</h1>
      <div style={{ marginBottom: "40px" }}>
        <h2>Account Settings</h2>
        <AccountSettings />
      </div>
      <div>
        <h2>Theme Settings</h2>
        <ThemeSettings />
      </div>
    </div>
  );
};

export default SettingsPage;
