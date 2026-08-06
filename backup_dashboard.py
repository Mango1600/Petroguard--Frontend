from pathlib import Path
import shutil

shutil.copy("src/pages/Dashboard.jsx", "src/pages/Dashboard.blacktest.backup.jsx")

print("Dashboard backup created")
