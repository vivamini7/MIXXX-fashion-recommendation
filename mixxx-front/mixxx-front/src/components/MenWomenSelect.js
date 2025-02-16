import { Routes, Route, useNavigate } from "react-router-dom";
import MenCategorySelect from "./select-category/MenCategorySelect";
import WomenCategorySelect from "./select-category/WomenCategorySelect";
import "./MenWomenSelect.css"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<MenWomenSelect />} />
      <Route path="/select-category/men" element={<MenCategorySelect />} />
      <Route path="/select-category/women" element={<WomenCategorySelect />} />
    </Routes>
  );
}

function MenWomenSelect() {
  const navigate = useNavigate();

  return (
    <div className="select-container">
      <div
        className="option female"
        onClick={() => navigate("/select-category/women")}
      >
      </div>
      <div
        className="option male"
        onClick={() => navigate("/select-category/men")}
      >
      </div>
      <div className="mixxx">MIXXX</div>
    </div>
  );
}