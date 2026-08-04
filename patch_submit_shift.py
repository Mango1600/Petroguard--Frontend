from pathlib import Path

p = Path("src/pages/ShiftReconciliation.jsx")
text = p.read_text()

# Add submitted state
old = 'const [loading, setLoading] = useState(false);'
new = '''const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);'''
text = text.replace(old, new)

# Add submitShift function before loadReceipts
marker = "async function loadReceipts() {"

submit_fn = '''
  async function submitShift() {
    if (!stationId) {
      alert("Select a station first.");
      return;
    }

    setLoading(true);

    const { error } = await supabase
      .from("staff_shifts")
      .update({
        status: "submitted",
        submitted_at: new Date().toISOString()
      })
      .eq("station_id", Number(stationId))
      .eq("status", "open");

    setLoading(false);

    if (error) {
      alert(error.message);
      return;
    }

    setSubmitted(true);
    alert("✅ Shift submitted for Manager Approval");
  }

'''

text = text.replace(marker, submit_fn + marker)

# Add button before closing div
button = '''
      <br /><br />

      <button
        onClick={submitShift}
        disabled={loading || submitted}
        style={{width:"100%",padding:15}}
      >
        {submitted ? "✅ SHIFT SUBMITTED" : "📤 SUBMIT SHIFT"}
      </button>

'''

text = text.replace("</div>\n  );", button + "</div>\n  );")

p.write_text(text)

print("✅ Submit Shift added")
