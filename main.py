from ast import Str
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sentiment Model API",
    description="A simple API that use NLP model to predict the sentiment of the movie's reviews",
    version="0.1",)

class translation:
    english:str
    french:str
    kinyarwanda:str
    def __init__(self,english:str,french:str,kinyarwandaa:str):
        self.english=english
        self.french=french
        self.kinyarwanda=kinyarwandaa
    def setEnglish(self,value:str):
        self.english=value
    def setFrench(self,value:str):
        self.french=value
    def setKiny(self,value:str):
        self.kinyarwanda=value
    def getEnglish(self):
        return self.english
    def getFrench(self):
        return self.french
    def getKiny(self):
        return self.kinyarwanda
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
@app.get("/greetings/{greetingId}")
def createGreetings(greetingId:int,greet_me:Union[str,None]=None):
    greetings=translation("How are you?","comment allez vous?","Umez'ute?")

    if greetingId>3:
        greet_me="Invalid input"
    elif greetingId<=0:
        greet_me="Invalid input"
    elif greetingId==1:
        greet_me=greetings.getEnglish()
    elif greetingId==2:
        greet_me=greetings.getFrench()
    else:
        greet_me=greetings.getKiny()
        
    return {"Greetings ":greet_me}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
