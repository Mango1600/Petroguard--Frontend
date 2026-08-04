from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

first = code.find("if(shiftStarted){")
second = code.find("if(shiftStarted){", first + 1)

if second != -1:
    end = code.find("}", second)

    block = code[second:end+2]

    code = code.replace(block, "", 1)

    p.write_text(code)

    print("✅ Duplicate ShiftActive removed")
else:
    print("✅ No duplicate found")
