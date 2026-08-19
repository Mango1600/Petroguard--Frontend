
import { useRef, useState, useEffect } from "react";
import { uploadVideoEvidence } from "../services/evidenceService";

export default function VideoCapture({
  onComplete,
  stationId,
  uploadedBy,
  recordId,
  shiftId,
  evidenceType = "SHIFT_VIDEO",
  moduleName
}) {
  const videoRef = useRef(null);
  const recorderRef = useRef(null);
  const timerRef = useRef(null);

  const [recording, setRecording] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const [videoUrl, setVideoUrl] = useState("");
  const [completed, setCompleted] = useState(false);

  useEffect(() => {
    startCamera();

    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
        timerRef.current = null;
      }

      stopCamera();
    };
  }, []);

  async function startCamera() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: "environment"
        },
        audio: true
      });

      videoRef.current.srcObject = stream;

      const recorder = new MediaRecorder(stream);
      recorderRef.current = recorder;

      const chunks = [];

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunks.push(e.data);
        }
      };

      recorder.onstop = () => {
        const blob = new Blob(chunks, {
          type: "video/webm"
        });

        const url = URL.createObjectURL(blob);
        setVideoUrl(url);

        uploadVideoEvidence({
          videoBlob: blob,
          fileName: "shift_evidence.webm",
          stationId,
          recordId: recordId ?? shiftId,
          moduleName: moduleName || evidenceType,
          uploadedBy,
          description: "Shift video evidence"
        }).then((result)=>{
          console.log("VIDEO UPLOAD:", result);

          stopCamera();
          setCompleted(true);

          if (onComplete) {
            onComplete(result);
          }
        });
      };

    } catch (error) {
      console.log(error);
    }
  }


  function startRecording() {
    if (!recorderRef.current) return;

    // Clear any previous timer before starting a new recording.
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }

    setSeconds(0);
    recorderRef.current.start();
    setRecording(true);

    timerRef.current = setInterval(() => {
      setSeconds((s) => {
        if (s >= 300) {
          clearInterval(timerRef.current);
          timerRef.current = null;
          stopRecording();
          return s;
        }

        return s + 1;
      });
    }, 1000);
  }


  function stopRecording() {
    // Stop the timer immediately.
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }

    if (recorderRef.current &&
        recorderRef.current.state === "recording") {

      recorderRef.current.stop();
    }

    setRecording(false);
  }


  function stopCamera() {
    const stream = videoRef.current?.srcObject;

    if (stream) {
      stream.getTracks().forEach(track => track.stop());
    }
  }


  return (
    <div style={{padding:20}}>

      <h3>🎥 PetroGuard Video Evidence</h3>

      {!completed && (
        <video
          ref={videoRef}
          autoPlay
          playsInline
          style={{
            width:"100%",
            borderRadius:10
          }}
        />
      )}

      {completed && (
        <p>✅ Video Evidence Completed</p>
      )}

      <p>
        Recording Time: {Math.floor(seconds/60)}:
        {(seconds%60).toString().padStart(2,"0")}
      </p>


      {!completed && !recording && !videoUrl && (
        <button
          onClick={startRecording}
          style={{width:"100%",padding:15}}
        >
          ▶️ START RECORDING
        </button>
      )}


      {!completed && recording && (
        <button
          onClick={stopRecording}
          style={{width:"100%",padding:15}}
        >
          ⏹ STOP RECORDING
        </button>
      )}


      {videoUrl && (
        <p>
          ✅ Video Recorded Successfully
        </p>
      )}

    </div>
  );
}