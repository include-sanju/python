import threading
class SanjanaMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = SanjanaMessenger(name = 'send')
y = SanjanaMessenger(name = 'recieve')

x.start()
y.start()
