from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += (self.velocity * dt)
    
  def split(self):
    self.kill()
    
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    new_velocity_one = self.velocity.rotate(random_angle)
    new_velocity_two = self.velocity.rotate(-random_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
    new_asteroid_one.velocity = new_velocity_one * 1.2
    new_asteroid_two.velocity = new_velocity_two * 1.2
    