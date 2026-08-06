from pathlib import Path

p = Path("src/services/evidenceService.js")

text = p.read_text()

old = '''    const { data: evidence, error: evidenceError } =
      await supabase
        .from("evidence")
        .insert({'''

new = '''    console.log("EVIDENCE INSERT DATA", {
      companyId,
      stationId,
      uploadedBy,
      recordId,
      moduleName,
      evidenceType
    });

    const { data: evidence, error: evidenceError } =
      await supabase
        .from("evidence")
        .insert({'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Evidence insert debug added.")
else:
    print("Nothing patched. Check current file.")
