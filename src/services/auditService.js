src/services/auditService.jssrc/services/auditService.js
import { supabase } from "../lib/supabase";

export async function createAuditLog({
  companyId = null,
  stationId = null,
  moduleName,
  recordId,
  action,
  performedBy = null,
  oldData = null,
  newData = null,
}) {
  try {
    const { error } = await supabase
      .from("audit_logs")
      .insert({
        company_id: companyId,
        station_id: stationId,
        module_name: moduleName,
        record_id: String(recordId),
        action,
        performed_by: performedBy,
        old_data: oldData,
        new_data: newData,
      });

    if (error) throw error;

    return true;
  } catch (err) {
    console.error("Audit Log Error:", err);

    return false;
  }
}
