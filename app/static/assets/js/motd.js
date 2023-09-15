// Fetch MOTD data from API and store in session storage
function fetchMotdData() {
  if (isMotdBannerClosed()) {
    return;
  }

  if (!motdFetched) {
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

        // Store MOTD in session storage
        sessionStorage.setItem("motdFetched", "true");
        sessionStorage.setItem("motdTitle", title);
        sessionStorage.setItem("motdMessage", message);

        updateMotdDisplay(isMotdEnabled, title, message);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  } else {
    // MOTD has already been fetched
    const title = sessionStorage.getItem("motdTitle");
    const message = sessionStorage.getItem("motdMessage");
    updateMotdDisplay(true, title, message);
    shouldShowMotd();
  }
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

function isMotdBannerClosed() {
  return sessionStorage.getItem("motdClosed") === "true";
}

function setMotdBannerClosed() {
  sessionStorage.setItem("motdClosed", "true");
}

function shouldShowMotd() {
  if (!motdFetched || isMotdBannerClosed()) {
    return;
  }

  const motdBanner = document.getElementById("motd-banner");
  if (motdBanner.style.display !== "flex") {
    showMotd(motdBanner);
  }
}

function closeMotd(motdBanner) {
  motdBanner.style.display = "none";
  setMotdBannerClosed();
}

function showMotd(motdBanner) {
  motdBanner.style.display = "flex";
}

const motdFetched = sessionStorage.getItem("motdFetched") === "true";

// Event listener for close button
const closeMotdButton = document.getElementById("close-motd");
closeMotdButton.addEventListener("click", function () {
  closeMotd(document.getElementById("motd-banner"));
});

// Fetch MOTD status and update when page loads
window.addEventListener("load", fetchMotdData);
