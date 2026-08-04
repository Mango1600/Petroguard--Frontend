from pathlib import Path

file = Path("src/pages/ShiftActive.jsx")

text = file.read_text()

text = text.replace(
'import React from "react";',
'import React, { useState } from "react";'
)

text = text.replace(
'export default function ShiftActive({shift}){',
'''export default function ShiftActive({shift}){

const [handover,setHandover] = useState(false);
const [closing,setClosing] = useState(false);
'''
)

text = text.replace(
'<div style={{padding:20}}>',
'''<div style={{padding:20}}>

{handover && (
  <AttendantHandover shift={shift}/>
)}
'''
)

file.write_text(text)

print("ShiftActive handover state patched")
