import { useRef, useState, useEffect } from "react";

export default function CameraCapture({ onCapture }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [cameraOpen, setCameraOpen] = useState(false);
  const [stream, setStream] = useState(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [recording, setRecording] = useState(false);
  const [videoUrl, setVideoUrl] = useState(null);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!cameraOpen) return;

    async function startCamera() {
      try {
        const mediaStream =
          await navigator.mediaDevices.getUserMedia({
            video: {
              facingMode: "environment",
            },
            audio: false,
          });

        setStream(mediaStream);

        if (videoRef.current) {
          videoRef.current.srcObject = mediaStream;
        }
      } catch (err) {
        console.error(err);
        setError("Unable to access camera.");
      }
    }

    startCamera();

    return () => {
      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
    };
  }, [cameraOpen]);  

function startRecording() {

  if (!stream) return;

  chunksRef.current = [];

  const recorder = new MediaRecorder(stream);

  mediaRecorderRef.current = recorder;

  recorder.ondataavailable = (event) => {
    if (event.data.size > 0) {
      chunksRef.current.push(event.data);
    }
  };

  recorder.onstop = () => {
    const blob = new Blob(
      chunksRef.current,
      { type: "video/webm" }
    );

    setVideoUrl(URL.createObjectURL(blob));
  };

  recorder.start();
  setRecording(true);
}


function stopRecording() {

  if (mediaRecorderRef.current) {
    mediaRecorderRef.current.stop();
  }

  setRecording(false);
}


function capturePhoto() {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    if (!video || !canvas) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const context = canvas.getContext("2d");

    context.drawImage(video, 0, 0);

    const image = canvas.toDataURL("image/jpeg", 0.9);

    setCapturedImage(image);

    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
    }

    setCameraOpen(false);
  }

  function usePhoto() {
    if (onCapture && capturedImage) {
      onCapture(capturedImage);

      setVideoUrl(null);
      setCapturedImage(null);
      setCameraOpen(false);

      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
    }
  }

  function retakePhoto() {
    setCapturedImage(null);
    setCameraOpen(true);
  }  return (
    <div>
      <h3>📹 PetroGuard Video Evidence Capture</h3>

      {error && <p>{error}</p>}

      {!cameraOpen && !capturedImage && (
        <button onClick={() => setCameraOpen(true)}>
          📹 Start Evidence Capture
        </button>
      )}

      {cameraOpen && (
        <>
          <video
            ref={videoRef}
            autoPlay
            playsInline
            style={{
              width: "100%",
              maxWidth: "400px",
              borderRadius: "8px",
            }}
          />

          <br />
          <br />

          <button onClick={recording ? stopRecording : startRecording}>
{
recording ? "⏹ Stop Video" : "🔴 Record Video"
}
</button>

<button onClick={capturePhoto}>
            📸 Capture Photo
          </button>

          <button
            onClick={() => {
              if (stream) {
                stream.getTracks().forEach((track) => track.stop());
              }
              setCameraOpen(false);
            }}
            style={{ marginLeft: "10px" }}
          >
            ❌ Close
          </button>
        </>
      )}

      
      {!capturedImage && videoUrl && (
        <>
          <video
            src={videoUrl}
            controls
            style={{
              width:"100%",
              maxWidth:"400px",
              borderRadius:"8px"
            }}
          />

          <br/><br/>

          <button
            onClick={()=>{
              onCapture(videoUrl);
              setVideoUrl(null);
              setCapturedImage(null);
              setCameraOpen(false);
            }}
          >
            ✅ Use Video
          </button>

          <button
            onClick={()=>{
              setVideoUrl(null);
              setCameraOpen(true);
            }}
            style={{marginLeft:"10px"}}
          >
            🔄 Retake Video
          </button>

        </>
      )}


      {!videoUrl && capturedImage && (
        <>
          <img
            src={capturedImage}
            alt="Evidence"
            style={{
              width: "100%",
              maxWidth: "400px",
              borderRadius: "8px",
            }}
          />

          <br />
          <br />

          <button onClick={retakePhoto}>
            🔄 Retake
          </button>

          <button
            onClick={usePhoto}
            style={{ marginLeft: "10px" }}
          >
            ✅ Use Photo
          </button>
        </>
      )}

      <canvas
        ref={canvasRef}
        style={{ display: "none" }}
      />
    </div>
  );
}