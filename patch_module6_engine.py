from pathlib import Path

FILE = Path("src/pages/PumpShiftReconciliation.jsx")

text = FILE.read_text()

text = text.replace(
'''const [status,setStatus] = useState("CHECKING");''',
'''const [status,setStatus] = useState("CHECKING");
const [variance,setVariance] = useState(0);
const [meterStatus,setMeterStatus] = useState("CHECKING");
const [evidenceStatus,setEvidenceStatus] = useState("CHECKING");'''
)

old = '''function validate(data){

let result="PASS";


data.forEach(item=>{

if(
!item.opening_evidence ||
!item.closing_evidence
){

result="REVIEW REQUIRED";

}

});


setStatus(result);

}'''

new = '''async function validate(data){

let result="PASS";


let evidenceOK=true;

data.forEach(item=>{

if(
!item.opening_evidence ||
!item.closing_evidence
){

evidenceOK=false;

}

});


setEvidenceStatus(
evidenceOK ? "COMPLETE" : "MISSING"
);


if(!evidenceOK){

result="REVIEW REQUIRED";

}


let opening = Number(
data[0]?.opening_meter || 0
);


let closing = Number(
data[data.length-1]?.closing_meter || 0
);


let movement = closing - opening;


setMeterStatus(
movement >= 0 ? "OK" : "CHECK"
);


setVariance(movement);


setStatus(result);

}'''

if old in text:
    text = text.replace(old,new,1)

insert = '''
<h3>
Meter Movement
</h3>

<p>
Total Meter Movement: {variance}
</p>

<p>
Meter Status: {meterStatus}
</p>


<h3>
Evidence Status
</h3>

<p>
{evidenceStatus}
</p>
'''

text = text.replace(
'''<h3>
Reconciliation Status
</h3>''',
insert +
'''
<h3>
Reconciliation Status
</h3>'''
)

FILE.write_text(text)

print("Module 6 reconciliation engine added.")
