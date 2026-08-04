import { useRef, useState, useEffect } from "react";
import { supabase } from "../lib/supabase";

export default function CameraCapture({
  onCapture,
  mode = "both",
  title = "Enterprise Evidence Capture"
}) {

  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const mediaRecorderRef = useRef(null);

  const [cameraOpen, setCameraOpen] = useState(false);
  const [stream, setStream] = useState(null);

  const [capturedPhoto, setCapturedPhoto] = useState(null);
  const [recordedVideo, setRecordedVideo] = useState(null);

  const [recording, setRecording] = useState(false);

  const [gps, setGps] = useState(null);
  const [deviceInfo, setDeviceInfo] = useState("");
  const [networkInfo, setNetworkInfo] = useState("");
  const [batteryLevel, setBatteryLevel] = useState("");
  const [timestamp, setTimestamp] = useState("");
  const [shaHash, setShaHash] = useState("");
  const [aiVerified] = useState(false);

  const [error, setError] = useState("");


  useEffect(() => {

    setTimestamp(new Date().toISOString());

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          setGps({
            latitude: pos.coords.latitude,
            longitude: pos.coords.longitude
          });
        },
        () => {}
      );
    }

    setDeviceInfo(navigator.userAgent);

    if (navigator.connection) {
      setNetworkInfo(
        navigator.connection.effectiveType || ""
      );
    }

    if (navigator.getBattery) {
      navigator.getBattery().then((battery) => {
        setBatteryLevel(
          Math.round(battery.level * 100)
        );
      });
    }

  }, []);


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

    setCapturedPhoto(image);

    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
    }

    setCameraOpen(false);
  }


  async function uploadEvidence() {

    if (!capturedPhoto) return null;

    const response = await fetch(capturedPhoto);
    const blob = await response.blob();

    const fileName =
      `opening/${Date.now()}.jpg`;

    const { data, error } =
      await supabase.storage
        .from("petroguard-evidence")
        .upload(fileName, blob, {
          contentType: "image/jpeg"
        });

    if (error) {
      console.error(error);
      setError("Evidence upload failed.");
      return null;
    }

    return data.path;
  }

  async function usePhoto() {

    const path = await uploadEvidence();

    if (onCapture && path) {
      onCapture(path);
    }
  }

  function retakePhoto() {
    setCapturedPhoto(null);
    setCameraOpen(true);
  }  return (
    <div>
      <h3>📷 Evidence Capture</h3>

      {error && <p>{error}</p>}

      {!cameraOpen && !capturedPhoto && (
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

      {capturedPhoto && (
        <>
          <img
            src={capturedPhoto}
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