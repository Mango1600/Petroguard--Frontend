from pathlib import Path

target = Path("src/pages/AttendantPumpReading.jsx")

if not target.exists():
    print("❌ AttendantPumpReading.jsx not found")
    exit()

code = target.read_text()

if "saveAndStartShift" in code:
    print("✅ SAVE & START SHIFT already patched")
    exit()

function = r'''

async function saveAndStartShift() {

  try {

    if (!openingMeter) {
      alert("Opening meter required");
      return;
    }

    const { data: shift, error: shiftError } = await supabase
      .from("staff_shifts")
      .insert([{
        station_id: stationId,
        pump_id: pumpId,
        status: "open",
        opening_meter: Number(openingMeter),
        opened_by: staffId,
        start_time: new Date().toISOString()
      }])
      .select()
      .single();


    if (shiftError) {
      console.log(shiftError);
      alert("Shift creation failed");
      return;
    }


    const { error: attendantError } = await supabase
      .from("shift_attendants")
      .insert([{
        shift_id: shift.id,
        staff_id: staffId,
        status: "ACTIVE",
        activity_type: "SHIFT_STARTED",
        start_time: new Date().toISOString()
      }]);


    if (attendantError) {
      console.log(attendantError);
      alert("Attendant assignment failed");
      return;
    }


    alert("✅ PetroGuard Shift Started");

    window.location.reload();


  } catch (error) {

    console.log(error);
    alert("Error starting shift");

  }

}

'''

button = r'''

<button
onClick={saveAndStartShift}
style={{
 width:"100%",
 padding:12,
 marginTop:15
}}
>
▶ SAVE & START SHIFT
</button>

'''

# Add function before return
code = code.replace(
    "return (",
    function + "\nreturn (",
    1
)

# Add button before closing UI area
code = code.replace(
    "</div>",
    button + "\n</div>",
    1
)

target.write_text(code)

print("✅ PetroGuard SAVE & START SHIFT patch created")
