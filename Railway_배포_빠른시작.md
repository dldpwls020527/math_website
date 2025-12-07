# 🚂 Railway 배포 빠른 시작 가이드

GitHub 저장소: **dldpwls020527/math-website**

---

## 🚀 단계별 배포 가이드

### 1단계: Railway 계정 생성 (2분)

1. **Railway 웹사이트 접속**
   - 브라우저에서 https://railway.app 열기

2. **로그인/가입**
   - "Start a New Project" 또는 "Login" 클릭
   - **"Continue with GitHub"** 버튼 클릭
   - GitHub 계정으로 로그인 (dldpwls020527)
   - Railway가 GitHub 접근 권한을 요청하면 **"Authorize Railway"** 또는 **"승인"** 클릭

---

### 2단계: 프로젝트 배포 (3분)

1. **새 프로젝트 생성**
   - Railway 대시보드에서 **"New Project"** 버튼 클릭
   - 또는 **"+ New"** → **"Project"** 클릭

2. **GitHub 저장소 연결**
   - **"Deploy from GitHub repo"** 선택
   - GitHub 저장소 목록에서 **`math-website`** 찾아서 클릭
   - 또는 검색창에 `math-website` 입력

3. **배포 시작**
   - 저장소 선택 후 자동으로 배포가 시작됩니다
   - "Deployments" 탭에서 진행 상황 확인 가능

---

### 3단계: 배포 진행 확인 (5-10분)

1. **배포 상태 확인**
   - Railway 대시보드에서 프로젝트 클릭
   - "Deployments" 탭에서 상태 확인:
     - **Building...** → 패키지 설치 중
     - **Deploying...** → 배포 중
     - **Active** → 완료! ✅

2. **로그 확인 (선택사항)**
   - "Deployments" → 최신 배포 클릭 → "View Logs"
   - 오류가 있으면 여기서 확인 가능

---

### 4단계: 외부 접속 URL 확인 (1분)

1. **도메인 생성**
   - 프로젝트 대시보드로 이동
   - 우측 상단 또는 "Settings" 탭 클릭
   - **"Domains"** 섹션 찾기
   - **"Generate Domain"** 버튼 클릭
   - 또는 자동으로 도메인이 생성되어 있을 수 있습니다

2. **URL 확인**
   - 생성된 도메인 확인 (예: `https://math-website-production.up.railway.app`)
   - 이 URL을 복사하세요!

---

### 5단계: 웹사이트 테스트

1. **브라우저에서 접속**
   - 복사한 URL을 브라우저 주소창에 입력
   - 예: `https://math-website-production.up.railway.app`

2. **작동 확인**
   - 웹사이트가 정상적으로 열리는지 확인
   - 메인 페이지, 공식 목록, 검색 기능 테스트

---

## ✅ 완료!

이제 **이 URL을 누구에게나 공유**할 수 있습니다!

- ✅ 전 세계 어디서나 접속 가능
- ✅ 24시간 자동 실행
- ✅ HTTPS 자동 지원
- ✅ 영구 URL 제공

---

## 🔄 코드 수정 후 재배포

코드를 수정했다면:

1. **GitHub에 업로드**
   - GitHub Desktop 또는 웹 인터페이스로 변경사항 업로드

2. **Railway 자동 재배포**
   - Railway가 자동으로 GitHub 변경사항 감지
   - 자동으로 재배포 시작 (약 5분)
   - 별도 작업 불필요!

---

## 🎯 화면 예시

### Railway 대시보드:
```
┌─────────────────────────────────────┐
│ Projects                            │
│                                     │
│ [+ New Project]                     │
│                                     │
│ ┌─────────────────────────────┐   │
│ │ math-website                │   │
│ │ Active                      │   │
│ │ https://math-website...     │   │
│ └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### 저장소 연결 화면:
```
┌─────────────────────────────────────┐
│ Select a repository                 │
│                                     │
│ [Search repositories...]            │
│                                     │
│ 📦 math-website                     │
│    dldpwls020527/math-website      │
│                                     │
│ 📦 other-repo                       │
│    ...                             │
└─────────────────────────────────────┘
```

---

## 🆘 문제 해결

### 배포가 실패하는 경우

1. **로그 확인**
   - 프로젝트 → Deployments → 최신 배포 클릭 → View Logs
   - 오류 메시지 확인

2. **일반적인 오류:**
   - `requirements.txt` 패키지 오류
     - 로그에서 어떤 패키지가 문제인지 확인
     - `requirements.txt` 수정 후 GitHub에 다시 업로드
   
   - Python 버전 문제
     - `runtime.txt`에서 Python 버전 확인
     - 필요시 수정

   - `Procfile` 오류
     - `Procfile` 내용: `web: python app.py` 확인

### 웹사이트가 작동하지 않는 경우

1. **URL 확인**
   - 올바른 URL인지 확인
   - `https://`로 시작하는지 확인

2. **서비스 상태 확인**
   - Railway 대시보드에서 서비스가 "Active" 상태인지 확인
   - "Building" 또는 "Deploying" 중이면 완료될 때까지 기다리기

3. **로그 확인**
   - 배포 로그에서 런타임 오류 확인

---

## 💡 팁

1. **도메인 이름 변경**
   - Settings → Domains → Generate Domain 클릭
   - 새로운 도메인 생성 가능

2. **커스텀 도메인 연결**
   - Settings → Domains → Custom Domain
   - 자신의 도메인 연결 가능

3. **환경 변수 설정**
   - Settings → Variables
   - 필요한 환경 변수 추가 가능

---

## 🎉 다음 단계

배포가 완료되면:
1. ✅ URL을 친구들에게 공유
2. ✅ 스마트폰에서도 접속 테스트
3. ✅ 코드 수정 후 자동 재배포 확인

**이제 전 세계 어디서나 접속 가능한 웹사이트가 완성되었습니다!** 🚀

