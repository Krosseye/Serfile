const motd_status = document
  .getElementById("flask-data-motd")
  .textContent.toLowerCase();

const isMotdEnabled = motd_status === "true";

// Close MOTD banner
function closeMotd() {
  const motdBanner = document.getElementById("motd-banner");
  motdBanner.style.display = "none";
}

// Show MOTD banner
function showMotd() {
  const motdBanner = document.getElementById("motd-banner");
  motdBanner.style.display = "block";
}

// Event listener for close button
const closeMotdButton = document.getElementById("close-motd");
closeMotdButton.addEventListener("click", closeMotd);

// Check if MOTD is enabled and show or hide
window.addEventListener("load", function () {
  if (isMotdEnabled) {
    showMotd();
  } else {
    closeMotd();
  }
});
