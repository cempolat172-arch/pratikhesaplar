from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.4.0")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/kredi-hesaplama", response_class=HTMLResponse)
async def kredi(request: Request):
    return templates.TemplateResponse(request=request, name="kredi.html")

@app.get("/kdv-hesaplama", response_class=HTMLResponse)
async def kdv(request: Request):
    return templates.TemplateResponse(request=request, name="kdv.html")

@app.get("/maas-hesaplama", response_class=HTMLResponse)
async def maas(request: Request):
    return templates.TemplateResponse(request=request, name="maas.html")

@app.get("/kidem-tazminati-hesaplama", response_class=HTMLResponse)
async def kidem(request: Request):
    return templates.TemplateResponse(request=request, name="kidem.html")

@app.get("/metrekare-hesaplama", response_class=HTMLResponse)
async def metrekare(request: Request):
    return templates.TemplateResponse(request=request, name="metrekare.html")

@app.get("/yol-yakit-hesaplama", response_class=HTMLResponse)
async def yakit(request: Request):
    return templates.TemplateResponse(request=request, name="yakit.html")

@app.get("/kalori-hesaplama", response_class=HTMLResponse)
async def kalori(request: Request):
    return templates.TemplateResponse(request=request, name="kalori.html")

@app.get("/vki-hesaplama", response_class=HTMLResponse)
async def vki(request: Request):
    return templates.TemplateResponse(request=request, name="vki.html")

@app.get("/hata-kodlari", response_class=HTMLResponse)
async def ariza_kodlari(request: Request):
    return templates.TemplateResponse(request=request, name="hata-kodlari.html")
