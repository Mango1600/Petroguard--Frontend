
import { useRef, useState, useEffect } from "react";
import { uploadVideoEvidence } from "../services/evidenceService";

export default function VideoCapture({
  onComplete,
  stationId,
  staffId,
  recordId
}) {
  const videoRef = useRef(null);
  const recorderRef = useRef(null);

  const [recording, setRecording] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const [videoUrl, setVideoUrl] = useState("");

  useEffect(() => {
    startCamera();

    return () => {
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

      if (!window.MediaRecorder) {
        console.error("MediaRecorder not supported");
        return;
      }

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
          fileName: "opening_shift_video.webm",
          stationId,
          recordId,
          moduleName: "open_shift",
          uploadedBy: staffId,
          description: "Opening shift video evidence"
        }).then((result)=>{
          console.log("VIDEO UPLOAD:", result);

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

    recorderRef.current.start();
    setRecording(true);

    const timer = setInterval(() => {
      setSeconds((s) => {

        if (s >= 300) {
          clearInterval(timer);
          stopRecording();
          return s;
        }

        return s + 1;
      });
    },1000);
  }


  function stopRecording() {
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

      <video
        ref={videoRef}
        autoPlay
        playsInline
        style={{
          width:"100%",
          borderRadius:10
        }}
      />

      <p>
        Recording Time: {Math.floor(seconds/60)}:
        {(seconds%60).toString().padStart(2,"0")}
      </p>


      {!recording && !videoUrl && (
        <button
          onClick={startRecording}
          style={{width:"100%",padding:15}}
        >
          ▶️ START RECORDING
        </button>
      )}


      {recording && (
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
