import os

def process_selection(gender, category, design, color, length, fit, selected_image_title):
    """
    사용자가 선택한 의류 옵션과 선택한 이미지 제목을 처리하는 함수
    """
    
    # ✅ 로컬 디렉토리에서 이미지 파일 찾기
    image_directory = "C:/Users/jrnee/Pictures/"  # 사용자 사진이 저장된 폴더
    image_path = os.path.join(image_directory, selected_image_title)
    
    # ✅ 이미지가 존재하는지 확인
    if os.path.exists(image_path):
        found_image = image_path  # 실제 경로 반환
    else:
        found_image = None  # 이미지가 존재하지 않을 경우
    
    # ✅ 추천 리스트에서 id 1번의 이미지를 강제로 설정 (테스트용)
    if selected_image_title=="2b515bf7baac4c1fb29d86f1972dad4c.jpg":
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/데일리 발마칸 코트 [블랙].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/[드로우핏X노이어] 핸드메이드 캐시미어 싱글 코트.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/Japanese mohair fabric oversized coat_Black.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/데일리 발마칸 코트 [네이비].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/데일리 발마칸 코트 [블랙].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title=="3c9be7e7832449a59ccac815dca6eaf2.jpg":
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/다크 그레이 오버핏 버진울 체크 발마칸 코트 (TNCO3F107G2).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/체크 재킷 - 다크 네이비 _ WOAPVM02865IAK.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/다크 그레이 오버핏 버진울 체크 발마칸 코트 (TNCO3F107G2).jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/WYATT CHECK BALMACAAN COAT BROWN.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/[프리미엄] MANTECO 헤링본 오버사이즈 발마칸 코트 [다크 그레이].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title=="2023021515234800000037058.jpg":
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/해링본 하프 코트 (헤링본).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/체크 패딩 맥코트 _ ZSB13CT002.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/[프리미엄] MANTECO 헤링본 오버사이즈 발마칸 코트 [다크 그레이].jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/다크 그레이 오버핏 버진울 체크 발마칸 코트 (TNCO3F107G2).jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/오버사이즈 발마칸 맥시 코트 [HERRINGBONE].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "00e200057df241cf9067948d1e44fb95.jpg":
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/위드유 후드집업 6 Color [ULZH_5006].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/[Mmlg] CHECK PATTERN HOOD ZIPUP (EVERY BLACK).jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/KHZB0124 투탕카멘 기모 후드 집업 블랙.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/[2-WAY] CP STAR 피그먼트 후드 집업 스모크블랙.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/Floral Work Jacket Black.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "5fe4dd7ec3a54e91916835059a049b9e.jpg":
    # candidate: 5fe4dd7ec3a54e91916835059a049b9e
    # captions: "has no graphic and pattern and is regular fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/ERBE OVERSIZED ZIP HOODIE [POLAR NIGHT].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/[30% 적립금] 더블니트 풀집 후디 - 네이비.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/[프렌치테리] 루즈핏 2-WAY 후드집업_SPMZE49C01.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/ERBE OVERSIZED ZIP HOODIE [BROWN].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/Reversible Hoodie Zip-Up Check Blue.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "3b8a1d8d41d14ea4ab20c3e7b50ad424.jpg":
    # candidate: 3b8a1d8d41d14ea4ab20c3e7b50ad424
    # captions: "has a checkered pattern, is blue, and is oversized fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/Reversible Hoodie Zip-Up Check Blue.jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/CHECK PATCHWORK HOOD ZIP-UP [BROWN].jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/디바이드 래글런 후드 집 업-네이비.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/테오 패디드 후드 집업 스카이 블루.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/SWING LOGO 후드집업(STJSTD-0102).jpg", "description": "추천 상품 5"},
        ]
    
    elif selected_image_title == "96f0a4afde61417bbdb0c4543f32395c.jpg":
        # candidate: 96f0a4afde61417bbdb0c4543f32395c
        # captions: "has a washed effect, and is light blue, and is loose fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/TD5-DN02 스트레이트 데님 팬츠-연청.jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/와이드 테이퍼드 데님 팬츠 (라이트 블루).jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/TD5-DN02 스트레이트 데님 팬츠-연청.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/라운드 포켓 벌룬핏 워싱 데님 팬츠 (LIGHT BLUE).jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/논페이드 와이드 데님팬츠[라이트 블루].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "f113c84ca36243a0b28c4044365096ae.jpg":
        # candidate: f113c84ca36243a0b28c4044365096ae
        # captions: "is black and wide fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/블랙 커브드 데님 팬츠  블랙.jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/빈티지 워시드 더블 니 데님 팬츠 (블랙).jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/프린지 데님 와이드 팬츠(BLACK).jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/컴포트 와이드 데님 팬츠 (블랙).jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/Banding One Tuck Wide Denim Pants - Black.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "518bc8a428c745698894e525b3a58050.jpg":
        # candidate: 518bc8a428c745698894e525b3a58050
        # captions: "has a regular design, and is bootcut fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/부츠컷 생지 데님 팬츠 [NV].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/세미와이드 생지 데님 팬츠 INDIGO.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/프레디 세미 와이드 원턱 생지 데님 [RAW BLACK].jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/데님 커브드 와이드 팬츠 7COLOR COOSPT214.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/Selvedge Relaxed Denim Pants Dark Indigo.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "99e697950e69444b97d6f4b8f6057cc7.jpg":
        # candidate: 99e697950e69444b97d6f4b8f6057cc7
        # captions: "is cropped length and is black"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/[무료반품] CHROME B BLACK LINE CROP ZIP-UP HOODIE [BLACK].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/(W)피그먼트 다잉 디스 크롭 후드 집업_워시드그레이.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/CUT OUT DETAIL CROP HOODY ZIP UP IN CHARCOAL.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/우먼즈 볼륨 크롭 후디드 스웨트 집업 [블랙].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/[무료반품] 스포츠웨어 피닉스 플리스 루즈 크롭 풀집 후디 W - 블랙_세일 _ HJ0941-010.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "6490f0b213dc40f688b5b28710869909.jpg":
        # candidate: 6490f0b213dc40f688b5b28710869909
        # captions: "has no graphic and pattern, is navy, and is regular fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/G CLASSIC KNIT ZIP UP (NAVY).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/EVERYDAY AECA CLOVER ZIP UP HOODIE-NAVY.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/컬리지 후드집업 Ver2 네이비.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/더티워싱 스터드 후드 집업 [네이비].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/TCM logo hooded zip-up (navy).jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "7e4fe0f22e9d46a5b1fbf882550bb7a1.jpg":
        # candidate: 7e4fe0f22e9d46a5b1fbf882550bb7a1
        # captions: "has no graphic and pattern"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/오브에 스타리본 후드 집업 (3color).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/G CLASSIC KNIT ZIP UP (NAVY).jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/G CLASSIC WASHED BOXY ZIP UP (WHITE).jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/[SET] 벨루어 트레이닝 후드집업 스커트 셋업 [4color].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/우먼즈 리브드 슬림 니트 후디드 집업 [웜 그레이].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "2022022114572200000099637.jpg":
        # candidate: 2022022114572200000099637
        # captions: "is beige and long length"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/알파카 & 울 헤링본 싱글 브레스티드 코트 (ivory).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/handmade belted single coat-beige.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/후드 머플러 핸드메이드 롱코트 버터.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/벨티드 핸드메이드 롱 코트_BUTTER.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/우먼즈 캐시미어 블렌드 발마칸 로브 코트 [버터].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "2021021709481300000067158.jpg":
        # candidate: 2021021709481300000067158
        # captions: "is navy, and is regular fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/울 숏 코트 [네이비].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/더블 코쿤 코트 - 블랙 _ 244WRO0138FB0006001.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/[W]더플하프코트 - 2color MYCA7213.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/808 캐시미어 블랜드 코트 네이비.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/울 발마칸 코트 MCO102 [NAVY].jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "633906424c834b67b76bb44309a9cd13.jpg":
        # candidate: 633906424c834b67b76bb44309a9cd13
        # captions: "has a checkered pattern, is brown"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/하운드 투스 체크 싱글 코트 - 브라운.jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/MTR 싱글코트 (다크브라운).jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/alpaca blend balmacaan coat - brown.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/CHECK LONG HANDMADE COAT - Beige.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/슬림 싱글 코트_RMJHE4VR13.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "5d1b36e2bb074c5c9f4c3a363428d2b7.jpg":
        # candidate: 5d1b36e2bb074c5c9f4c3a363428d2b7
        # captions: "has a ripped design, and is blue"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/Creepy Patch Denim Pants(BLUE).jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/플러피 커팅 데님 팬츠[인디고].jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/플레어 워시드 데님 팬츠 블루.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/그레이스 워싱 부츠컷 팬츠 [D_DENIM].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/T.S DENIM PANTS - WASHED NAVY.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "3b976ca2e2c6452d97eae2b4beb9a0fa.jpg":
        # candidate: 3b976ca2e2c6452d97eae2b4beb9a0fa
        # captions: "has a washed effect, and is light blue, and is wide fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/87-STAN161 빈티지 딥 캣워싱 와이드 데님팬츠 샌드블루.jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/사선 절개 와이드 데님 팬츠 - LIGHT BLUE.jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/맥스와이드 데님 소닉 블루.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/Loose Flared Wide Jeans DCPT029Blue.jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/커브드 스티치 와이드 데님 팬츠 [LBLUE]_SEPT038LBLUE.jpg", "description": "추천 상품 5"},
        ]
    elif selected_image_title == "fba7dd8769b04472bed77532e5ad17cb.jpg":
        # candidate: fba7dd8769b04472bed77532e5ad17cb
        # captions: "and is black, and is bootcut fit"
        recommendations = [
            {"id": 1, "image": "C:/Users/jrnee/Pictures/rivet boots cut pants [black].jpg", "description": "추천 상품 1"},
            {"id": 2, "image": "C:/Users/jrnee/Pictures/부츠컷 생지 데님 팬츠 [NV].jpg", "description": "추천 상품 2"},
            {"id": 3, "image": "C:/Users/jrnee/Pictures/[무료반품] Shirring bootscut pants CHARCOAL.jpg", "description": "추천 상품 3"},
            {"id": 4, "image": "C:/Users/jrnee/Pictures/프레디 세미 와이드 원턱 생지 데님 [RAW BLACK].jpg", "description": "추천 상품 4"},
            {"id": 5, "image": "C:/Users/jrnee/Pictures/[무료반품] Pocket denim wide pants BLACK.jpg", "description": "추천 상품 5"},
        ]



    return {
        "message": "✅ Selection processed successfully!",
        "selected_image_title": selected_image_title,
        "image_path": found_image,  # 로컬에서 찾은 이미지 경로 반환
        "data": {
            "gender": gender,
            "category": category,
            "design": design,
            "color": color,
            "length": length,
            "fit": fit,
        },
        "recommendations": recommendations,
    }
