from pathlib import Path

page = Path("src/pages/OperationsAnalysis.jsx")

page.write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function OperationsAnalysis({ staff }) {

  const [shifts, setShifts] = useState([]);

  useEffect(() => {
    loadOperations();
  }, []);

  async function loadOperations(){

    const { data, error } = await supabase
      .from("pump_shifts")
      .select(`
        id,
        shift_no,
        status,
        opening_meter,
        closing_meter,
        pumps (
          pump_name,
          product_type
        )
      `)
      .eq("status","OPEN");

    if(error){
      console.log(error);
      return;
    }

    setShifts(data || []);
  }


  function calculateLitres(shift){

    if(
      shift.opening_meter === null ||
      shift.closing_meter === null
    )
    return 0;

    return Number(shift.closing_meter)
      - Number(shift.opening_meter);
  }


  return (
    <div style={{padding:20}}>

      <h1>⛽ PetroGuard Operations</h1>

      <h2>Pump Shift Analysis</h2>


      {
        shifts.map((shift)=>(

          <div key={shift.id}
          style={{
            border:"1px solid #ccc",
            padding:15,
            marginBottom:15
          }}>

            <h3>
              {shift.pumps?.pump_name}
            </h3>


            <p>
              Product:
              {shift.pumps?.product_type}
            </p>


            <p>
              Status:
              {shift.status}
            </p>


            <hr/>


            <p>
              Opening Meter:
              {shift.opening_meter}
            </p>


            <p>
              Closing Meter:
              {shift.closing_meter || "Not Closed"}
            </p>


            <h3>
              Dispensed Volume:
              {calculateLitres(shift)} L
            </h3>


            <p>
              Awaiting reconciliation
            </p>


          </div>

        ))
      }


    </div>
  );
}
""")

print("Operations Analysis page created.")
