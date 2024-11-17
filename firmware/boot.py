import gc
import webrepl
import network
import time

webrepl.start()
gc.collect()

time.sleep(5)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("Vodafone-A70131445", "3LAHqtxEs9HsYkcr")

