import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import { uploadEvidence } from "../services/evidenceService";
export default function TankDipEntry({ staff }) {
  console.log("TankDipEntry staff:", staff);
  const [tanks, setTanks] = useState([]);
  const [loading, setLoading] = useState(false);
const [evidenceImage, setEvidenceImage] = useState(null);

  const [form, setForm] = useState({
    tank_id: "",
    product_type: "",
    reading_period: "Morning",
    opening_volume: "",
    deliveries: "",
    closing_volume: "",
    expected_volume: "",
    variance: "",
    reading_date: new Date().toISOString().slice(0, 10),
    status: "DRAFT",
  });

  useEffect(() => {
  loadTanks();
}, [staff]);

  async function loadTanks() {
    if (!staff?.station_id) {
      console.log("No staff station yet");
      return;
    }

    setLoading(true);

    const { data, error } = await supabase
      .from("tanks")
      .select("*")
      .eq("station_id", staff.station_id)
      .order("tank_name");
console.log("STAFF:", staff);
console.log("TANKS:", data);
console.log("ERROR:", error);


    if (error) {
      alert(error.message);
      setLoading(false);
      return;
    }

    setTanks(data || []);
    setLoading(false);
  }  async function handleTankChange(tankId) {
    const tank = tanks.find((t) => t.id === Number(tankId));

    if (!tank) return;

    const { data } = await supabase
      .from("tank_readings")
      .select("closing_volume")
      .eq("tank_id", tank.id)
      .order("reading_date", { ascending: false })
      .limit(1);

    const opening =
      data && data.length > 0
        ? Number(data[0].closing_volume)
        : Number(tank.current_volume || 0);

    setForm((prev) => ({
      ...prev,
      tank_id: tank.id,
      product_type: tank.product_type,
      opening_volume: opening,
    }));
  }

  function calculateValues(closingVolume, deliveries) {
    const opening = Number(form.opening_volume || 0);
    const delivered = Number(deliveries || 0);
    const closing = Number(closingVolume || 0);

    const expected = opening + delivered;
    const variance = closing - expected;

    setForm((prev) => ({
      ...prev,
      closing_volume: closing,
      deliveries: delivered,
      expected_volume: expected,
      variance: variance,
    }));
  }

  async function saveReading(e) {
    e.preventDefault();
if (!form.tank_id) {
  alert("Please select a tank.");
  return;
}

if (Number(form.closing_volume) <= 0) {
  alert("Closing volume must be greater than zero.");
  return;
}

if (
  Number(form.opening_volume) === 0 &&
  Number(form.deliveries) === 0 &&
  Number(form.closing_volume) > 0
) {
  alert(
    "Opening volume cannot be zero for a normal tank dip. Use Initial Stock Entry for a new tank."
  );
  return;
}

    const { data: reading, error } = await supabase
      .from("tank_readings")
      .insert([
        {
          tank_id: Number(form.tank_id),
          station_id: staff.station_id,
          staff_id: staff.id,
          product_type: form.product_type,
          opening_volume: Number(form.opening_volume),
          deliveries: Number(form.deliveries),
          closing_volume: Number(form.closing_volume),
          expected_volume: Number(form.expected_volume),
          variance: Number(form.variance),
          reading_period: form.reading_period,
          reading_date: form.reading_date,
          status: "DRAFT",
        },
            ])
      .select()
      .single();

    if (error) {
      alert(error.message);
      return;
    }
if (evidenceImage) {
  await uploadEvidence({
    imageData: evidenceImage,
    fileName: "tank-dip-photo.jpg",
    stationId: staff.station_id,
    recordId: reading.id,
    moduleName: "tank_readings",
    evidenceType: "TANK_DIP_PHOTO",
    uploadedBy: staff.id,
  });
}
await supabase
  .from("tanks")
  .update({
    current_volume: Number(form.closing_volume),
  })
  .eq("id", Number(form.tank_id));

    alert("Tank dip reading saved successfully.");

    setForm({
      tank_id: "",
      product_type: "",
      reading_period: "Morning",
      opening_volume: "",
      deliveries: 0,
      closing_volume: "",
      expected_volume: "",
      variance: "",
      reading_date: new Date().toISOString().slice(0, 10),
      status: "DRAFT",
    });

    loadTanks();
  }  return (
    <div>
      <h2>Tank Dip Entry</h2>

      {loading ? (
        <p>Loading tanks...</p>
      ) : (
        <form onSubmit={saveReading}>

          <label>Tank</label>
          <br /> *
          <select

            value={form.tank_id}
            onChange={(e) => handleTankChange(e.target.value)}
          >
            <option value="">Select Tank</option>

            {tanks.map((tank) => (
              <option key={tank.id} value={tank.id}>
                {tank.tank_name} ({tank.product_type})
              </option>
            ))}
          </select>
<p>Number of tanks: {tanks.length}</p>

<ul>
  {tanks.map((tank) => (
    <li key={tank.id}>
      {tank.tank_name} ({tank.product_type})
    </li>
  ))}
</ul>

          <br />

          <CameraCapture
            onCapture={(image) => setEvidenceImage(image)}
          />

          <br />

          <button type="submit">
            Save Tank Dip Reading
          </button>

        </form>
      )}
    </div>
  );
}
