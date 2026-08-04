from pathlib import Path

p = Path("src/pages/ShiftActive.jsx")
code = p.read_text()

if 'import AttendantHandover' not in code:
    code = 'import AttendantHandover from "./AttendantHandover";\n' + code

code = code.replace(
'''export default function ShiftActive({shift}){     
return (
<div style={{padding:20}}>''',
'''export default function ShiftActive({shift}){

const [handover,setHandover] = React.useState(false);

if(handover){
  return <AttendantHandover shift={shift}/>;
}

return (
<div style={{padding:20}}>'''
)

code = code.replace(
'''<button style={{width:"100%",padding:12}}>
🤝 Handover Attendant
</button>''',
'''<button
style={{width:"100%",padding:12}}
onClick={()=>setHandover(true)}
>
🤝 Handover Attendant
</button>'''
)

code = code.replace(
'import AttendantHandover from "./AttendantHandover";\n',
'import React from "react";\nimport AttendantHandover from "./AttendantHandover";\n'
)

p.write_text(code)

print("✅ Handover connected to ShiftActive")
