const express = require("express");
const app = express();
const port = 3100;

const mqtt = require("mqtt");
var client = mqtt.connect("mqtt://test.mosquitto.org");

app.get("/", (req, rsp) => {
    //rsp.json({ info: "test api by xzl" });
    console.log(req.query);
    console.log(req.query.value);
    console.log();

    if (req.query.value == "myvalue1") {
        client.publish("konkuk/emb/test", "ON", () => {
            console.log("mqtt:on success");
        });
    } else if (req.query.value == "myvalue2") {
        client.publish("konkuk/emb/test", "OFF", () => {
            console.log("mqtt:off success");
        });
    }
});

app.get("/h1/", (req, rsp) => {
    rsp.json({ info: "button Clicked" });
});

app.listen(port, function() {
    console.log("running as :", port);
});
