import colorsys

import cv2
import math
import os
import random as rnd
import numpy as np

from PIL import Image, ImageDraw, ImageFilter


def gaussian_noise(height: int, width: int) -> Image:
    """
    Create a background with Gaussian noise (to mimic paper)
    """

    # We create an all white image
    image = np.ones((height, width)) * 255

    # We add gaussian noise
    cv2.randn(image, 235, 10)

    return Image.fromarray(image).convert("RGBA")


def plain_white(height: int, width: int) -> Image:
    """
    Create a plain white background
    """

    return Image.new("L", (width, height), 255).convert("RGBA")


def quasicrystal(height: int, width: int) -> Image:
    """
    Create a background with quasicrystal (https://en.wikipedia.org/wiki/Quasicrystal)
    """

    image = Image.new("L", (width, height))
    pixels = image.load()

    frequency = rnd.random() * 30 + 20  # frequency
    phase = rnd.random() * 2 * math.pi  # phase
    rotation_count = rnd.randint(10, 20)  # of rotations

    for kw in range(width):
        y = float(kw) / (width - 1) * 4 * math.pi - 2 * math.pi
        for kh in range(height):
            x = float(kh) / (height - 1) * 4 * math.pi - 2 * math.pi
            z = 0.0
            for i in range(rotation_count):
                r = math.hypot(x, y)
                a = math.atan2(y, x) + i * math.pi * 2.0 / rotation_count
                z += math.cos(r * math.sin(a) * frequency + phase)
            c = int(255 - round(255 * z / rotation_count))
            pixels[kw, kh] = c  # grayscale
    return image.convert("RGBA")


def apply_random_hue(image: Image) -> Image:
    image = image.convert("RGB")

    hsv_image = image.convert("HSV")
    hsv_pixels = hsv_image.load()
    width, height = hsv_image.size

    hue_shift = rnd.randint(0, 255)

    for x in range(width):
        for y in range(height):
            h, s, v = hsv_pixels[x, y]
            if s < 50:
                s = 128
            h = (h + hue_shift) % 256
            hsv_pixels[x, y] = (h, s, v)

    result = hsv_image.convert("RGBA")
    return result



def apply_random_color_segments(image: Image, num_segments: int = 50) -> Image:
    width, height = image.size

    seeds = []
    for _ in range(num_segments):
        sx = rnd.randint(0, width - 1)
        sy = rnd.randint(0, height - 1)
        color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255), 255)
        seeds.append((sx, sy, color))

    overlay = Image.new("RGBA", (width, height))
    overlay_pixels = overlay.load()
    for x in range(width):
        for y in range(height):
            min_dist = float('inf')
            seg_color = (0, 0, 0, 0)
            for sx, sy, color in seeds:
                # 유클리드 거리의 제곱 (비교만 하므로 제곱근 계산은 생략)
                dist = (x - sx) ** 2 + (y - sy) ** 2
                if dist < min_dist:
                    min_dist = dist
                    seg_color = color
            overlay_pixels[x, y] = seg_color

    base = image.convert("RGBA")
    base_pixels = base.load()
    for x in range(width):
        for y in range(height):
            # 원본 이미지의 픽셀 밝기 (그레이스케일 기준)
            base_pixel = base_pixels[x, y]
            brightness = base_pixel[0]  # R값 (0~255)

            # 오버레이의 색상
            oR, oG, oB, oA = overlay_pixels[x, y]
            # 밝기에 비례하여 색상을 조절 (밝기가 낮으면 어둡게, 높으면 원래 색에 가깝게)
            new_color = (
                oR * brightness // 255,
                oG * brightness // 255,
                oB * brightness // 255,
                255
            )
            base_pixels[x, y] = new_color

    return base

def apply_random_straight_line_segments(image: Image, num_lines: int = 3) -> Image:
    width, height = image.size

    # 1. 랜덤 직선 생성
    lines = []
    # 이미지 전체를 덮을 수 있도록 대각선 길이를 기준으로 범위를 잡음
    max_dist = math.sqrt(width**2 + height**2)
    for _ in range(num_lines):
        theta = rnd.uniform(0, math.pi)
        # d는 음수부터 양수까지 선택하여 직선의 위치를 다양하게 함
        d = rnd.uniform(-max_dist/2, max_dist/2)
        lines.append((theta, d))

    # 영역별 색상을 저장할 딕셔너리 (시그니처 -> (R,G,B))
    region_colors = {}

    # 원본 이미지를 RGBA로 변환하여 작업 (쿼시크리스탈 패턴)
    output = image.convert("RGBA")
    output_pixels = output.load()

    # 밝기 정보는 원본 이미지의 그레이스케일 값으로 계산 (쿼시크리스탈은 그레이스케일 생성)
    grayscale = image.convert("L")
    gray_pixels = grayscale.load()

    # 각 픽셀마다 직선들에 대한 부호를 계산하여 영역 결정
    for x in range(width):
        for y in range(height):
            signature = []
            for theta, d in lines:
                # 좌표 (x, y)에 대해 직선의 결정 함수: x*cos(theta) + y*sin(theta) - d
                # 값이 0 이상이면 1, 미만이면 0
                if x * math.cos(theta) + y * math.sin(theta) - d >= 0:
                    signature.append(1)
                else:
                    signature.append(0)
            signature = tuple(signature)
            # 해당 영역에 아직 색상이 할당되지 않았다면 랜덤 색상을 생성
            if signature not in region_colors:
                region_colors[signature] = (
                    rnd.randint(0, 255),
                    rnd.randint(0, 255),
                    rnd.randint(0, 255)
                )
            r, g, b = region_colors[signature]
            # 원본 픽셀의 밝기를 구함 (0~255)
            brightness = gray_pixels[x, y]
            # 밝기에 비례하도록 색상을 모듈레이션 (밝기가 낮으면 어둡게, 높으면 원래 색에 가깝게)
            mod_r = r * brightness // 255
            mod_g = g * brightness // 255
            mod_b = b * brightness // 255

            # RGB (0~255)를 0~1 범위로 변환 후 HSV로 변환
            h, s, v = colorsys.rgb_to_hsv(mod_r/255.0, mod_g/255.0, mod_b/255.0)

            # 채도를 더욱 낮추고 명도를 높이기 위한 조절 값
            sat_factor = 0.3       # 채도를 30%로 낮춤 (원래 50%였던 값을 더 낮춤)
            brightness_increase = 0.05  # 명도를 0.2만큼 증가

            s = s * sat_factor
            v = min(1, v + brightness_increase)

            # 다시 HSV를 RGB로 변환 (0~1 범위를 0~255 범위로)
            new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, v)
            new_color = (int(new_r * 255), int(new_g * 255), int(new_b * 255), 255)

            output_pixels[x, y] = new_color

    return output


def image(height: int, width: int, image_dir: str) -> Image:
    """
    Create a background with a image
    """
    images = os.listdir(image_dir)

    if len(images) > 0:
        pic = Image.open(
            os.path.join(image_dir, images[rnd.randint(0, len(images) - 1)])
        )

        if pic.size[0] < width:
            pic = pic.resize(
                [width, int(pic.size[1] * (width / pic.size[0]))],
                Image.Resampling.LANCZOS,
            )
        if pic.size[1] < height:
            pic = pic.resize(
                [int(pic.size[0] * (height / pic.size[1])), height],
                Image.Resampling.LANCZOS,
            )

        if pic.size[0] == width:
            x = 0
        else:
            x = rnd.randint(0, pic.size[0] - width)
        if pic.size[1] == height:
            y = 0
        else:
            y = rnd.randint(0, pic.size[1] - height)

        return pic.crop((x, y, x + width, y + height))
    else:
        raise Exception("No images where found in the images folder!")
