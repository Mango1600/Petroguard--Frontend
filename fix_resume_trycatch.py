from pathlib import Path

path = Path("src/pages/ResumeAssignment.jsx")
text = path.read_text()

text = text.replace(
"""async function load(){

const businessDay = await getOpenBusinessDay(""",
"""async function load(){

try{

const businessDay = await getOpenBusinessDay("""
)

text = text.replace(
"""setAttendants(data||[]);

}
""",
"""setAttendants(data||[]);

}catch(err){

console.error(err);
setMessage(err.message || "Resume load failed.");

}

}
"""
)

path.write_text(text)

print("ResumeAssignment try/catch added.")
