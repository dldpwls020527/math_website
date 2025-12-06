# 🎯 GitHub Desktop 단계별 가이드

현재 상황: "This directory does not appear to be a Git repository" 메시지 표시됨

## ✅ 지금 해야 할 일

**"Add repository" (파란색 버튼) 클릭하세요!**

이것은 정상적인 메시지입니다. GitHub Desktop이 자동으로 Git 저장소를 만들어줍니다.

---

## 📋 다음 단계 (버튼 클릭 후)

### 1단계: 저장소 추가 완료
- "Add repository" 클릭하면 GitHub Desktop 메인 화면으로 이동합니다
- 좌측에 변경사항이 표시됩니다

### 2단계: 첫 커밋 만들기
1. 좌측 하단 "Summary" 필드에 메시지 입력:
   ```
   Initial commit: 수학 공식 웹사이트
   ```
2. 좌측 하단에 "Description" (선택사항)에도 입력 가능:
   ```
   중고등학생을 위한 수학 공식 학습 웹사이트
   ```
3. **"Commit to main"** 버튼 클릭

### 3단계: GitHub에 업로드 (Publish)
1. 상단 메뉴에서 **"Repository"** → **"Publish repository"** 클릭
   - 또는 좌측 상단에 "Publish repository" 버튼이 보이면 직접 클릭
2. 팝업 창에서:
   - **Name**: `math-website` (또는 원하는 이름)
   - **Description**: (선택사항) "수학 공식 웹사이트"
   - **"Keep this code private"** 체크 해제 ⚠️ (Public으로 설정해야 Railway 배포 가능)
3. **"Publish Repository"** 버튼 클릭

### 4단계: 완료! ✅
- 업로드가 시작됩니다 (1-2분 소요)
- 완료되면 GitHub 웹사이트에서 확인 가능:
  - https://github.com/dldpwls020527/math-website

---

## 🖼️ 화면 예시

### 커밋 화면:
```
┌─────────────────────────────────┐
│ Changes (15)                    │
│ + app.py                        │
│ + requirements.txt              │
│ + templates/index.html          │
│ ... (모든 파일)                 │
│                                 │
│ Summary: [Initial commit...]    │
│ Description: [선택사항]          │
│                                 │
│ [Commit to main]                │
└─────────────────────────────────┘
```

### Publish 화면:
```
┌─────────────────────────────────┐
│ Publish repository              │
│                                 │
│ Name: math-website              │
│ Description: (선택사항)          │
│ ☐ Keep this code private        │
│                                 │
│ [Publish Repository]  [Cancel]  │
└─────────────────────────────────┘
```

---

## ⚠️ 주의사항

1. **"Keep this code private" 체크 해제 필수!**
   - Railway 배포를 위해서는 Public 저장소여야 합니다
   - 체크 해제하면 Public 저장소로 생성됩니다

2. **파일이 모두 보이는지 확인**
   - 좌측 Changes 섹션에 모든 파일이 표시되어야 합니다
   - 만약 일부 파일이 안 보인다면 `.gitignore` 파일을 확인하세요

---

## 🔄 이후 코드 수정 시

1. 파일 수정
2. GitHub Desktop에서 변경사항 자동 감지
3. Summary에 메시지 입력
4. "Commit to main" 클릭
5. 상단 "Push origin" 버튼 클릭 (또는 "Repository" → "Push")

---

## 🚀 다음 단계: Railway 배포

GitHub 업로드 완료 후:
1. https://railway.app 접속
2. GitHub 계정으로 로그인
3. "New Project" → "Deploy from GitHub repo"
4. `math-website` 저장소 선택
5. 자동 배포!

자세한 내용: `Railway_배포_완벽가이드.md`

