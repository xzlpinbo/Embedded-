const express = require("express");
const app = express();
const port = 3100;
const mqtt = require("mqtt");

//mqtt 연결 주소
var client = mqtt.connect("mqtt://test.mosquitto.org");

app.get("/", (req, rsp) => {
    //rsp.json({ info: "test api by xzl" }); //response

    console.log(req.query);
    console.log(req.query.value);
    console.log();

    //ON 버튼 누를 시 해당 topic에 "ON" 메시지 전송 
    if (req.query.value == "myvalue1") {
        client.publish("konkuk/emb/test", "ON", () => {
            console.log("mqtt:on success");
        });

    //OFF 버튼 누를 시 해당 topic에 "OFF" 메시지 전송 
    } else if (req.query.value == "myvalue2") {
        client.publish("konkuk/emb/test", "OFF", () => {
            console.log("mqtt:off success");
        });
    }
});

//port listener
app.listen(port, function() {
    console.log("running as :", port);
});
