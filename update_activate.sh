#!/data/data/com.termux/files/usr/bin/bash

cd ~/petroguard-frontend || exit 1

echo "Creating backups..."

cp src/App.jsx src/App_before_activate.bak
cp src/pages/Login.jsx src/pages/Login_before_activate.bak

echo "Updating App.jsx..."

cat > src/App.jsx << 'APP'
import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import ActivateAccount from "./pages/ActivateAccount";

export default function App() {
  const [staff, setStaff] = useState(null);
  const [page, setPage] = useState("login");

  if (!staff) {
    if (page === "activate") {
      return (
        <ActivateAccount
          goToLogin={() => setPage("login")}
        />
      );
    }

    return (
      <Login
        onLogin={setStaff}
        goToActivate={() => setPage("activate")}
      />
    );
  }

  return <Dashboard staff={staff} />;
}
APP

echo "Updating Login.jsx..."

sed -i \
's/export default function Login({ onLogin }) {/export default function Login({ onLogin, goToActivate }) {/' \
src/pages/Login.jsx

sed -i '/<button type="submit">/,/<\/button>/a\
\
        <br /><br />\
\
        <button\
          type="button"\
          onClick={goToActivate}\
        >\
          Activate New Account\
        </button>' src/pages/Login.jsx

echo "Update completed."
echo "Backups created:"
echo "src/App_before_activate.bak"
echo "src/pages/Login_before_activate.bak"

