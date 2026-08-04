from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Fix Save Draft button
text = text.replace(
    '<button onClick={() => savePayment("draft") disabled={isLocked}>',
    '<button onClick={() => savePayment("draft")} disabled={isLocked}>'
)

# Fix Submit button
text = text.replace(
    '<button\n        style={{ marginLeft:"10px" }}\n        onClick={() => savePayment("submitted")} disabled={isLocked}',
    '<button\n        style={{ marginLeft:"10px" }}\n        onClick={() => savePayment("submitted")}\n        disabled={isLocked}'
)

path.write_text(text)

print("Button syntax repaired successfully.")
