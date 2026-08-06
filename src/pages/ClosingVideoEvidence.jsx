import { useState } from "react";
import VideoCapture from "../components/VideoCapture";
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

      <VideoCapture
        evidenceType="closing_shift_video"
        onComplete={(evidenceId)=>{
          setVideo(evidenceId);
        }}
      />

      <br/><br/>

      <button
        style={{width:"100%",padding:15}}
        onClick={()=>{

          if(!video){
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