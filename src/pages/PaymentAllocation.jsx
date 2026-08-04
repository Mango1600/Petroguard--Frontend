
import { useState, useEffect } from "react";
import { supabase } from "../lib/supabase";



function payment_rows() {

    return [
        {
            payment_method: "CASH",
            amount: Number(cash || 0)
        },

        {
            payment_method: "POS",
            amount: Number(pos || 0)
        },

        {
            payment_method: "BANK_TRANSFER",
            amount: Number(bankTransfer || 0)
        },

        {
            payment_method: "CREDIT",
            amount: Number(credit || 0)
        }

    ].filter(
        item => item.amount > 0
    );
}


export default function PaymentAllocation({ meterSale }) {

  const [totalSales, setTotalSales] = useState(0);

  const [cash, setCash] = useState("");
  const [pos, setPos] = useState("");
  const [bankTransfer, setBankTransfer] = useState("");
  const [credit, setCredit] = useState("");

  const [customerName, setCustomerName] = useState("");
  const [customerPhone, setCustomerPhone] = useState("");

  const [message, setMessage] = useState("");

  useEffect(() => {
    if (meterSale) {
      setTotalSales(meterSale.total_amount);
    }
  }, [meterSale]);


  function validate() {

    const allocated =
      Number(cash || 0) +
      Number(pos || 0) +
      Number(bankTransfer || 0) +
      Number(credit || 0);


    if (allocated !== Number(totalSales)) {
      setMessage(
        "Payment allocation must equal calculated sales amount"
      );
      return false;
    }


    if (Number(credit || 0) > 0) {

      if (!customerName || !customerPhone) {
        setMessage(
          "Customer details required for credit sales"
        );
        return false;
      }
    }


    return true;
  }


  async function saveAllocation() {

    if (!validate()) return;


    setMessage("Allocation ready for submission");
  }


  return (
    <div>

      <h2>Payment Allocation</h2>

      <h3>
        Calculated Sales: ₦{totalSales}
      </h3>

      <input
        placeholder="Cash"
        value={cash}
        onChange={(e)=>setCash(e.target.value)}
      />

      <input
        placeholder="POS"
        value={pos}
        onChange={(e)=>setPos(e.target.value)}
      />

      <input
        placeholder="Bank Transfer"
        value={bankTransfer}
        onChange={(e)=>setBankTransfer(e.target.value)}
      />

      <input
        placeholder="Credit"
        value={credit}
        onChange={(e)=>setCredit(e.target.value)}
      />


      {Number(credit || 0) > 0 && (
        <>
          <input
            placeholder="Customer Name"
            value={customerName}
            onChange={(e)=>setCustomerName(e.target.value)}
          />

          <input
            placeholder="Customer Phone"
            value={customerPhone}
            onChange={(e)=>setCustomerPhone(e.target.value)}
          />
        </>
      )}


      <button onClick={saveAllocation}>
        Validate Payment
      </button>

      <p>{message}</p>

    </div>
  );


async function savePaymentAllocation() {

    if (!validate()) return;

    const allocation = {
        business_day_id: meterSale.business_day_id,
        pump_shift_id: meterSale.pump_shift_id,
        assignment_id: meterSale.assignment_id,
        meter_sale_id: meterSale.id,

        payment_method: "MULTIPLE",

        amount:
            Number(cash || 0) +
            Number(pos || 0) +
            Number(bankTransfer || 0) +
            Number(credit || 0),

        customer_name:
            Number(credit || 0) > 0
            ? customerName
            : null,

        customer_phone:
            Number(credit || 0) > 0
            ? customerPhone
            : null
    };


    const { error } = await supabase
        .from("payment_allocations")
        .insert(allocation);


    if (error) {
        setMessage(error.message);
        return;
    }

    setMessage(
        "Payment allocation saved successfully"
    );
}

}
