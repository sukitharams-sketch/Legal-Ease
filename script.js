document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const fileInput = document.getElementById("docUpload");
  const uploadBtn = document.getElementById("uploadBtn");
  const getStartedBtn = document.querySelector(".hero button");

  // Handle "Get Started" smooth scroll or action
  if (getStartedBtn) {
    getStartedBtn.addEventListener("click", () => {
      const generatorSection = document.getElementById("generate");
      if (generatorSection) {
        generatorSection.scrollIntoView({ behavior: "smooth" });
      } else {
        alert("Welcome to Legal-Ease! Select or upload a document to begin.");
      }
    });
  }

  // Handle Document Processing
  if (uploadBtn && fileInput) {
    uploadBtn.addEventListener("click", () => {
      const file = fileInput.files[0];

      if (!file) {
        alert("Please select a legal document (PDF, TXT, or DOCX) first.");
        return;
      }

      // Show processing state
      uploadBtn.textContent = "Analyzing Document...";
      uploadBtn.disabled = true;

      // Simulate AI analysis delay
      setTimeout(() => {
        alert(`Successfully analyzed "${file.name}"!\n\nSummary generated: Key terms, risks, and important clauses extracted.`);
        uploadBtn.textContent = "Process Document";
        uploadBtn.disabled = false;
      }, 1500);
    });
  }
});
