from pathlib import Path

p = Path("src/services/evidenceService.js")
text = p.read_text()

old = 'console.log("EVIDENCE INSERT DATA", {'

new = 'alert(JSON.stringify({companyId, stationId, uploadedBy, recordId, moduleName, evidenceType}));\n\n    console.log("EVIDENCE INSERT DATA", {'

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Alert debug added.")
else:
    print("Already patched or text changed.")
