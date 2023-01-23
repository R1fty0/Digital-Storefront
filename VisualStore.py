import pygame


class WindowManagement:
    def __init__(self, FPS, WindowWidth, WindowHeight, Caption):
        """ Contains the information needed for the core game loop to run."""
        self.FPS = FPS
        self.WindowWidth = WindowWidth
        self.WindowHeight = WindowHeight
        self.Caption = Caption

    def get_parameter(self, parameterType):
        """ Returns a parameter upon request. """
        if parameterType.upper() == "FPS":
            return self.FPS
        elif parameterType.upper() == "WindowWidth":
            return self.WindowWidth
        elif parameterType.upper() == "WindowHeight":
            return self.WindowHeight
        elif parameterType.upper() == "Caption":
            return self.Caption
        else:
            print("Invalid Request, Please double check spelling")
            pass

    def create_game_window(self):
        """Creates a game window that displayed the visuals of the game."""
        Window = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        pygame.display.set_caption(str(self.Caption))


Storefront = WindowManagement(75, 800, 600, "Digital Storefront!")


def Store():
    FPSClock = pygame.time.Clock()  # Clock that maintains FPS

    Storefront.create_game_window()   # Creates Game Window

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Loop - code runs here
        FPSClock.tick(Storefront.FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False

    pygame.quit()   # Quits program
