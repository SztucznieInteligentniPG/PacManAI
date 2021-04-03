from actor import Actor
from controller import Controller
from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from renderer import Renderer
from texture import Texture
from vector2 import Vector2Int, Vector2Float
from world import World


actor: Actor = None
controller: Controller = None
direction = Direction.DEFAULT
entity: Entity = None
entityEntry = EntityDictionary.WALL
texture = Texture.PACMAN_0
position = Vector2Float(0.5, 0.5)
model = Model(direction, texture, position, position)
renderer = Renderer(None)
worldPosition = Vector2Int(1, 1)
world = World(worldPosition)

print(world.grid)
