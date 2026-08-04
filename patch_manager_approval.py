from pathlib import Path

p = Path("src/pages/ManagerDashboard.jsx")
text = p.read_text()

# Add state
text = text.replace(
'const [loading, setLoading] = useState(false);',
'''const [loading, setLoading] = useState(false);
const [pendingShifts, setPendingShifts] = useState([]);'''
)

# Load submitted shifts
marker = "useEffect(() => {"

insert = '''
async function loadPendingShifts() {
  const { data } = await supabase
    .from("staff_shifts")
    .select("*")
    .eq("status","submitted")
    .order("submitted_at",{ascending:false});

  setPendingShifts(data || []);
}

async function approveShift(id) {
  const { error } = await supabase
    .from("staff_shifts")
    .update({
      status:"approved",
      approved_at:new Date().toISOString()
    })
    .eq("id",id);

  if(error){
    alert(error.message);
    return;
  }

  alert("✅ Shift Approved");
  loadPendingShifts();
}

'''

text = text.replace(marker, insert + marker)

# Call loader
text = text.replace(
"useEffect(() => {",
"useEffect(() => {\n  loadPendingShifts();"
)

# Add Pending Shifts section
section = '''
<hr/>

<h2>Pending Shift Approval</h2>

{pendingShifts.map(shift => (
  <div
    key={shift.id}
    style={{
      border:"1px solid #ccc",
      padding:12,
      marginBottom:12,
      borderRadius:8
    }}
  >
    <p><b>Shift ID:</b> {shift.id}</p>
    <p><b>Staff:</b> {shift.staff_id}</p>
    <p><b>Station:</b> {shift.station_id}</p>

    <button
      onClick={() => approveShift(shift.id)}
      style={{padding:10}}
    >
      ✅ APPROVE SHIFT
    </button>
  </div>
))}
'''

text = text.replace("</div>\n  );", section + "\n</div>\n  );")

p.write_text(text)

print("✅ Manager Approval added")
