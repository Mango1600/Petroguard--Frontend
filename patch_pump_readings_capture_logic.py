from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
'  const [errorMessage, setErrorMessage] = useState("");',
'''  const [errorMessage, setErrorMessage] = useState("");

  const [activeShift, setActiveShift] = useState(null);
  const [activeAssignment, setActiveAssignment] = useState(null);

  const [openingMeter, setOpeningMeter] = useState("");
  const [closingMeter, setClosingMeter] = useState("");
  const [openingEvidence, setOpeningEvidence] = useState("");
  const [closingEvidence, setClosingEvidence] = useState("");'''
)

text = text.replace(
'  useEffect(() => {\\n    loadData();\\n  }, []);',
'''  useEffect(() => {
    loadData();
    loadActivePumpShift();
  }, []);'''
)

insert = '''

  async function loadActivePumpShift() {

    const { data: shift } = await supabase
      .from("pump_shifts")
      .select(`
        *,
        attendant_assignments(
          id,
          staff_id,
          status
        )
      `)
      .eq("status", "OPEN")
      .single();

    if (!shift) return;

    const assignment = shift.attendant_assignments?.find(
      (a) => a.status === "ACTIVE"
    );

    setActiveShift(shift);
    setActiveAssignment(assignment);
  }


  async function savePumpReading() {

    if (
      !activeShift ||
      !activeAssignment ||
      !openingMeter ||
      !closingMeter
    ) {
      alert("Complete pump shift, assignment and meter details");
      return;
    }


    const { error } = await supabase
      .from("pump_readings")
      .insert([
        {
          business_day_id: activeShift.business_day_id,
          pump_shift_id: activeShift.id,
          assignment_id: activeAssignment.id,
          staff_id: activeAssignment.staff_id,
          pump_id: activeShift.pump_id,

          opening_meter: Number(openingMeter),
          closing_meter: Number(closingMeter),

          opening_meter_photo: openingEvidence,
          closing_meter_photo: closingEvidence,

          status: "draft"
        }
      ]);


    if (error) {
      console.log(error);
      alert(error.message);
      return;
    }

    alert("Pump Reading Saved");

    loadData();
  }

'''

text = text.replace(
'  async function submitReading(id) {',
insert + '  async function submitReading(id) {'
)


file.write_text(text)

print("Pump reading capture logic added")
