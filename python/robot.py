__author__ = 'eric.stockmeyer'

from socketIO_client import SocketIO


################################ MAIN ################################

def main():

    try:

        while True:
            # keep websocket alive by sending ping on interval
            piClient.ping()

            # look for incoming serial data
            with SocketIO('node.labsmb.com', 8990) as socketIO:
                socketIO.emit('bbb', {'xxx': 'yyy'}, on_bbb_response)
                socketIO.wait_for_callbacks(seconds=1)

    except KeyboardInterrupt:
        piClient.close()
        serialPort.close()



def on_bbb_response(*args):
    print 'on_bbb_response', args


if __name__ == "__main__":
    main()