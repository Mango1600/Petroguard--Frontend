from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
t = p.read_text()

# Remove invalid state call
t = t.replace(
    "setRecording(false);                          setRecorded(true);",
    """setRecording(false);

    if (timerRef.current) {
      clearInterval(timerRef.current);
    }"""
)

# Add timer reference if missing
if 'const timerRef = useRef(null);' not in t:
    t = t.replace(
        'const recorderRef = useRef(null);',
        '''const recorderRef = useRef(null);
  const timerRef = useRef(null);'''
    )

# Store timer
t = t.replace(
    'const timer = setInterval(() => {',
    'timerRef.current = setInterval(() => {'
)

# Clear timer on stop
t = t.replace(
    'recorderRef.current.stop();',
    '''recorderRef.current.stop();

      if (timerRef.current) {
        clearInterval(timerRef.current);
      }'''
)

p.write_text(t)

print("✅ VideoCapture stop fix applied")
