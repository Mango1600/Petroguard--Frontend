/**
 * PetroGuard Engine™
 * Verification Engine v1
 */

export const STATUS = {
  DRAFT: "DRAFT",
  SUBMITTED: "SUBMITTED",
  VERIFIED: "VERIFIED",
  APPROVED: "APPROVED",
};

export function canTransition(current, next) {
  const flow = {
    DRAFT: ["SUBMITTED"],
    SUBMITTED: ["VERIFIED"],
    VERIFIED: ["APPROVED"],
    APPROVED: [],
  };

  return flow[current]?.includes(next) || false;
}

export function changeStatus(record, nextStatus, userId = null) {
  const currentStatus = record.status || STATUS.DRAFT;

  if (!canTransition(currentStatus, nextStatus)) {
    return {
      success: false,
      error: `Invalid transition: ${currentStatus} → ${nextStatus}`,
    };
  }

  return {
    success: true,
    data: {
      ...record,
      status: nextStatus,
      updated_by: userId,
      updated_at: new Date().toISOString(),
    },
  };
}

export function isApproved(status) {
  return status === STATUS.APPROVED;
}src/engines/verificationEngine.js
