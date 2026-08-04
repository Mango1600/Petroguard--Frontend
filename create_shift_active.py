from pathlib import Path

Path("src/pages/ShiftActive.jsx").write_text(r'''
export default function ShiftActive({shift}){

return (
<div style={{padding:20}}>

<h2>🟢 SHIFT ACTIVE</h2>

<p>Shift No: {shift?.id}</p>
<p>Pump: Pump 1 (PMS)</p>
<p>Opening Meter: {shift?.opening_meter || 1000}</p>

<hr/>

<h3>Status: 🟢 Working</h3>

<button style={{width:"100%",padding:12}}>
🟢 Continue Working
</button>

<br/><br/>

<button style={{width:"100%",padding:12}}>
🤝 Handover Attendant
</button>

<br/><br/>

<button style={{width:"100%",padding:12}}>
🔴 Close Pump Shift
</button>

</div>
)

}
''')

print("✅ Shift Active page created")
