from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

bad = """
};


/>;
  }
"""

good = """
}

if(shiftStarted){
  return (
    <ShiftActive
      shift={{
        id: shift?.id,
        opening_meter: 1000
      }}
    />
  );
}
"""

if bad in code:
    code = code.replace(bad, good)
    p.write_text(code)
    print("✅ ShiftActive block repaired")
else:
    print("❌ Broken block not found")
