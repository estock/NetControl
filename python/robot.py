__author__ = 'eric.stockmeyer'

from socketIO_client import SocketIO


################################ MAIN ################################

def main():

    print 'running main'
    try:

        with SocketIO('node.labsmb.com', 8990) as socketIO:
            socketIO.emit('bbb', {'xxx': 'yyy'}, on_bbb_response)
            socketIO.on('command', command_response)
            #socketIO.on('aaa_response', on_aaa_response)


        while True:
            # keep websocket alive by sending ping on interval
            #piClient.ping()

            # look for incoming serial data
            print 'waiting'
            socketIO.wait_for_callbacks(seconds=1)

    except KeyboardInterrupt:
        print "Done..."

def on_bbb_response(*args):
    print 'bbb function'
    print 'on_bbb_response', args

def command_response(*args):
    #print 'aaa function'
    print 'command_response', args

if __name__ == "__main__":
    main()