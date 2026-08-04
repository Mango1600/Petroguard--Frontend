from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

text = text.replace(
'import ShiftReconciliation from "./ShiftReconciliation";',
'import ShiftReconciliation from "./ShiftReconciliation";\nimport ShiftClose from "./ShiftClose";'
)

text = text.replace(
'if (page === "reconciliation") return <ShiftReconciliation staff={staff} />;',
'if (page === "reconciliation") return <ShiftReconciliation staff={staff} />;\n  if (page === "close") return <ShiftClose staff={staff} />;'
)

insert = '''
      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => setPage("close")}
      >
        🔴 CLOSE SHIFT
      </button>
'''

text = text.replace(
'''      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => setPage("reconciliation")}
      >
        💰 SHIFT RECONCILIATION
      </button>''',
'''      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => setPage("reconciliation")}
      >
        💰 SHIFT RECONCILIATION
      </button>
''' + insert
)

p.write_text(text)

print("✅ Shift Close connected")
