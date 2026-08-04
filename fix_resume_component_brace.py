from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

text = text.replace(
"""
</div>

}
""",
"""
</div>
);
}
"""
)

file.write_text(text)

print("ResumeAssignment component brace fixed.")
