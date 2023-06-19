from SX127x.LoRa import *
from SX127x.board_config import BOARD
import time
from SX127x.LoRa import LoRa
from SX127x.constants import *


# definicoes do  módulo e da placa
BOARD.setup()
lora = LoRa()
print(BOARD.spidev)
print(lora.get_all_registers)
BOARD.blink(0.2, 4)

# construcao do codigo
BOARD.reset()
BOARD.blink(0.2, 6)
lora.set_mode(MODE.STDBY)
lora.__init__(lora, verbose= True, do_calibration= True, calibration_freq=910)
payload = "enviando mensagens pela primeira vez"
lora.write_payload(payload)