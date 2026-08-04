import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function Login({ onLogin, goToActivate }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  async function handleForgotPassword() {
    if (!email) {
      setMessage("Enter your email first.");
      return;
    }

    const { error } = await supabase.auth.resetPasswordForEmail(email);

    if (error) {
      alert(error.message);
      setMessage(error.message);
      return;
    }

    setMessage("Password reset link sent to your email.");
  }

  async function handleLogin(e) {
    e.preventDefault();

    setMessage("Logging in...");

    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    const user = data.user;

    setMessage("Auth OK - Loading staff...");
    
    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);

    console.log("STAFF RESULT", staffRows, staffError);

    if (staffError) {
      setMessage("STAFF ERROR: " + staffError.message);
      return;
    }

    setMessage("STAFF ROWS: " + String(staffRows ? staffRows.length : 0));

    if (!staffRows || staffRows.length === 0) {
      setMessage("No staff record linked to this account.");
      return;
    }

    const staff = staffRows[0];

    if (staff.status !== "active") {
      setMessage("Account is not active");
      return;
    }

    
onLogin(staff);
    setMessage("AFTER ONLOGIN");

  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>⛽ PetroGuard Enterprise</h1>

      <h3>Sign In</h3>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <br /><br />

        <input
          type={showPassword ? "text" : "password"}
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <br /><br />

        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
        >
          {showPassword ? "🙈 Hide Password" : "👁 Show Password"}
        </button>

        <br /><br />

        <button type="submit">
          Login
        </button>

        <br /><br />

        <button
          type="button"
          onClick={handleForgotPassword}
        >
          Forgot Password?
        </button>

        <br /><br />

        <button
          type="button"
          onClick={goToActivate}
        >
          Activate New Account
        </button>
      </form>

      <p>{message}</p>
    </div>
  );
}
