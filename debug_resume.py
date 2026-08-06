from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
t = p.read_text()

t = t.replace(
    "async function createResumeAssignment(",
    'async function createResumeAssignment(\n'
    '/* DEBUG */\n'
)

t = t.replace(
    'const { data, error } = await supabase',
    'console.log("DEBUG: About to insert assignment");\n'
    'const { data, error } = await supabase',
    1
)

t = t.replace(
    'if(error){',
    'console.log("DEBUG: Insert finished", {data, error});\nif(error){',
    1
)

p.write_text(t)
print("Debug logging added.")
