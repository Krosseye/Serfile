function isMotdBannerClosed() {
  return sessionStorage.getItem("motdClosed") === "true";
}

function setMotdBannerClosed() {
  sessionStorage.setItem("motdClosed", "true");
}

// Fetch MOTD data from API
function fetchMotdData() {
  // Check if MOTD banner is closed in session storage
  if (isMotdBannerClosed()) {
    return;
  }

  fetch("/api/motd")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const isMotdEnabled = data.enabled;
      const title = data.title;
      const message = data.message;

      updateMotdDisplay(isMotdEnabled, title, message);
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// Update MOTD display
function updateMotdDisplay(isMotdEnabled, title, message) {
  const motdBanner = document.getElementById("motd-banner");
  const titleElement = document.getElementById("motd-title");
  const messageElement = document.getElementById("motd-message");

  if (isMotdEnabled) {
    showMotd(motdBanner);
    titleElement.textContent = title;
    messageElement.textContent = message;
  } else {
    closeMotd(motdBanner);
    titleElement.textContent = "";
    messageElement.textContent = "";
  }
}

// Close MOTD banner and set session storage
function closeMotd(motdBanner) {
  motdBanner.style.display = "none";
  setMotdBannerClosed();
}

// Show MOTD banner
function showMotd(motdBanner) {
  motdBanner.style.display = "block";
}

// Event listener for close button
const closeMotdButton = document.getElementById("close-motd");
closeMotdButton.addEventListener("click", function () {
  closeMotd(document.getElementById("motd-banner"));
});

// Fetch MOTD status and update when page loads
window.addEventListener("load", fetchMotdData);
