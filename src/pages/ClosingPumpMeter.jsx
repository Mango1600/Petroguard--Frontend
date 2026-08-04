import { useState } from "react";
import ClosingVideoEvidence from "./ClosingVideoEvidence";

export default function ClosingPumpMeter({ shift }) {

  const [closingMeter,setClosingMeter]=useState("");
  const [next,setNext]=useState(false);

  const opening=Number(shift?.opening_meter||0);
  const closing=Number(closingMeter||0);
  const litres=closing-opening;

  if(next){
    return (
      <ClosingVideoEvidence
        shift={shift}
        openingMeter={opening}
        closingMeter={closing}
        litresSold={litres}
      />
    );
  }

  return(
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>

      <h2>🔴 CLOSING PUMP METER</h2>

      <p><b>Shift:</b> {shift?.id}</p>
      <p><b>Pump:</b> {shift?.pump_id}</p>

      <label>Opening Meter</label>

      <input
        value={opening}
        readOnly
        style={{width:"100%",padding:12}}
      />

      <br/><br/>

      <label>Closing Meter</label>

      <input
        type="number"
        value={closingMeter}
        onChange={(e)=>setClosingMeter(e.target.value)}
        style={{width:"100%",padding:12}}
      />

      <br/><br/>

      <h3>Litres Sold: {litres>0?litres:0}</h3>

      <button
        style={{width:"100%",padding:15}}
        onClick={()=>{

          if(!closingMeter){
            return;
          }

          setNext(true);

        }}
      >
        Continue to Closing Video
      </button>

    </div>
  );

}