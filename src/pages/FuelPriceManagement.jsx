import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function FuelPriceManagement() {

  const [prices, setPrices] = useState([]);

  const [productType, setProductType] = useState("PMS");
  const [unitPrice, setUnitPrice] = useState("");
  const [effectiveDate, setEffectiveDate] = useState("");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");


  useEffect(() => {
    loadPrices();
  }, []);


  async function loadPrices() {

    const { data, error } = await supabase
      .from("fuel_prices")
      .select("*")
      .order("effective_date", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setPrices(data || []);

  }



  async function savePrice(e) {

    e.preventDefault();


    if (!productType || !unitPrice || !effectiveDate) {
      setMessage("Please fill all fields");
      return;
    }


    setLoading(true);
    setMessage("");


    const { error } = await supabase
      .from("fuel_prices")
      .insert([
        {
          product_type: productType,
          unit_price: Number(unitPrice),
          effective_date: effectiveDate,
        },
      ]);



    if (error) {

      console.error(error);
      setMessage(error.message);
      setLoading(false);
      return;

    }


    setMessage("Price added successfully");


    setUnitPrice("");
    setEffectiveDate("");


    await loadPrices();


    setLoading(false);

  }  return (
    <div>

      <h2>
        Fuel Price Management
      </h2>


      {message && (
        <p>{message}</p>
      )}


      <hr />


      <h3>
        Add New Price
      </h3>


      <form onSubmit={savePrice}>


        <div>
          <label>
            Product Type
          </label>

          <br />

          <select
            value={productType}
            onChange={(e) => setProductType(e.target.value)}
          >

            <option value="PMS">
              PMS
            </option>

            <option value="AGO">
              AGO
            </option>

            <option value="DPK">
              DPK
            </option>

            <option value="LPG">
              LPG
            </option>

            <option value="CNG">
              CNG
            </option>

          </select>

        </div>


        <br />


        <div>
          <label>
            Unit Price
          </label>

          <br />

          <input
            type="number"
            value={unitPrice}
            onChange={(e) => setUnitPrice(e.target.value)}
            placeholder="Enter price"
          />

        </div>


        <br />


        <div>
          <label>
            Effective Date
          </label>

          <br />

          <input
            type="date"
            value={effectiveDate}
            onChange={(e) => setEffectiveDate(e.target.value)}
          />

        </div>


        <br />


        <button
          type="submit"
          disabled={loading}
        >

          {loading
            ? "Saving..."
            : "Save Price"}

        </button>


      </form>


      <hr />


      <h3>
        Price History
      </h3>


      {prices.length === 0 ? (

        <p>
          No prices found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>

              <th>
                ID
              </th>

              <th>
                Product
              </th>

              <th>
                Unit Price
              </th>

              <th>
                Effective Date
              </th>

              <th>
                Created
              </th>

            </tr>

          </thead>


          <tbody>

            {prices.map((price) => (

              <tr key={price.id}>

                <td>
                  {price.id}
                </td>

                <td>
                  {price.product_type}
                </td>

                <td>
                  {price.unit_price}
                </td>

                <td>
                  {price.effective_date}
                </td>

                <td>
                  {price.created_at}
                </td>

              </tr>

            ))}

          </tbody>


        </table>

      )}

    </div>
  );
}
