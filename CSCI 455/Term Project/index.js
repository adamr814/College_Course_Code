import React, { useState } from "react";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

function App() {
  const [activeTab, setActiveTab] = useState("Patient Management");

  const handleTabClick = (tabName) => {
    setActiveTab(tabName);
  };
  return (
    <div className="app-container">
      <header className="top-bar">
        <img src="icon.svg" alt="App Icon" className="app-icon" />
        <nav className="top-nav">
          <button
            onClick={() => {
              /* Implement Notifications Functionality */
            }}
          >
            Notifications
          </button>
          <button
            onClick={() => {
              /* Implement Messages Functionality */
            }}
          >
            Messages
          </button>
          <button
            onClick={() => {
              /* Implement Settings Functionality */
            }}
          >
            Settings
          </button>
          <div className="account-dropdown">
            <button>My Account</button>
            {/* Add dropdown menu content here (currently empty) */}
          </div>
        </nav>
      </header>
      <div className="spacer" /> {/* Spacer to separate top bar */}
      <div className="main-content">
        <aside className="side-menu">
          <ul>
            <li
              className={activeTab === "Patient Management" ? "active" : ""}
              onClick={() => handleTabClick("Patient Management")}
            >
              Patient Management
            </li>
            <li
              className={activeTab === "Appointments" ? "active" : ""}
              onClick={() => handleTabClick("Appointments")}
            >
              Appointments
            </li>
            <li
              className={activeTab === "Labs/Results" ? "active" : ""}
              onClick={() => handleTabClick("Labs/Results")}
            >
              Labs/Results
            </li>
          </ul>
        </aside>
        <div className="content-area">
          {/* Content based on the active tab will be displayed here */}
          {activeTab === "Patient Management" && (
            <div>{/* Patient Management Content */}</div>
          )}
          {activeTab === "Appointments" && (
            <div>{/* Appointments Content */}</div>
          )}
          {activeTab === "Labs/Results" && (
            <div>{/* Labs/Results Content */}</div>
          )}
        </div>
      </div>
    </div>
  );
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
