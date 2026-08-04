from pathlib import Path

file = Path("src/components/CameraCapture.jsx")
text = file.read_text()

marker = "useEffect(() => {"

addition = '''
  useEffect(() => {

    setTimestamp(new Date().toISOString());

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          setGps({
            latitude: pos.coords.latitude,
            longitude: pos.coords.longitude
          });
        },
        () => {}
      );
    }

    setDeviceInfo(navigator.userAgent);

    if (navigator.connection) {
      setNetworkInfo(
        navigator.connection.effectiveType || ""
      );
    }

    if (navigator.getBattery) {
      navigator.getBattery().then((battery) => {
        setBatteryLevel(
          Math.round(battery.level * 100)
        );
      });
    }

  }, []);

'''

if addition.strip() not in text:
    text = text.replace(marker, addition + "\n" + marker, 1)

file.write_text(text)

print("Enterprise Camera Step 2 complete")
