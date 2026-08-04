from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Disable all inputs
text = text.replace(
    'onChange={handleChange}/>',
    'onChange={handleChange} disabled={isLocked}/>'
)

# Disable Save Draft button
text = text.replace(
    '<button onClick={() => savePayment("draft")}>',
    '<button onClick={() => savePayment("draft")} disabled={isLocked}>'
)

# Disable Submit button
text = text.replace(
    'onClick={() => savePayment("submitted")}',
    'onClick={() => savePayment("submitted")} disabled={isLocked}'
)

# Add lock message
if "Awaiting Manager approval." not in text:
    text = text.replace(
        '<button onClick={() => savePayment("draft")}',
        '''{isLocked && (
        <p style={{color:"red",fontWeight:"bold"}}>
          🔒 This Payment Summary has been submitted.<br/>
          Awaiting Manager approval.
        </p>
      )}

      <button onClick={() => savePayment("draft")'''
    )

path.write_text(text)
print("Record locking UI applied successfully.")
