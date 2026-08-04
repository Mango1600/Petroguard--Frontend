from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

old = """
      manager_approval:
        settings?.manager_approval_required ? false : true
"""

new = """
      const { data: approval } = await supabase
        .from("daily_reconciliation")
        .select("status")
        .eq("station_id", staff.station_id)
        .eq("reconciliation_date", today)
        .maybeSingle();


      manager_approval:
        settings?.manager_approval_required
          ? approval?.status === "Approved"
          : true
"""

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Manager approval validation added successfully.")
