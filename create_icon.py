#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
아이콘 생성 스크립트
수의학 강의 다운로더 아이콘 생성
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """수의학 강의 다운로더 아이콘 생성"""

    # 여러 크기의 아이콘 생성 (Windows ICO 표준)
    sizes = [256, 128, 64, 48, 32, 16]
    images = []

    for size in sizes:
        # 새 이미지 생성 (RGBA)
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # 배경 원 (파란색 그라데이션)
        margin = max(2, size // 20)
        draw.ellipse([margin, margin, size-margin, size-margin],
                    fill=(41, 128, 185, 255),
                    outline=(52, 152, 219, 255),
                    width=max(1, size // 40))

        # 십자가 그리기 (수의학 상징)
        cross_width = max(2, size // 10)
        cross_length = size // 3
        center = size // 2

        # 수직선
        draw.rectangle([center - cross_width//2, center - cross_length,
                       center + cross_width//2, center + cross_length],
                      fill=(255, 255, 255, 255))

        # 수평선
        draw.rectangle([center - cross_length, center - cross_width//2,
                       center + cross_length, center + cross_width//2],
                      fill=(255, 255, 255, 255))

        # 하단에 다운로드 화살표
        arrow_size = size // 6
        arrow_y = size - size // 4
        arrow_x = center
        arrow_width = max(1, size // 30)

        # 화살표 몸통
        draw.rectangle([arrow_x - arrow_width, arrow_y - arrow_size,
                       arrow_x + arrow_width, arrow_y],
                      fill=(46, 204, 113, 255))

        # 화살표 머리 (삼각형)
        arrow_head_size = arrow_size // 2
        points = [
            (arrow_x, arrow_y + arrow_head_size),  # 아래 점
            (arrow_x - arrow_head_size, arrow_y),  # 왼쪽 위
            (arrow_x + arrow_head_size, arrow_y),  # 오른쪽 위
        ]
        draw.polygon(points, fill=(46, 204, 113, 255))

        images.append(img)

    # ICO 파일로 저장 (모든 크기 포함)
    images[0].save('icon.ico', format='ICO', sizes=[(s, s) for s in sizes])
    print(f"✓ icon.ico 생성 완료 (크기: {', '.join(map(str, sizes))})")

    # PNG도 저장 (256x256)
    images[0].save('icon.png', format='PNG')
    print(f"✓ icon.png 생성 완료 (256x256)")

    # macOS용 ICNS 파일 생성을 위한 개별 PNG 파일들 생성
    icon_dir = 'icon.iconset'
    if not os.path.exists(icon_dir):
        os.makedirs(icon_dir)

    # macOS iconset 표준 크기
    mac_sizes = {
        16: 'icon_16x16.png',
        32: ['icon_16x16@2x.png', 'icon_32x32.png'],
        64: 'icon_32x32@2x.png',
        128: 'icon_128x128.png',
        256: ['icon_128x128@2x.png', 'icon_256x256.png'],
        512: ['icon_256x256@2x.png', 'icon_512x512.png'],
        1024: 'icon_512x512@2x.png'
    }

    for size in [16, 32, 64, 128, 256, 512, 1024]:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # 배경 원
        margin = max(2, size // 20)
        draw.ellipse([margin, margin, size-margin, size-margin],
                    fill=(41, 128, 185, 255),
                    outline=(52, 152, 219, 255),
                    width=max(1, size // 40))

        # 십자가
        cross_width = max(2, size // 10)
        cross_length = size // 3
        center = size // 2
        draw.rectangle([center - cross_width//2, center - cross_length,
                       center + cross_width//2, center + cross_length],
                      fill=(255, 255, 255, 255))
        draw.rectangle([center - cross_length, center - cross_width//2,
                       center + cross_length, center + cross_width//2],
                      fill=(255, 255, 255, 255))

        # 다운로드 화살표
        arrow_size = size // 6
        arrow_y = size - size // 4
        arrow_x = center
        arrow_width = max(1, size // 30)
        draw.rectangle([arrow_x - arrow_width, arrow_y - arrow_size,
                       arrow_x + arrow_width, arrow_y],
                      fill=(46, 204, 113, 255))
        arrow_head_size = arrow_size // 2
        points = [
            (arrow_x, arrow_y + arrow_head_size),
            (arrow_x - arrow_head_size, arrow_y),
            (arrow_x + arrow_head_size, arrow_y),
        ]
        draw.polygon(points, fill=(46, 204, 113, 255))

        # 저장
        if size in mac_sizes:
            filenames = mac_sizes[size]
            if isinstance(filenames, str):
                filenames = [filenames]
            for filename in filenames:
                img.save(os.path.join(icon_dir, filename), format='PNG')

    print(f"✓ macOS iconset 생성 완료 ({icon_dir}/)")
    print(f"\nmacOS에서 .icns 파일 생성 방법:")
    print(f"  iconutil -c icns icon.iconset")

if __name__ == '__main__':
    create_icon()
    print("\n아이콘 생성이 완료되었습니다!")
