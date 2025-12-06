# 🔧 GitHub Desktop "Add repository" 버튼이 안 눌릴 때 해결방법

## 방법 1: "Create a repository here instead" 사용 ⭐

대화상자에 **"Create a repository here instead"** 옵션이 있다면:
1. 해당 옵션/버튼 클릭
2. GitHub Desktop이 자동으로 Git 저장소 생성
3. 그 다음 "Add repository" 버튼이 활성화됨

## 방법 2: 다른 경로로 다시 시도

1. GitHub Desktop에서 대화상자 **닫기** (X 버튼)
2. 다시 **"File" → "Add Local Repository"** 클릭
3. **"Choose..."** 버튼 클릭
4. `C:\Users\dldpw\Desktop\math` 폴더를 다시 선택

## 방법 3: GitHub Desktop에서 직접 저장소 생성

1. GitHub Desktop에서 **"File" → "New Repository"** 클릭
2. **"Local path"** 설정:
   - `C:\Users\dldpw\Desktop\math` 입력
   - 또는 "Choose..." 버튼으로 폴더 선택
3. **"Git ignore"**: None 선택
4. **"Initialize this repository with a README"**: 체크 해제
5. **"Create Repository"** 버튼 클릭

이렇게 하면 GitHub Desktop이 직접 Git 저장소를 생성하고 연결합니다!

## 방법 4: 웹 인터페이스로 직접 업로드 (가장 간단) ⭐⭐

GitHub Desktop이 계속 안 되면 웹에서 직접 업로드:

### 1단계: GitHub 저장소 생성
1. 브라우저에서 https://github.com/new 접속
2. Repository name: `math-website`
3. Description: "수학 공식 웹사이트"
4. **Public** 선택
5. **"Add a README file"** 체크 해제
6. **"Create repository"** 클릭

### 2단계: 파일 업로드
1. 생성된 저장소 페이지에서 **"uploading an existing file"** 클릭
2. 또는 **"Add file" → "Upload files"** 클릭
3. `C:\Users\dldpw\Desktop\math` 폴더의 모든 파일을 드래그 앤 드롭
   - `app.py`
   - `requirements.txt`
   - `Procfile`
   - `runtime.txt`
   - `templates` 폴더 (전체)
   - `static` 폴더 (전체)
   - `data` 폴더 (전체)
   - 기타 모든 파일
4. 하단에 커밋 메시지 입력: `Initial commit: 수학 공식 웹사이트`
5. **"Commit changes"** 버튼 클릭

### 완료!
- 업로드 완료!
- https://github.com/dldpwls020527/math-website 에서 확인

---

## 추천 순서

1. **먼저 방법 3 시도** (GitHub Desktop에서 New Repository)
2. 안 되면 **방법 4 사용** (웹에서 직접 업로드) - 가장 확실함!

---

## 다음 단계: Railway 배포

GitHub 업로드 완료 후:
1. https://railway.app 접속
2. "New Project" → "Deploy from GitHub repo"
3. `math-website` 저장소 선택
4. 자동 배포!

