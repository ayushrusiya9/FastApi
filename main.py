from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
def home():
    return items

items = [{"name":"ayuh","age":21},{"name":"ayush","age":21,"city":"bhopal"}]

@app.post("/create")
def create( name :str,age:int,city:str):
    d = {}
    d["name"] = name
    d["age"] = age
    d["city"] = city
    items.append(d)
    print(items)
    return items

@app.put("/update/{name}")
def update(name):
    for i in items:
        if i["name"] == name:
            i["name"] = "piyush"
            i["age"] = 32
            i["city"] = "indore"
        print(i)
    return i

@app.delete("/del/{name}")
def delete(name):
    for i in items:
        if i["name"] == name:
            i["name"] = ""
        print(i)
    return i