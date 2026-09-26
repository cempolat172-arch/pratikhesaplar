from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.1.0")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/kredi", response_class=HTMLResponse)
async def kredi(request: Request):
    return templates.TemplateResponse("kredi.html", {"request": request})

@app.get("/kdv", response_class=HTMLResponse)
async def kdv(request: Request):
    return templates.TemplateResponse("kdv.html", {"request": request})

@app.get("/maas", response_class=HTMLResponse)
async def maas(request: Request):
    return templates.TemplateResponse("maas.html", {"request": request})

@app.get("/kidem", response_class=HTMLResponse)
async def kidem(request: Request):
    return templates.TemplateResponse("kidem.html", {"request": request})

@app.get("/metrekare", response_class=HTMLResponse)
async def metrekare(request: Request):
    return templates.TemplateResponse("metrekare.html", {"request": request})

@app.get("/yakit", response_class=HTMLResponse)
async def yakit(request: Request):
    return templates.TemplateResponse("yakit.html", {"request": request})

@app.get("/kalori", response_class=HTMLResponse)
async def kalori(request: Request):
    return templates.TemplateResponse("kalori.html", {"request": request})

@app.get("/vki", response_class=HTMLResponse)
async def vki(request: Request):
    return templates.TemplateResponse("vki.html", {"request": request})

@app.get("/ariza-kodlari", response_class=HTMLResponse)
async def ariza_kodlari(request: Request):
    return templates.TemplateResponse("hata-kodlari.html", {"request": request})
