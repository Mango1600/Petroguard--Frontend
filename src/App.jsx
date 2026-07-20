import { useState, useEffect } from "react";
import { supabase } from "./lib/supabase";
import Dashboard from "./pages/Dashboard";

function App() {
  const [loggedIn, setLoggedIn] = useState(null);
  const [staff, setStaff] = useState(null);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    checkSession();
  }, []);

  async function checkSession() {
    const { data } = await supabase.auth.getSession();

    if (data.session) {
      await loadStaff(data.session.user.id);
      setLoggedIn(true);
    } else {
      setLoggedIn(false);
    }
  }

  async function loadStaff(userId) {
    const { data, error } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", userId)
      .single();

    if (error) {
      console.error(error);
      setMessage("Staff profile not found");
      return;
    }

    setStaff(data);
  }

  async function handleLogin(e) {
    e.preventDefault();

    const { data, error } =
      await supabase.auth.signInWithPassword({
        email,
        password,
      });
console.log("LOGIN USER ID:", data.user.id);
console.log("LOGIN EMAIL:", data.user.email);

    if (error) {
      setMessage(error.message);
      return;
    }

    await loadStaff(data.user.id);

    setLoggedIn(true);
  }

  if (loggedIn === null) {
    return <p>Loading...</p>;
  }

  if (loggedIn && staff) {
    return (
      <Dashboard staff={staff} />
    );
  }

  if (loggedIn && !staff) {
    return (
      <div>
        <h2>Staff profile missing</h2>
        <p>{message}</p>
      </div>
    );
  }

  return (
    <div>
      <h1>PetroGuard</h1>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <br />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <br />

        <button type="submit">
          Login
        </button>
      </form>

      <p>{message}</p>
    </div>
  );
}

export default App;

