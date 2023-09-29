

window.onload = () => {

    let speed_live = document.getElementById("live-speed");
    let rpm_live = document.getElementById("live-RPM");   
    let intake_live = document.getElementById("live-intake");
    
    speedSocket = new WebSocket(`ws://127.0.0.1:6112/speed_live`);
    speedSocket.onmessage = (event) => {
        // console.log(event)
        speed_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }

    rpmSocket = new WebSocket(`ws://127.0.0.1:6112/rpm_live`);
    rpmSocket.onmessage = (event) => {
        // console.log(event)
        rpm_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }

    intakeSocket = new WebSocket(`ws://127.0.0.1:6112/intake_live`);
    intakeSocket.onmessage = (event) => {
        // console.log(event)
        intake_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }

}