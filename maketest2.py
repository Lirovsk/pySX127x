from SX127x.LoRa import *
from SX127x.board_config import BOARD
import time 
from SX127x.LoRa import LoRa

BOARD.setup()


# definicoes do LoRa
lora = LoRa()
BOARD.reset()
BOARD.blink(0.2, 2)

# construcao do codigo
lora.set_mode(MODE.STDBY)
payload = ["2023"]
lora.write_payload(payload)
BOARD.blink(0.4, 3)
lora.set_mode(MODE.SLEEP)
time.sleep(1)
lora.set_mode(MODE.STDBY)
msg = ["2023.2"]
lora.write_payload(msg)
BOARD.blink(0.1, 3)