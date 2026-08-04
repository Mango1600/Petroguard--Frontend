from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add useEffect import if missing
text = text.replace(
    'import { useState } from "react";',
    'import { useState, useEffect } from "react";'
)

# Add useEffect before return
if "loadPaymentStatus();" not in text:
    text = text.replace(
        "return (",
        """useEffect(() => {
    loadPaymentStatus();
  }, []);

  return ("""
    )

path.write_text(text)

print("useEffect added successfully.")
