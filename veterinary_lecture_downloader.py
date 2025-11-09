#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
수의학 강의 다운로더 (Veterinary Lecture Downloader)
"""

import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
import platform

class VeterinaryLectureDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("수의학 강의 다운로더")
        self.root.geometry("700x550")
        self.root.resizable(True, True)

        # 기본 다운로드 경로 설정
        self.default_download_path = str(Path.home() / "Downloads" / "수의학강의")

        # UI 생성
        self.create_widgets()

        # yt-dlp 확인
        self.check_ytdlp()

    def create_widgets(self):
        # 메인 프레임
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 그리드 가중치 설정
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # 제목
        title_label = ttk.Label(main_frame, text="🎓 수의학 강의 다운로더",
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # URL 입력
        ttk.Label(main_frame, text="강의 URL:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, width=60)
        self.url_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # URL 예시 힌트
        hint_label = ttk.Label(main_frame, text="(m3u8 스트림 URL을 입력하세요)",
                              font=('Arial', 8), foreground='gray')
        hint_label.grid(row=2, column=1, columnspan=2, sticky=tk.W)

        # 저장 경로
        ttk.Label(main_frame, text="저장 경로:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.path_entry = ttk.Entry(main_frame, width=50)
        self.path_entry.insert(0, self.default_download_path)
        self.path_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)

        browse_btn = ttk.Button(main_frame, text="찾아보기", command=self.browse_folder)
        browse_btn.grid(row=3, column=2, padx=(5, 0), pady=5)

        # 파일명
        ttk.Label(main_frame, text="파일명:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.filename_entry = ttk.Entry(main_frame, width=60)
        self.filename_entry.insert(0, "lecture_%(id)s.%(ext)s")
        self.filename_entry.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # 옵션 프레임
        options_frame = ttk.LabelFrame(main_frame, text="다운로드 옵션", padding="10")
        options_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        options_frame.columnconfigure(0, weight=1)

        # 화질 선택
        quality_frame = ttk.Frame(options_frame)
        quality_frame.grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Label(quality_frame, text="화질:").pack(side=tk.LEFT, padx=(0, 10))

        self.quality_var = tk.StringVar(value="best")
        qualities = [("최고 화질", "best"), ("고화질 (1080p)", "1080"),
                    ("중간 화질 (720p)", "720"), ("저화질 (480p)", "480")]
        for text, value in qualities:
            ttk.Radiobutton(quality_frame, text=text, variable=self.quality_var,
                           value=value).pack(side=tk.LEFT, padx=5)

        # 다운로드 버튼
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)

        self.download_btn = ttk.Button(button_frame, text="⬇ 다운로드 시작",
                                       command=self.start_download,
                                       style='Accent.TButton')
        self.download_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(button_frame, text="⏹ 중지",
                                   command=self.stop_download, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # 진행 상태
        ttk.Label(main_frame, text="진행 상태:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # 로그 출력
        ttk.Label(main_frame, text="로그:").grid(row=8, column=0, sticky=(tk.W, tk.N), pady=5)
        self.log_text = scrolledtext.ScrolledText(main_frame, height=12, width=70)
        self.log_text.grid(row=8, column=1, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        main_frame.rowconfigure(8, weight=1)

        # 하단 상태바
        self.status_label = ttk.Label(main_frame, text="준비 완료", relief=tk.SUNKEN)
        self.status_label.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))

        # 다운로드 프로세스
        self.download_process = None

    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.path_entry.get())
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def log(self, message):
        """로그 메시지 추가"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def check_ytdlp(self):
        """yt-dlp 설치 여부 확인 및 자동 설치"""
        self.log("yt-dlp 확인 중...")

        try:
            # yt-dlp 버전 확인
            result = subprocess.run(['yt-dlp', '--version'],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip()
                self.log(f"✓ yt-dlp 발견: 버전 {version}")
                self.status_label.config(text=f"yt-dlp 버전 {version} 준비 완료")
                return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        # yt-dlp가 없으면 설치 시도
        self.log("yt-dlp가 설치되어 있지 않습니다. 자동 설치를 시작합니다...")
        self.status_label.config(text="yt-dlp 설치 중...")

        if self.install_ytdlp():
            self.log("✓ yt-dlp 설치 완료!")
            self.status_label.config(text="yt-dlp 설치 완료 - 준비 완료")
            return True
        else:
            self.log("✗ yt-dlp 설치 실패. 수동으로 설치해주세요.")
            self.status_label.config(text="yt-dlp 설치 필요")
            messagebox.showwarning("설치 필요",
                "yt-dlp 설치에 실패했습니다.\n\n"
                "다음 방법 중 하나로 설치해주세요:\n"
                "1. pip install yt-dlp\n"
                "2. https://github.com/yt-dlp/yt-dlp/releases 에서 다운로드")
            return False

    def install_ytdlp(self):
        """yt-dlp 자동 설치"""
        try:
            # pip로 설치 시도
            self.log("pip를 사용하여 yt-dlp 설치 중...")
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'],
                                  capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return True

            # pipx 시도
            self.log("pipx를 사용하여 yt-dlp 설치 시도 중...")
            result = subprocess.run(['pipx', 'install', 'yt-dlp'],
                                  capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return True

        except Exception as e:
            self.log(f"설치 오류: {str(e)}")

        return False

    def start_download(self):
        """다운로드 시작"""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("입력 오류", "URL을 입력해주세요.")
            return

        save_path = self.path_entry.get().strip()
        if not save_path:
            messagebox.showwarning("입력 오류", "저장 경로를 입력해주세요.")
            return

        # 저장 경로 생성
        os.makedirs(save_path, exist_ok=True)

        filename = self.filename_entry.get().strip()
        output_template = os.path.join(save_path, filename)

        # UI 업데이트
        self.download_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress.start()
        self.log(f"\n{'='*50}")
        self.log(f"다운로드 시작: {url}")
        self.log(f"저장 위치: {save_path}")
        self.status_label.config(text="다운로드 중...")

        # 별도 스레드에서 다운로드
        download_thread = threading.Thread(
            target=self.download_video,
            args=(url, output_template),
            daemon=True
        )
        download_thread.start()

    def download_video(self, url, output_template):
        """실제 다운로드 실행"""
        try:
            # yt-dlp 명령어 구성
            quality = self.quality_var.get()

            cmd = ['yt-dlp']

            # 화질 설정
            if quality == 'best':
                cmd.extend(['-f', 'bestvideo+bestaudio/best'])
            else:
                cmd.extend(['-f', f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'])

            # 출력 템플릿
            cmd.extend(['-o', output_template])

            # 진행 상태 표시
            cmd.append('--newline')

            # URL
            cmd.append(url)

            self.log(f"실행 명령: {' '.join(cmd)}")

            # 다운로드 실행
            self.download_process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            # 출력 로그 실시간 표시
            for line in self.download_process.stdout:
                self.log(line.strip())

            self.download_process.wait()

            if self.download_process.returncode == 0:
                self.log("✓ 다운로드 완료!")
                self.root.after(0, lambda: messagebox.showinfo("완료", "다운로드가 완료되었습니다!"))
                self.root.after(0, lambda: self.status_label.config(text="다운로드 완료"))
            else:
                self.log(f"✗ 다운로드 실패 (종료 코드: {self.download_process.returncode})")
                self.root.after(0, lambda: messagebox.showerror("오류", "다운로드 중 오류가 발생했습니다."))
                self.root.after(0, lambda: self.status_label.config(text="다운로드 실패"))

        except Exception as e:
            self.log(f"✗ 오류 발생: {str(e)}")
            self.root.after(0, lambda: messagebox.showerror("오류", f"오류가 발생했습니다:\n{str(e)}"))
            self.root.after(0, lambda: self.status_label.config(text="오류 발생"))
        finally:
            self.root.after(0, self.download_finished)

    def stop_download(self):
        """다운로드 중지"""
        if self.download_process and self.download_process.poll() is None:
            self.download_process.terminate()
            self.log("다운로드가 중지되었습니다.")
            self.status_label.config(text="다운로드 중지됨")
            self.download_finished()

    def download_finished(self):
        """다운로드 종료 후 UI 업데이트"""
        self.download_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.progress.stop()
        self.download_process = None


def main():
    root = tk.Tk()

    # 아이콘 설정 (실행 파일에 포함된 경우)
    try:
        if getattr(sys, 'frozen', False):
            # PyInstaller로 패키징된 경우
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, 'icon.ico')
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except:
        pass

    app = VeterinaryLectureDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
