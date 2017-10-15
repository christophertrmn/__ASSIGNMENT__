class keluarout():
    def __init__(self,quit):
        self.quit = quit

    def printoutklr(self):
        print(self.quit)
        quit()

class lanjutan(keluarout):
    def __init__(self,quit,quit2):
        keluarout.__init__(self,quit)
        self.quit2=quit2

    def mantap(self):
        print(self.quit , self.quit2)
        quit()
