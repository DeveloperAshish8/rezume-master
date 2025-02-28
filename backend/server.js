const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const { PythonShell } = require("python-shell");

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.post("/predict", (req, res) => {
  const { resume_text } = req.body;

  if (!resume_text) {
    console.log("❌ No resume_text received in request body");
    return res.status(400).json({ error: "resume_text is required" });
  }

  console.log("✅ Received resume_text:", resume_text);

  let pyshell = new PythonShell("./scripts/predict.py", {
    mode: "json",
    pythonPath: "python",
  });

  console.log("✅ Sending data to Python script...");

  // ✅ Send JSON data correctly
  pyshell.send({ resume_text });

  pyshell.on("message", (message) => {
    console.log("✅ Python response received:", message);
    res.json(message);
  });

  pyshell.on("stderr", (stderr) => {
    console.error("❌ Python stderr:", stderr);
  });

  pyshell.end((err) => {
    if (err) {
      console.error("❌ PythonShell error:", err);
      res.status(500).json({ error: "Error processing request" });
    } else {
      console.log("✅ Python script execution completed.");
    }
  });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
