import React from "react";
import {Route, Routes, HashRouter} from "react-router-dom";

import Landing from "./pages/Landing";
import Animated from "./pages/Animated";
import Training from "./pages/Training";
import DoodleNet from "./pages/DoodleNet";

export default function App() {
  return (
    <HashRouter>
        <Routes>
          <Route path="/" element={<Landing/>} />
          <Route path='/Animated' element={<Animated/>} />
          <Route path='/Training' element={<Training/>} />
          <Route path='/DoodleNet' element={<DoodleNet/>} />
        </Routes>
    </HashRouter>
  );
}
