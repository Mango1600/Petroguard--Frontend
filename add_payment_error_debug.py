from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add console.log before payload
if 'console.log("STAFF:", staff);' not in text:
    text = text.replace(
        "const payload = {",
        'console.log("STAFF:", staff);\n\n      const payload = {'
    )

# Improve error message
text = text.replace(
    'setMessage("SAVE ERROR: " + err.message);',
    '''setMessage(
`SAVE ERROR:
${err.message}

CODE: ${err.code || ""}
DETAILS: ${err.details || ""}
HINT: ${err.hint || ""}`
);'''
)

path.write_text(text)

print("PaymentSummary debug added successfully.")
