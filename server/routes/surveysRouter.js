const express = require("express");
const router = express.Router();

router.use(express.json());

router.get("/:surveyId", (req, res) => {
  res.send();
});

router.post("/:surveyId", (req, res) => {
    res.send();
});

router.delete("/:survey", (req, res) => {
    res.send();
});

module.exports = router;
