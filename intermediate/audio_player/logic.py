import pygame.mixer
class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.track = None
        self.is_playing = False

    def load(self, file_path):
        self.track = file_path
        pygame.mixer.music.load(file_path)

    def play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause() if self.track else pygame.mixer.music.play()
            self.is_playing = True

    def seek(self, position):
        if pygame.mixer.music.get_busy():  # Check if music is playing
            pygame.mixer.music.set_pos(position)
        else:
            pygame.mixer.music.play(start=position)  # Restart from the new position

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
