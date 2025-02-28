import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./components/home/Home";
import Main from "./components/home/Main";
import Reflect from "./Resume/Reflect";
import Review from "./components/review/Review";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/resume" element={<Main />} />
      <Route path="/resume/download" element={<Reflect />} />
      <Route path="/review" element={<Review />} />
    </Routes>
  );
}

export default App;
