// document.getElementById("marksheet").addEventListener("change", function() {
//     document.getElementById("file-name").innerText = "Uploaded: " + this.files[0].name;
// });

// document.getElementById("stream").addEventListener("change", updatePrediction);
// document.getElementById("marks").addEventListener("input", updatePrediction);

// function updatePrediction() {
//     let stream = document.getElementById("stream").value;
//     let marks = parseInt(document.getElementById("marks").value);
//     let resultDiv = document.getElementById("result");
//     let college = "Unknown";

//     if (!stream || isNaN(marks)) {
//         resultDiv.innerHTML = `<h3>Please select a stream and enter marks.</h3>`;
//         return;
//     }

//     if (marks >= 90) {
//         if (stream === "science") college = "IITs, NITs, BITS, IIITs";
//         else if (stream === "commerce") college = "SRCC, LSR, Christ University";
//         else if (stream === "arts") college = "JNU, DU, Ashoka University";
//     } else if (marks >= 75) {
//         if (stream === "science") college = "State Engineering Colleges, Private Universities";
//         else if (stream === "commerce") college = "Amity, Symbiosis, NMIMS";
//         else if (stream === "arts") college = "Jamia Millia, Presidency University";
//     } else {
//         college = "Consider Private Colleges & Alternative Paths";
//     }

//     resultDiv.innerHTML = `<h3>Best Fit: ${college}</h3>`;
// }

// document.getElementById("college-form").addEventListener("submit", function(event) {
//     event.preventDefault();
//     updatePrediction();
// });
