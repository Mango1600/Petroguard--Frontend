from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

# Remove first debug pre block
start = text.find('    <pre\n      style={{')
end = text.find('    </pre>', start)

if start != -1 and end != -1:
    end = end + len('    </pre>')
    text = text[:start] + text[end:]
    print("✅ Removed first debug block")
else:
    print("⚠️ First debug block not found")

# Remove second debug return block
start = text.find('return (\n  <div style={{padding:20}}>')

if start != -1:
    end = text.find(');', start)
    if end != -1:
        end += 2
        text = text[:start] + text[end:]
        print("✅ Removed second debug return")
else:
    print("⚠️ Second debug return not found")

file.write_text(text)
