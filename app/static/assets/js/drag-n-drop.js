const dropArea = document.getElementById("drop-area");
const path = document.getElementById("flask-data-path").textContent;
const uploadOverlay = document.getElementById("upload-overlay");
const body = document.getElementById("body");
const progressDiv = document.getElementById("upload-progress");
const progressOverlay = document.getElementById("upload-progress-overlay"); // Add this line

let totalFiles = 0;
let currentFileIndex = 0;
let successfulUploads = 0;

// Handle file drop
function handleFileDrop(e) {
  e.preventDefault();
  if (e.dataTransfer.types.includes("Files")) {
    const files = e.dataTransfer.files;
    totalFiles = files.length;
    currentFileIndex = 0;
    successfulUploads = 0;
    document.getElementById("upload-progress-icon").textContent = "⏳";
    progressOverlay.style.display = "flex"; // Show the progress overlay
    uploadNextFile(files);
    uploadOverlay.style.display = "none";
  }
}

// Handle drag leave event
function handleDragLeave(e) {
  e.preventDefault();
  uploadOverlay.style.display = "none";
}

// Handle file upload
function uploadNextFile(files) {
  if (currentFileIndex < totalFiles) {
    const file = files[currentFileIndex];
    const formData = new FormData();
    formData.append("file", file);

    const directory = path;
    const overwrite = false;

    progressDiv.textContent = `Uploading file ${
      currentFileIndex + 1
    }  of ${totalFiles}`;

    // Send the file to the API endpoint
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
          successfulUploads++;
        } else {
          // handleUploadError();
        }

        currentFileIndex++;
        uploadNextFile(files); // Upload the next file

        // Check if all files are uploaded
        if (currentFileIndex === totalFiles) {
          // All files have been uploaded
          if (successfulUploads === totalFiles) {
            progressDiv.textContent = "All files uploaded successfully";
          } else {
            document.getElementById("upload-progress-icon").textContent = "🤕";
            progressDiv.textContent = "Some files failed to upload";
          }
          // Refresh the page after all files are successfully uploaded
          if (successfulUploads === totalFiles) {
            window.location.reload();
            progressOverlay.style.display = "none"; // Hide the progress overlay
          }
        }
      })
      .catch((error) => {
        console.error("File upload failed:", error);
        // handleUploadError();
        currentFileIndex++;
        uploadNextFile(files); // Upload the next file
      });
  }
}

const closeButton = document.getElementById("close-upload-progress-overlay");
closeButton.addEventListener("click", function () {
  document.getElementById("upload-progress-overlay").style.display = "none";
});

// Handle upload errors
function handleUploadError() {
  alert("File upload failed");
}

// Event listeners
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  if (e.dataTransfer.types.includes("Files")) {
    uploadOverlay.style.display = "flex";
  }
});

dropArea.addEventListener("drop", handleFileDrop);
dropArea.addEventListener("dragleave", handleDragLeave);

// Prevent default drag-n-drop behavior for body
body.addEventListener("dragenter", preventDefaultBehavior);
body.addEventListener("dragover", preventDefaultBehavior);
body.addEventListener("drop", preventDefaultBehavior);
function preventDefaultBehavior(event) {
  event.preventDefault();
}
