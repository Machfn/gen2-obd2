


window.onload = () => {
    function updateFrame(new_url) {
        document.getElementById('live-source').contentWindow.location = `http://127.0.0.1:5550/${new_url}`
    }
    let speed_live = document.getElementById("live-speed");
    let rpm_live = document.getElementById("live-RPM");   
    let intake_live = document.getElementById("live-intake");
    
    speedSocket = new WebSocket(`ws://127.0.0.1:6112/speed_live`);
    speedSocket.onmessage = (event) => {
        // console.log(event)
        speed_live.innerHTML = event.data;
        // console.log(event.data);
    }

    rpmSocket = new WebSocket(`ws://127.0.0.1:6112/rpm_live`);
    rpmSocket.onmessage = (event) => {
        // console.log(event)
        rpm_live.innerHTML = event.data;
        // console.log(event.data);
    }

}