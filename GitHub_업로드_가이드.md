# 📤 GitHub에 코드 업로드하기

GitHub 사용자명: **dldpwls020527**

## 방법 1: GitHub Desktop 사용 (가장 쉬움) ⭐ 추천

### 1단계: GitHub Desktop 설치
1. https://desktop.github.com/ 접속
2. "Download for Windows" 클릭
3. 설치 파일 실행 및 설치

### 2단계: GitHub Desktop에서 로그인
1. GitHub Desktop 실행
2. "Sign in to GitHub.com" 클릭
3. GitHub 계정으로 로그인 (dldpwls020527)

### 3단계: GitHub 저장소 생성 및 연결
1. GitHub Desktop에서 "File" → "Add Local Repository" 클릭
2. "Choose..." 클릭
3. `C:\Users\dldpw\Desktop\math` 폴더 선택
4. "Add repository" 클릭

### 4단계: GitHub 저장소 생성 (처음 한 번만)
1. GitHub Desktop 상단 "Publish repository" 클릭
   - 또는 "Repository" → "Publish repository" 클릭
2. Repository name: `math-website` (또는 원하는 이름)
3. "Keep this code private" 체크 해제 (Public으로 설정)
4. "Publish Repository" 클릭

### 5단계: 업로드 완료!
- GitHub 웹사이트에서 확인: https://github.com/dldpwls020527/math-website

---

## 방법 2: Git 명령어 사용

### 1단계: Git 설치
1. https://git-scm.com/download/win 접속
2. 다운로드 및 설치 (기본 설정 그대로 진행)
3. PowerShell 재시작

### 2단계: GitHub 저장소 웹에서 생성
1. https://github.com/new 접속
2. Repository name: `math-website`
3. Description: (선택사항) "수학 공식 웹사이트"
4. Public 선택
5. "Add a README file" 체크하지 않기
6. "Create repository" 클릭

### 3단계: 명령어로 업로드
PowerShell에서 실행:

```powershell
# 프로젝트 폴더로 이동
cd C:\Users\dldpw\Desktop\math

# Git 초기화 (처음 한 번만)
git init

# 모든 파일 추가
git add .

# 커밋
git commit -m "Initial commit: 수학 공식 웹사이트"

# GitHub 저장소 연결 (math-website는 위에서 만든 저장소 이름)
git remote add origin https://github.com/dldpwls020527/math-website.git

# 브랜치 이름을 main으로 설정
git branch -M main

# GitHub에 업로드
git push -u origin main
```

**로그인 요구 시:**
- 사용자명: dldpwls020527
- 비밀번호: GitHub Personal Access Token 사용 필요
  - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
  - 권한: repo 체크
  - 생성된 토큰을 비밀번호 대신 입력

---

## 방법 3: 웹 인터페이스 사용 (간단하지만 제한적)

1. https://github.com/new 접속
2. Repository name: `math-website`
3. "Add a README file" 체크
4. "Create repository" 클릭
5. "uploading an existing file" 클릭
6. 모든 파일 드래그 앤 드롭
7. "Commit changes" 클릭

---

## ✅ 업로드 후 확인

업로드가 완료되면:
- https://github.com/dldpwls020527/math-website 에서 확인 가능
- 파일들이 모두 보이는지 확인

---

## 🔄 코드 수정 후 재업로드

### GitHub Desktop 사용 시:
1. 파일 수정
2. GitHub Desktop에서 변경사항 확인
3. 좌측 하단 메시지 입력 (예: "Update formula")
4. "Commit to main" 클릭
5. "Push origin" 클릭

### Git 명령어 사용 시:
```powershell
git add .
git commit -m "Update: 변경사항 설명"
git push
```

---

## 🚀 다음 단계: Railway 배포

GitHub에 업로드가 완료되면:
1. https://railway.app 접속
2. "Start a New Project" → "Deploy from GitHub repo"
3. `dldpwls020527/math-website` 저장소 선택
4. 자동 배포 시작!

자세한 내용은 `Railway_배포_완벽가이드.md` 참고

