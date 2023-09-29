function calculateCharacterLimit(screenWidth) {
  const referenceScreenWidth = 1920;
  const referenceCharacterLimit = 85;
  const characterLimit = Math.round(
    (screenWidth / referenceScreenWidth) * referenceCharacterLimit
  );
  return Math.max(characterLimit, 1);
}

function truncateText(className, screenWidth) {
  const characterLimit = calculateCharacterLimit(screenWidth);
  const elements = document.querySelectorAll("." + className);
  elements.forEach((element) => {
    const text = element.title;
    if (text.length > characterLimit) {
      const truncatedText = text.slice(0, characterLimit) + "...";
      element.textContent = truncatedText;
    } else {
      element.textContent = text; // Set to the original title text
    }
  });
}

function truncateTextOnLoad() {
  const screenWidth = window.innerWidth;
  truncateText("file-name", screenWidth);
}

function truncateTextOnResize() {
  const screenWidth = window.innerWidth;
  truncateText("file-name", screenWidth);
}

window.addEventListener("load", truncateTextOnLoad);
window.addEventListener("resize", truncateTextOnResize);
