from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

if 'import ShiftActive from "./ShiftActive";' not in code:
    code = code.replace(
        'import CameraCapture from "../components/CameraCapture";',
        'import CameraCapture from "../components/CameraCapture";\nimport ShiftActive from "./ShiftActive";'
    )

if "const [shiftStarted" not in code:
    code = code.replace(
        'const [message, setMessage] = useState("");',
        'const [message, setMessage] = useState("");\n  const [shiftStarted,setShiftStarted]=useState(false);'
    )

old = 'onClick={() => setMessage("▶ Operation Started")}'

new = 'onClick={() => setShiftStarted(true)}'

code = code.replace(old,new)

# Insert Shift Active before the return ending
code = code.replace(
    'return (',
    '''if(shiftStarted){
    return <ShiftActive shift={{
      id: shift?.id,
      opening_meter: 1000
    }}/>;
  }

  return ('''
)

p.write_text(code)

print("✅ START OPERATION connected to Shift Active")
