import React from "react";
import "./App.css";

//port : api 3100
//localhost port : 3000 (default)

function App() {
    function btn1_click() {
        window.location.href = "http://172.30.1.37:3100/?value=myvalue1";
    }
    function btn2_click() {
        window.location.href = "http://172.30.1.37:3100/?value=myvalue2";
    }
    return (
        <div className="outdiv">
            <div>
                <button className="btn1" onClick={btn1_click}>
                    btn1
                </button>
            </div>
            <div>
                <button className="btn2" onClick={btn2_click}>
                    btn2
                </button>
            </div>
        </div>
    );
}

export default App;
