from SX127x.LoRa import *
from SX127x.board_config import BOARD
import time 
from SX127x.LoRa import LoRa

BOARD.setup()


# definicoes do LoRa
lora = LoRa()
lora.__init__(lora, verbose= True, do_calibration= True, calibration_freq=910)


# construcao do codigo
lora.set_mode(MODE.STDBY)
payload = "enviando mensagens pela primeira vez"
lora.write_payload(payload)
lora.set_mode(MODE.SLEEP)
time.sleep(1)
lora.set_mode(MODE.STDBY)
msg = "enviando mensagens pela segunda vez"
lora.write_payload(msg)