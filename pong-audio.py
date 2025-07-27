import pygame

pygame.init()
pygame.mixer.music.load("C:\\Users\\Ionut\\Music\\Unknown Worlds\\Subnautica\\Elektronomia - Sky High [NCS Release].mp3")

muted = False
def play_song():
    pygame.mixer_music.play(-1)

def stop_song():
    pygame.mixer_music.stop()

def toggle_mute():
    global muted
    muted = not muted
    if muted:
        pygame.mixer_music.pause()
    else:
        pygame.mixer_music.unpause()

def draw_mute_button(screen):
    mute_button = pygame.image.load("C:\\Users\\Ionut\\Desktop\\image.png")
    mute_button_muted = pygame.image.load("C:\\Users\\Ionut\\Desktop\\image1.png")
    if muted:
        screen.blit(mute_button_muted, (1910, 1070))
    else:
        screen.blit(mute_button, (1910, 1070))


