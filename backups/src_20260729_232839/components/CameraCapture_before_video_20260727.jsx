import { useRef, useState, useEffect } from "react";

export default function CameraCapture({ onCapture }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [cameraOpen, setCameraOpen] = useState(false);
  const [stream, setStream] = useState(null);
  const [capturedImage, setCapturedImage] = useState(null);
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
  }, [cameraOpen]);  function capturePhoto() {
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
    }
  }

  function retakePhoto() {
    setCapturedImage(null);
    setCameraOpen(true);
  }  return (
    <div>
      <h3>📷 Evidence Capture</h3>

      {error && <p>{error}</p>}

      {!cameraOpen && !capturedImage && (
        <button onClick={() => setCameraOpen(true)}>
          📷 Capture Evidence
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

      {capturedImage && (
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
