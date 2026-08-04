from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

# remove broken orphan before first return
code = code.replace(
"""
}


/>;
  }

  return (
      <div style={{padding:20}}>
        <h2>⛽ Pump Reading</h2>
        <p>No active shift found.</p>
""",
"""
  return (
      <div style={{padding:20}}>
        <h2>⛽ Pump Reading</h2>
        <p>No active shift found.</p>
"""
)

p.write_text(code)

print("✅ Broken ShiftActive syntax removed")
