import { useState } from "react";
import CameraCapture from "../components/CameraCapture";
import CashDeclaration from "./CashDeclaration";

export default function ClosingVideoEvidence({
  shift,
  openingMeter,
  closingMeter,
  litresSold
}) {

  const [video,setVideo]=useState(null);
  const [done,setDone]=useState(False if False else False)

  if(done){
    return (
      <CashDeclaration
        shift={shift}
        openingMeter={openingMeter}
        closingMeter={closingMeter}
        litresSold={litresSold}
        closingVideo={video}
      />
    );
  }

  return(
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>

      <h2>📹 CLOSING VIDEO EVIDENCE</h2>

      <p><b>Shift:</b> {shift?.id}</p>
      <p><b>Opening:</b> {openingMeter}</p>
      <p><b>Closing:</b> {closingMeter}</p>
      <p><b>Litres Sold:</b> {litresSold}</p>

      <CameraCapture
        onCapture={(evidence)=>{
          setVideo(evidence);
        }}
      />

      <br/><br/>

      <button
        style={{width:"100%",padding:15}}
        onClick={()=>{

          if(!video){
            alert("Capture closing video");
            return;
          }

          setDone(true);

        }}
      >
        ✅ COMPLETE PUMP SHIFT
      </button>

    </div>
  );

}
