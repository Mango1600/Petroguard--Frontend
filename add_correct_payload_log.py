from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

old = """  const { data, error } = await supabase              .from("attendant_assignments")"""

new = """  console.log("ASSIGNMENT PAYLOAD", payload);

  const { data, error } = await supabase              .from("attendant_assignments")"""

if old in text:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("Correct payload log added")
else:
    print("Target not found")
