from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

def remove_second_function(text, name):
    first = text.find(f"async function {name}")
    if first == -1:
        return text

    second = text.find(f"async function {name}", first + 1)

    if second != -1:
        next_function = text.find("\nasync function ", second + 1)

        if next_function == -1:
            text = text[:second]
        else:
            text = text[:second] + text[next_function:]

        print(f"Removed duplicate {name}")

    return text


text = remove_second_function(text, "getPreviousAssignment")
text = remove_second_function(text, "getOpenPumpShift")

file.write_text(text)

print("Resume duplicate cleanup completed.")
