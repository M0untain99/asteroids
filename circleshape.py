import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Check if this object has collided with another circle
    def collision_check(self, circle2):
        combined_radius = self.radius + circle2.radius  # Calculate the combined radii
        
        p1 = self.position  # Get this objects position
        p2 = circle2.position  # Get the position of the 2nd object

        distance = p1.distance_to(p2)  # Get the distance between the 2 objects

        if distance <= combined_radius:  # If the distance between them is less than their combined radii
            return True

        return False