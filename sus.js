

window.onload = () => {

    let speed_live = document.getElementById("live-speed");
    let rpm_live = document.getElementById("live-RPM");   
    let intake_live = document.getElementById("live-intake");
    let fuel_live = document.getElementById("live-fuel");
    
    

    // Live speed data from websocket Quart App
    speedSocket = new WebSocket(`ws://127.0.0.1:6112/speed_live`);
    speedSocket.onmessage = (event) => {
        // console.log(event)
        speed_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }


    // Live Rmp data from websocket Quart App
    rpmSocket = new WebSocket(`ws://127.0.0.1:6112/rpm_live`);
    rpmSocket.onmessage = (event) => {
        // console.log(event)
        rpm_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }


    // Live intake data from websocket Quart App
    intakeSocket = new WebSocket(`ws://127.0.0.1:6112/intake_live`);
    intakeSocket.onmessage = (event) => {
        // console.log(event)
        intake_live.innerHTML = Math.round(event.data);
        // console.log(event.data);
    }

    //Livw Fuel Level from socket
    fuelSocket = new WebSocket(`ws://127.0.0.1:6112/fuel_live`);
    fuelSocket.onmessage = (event) => {
        // fuel info is passed down as string
        let fuel_data = event.data;
        fuel_live.innerHTML = `${fuel_data}%`;
    }
}