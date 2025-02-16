import { useState } from "react";
import { Button } from "../ui/button";
import "./Option.css";
import "./Option1.css";

export default function HoodieOptions() {
  const [image, setImage] = useState(null);
  const [showResults, setShowResults] = useState(false);
  const [results, setResults] = useState([]);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
  };
  const [selectedOptions, setSelectedOptions] = useState({
    design: "none",
    color: "none",
    length: "none",
    fit: "none",
  });

  const handleOptionSelect = (category, value) => {
    setSelectedOptions((prev) => ({
      ...prev,
      [category]: value,
    }));
  };
  const handleConfirm = async () => {
    const formData = new FormData();
  
    // 옵션 데이터 추가
    formData.append("gender", "men");
    formData.append("category", "coat");
    formData.append("design", selectedOptions.design);
    formData.append("color", selectedOptions.color);
    formData.append("length", selectedOptions.length);
    formData.append("fit", selectedOptions.fit);
  
    // 이미지 추가
    const fileInput = document.getElementById("fileUpload");
    if (fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name; // 파일 제목만 가져오기
        formData.append("selected_image_title", fileName);
    } else {
        alert("이미지를 선택하세요!");
        return;
    }
  
    console.log("보낼 데이터:", [...formData.entries()]);
  
    try {
      const response = await fetch("http://127.0.0.1:8000/submit-selection/", {
        method: "POST",
        body: formData, // multipart/form-data 형식으로 전송
      });
  
      if (response.ok) {
        const data = await response.json();
        

        setResults(data.recommendations);
        setShowResults(true); // 결과 페이지로 이동
      } else {
        alert("전송 실패");
      }
    } catch (error) {
      console.error("Error sending data:", error);
      alert("서버 오류 발생");
    }
  };

  if (showResults) {
    return <ResultsPage results={results} />;
  }

  return (
    <div className="options-container">
    {/* 왼쪽 - 이미지 업로드 */}
    <div className="upload-section">
      <h2 className="upload-title">MIXXX & MATCH</h2>
      <div className="upload-box">
          {image ? (
            <img src={image} alt="Uploaded" className="uploaded-image" />
          ) : (
            <div className="upload-placeholder">사진을 업로드 하세요</div>
          )}
        </div>
        <input type="file" accept="image/*" onChange={handleImageUpload} className="image-input" id="fileUpload" />
        <label htmlFor="fileUpload" className="upload-button">
          <strong>PHOTO</strong> UPLOAD
        </label>
      </div>
    {/* 오른쪽 - 옵션 선택 */}
    <div className="options-section">
      <h1 className="title">
        MEN’S <span className="highlight">PANTS</span>
      </h1>
      <h3 className="subtitle">Select <span className="bold">OPTIONS</span></h3>
      <div className="options-grid">
          {/* 옵션 선택 */}
          {[
            { category: "design", title: "DESIGN (PATTERN)", values: ["none", "Solid", "Graphic", "Stripe", "Check", "Camo"] },
            { category: "color", title: "COLORS", values: ["none", "Black", "White", "Gray", "Blue", "Red", "Navy", "Brown"] },
            { category: "length", title: "LENGTH", values: ["none", "Crop", "Regular", "Long"] },
            { category: "fit", title: "FIT", values: ["none", "Slim", "Regular", "Oversize"] },
          ].map(({ category, title, values }) => (
            <div key={category} className="option-group">
              <h3 className="option-title">{title}</h3>
              <div className="button-group">
                {values.map((value) => (
                  <button
                    key={value}
                    className={`option-button ${selectedOptions[category] === value ? "selected" : ""}`}
                    onClick={() => handleOptionSelect(category, value)}
                  >
                    {value === "none" ? "변경 없음" : value}
                  </button>
                ))}
              </div>
            </div>
          ))}
        </div>
      <div className="next-button-container">
        <Button onClick={handleConfirm} className="next-button-container">Next</Button>
      </div>
    </div>
  </div>
  );
}

// ✅ 결과 페이지 컴포넌트
function ResultsPage({ results }) {
  const [selectedIndex, setSelectedIndex] = useState(2); // 중앙 카드 초기값 설정

  const nextSlide = () => {
    setSelectedIndex((prev) => (prev < results.length - 1 ? prev + 1 : 0));
  };

  const prevSlide = () => {
    setSelectedIndex((prev) => (prev > 0 ? prev - 1 : results.length - 1));
  };

  return (
    <div className="results-container">
      <h1 className="results-title">
        MEN’S <span className="highlight">COAT</span> Selected OPTIONS
      </h1>

      <div className="carousel-container">
        <div className="results-carousel">
          {results.map((item, index) => {
            let position = "side-card";
            if (index === selectedIndex) position = "active";

            let imageUrl = item.image;

            // ✅ FastAPI에서 제공하는 URL이므로 변경 필요
            if (imageUrl && imageUrl.startsWith("C:/")) {
              imageUrl = `http://127.0.0.1:8000/uploaded_images/${imageUrl.split("/").pop()}`;
            }

            return (
              <div key={item.id} className={`result-card ${position}`}>
                <div className="card-content">
                <div className="card-header">
                    <div className="icons">
                      <span className="icon">♡</span>
                    </div>
                </div>
                  {imageUrl ? (
                    <img src={imageUrl} alt={item.description} className="result-image" />
                  ) : (
                    <p className="description">이미지를 찾을 수 없습니다.</p>
                  )}
                  <p className="description">{item.description}</p>
                 
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="retry-container">
        <button className="carousel-button" onClick={prevSlide}>{"<"}</button>
        <button className="retry-button" onClick={() => window.location.reload()}>Retry</button>
        <button className="carousel-button" onClick={nextSlide}>{">"}</button>
      </div>
    </div>
  );
}
