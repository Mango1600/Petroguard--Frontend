from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
text = p.read_text()

# Remove closing meter state
text = text.replace(
'const [closingMeter, setClosingMeter] = useState("");',
''
)

# Remove closing calculation save function
start = text.find("async function saveReading()")
end = text.find("if (!shift)")

if start != -1 and end != -1:
    text = text[:start] + text[end:]

# Remove closing meter input block
start = text.find('<input\n        type="number"\n        placeholder="Closing Meter"')
if start != -1:
    end = text.find('</input>', start)
    if end == -1:
        end = text.find('/>', start) + 2
    text = text[:start] + text[end:]

# Remove save button
start = text.find('💾 SAVE PUMP READING')
if start != -1:
    btn_start = text.rfind('<button', 0, start)
    btn_end = text.find('</button>', start) + len('</button>')
    text = text[:btn_start] + text[btn_end:]

p.write_text(text)

print("✅ Active shift changed to opening-only workflow")
