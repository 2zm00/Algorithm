from PIL import Image, ImageDraw, ImageFont

# 이미지 크기 및 배경 설정
image_width = 400
image_height = 400
background_color = "lightblue"

# 이미지 생성
image = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# 캐릭터 이미지 추가
character_image_path = "character_image.png"  # 여기에 원하는 캐릭터 이미지 파일 경로 입력
character_image = Image.open(character_image_path)
character_image = character_image.resize((200, 200))  # 이미지 크기 조정
image.paste(character_image, (100, 100))  # 캐릭터 이미지를 중앙에 추가 (좌표 조정 필요)

# 이미지 저장
image.save("zmo_profile_image.png")

# 이미지 표시 (옵션)
image.show()us