from pathlib import Path

file = Path("src/pages/AttendantPumpReading.jsx")

code = file.read_text()

# Add evidence save function before return
if "saveEvidence" not in code:

    insert = r'''

async function saveEvidence(fileData){

  try {

    const { data: evidence, error } = await supabase
      .from("evidence")
      .insert([{
        station_id: staff.station_id,
        uploaded_by: staff.user_id,
        evidence_type: "PHOTO",
        file_name: "opening_shift_evidence.jpg",
        file_path: fileData,
        mime_type: "image/jpeg",
        capture_time: new Date().toISOString(),
        description: "Opening shift evidence",
        status: "ACTIVE"
      }])
      .select()
      .single();


    if(error){
      console.log(error);
      alert("Evidence save failed");
      return;
    }


    await supabase
      .from("evidence_links")
      .insert([{
        evidence_id: evidence.id,
        module_name: "staff_shifts",
        record_id: String(shift.id)
      }]);


    setMessage("✅ Opening Evidence Saved");

  } catch(err){

    console.log(err);
    alert("Evidence error");

  }

}

'''

    code = code.replace(
        "return (",
        insert + "\nreturn ("
    )


# Connect CameraCapture callback
code = code.replace(
'''onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          setMessage("📹 Opening evidence captured");
        }}''',
'''onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          saveEvidence(evidence);
        }}'''
)


file.write_text(code)

print("✅ Evidence save connected to Shift")
