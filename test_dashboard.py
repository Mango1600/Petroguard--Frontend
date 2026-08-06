from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
export default function Dashboard({ staff }) {
  return (
    <div style={{padding:"30px", color:"black", background:"white"}}>
      DASHBOARD TEST<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Dashboard test created")
