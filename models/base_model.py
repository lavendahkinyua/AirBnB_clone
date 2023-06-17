#!/usr/bin/python3
""" defining a class basemodel """
import uuid
#the reason we have used from its because the datetime class is in a module
from import datetime
#defining a class
class BaseModel:
#instance attribute ..self is an object placeholder that why we use use it to define instance attributes it will be replaced with actual objects when we are calling the object
  def __init__(self):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now
    self.updated_at = datetime.now
  def __str__(self):
     return ("[{}] ({}) {}".format(type(self).__name__), (self.id), (self.__dict__)) 