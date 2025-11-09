#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
수의학 강의 다운로더 실행 파일 빌드 스크립트
PyInstaller를 사용하여 Windows/Mac 실행 파일 생성
"""

import subprocess
import sys
import os
import platform

# Windows 콘솔 인코딩 문제 해결
if platform.system() == 'Windows':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def build_executable():
    """실행 파일 빌드"""

    print("=" * 60)
    print("수의학 강의 다운로더 - 실행 파일 빌드")
    print("=" * 60)

    # PyInstaller 설치 확인
    try:
        import PyInstaller
        print(f"✓ PyInstaller {PyInstaller.__version__} 발견")
    except ImportError:
        print("PyInstaller를 설치하는 중...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
        print("✓ PyInstaller 설치 완료")

    # yt-dlp 및 pycryptodomex 설치 확인
    print("필요한 패키지 설치 중...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'yt-dlp', 'pycryptodomex'],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✓ yt-dlp, pycryptodomex 설치 완료")
    except:
        pass

    # 아이콘 파일 확인
    icon_file = 'icon.ico' if platform.system() == 'Windows' else 'icon.icns'
    if not os.path.exists(icon_file):
        if platform.system() == 'Windows' and not os.path.exists('icon.ico'):
            print("⚠ icon.ico 파일이 없습니다. 먼저 create_icon.py를 실행하세요.")
        elif platform.system() == 'Darwin' and not os.path.exists('icon.icns'):
            print("⚠ icon.icns 파일이 없습니다.")
            print("  다음 명령으로 생성하세요: iconutil -c icns icon.iconset")
        icon_file = None

    # PyInstaller 명령어 구성
    cmd = [
        'pyinstaller',
        '--name=수의학강의다운로더',
        '--onefile',  # 단일 실행 파일로 생성
        '--windowed',  # GUI 모드 (콘솔 창 숨김)
        '--clean',
    ]

    # 아이콘 추가
    if icon_file and os.path.exists(icon_file):
        cmd.append(f'--icon={icon_file}')
        print(f"✓ 아이콘 파일: {icon_file}")

    # 메타데이터 추가 (Windows)
    if platform.system() == 'Windows':
        cmd.extend([
            '--version-file=version_info.txt',
        ])

    # yt-dlp와 Cryptodome을 포함시키기 위한 hidden import
    cmd.extend([
        '--hidden-import=yt_dlp',
        '--collect-all=yt_dlp',
        '--hidden-import=Cryptodome',
        '--hidden-import=Cryptodome.Cipher',
        '--hidden-import=Cryptodome.Cipher.AES',
        '--collect-all=Cryptodome',
    ])

    # 메인 스크립트
    cmd.append('veterinary_lecture_downloader.py')

    print("\n빌드 명령:")
    print(' '.join(cmd))
    print("\n빌드를 시작합니다...")

    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 60)
        print("✓ 빌드 완료!")
        print("=" * 60)

        if platform.system() == 'Windows':
            exe_path = os.path.join('dist', '수의학강의다운로더.exe')
            print(f"\n실행 파일 위치: {os.path.abspath(exe_path)}")
        elif platform.system() == 'Darwin':
            app_path = os.path.join('dist', '수의학강의다운로더.app')
            print(f"\n애플리케이션 위치: {os.path.abspath(app_path)}")
        else:
            bin_path = os.path.join('dist', '수의학강의다운로더')
            print(f"\n실행 파일 위치: {os.path.abspath(bin_path)}")

        print("\n실행 파일을 테스트해보세요!")

    except subprocess.CalledProcessError as e:
        print(f"\n✗ 빌드 실패: {e}")
        sys.exit(1)


def create_version_info():
    """Windows용 버전 정보 파일 생성"""
    if platform.system() != 'Windows':
        return

    version_info = """# UTF-8
#
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u''),
        StringStruct(u'FileDescription', u'수의학 강의 다운로더'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'veterinary_lecture_downloader'),
        StringStruct(u'LegalCopyright', u''),
        StringStruct(u'OriginalFilename', u'수의학강의다운로더.exe'),
        StringStruct(u'ProductName', u'수의학 강의 다운로더'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""

    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_info)

    print("✓ Windows 버전 정보 파일 생성 완료")


if __name__ == '__main__':
    create_version_info()
    build_executable()
