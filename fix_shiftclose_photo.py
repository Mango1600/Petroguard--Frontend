from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")

s = p.read_text()

s = s.replace(
'const [photoDone, setPhotoDone] = useState(false);',
'const [photoDone, setPhotoDone] = useState(false);\n  const [photo, setPhoto] = useState(null);'
)

s = s.replace(
'onCapture={() => setPhotoDone(true)}',
'onCapture={(image) => { setPhoto(image); setPhotoDone(true); }}'
)

s = s.replace(
'onClick={onComplete}',
'onClick={() => onComplete({ meter, photo })}'
)

p.write_text(s)

print("✅ ShiftClose evidence data callback fixed.")
