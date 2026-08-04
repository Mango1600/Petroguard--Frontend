from pathlib import Path

file = Path("src/pages/PaymentAllocation.jsx")

text = file.read_text()

if "payment_rows" in text:
    print("Multi payment rows already exist")
else:

    addition = r'''

function payment_rows() {

    return [
        {
            payment_method: "CASH",
            amount: Number(cash || 0)
        },

        {
            payment_method: "POS",
            amount: Number(pos || 0)
        },

        {
            payment_method: "BANK_TRANSFER",
            amount: Number(bankTransfer || 0)
        },

        {
            payment_method: "CREDIT",
            amount: Number(credit || 0)
        }

    ].filter(
        item => item.amount > 0
    );
}

'''

    marker = "export default function PaymentAllocation"

    text = text.replace(
        marker,
        addition + "\n" + marker
    )

    file.write_text(text)

    print("Module 5 payment rows added")
