
import pygame

# pygame에 있는 데이터 초기화
pygame.init()

#set_mode() 리턴타입이 surface
screen_surf = pygame.display.set_mode((1280,720))
# 이미지 가져오기
ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')
# 이미지가 표시될 위치
# ship_rect 의 위치를 전체 스크린의 중간 바텀에 위치시킴
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom
alien_rect = pygame.rect.Rect(200, 200, 200, 200)


bullet_rect = None
bullets = []

clock = pygame.time.Clock()

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False


# 무한루프
while True:
    # Process player inputs.
    # 이벤트 동작을 처리 하도록 큐 형태로 저장
    for event in pygame.event.get():
        # 이벤트가 정지될 경우
        if event.type == pygame.QUIT:
            pygame.quit()
            # 예외 발생시켜 강제로 종료
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알 발사
                bullet_rect = pygame.rect.Rect(0, 0, 5, 6)
                bullet_rect.midbottom = ship_rect.midtop
                bullets.append(bullet_rect)
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False 
            elif event.key == pygame.K_UP:
                up_pressed = False 
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    # 이벤트 업데이트
    # Do logical updates here.
    if right_pressed:
        ship_rect.x = ship_rect.x + 5
        alien_rect.x = alien_rect.x + 6

    if left_pressed:
        ship_rect.x = ship_rect.x - 5
        alien_rect.x = alien_rect.x - 6

    if up_pressed:
        ship_rect.y = ship_rect.y - 5
        alien_rect.y = alien_rect.y - 6

    if down_pressed:
        ship_rect.y = ship_rect.y + 5
        alien_rect.y = alien_rect.y + 6

    if bullets:
        for bullet in bullets:
            bullet.y = bullet.y - 4

    # 색상 채우기 RGB
    screen_surf.fill('white')  # Fill the display with a solid color

    # Render the graphics here .
    # 화면에 이미지를 출력
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
        for bullet in bullets: 
            pygame.draw.rect(screen_surf, 'red', bullet)

    pygame.display.flip()  # Refresh on-screen display
    # 프레임 수(초당 60번 반복)
    clock.tick(60)         # wait until next frame (at 60 FPS)
    