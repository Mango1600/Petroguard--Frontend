from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

# remove wrong location
text = text.replace(
'  console.log("ASSIGNMENT PAYLOAD", payload);\n\n',
''
)

# add correct location before insert
old = '''  const { data, error } = await supabase
    .from("attendant_assignments")'''

new = '''  console.log("ASSIGNMENT PAYLOAD", payload);

  const { data, error } = await supabase
    .from("attendant_assignments")'''

text = text.replace(old, new, 1)

file.write_text(text)

print("Payload log moved correctly")
