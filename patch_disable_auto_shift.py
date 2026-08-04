from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

text = text.replace(
'''  useEffect(() => {
    checkActiveShift();
  }, []);
''',
'''  // ShiftStatus now controls navigation.
  // useEffect(() => {
  //   checkActiveShift();
  // }, []);
''')

p.write_text(text)

print("✅ Automatic shift check disabled")
