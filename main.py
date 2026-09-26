from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.2.0")
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

@app.get("/sitemap.xml")
async def sitemap():
    # Güncel tarih (sitemap için)
    import datetime
    today = datetime.date.today().isoformat()
    
    # Tüm sayfaların listesi
    pages = [
        "",
        "/kredi-hesaplama",
        "/kdv-hesaplama",
        "/maas-hesaplama",
        "/kidem-tazminati-hesaplama",
        "/metrekare-hesaplama",
        "/yol-yakit-hesaplama",
        "/kalori-hesaplama",
        "/vki-hesaplama",
        "/hata-kodlari"
    ]
    
    domain = "https://pratikhesaplar.com"
    
    xml_content = f'<?xml version="1.0" encoding="UTF-8"?>\\n'
    xml_content += f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
    
    for page in pages:
        priority = "1.0" if page == "" else "0.8"
        xml_content += f"  <url>\\n"
        xml_content += f"    <loc>{domain}{page}</loc>\\n"
        xml_content += f"    <lastmod>{today}</lastmod>\\n"
        xml_content += f"    <changefreq>weekly</changefreq>\\n"
        xml_content += f"    <priority>{priority}</priority>\\n"
        xml_content += f"  </url>\\n"
        
    xml_content += "</urlset>"
    
    return Response(content=xml_content, media_type="application/xml")
