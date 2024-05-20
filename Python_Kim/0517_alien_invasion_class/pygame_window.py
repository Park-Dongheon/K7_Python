import pygame

# pygame에 있는 데이터 초기화
pygame.init()

def init():
    # set_mode() 리턴타입이 surface
    screen_surf = pygame.display.set_mode((1280, 720))
    return screen_surf

def create_ship(screen_surf):
    global ship_img
    # 이미지가 표시될 위치
    # ship_rect 의 위치를 전체 스크린의 중간 바텀에 위치시킴
    ship_rect = ship_img.get_rect()
    ship_rect.midbottom = screen_surf.get_rect().midbottom

    return ship_rect

def create_alien():
    global alien_img

    alien_rect = alien_img.get_rect()
    alien_x_pos = alien_rect.width
    alien_y_pos = alien_rect.height

    aliens = []
    for _ in range(10):
        alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                                alien_rect.width,\
                                alien_rect.height)
        alien_x_pos += alien_rect.width * 2
        aliens.append(alien)

    return aliens

def create_bullet():
    global ship_rect
    global bullets
    bullet_rect = pygame.rect.Rect(0, 0, 500, 10)
    bullet_rect.midbottom = ship_rect.midtop
    bullets.append(bullet_rect)

def handle_event():
    global ship_rect
    global bullets
    global left_pressed, right_pressed
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
                    create_bullet()
            elif event.key == pygame.K_q:
                pygame.quit()
                raise SystemExit
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                ship_rect.y = ship_rect.y - 10
            elif event.key == pygame.K_DOWN:
                ship_rect.y = ship_rect.y + 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False

    # return left_pressed, right_pressed

def update_object(screen_surf):
    global ship_rect
    global bullets, aliens, alien_img
    global left_pressed, right_pressed
    global alien_x_direction, alien_x_direction_changed
    if right_pressed:
        screen_rect = screen_surf.get_rect()
        # 화면의 전체 길이 - 우주선 길이 = 우주선의 x축 범위
        if ship_rect.x < screen_rect.width-ship_rect.width:
            ship_rect.x = ship_rect.x + 10

    if left_pressed:
        if 0 < ship_rect.x:
            ship_rect.x = ship_rect.x - 10

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

def render_object(screen_surf):
    global ship_img, ship_rect
    global aliens, bullets, alien_img
    # 색상 채우기 RGB
    screen_surf.fill('white')  # Fill the display with a solid color

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


screen_surf = init()

# 이미지 가져오기
ship_img = pygame.image.load('0517_alien_invasion/images/ship.bmp')
alien_img = pygame.image.load('0517_alien_invasion/images/alien.bmp')

ship_rect = create_ship(screen_surf)
aliens = create_alien()

bullet_rect = None
bullets = []

clock = pygame.time.Clock()

right_pressed = False
left_pressed = False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False
is_running = True

# 무한루프
while True:
    # Process player inputs.
    handle_event()
    update_object(screen_surf)
    render_object(screen_surf)

    pygame.display.flip()  # Refresh on-screen display
    # 프레임 수(초당 60번 반복)
    clock.tick(60)         # wait until next frame (at 60 FPS)

    # if len(aliens) == 0:
    #     print('Game Over!')
    #     is_running = False
       
    #game_over_msg.render('Game Over!', True, (0, 0, 0))

