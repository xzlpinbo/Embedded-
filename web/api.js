const express = require("express");
const app = express();
const port = 3100;

app.get("/", (req, rsp) => {
    rsp.json({ info: "test api by xzl" });
    console.log(req.query);
    console.log(req.query.value);
});

app.get("/h1/", (req, rsp) => {
    rsp.json({ info: "test api by h1" });
});

app.listen(port, function() {
    console.log("running as :", port);
});
