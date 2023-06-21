# Desc: esse código serve como teste para um transmissão de dados com o lora
import time 
from tx_beacon import *
from rx_cont import *
from SX127x.board_config import BOARD

# definicoes do LoRa
lora = LoRaBeacon(LoRa)
lo = LoRa()
lora.__init__(lora, verbose=False)
BOARD.blink(0.2, 4)

# construcao do codigo
payload = ["enviando a primeira mensagem com o lora"]
lora.start(lora)
lo.write_payload(payload)
lora.on_tx_done(lora)
