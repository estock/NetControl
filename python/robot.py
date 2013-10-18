__author__ = 'eric.stockmeyer'

from socketIO_client import SocketIO


################################ MAIN ################################

def main():

    try:
        # initialize serial port
        serialPort = serial.Serial(port='/dev/ttyUSB0',baudrate='9600')
        serialPort.flushInput()

        # initialize websocket client
        piClient = PiClient('ws://ec2-23-20-219-99.compute-1.amazonaws.com:8080/ws', serialPort)
        piClient.connect()

        while True:
        # keep websocket alive by sending ping on interval

        with SocketIO('ws://node.labsmb.com', 8990) as socketIO:
            socketIO.emit('bbb', {'xxx': 'yyy'}, on_bbb_response)
            socketIO.wait_for_callbacks(seconds=1)

    except KeyboardInterrupt:
        piClient.close()
        serialPort.close()

def on_bbb_response(*args):
    print 'on_bbb_response', args
