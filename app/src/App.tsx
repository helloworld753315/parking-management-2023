import React from "react";
import "./App.css";
// import Info from './assets/svg/info.svg';
import ParkingInfo from "./components/ParkingInfo";

function App() {
  return (
    <div className="App">
      <h1 className="font-mono text-left text-3xl m-20">
        駐車場情報見れるくん
      </h1>
      <header className="App-header">  
        <ParkingInfo rate={0} />
      </header>
    </div>
  );
}

export default App;
