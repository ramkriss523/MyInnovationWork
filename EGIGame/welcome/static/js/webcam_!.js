var constraints = { video: { facingMode: "user" }, audio: false };
// Define constants
const cameraView = document.getElementById('video'),
    cameraOutput = document.getElementById("camera--output"),
    cameraSensor = document.getElementById("camera--sensor"),
    cameraTrigger = document.getElementById('next_btn')
// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
        cameraView.play();
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}
window.addEventListener("load", cameraStart, false);
