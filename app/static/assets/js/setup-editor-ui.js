function downloadFile() {
  const fileLink = document.createElement("a");

  const filePath = document.getElementById("flask-data-file-path").textContent;

  fileLink.setAttribute("href", filePath);
  fileLink.setAttribute("download", "filename");
  fileLink.style.display = "none";

  document.body.appendChild(fileLink);

  fileLink.click();

  document.body.removeChild(fileLink);
}

function copyToClipboard(text) {
  navigator.clipboard
    .writeText(text)
    .then(() => {
      console.log("Link copied to clipboard: " + text);
    })
    .catch((err) => {
      console.error("Error copying link to clipboard: ", err);
    });
}

function copyLink() {
  const currentURL = window.location.href;
  const pathname = window.location.pathname;

  const domain = currentURL.replace(pathname, "");

  const filePath = document
    .getElementById("flask-data-file-path")
    .textContent.trim();

  const fullLink = `${domain}${filePath}`;
  copyToClipboard(fullLink);
}

function closeEditor() {
  const filePath = document
    .getElementById("flask-data-file-path")
    .textContent.trim();

  // Remove the first 5 characters (`/file`)
  var directoryPath = filePath.substring(5);

  // Remove the file name
  var lastSeparatorIndex = directoryPath.lastIndexOf("/");
  if (lastSeparatorIndex !== -1) {
    directoryPath = directoryPath.substring(0, lastSeparatorIndex);
  }

  window.location.href = `/browser${directoryPath}`;
}

function toggleFullscreen() {
  const page = document.documentElement;

  if (
    !document.fullscreenElement &&
    !document.mozFullScreenElement &&
    !document.webkitFullscreenElement &&
    !document.msFullscreenElement
  ) {
    // If the page is not in fullscreen, request fullscreen
    if (page.requestFullscreen) {
      page.requestFullscreen(); // Standard method
    } else if (page.mozRequestFullScreen) {
      page.mozRequestFullScreen(); // Firefox-specific method
    } else if (page.webkitRequestFullscreen) {
      page.webkitRequestFullscreen(); // Webkit-specific method
    } else if (page.msRequestFullscreen) {
      page.msRequestFullscreen(); // Microsoft-specific method
    }
  } else {
    // If the page is already in fullscreen, exit fullscreen
    if (document.exitFullscreen) {
      document.exitFullscreen(); // Standard method
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen(); // Firefox-specific method
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen(); // Webkit-specific method
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen(); // Microsoft-specific method
    }
  }
}
