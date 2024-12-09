from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        print("PC initialized")

class MotherBoard(ABC):
    @abstractmethod
    def start_MotherBoard(self):
        print("MotherBoard started")

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass

class Storage(PC, MotherBoard, RAM, Processor):
    @abstractmethod
    def storage_data(self):
        pass

    def start_MotherBoard(self):
        # self.start_processor()
        print("MotherBoard is Started")

    def start_ram(self):
        # self.start_ram()
        print("RAM is started")

    def start_processor(self):
        # self.start_processor()
        print("Processor is started")

    def storage_data(self):
        print("Data is stored")


    @staticmethod
    def loadOS():
        print("Operating System loaded")

    def startMouse(self):
        print("Mouse connected")

    def useHeadPhone(self):
        print("Headphones connected")

    def runTC(self):
        self.start_MotherBoard()
        self.start_ram()
        self.start_processor()
        self.storage_data()
        self.loadOS()
        self.startMouse()
        self.useHeadPhone()

obj = Storage()
obj.runTC()