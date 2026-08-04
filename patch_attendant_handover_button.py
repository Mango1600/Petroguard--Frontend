from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

# Add states after assignment state
text = text.replace(
'const [assignment, setAssignment] = useState(null);',
'''const [assignment, setAssignment] = useState(null);
  const [closingMeter, setClosingMeter] = useState("");
  const [closingEvidence, setClosingEvidence] = useState("");'''
)

# Add function before return
marker = "  return ("

handover_function = """
  async function handleHandover() {
    if (!closingMeter || !closingEvidence) {
      alert("Closing meter and evidence required");
      return;
    }

    const { error } = await supabase
      .from("attendant_assignments")
      .update({
        closing_meter: Number(closingMeter),
        closing_evidence: closingEvidence,
        closing_evidence_time: new Date().toISOString(),
        handed_over_at: new Date().toISOString(),
        status: "HANDED_OVER",
        evidence_locked: true
      })
      .eq("id", assignment.id);

    if (error) {
      console.log(error);
      return;
    }

    loadPumpShift();
  }

"""

text = text.replace(marker, handover_function + marker)

# Replace button
text = text.replace(
"<button>Handover Pump</button>",
"""
<input
type="number"
placeholder="Closing Meter"
value={closingMeter}
onChange={(e)=>setClosingMeter(e.target.value)}
/>

<input
placeholder="Closing Evidence"
value={closingEvidence}
onChange={(e)=>setClosingEvidence(e.target.value)}
/>

<button onClick={handleHandover}>
Handover Pump
</button>
"""
)

file.write_text(text)

print("Handover button patched")
