
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
                    null,

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
