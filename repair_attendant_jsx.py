from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

old = '''
    )}
      ) : (
        <p style={{color:"green",fontWeight:"bold"}}>
'''

new = '''
    )}
'''

code = code.replace(old, new)

p.write_text(code)

print("✅ JSX repaired")
