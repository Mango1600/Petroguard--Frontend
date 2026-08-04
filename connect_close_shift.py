from pathlib import Path

f=Path("src/pages/ShiftActive.jsx")
t=f.read_text()

if 'import ClosingPumpMeter' not in t:
    t=t.replace(
        'import AttendantHandover from "./AttendantHandover";',
        'import AttendantHandover from "./AttendantHandover";\nimport ClosingPumpMeter from "./ClosingPumpMeter";'
    )

t=t.replace(
    'const [handover,setHandover]=useState(false);',
    '''const [handover,setHandover]=useState(false);
const [closing,setClosing]=useState(false);'''
)

t=t.replace(
    'if(handover){',
    '''if(closing){
  return <ClosingPumpMeter shift={shift}/>;
}

if(handover){'''
)

t=t.replace(
'''<button style={{width:"100%",padding:12}}>
🔴 Close Pump Shift
</button>''',
'''<button
style={{width:"100%",padding:12}}
onClick={()=>setClosing(true)}
>
🔴 Close Pump Shift
</button>'''
)

f.write_text(t)

print("✅ Close Pump Shift connected")
