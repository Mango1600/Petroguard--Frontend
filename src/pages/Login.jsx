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

    console.log("AUTH ERROR:", error);
    console.log("AUTH DATA:", data);

    if (error) {
      setMessage(error.message);
      return;
    }

    if (!data?.user) {
      setMessage("No authenticated user returned.");
      return;
    }

    const user = data.user;

    alert(JSON.stringify({
      auth_user: data.user,
      auth_session: data.session
    }, null, 2));

    setMessage("MARKER 2026 - BEFORE STAFF QUERY");
    
    const staffPromise = supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id)
      .limit(1);

    const timeoutPromise = new Promise((_, reject) =>
      setTimeout(() => reject(new Error("STAFF QUERY TIMEOUT")), 10000)
    );

    const { data: staffRows, error: staffError } =
      await Promise.race([staffPromise, timeoutPromise]);

    console.log("STAFF RESULT", staffRows, staffError);

    if (staffError) {
      setMessage("STAFF ERROR: " + staffError.message);
      return;
    }

    if (!staffRows || staffRows.length === 0) {
      setMessage("No staff record linked to this account.");
      return;
    }

    const staff = staffRows[0];

    if (staff.status !== "active") {
      setMessage("Account is not active");
      return;
    }

    alert("MARKER 2026 - STAFF FOUND\\n" + JSON.stringify(staff, null, 2));

    onLogin(staff);

    alert("MARKER 2026 - AFTER onLogin");

    return;
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
