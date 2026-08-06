from pathlib import Path

print("""
Run this SQL in Supabase SQL Editor:

select 
id,
name,
email,
role,
user_id,
status
from staff
where email='manager@petroguard.com';
""")
