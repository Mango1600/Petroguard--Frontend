from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

old = """async function load(){

const {data:last}=await supabase
.from("attendant_assignments")
.select("closing_meter")
.eq("pump_shift_id",pumpShiftId)
.order("assignment_no",{ascending:false})
.limit(1)
.single();

if(last){
setPreviousMeter(last.closing_meter);
setOpeningMeter(last.closing_meter);
}
"""

new = """async function load(){

const businessDay = await getOpenBusinessDay(1);

if(!businessDay){
setMessage("No OPEN Business Day found.");
return;
}

const pumpShift = await getOpenPumpShift(businessDay.id);

if(!pumpShift){
setMessage("No OPEN Pump Shift found.");
return;
}

const previous = await getPreviousAssignment(pumpShift.id);

if(previous){
setPreviousMeter(previous.closing_meter);
setOpeningMeter(previous.closing_meter);
}
"""

if old in text:
    text = text.replace(old, new, 1)
    FILE.write_text(text)
    print("Dynamic Business Day and Pump Shift loading connected.")
else:
    print("Target block not found.")
