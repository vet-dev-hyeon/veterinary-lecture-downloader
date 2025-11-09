# 🎓 수의학 강의 다운로더 (Veterinary Lecture Downloader)

수의학 강의 동영상을 쉽게 다운로드할 수 있는 GUI 애플리케이션입니다.

## ✨ 주요 기능

- 🖱️ **사용하기 쉬운 GUI** - 클릭 몇 번으로 간편하게 다운로드
- 🎥 **HLS 스트림 지원** - m3u8 형식의 스트리밍 동영상 다운로드
- ⚙️ **자동 설치** - yt-dlp가 없으면 자동으로 설치
- 📊 **실시간 진행 상태** - 다운로드 진행 상황 실시간 확인
- 🎨 **화질 선택** - 최고 화질부터 저화질까지 선택 가능
- 💾 **저장 경로 설정** - 원하는 위치에 파일 저장

## 📦 설치 방법

### 방법 1: 실행 파일 사용 (권장)

Python이 설치되어 있지 않아도 사용할 수 있습니다.

#### Windows
1. `dist/수의학강의다운로더.exe` 파일을 다운로드
2. 실행 파일을 더블클릭하여 실행
3. Windows Defender가 경고할 경우 "추가 정보" → "실행" 클릭

#### macOS
1. `dist/수의학강의다운로더.app` 파일을 다운로드
2. Applications 폴더로 이동 (선택사항)
3. 앱을 더블클릭하여 실행
4. "확인되지 않은 개발자" 경고가 나오면:
   - 시스템 환경설정 → 보안 및 개인 정보 보호 → "확인 없이 열기" 클릭

### 방법 2: Python 스크립트로 실행

Python 3.7 이상이 설치되어 있어야 합니다.

```bash
# 1. 필요한 패키지 설치
pip install -r requirements.txt

# 2. 프로그램 실행
python veterinary_lecture_downloader.py
```

## 🔨 실행 파일 빌드 방법

직접 실행 파일을 만들고 싶다면:

### Windows에서 빌드

```bash
# 1. 필요한 패키지 설치
pip install -r requirements.txt

# 2. 아이콘 생성
python create_icon.py

# 3. 실행 파일 빌드
python build_exe.py
```

빌드 완료 후 `dist/수의학강의다운로더.exe` 파일이 생성됩니다.

### macOS에서 빌드

```bash
# 1. 필요한 패키지 설치
pip3 install -r requirements.txt

# 2. 아이콘 생성
python3 create_icon.py

# 3. macOS용 아이콘 변환
iconutil -c icns icon.iconset

# 4. 실행 파일 빌드
python3 build_exe.py
```

빌드 완료 후 `dist/수의학강의다운로더.app` 파일이 생성됩니다.

### Linux에서 빌드

```bash
# 1. 필요한 패키지 설치
pip3 install -r requirements.txt

# 2. 아이콘 생성
python3 create_icon.py

# 3. 실행 파일 빌드
python3 build_exe.py
```

빌드 완료 후 `dist/수의학강의다운로더` 파일이 생성됩니다.

## 📖 사용 방법

### 1. m3u8 URL 찾기

브라우저에서 동영상을 재생한 후:

1. **개발자 도구 열기** (F12 또는 Ctrl+Shift+I)
2. **Network 탭** 선택
3. **Media 또는 All** 필터 선택
4. 동영상 재생
5. `.m3u8` 파일 찾기
6. URL 복사

### 2. 다운로드

1. 프로그램 실행
2. m3u8 URL을 "강의 URL" 필드에 붙여넣기
3. 저장 경로 선택 (기본값: `사용자/Downloads/수의학강의`)
4. 파일명 설정 (선택사항)
5. 화질 선택
6. **"다운로드 시작"** 버튼 클릭
7. 완료될 때까지 대기

## 🎬 지원 형식

- ✅ HLS 스트림 (m3u8)
- ✅ 일반 동영상 URL (mp4, mkv 등)
- ✅ 암호화된 HLS 스트림 (AES-128)
- ✅ YouTube, Vimeo 등 주요 플랫폼

## ⚠️ 주의사항

1. **저작권 준수**: 본인이 시청 권한이 있는 콘텐츠만 다운로드하세요
2. **네트워크 속도**: 다운로드 속도는 인터넷 속도에 따라 달라집니다
3. **디스크 공간**: 충분한 저장 공간이 있는지 확인하세요
4. **방화벽**: 일부 방화벽에서 차단될 수 있습니다

## 🔧 문제 해결

### 로그 파일 확인
프로그램 실행 시 자동으로 로그 파일이 생성됩니다:
- **위치**: EXE 파일과 같은 디렉토리
- **파일명**: `veterinary_downloader_YYYYMMDD.log`
- **내용**: 모든 실행 기록, 오류 메시지, 다운로드 상태

문제 발생 시 이 로그 파일을 확인하면 원인을 파악할 수 있습니다.

### yt-dlp 설치 실패
수동으로 설치:
```bash
pip install yt-dlp
# 또는
pipx install yt-dlp
```

### 다운로드 실패
1. URL이 정확한지 확인
2. 인터넷 연결 확인
3. **로그 파일 확인** (`veterinary_downloader_*.log`)
4. 로그에 표시된 오류 메시지 확인
5. yt-dlp 업데이트:
   ```bash
   pip install --upgrade yt-dlp
   ```

### Windows Defender 경고
- 서명되지 않은 exe 파일이므로 경고가 표시될 수 있습니다
- "추가 정보" → "실행"을 클릭하여 실행할 수 있습니다
- 또는 Python 스크립트로 직접 실행하세요

## 📁 파일 구조

```
.
├── veterinary_lecture_downloader.py  # 메인 프로그램
├── create_icon.py                    # 아이콘 생성 스크립트
├── build_exe.py                      # 실행 파일 빌드 스크립트
├── requirements.txt                  # Python 패키지 의존성
├── icon.ico                          # Windows 아이콘
├── icon.png                          # PNG 아이콘
├── icon.iconset/                     # macOS 아이콘 세트
├── README.md                         # 이 파일
└── dist/                            # 빌드된 실행 파일 (빌드 후 생성)
    ├── 수의학강의다운로더.exe        # Windows 실행 파일
    └── 수의학강의다운로더.app        # macOS 앱 번들
```

## 🛠️ 기술 스택

- **Python 3.7+** - 프로그래밍 언어
- **tkinter** - GUI 프레임워크
- **yt-dlp** - 동영상 다운로드 엔진
- **Pillow** - 아이콘 생성
- **PyInstaller** - 실행 파일 패키징

## 📝 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 🙋 지원

문제가 발생하거나 개선 사항이 있다면 이슈를 등록해주세요.

---

**Made with ❤️ for Veterinary Students**
