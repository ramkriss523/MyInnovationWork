var constraints = { video: { facingMode: "user" }, audio: false };
// Define constants
const cameraView = document.getElementById('video'),
    cameraOutput = document.getElementById("camera--output"),
    cameraSensor = document.getElementById("camera--sensor"),
    cameraTrigger = document.getElementById('next_btn'),
    image_1 = document.getElementById('video_img')
// Access the device camera and stream to cameraView
var localStream;
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
        cameraView.play();
        localStream = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}

const cameraToggle = document.getElementById('toggle_button');
const lbl_video = document.getElementById('lbl_video');
var flag = 0
cameraToggle.onclick = function() {
  if (flag == 1){
    localStream.getTracks()[0].stop();
    image_1.style.visibility='visible';
    cameraView.style.visibility='hidden';
    lbl_video.innerHTML = "Video Off";
    flag = 0;
  }
  else{
    cameraView.style.visibility='visible';
    image_1.style.visibility='hidden';
    lbl_video.innerHTML = "Video On";
    cameraStart();
    flag = 1;
  }
}
