from pathlib import Path

p = Path("src/components/CameraCapture.jsx")

code = p.read_text()

if "MediaRecorder" in code:
    print("✅ Video recording already exists")
    raise SystemExit

code = code.replace(
'const [capturedImage, setCapturedImage] = useState(null);',
'''const [capturedImage, setCapturedImage] = useState(null);
  const [recording,setRecording]=useState(false);
  const [recordedVideo,setRecordedVideo]=useState(null);
  const mediaRecorderRef=useRef(null);
  const recordedChunksRef=useRef([]);'''
)

insert = r'''

  function startVideoRecording(){

    if(!stream) return;

    recordedChunksRef.current=[];

    const recorder=new MediaRecorder(stream,{
      mimeType:"video/webm"
    });

    mediaRecorderRef.current=recorder;

    recorder.ondataavailable=(e)=>{
      if(e.data.size>0){
        recordedChunksRef.current.push(e.data);
      }
    };

    recorder.onstop=()=>{

      const blob=new Blob(
        recordedChunksRef.current,
        {type:"video/webm"}
      );

      const url=URL.createObjectURL(blob);

      setRecordedVideo({
        blob,
        url
      });

      setRecording(false);

    };

    recorder.start();

    setRecording(true);

  }

  function stopVideoRecording(){

    if(mediaRecorderRef.current){
      mediaRecorderRef.current.stop();
    }

    if(stream){
      stream.getTracks().forEach(track=>track.stop());
    }

    setCameraOpen(false);

  }

  function useVideo(){

    if(onCapture && recordedVideo){
      onCapture(recordedVideo);
      setRecordedVideo(null);
    }

  }

'''
code = code.replace("function capturePhoto()", insert + "\nfunction capturePhoto()")

old = '''
          <button onClick={capturePhoto}>
            📸 Capture Photo
          </button>
'''

new = '''
          <button onClick={capturePhoto}>
            📸 Capture Photo
          </button>

          <button
            onClick={
              recording
                ? stopVideoRecording
                : startVideoRecording
            }
            style={{marginLeft:"10px"}}
          >
            {recording ? "⏹ Stop Video" : "🔴 Record Video"}
          </button>
'''

code = code.replace(old, new)

code = code.replace(
'''      {capturedImage && (''',
'''      {recordedVideo && (

        <>

          <video
            src={recordedVideo.url}
            controls
            style={{
              width:"100%",
              maxWidth:"400px",
              borderRadius:"8px"
            }}
          />

          <br/><br/>

          <button
            onClick={useVideo}
          >
            ✅ Use Video
          </button>

          <button
            onClick={()=>{
              setRecordedVideo(null);
              setCameraOpen(true);
            }}
            style={{marginLeft:"10px"}}
          >
            🔄 Retake
          </button>

        </>

      )}

      {capturedImage && ('''
)

p.write_text(code)

print("✅ Real video recording added")
