"""
USAGE - This code is a simple example of how to create an API using FastAPI. 
        It creates an instance of the FastAPI class and defines two endpoints. 
        The first endpoint is a GET request to the root path, which returns a 
        JSON object with a "Data" key and a value of "Test". The second endpoint is a 
        GET request to the "/about" path, which returns a JSON object with a "Data" key 
        and a value of "About_endpoint_data".
"""

from fastapi import FastAPI

app = FastAPI() # Creates api object 

@app.get("/")   #This in an "endpoint"
def home():
    return {"Data": "Test"}

@app.get("/about")
def about():
    return {"Data", "About_endpoint_data"}
