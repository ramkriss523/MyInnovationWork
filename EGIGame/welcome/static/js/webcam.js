cameraTrigger.onclick = function() {
  const canvas = document.createElement('canvas');
  document.querySelector('body').appendChild(canvas);
  const videoElement = document.querySelector('video');
  canvas.width = videoElement.width;
  canvas.height = videoElement.height;

  // copy full video frame into the canvas
  canvas.getContext('2d').drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);

  // get image data URL and remove canvas
  const snapshot = canvas.toDataURL("image/png");
  console.log(snapshot)
  document.getElementById("image_data").value += snapshot;
  console.log(document.getElementById("image_data").value)
  canvas.parentNode.removeChild(canvas);
};
