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

  const filePath = document.getElementById("flask-data-file-path").textContent;

  const fullLink = `${domain}${filePath}`;
  copyToClipboard(fullLink);
}
