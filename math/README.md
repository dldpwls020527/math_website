# 📐 수학 공식 웹사이트

중고등학생을 위한 수학 공식 학습 웹사이트입니다.

## 🚀 빠른 시작

### 1. 가상환경 활성화
```bash
conda activate solar
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 웹사이트 실행
```bash
python app.py
```

### 4. 브라우저에서 접속
웹 브라우저에서 `http://localhost:5000` 또는 `http://127.0.0.1:5000`으로 접속하세요.

## 📁 프로젝트 구조

```
math_program/
├── app.py                    # Flask 메인 애플리케이션
├── requirements.txt          # Python 패키지 목록
├── templates/                # HTML 템플릿
│   ├── index.html           # 메인 페이지
│   ├── formulas.html        # 공식 목록
│   └── formula_detail.html  # 공식 상세
├── static/                   # 정적 파일
│   ├── css/
│   │   └── style.css        # 스타일시트
│   ├── js/
│   │   └── main.js          # JavaScript
│   └── images/              # 이미지 파일 (선택사항)
└── data/                     # 수학 공식 데이터
    └── formulas.json         # 공식 데이터 (JSON)
```

## ✨ 주요 기능

1. **카테고리별 공식 분류**
   - 중학교 수학
   - 수학 I
   - 수학 II
   - 미적분
   - 확률과 통계

2. **수학 공식 표시**
   - MathJax를 사용한 LaTeX 수식 렌더링
   - 예: $E = mc^2$, $\int_{a}^{b} f(x)dx$

3. **다양한 미디어 지원**
   - 📷 **이미지**: 공식 설명을 위한 시각적 자료
   - 🎥 **동영상**: YouTube, Vimeo 등 동영상 설명
   - 💻 **코드**: Python 등 프로그래밍 코드 예제

4. **검색 기능**
   - 공식 이름, 설명으로 실시간 검색 (단순 텍스트 매칭)
   - 검색 결과에 미디어 타입 표시 (이미지/동영상/코드)

5. **반응형 디자인**
   - 모바일, 태블릿, 데스크톱 지원
   - 현대적이고 깔끔한 UI

## 🛠 기술 스택

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **수식 렌더링**: MathJax 3.0
- **데이터 형식**: JSON

## 📝 수학 공식 추가하기

`data/formulas.json` 파일을 편집하여 새로운 공식을 추가할 수 있습니다.

### 기본 구조
```json
{
  "id": 13,
  "name": "공식 이름",
  "formula": "LaTeX 수식",
  "description": "공식 설명",
  "example": "예제 (선택사항)",
  "image": "이미지 URL 또는 경로 (선택사항)",
  "video": "YouTube/Vimeo URL 또는 동영상 경로 (선택사항)",
  "code": {
    "language": "python",
    "content": "코드 내용",
    "description": "코드 설명 (선택사항)"
  }
}
```

### 이미지 추가 방법
- 외부 URL 사용: `"image": "https://example.com/image.png"`
- 로컬 파일 사용: `"image": "/static/images/formula1.png"` (파일은 `static/images/` 폴더에 저장)

### 동영상 추가 방법
- YouTube: `"video": "https://www.youtube.com/watch?v=VIDEO_ID"`
- Vimeo: `"video": "https://vimeo.com/VIDEO_ID"`
- 로컬 동영상: `"video": "/static/videos/formula1.mp4"`

### 코드 예제 추가 방법
```json
"code": {
  "language": "python",
  "content": "def example():\n    return 'Hello'",
  "description": "코드 설명"
}
```

## 🔧 개발 팁

- 수식은 LaTeX 형식으로 작성합니다
- 인라인 수식: `$수식$` 또는 `\(수식\)`
- 블록 수식: `$$수식$$` 또는 `\[수식\]`
- MathJax는 자동으로 수식을 렌더링합니다

## 📚 참고 자료

- [Flask 공식 문서](https://flask.palletsprojects.com/)
- [MathJax 문서](https://www.mathjax.org/)
- [LaTeX 수식 작성 가이드](https://www.overleaf.com/learn/latex/Mathematical_expressions)

