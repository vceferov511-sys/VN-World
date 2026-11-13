const express = require("express");
const cors = require("cors");
const OpenAI = require("openai");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.post("/chat", async (req, res) => {
  try {
    const message = req.body.message;

    if (!message || typeof message !== "string") {
      return res.status(400).json({ error: "Mesaj boşdur" });
    }

    const response = await client.responses.create({
      model: "gpt-5-mini",
      input: message
    });

    res.json({ reply: response.output_text });
  } catch (error) {
    console.error("AI XƏTASI:", error);
    res.status(500).json({ error: "AI cavab verə bilmədi" });
  }
});

app.listen(process.env.PORT || 3000, "0.0.0.0", () => {
  console.log("V.N World AI server hazırdır: 3000");
});
