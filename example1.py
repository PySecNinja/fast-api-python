from fastapi import FastAPI

app = FastAPI() # Creates api object 

@app.get("/")   #This in an "endpoint"
def home():
    return {"Data": "Test"}

@app.get("/about")
def about():
    return {"Data", "About_endpoint_data"}