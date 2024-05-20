import pygame

# pygame에 있는 데이터 초기화
pygame.init()

# set_mode() 리턴타입이 surface
screen_surf = pygame.display.set_mode((1280, 720))
game_over_msg = pygame.font.Font(None, 64)
# screen_surf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# 이미지 가져오기
ship_img = pygame.image.load('0517_alien_invasion/images/ship.bmp')
alien_img = pygame.image.load('0517_alien_invasion/images/alien.bmp')
# 이미지가 표시될 위치
# ship_rect 의 위치를 전체 스크린의 중간 바텀에 위치시킴
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

# alien_rect = pygame.rect.Rect(200, 200, 200, 200)

# aliens = []
# for i in range(5):
#     alien = pygame.rect.Rect(100+200*i, 100, 100, 100)
#     aliens.append(alien)
    # alien2 = pygame.rect.Rect(100+200, 100, 100, 100)
    # alien3 = pygame.rect.Rect(100+400, 100, 100, 100)
# aliens = [alien1, alien2]

aliens = []
alien_rect = alien_img.get_rect()
alien_x_pos = alien_rect.width
alien_y_pos = alien_rect.height

for _ in range(10):
    alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                            alien_rect.width,\
                            alien_rect.height)
    alien_x_pos += alien_rect.width * 2
    aliens.append(alien)

bullet_rect = None
bullets = []

clock = pygame.time.Clock()

right_pressed = False
left_pressed = False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False
is_running = True
# up_pressed = False
# down_pressed = False

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
                # 총알 발사, 연속으로 5개 이하 발사
                if len(bullets) < 5:
                    bullet_rect = pygame.rect.Rect(0, 0, 500, 10)
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect)
            elif event.key == pygame.K_q:
                pygame.quit()
                raise SystemExit
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                ship_rect.y = ship_rect.y - 10
                alien_rect.y = alien_rect.y - 20
            elif event.key == pygame.K_DOWN:
                ship_rect.y = ship_rect.y + 10
                alien_rect.y = alien_rect.y + 20

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False 
            # elif event.key == pygame.K_UP:
            #     up_pressed = False 
            # elif event.key == pygame.K_DOWN:
            #     down_pressed = False

    # 이벤트 업데이트
    # Do logical updates here.
    if is_running:
        if right_pressed:
            screen_rect = screen_surf.get_rect()
            # 화면의 전체 길이 - 우주선 길이 = 우주선의 x축 범위
            if ship_rect.x < screen_rect.width-ship_rect.width:
                ship_rect.x = ship_rect.x + 10
            # 화면의 전체 길이 - 외계인 길이 = 외계인의 x축 범위
            if alien_rect.x < screen_rect.width-alien_rect.width:
                alien_rect.x = alien_rect.x + 20

        if left_pressed:
            if 0 < ship_rect.x:
                ship_rect.x = ship_rect.x - 10
            if 0 < alien_rect.x:
                alien_rect.x = alien_rect.x - 20

        # if up_pressed:
        #     ship_rect.y = ship_rect.y - 10
        #     alien_rect.y = alien_rect.y - 20

        # if down_pressed:
        #     ship_rect.y = ship_rect.y + 10
        #     alien_rect.y = alien_rect.y + 20


        # 외계인들 자동 움직이기
        if aliens:
            screen_rect = screen_surf.get_rect()
            for alien in aliens:
                if screen_rect.width - alien.width < alien.x:
                    alien_x_direction = -1
                    alien_x_direction_changed = True
                    break
                elif alien.x < screen_rect.x:
                    alien_x_direction = 1
                    alien_x_direction_changed = True
                    break

            for alien in aliens:
                print(alien.y, alien_y_pos)
                alien.x += alien_x_direction * 2
                if alien_x_direction_changed:
                    alien.y += alien_img.get_rect().height
    
        alien_x_direction_changed = False

        if bullets:
            screen_rect = screen_surf.get_rect()

            for bullet in bullets:
                if bullet.y < 0:
                    bullets.remove(bullet)

            for bullet in bullets:
                bullet.y = bullet.y - 10

        for alien in aliens:
            for bullet in bullets:
                if pygame.rect.Rect.colliderect(alien, bullet):
                    aliens.remove(alien)
                    bullets.remove(bullet)
        
        if len(aliens) == 0:
            print('Game Over!')
            is_running = False

    # 색상 채우기 RGB
    screen_surf.fill('white')  # Fill the display with a solid color
    game_over_msg.render('Game Over!', True, (0,0,0))

    # Render the graphics here .
    # 화면에 이미지를 출력
    screen_surf.blit(ship_img, ship_rect)
    # screen_surf.blit(alien_img, alien_rect)
    if aliens:
        for alien in aliens:
            screen_surf.blit(alien_img, alien)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet)

    pygame.display.flip()  # Refresh on-screen display
    # 프레임 수(초당 60번 반복)
    clock.tick(60)         # wait until next frame (at 60 FPS)

