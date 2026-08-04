from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
text = p.read_text()

old = '''    setActiveShift(newShift);

    setMessage("✅ Shift opened");'''

new = '''    setActiveShift(newShift);

    await supabase
      .from("shift_attendants")
      .insert([{
        shift_id: newShift.id,
        staff_id: staff.id,
        station_id: staff.station_id,
        activity_type: "OPENED_SHIFT"
      }]);

    setMessage("✅ Shift opened");'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Opening attendant activity added")
else:
    print("⚠️ Target block not found")
