import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

import { ClockInput } from "./components/ClockInput";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  const getTime = async () => {
    const config = {
      headers: {
        "content-type": "application/json",
      },
    };

    const body = JSON.stringify({
      time: "20:48:30",
    });

    const response = await axios.post(
      "http://localhost:5000/time",
      body,
      config
    );
    setCurrentTime(response.data.time);
  };

  useEffect(() => {
    getTime();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <ClockInput />
      <p>The current time is {currentTime}</p>
    </div>
  );
}

export default App;
