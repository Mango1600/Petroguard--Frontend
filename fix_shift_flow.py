import os

target = 'alert("ACTIVE SHIFT: " + JSON.stringify(activeShift));'

replacement = '''// Active shift found - continue workflow
setCurrentPage("openingVideo");'''

for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith((".jsx", ".js")):
            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if target in content:
                content = content.replace(target, replacement)

                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

                print("Fixed:", path)

print("Done")
