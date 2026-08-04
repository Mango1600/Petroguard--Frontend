import Dashboard from "./pages/Dashboard";

export default function App() {
  return (
    <Dashboard
      staff={{
        name: "Test User",
        role: "Developer",
        station_id: 1,
      }}
    />
  );
}