import urllib.request
import json
import re
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.6.0")
templates = Jinja2Templates(directory="templates")

@app.api_route("/", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "title": "Pratik Hesaplar | Türkiye'nin En Kapsamlı Hesaplama ve Arıza Portalı",
            "description": "Kredi, KDV, maaş, kıdem tazminatı, yol yakıt maliyeti hesaplama araçları ve tüm markalara ait kombi, klima, beyaz eşya arıza kodları tek bir platformda."
        }
    )

@app.api_route("/kredi-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
@app.api_route("/kredi-hesaplama/{tutar}-tl-{vade}-ay", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def kredi(request: Request, tutar: str = "", vade: str = ""):
    import datetime
    year = datetime.datetime.now().year
    
    if tutar and vade:
        title = f"{tutar} TL {vade} Ay Kredi Hesaplama {year} | Pratik Hesaplar"
        desc = f"{year} yılı güncel faiz oranlarıyla {tutar} TL tutarındaki kredinin {vade} ay vadeli taksit ve geri ödeme tablosunu anında hesaplayın."
    else:
        title = f"Kredi Hesaplama Aracı {year} | İhtiyaç, Taşıt ve Konut Kredisi - Pratik Hesaplar"
        desc = f"{year} yılı güncel faiz oranlarıyla hızlı kredi hesaplama yapın. İstediğiniz vade oranlarına göre aylık taksit miktarını ve toplam geri ödeme tutarını anında öğrenin."
        
    return templates.TemplateResponse(
        request=request, 
        name="kredi.html",
        context={
            "title": title,
            "description": desc,
            "tutar": tutar,
            "vade": vade,
            "year": year
        }
    )

@app.api_route("/kdv-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def kdv(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kdv.html",
        context={
            "title": "KDV Hesaplama 2026 | KDV Dahil ve Hariç Hesaplama - Pratik Hesaplar",
            "description": "%1, %10 ve %20 güncel KDV oranları ile KDV dahil ve KDV hariç tutarları saniyeler içinde hesaplayın. Pratik ve net hesaplama aracı."
        }
    )

@app.api_route("/maas-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def maas(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="maas.html",
        context={
            "title": "Maaş Hesaplama | Brütten Nete Detaylı Maaş - Pratik Hesaplar",
            "description": "Brüt maaşınızı girin; SGK işçi payı, işsizlik sigortası, gelir ve damga vergisi kesintilerini düşerek net ele geçen maaşınızı detaylıca hesaplayın."
        }
    )

@app.api_route("/kidem-tazminati-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def kidem(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kidem.html",
        context={
            "title": "Kıdem Tazminatı Hesaplama | Brüt ve Net Tazminat Hesapla - Pratik Hesaplar",
            "description": "Çalıştığınız yıl, ay ve gün sayısına göre kıdem ve ihbar tazminatınızı anında hesaplayın. Damga vergisi kesintili net tazminat tutarınızı öğrenin."
        }
    )

@app.api_route("/metrekare-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def metrekare(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="metrekare.html",
        context={
            "title": "Metrekare (m²) Hesaplama | Alan Hesaplama Aracı - Pratik Hesaplar",
            "description": "Oda, arsa, duvar veya yüzey alanları için en ve boy ölçülerini girerek hızlıca metrekare (m2) hesabı yapın. İnşaat ve boya işlemleri için pratik araç."
        }
    )

@app.api_route("/yol-yakit-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def yakit(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="yakit.html",
        context={
            "title": "Yol ve Yakıt Hesaplama | Yakıt Tüketim Maliyeti - Pratik Hesaplar",
            "description": "Seyahatleriniz için yol ve yakıt maliyeti hesaplama aracı. Gideceğiniz mesafe ve aracınızın tüketimine göre toplam seyahat masrafınızı hesaplayın."
        }
    )

@app.api_route("/kalori-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def kalori(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kalori.html",
        context={
            "title": "Günlük Kalori İhtiyacı Hesaplama | Pratik Hesaplar",
            "description": "Kilo, boy, yaş ve cinsiyetinize göre bazal metabolizma hızınızı (BMR) ve günlük almanız gereken ortalama kalori miktarını hesaplayın."
        }
    )

@app.api_route("/vki-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def vki(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="vki.html",
        context={
            "title": "Vücut Kitle İndeksi (VKİ) Hesaplama ve İdeal Kilo - Pratik Hesaplar",
            "description": "Boy ve kilo oranınıza göre Vücut Kitle Endeksinizi (BMI) anında hesaplayın. Obezite durumunuzu ve olmanız gereken ideal kiloyu öğrenin."
        }
    )

@app.api_route("/hata-kodlari", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def ariza_kodlari(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="hata-kodlari.html",
        context={
            "title": "Kombi, Klima ve Beyaz Eşya Arıza Kodları | Geniş Arşiv - Pratik Hesaplar",
            "description": "Vaillant, Demirdöküm, Bosch, Arçelik, Beko ve diğer tüm markalara ait kombi, çamaşır makinesi, bulaşık makinesi, klima ve buzdolabı arıza kodları sözlüğü."
        }
    )

@app.api_route("/gunluk-su-ihtiyaci-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def su_ihtiyaci(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="su-ihtiyaci.html",
        context={
            "title": "Günlük Su İhtiyacı Hesaplama (Litre/Bardak) | Pratik Hesaplar",
            "description": "Kilonuza, hareket seviyenize ve mevsim şartlarına göre vücudunuzun günlük su tüketim ihtiyacını ücretsiz hesaplayın."
        }
    )

@app.api_route("/gebelik-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def gebelik(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="gebelik.html",
        context={
            "title": "Gebelik ve Tahmini Doğum Tarihi Hesaplama | Pratik Hesaplar",
            "description": "Son adet tarihinize (SAT) göre kaç haftalık hamile olduğunuzu, tahmini doğum tarihinizi ve bebeğinizin burcunu hesaplayın."
        }
    )

@app.api_route("/enflasyon-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def enflasyon(request: Request):
    return templates.TemplateResponse(
        request=request, name="enflasyon.html",
        context={"title": "Enflasyon ve Satın Alma Gücü Hesaplama | Pratik Hesaplar", "description": "Geçmişten günümüze enflasyon oranları ile paranızın satın alma gücünü ve değer kaybını hesaplayın."}
    )

@app.api_route("/mtv-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def mtv(request: Request):
    return templates.TemplateResponse(
        request=request, name="mtv.html",
        context={"title": "MTV ve Araç Gecikme Zammı Hesaplama | Pratik Hesaplar", "description": "Araç yaşı ve motor hacmine göre Motorlu Taşıtlar Vergisi (MTV) ve muayene gecikme cezasını öğrenin."}
    )

@app.api_route("/yatirim-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def yatirim(request: Request):
    return templates.TemplateResponse(
        request=request, name="yatirim.html",
        context={"title": "Bileşik Getiri ve Yatırım Hesaplama | Pratik Hesaplar", "description": "Mevduat, altın, fon birikimleriniz için bileşik faiz getirisini hesaplayarak geleceğinizi planlayın."}
    )

@app.api_route("/emeklilik-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def emeklilik(request: Request):
    return templates.TemplateResponse(
        request=request, name="emeklilik.html",
        context={"title": "Emeklilik Yaşı ve Şartları Hesaplama (SSK/Bağkur) | Pratik Hesaplar", "description": "İşe giriş tarihinize ve prim gününüze göre ne zaman emekli olacağınızı ve kalan şartlarınızı sorgulayın."}
    )

@app.api_route("/hesap-makinesi", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def hesap_makinesi(request: Request):
    return templates.TemplateResponse(
        request=request, name="hesap-makinesi.html",
        context={"title": "Gelişmiş Online Hesap Makinesi | Pratik Hesaplar", "description": "Dört işlem, karekök, yüzde hesaplama ve bilimsel fonksiyonları bir arada sunan gelişmiş online hesap makinesi."}
    )

@app.api_route("/yas-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def yas_hesaplama(request: Request):
    return templates.TemplateResponse(
        request=request, name="yas.html",
        context={"title": "Yaş ve Gün Hesaplama Aracı | Pratik Hesaplar", "description": "Doğum tarihinizi girerek kaç yıl, ay, gün, saat ve dakikadır yaşadığınızı hesaplayın."}
    )

@app.api_route("/emeklilik-sayaci", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def emeklilik_sayaci(request: Request):
    return templates.TemplateResponse(
        request=request, name="emeklilik-sayaci.html",
        context={"title": "Emeklilik Geri Sayımı ve Yaş Hesaplama | Pratik Hesaplar", "description": "Emekliliğinize kalan süreyi detaylı bir geri sayım aracı ile hesaplayın."}
    )

@app.api_route("/saat-farki-hesaplama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def saat_farki(request: Request):
    return templates.TemplateResponse(
        request=request, name="saat-farki.html",
        context={"title": "Saat Farkı ve Zaman Dilimi Hesaplama | Pratik Hesaplar", "description": "Dünya şehirleri arasındaki anlık saat farkını ve zaman dilimlerini hesaplayın."}
    )

@app.api_route("/metin-sayaci", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def metin_sayaci(request: Request):
    return templates.TemplateResponse(
        request=request, name="metin-sayaci.html",
        context={"title": "Metin ve Kelime Sayacı | Pratik Hesaplar", "description": "Metinlerinizin kelime, karakter (boşluklu/boşluksuz), cümle sayısını ve tahmini okuma süresini anında hesaplayın."}
    )

@app.api_route("/qr-kod-olusturucu", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def qr_kod_olusturucu(request: Request):
    return templates.TemplateResponse(
        request=request, name="qr-kod-olusturucu.html",
        context={"title": "Ücretsiz QR Kod (Karekod) Oluşturucu | Pratik Hesaplar", "description": "Bağlantılarınızı ve metinlerinizi saniyeler içinde ücretsiz olarak QR koda (karekoda) dönüştürün ve indirin."}
    )

@app.api_route("/guvenli-sifre-olustur", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def guvenli_sifre(request: Request):
    return templates.TemplateResponse(
        request=request, name="sifre-olusturucu.html",
        context={"title": "Güvenli Şifre Oluşturucu (Password Generator) | Pratik Hesaplar", "description": "Kırılması zor ve güvenli şifreler üretin. Büyük harf, küçük harf, rakam ve sembolleri kullanarak rastgele parolalar oluşturun."}
    )

@app.api_route("/cv-hazirlama", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def cv_hazirlama(request: Request):
    return templates.TemplateResponse(
        request=request, name="cv-hazirlama.html",
        context={
            "title": "Gerçekten %100 Ücretsiz Online CV Hazırlama (Sürpriz Ücret Yok)", 
            "description": "Son aşamada para isteyen siteleri unutun. Üyeliksiz, kredi kartsız ve gizli ücretsiz tamamen bedava CV (Özgeçmiş) oluşturup anında PDF olarak indirin."
        }
    )


@app.api_route("/rehber", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def rehber_index(request: Request):
    return templates.TemplateResponse(
        request=request, name="rehber-index.html",
        context={"title": "Bilgi Bankası ve Rehberler | Pratik Hesaplar", "description": "Kredi, tazminat, özgeçmiş hazırlama ve dijital araçlar hakkında en güncel ipuçları, SEO uyumlu detaylı rehberler."}
    )

@app.api_route("/rehber/kidem-tazminati-nasil-hesaplanir", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def rehber_kidem(request: Request):
    return templates.TemplateResponse(
        request=request, name="rehber-kidem.html",
        context={"title": "Kıdem Tazminatı Nasıl Hesaplanır? 2026 Güncel Şartlar", "description": "İstifa edince kıdem tazminatı alınır mı? Brüt ve net maaş üzerinden tazminat hesaplama şartları."}
    )

@app.api_route("/rehber/kredi-cekerken-nelere-dikkat-etmeli", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def rehber_kredi(request: Request):
    return templates.TemplateResponse(
        request=request, name="rehber-kredi.html",
        context={"title": "Kredi Çekerken Nelere Dikkat Etmeli? Faiz Hesaplama Tüyoları", "description": "İhtiyaç, konut veya taşıt kredisi alırken faiz yükünü azaltmanın yolları ve doğru taksit hesaplama teknikleri."}
    )

@app.api_route("/rehber/ats-uyumlu-cv-nasil-hazirlanir", response_class=HTMLResponse, methods=["GET", "HEAD"])
async def rehber_cv(request: Request):
    return templates.TemplateResponse(
        request=request, name="rehber-cv.html",
        context={"title": "ATS Uyumlu CV Nasıl Hazırlanır? Ücretsiz Rehber", "description": "İnsan kaynakları programlarından (ATS) %100 geçen, modern ve profesyonel CV hazırlamanın altın kuralları."}
    )


@app.api_route("/api/piyasa", methods=["GET", "HEAD"])
async def api_piyasa():
    import urllib.request
    import json
    import re
    from fastapi.responses import JSONResponse

    truncgil_data = {}
    try:
        req = urllib.request.Request('https://finans.truncgil.com/today.json', headers={'User-Agent': 'Mozilla/5.0'})
        truncgil_data = json.loads(urllib.request.urlopen(req, timeout=5).read().decode('utf-8'))
    except Exception as e:
        pass

    benzin, motorin, lpg = "84,50", "94,80", "41,20"
    try:
        req_fuel = urllib.request.Request('https://www.tppd.com.tr/istanbul-akaryakit-fiyatlari', headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req_fuel, timeout=5).read().decode('utf-8')
        
        b_match = re.search(r'data-title="KURŞUNSUZ BENZİN \(TL/LT\)"[^>]*>\s*([\d,]+)', html)
        m_match = re.search(r'data-title="MOTORİN \(TL/LT\)"[^>]*>\s*([\d,]+)', html)
        l_match = re.search(r'data-title="GAZ"[^>]*>\s*([\d,]+)', html)
        
        if b_match: benzin = b_match.group(1)
        if m_match: motorin = m_match.group(1)
        if l_match: lpg = l_match.group(1)
    except:
        pass

    return JSONResponse({
        "truncgil": truncgil_data,
        "fuel": {
            "benzin": benzin,
            "motorin": motorin,
            "lpg": lpg
        }
    })

@app.api_route("/sitemap.xml", response_class=FileResponse, methods=["GET", "HEAD"])
async def sitemap():
    return FileResponse("sitemap.xml", media_type="application/xml")

@app.api_route("/robots.txt", response_class=PlainTextResponse, methods=["GET", "HEAD"])
async def robots():
    content = "User-agent: *\nAllow: /\n\nSitemap: https://pratikhesaplar.com/sitemap.xml\n"
    return PlainTextResponse(content=content)
