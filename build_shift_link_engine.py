from pathlib import Path

p=Path("src/pages/CashDeclaration.jsx")
t=p.read_text()

t=t.replace(
"shift_id: shift?.id,",
"""shift_id:
shift?.staff_shift_id ??
shift?.shift_id ??
shift?.id,"""
)

t=t.replace(
"staff_id: shift?.staff_id,",
"""staff_id:
shift?.staff_id,"""
)

p.write_text(t)

print("✅ Shift link engine applied")
