from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
code = p.read_text()

# Add video preview after photo preview
if "{videoUrl && (" not in code:

    insert = r'''
      {videoUrl && (
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
'''

    code = code.replace(
        "{capturedImage && (",
        insert + "\n\n      {capturedImage && ("
    )

p.write_text(code)

print("✅ Video preview completed")
