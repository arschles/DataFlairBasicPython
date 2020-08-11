import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  const getTime = async () => {
    const sample = "Testfart";
    const response = await axios.post("http://localhost:5000/test", sample);
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
      <p>The current time is {currentTime}</p>
    </div>
  );
}

export default App;
