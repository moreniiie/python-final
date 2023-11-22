from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


import os




app = FastAPI()

current_directory = os.path.dirname(os.path.realpath(__file__))
templates_directory = os.path.join(current_directory, "templates")
static_directory = os.path.join(current_directory, "static")

app.mount("/static", StaticFiles(directory=static_directory), name="static")

templates = Jinja2Templates(directory=templates_directory)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("firstpage.html", {"request": request})

@app.get("/form.html", response_class=HTMLResponse)
def read_form_html(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)





