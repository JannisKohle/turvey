const express = require("express");
const app = express();

const surveysRouter = require("./routes/surveysRoutes");

app.use(express.json());

app.use("/surveys", surveysRouter);

app.listen(3000, () => console.log("Listening on port 3000"));
