class Counter:

    def __init__(self):
        self.counter = 0

    def inc(self):
        self.counter = self.counter+1

    def __str__(self):
        return str(self.counter)

import tkinter

class MyFrame(tkinter.Frame):

    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
                                        # on the controller object when the user generates events
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.controller.buttonPressed
        self.incrementButton.pack({"side": "left"})

        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] =  self.quit
        self.quitButton.pack({"side": "left"})

class Controller:

    def __init__(self):
        root = tkinter.Tk()
        self.model = Counter()
        self.view = MyFrame(self)
        self.view.mainloop()

    def buttonPressed(self):
        self.model.inc()
        self.view.labelForOutput["text"] = str(self.model)

if __name__ == "__main__":
    c = Controller()