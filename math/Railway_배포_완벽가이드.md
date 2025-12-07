# 🚂 Railway 배포 완벽 가이드

Railway에 배포하면 **누구나 인터넷에서 접속할 수 있는 웹사이트**가 됩니다!

---

## 🤔 Railway 배포란?

### 간단 설명
1. **내가 Railway에 웹사이트 코드를 올림** (배포)
2. **Railway가 자동으로 서버를 만들어서 실행시킴**
3. **Railway가 고유한 URL을 제공함** (예: `https://math-website-production.up.railway.app`)
4. **이 URL을 다른 사람에게 공유**
5. **다른 사람은 그냥 브라우저에서 그 URL만 입력하면 접속됨** ✨

### 중요한 점
- ❌ **다른 접속자가 Railway 계정이 필요 없음**
- ❌ **다른 접속자가 Railway에 가입할 필요 없음**
- ✅ **그냥 브라우저에서 URL만 입력하면 됨**
- ✅ **전 세계 어디서나 접속 가능**
- ✅ **24시간 자동으로 실행됨** (내 컴퓨터 꺼도 됨!)

---

## 📋 전체 과정 요약

```
[내 컴퓨터] → [GitHub] → [Railway] → [인터넷] → [누구나 접속 가능]
   코드 업로드   저장소    자동 배포    URL 제공
```

---

## 🚀 단계별 상세 가이드

### 1단계: GitHub 저장소 준비 (5분)

#### 1-1. GitHub 계정이 없다면
1. https://github.com 접속
2. "Sign up" 클릭하여 무료 계정 생성

#### 1-2. 새 GitHub 저장소 생성
1. GitHub 로그인 후 우측 상단 "+" → "New repository" 클릭
2. 저장소 이름 입력 (예: `math-website`)
3. **Public** 선택 (무료 계정은 Public만 무료)
4. "Add a README file" 체크하지 않기 (이미 파일 있음)
5. "Create repository" 클릭

#### 1-3. 로컬 파일을 GitHub에 업로드

**방법 A: GitHub Desktop 사용 (가장 쉬움)**

1. GitHub Desktop 설치: https://desktop.github.com/
2. GitHub Desktop 실행
3. "File" → "Add Local Repository" 클릭
4. 프로젝트 폴더 선택 (예: `C:\Users\dldpw\Desktop\math`)
5. 좌측 하단에 변경사항 확인
6. 좌측 하단에 메시지 입력 (예: "Initial commit")
7. "Commit to main" 클릭
8. "Publish repository" 클릭
9. 저장소 이름 확인 후 "Publish repository" 클릭

**방법 B: 명령어 사용**

```powershell
# 1. Git이 설치되어 있는지 확인
git --version

# 2. Git이 없다면 설치
# https://git-scm.com/download/win 에서 다운로드

# 3. 프로젝트 폴더로 이동
cd C:\Users\dldpw\Desktop\math

# 4. Git 초기화 (처음 한 번만)
git init

# 5. 모든 파일 추가
git add .

# 6. 커밋 (변경사항 저장)
git commit -m "Initial commit"

# 7. GitHub 저장소 연결 (YOUR_USERNAME을 실제 GitHub 사용자명으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/math-website.git

# 8. GitHub에 업로드
git branch -M main
git push -u origin main
```

**GitHub 사용자명/비밀번호 입력 요구 시:**
- GitHub에서 Personal Access Token 사용 필요할 수 있음
- Settings → Developer settings → Personal access tokens → Generate new token

---

### 2단계: Railway 계정 생성 및 연결 (2분)

1. **Railway 웹사이트 접속**
   - https://railway.app 접속

2. **로그인/가입**
   - "Start a New Project" 또는 "Login" 클릭
   - "Continue with GitHub" 선택
   - GitHub 계정으로 로그인
   - Railway 접근 권한 허용 클릭

---

### 3단계: Railway에 프로젝트 배포 (5분)

1. **새 프로젝트 생성**
   - Railway 대시보드에서 "New Project" 클릭
   - 또는 "+ New" 버튼 클릭

2. **GitHub 저장소 연결**
   - "Deploy from GitHub repo" 선택
   - 저장소 목록에서 방금 만든 `math-website` 저장소 선택
   - "Deploy Now" 클릭

3. **배포 진행 확인**
   - "Deployments" 탭에서 배포 진행 상황 확인
   - "Building..." → "Deploying..." → "Active" 상태로 변경됨
   - 약 5-10분 소요

---

### 4단계: 외부 접속 URL 확인 (1분)

1. **도메인 확인**
   - 배포가 완료되면 프로젝트 대시보드로 이동
   - "Settings" 탭 클릭
   - "Domains" 섹션 확인
   - 또는 프로젝트 메인 화면에서 "Generate Domain" 클릭

2. **URL 복사**
   - 예시: `https://math-website-production.up.railway.app`
   - 이 URL을 복사하세요!

---

### 5단계: 웹사이트 테스트

1. **브라우저에서 접속**
   - 복사한 URL을 브라우저 주소창에 입력
   - 예: `https://math-website-production.up.railway.app`

2. **작동 확인**
   - 웹사이트가 정상적으로 열리는지 확인
   - 기능들이 제대로 작동하는지 테스트

---

### 6단계: 다른 사람에게 공유

이제 **이 URL을 누구에게나 공유**할 수 있습니다!

**공유 방법:**
- 카카오톡, 메신저로 URL 전송
- 이메일로 전송
- 소셜미디어에 게시
- QR 코드 생성

**다른 사람이 해야 할 일:**
- 그냥 브라우저에서 URL 입력
- 끝! (별도 설치나 가입 없음)

---

## 🔄 코드 수정 후 재배포

웹사이트를 수정했다면:

### GitHub Desktop 사용 시:
1. 파일 수정
2. GitHub Desktop에서 변경사항 확인
3. 좌측 하단에 메시지 입력 (예: "Update formula")
4. "Commit to main" 클릭
5. "Push origin" 클릭
6. Railway가 자동으로 재배포 (몇 분 소요)

### 명령어 사용 시:
```powershell
git add .
git commit -m "Update formula"
git push
```

Railway가 자동으로 변경사항을 감지하고 재배포합니다!

---

## 🎯 실제 사용 예시

### 상황: 친구에게 내 웹사이트 보여주기

**내가 할 일:**
1. Railway에 배포 완료
2. URL 확인: `https://math-website-production.up.railway.app`
3. 친구에게 URL 전송: "이거 봐봐! https://math-website-production.up.railway.app"

**친구가 할 일:**
1. 카카오톡/메신저에서 URL 확인
2. URL 클릭 또는 브라우저에 입력
3. 웹사이트 보기 ✅

**친구는:**
- Railway 계정 불필요
- 가입 불필요
- 설치 불필요
- 그냥 URL만 있으면 됨!

---

## 🔍 Railway 대시보드에서 확인할 수 있는 것들

1. **Deployments (배포)**
   - 배포 기록 확인
   - 로그 확인 (오류 발생 시)

2. **Settings (설정)**
   - 도메인 변경
   - 환경 변수 설정

3. **Metrics (통계)**
   - 트래픽 확인
   - 사용량 확인

---

## ⚠️ 주의사항

1. **무료 플랜 제한**
   - 월 500시간 무료 (약 20일)
   - 사용량 초과 시 유료 플랜 필요

2. **저장소는 Public으로 설정**
   - 무료 GitHub 계정은 Private 저장소 배포 시 비용 발생 가능

3. **첫 배포는 시간이 걸림**
   - 5-10분 정도 소요
   - 인내심을 가지세요!

---

## 🆘 문제 해결

### 배포가 실패하는 경우
1. Railway 대시보드 → Deployments → 로그 확인
2. 오류 메시지 확인
3. 일반적인 오류:
   - `requirements.txt`에 패키지 누락
   - Python 버전 문제
   - `Procfile` 오류

### 웹사이트가 작동하지 않는 경우
1. URL이 올바른지 확인
2. Railway 대시보드에서 서비스가 "Active" 상태인지 확인
3. 로그에서 오류 확인

### 코드 변경이 반영되지 않는 경우
1. GitHub에 제대로 푸시되었는지 확인
2. Railway가 새 배포를 감지했는지 확인 (Deployments 탭)
3. 배포 완료까지 기다리기 (몇 분 소요)

---

## ✅ 체크리스트

배포 전 확인사항:
- [ ] GitHub 저장소 생성 완료
- [ ] 코드가 GitHub에 업로드됨
- [ ] Railway 계정 생성 및 GitHub 연결 완료
- [ ] `Procfile` 파일 존재 확인
- [ ] `requirements.txt` 파일 존재 확인
- [ ] `app.py`가 `PORT` 환경변수 지원 (이미 완료)

---

## 🎉 완료!

Railway 배포를 완료하면:
- ✅ 전 세계 어디서나 접속 가능
- ✅ 24시간 자동 실행
- ✅ HTTPS 자동 지원 (보안)
- ✅ 영구 URL 제공
- ✅ 자동 재배포 (코드 수정 시)

**이제 다른 사람들에게 URL만 공유하면 됩니다!** 🚀

