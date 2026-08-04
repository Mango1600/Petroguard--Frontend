import { useEffect, useState } from "react";
import { getOCC } from "../lib/occApi";

export default function OCCPanel() {
  const [occ, setOcc] = useState(null);

  useEffect(() => {
    getOCC().then(setOcc).catch(console.error);
  }, []);

  if (!occ) return <p>Loading OCC...</p>;

  return (
    <div>
      <h2>⛽ PetroGuard OCC</h2>
      <p>Business: {occ.business?.status}</p>
      <p>Staff Present: {occ.attendance?.length}</p>
      <p>Sales: ₦{occ.sales?.total}</p>
      <p>Tank Variance: {occ.tank?.variance} L</p>
      <p>Reconciliation: {occ.reconciliation?.status}</p>
    </div>
  );
}