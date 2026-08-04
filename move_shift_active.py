from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

block = """
if(shiftStarted){
    return <ShiftActive shift={{
      id: shift?.id,
      opening_meter: 1000
    }}/>;
  }
"""

code = code.replace(block, "")

insert = """
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

code = code.replace("  return (", insert + "  return (", 1)

p.write_text(code)

print("✅ ShiftActive moved before return")
