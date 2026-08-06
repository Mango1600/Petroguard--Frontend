from pathlib import Path

p = Path("src/services/evidenceService.js")
text = p.read_text()

text = text.replace(
'console.error("Evidence Upload Error:", error);',
'console.error("Evidence Upload Error FULL:", JSON.stringify(error, null, 2));'
)

p.write_text(text)

print("✅ Debug added")
