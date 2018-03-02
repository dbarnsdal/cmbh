import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class pizzajesus(pygame.sprite.Sprite):
    def __init__(self):
        super(pizzajesus, self).__init__()
        self.images = []
        self.images.append(load_image('pizzajesus.png'))
        self.images.append(load_image('pizzajesus2.png'))
        self.images.append(load_image('pizzajesus3.png'))

        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 50, 75)

class seesaw(pygame.sprite.Sprite):
    def __init__(self):
        super(pizzajesus, self).__init__()
        self.images = []
        self.images.append(load_image('seesawA.png'))
        self.images.append(load_image('seesawB.png'))

            # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 50, 75)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap:
            self.edit()
        return super(seesaw, self).on_touch_down(touch)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 900))

    my_sprite = pizzajesus()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()