from pathlib import Path

p = Path("src/pages/CashDeclaration.jsx")

if not p.exists():
    print("❌ CashDeclaration.jsx not found")
    raise SystemExit

t = p.read_text()

if "showCreditCustomers" in t:
    print("✅ Credit customer section already exists")
    raise SystemExit

insert = '''

const [showCreditCustomers,setShowCreditCustomers]=useState(false);

const [creditCustomers,setCreditCustomers]=useState([
{
name:"",
invoice:"",
amount:"",
remarks:""
}
]);

function addCustomer(){
setCreditCustomers([
...creditCustomers,
{
name:"",
invoice:"",
amount:"",
remarks:""
}
]);
}

'''

t = t.replace(
'const [expenses',
insert + '\nconst [expenses'
)

ui = '''

<hr/>

<label>

<input
type="checkbox"
checked={showCreditCustomers}
onChange={(e)=>setShowCreditCustomers(e.target.checked)}
/>

 Credit sales made during this shift

</label>

{showCreditCustomers && (

<div>

{creditCustomers.map((c,i)=>(

<div
key={i}
style={{
border:"1px solid #ddd",
padding:10,
marginTop:10,
borderRadius:8
}}>

<input
placeholder="Customer Name"
value={c.name}
onChange={(e)=>{
const x=[...creditCustomers];
x[i].name=e.target.value;
setCreditCustomers(x);
}}
style={{width:"100%",padding:10}}
/>

<br/><br/>

<input
placeholder="Invoice / Credit Slip No."
value={c.invoice}
onChange={(e)=>{
const x=[...
