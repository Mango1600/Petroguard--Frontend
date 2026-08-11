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
          .select("id, station_id, business_date, status")
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

      // Close the Business Day through one database transaction.
      const { data: updatedDay, error: closeError } =
        await supabase.rpc("close_business_day", {
          p_business_day_id: businessDay.id,
          p_staff_id: staff.id,
          p_auth_user_id: user.id
        });

      if (closeError) {
        throw closeError;
      }

      if (!updatedDay || updatedDay.status !== "CLOSED") {
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
