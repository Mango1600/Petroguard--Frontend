from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

old = '''    if (data) {
      setPage("attendantPump");
    } else {
      setPage("open");
    }'''

new = '''    if (data) {

      const { data: existingActivity } = await supabase
        .from("shift_attendants")
        .select("id")
        .eq("shift_id", data.id)
        .eq("staff_id", staff.id)
        .eq("activity_type", "CONTINUED_SHIFT")
        .maybeSingle();

      if (!existingActivity) {
        await supabase
          .from("shift_attendants")
          .insert([{
            shift_id: data.id,
            staff_id: staff.id,
            station_id: staff.station_id,
            activity_type: "CONTINUED_SHIFT"
          }]);
      }

      setPage("attendantPump");
    } else {
      setPage("open");
    }'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Continued shift activity added")
else:
    print("⚠️ Target block not found")
