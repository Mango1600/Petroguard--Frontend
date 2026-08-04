from pathlib import Path

f = Path("src/pages/ShiftActive.jsx")
t = f.read_text()

if "useState" not in t:
    t = t.replace(
        'import React from "react";',
        'import React, { useState } from "react";'
    )

t = t.replace(
    "export default function ShiftActive({shift}){",
    """export default function ShiftActive({shift}){

const [handover,setHandover]=useState(false);

if(handover){
  return <AttendantHandover
    shift={shift}
    currentAttendant={{id:1}}
  />;
}
"""
)

f.write_text(t)

print("✅ ShiftActive connected to Handover")o

