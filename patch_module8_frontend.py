from pathlib import Path

files = {}

files["src/pages/ManagerApproval.jsx"] = r'''
import { useState } from "react";
import { supabase } from "../lib/supabase";


export default function ManagerApproval({ reviewData }) {


    const [comments, setComments] = useState("");

    const [message, setMessage] = useState("");



    async function submitApproval(action){


        const approval = {

            business_day_id:
                reviewData.business_day_id,

            pump_shift_id:
                reviewData.pump_shift_id,

            reconciliation_id:
                reviewData.reconciliation_id,

            manager_id:
                reviewData.manager_id,

            action,

            comments

        };



        const { error } =
            await supabase
            .from("manager_approvals")
            .insert(approval);



        if(error){

            setMessage(error.message);
            return;

        }



        setMessage(
            "Manager decision recorded"
        );


    }



    return (

        <div>

            <h2>
                Manager Approval
            </h2>


            <p>
                Review Pump Shift:
                {reviewData.pump_shift_id}
            </p>


            <textarea

                placeholder="Manager comments"

                value={comments}

                onChange={
                    e=>setComments(e.target.value)
                }

            />


            <button
                onClick={
                    ()=>submitApproval("APPROVE")
                }
            >
                Approve
            </button>


            <button
                onClick={
                    ()=>submitApproval("REJECT")
                }
            >
                Reject
            </button>


            <button
                onClick={
                    ()=>submitApproval("INVESTIGATION")
                }
            >
                Request Investigation
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


print("Module 8 frontend complete")
