import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function InventoryManagement() {

  const [inventory, setInventory] = useState([]);
  const [movements, setMovements] = useState([]);

  const [loading, setLoading] = useState(false);



  useEffect(() => {
    loadInventory();
    loadMovements();
  }, []);



  async function loadInventory() {

    setLoading(true);


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
      .order("created_at", {
        ascending: false,
      });



    if (error) {
      console.error(error);
      setLoading(false);
      return;
    }


    setInventory(data || []);

    setLoading(false);

  }



  async function loadMovements() {

    const { data, error } = await supabase
      .from("inventory_movements")
      .select(`
        id,
        movement_type,
        quantity,
        balance_after,
        reference_module,
        created_at,
        products(product_name),
        stations(name)
      `)
      .order("created_at", {
        ascending: false,
      });



    if (error) {
      console.error(error);
      return;
    }


    setMovements(data || []);

  }  return (
    <div>

      <h2>
        Inventory Management
      </h2>


      <button onClick={loadInventory}>
        Refresh Inventory
      </button>


      <hr />


      <h3>
        Current Stock
      </h3>


      {loading ? (

        <p>
          Loading inventory...
        </p>

      ) : inventory.length === 0 ? (

        <p>
          No inventory records found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>

              <th>
                Station
              </th>

              <th>
                Product
              </th>

              <th>
                Quantity
              </th>

              <th>
                Unit
              </th>

              <th>
                Type
              </th>

            </tr>

          </thead>


          <tbody>

            {inventory.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.stations?.name}
                </td>

                <td>
                  {item.products?.product_name}
                </td>

                <td>
                  {item.quantity}
                </td>

                <td>
                  {item.unit_of_measure}
                </td>

                <td>
                  {item.movement_type}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}


      <hr />


      <h3>
        Inventory Movement History
      </h3>


      {movements.length === 0 ? (

        <p>
          No movements found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>

              <th>
                Date
              </th>

              <th>
                Station
              </th>

              <th>
                Product
              </th>

              <th>
                Movement
              </th>

              <th>
                Quantity
              </th>

              <th>
                Balance
              </th>

              <th>
                Source
              </th>

            </tr>

          </thead>


          <tbody>

            {movements.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.created_at}
                </td>

                <td>
                  {item.stations?.name}
                </td>

                <td>
                  {item.products?.product_name}
                </td>

                <td>
                  {item.movement_type}
                </td>

                <td>
                  {item.quantity}
                </td>

                <td>
                  {item.balance_after}
                </td>

                <td>
                  {item.reference_module}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}

    </div>
  );

}
