import threading as thr

def fim():
    print('Fim do tempo!')

timer = thr.Timer(5.0, fim)

timer.start()
