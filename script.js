document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("predictor-form");
    const resultDiv = document.getElementById("prediction-result");
    const fileInput = document.getElementById("document");
    const fileNameDisplay = document.getElementById("file-name");

    // Display file name when uploaded
    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = "Uploaded: " + fileInput.files[0].name;
        }
    });

    // Form submission handling
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        
        const score = parseInt(document.getElementById("exam-score").value);
        const course = document.getElementById("course").value;

        let predictionMessage = "";

        if (score > 85) {
            predictionMessage = "✅ High chance of getting into top colleges!";
        } else if (score > 60) {
            predictionMessage = "🔷 Might get admission in mid-tier colleges.";
        } else {
            predictionMessage = "⚠️ You may need to consider backup options.";
        }

        resultDiv.innerHTML = `<p>${predictionMessage}</p>`;
    });
});
