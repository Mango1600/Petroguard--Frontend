from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
text = p.read_text()

old = '''
await supabase
.from("attendant_assignments")
.insert({
pump_shift_id:pumpShiftId,
staff_id: loggedInStaff.id,
assignment_no:(last?.assignment_no||0)+1,
status:"ACTIVE",
opening_meter:openingMeter,
opening_evidence:evidence
});


setMessage("Pump Shift resumed successfully.");

setEvidence("");
setOpeningMeter("");
setTimeout(() => {
  if(onResumeSuccess){
    onResumeSuccess();
  }
}, 1000);
'''

new = '''
const { error } = await supabase
.from("attendant_assignments")
.insert({
pump_shift_id:pumpShiftId,
staff_id: loggedInStaff.id,
assignment_no:(last?.assignment_no||0)+1,
status:"ACTIVE",
opening_meter:openingMeter,
opening_evidence:evidence
});

if(error){
  return setMessage(error.message);
}

setMessage("Pump Shift resumed successfully.");

setEvidence("");
setOpeningMeter("");

await load();

if(onResumeSuccess){
  await onResumeSuccess();
}
'''

if old not in text:
    print("❌ Block not found.")
else:
    p.write_text(text.replace(old, new))
    print("✅ ResumeAssignment fixed.")
