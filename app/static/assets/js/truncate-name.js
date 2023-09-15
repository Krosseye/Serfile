function truncateTextContentByClass(className, limit) {
  const elements = document.querySelectorAll("." + className);
  elements.forEach((element) => {
    const text = element.textContent.trim();
    if (text.length > limit) {
      const truncatedText = text.slice(0, limit) + "...";

      element.textContent = truncatedText;
    }
  });
}
truncateTextContentByClass("file-name", 100);
