from pathlib import Path
import shutil

dashboard = Path("src/pages/Dashboard.jsx")
backup = Path("src/pages/Dashboard_production_backup.jsx")

if dashboard.exists() and not backup.exists():
    shutil.copy(dashboard, backup)

dashboard.write_text("""
export default function Dashboard({ staff }) {
  return (
    <div style={{padding:20}}>
      <h1>PetroGuard Dashboard</h1>

      <h2>Developer Login Successful</h2>

      <p>Name: {staff?.name}</p>

      <p>Role: {staff?.role}</p>

      <p>Station: {staff?.station_id}</p>
    </div>
  );
}
""", encoding="utf-8")

print("✅ Dashboard isolated.")
