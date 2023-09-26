function updateFrame(new_url) {
    document.getElementById('live-source').contentWindow.location = `http://127.0.0.1:5550/${new_url}`
}