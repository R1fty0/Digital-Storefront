import pygame


class Text:
    pygame.font.init()  # Constructor for Fonts in Pygame

    def __init__(self, text, font, size, bold, italic, aa, color, horizontalPos, verticalPos):
        """ Creates and displays text on screen upon request. Note: aa = anti-aliasing. """
        self.text = text
        self.font = font
        self.size = size
        self.bold = bold
        self.italic = italic
        self.aa = aa
        self.color = color
        self.horizontalPos = horizontalPos
        self.verticalPos = verticalPos

    def create_text(self):
        """ Creates the text that is displayed. """
        font = pygame.font.SysFont(str(self.font), int(self.size), bool(self.bold), bool(self.italic))
        text = font.render(str(self.text), bool(self.aa), self.color)
        return text


class WindowManagement:
    def __init__(self, FPS, WindowWidth, WindowHeight, Caption):
        """ Contains the information needed for the core menu loop to run."""
        self.FPS = FPS
        self.WindowWidth = WindowWidth
        self.WindowHeight = WindowHeight
        self.Caption = Caption
        self.Window = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))

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
        """Creates a game window that contains all the visuals of the application."""
        pygame.display.set_caption(str(self.Caption))


class Color:
    def __init__(self, color):  # Constructor
        """ Create a color based off of 3 values (Red, Green, Blue). """
        self.color = color  # Tuple containing Color RGB Values

    def get_color(self):  # Getter
        """ Returns a color upon request. This method is required to access the color values of a color. """
        return self.color  # Returns the color tuple
