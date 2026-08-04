from pathlib import Path

code = r'''import { useState } from "react";

export default function CashDeclaration(){

const [cash,setCash]=useState("");
const [pos,setPos]=useState("");
const [transfer,setTransfer]=useState("");
const [credit,setCredit]=useState("");
const [expenses,setExpenses]=useState("");

const [customers,setCustomers]=useState([]);

function addCustomer(){

setCustomers([
...customers,
{
name:"",
invoice:"",
amount:"",
remarks:""
}
]);

}

return(

<div style={{padding:20,maxWidth:550,margin:"auto"}}>

<h2>💰 CASH DECLARATION</h2>

<input
placeholder="Cash at Hand"
value={cash}
onChange={(e)=>setCash(e.target.value)}
style={{width:"100%",padding:12}}
/>

<br/><br/>

<input
placeholder="POS Sales"
value={pos}
onChange={(e)=>setPos(e.target.value)}
style={{width:"100%",padding:12}}
/>

<br/><br/>

<input
placeholder="Bank Transfer"
value={transfer}
onChange={(e)=>setTransfer(e.target.value)}
style={{width:"100%",padding:12}}
/>

<br/><br/>

<input
