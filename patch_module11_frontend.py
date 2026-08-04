from pathlib import Path

files = {}

files["src/pages/OperationalReports.jsx"] = r'''
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";


export default function OperationalReports() {


    const [reports, setReports] = useState([]);



    async function loadReports(){


        const { data, error } =

            await supabase
            .from("operational_reports")
            .select("*")
            .order(
                "created_at",
                {
                    ascending:false
                }
            );


        if(!error){

            setReports(data || []);

        }

    }



    useEffect(()=>{

        loadReports();

    },[]);



    return (

        <div>


            <h2>
                Operational Intelligence
            </h2>


            {

            reports.map(report => (

                <div key={report.id}>


                    <h3>
                        {report.report_type}
                    </h3>


                    <p>
                        Generated:
                        {report.created_at}
                    </p>


                    <pre>

                        {
                        JSON.stringify(
                            report.report_data,
                            null,
                            2
                        )
                        }

                    </pre>


                </div>

            ))

            }


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


print("Module 11 frontend complete")
