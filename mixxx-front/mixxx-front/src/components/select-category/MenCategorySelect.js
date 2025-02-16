import { Routes, Route, useNavigate } from "react-router-dom";
import MenHoodieOptions from "../Options/MenHoodieOptions";
import MenJeanOptions from "../Options/MenJeanOptions";
import MenCoatOptions from "../Options/MenCoatOptions";
import "./CategorySelect.css"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<MenCategorySelect />} />
      <Route path="/hoodie-options/men" element={<MenHoodieOptions />} />
      <Route path="/jean-options/men" element={<MenJeanOptions />} />
      <Route path="/coat-options/men" element={<MenCoatOptions />} />
    </Routes>
  );
}

function MenCategorySelect() {
  const navigate = useNavigate();

  return (
    <div className="category-container">
      <div className="header">
        <div className="quote-box">
          <img src="/select.png" alt="Select" className="select-image" />
        </div>
      </div>
      <div className="category-grid">
        <div className="category-card" onClick={() => navigate("/hoodie-options/men")}>
          <img src="/hoodie.png" alt="Hoodie" className="category-image" />
        </div>
        <div className="category-card" onClick={() => navigate("/jean-options/men")}>
          <img src="/pants.png" alt="Pants" className="category-image" />
        </div>
        <div className="category-card" onClick={() => navigate("/coat-options/men")}>
          <img src="/coat.png" alt="Coat" className="category-image" />
        </div>
      </div>
    </div>
  );
}
