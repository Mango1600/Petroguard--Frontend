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

    console.log("========== AUTH RESULT ==========");
    console.log("AUTH DATA:", data);
    console.log("AUTH USER:", data?.user);
    console.log("AUTH SESSION:", data?.session);
    console.log("AUTH ERROR:", error);
    console.log("================================");


    if (error) {
      setMessage(error.message);
      return;
    }

    const user = data.user;

    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);

    if (staffError) {
      console.log(staffError);
      setMessage(staffError.message);
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

    
console.log("LOGIN SUCCESS", staff);
alert("LOGIN SUCCESS: " + JSON.stringify(staff));
onLogin(staff);

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
