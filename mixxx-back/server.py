from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from process_selection import process_selection

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안 필요시 특정 도메인으로 변경)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 'Pictures' 폴더를 FastAPI에서 정적 파일로 제공
app.mount("/uploaded_images", StaticFiles(directory="C:/Users/jrnee/Pictures"), name="uploaded_images")

@app.post("/submit-selection/")
async def submit_selection(
    gender: str = Form(...),
    category: str = Form(...),
    design: str = Form(...),
    color: str = Form(...),
    length: str = Form(...),
    fit: str = Form(...),
    selected_image_title: str = Form(...)
):
    """React에서 선택한 옵션과 업로드한 이미지 제목을 함께 받는 API"""

    print(f"📌 받은 데이터: {gender}, {category}, {design}, {color}, {length}, {fit}")
    print(f"📁 선택된 이미지 제목: {selected_image_title}")

    response = process_selection(gender, category, design, color, length, fit, selected_image_title)

    return response
