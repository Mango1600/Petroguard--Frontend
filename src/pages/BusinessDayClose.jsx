import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function BusinessDayClose({ staff }) {
  const [message, setMessage] = useState("");
  const [closing, setClosing] = useState(false);

  async function closeBusinessDay() {
    if (!staff?.station_id || !staff?.id) {
      setMessage("Manager staff information is not available.");
      return;
    }

    setClosing(true);
    setMessage("");

    try {
      // Get the authenticated Supabase user.
      const {
        data: { user },
        error: userError
      } = await supabase.auth.getUser();

      if (userError) {
        throw userError;
      }

      if (!user?.id) {
        throw new Error("Authenticated Manager user could not be identified.");
      }

      // Find the current OPEN Business Day for this station.
      const { data: businessDay, error: businessDayError } =
        await supabase
          .from("business_days")
          .select("*")
          .eq("station_id", staff.station_id)
          .eq("status", "OPEN")
          .order("opened_at", { ascending: false })
          .limit(1)
          .maybeSingle();

      if (businessDayError) {
        throw businessDayError;
      }

      if (!businessDay) {
        setMessage("No OPEN Business Day found for this station.");
        return;
      }

      // Record the closure using the LIVE business_day_closures schema.
      const { error: closureError } = await supabase
        .from("business_day_closures")
        .insert({
          station_id: businessDay.station_id,
          business_date: businessDay.business_date,
          closed_by: staff.id,
          status: "CLOSED",
          pump_readings_completed: true,
          tank_dip_completed: true,
          payment_summary_completed: true,
          manager_approval_completed: true,
          notes: "Business Day closed from Manager Dashboard"
        });

      if (closureError) {
        throw closureError;
      }

      // Actually close the Business Day.
      const { data: updatedDay, error: updateError } =
        await supabase
          .from("business_days")
          .update({
            status: "CLOSED",
            closed_at: new Date().toISOString(),
            closed_by: user.id
          })
          .eq("id", businessDay.id)
          .eq("station_id", staff.station_id)
          .eq("status", "OPEN")
          .select()
          .single();

      if (updateError) {
        throw updateError;
      }

      // Never report success unless the database confirms CLOSED.
      if (updatedDay?.status !== "CLOSED") {
        throw new Error(
          "Business Day close could not be verified in the database."
        );
      }

      setMessage(
        `Business Day ${updatedDay.id} (${updatedDay.business_date}) closed successfully.`
      );
    } catch (error) {
      console.error("Business Day Close Error:", error);
      setMessage(error.message || "Unable to close Business Day.");
    } finally {
      setClosing(false);
    }
  }

  return (
    <div>
      <h2>🔒 Close Business Day</h2>

      <p>
        <strong>Station:</strong> {staff?.station_id ?? "-"}
      </p>

      <p>
        This will close the currently OPEN Business Day for this station.
      </p>

      <button
        onClick={closeBusinessDay}
        disabled={closing}
      >
        {closing ? "Closing Business Day..." : "Close Business Day"}
      </button>

      <p>{message}</p>
    </div>
  );
}
