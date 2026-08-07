import { useState } from "react";
import VideoCapture from "../components/VideoCapture";
import CameraCapture from "../components/CameraCapture";

export default function ShiftClose({ onComplete, loggedInStaff, assignment, shift }) {
  const [videoDone, setVideoDone] = useState(false);
  const [photoDone, setPhotoDone] = useState(false);
  const [photo, setPhoto] = useState(null);
  const [meter, setMeter] = useState("");

  return (
    <div style={{padding:20}}>

      <h2>Shift Close</h2>

      {!videoDone && (
        <>
          <h3>1. Closing Video Evidence</h3>
          <VideoCapture
            onComplete={() => setVideoDone(true)}
          />
        </>
      )}

      {videoDone && !photoDone && (
        <>
          <h3>2. Closing Photo Evidence</h3>
          <CameraCapture
            title="Closing Evidence"
            stationId={shift?.pumps?.station_id || null}
            uploadedBy={loggedInStaff?.user_id || null}
            recordId={assignment?.pump_shift_id || null}
            moduleName="SHIFT_CLOSE"
            onCapture={(evidenceId) => { setPhoto(evidenceId); setPhotoDone(true); }}
          />
        </>
      )}

      {photoDone && (
        <>
          <h3>3. Closing Meter</h3>

          <input
            type="number"
            placeholder="Closing Meter"
            value={meter}
            onChange={(e)=>setMeter(e.target.value)}
          />

          <br/><br/>

          <button
            disabled={!meter}
            onClick={() => onComplete({ meter, photo })}
          >
            Finish Shift
          </button>
        </>
      )}
    </div>
  );
}