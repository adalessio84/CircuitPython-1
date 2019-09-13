from digitalio import DigitalInOut, Direction, Pull
import board
import time
max = 4
start = time.monotonic()
photo = DigitalInOut(board.D2)
photo.direction = Direction.INPUT
photo.pull = Pull.UP
photo_state = False
last_state = False
value = 0
limit = 0
while True:
    photo_state = photo.value
    if photo_state and not last_state:
        value = value + 1
        # print("# of interrupts:")
        # print(value)
    last_state = photo_state
    remaining = max + start - time.monotonic()
    if remaining <= 0:
        print("# of interrupts:", (value))
        max += 4
        value = 0

