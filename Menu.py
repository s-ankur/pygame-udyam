__author__ = 'AnkuR'
import pygame
from Engine import screen,clock,FPS


menus=(pygame.image.load('_menu.bmp'),pygame.image.load('_instr.bmp'),pygame.image.load('_credits.bmp'))


def menuloop():
    load_menu(0)
    MenuManager.new=0
    while MenuManager.events():
        if MenuManager.status_changed():
            load_menu(MenuManager.new)
        clock.tick(FPS)


def load_menu(n):
    pygame.mixer.music.load('_music_'+str(n)+'.wav')
    pygame.mixer.music.play(-1)
    screen.blit(menus[n], (0,0))
    pygame.display.update()


class MenuManager:
    new=0
    old=0

    @classmethod
    def status_changed(cls):
        x=cls.old!=cls.new
        cls.old=cls.new
        return x

    @classmethod
    def events(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button(X) is pressed, then quit the program
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    cls.new=0
                elif event.key == pygame.K_i:
                    cls.new=1
                elif event.key == pygame.K_c:
                    cls.new=2
                elif event.key == pygame.K_p:
                    pygame.mixer.music.load('_music_3.wav')
                    pygame.mixer.music.play(-1)
                    return False

        return True

