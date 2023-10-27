import pygame
import random
import pygame.mixer
import pyautogui
# Oyun ekranı boyutları
screen_width = 800
screen_height = 600

# Renk tanımları
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Pencereyi oluştur
pygame.init()
pygame.mixer.init()



# Pencere oluşturma
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platform Oyunu")
# pencere modunda çalıştırma

pencere_modu = True






# Müzik dosyasının yolu
pygame.mixer.music.load("yt1s.com - Undertale OST 002  Start Menu.mp3")
pygame.mixer.music.play(-1)



# Oyuncu özellikleri
player_width = 50
player_height = 50
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height
player_x_change = 0
player_y_change = 0
player_gravity = 1
player_x=50
player_y=150

# Platform 1 özellikleri
platform_width = 100
platform_height = 20
platform_x =200
platform_y = 150



# İkinci platform özellikleri
platform2_width = 100
platform2_height = 20
platform2_x =50
platform2_y = 300


# Zemin özellikleri
floor_width = screen_width
floor_height = 50
floor_x = 0
floor_y = screen_height - floor_height

# Diken özellikleri
spike_width = 20
spike_height = 30
spike_speed = 1
spike_gap = 200
spike_list = []


# Oyun başlangıç ekranı
def start_screen():
    start = True
    pencere_modu = True # varsayılan olarak pencere modunda başlayalım
    screen = pygame.display.set_mode((screen_width, screen_height))
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if pencere_modu:
                        # tam ekran moduna geçiş
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        pencere_modu = False
                    else:
                        # pencere moduna geçiş
                        screen = pygame.display.set_mode((screen_width, screen_height))
                        pencere_modu = True

        # Ekranı siyah olarak doldur
        screen.fill(black)
        
        # Başlık metnini ekrana yazdır
        font = pygame.font.SysFont(None, 60)
        text = font.render("PLATFORM OYUNU", True, white)
        screen.blit(text, (screen_width/2 - text.get_width()/2, 200))
        # Başlık metnini ekrana yazdır
        font = pygame.font.SysFont(None, 40)
        text = font.render("Tam Ekran 'f'", True, white)
        screen.blit(text, (screen_width/2 - text.get_width()/2, 460))
       
        # Butonları ekrana yazdır
        mouse_pos = pygame.mouse.get_pos()

        start_button = pygame.draw.rect(screen, white, (screen_width/2 - 100, 300, 200, 50))
        quit_button = pygame.draw.rect(screen, white, (screen_width/2 - 100, 370, 200, 50))

        font = pygame.font.SysFont(None, 40)
        text = font.render("OYUNA BAŞLA", True, black)
        screen.blit(text, (screen_width/2 - text.get_width()/2, 310))

        text = font.render("ÇIKIŞ", True, black)
        screen.blit(text, (screen_width/2 - text.get_width()/2, 380))

        # Butonların üzerine gelindiğinde renklerini değiştir
        if start_button.collidepoint(mouse_pos):
            start_button = pygame.draw.rect(screen, red, (screen_width/2 - 100, 300, 200, 50))
            text = font.render("OYUNA BAŞLA", True, white)
            screen.blit(text, (screen_width/2 - text.get_width()/2, 310))

        elif quit_button.collidepoint(mouse_pos):
            quit_button = pygame.draw.rect(screen, red, (screen_width/2 - 100, 370, 200, 50))
            text = font.render("ÇIKIŞ", True, white)
            screen.blit(text, (screen_width/2 - text.get_width()/2, 380))
        
          
        # Tıklama ile butonların fonksiyonlarını çağır
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mouse_pos):
                    start = False
                    pygame.mixer.music.load("yt1s.com - Deltarune Chapter 2 OST 06  A CYBERS WORLD.mp3")
                    pygame.mixer.music.play(-1)
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
           
        pygame.display.update()

# Oyun başlangıç ekranını göster
start_screen()

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
     

        
      
        # Klavye tuşlarına tepki verme
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if pencere_modu:
                    # tam ekran moduna geçiş
                    ekran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    pencere_modu = False
                else:
                    # pencere moduna geçiş
                    ekran = pygame.display.set_mode((screen_width, screen_height))
                    pencere_modu = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                
                     pygame.display.set_mode((800, 600))
       
                 
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            elif event.key == pygame.K_SPACE:
                if player_y_change == 0 or platform_y == player_y and platform_x == player_x or platform2_y == player_y and platform2_x == player_x:
                    player_gravity = 0.01
                    player_y_change = -2.5
        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    # Oyuncu hareketleri
    player_x += player_x_change
    player_y += player_y_change
    player_y_change += player_gravity
    
    # Oyuncu sınırları
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    elif player_y > screen_height - player_height:
        player_y = screen_height - player_height
        player_y_change = 0

    # Platform hareketleri
    
   
    # Çarpışma tespiti
    if player_y_change > 0 and player_y + player_height >= platform_y and player_x + player_width > platform_x and player_x < platform_x + platform_width and player_y < platform_y:
        player_y_change = 0
        player_y = platform_y - player_height
        player_gravity = 0.01

    if player_y_change > 0 and player_y + player_height >= platform2_y and player_x + player_width > platform2_x and player_x < platform2_x + platform2_width and player_y < platform2_y:
            player_y_change = 0
            player_y = platform2_y - player_height
            player_gravity = 0.01

  

    
        
    

   


       



        
    # Ekranı güncelle
    screen.fill(black)
    pygame.draw.rect(screen, white, [platform_x, platform_y, platform_width, platform_height])
    pygame.draw.rect(screen, white, [platform2_x, platform2_y, platform2_width, platform2_height])
    pygame.draw.rect(screen, red, [player_x, player_y, player_width, player_height])
    # Üçgen çizme
    pygame.draw.polygon(screen, red, [(40, 400), (80, 400), (60, 360)])

    pygame.display.update()


# Pygame çıkışı
pygame.quit()
