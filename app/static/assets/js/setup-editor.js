let hasUnsavedChanges = false;
const fileNameElement = document.getElementById("filename");
const fileName = fileNameElement.textContent;
const title = document.getElementById("flask-data-title").textContent.trim();
const filePath = document
  .getElementById("flask-data-file-path")
  .textContent.trim();
const fileApiRoute = `/file/${filePath}`;

function checkDarkMode() {
  const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  return darkModeMediaQuery.matches;
}

function setupEditor() {
  const fileContentsElement = document.getElementById(
    "flask-data-file-contents"
  );
  const fileContents = fileContentsElement.textContent.trim();
  fileContentsElement.parentNode.removeChild(fileContentsElement);

  const editor = ace.edit("editor");
  const modelist = ace.require("ace/ext/modelist");
  const mode = modelist.getModeForPath(filePath).mode;

  editor.setTheme(`ace/theme/tomorrow${checkDarkMode() ? "_night" : ""}`);
  editor.getSession().setMode(mode);
  editor.getSession().setValue(fileContents);
  editor.setShowPrintMargin(false);
  editor.gotoLine(editor.getSession().getLength());
  editor.navigateLineEnd();

  editor.getSession().on("change", function () {
    hasUnsavedChanges = true;
    fileNameElement.textContent = `${fileName} •`;
    fileNameElement.setAttribute("title", `/${filePath} • Modified`);
  });

  return editor;
}

function saveChanges(editor) {
  const fileContent = editor.getSession().getValue();

  const formData = new FormData();
  formData.append(
    "file",
    new Blob([fileContent], { type: "application/octet-stream" }),
    filePath
  );

  fetch(`/api/update/${filePath}`, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (response.ok) {
        hasUnsavedChanges = false;
        fileNameElement.textContent = `${fileName}`;
        fileNameElement.setAttribute("title", `/${filePath}`);
        return response.json();
      } else {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
    })
    .then((result) => {
      showElementForTime("update-overlay", 1.5);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

window.addEventListener("beforeunload", function (e) {
  if (hasUnsavedChanges) {
    e.preventDefault();
    e.returnValue = ""; // Display a confirmation prompt
  }
});

window.addEventListener("load", function () {
  const editor = setupEditor();

  document
    .getElementById("editor-save-button")
    .addEventListener("click", function () {
      saveChanges(editor);
    });
});

function downloadFile() {
  const fileLink = document.createElement("a");

  const filePath = document
    .getElementById("flask-data-file-path")
    .textContent.trim();

  fileLink.setAttribute("href", `/file/${filePath}`);
  fileLink.setAttribute("download", "filename");
  fileLink.style.display = "none";

  document.body.appendChild(fileLink);

  fileLink.click();

  document.body.removeChild(fileLink);

  showElementForTime("download-overlay", 1.5);
}

function showElementForTime(elementId, timeLengthInSeconds) {
  const element = document.getElementById(elementId);
  if (!element) {
    console.error(`Element with ID "${elementId}" not found.`);
    return;
  }
  element.style.display = "flex";
  setTimeout(function () {
    element.style.display = "none";
  }, timeLengthInSeconds * 1000);
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

  const fullLink = `${domain}/file/${filePath}`;
  copyToClipboard(fullLink);
  showElementForTime("clipboard-overlay", 1.5);
}

function closeEditor() {
  const filePath = document
    .getElementById("flask-data-file-path")
    .textContent.trim();

  let directoryPath = filePath;

  // Remove the file name
  var lastSeparatorIndex = directoryPath.lastIndexOf("/");
  if (lastSeparatorIndex !== -1) {
    directoryPath = directoryPath.substring(0, lastSeparatorIndex);
  }

  window.location.href = `/browser/${directoryPath}`;
}

function toggleFullscreen() {
  const page = document.documentElement;

  if (
    !document.fullscreenElement &&
    !document.mozFullScreenElement &&
    !document.webkitFullscreenElement &&
    !document.msFullscreenElement
  ) {
    if (page.requestFullscreen) {
      page.requestFullscreen(); // Standard method
    } else if (page.mozRequestFullScreen) {
      page.mozRequestFullScreen(); // Firefox method
    } else if (page.webkitRequestFullscreen) {
      page.webkitRequestFullscreen(); // Webkit method
    } else if (page.msRequestFullscreen) {
      page.msRequestFullscreen(); // Microsoft method
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen(); // Standard method
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen(); // Firefox method
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen(); // Webkit method
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen(); // Microsoft method
    }
  }
}
