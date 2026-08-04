from pathlib import Path

file = Path("src/pages/AttendantPumpReading.jsx")

code = file.read_text()

first = code.find("async function saveEvidence(fileData){")
second = code.find("async function saveEvidence(fileData){", first + 1)

if second != -1:
    end = code.find("return (", second)

    if end != -1:
        code = code[:second] + code[end:]

        file.write_text(code)
        print("✅ Duplicate saveEvidence removed")
    else:
        print("❌ Could not find duplicate end")
else:
    print("✅ No duplicate found")
