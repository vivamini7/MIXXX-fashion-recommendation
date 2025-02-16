import { Routes, Route, useNavigate } from "react-router-dom";
import WomenHoodieOptions from "../Options/WomenHoodieOptions";
import WomenJeanOptions from "../Options/WomenJeanOptions";
import WomenCoatOptions from "../Options/WomenCoatOptions";
import "./CategorySelect.css"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<WomenCategorySelect />} />
      <Route path="/hoodie-options/women" element={<WomenHoodieOptions />} />
      <Route path="/jean-options/women" element={<WomenJeanOptions />} />
      <Route path="/coat-options/women" element={<WomenCoatOptions />} />
    </Routes>
  );
}

function WomenCategorySelect() {
  const navigate = useNavigate();

  return (
    <div className="category-container">
      <div className="header">
        <div className="quote-box">
          <img src="/select.png" alt="Select" className="select-image" />
        </div>
      </div>
      <div className="category-grid">
        <div className="category-card" onClick={() => navigate("/hoodie-options/women")}>
          <img src="/hoodie.png" alt="Hoodie" className="category-image" />
        </div>
        <div className="category-card" onClick={() => navigate("/jean-options/women")}>
          <img src="/pants.png" alt="Pants" className="category-image" />
        </div>
        <div className="category-card" onClick={() => navigate("/coat-options/women")}>
          <img src="/coat.png" alt="Coat" className="category-image" />
        </div>
      </div>
    </div>
  );
}
