# 🚀 빠른 시작 가이드

## Windows 사용자

### 1️⃣ 실행 파일 만들기

```cmd
# 명령 프롬프트(CMD) 또는 PowerShell에서 실행

# 필요한 패키지 설치
pip install -r requirements.txt

# 아이콘 생성
python create_icon.py

# EXE 파일 빌드
python build_exe.py
```

실행 후 `dist/수의학강의다운로더.exe` 파일이 생성됩니다!

### 2️⃣ 프로그램 실행

1. `수의학강의다운로더.exe` 더블클릭
2. URL 입력창에 m3u8 링크 붙여넣기
3. "다운로드 시작" 버튼 클릭

### 💡 Tip: EXE 파일 배포

`dist/수의학강의다운로더.exe` 파일만 복사해서 다른 컴퓨터에서도 사용 가능합니다!
(Python 설치 필요 없음)

---

## macOS 사용자

### 1️⃣ 앱 만들기

```bash
# 터미널에서 실행

# 필요한 패키지 설치
pip3 install -r requirements.txt

# 아이콘 생성
python3 create_icon.py

# macOS용 아이콘 변환
iconutil -c icns icon.iconset

# 앱 빌드
python3 build_exe.py
```

실행 후 `dist/수의학강의다운로더.app` 파일이 생성됩니다!

### 2️⃣ 프로그램 실행

1. `수의학강의다운로더.app`을 Applications 폴더로 이동 (선택사항)
2. 앱 아이콘 더블클릭
3. 보안 경고가 나오면:
   - 시스템 환경설정 → 보안 및 개인 정보 보호
   - "확인 없이 열기" 클릭

---

## Linux 사용자

### 1️⃣ 실행 파일 만들기

```bash
# 필요한 패키지 설치
pip3 install -r requirements.txt

# 아이콘 생성
python3 create_icon.py

# 빌드
python3 build_exe.py
```

### 2️⃣ 프로그램 실행

```bash
# 실행 권한 부여
chmod +x dist/수의학강의다운로더

# 실행
./dist/수의학강의다운로더
```

---

## Python 스크립트로 바로 실행 (모든 OS)

실행 파일을 만들지 않고 바로 사용하려면:

```bash
# 1. 필수 패키지만 설치
pip install yt-dlp pillow

# 2. 프로그램 실행
python veterinary_lecture_downloader.py
```

---

## 🎯 m3u8 URL 찾는 방법

### Chrome / Edge / Firefox

1. **F12** 또는 **Ctrl+Shift+I** 눌러서 개발자 도구 열기
2. **Network** 탭 클릭
3. **Media** 또는 **All** 필터 선택
4. 동영상 재생
5. 목록에서 `.m3u8` 파일 찾기
6. 오른쪽 클릭 → **Copy** → **Copy URL**

### Safari (macOS)

1. **개발자용** 메뉴 활성화:
   - 환경설정 → 고급 → "메뉴 막대에서 개발자용 메뉴 보기" 체크
2. **개발자용** → **웹 속성 보기**
3. **네트워크** 탭
4. 동영상 재생
5. `.m3u8` 파일 찾아서 URL 복사

---

## ❓ 자주 묻는 질문

### Q: yt-dlp가 자동으로 설치되나요?
A: 네! 프로그램 실행 시 yt-dlp가 없으면 자동으로 설치를 시도합니다.

### Q: Python이 없어도 실행되나요?
A: 네! 빌드한 EXE/APP 파일은 Python 없이도 실행됩니다.

### Q: 다운로드가 느려요
A: 인터넷 속도에 따라 다릅니다. 화질을 낮추면 더 빠릅니다.

### Q: 에러가 발생했어요
A: 로그 창의 메시지를 확인하고, URL이 올바른지 체크하세요.

---

## 📞 도움이 필요하신가요?

전체 문서는 [README.md](README.md)를 참고하세요!
