#!/usr/bin/python3
#define a class
import json
class FileStorage:
#here the variable file path stores a string that is the path of a JSON file
    __file_path = "file.json"
#here the variable/attribute objects stores a dictionary for now its empty
    __objects = {}
    def all(self):
      return self.__objects
    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__object.items()}
        with open(self.__file_path, "w") as file
            json.dump(obj_dict, file)
    def reload(self):
        with open(self.__file_path, "r") as file
            obj_dict = json.load(file)
