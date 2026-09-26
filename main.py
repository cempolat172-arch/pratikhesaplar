import datetime
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.3.0")
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

@app.get("/sitemap.xml", response_class=Response)
async def sitemap():
    today = datetime.date.today().isoformat()
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://pratikhesaplar.com/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/kredi-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/kdv-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/maas-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/kidem-tazminati-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/metrekare-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/yol-yakit-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/kalori-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/vki-hesaplama</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pratikhesaplar.com/hata-kodlari</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""
    return Response(content=xml_content, media_type="application/xml")
