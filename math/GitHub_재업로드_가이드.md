# 🔄 GitHub에 변경사항 재업로드하기

이미지 관리 기능이 추가된 새 버전을 GitHub에 업로드하는 방법입니다.

---

## 방법 1: GitHub Desktop 사용 (가장 쉬움) ⭐ 추천

### 1단계: GitHub Desktop 열기

1. **GitHub Desktop 실행**
2. 저장소가 이미 열려있어야 합니다
   - 없다면: "File" → "Add Local Repository" → `C:\Users\dldpw\Desktop\math` 선택

### 2단계: 변경사항 확인

1. GitHub Desktop 좌측에 **변경사항 목록**이 표시됩니다
2. 추가된 파일들 확인:
   - `app.py` (수정됨)
   - `templates/admin_images.html` (새 파일)
   - 기타 변경된 파일들

### 3단계: 커밋 및 업로드

1. **하단 "Summary" 필드**에 메시지 입력:
   ```
   이미지 관리 기능 추가
   - 이미지 업로드 기능
   - 이미지 관리 페이지
   - 공식에 이미지 연결 기능
   ```

2. **"Commit to main"** 버튼 클릭

3. **상단 "Push origin"** 버튼 클릭
   - 또는 "Repository" → "Push"

### 4단계: 완료! ✅

- 업로드 완료!
- GitHub에서 확인: https://github.com/dldpwls020527/math-website

---

## 방법 2: 웹 인터페이스 사용

### 1단계: GitHub 저장소 접속

1. 브라우저에서 https://github.com/dldpwls020527/math-website 접속
2. **"Add file"** → **"Upload files"** 클릭

### 2단계: 변경된 파일 업로드

1. 파일 탐색기에서 `C:\Users\dldpw\Desktop\math` 폴더 열기
2. **변경/추가된 파일만 선택**:
   - `app.py` (수정됨)
   - `templates/admin_images.html` (새 파일)
   - 또는 모든 파일 선택 (Ctrl + A)

3. 파일들을 브라우저로 드래그 앤 드롭

### 3단계: 커밋

1. 하단 커밋 메시지 입력:
   ```
   이미지 관리 기능 추가
   ```

2. **"Commit changes"** 버튼 클릭

### 4단계: 완료! ✅

---

## 방법 3: Git 명령어 사용

Git이 설치되어 있다면:

```powershell
# 프로젝트 폴더로 이동
cd C:\Users\dldpw\Desktop\math

# 변경사항 확인
git status

# 모든 변경사항 추가
git add .

# 커밋
git commit -m "이미지 관리 기능 추가"

# GitHub에 업로드
git push
```

---

## 🚀 업로드 후 Railway 자동 재배포

GitHub에 업로드하면:

1. **Railway가 자동으로 변경사항 감지** (약 1-2분)
2. **자동으로 재배포 시작**
3. Railway 대시보드에서 재배포 진행 상황 확인

### Railway 재배포 확인

1. https://railway.app 접속
2. 프로젝트 클릭
3. "Deployments" 탭에서 재배포 진행 상황 확인
4. "Active" 상태가 되면 완료!

---

## ✅ 업로드 후 확인사항

### GitHub에서 확인
- https://github.com/dldpwls020527/math-website
- 새로 추가된 파일들이 보이는지 확인
- `templates/admin_images.html` 파일 확인

### Railway에서 확인
- 재배포가 완료되면
- 웹사이트 URL + `/admin/images` 접속
- 이미지 관리 페이지가 작동하는지 테스트

---

## 🔄 코드 수정 후 계속 업로드하는 방법

앞으로 코드를 수정할 때마다:

### GitHub Desktop 사용 시:
1. 파일 수정
2. GitHub Desktop에서 변경사항 자동 감지
3. Summary에 메시지 입력
4. "Commit to main" 클릭
5. "Push origin" 클릭

### 웹 인터페이스 사용 시:
1. 파일 수정 후 저장
2. GitHub → "Add file" → "Upload files"
3. 변경된 파일만 업로드
4. "Commit changes" 클릭

---

## 💡 팁

1. **커밋 메시지는 명확하게 작성**
   - 무엇을 변경했는지 설명
   - 예: "이미지 관리 기능 추가", "버그 수정" 등

2. **작은 변경사항도 자주 업로드**
   - 큰 변경사항보다 작은 변경사항을 여러 번 업로드하는 것이 좋습니다

3. **Railway 자동 재배포 확인**
   - GitHub에 푸시하면 Railway가 자동으로 재배포합니다
   - 재배포 완료까지 5-10분 소요될 수 있습니다

---

## 🆘 문제 해결

### GitHub Desktop에서 "Push origin" 버튼이 비활성화된 경우

1. **인터넷 연결 확인**
2. **GitHub 계정 로그인 확인**
3. **변경사항이 커밋되었는지 확인**

### 업로드가 실패하는 경우

1. **GitHub 저장소 권한 확인**
2. **파일 크기 확인** (너무 큰 파일은 제외)
3. **인터넷 연결 확인**

---

**이제 변경사항을 GitHub에 업로드하고 Railway에 자동 배포할 수 있습니다!** 🚀

