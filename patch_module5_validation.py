from pathlib import Path

file = Path("meter_sales_builder.py")

text = file.read_text()

addition = r'''

# ==========================================
# MODULE 5 - PAYMENT ALLOCATION VALIDATION
# Production Rules
# ==========================================

def validate_payment_allocation(
    total_sales_amount,
    cash,
    pos,
    bank_transfer,
    credit
):
    allocated_amount = (
        cash +
        pos +
        bank_transfer +
        credit
    )

    if allocated_amount != total_sales_amount:
        raise ValueError(
            "Payment allocation does not match calculated sales amount"
        )

    return {
        "total_sales_amount": total_sales_amount,
        "cash": cash,
        "pos": pos,
        "bank_transfer": bank_transfer,
        "credit": credit,
        "status": "BALANCED"
    }


'''

if "MODULE 5 - PAYMENT ALLOCATION VALIDATION" not in text:
    file.write_text(text + addition)
    print("Module 5 validation added successfully")
else:
    print("Validation already exists")
