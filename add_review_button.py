from pathlib import Path

path = Path("src/pages/ManagerApproval.jsx")
text = path.read_text()

old = """            <button onClick={() => approve(r.id)}>
              ✅ Approve
            </button>"""

new = """            <button onClick={() => setSelectedRecord(r)}>
              👁 Review
            </button>

            <button
              style={{ marginLeft: "10px" }}
              onClick={() => approve(r.id)}
            >
              ✅ Approve
            </button>"""

text = text.replace(old, new)

if "const [selectedRecord, setSelectedRecord]" not in text:
    text = text.replace(
        "const [records, setRecords] = useState([]);",
        """const [records, setRecords] = useState([]);
  const [selectedRecord, setSelectedRecord] = useState(null);"""
    )

path.write_text(text)

print("Review button added successfully.")
