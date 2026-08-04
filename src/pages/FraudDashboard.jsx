
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";


export default function FraudDashboard() {


    const [alerts, setAlerts] = useState([]);


    async function loadAlerts(){

        const { data, error } =

            await supabase
            .from("fraud_alerts")
            .select("*")
            .order(
                "created_at",
                {
                    ascending:false
                }
            );


        if(!error){

            setAlerts(data || []);

        }

    }



    useEffect(()=>{

        loadAlerts();

    },[]);



    return (

        <div>

            <h2>
                Fraud Monitoring
            </h2>


            {

            alerts.map(alert => (

                <div key={alert.id}>


                    <h3>
                        {alert.alert_type}
                    </h3>


                    <p>
                        Risk Score:
                        {alert.risk_score}
                    </p>


                    <p>
                        Risk Level:
                        {alert.risk_level}
                    </p>


                    <p>
                        Status:
                        {alert.status}
                    </p>


                    <p>
                        {alert.description}
                    </p>


                </div>

            ))

            }


        </div>

    );

}
