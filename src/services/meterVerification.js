export function verifyMeterReading({
  enteredReading,
  ocrReading
}) {
  const entered = Number(enteredReading);
  const ocr = Number(ocrReading);

  return {
    enteredReading: entered,
    ocrReading: ocr,
    matched: entered === ocr,
    difference: Math.abs(entered - ocr)
  };
}
