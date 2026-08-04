from pathlib import Path

file = Path("src/pages/PaymentAllocation.jsx")

if not file.exists():
    raise FileNotFoundError("PaymentAllocation.jsx not found")

text = file.read_text()

if "payment_allocations" in text:
    print("Supabase save logic already exists")
else:

    insert_point = text.rfind("}")

    addition = r'''

async function savePaymentAllocation() {

    if (!validate()) return;

    const allocation = {
        business_day_id: meterSale.business_day_id,
        pump_shift_id: meterSale.pump_shift_id,
        assignment_id: meterSale.assignment_id,
        meter_sale_id: meterSale.id,

        payment_method: "MULTIPLE",

        amount:
            Number(cash || 0) +
            Number(pos || 0) +
            Number(bankTransfer || 0) +
            Number(credit || 0),

        customer_name:
            Number(credit || 0) > 0
            ? customerName
            : null,

        customer_phone:
            Number(credit || 0) > 0
            ? customerPhone
            : null
    };


    const { error } = await supabase
        .from("payment_allocations")
        .insert(allocation);


    if (error) {
        setMessage(error.message);
        return;
    }

    setMessage(
        "Payment allocation saved successfully"
    );
}

'''

    text = text[:insert_point] + addition + text[insert_point:]

    file.write_text(text)

    print("Module 5 Supabase save logic added")
