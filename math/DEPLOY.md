# 🌐 외부 접근 가능한 웹사이트 배포 방법

## 방법 1: ngrok (가장 빠름) ⭐ 추천

ngrok은 로컬 서버를 외부에 노출시키는 터널링 서비스입니다.

### 설치 및 사용

1. **ngrok 설치**
```bash
# Linux
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok

# 또는 직접 다운로드
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar xvzf ngrok-v3-stable-linux-amd64.tgz
sudo mv ngrok /usr/local/bin
```

2. **ngrok 계정 생성 및 인증** (무료)
   - https://ngrok.com 에서 가입
   - 인증 토큰 받기

3. **ngrok 실행**
```bash
# Flask 서버가 실행 중인 상태에서 다른 터미널에서
ngrok http 5000
```

4. **외부 URL 받기**
   - ngrok이 제공하는 URL (예: `https://abc123.ngrok.io`)을 사용
   - 이 URL을 누구에게나 공유 가능

### 장점
- ✅ 즉시 사용 가능
- ✅ 무료 플랜 제공
- ✅ HTTPS 자동 지원
- ✅ 설정 간단

### 단점
- ❌ 무료 플랜은 URL이 매번 변경됨
- ❌ 세션이 끊기면 URL 변경

---

## 방법 2: Railway (클라우드 호스팅) ⭐ 추천

Railway는 Flask 앱을 쉽게 배포할 수 있는 클라우드 플랫폼입니다.

### 배포 단계

1. **Railway 계정 생성**
   - https://railway.app 에서 GitHub 계정으로 가입

2. **프로젝트 설정 파일 생성**

`Procfile` 생성:
```
web: python app.py
```

`runtime.txt` 생성 (선택사항):
```
python-3.11
```

3. **Railway에 배포**
   - Railway 대시보드에서 "New Project" 클릭
   - "Deploy from GitHub repo" 선택
   - 저장소 연결
   - 자동으로 배포 시작

4. **환경 변수 설정** (필요한 경우)
   - Railway 대시보드에서 환경 변수 추가

### 장점
- ✅ 무료 플랜 제공
- ✅ 영구 URL 제공
- ✅ 자동 배포
- ✅ HTTPS 자동 지원

---

## 방법 3: Render (클라우드 호스팅)

Render도 Flask 앱 배포에 좋은 옵션입니다.

### 배포 단계

1. **Render 계정 생성**
   - https://render.com 에서 가입

2. **프로젝트 설정**

`render.yaml` 생성:
```yaml
services:
  - type: web
    name: math-formula-website
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: PORT
        value: 5000
```

3. **Render에 배포**
   - Render 대시보드에서 "New Web Service" 선택
   - GitHub 저장소 연결
   - 자동 배포

### 장점
- ✅ 무료 플랜 제공
- ✅ 영구 URL
- ✅ 자동 배포

---

## 방법 4: PythonAnywhere

Python 웹 앱 전용 호스팅 서비스입니다.

### 배포 단계

1. **계정 생성**
   - https://www.pythonanywhere.com 에서 가입 (무료)

2. **파일 업로드**
   - Files 탭에서 프로젝트 파일 업로드

3. **웹 앱 설정**
   - Web 탭에서 Flask 앱 생성
   - 소스 코드 경로 설정
   - WSGI 파일 설정

### 장점
- ✅ Python 전용
- ✅ 무료 플랜
- ✅ 영구 URL

---

## 방법 5: Replit (온라인 IDE + 호스팅)

Replit은 코드 편집과 배포를 한 곳에서 할 수 있습니다.

### 배포 단계

1. **Replit 계정 생성**
   - https://replit.com 에서 가입

2. **프로젝트 가져오기**
   - GitHub에서 import 또는 직접 파일 업로드

3. **실행**
   - Run 버튼 클릭
   - 자동으로 외부 URL 생성

### 장점
- ✅ 온라인 IDE 포함
- ✅ 즉시 배포
- ✅ 무료 플랜

---

## 빠른 시작: ngrok 사용하기

가장 빠르게 외부 접근을 원한다면 ngrok을 사용하세요:

```bash
# 1. Flask 서버 실행 (이미 실행 중)
python app.py

# 2. 새 터미널에서 ngrok 실행
ngrok http 5000

# 3. ngrok이 제공하는 URL 사용 (예: https://abc123.ngrok.io)
```

이 URL을 누구에게나 공유할 수 있습니다!

