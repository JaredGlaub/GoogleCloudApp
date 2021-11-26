import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Landing from "./pages/Landing";
import How from "./pages/How";
import Features from "./pages/Features";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />}>
          <Route index element={<Features />} />
          <Route index element={<How />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}