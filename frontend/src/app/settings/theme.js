import React, { useState, useEffect } from "react";

const ThemeSettings = () => {
  const [theme, setTheme] = useState(
    () => localStorage.getItem("theme") || "light"
  );

  useEffect(() => {
    document.body.className = theme;
    localStorage.setItem("theme", theme);
  }, [theme]);

  const toggleTheme = () => {
    const newTheme = theme === "light" ? "dark" : "light";
    setTheme(newTheme);
  };

  return (
    <div>
      <h1>Theme Settings</h1>
      <p>Switch between light and dark themes:</p>
      <button onClick={toggleTheme}>
        {theme === "light" ? "Switch to Dark Mode" : "Switch to Light Mode"}
      </button>
      <p>Current Theme: {theme}</p>
    </div>
  );
};

export default ThemeSettings;
