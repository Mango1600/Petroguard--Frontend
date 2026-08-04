from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

# Add service imports
text = text.replace(
'import { VideoCapture } from "../components/VideoCapture";',
'import { VideoCapture } from "../components/VideoCapture";'
)

if 'getOpenBusinessDay' not in text:
    text = text.replace(
        'import VideoCapture from "../components/VideoCapture";',
        '''import VideoCapture from "../components/VideoCapture";
import { getOpenBusinessDay } from "../lib/businessDay";
import { createPumpShift } from "../lib/pumpShift";
import { createAssignment } from "../lib/pumpShiftAssignment";'''
    )

start = text.index("  async function createShift() {")

end = text.index("\n  if (showVideo)", start)

new_function = r'''  async function createShift() {

    try {

      const { data: businessDay, error: bdError } =
        await getOpenBusinessDay(staff.station_id);


      if (bdError) {
        throw bdError;
      }


      if (!businessDay) {
        throw new Error("No OPEN Business Day found.");
      }


      const pumpShift = await createPumpShift({

        businessDayId: businessDay.id,

        pumpId: Number(pumpId),

        openingMeter: Number(openingMeter),

        openingEvidence: null,

        staffId: staff.id

      });


      await createAssignment({

        pumpShiftId: pumpShift.id,

        staffId: staff.id,

        assignmentNo: 1,

        openingMeter: Number(openingMeter),

        openingEvidence: null,

        assignedBy: staff.id

      });


      setActiveShift(pumpShift);

      setMessage("✅ Pump Shift opened");


      if (onShiftOpened) {
        onShiftOpened();
      }


    } catch(error) {

      console.log(error);

      setMessage(error.message);

    }

  }

'''

text = text[:start] + new_function + text[end:]

file.write_text(text)

print("OpenShift production bridge patched")
