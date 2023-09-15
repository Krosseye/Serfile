function updateAnchorHref(className, supportedFileTypes) {
  const elements = document.getElementsByClassName(className);
  const path = document.getElementById("flask-data-path").textContent;
  for (const element of elements) {
    const fileName = element.textContent.trim();

    const fileExtension = fileName.split(".").pop().toLowerCase();

    if (supportedFileTypes.includes(fileExtension)) {
      element.href = `/edit/${path}/${fileName}`;
      element.target = "_self";
    }
  }
}

const supportedFileTypes = [
  "txt",
  "js",
  "html",
  "css",
  "json",
  "xml",
  "php",
  "java",
  "py",
  "rb",
  "cpp",
  "c",
  "h",
  "markdown",
  "md",
  "sql",
  "yaml",
  "yml",
  "ini",
  "conf",
  "sh",
  "jsx",
  "tsx",
  "jsx",
  "php",
  "vue",
  "perl",
];
updateAnchorHref("file-name", supportedFileTypes);
