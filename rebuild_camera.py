from pathlib import Path

code = r'''import { useRef, useState } from "react";

export default function CameraCapture({
  onCapture,
  title = "Evidence Capture"
}) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [stream, setStream] = useState(null);
  const [cameraOpen, setCameraOpen] = useState(false);
  const [photo, setPhoto] = useState(null);
  const [error, setError] = useState("");

  async function openCamera() {
    try {
      const s = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: "environment" },
        audio: false
      });

      setStream(s);
      setCameraOpen(true);

      setTimeout(() => {
        if (videoRef.current) {
          videoRef.current.srcObject = s;
        }
      }, 100);

    } catch (e) {
      console.error(e);
      setError("Unable to access camera.");
    }
  }

  function capture() {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    if (!video || !canvas) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    const img = canvas.toDataURL("image/jpeg", 0.9);

    setPhoto(img);

    if (stream) {
      stream.getTracks().forEach(t => t.stop());
    }

    setCameraOpen(false);
  }

  function retake() {
    setPhoto(null);
    openCamera();
  }

  function usePhoto() {
    if (photo && onCapture) {
      onCapture(photo);
    }
  }

  return (
    <div style={{marginTop:20}}>
      <h3>{title}</h3>

      {error && <p>{error}</p>}

      {!cameraOpen && !photo && (
        <button onClick={openCamera}>
          📷 Capture Evidence
        </button>
      )}

      {cameraOpen && (
        <>
          <video
            ref={videoRef}
            autoPlay
            playsInline
            style={{width:"100%",maxWidth:"400px"}}
          />

          <br/><br/>

          <button onClick={capture}>
            📸 Capture Photo
          </button>
        </>
      )}

      {photo && (
        <>
          <img
            src={photo}
            alt="Evidence"
            style={{width:"100%",maxWidth:"400px"}}
          />

          <br/><br/>

          <button onClick={retake}>
            🔄 Retake
          </button>

          <button
            onClick={usePhoto}
            style={{marginLeft:10}}
          >
            ✅ Use Photo
          </button>
        </>
      )}

      <canvas
        ref={canvasRef}
        style={{display:"none"}}
      />
    </div>
  );
}
'''

Path("src/components/CameraCapture.jsx").write_text(code)

print("✅ CameraCapture rebuilt successfully.")
