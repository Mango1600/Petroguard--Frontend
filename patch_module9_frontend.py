from pathlib import Path

files = {}

files["src/pages/BusinessDayClose.jsx"] = r'''
import { useState } from "react";
import { supabase } from "../lib/supabase";


export default function BusinessDayClose({ businessDayId, userId }) {


    const [evidence, setEvidence] = useState("");

    const [message, setMessage] = useState("");



    async function closeBusinessDay(){


        const { data, error } =

            await supabase
            .from("business_day_closures")
            .insert({

                business_day_id:
                    businessDayId,

                closed_by:
                    userId,

                closing_evidence:
                    evidence,

                status:
                    "CLOSED"

            })

            .select();



        if(error){

            setMessage(error.message);
            return;

        }


        setMessage(
            "Business Day closed successfully"
        );


    }



    return (

        <div>

            <h2>
                Close Business Day
            </h2>


            <input

                placeholder="Closing Evidence Reference"

                value={evidence}

                onChange={
                    e=>setEvidence(e.target.value)
                }

            />


            <button

                onClick={closeBusinessDay}

            >
                Close Business Day

            </button>


            <p>
                {message}
            </p>


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


print("Module 9 frontend complete")
