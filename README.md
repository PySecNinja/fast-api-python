# Build your own API

# What is an API?

## Explain API’s like Im 5.

An API is like a magic button that different programs can push to talk to each other and share information. Imagine you have a toy box with different toy cars inside, and you have a friend who has a toy box with toy houses. An API is like a secret knock that you can use to open the lid of your toy box and show your friend the cars inside, and your friend can use the same knock to open their toy box and show you the houses. In this way, the toy cars and houses can play together, just like how different programs can share information and work together with the help of an API.

## Practical Example

For example, a weather website might have an API that allows a developer to retrieve current weather data for a specific location in a format that can be easily integrated into their own website or application.

## Rest API Architecture

![Screenshot 2023-01-18 at 6.20.42 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_6.20.42_PM.png)

# Understanding Json Data

## What is json?

JSON is a text-based format for representing data, which is commonly used for exchanging data between different systems, especially in web applications. JSON is based on a subset of the JavaScript Programming Language and it is used to represent simple data structures and objects, and arrays. JSON is a standard format and it's supported by almost all the programming languages.

## Is it a like a python dictionary?

A Python dictionary, on the other hand, is a built-in data structure in the Python programming language. It is a collection of key-value pairs, where each key is unique and the value can be of any type. Like JSON, Python dictionaries are also used to store and organize data in a structured way.

## Python Dictionary vs Json

JSON (JavaScript Object Notation) and Python dictionaries are similar in that they are both used to store and organize data in a structured format. However, they are not exactly the same thing.

It's important to note that JSON data can be easily converted to and from Python dictionaries, using the built-in json module in python. This allows to easily exchange data between systems that use different formats.

Therefore, JSON is a format for storing and exchanging data and Python dictionaries is a data structure for storing data in Python. They share similarities but are not exactly the same thing.

# Lets Code!

### Install dependancies

```bash
pip3 install fastapi
pip3 install uvicorn
```

### Fast API Docs

[FastAPI](https://fastapi.tiangolo.com/)

Directory and Project Structure

```bash
fast-api-python
├── README.md
└── example1.py
```

### Create example1.py

```python
from fastapi import FastAPI

app = FastAPI()                 # Creates api object 

@app.get("/")                   #This the root of an "endpoint" 
def home():
    return {"Data": "Test"}
```

Informational Block

```python
# endpoints
/
/about

/hello
/get-item
localhost/hello

# Methods
GET     # Returns information
POST    # Sending information or creating data
PUT     # Update something thats existing in the data base 
DELETE  # Deleting info
```

### Start web server to run locally

example1 in the name of our .py file above and app is the FastAPI object in our code

```bash
uvicorn example1:app --reload
```

Now go to the local host and youll see our data from our python script

```python
http://127.0.0.1:8000/
```

### Documentation

FastAPI automatically creates an api documentation for how to interact with it

```python
http://127.0.0.1:8000/docs
```

## Create another endpoint

Edit [main.py](http://main.py) and save it

```python
from fastapi import FastAPI

app = FastAPI()                 # Creates api object 

@app.get("/")                   #This the root of an "endpoint" 
def home():
    return {"Data": "Test"}

@app.get("/about")              #This is another directory of an endpoint
def about():
    return {"Data", "About_endpoint_data"}
```

unicorn is still running our server in the terminal. Reload the web page and youll see the data.

```python
http://127.0.0.1:8000/about
```

# Interacting with our API

create example2.py

```python
from fastapi import FastAPI

app = FastAPI()                 # Creates api object 

inventory = {
        1:  {
            "name": "Milk",
            "price": 3.99,
            "brand": "fairlife"
        }
    
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work
    return inventory[item_id]
```

### Trust but Verify

Make sure you saved the code

Interact with the code we just wrote

```python
http://127.0.0.1:8000/get-item/1
```

Try typing a letter and see the error you get 

```python
http://127.0.0.1:8000/get-item/f
```

try going to the number 2 in our inventory list - see the error because we have created it yet

```python
http://127.0.0.1:8000/get-item/2
```

### Adding PATH parameters

edit example2.py

```python
from fastapi import FastAPI, Path

app = FastAPI()                 # Creates api object 

inventory = {
        1:  {
            "name": "Milk",
            "price": 3.99,
            "brand": "fairlife"
        }
    
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, lt=2, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]
```

Description above gets added to the docs here.

![Screenshot 2023-01-18 at 7.04.07 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_7.04.07_PM.png)

Constraints added 

greater than 1 and less than 2

```python
gt=0, lt=2
```

### Trust but Verify

Make sure you saved the code

Interact with the code we just wrote

```python
http://127.0.0.1:8000/get-item/1
```

Try typing any number besides 1. The error message is more helpful now.

```python
http://127.0.0.1:8000/get-item/0
http://127.0.0.1:8000/get-item/2
```

# Adding Query Parameters

### examples of query parameters

```python
"facebook.com/home?redirect="
"facebook.com/home?key="
"facebook.com/home?redirect=/drew&msg=fail"
```

See how they all have the syntax 

```python
?<variable_name>=
```

### Having our endpoint accept query parameters

```python
from fastapi import FastAPI, Path

app = FastAPI()                 # Creates api object 

inventory = {
        1:  {
            "name": "Milk",
            "price": 3.99,
            "brand": "fairlife"
        }
    
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, lt=2, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not FOund"}
```

### How to call the new endpoint we made

```python
http://127.0.0.1:8000/get-by-name?name=Milk
http://127.0.0.1:8000/get-by-name?name=drew
http://127.0.0.1:8000/get-by-name
```

# Request Body & Post method

Adding information to a database

edit and save example2.py

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()                 # Creates api object 

inventory = {
        1:  {
            "name": "Milk",
            "price": 3.99,
            "brand": "fairlife"
        }
    
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not FOund"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]
```

### Trust but Verify

Add item ID below and add info for name and price

![Screenshot 2023-01-18 at 7.49.20 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_7.49.20_PM.png)

Hit Execute and added Items are stored in memory. The json code in the picture should have the comma on the last KEY=VALUE pair

![Screenshot 2023-01-18 at 7.51.43 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_7.51.43_PM.png)

Now add ID 2 and you should GET the data we previously POSTED

![Screenshot 2023-01-18 at 7.54.56 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_7.54.56_PM.png)

### Refactor code

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()                 # Creates api object 

inventory = {}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not FOund"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]
```

We now have an empty inventory list 

Lets go to the docs

```python
http://127.0.0.1:8000/docs
```

POST /create-items/{item_id}

```json
{
  "name": "milk",
  "price": 5.99,
  "brand": "fairlife"
}
```

```json
{
  "name": "milk",
  "price": 5.99
}
```

GET/get-by-name

```json
Enter eggs or milk
```

GET/get-item/{item_id}

```json
Enter 1 and 2 see how you retrieved the info you just posted
```

# PUT Request

put updates items

edit example2.py

```python
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()                 # Creates api object 

inventory = {}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

    

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not FOund"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name                # Updates the item in our inventory

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]
```

Go to docs and add an item 

```python
http://127.0.0.1:8000/docs
```

POST /create-items/{item_id}

```python
{
  "name": "milk",
  "price": 3.99
}
```

Lets update the added item now

PUT/update-item/{item_id}

```python
{
  "brand": "fairlife"
}
```

![Screenshot 2023-01-18 at 8.22.41 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_8.22.41_PM.png)

Lets update the added item now

PUT/update-item/{item_id}

```python
{
  "name": "eggs"
}
```

![Screenshot 2023-01-18 at 8.26.29 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_8.26.29_PM.png)

Works the manuel way too

```python
http://127.0.0.1:8000/get-by-name?name=eggs
```

![Screenshot 2023-01-18 at 8.27.40 PM.png](Build%20your%20own%20API%20cc0f2a3c80b04f9b9b0ad38d09d3f814/Screenshot_2023-01-18_at_8.27.40_PM.png)

# Delete Method

edit example2.py

```python
from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()                 # Creates api object 

inventory = {}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

    

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not FOund"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name                # Updates the item in our inventory

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the Item to Delete.", gt=0)):
    if item_id not in inventory:
        return {"Error": "ID Does not exist"}
    
    del inventory[item_id]
    return {"Success": "Item Deleted"}
```

Go to docs

Create an item

Delete the item

# Status codes

```python
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()                 # Creates api object 

inventory = {}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

    

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, gt=0, description="The ID of the item you would like to view")) :                 # Uses the int forces the parameter being passed to be an integer otherwise it wont work 
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not Found")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    
    if item.name != None:
        inventory[item_id].name = item.name                # Updates the item in our inventory

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the Item to Delete.", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist")
    
    del inventory[item_id]
    return {"Success": "Item Deleted"}
```

Go to the docs and try to find item ID 1 and see the error we now get