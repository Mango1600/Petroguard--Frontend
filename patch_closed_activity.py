from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")
text = p.read_text()

old = '''    setMessage(`✅ Closing saved. PetroGuard calculated ${litres} litres`);'''

new = '''    await supabase
      .from("shift_attendants")
      .insert([{
        shift_id: shift.id,
        staff_id: staff.id,
        station_id: staff.station_id,
        activity_type: "CLOSED_SHIFT"
      }]);

    setMessage(`✅ Closing saved. PetroGuard calculated ${litres} litres`);'''

if old in text:
    text = text.replace(old,new)
    p.write_text(text)
    print("✅ Closing attendant activity added")
else:
    print("⚠️ Closing save message block not found")
