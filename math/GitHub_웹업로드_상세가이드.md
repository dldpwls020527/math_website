# 📤 GitHub 웹에서 파일 업로드 상세 가이드

## 방법 1: 저장소 생성 직후 업로드

### 1단계: 새 저장소 생성
1. https://github.com/new 접속
2. Repository name: `math-website`
3. **Public** 선택
4. **"Add a README file"** 체크 해제 ⚠️
5. **"Create repository"** 클릭

### 2단계: 파일 업로드
저장소를 만들면 바로 다음 화면이 나타납니다:

```
┌─────────────────────────────────────┐
│ Quick setup                         │
│                                     │
│ …or create a new repository on ...  │
│                                     │
│ …or push an existing repository ... │
│                                     │
│                                     │
│ ⬇️ 아래쪽에 ⬇️                        │
│                                     │
│ …or upload an existing file         │  ← 이 링크 클릭!
└─────────────────────────────────────┘
```

**"uploading an existing file"** 링크를 클릭하세요!
- 화면 하단에 있을 수 있습니다
- 스크롤 내려서 찾으세요

---

## 방법 2: "Add file" 버튼 사용 (더 확실함) ⭐

저장소가 이미 만들어져 있거나, 링크를 찾을 수 없다면:

### 1단계: 저장소 페이지로 이동
- https://github.com/dldpwls020527/math-website 접속
- 또는 저장소 목록에서 `math-website` 클릭

### 2단계: 파일 업로드
1. 저장소 페이지 우측 상단에 **"Add file"** 버튼 확인
2. **"Add file"** 버튼 클릭
3. 드롭다운 메뉴에서 **"Upload files"** 선택

### 화면 예시:
```
┌─────────────────────────────────────────┐
│ [Code] [Issues] [Pull requests] ...     │
│                                         │
│ [<> Code] ▼ [Add file ▼]  [Code ▼]     │
│              └─ New file               │
│              └─ Upload files  ← 여기!  │
│                                         │
└─────────────────────────────────────────┘
```

---

## 방법 3: 직접 URL로 접속

저장소를 만든 직후에는 다음 URL로 바로 업로드 페이지로 이동할 수 있습니다:
```
https://github.com/dldpwls020527/math-website/upload
```

---

## 📋 파일 업로드 단계 (공통)

어떤 방법을 사용하든, 업로드 화면에서는:

### 1단계: 파일 드래그 앤 드롭
1. 파일 탐색기에서 `C:\Users\dldpw\Desktop\math` 폴더 열기
2. **모든 파일과 폴더 선택**:
   - Ctrl + A (전체 선택)
   - 또는 개별 선택:
     - `app.py`
     - `requirements.txt`
     - `Procfile`
     - `runtime.txt`
     - `templates` 폴더 (전체)
     - `static` 폴더 (전체)
     - `data` 폴더 (전체)
     - 기타 모든 파일
3. 선택한 파일들을 브라우저로 **드래그 앤 드롭**

### 2단계: 커밋
1. 화면 하단으로 스크롤
2. "Commit changes" 섹션에서:
   - 첫 번째 필드 (커밋 메시지): `Initial commit: 수학 공식 웹사이트`
   - 두 번째 필드 (설명, 선택사항): 비워도 됨
3. **"Commit changes"** (또는 "Commit new files") 버튼 클릭

### 3단계: 완료! ✅
- 업로드 완료!
- 저장소 페이지에서 모든 파일이 보이는지 확인

---

## 🎯 가장 확실한 방법

1. https://github.com/new 에서 저장소 생성
2. 저장소 생성 후 화면에서 **스크롤을 내려서** "uploading an existing file" 찾기
3. 또는 저장소 페이지에서 **"Add file" → "Upload files"** 클릭
4. 파일 드래그 앤 드롭
5. "Commit changes" 클릭

---

## 📸 화면에서 찾는 팁

### "Add file" 버튼 위치:
```
GitHub 저장소 페이지
├── 상단 메뉴: Code | Issues | Pull requests | ...
├── 파일 목록 영역
└── 우측 상단: [Add file ▼] ← 여기!
    ├── New file
    └── Upload files ← 클릭!
```

### "uploading an existing file" 링크 위치:
```
저장소 생성 직후 화면
├── "Quick setup" 제목
├── "…or create a new repository on ..."
├── "…or push an existing repository ..."
└── 스크롤 ↓
    └── "…or upload an existing file" ← 여기!
```

---

## 🆘 여전히 못 찾겠다면

**직접 URL 사용:**
1. 저장소 생성: https://github.com/new
2. 업로드 페이지: https://github.com/dldpwls020527/math-website/upload

또는 저장소 페이지에서 주소창에 `/upload` 추가:
```
https://github.com/dldpwls020527/math-website/upload
```

