from actor import Actor
from controller import Controller
from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from position import Position
from renderer import Renderer
from texture import Texture
from world import World
from world_position import WorldPosition

actor: Actor = None
controller: Controller = None
direction: Direction = Direction.UP
entity: Entity = None
entityEntry: EntityDictionary = None
texture: Texture = Texture.PACMAN_0
position: Position = Position(0.5, 0.5)
model: Model = Model(direction, texture, position, position)
renderer: Renderer = Renderer(None)
world: World = World((20, 20))
worldPosition: WorldPosition = WorldPosition(1, 1)

print(world.grid)
