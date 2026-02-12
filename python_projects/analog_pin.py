import MCP3008_simple as MCP
import time

try:
    while True:
        val = MCP.getResult(0, 10)
        print(val)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('pins ready to go')