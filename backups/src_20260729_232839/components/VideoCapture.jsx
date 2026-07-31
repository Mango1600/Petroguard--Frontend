import { supabase } from "../lib/supabase";
import { useRef, useState, useEffect } from "react";

export default function VideoCapture({
  onComplete,
  shiftId,
  stationId,
  staffId,
  evidenceType
}) {
  const videoRef = useRef(null);
  const recorderRef = useRef(null);

  const [recording, setRecording] = useState(false);
  const [seconds, setSeconds] = useState(0);
  const [videoUrl, setVideoUrl] = useState("");
const [uploading, setUploading] = useState(false);
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

      const recorder = new MediaRecorder(stream);
      recorderRef.current = recorder;

      const chunks = [];

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunks.push(e.data);
        }
      };

      recorder.onstop = async () => {
        const blob = new Blob(chunks, {
          type: "video/webm"
        });

        const url = URL.createObjectURL(blob);
        setVideoUrl(url);

        console.log("🎥 Video captured:", blob.size, blob.type);

        try {
          setUploading(true);

          const file = new File(
            [blob],
            `video-${Date.now()}.webm`,
            { type: "video/webm" }
          );

          const filePath = `${shiftId}/${file.name}`;

          const { error: uploadError } =
            await supabase.storage
              .from("petroguard-evidence")
              .upload(filePath, file);

          if (uploadError) {
            console.log(uploadError);
            return;
          }

          const { error: dbError } =
            await supabase
              .from("evidence")
              .insert([{
                shift_id: shiftId,
                station_id: stationId,
                uploaded_by: staffId,
                evidence_type: evidenceType || "shift_video",
                file_name: file.name,
                file_path: filePath,
                mime_type: file.type,
                file_size: file.size,
                capture_time: new Date().toISOString(),
                status: "Pending"
              }]);

          if (dbError) {
            console.log(dbError);
            return;
          }

          console.log("✅ Video evidence saved");

        } finally {
          setUploading(false);
        }

        if (onComplete) {
          onComplete(blob);
        }
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
