# 🔧 이클립스에서 프로젝트 설정하기

이클립스에서 이 Flask 프로젝트를 개발하고 실행하는 방법입니다.

## 1. 이클립스 설치 및 PyDev 설정

### PyDev 플러그인 설치

1. **이클립스 실행**
2. **Help → Eclipse Marketplace** 메뉴 선택
3. "PyDev" 검색
4. "PyDev - Python IDE for Eclipse" 설치
5. 이클립스 재시작

## 2. 프로젝트 가져오기

### 방법 1: 기존 프로젝트로 가져오기

1. **File → Import** 선택
2. **General → Existing Projects into Workspace** 선택
3. **Browse** 버튼 클릭하여 `/DATA/leeyj/math_program` 폴더 선택
4. **Finish** 클릭

### 방법 2: 새 프로젝트로 만들기

1. **File → New → PyDev Project** 선택
2. Project name: `math_program`
3. Project contents: `/DATA/leeyj/math_program` 선택
4. **Finish** 클릭

## 3. Python 인터프리터 설정

1. **Window → Preferences** (또는 **Eclipse → Preferences** on Mac)
2. **PyDev → Interpreters → Python Interpreter** 선택
3. **New** 버튼 클릭
4. Interpreter name: `solar` (또는 원하는 이름)
5. Interpreter Executable: conda 환경의 Python 경로 입력
   - 예: `/opt/anaconda3/envs/solar/bin/python`
   - 또는: `which python` 명령어로 경로 확인
6. **OK** 클릭

## 4. 프로젝트 인터프리터 설정

1. 프로젝트를 **우클릭 → Properties**
2. **PyDev - Interpreter/Grammar** 선택
3. **Interpreter** 드롭다운에서 `solar` 선택
4. **Apply and Close** 클릭

## 5. Flask 서버 실행 설정

### Run Configuration 만들기

1. **Run → Run Configurations** 선택
2. **Python Run** 더블 클릭하여 새 설정 생성
3. 설정:
   - **Name**: `Flask Math Website`
   - **Main Module**: `app.py` 선택
   - **Working Directory**: `${workspace_loc:math_program}`
   - **Arguments**: 없음
   - **Environment**: 
     - `FLASK_APP=app.py`
     - `FLASK_ENV=development`
4. **Apply** → **Run** 클릭

### 또는 간단하게 실행

1. `app.py` 파일을 열기
2. **우클릭 → Run As → Python Run** 선택

## 6. 디버깅 설정

1. `app.py`에 브레이크포인트 설정
2. **Run → Debug Configurations**
3. 위의 Run Configuration과 동일하게 설정
4. **Debug** 버튼 클릭

## 7. 이클립스에서 유용한 기능

### 코드 자동 완성
- `Ctrl + Space`: 자동 완성
- Flask, Python 함수 자동 완성 지원

### 코드 포맷팅
- `Ctrl + Shift + F`: 코드 포맷팅

### 실행 단축키
- `Ctrl + F11`: 마지막 실행 설정으로 실행
- `F11`: 디버그 모드로 실행

### 터미널 통합
- **Window → Show View → Terminal** 선택
- 이클립스 내에서 터미널 사용 가능

## 8. 문제 해결

### Python 인터프리터를 찾을 수 없는 경우
```bash
# conda 환경의 Python 경로 확인
which python
# 또는
conda info --envs
```

### 패키지가 인식되지 않는 경우
1. **Window → Preferences → PyDev → Interpreters → Python Interpreter**
2. **Libraries** 탭에서 필요한 라이브러리 경로 추가

### Flask 모듈을 찾을 수 없는 경우
```bash
# conda 환경에서 패키지 재설치
conda activate solar
pip install -r requirements.txt
```

## 9. 프로젝트 구조 확인

이클립스의 **Project Explorer**에서 다음 구조를 확인할 수 있습니다:

```
math_program/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── formulas.html
│   └── formula_detail.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── data/
    └── formulas.json
```

## 10. Git 연동 (선택사항)

1. **File → Import → Git → Projects from Git**
2. 저장소 URL 입력 또는 로컬 저장소 선택
3. 프로젝트 가져오기

---

## 💡 팁

- **PyDev Perspective** 사용: **Window → Perspective → Open Perspective → PyDev**
- **Code Analysis**: **PyDev → Code Analysis**에서 코드 품질 확인
- **Refactoring**: **Refactor** 메뉴에서 변수명 변경, 함수 추출 등 가능

이제 이클립스에서 Flask 웹사이트를 개발하고 실행할 수 있습니다!

