  
from abc import ABC, abstractmethod
from pickle import dumps, loads
import json

class SerializationInterface(ABC):
    
    @abstractmethod
    def json_ser(self):
        pass

    @abstractmethod
    def bin_ser(self):
        pass



class ListSerialization(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def json_ser(self):
        ser_data = json.dumps(self.data)
        return ser_data

    def bin_ser(self):
        ser_data = dumps(self.data)
        return ser_data


class DictSerialization(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def json_ser(self):
        ser_data = json.dumps(self.data)
        return ser_data

    def bin_ser(self):
        ser_data = dumps(self.data)
        return ser_data


class TupleSerialization(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def json_ser(self):
        ser_data = json.dumps(self.data)
        return ser_data

    def bin_ser(self):
        ser_data = dumps(self.data)
        return ser_data


class TextSerialization(SerializationInterface):

    def __init__(self, data):
        self.data = data

    def json_ser(self):
        ser_data = json.dumps(self.data)
        return ser_data

    def bin_ser(self):
        ser_data = dumps(self.data)
        return ser_data


class MyMeta(type, ABC):
    
    children_number = -1
    
    def __new__(meta_class,class_name, parents, attributes):
        meta_class.children_number += 1
        attributes['children_number'] = meta_class.children_number
        return type.__new__(meta_class,class_name, parents, attributes)


class Cls1(metaclass = MyMeta):
    pass


class Cls2(metaclass = MyMeta):
    pass