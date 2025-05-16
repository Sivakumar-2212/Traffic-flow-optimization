function updateTrafficData() {
    const trafficData = [
      "Heavy traffic on Route A due to construction 🚧",
      "Accident on Route C - expect 15 min delay 🚑",
      "Route B clear and optimal ✅",
      "Weather slowing down Route D ⛅"
    ];
  
    const suggestedRoutes = [
      "Use Route B for smooth flow",
      "Avoid Route C until cleared",
      "Alternate Route: Take E via Main Street",
      "Route A will improve post 6 PM"
    ];
  
    const responseTime = Math.floor(Math.random() * 80) + 40;
    const systemLoad = Math.floor(Math.random() * 50) + 30;
    const accuracy = (Math.random() * 5 + 95).toFixed(2);
  
    document.getElementById("traffic-data").innerText =
      trafficData[Math.floor(Math.random() * trafficData.length)];
  
    const routesList = document.getElementById("routes-list");
    routesList.innerHTML = "";
    suggestedRoutes.forEach(route => {
      const li = document.createElement("li");
      li.textContent = route;
      routesList.appendChild(li);
    });
  
    document.getElementById("response-time").innerText = responseTime;
    document.getElementById("system-load").innerText = systemLoad;
    document.getElementById("accuracy").innerText = accuracy;
  }
  
  setInterval(updateTrafficData, 5000);
  window.onload = updateTrafficData;
  