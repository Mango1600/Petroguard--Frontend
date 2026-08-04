from pathlib import Path

FILE = Path("src/pages/PumpShiftReconciliation.jsx")

text = FILE.read_text()

old = """
const [status,setStatus] = useState("CHECKING");
"""

new = """
const [status,setStatus] = useState("CHECKING");
const [auditTime,setAuditTime] = useState("");
const [gps,setGps] = useState(null);
"""

if old in text:
    text = text.replace(old,new,1)

old2 = """
useEffect(()=>{
load();
},[]);
"""

new2 = """
useEffect(()=>{
load();
captureAudit();
},[]);


function captureAudit(){

setAuditTime(
new Date().toLocaleString()
);


if(navigator.geolocation){

navigator.geolocation.getCurrentPosition(
(position)=>{

setGps({
latitude: position.coords.latitude,
longitude: position.coords.longitude,
accuracy: position.coords.accuracy
});

}
);

}

}
"""

if old2 in text:
    text = text.replace(old2,new2,1)


insert = """

<h3>
Audit Information
</h3>

<p>
Date / Time:
{auditTime}
</p>

<p>
GPS:
{
gps
?
`${gps.latitude}, ${gps.longitude} (±${gps.accuracy}m)`
:
"Waiting for location..."
}
</p>

"""


text = text.replace(
"""
<h3>
Reconciliation Status
</h3>
""",
insert +
"""
<h3>
Reconciliation Status
</h3>
""",
1
)


FILE.write_text(text)

print("Module 6 date time GPS audit layer added.")
