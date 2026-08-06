import { verifyMeterReading } from "../services/meterVerification";

export default function MeterVerification({
  enteredReading,
  ocrReading,
  onVerified,
  onFailed
}) {
  const result = verifyMeterReading({
    enteredReading,
    ocrReading
  });

  if (result.matched) {
    onVerified(result);
  } else {
    onFailed(result);
  }

  return (
    <div style={{padding:10}}>
      <b>Entered:</b> {result.enteredReading}<br/>
      <b>OCR:</b> {result.ocrReading}<br/>
      <b>Status:</b> {result.matched ? "✅ VERIFIED" : "❌ MISMATCH"}
    </div>
  );
}
