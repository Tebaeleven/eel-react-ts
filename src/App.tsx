import React from "react";
import logo from "./logo.svg";
import "./App.css";

export const eel = (window as any).eel;
eel.set_host("ws://localhost:8080");

function test() {
    eel.test();
}
function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.tsx</code> and save to reload.
                </p>
                <button onClick={test}>python関数を実行</button>
            </header>
        </div>
    );
}

export default App;
