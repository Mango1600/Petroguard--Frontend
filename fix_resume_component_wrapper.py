from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

marker = "async function load(){"

if "export default function ResumeAssignment" not in text:

    text = text.replace(
        marker,
        """
export default function ResumeAssignment({
  loggedInStaff,
  onResumeSuccess
}){

const [message,setMessage] = useState("");
const [previousMeter,setPreviousMeter] = useState("");
const [openingMeter,setOpeningMeter] = useState("");
const [evidence,setEvidence] = useState("");
const [attendants,setAttendants] = useState([]);

useEffect(()=>{
  load();
},[]);

""" + marker
    )

    text += "\n}\n"

    file.write_text(text)

    print("ResumeAssignment component wrapper restored.")

else:
    print("Wrapper already exists.")
