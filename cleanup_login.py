from pathlib import Path
import re

p = Path("src/pages/Login.jsx")
text = p.read_text()

pattern = r'''
\s*if \(staff\.status !== "active"\) \{
\s*setMessage\("Account is not active"\);
\s*return;
\s*\}

\s*onLogin\(staff\);
\s*setMessage\("AFTER ONLOGIN"\);
'''

new_text, count = re.subn(pattern, "", text, count=1)

if count:
    p.write_text(new_text)
    print("✅ Removed duplicate login code")
else:
    print("❌ Duplicate block not found")
