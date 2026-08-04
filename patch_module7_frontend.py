from pathlib import Path

files = {}

files["src/pages/Reconciliation.jsx"] = r'''
import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function Reconciliation({ pumpShiftId }) {

    const [result, setResult] = useState(null);
    const [message, setMessage] = useState("");


    async function runReconciliation(){

        const { data, error } =
            await supabase
            .rpc(
                "calculate_reconciliation",
                {
                    p_pump_shift_id:
                    pumpShiftId
                }
            );


        if(error){

            setMessage(error.message);
            return;

        }


        setMessage(
            "Reconciliation completed"
        );


        setResult(data);

    }


    return (

        <div>

            <h2>
                Shift Reconciliation
            </h2>


            <button
                onClick={runReconciliation}
            >
                Run Reconciliation
            </button>


            <p>{message}</p>


            {result && (

                <div>

                    <h3>
                        Reconciliation ID
                    </h3>

                    <p>{result}</p>

                    <p>
                        System calculated automatically
                    </p>

                </div>

            )}


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


print("Module 7 frontend complete")
