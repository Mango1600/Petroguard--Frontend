from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

text = text.replace(
"""  if(error){
    throw error;
  }

  return data;""",
"""  console.log("ASSIGNMENT INSERT RESULT", {data, error});

  if(error){
    throw error;
  }

  return data;"""
)

file.write_text(text)

print("Assignment insert debug added")
