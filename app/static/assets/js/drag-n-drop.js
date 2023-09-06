const dropArea = document.getElementById("drop-area");
const path = document.getElementById("flask-data-path").textContent;
const uploadOverlay = document.getElementById("upload-overlay");

// Handle file drop
function handleFileDrop(e) {
  e.preventDefault();
  const files = e.dataTransfer.files;
  uploadFiles(files);
  uploadOverlay.style.display = "none";
}

// Handle drag leave event
function handleDragLeave(e) {
  e.preventDefault();
  uploadOverlay.style.display = "none";
}

// Handle file upload
function uploadFiles(files) {
  const formData = new FormData();
  for (const file of files) {
    formData.append("file", file);
  }

  const directory = path;
  const overwrite = false;

  // Send files to API endpoint
  fetch(`/api/upload/${directory}?overwrite=${overwrite}`, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);

      // Check if upload was successful
      if (
        data.message === "File uploaded successfully" ||
        data.message === "File overwritten successfully"
      ) {
        window.location.reload();
      } else {
        handleUploadError();
      }
    })
    .catch((error) => {
      console.error("File upload failed:", error);
      handleUploadError();
    });
}

// Handle upload errors
function handleUploadError() {
  alert("File upload failed");
}

// Event listeners
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadOverlay.style.display = "flex";
});

dropArea.addEventListener("drop", handleFileDrop);
dropArea.addEventListener("dragleave", handleDragLeave);
