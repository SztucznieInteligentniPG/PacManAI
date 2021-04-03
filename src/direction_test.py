from direction import Direction

if Direction.DEFAULT is Direction.RIGHT:
    print("True")

if Direction.RIGHT is Direction.DEFAULT:
    print("True")

if Direction.DEFAULT is Direction.LEFT:
    print("False")

if Direction.LEFT is Direction.DEFAULT:
    print("False")
