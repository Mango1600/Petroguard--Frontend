from pathlib import Path

file = Path("src/components/VideoCapture.jsx")

text = file.read_text()

text = text.replace(
    'const [videoUrl, setVideoUrl] = useState("");',
    'const [videoUrl, setVideoUrl] = useState("");\n  const [completed, setCompleted] = useState(false);'
)

text = text.replace(
    '''stopCamera();
          setSeconds(0);

          if (onComplete) {''',
    '''stopCamera();
          setSeconds(0);
          setCompleted(true);

          if (onComplete) {'''
)

text = text.replace(
    '''      <video
        ref={videoRef}
        autoPlay
        playsInline
        style={{
          width:"100%",
          borderRadius:10
        }}
      />''',
    '''      {!completed && (
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
      )}'''
)

text = text.replace(
    '''      {!recording && !videoUrl && (
        <button''',
    '''      {!completed && !recording && !videoUrl && (
        <button'''
)

text = text.replace(
    '''      {recording && (
        <button''',
    '''      {!completed && recording && (
        <button'''
)

file.write_text(text)

print("✅ VideoCapture stop workflow patch applied.")
