import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function FuelDeliveryManagement() {

  const [suppliers, setSuppliers] = useState([]);
  const [stations, setStations] = useState([]);
  const [products, setProducts] = useState([]);
  const [deliveries, setDeliveries] = useState([]);

  const [supplierId, setSupplierId] = useState("");
  const [stationId, setStationId] = useState("");
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");


  useEffect(() => {
    loadSuppliers();
    loadStations();
    loadProducts();
  }, []);


  async function loadSuppliers() {

    const { data, error } = await supabase
      .from("suppliers")
      .select("id, supplier_name")
      .order("supplier_name");


    if (error) {
      console.error(error);
      return;
    }

    setSuppliers(data || []);

  }



  async function loadStations() {

    const { data, error } = await supabase
      .from("stations")
      .select("id, name")
      .order("name");


    if (error) {
      console.error(error);
      return;
    }

    setStations(data || []);

  }



  async function loadProducts() {

    const { data, error } = await supabase
      .from("products")
      .select("id, product_name, unit_of_measure")
      .order("product_name");


    if (error) {
      console.error(error);
      return;
    }

    setProducts(data || []);

  }  async function loadDeliveries() {

    const { data, error } = await supabase
      .from("inventory")
      .select(`
        id,
        quantity,
        unit_of_measure,
        movement_type,
        created_at,
        products(product_name),
        stations(name)
      `)
      .eq("reference_module", "Fuel Delivery")
      .order("created_at", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setDeliveries(data || []);

  }



  async function saveDelivery(e) {

    e.preventDefault();


    if (!supplierId || !stationId || !productId || !quantity) {
      setMessage("Please fill all fields");
      return;
    }


    setLoading(true);
    setMessage("");



    const selectedProduct = products.find(
      (product) => product.id === Number(productId)
    );


    const { data: inventoryData, error: inventoryError } =
      await supabase
        .from("inventory")
        .insert([
          {
            station_id: stationId,
            product_id: productId,
            quantity: Number(quantity),
            unit_of_measure: selectedProduct?.unit_of_measure || "Litre",
            movement_type: "IN",
            reference_module: "Fuel Delivery",
            reference_id: supplierId,
            notes: "Fuel delivery received",
          },
        ])
        .select()
        .single();



    if (inventoryError) {

      console.error(inventoryError);
      setMessage(inventoryError.message);
      setLoading(false);
      return;

    }



    await supabase
      .from("inventory_movements")
      .insert([
        {
          inventory_id: inventoryData.id,
          product_id: productId,
          station_id: stationId,
          movement_type: "IN",
          quantity: Number(quantity),
          balance_after: Number(quantity),
          reference_module: "Fuel Delivery",
          reference_id: supplierId,
          notes: "Fuel delivery received",
        },
      ]);



    setMessage("Fuel delivery recorded successfully");


    setSupplierId("");
    setStationId("");
    setProductId("");
    setQuantity("");


    await loadDeliveries();


    setLoading(false);

  }
  return (
    <div>

      <h2>
        Fuel Delivery Management
      </h2>


      {message && (
        <p>{message}</p>
      )}


      <hr />


      <h3>
        Receive Fuel Delivery
      </h3>


      <form onSubmit={saveDelivery}>


        <label>
          Supplier
        </label>
        <br />

        <select
          value={supplierId}
          onChange={(e) => setSupplierId(e.target.value)}
        >

          <option value="">
            Select Supplier
          </option>

          {suppliers.map((supplier) => (

            <option
              key={supplier.id}
              value={supplier.id}
            >
              {supplier.supplier_name}
            </option>

          ))}

        </select>


        <br />
        <br />


        <label>
          Station
        </label>
        <br />

        <select
          value={stationId}
          onChange={(e) => setStationId(e.target.value)}
        >

          <option value="">
            Select Station
          </option>

          {stations.map((station) => (

            <option
              key={station.id}
              value={station.id}
            >
              {station.name}
            </option>

          ))}

        </select>


        <br />
        <br />


        <label>
          Product
        </label>
        <br />

        <select
          value={productId}
          onChange={(e) => setProductId(e.target.value)}
        >

          <option value="">
            Select Product
          </option>

          {products.map((product) => (

            <option
              key={product.id}
              value={product.id}
            >
              {product.product_name}
            </option>

          ))}

        </select>


        <br />
        <br />


        <label>
          Quantity
        </label>
        <br />

        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          placeholder="Quantity received"
        />


        <br />
        <br />


        <button
          type="submit"
          disabled={loading}
        >

          {loading
            ? "Saving..."
            : "Receive Delivery"}

        </button>


      </form>


      <hr />


      <h3>
        Delivery History
      </h3>


      <button onClick={loadDeliveries}>
        Refresh
      </button>


      {deliveries.length === 0 ? (

        <p>
          No deliveries found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>

              <th>
                Product
              </th>

              <th>
                Station
              </th>

              <th>
                Quantity
              </th>

              <th>
                Unit
              </th>

              <th>
                Date
              </th>

            </tr>

          </thead>


          <tbody>

            {deliveries.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.products?.product_name}
                </td>

                <td>
                  {item.stations?.name}
                </td>

                <td>
                  {item.quantity}
                </td>

                <td>
                  {item.unit_of_measure}
                </td>

                <td>
                  {item.created_at}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}

    </div>
  );

}
