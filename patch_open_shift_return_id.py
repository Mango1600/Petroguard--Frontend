from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
text = p.read_text()

text = text.replace(
'const { error } = await supabase\n      .from("staff_shifts")',
'const { data: newShift, error } = await supabase\n      .from("staff_shifts")'
)

text = text.replace(
'      }]);',
'      }])\n      .select()\n      .single();',
1
)

p.write_text(text)

print("✅ OpenShift now returns new shift ID")
