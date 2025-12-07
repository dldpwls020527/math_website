# 🚀 외부 접근 가능한 웹사이트 배포 가이드

수학 공식 웹사이트를 외부에서 접근할 수 있도록 배포하는 방법입니다.

## 🎯 빠른 배포 방법 (선택)

### 방법 1: ngrok 사용 (가장 빠름) ⭐ 추천

로컬 서버를 즉시 외부에 노출시키는 방법입니다.

#### Windows에서 설치 및 사용

1. **ngrok 다운로드**
   - https://ngrok.com/download 에서 Windows용 다운로드
   - 또는 Chocolatey 사용: `choco install ngrok`

2. **ngrok 계정 생성** (무료)
   - https://dashboard.ngrok.com/signup 에서 가입
   - 인증 토큰 받기

3. **ngrok 인증**
   ```powershell
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

4. **Flask 서버 실행**
   ```powershell
   python app.py
   ```

5. **새 PowerShell 창에서 ngrok 실행**
   ```powershell
   ngrok http 5000
   ```

6. **외부 URL 사용**
   - ngrok이 제공하는 URL (예: `https://abc123.ngrok.io`) 사용
   - 이 URL을 누구에게나 공유 가능!

**장점**: 즉시 사용 가능, HTTPS 자동 지원  
**단점**: 무료 플랜은 세션이 끊기면 URL이 변경됨

---

### 방법 2: Railway 배포 (영구 URL) ⭐ 추천

Railway는 Flask 앱을 쉽게 배포할 수 있는 클라우드 플랫폼입니다.

#### 배포 단계

1. **GitHub 저장소 준비**
   - 이 프로젝트를 GitHub에 업로드

2. **Railway 계정 생성**
   - https://railway.app 에서 GitHub 계정으로 가입

3. **Railway에 배포**
   - Railway 대시보드에서 "New Project" 클릭
   - "Deploy from GitHub repo" 선택
   - 저장소 연결
   - 자동으로 배포 시작

4. **도메인 확인**
   - 배포 완료 후 Railway가 제공하는 URL 확인 (예: `https://math-formula-website.railway.app`)
   - 이 URL은 영구적으로 사용 가능!

**장점**: 영구 URL, 자동 배포, HTTPS 자동 지원, 무료 플랜  
**단점**: GitHub 저장소 필요

---

### 방법 3: Render 배포

Render도 Flask 앱 배포에 좋은 옵션입니다.

#### 배포 단계

1. **GitHub 저장소 준비**
   - 이 프로젝트를 GitHub에 업로드

2. **Render 계정 생성**
   - https://render.com 에서 가입

3. **Render에 배포**
   - Render 대시보드에서 "New +" → "Web Service" 선택
   - GitHub 저장소 연결
   - 다음 설정 사용:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python app.py`
   - "Create Web Service" 클릭

4. **도메인 확인**
   - 배포 완료 후 Render가 제공하는 URL 확인

**장점**: 영구 URL, 무료 플랜, 자동 배포  
**단점**: 무료 플랜은 15분 비활성 시 자동 정지

---

### 방법 4: PythonAnywhere 배포

Python 전용 호스팅 서비스입니다.

#### 배포 단계

1. **계정 생성**
   - https://www.pythonanywhere.com 에서 가입 (무료)

2. **파일 업로드**
   - Files 탭에서 프로젝트 폴더 전체 업로드
   - 또는 Bash에서 git clone

3. **가상환경 설정**
   ```bash
   mkvirtualenv math-website --python=python3.11
   pip install -r requirements.txt
   ```

4. **웹 앱 설정**
   - Web 탭에서 "Add a new web app" 클릭
   - Flask 선택
   - Python 3.11 선택
   - Source code 경로 설정: `/home/username/math`
   - WSGI 파일 경로 설정: `/var/www/username_pythonanywhere_com_wsgi.py`

5. **WSGI 파일 수정**
   ```python
   import sys
   path = '/home/username/math'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

6. **웹사이트 활성화**
   - Web 탭에서 "Reload" 클릭
   - URL 확인 (예: `username.pythonanywhere.com`)

**장점**: Python 전용, 무료 플랜, 영구 URL  
**단점**: 설정이 조금 복잡

---

### 방법 5: Replit 배포 (온라인 IDE + 호스팅)

코드 편집과 배포를 한 곳에서 할 수 있습니다.

#### 배포 단계

1. **Replit 계정 생성**
   - https://replit.com 에서 가입

2. **프로젝트 가져오기**
   - "Create Repl" → "Import from GitHub" 선택
   - 또는 파일 직접 업로드

3. **실행**
   - "Run" 버튼 클릭
   - 자동으로 외부 URL 생성

**장점**: 온라인 IDE 포함, 즉시 배포, 무료 플랜  
**단점**: 무료 플랜 제한 있음

---

## 📋 배포 전 체크리스트

배포하기 전에 확인해야 할 사항:

- [x] `app.py`가 `PORT` 환경변수를 지원하도록 수정됨
- [x] `Procfile` 생성됨 (Railway/Heroku용)
- [x] `runtime.txt` 생성됨 (Python 버전 지정)
- [x] `requirements.txt`에 모든 패키지 포함됨
- [ ] GitHub 저장소에 업로드 (클라우드 배포 시 필요)

---

## 🔧 로컬에서 외부 접근 테스트

로컬 네트워크에서 다른 기기로 접근 테스트:

1. **Flask 서버 실행**
   ```powershell
   python app.py
   ```

2. **로컬 IP 주소 확인**
   ```powershell
   ipconfig
   # IPv4 주소 확인 (예: 192.168.1.100)
   ```

3. **같은 Wi-Fi 네트워크의 다른 기기에서 접속**
   - 브라우저에서 `http://192.168.1.100:5000` 접속

**주의**: 방화벽에서 포트 5000 허용 필요할 수 있음

---

## 🌐 권장 배포 방법 비교

| 방법 | 속도 | 영구 URL | 난이도 | 비용 |
|------|------|----------|--------|------|
| ngrok | ⚡⚡⚡ | ❌ | ⭐ 쉬움 | 무료 |
| Railway | ⚡⚡ | ✅ | ⭐⭐ 보통 | 무료 |
| Render | ⚡⚡ | ✅ | ⭐⭐ 보통 | 무료 |
| PythonAnywhere | ⚡ | ✅ | ⭐⭐⭐ 어려움 | 무료 |
| Replit | ⚡⚡⚡ | ✅ | ⭐ 쉬움 | 무료 |

---

## 💡 추천

- **빠른 테스트**: ngrok 사용
- **영구 배포**: Railway 또는 Render 사용

---

## 🆘 문제 해결

### 포트가 이미 사용 중인 경우
```powershell
# 포트 5000 사용 중인 프로세스 확인
netstat -ano | findstr :5000

# 다른 포트 사용
set PORT=8000
python app.py
```

### 배포 후 오류가 발생하는 경우
- 로그 확인 (Railway, Render 등에서 제공)
- `requirements.txt`에 모든 패키지 포함되어 있는지 확인
- 환경변수 설정 확인

---

## 📞 도움이 필요하신가요?

배포 중 문제가 발생하면:
1. 배포 플랫폼의 로그 확인
2. `app.py`가 올바르게 실행되는지 로컬에서 확인
3. `requirements.txt`의 패키지 버전 확인

