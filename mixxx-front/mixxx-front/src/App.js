import { Routes, Route, useNavigate } from "react-router-dom";
import { FaBars, FaSearch, FaCamera } from "react-icons/fa";
import "./App.css";
import image from "./1.png";
import MenWomenSelect from "./components/MenWomenSelect";
import MenCategorySelect from "./components/select-category/MenCategorySelect";
import WomenCategorySelect from "./components/select-category/WomenCategorySelect";
import MenHoodieOptions from "./components/Options/MenHoodieOptions";
import MenJeanOptions from "./components/Options/MenJeanOptions";
import MenCoatOptions from "./components/Options/MenCoatOptions";
import WomenHoodieOptions from "./components/Options/WomenHoodieOptions";
import WomenJeanOptions from "./components/Options/WomenJeanOptions";
import WomenCoatOptions from "./components/Options/WomenCoatOptions";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/select-gender" element={<MenWomenSelect />} />
      <Route path="/select-category/men/*" element={<MenCategorySelect />} />
      <Route path="/select-category/women/*" element={<WomenCategorySelect />} />
      <Route path="/hoodie-options/men/*" element={<MenHoodieOptions />} />
      <Route path="/jean-options/men" element={<MenJeanOptions />} />
      <Route path="/coat-options/men" element={<MenCoatOptions />} />
      <Route path="/hoodie-options/women/*" element={<WomenHoodieOptions />} />
      <Route path="/jean-options/women" element={<WomenJeanOptions />} />
      <Route path="/coat-options/women" element={<WomenCoatOptions />} />
    </Routes>
  );
}

function Home() {
  const navigate = useNavigate();

  return (
    <div className="app-container">
      {/* Navbar */}
      <nav className="navbar">
        <div className="nav-left">
          <FaBars className="icon1" />
        </div>
        <h1 className="logo">MIXXX</h1>
        <div className="nav-right">
          <FaSearch className="icon2" />
          <FaCamera className="icon3" />
        </div>
      </nav>

      {/* First Section */}
      <section className="hero" style={{ backgroundImage: `url(${image})` }}>
        <div className="hero-overlay">
          <div className="hero-content">
            <span className="hero-tagline">
              <svg className="hero-icon" xmlns="http://www.w3.org/2000/svg" width="65" height="62" viewBox="0 0 65 62" fill="none">
                <path d="M32.5 0L39.6916 17.5664L57.9095 12.2366L48.6594 28.8117L64.1852 39.7319L45.4589 42.8343L46.6012 61.7815L32.5 49.075L18.3988 61.7815L19.5411 42.8343L0.814842 39.7319L16.3406 28.8117L7.09048 12.2366L25.3084 17.5664L32.5 0Z" fill="#EE5C21"/>
              </svg>
              MIXXX <span className="hero-tagline-light">IS What ?</span>
            </span>
          </div>
          <button className="shop-button">SHOP NOW</button>
        </div>
      </section>

      {/* Second Section - Find */}
      <section className="find-section">
        <h2 className="find-text">
          <span className="find-bold1">Find</span> Yours,<nobr />
          <br />
          <span className="find-bold2">Find</span> My Own Fit
        </h2>
        <svg className="find-arrow" xmlns="http://www.w3.org/2000/svg" width="134" height="134" viewBox="0 0 134 134" fill="none">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M2.34315 2.34315C5.46734 -0.781049 10.5327 -0.781049 13.6569 2.34315L117.792 106.478V8C117.792 3.58172 121.373 1.19209e-07 125.792 1.19209e-07C130.21 1.19209e-07 133.792 3.58172 133.792 8V125.792C133.792 130.21 130.21 133.792 125.792 133.792H8C3.58172 133.792 1.19209e-07 130.21 1.19209e-07 125.792C1.19209e-07 121.373 3.58172 117.792 8 117.792H106.478L2.34315 13.6569C-0.781049 10.5327 -0.781049 5.46734 2.34315 2.34315Z" fill="black"/>
        </svg>
      </section>

      {/* Third Section - Product Showcase */}
      <section className="product-section" style={{ marginBottom: "200px" }}>
        <div className="product-container">
          {['2.png', '3.png', '4.png', '5.png'].map((src, index) => (
            <div key={index} className="product-card">
              <img src={`/${src}`} alt={`Product ${index + 1}`} className="product-image" />
            </div>
          ))}
        </div>
      </section>

      {/* Fourth Section - Mix & Match */}
      <section className="mix-match-section">
        <div className="mix-match-container">
          <div className="mix-match-left">
            <img src="/6.png" alt="Mix & Match Main" className="mix-match-main" />
            <div className="mix-match-text">
              <h1 className="mix-title">MIXXX<span className="mix-subtitle">_내가 원하는 옷이 나올때까지 서치해주는 브랜드</span></h1>
            </div>
          </div>
          <div className="mix-match-right">
            <img src="/7.png" alt="Mix & Match Info" className="mix-match-card1" />
            <img src="/8.png" alt="Mix & Match Description" className="mix-match-card2" />
          </div>
        </div>
      </section>
      {/* Fifth Section - Repeating Text */}
      <section className="repeat-text-section">
        <div className="repeat-text-container">
          {Array(5).fill(null).map((_, index) => (
            <div key={index} className="repeat-text-wrapper">
              <span className="repeat-text">MIXXX</span>
              <span className="repeat-space"> </span>
              <span className="repeat-text">MATCH</span>
            </div>
          ))}
        </div>
      </section>
      {/* Sixth Section - Brand Statement */}
      <section className="brand-statement-section">
        <div className="brand-statement-container">
          <img src="/9.png" alt="Brand Model" className="brand-image" />
          <img src="/10.png" alt="Brand Slogan" className="brand-slogan" />
        </div>
      </section>
      {/* Seventh Section - Repeating Buttons */}
      <section className="repeating-buttons-section">
        <div className="repeating-buttons-container">
          {Array(10).fill(null).map((_, index) => (
            <div key={index} className="button-wrapper">
              <img src="/11.png" alt="Fashion Style Search" className="button-image" />
            </div>
          ))}
        </div>
      </section>
      <section className="how-it-works-section">
        <h2 className="how-it-works-title">
          <span className="how-bold">How</span> it use?
        </h2>
        {/* HoodieOptions로 이동하는 버튼 */}
        <button className="navigate-button" onClick={() => navigate("/select-gender")}>
          Next
        </button>
      </section>
    </div>
  );
} 