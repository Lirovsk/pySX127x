from board_config import *
import LoRa

BOARD.setup()
lora = LoRa()
lora.__init__(lora, verbose=False)