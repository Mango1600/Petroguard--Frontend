import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function ActivateAccount() {
  const [email, setEmail] = useState("");
  const [activationCode, setActivationCode] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleActivate(e) {
    e.preventDefault();

    if (password !== confirmPassword) {
      setMessage("Passwords do not match.");
      return;
    }

    setMessage(
      "Activation module is ready. Next step is connecting it to Staff Management."
    );
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>⛽ PetroGuard Enterprise</h1>

      <h2>Activate New Account</h2>

      <form onSubmit={handleActivate}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <br /><br />

        <input
          type="text"
          placeholder="Activation Code"
          value={activationCode}
          onChange={(e) => setActivationCode(e.target.value)}
        />

        <br /><br />

        <input
          type="password"
          placeholder="Create Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <br /><br />

        <input
          type="password"
          placeholder="Confirm Password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />

        <br /><br />

        <button type="submit">
          Activate Account
        </button>
      </form>

      <p>{message}</p>
    </div>
  );
}