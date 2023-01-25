import pygame
from VisualStoreData import WindowManagement, Color, Text
pygame.font.init()  # Constructor for Fonts in Pygame

"""
# Create Fonts for UI
    TitleFont = pygame.font.SysFont("Century Gothic", int(WindowWidth/20), True, False)
    
# Create Text for UI
    TitleLabel = TitleFont.render("Rebound", False, 1, Sliver.get_color())

# Display Text on Screen
    Window.blit(TitleLabel, (WindowWidth / 2 - TitleLabel.get_width() / 2, WindowHeight / 4 - TitleLabel.get_height() / 2))    

"""

Storefront = WindowManagement(75, 800, 600, "Digital Storefront!")
MenuBackground = Color((136, 212, 152))
White = Color((0, 0, 0))
menu = Text("Ma mere est tres petite", "Century Gothic", 30, False, False, False, White.get_color(), 100, 80)

"""
    Color Pallet: https://coolors.co/114b5f-1a936f-88d498-c6dabf-f3e9d2
"""


def Graphics(ScreenColor, text):
    Storefront.Window.fill(ScreenColor)
    Storefront.Window.blit(text.create_text(), (text.horizontalPos, text.verticalPos))
    pygame.display.update()  # Updates the Screen with whatever visuals were processed in this method prior.


def Store():



    FPSClock = pygame.time.Clock()  # Clock that maintains FPS

    Storefront.create_game_window()   # Creates Game Window

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Loop - code runs here
        FPSClock.tick(Storefront.FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False
            Graphics(MenuBackground.get_color(), menu)

    pygame.quit()   # Quits program


if __name__ == "__main__":
    Store()