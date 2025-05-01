fetch('https://api.waqi.info/feed/delhi/?token=demo')
  .then(response => response.json())
  .then(data => {
    const aqi = data.data.aqi;
    document.getElementById('pollution-data').innerText = `Live AQI: ${aqi}`;
  })
  .catch(() => {
    document.getElementById('pollution-data').innerText = 'Failed to load AQI data';
  });