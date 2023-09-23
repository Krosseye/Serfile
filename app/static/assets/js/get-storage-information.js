function updateStorageInfo() {
  fetch("/api/storage")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("storage-used").textContent = data.spaceUsed;
      document.getElementById("storage-total").textContent = data.spaceTotal;
      document.getElementById("storage-space").style.display = "block";
    })
    .catch((error) => {
      console.error("Error fetching storage information:", error);
    });
}

window.addEventListener("load", updateStorageInfo);
