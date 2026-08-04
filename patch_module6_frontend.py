from pathlib import Path

files = {}

files["src/pages/CashDeclaration.jsx"] = r'''
import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function CashDeclaration({ shiftData }) {

    const [cash, setCash] = useState("");
    const [pos, setPos] = useState("");
    const [transfer, setTransfer] = useState("");
    const [credit, setCredit] = useState("");
    const [expenses, setExpenses] = useState("");

    const [message, setMessage] = useState("");


    async function submitDeclaration(){

        const record = {

            business_day_id:
                shiftData.business_day_id,

            pump_shift_id:
                shiftData.pump_shift_id,

            assignment_id:
                shiftData.assignment_id,

            attendant_id:
                shiftData.attendant_id,

            cash_amount:
                Number(cash || 0),

            pos_amount:
                Number(pos || 0),

            bank_transfer_amount:
                Number(transfer || 0),

            credit_amount:
                Number(credit || 0),

            expenses_amount:
                Number(expenses || 0),

            status:
                "SUBMITTED"
        };


        const { error } =
            await supabase
            .from("cash_declarations")
            .insert(record);


        if(error){

            setMessage(error.message);
            return;

        }


        setMessage(
            "Cash declaration submitted"
        );

    }


    return (

        <div>

            <h2>
                Cash Declaration
            </h2>


            <input
                placeholder="Cash"
                onChange={
                    e=>setCash(e.target.value)
                }
            />


            <input
                placeholder="POS"
                onChange={
                    e=>setPos(e.target.value)
                }
            />


            <input
                placeholder="Bank Transfer"
                onChange={
                    e=>setTransfer(e.target.value)
                }
            />


            <input
                placeholder="Credit"
                onChange={
                    e=>setCredit(e.target.value)
                }
            />


            <input
                placeholder="Expenses"
                onChange={
                    e=>setExpenses(e.target.value)
                }
            />


            <button
                onClick={submitDeclaration}
            >
                Submit Declaration
            </button>


            <p>{message}</p>

        </div>

    );
}
'''

base = Path(".")

for path, content in files.items():

    file = base / path
    file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file.write_text(content)

    print(f"Created {path}")


print(
    "Module 6 frontend block complete"
)
