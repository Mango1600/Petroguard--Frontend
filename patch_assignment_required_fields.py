from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

text = text.replace(
"""    opening_evidence: openingEvidence ?? null,
    assigned_at: now
""",
"""    opening_evidence: openingEvidence ?? "PENDING_OPENING_EVIDENCE",
    assigned_at: now,
    evidence_locked: false
"""
)

file.write_text(text)

print("Assignment required fields patched")
