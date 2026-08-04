import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";

// eruda disabled for test

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);