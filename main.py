from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.6.0")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "title": "Pratik Hesaplar | Türkiye'nin En Kapsamlı Hesaplama ve Arıza Portalı",
            "description": "Kredi, KDV, maaş, kıdem tazminatı, yol yakıt maliyeti hesaplama araçları ve tüm markalara ait kombi, klima, beyaz eşya arıza kodları tek bir platformda."
        }
    )

@app.get("/kredi-hesaplama", response_class=HTMLResponse)
async def kredi(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kredi.html",
        context={
            "title": "Kredi Hesaplama Aracı | İhtiyaç, Taşıt ve Konut Kredisi - Pratik Hesaplar",
            "description": "Güncel faiz oranlarıyla hızlı kredi hesaplama yapın. İstediğiniz vade oranlarına göre aylık taksit miktarını ve toplam geri ödeme tutarını anında öğrenin."
        }
    )

@app.get("/kdv-hesaplama", response_class=HTMLResponse)
async def kdv(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kdv.html",
        context={
            "title": "KDV Hesaplama 2026 | KDV Dahil ve Hariç Hesaplama - Pratik Hesaplar",
            "description": "%1, %10 ve %20 güncel KDV oranları ile KDV dahil ve KDV hariç tutarları saniyeler içinde hesaplayın. Pratik ve net hesaplama aracı."
        }
    )

@app.get("/maas-hesaplama", response_class=HTMLResponse)
async def maas(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="maas.html",
        context={
            "title": "Maaş Hesaplama | Brütten Nete Detaylı Maaş - Pratik Hesaplar",
            "description": "Brüt maaşınızı girin; SGK işçi payı, işsizlik sigortası, gelir ve damga vergisi kesintilerini düşerek net ele geçen maaşınızı detaylıca hesaplayın."
        }
    )

@app.get("/kidem-tazminati-hesaplama", response_class=HTMLResponse)
async def kidem(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kidem.html",
        context={
            "title": "Kıdem Tazminatı Hesaplama | Brüt ve Net Tazminat Hesapla - Pratik Hesaplar",
            "description": "Çalıştığınız yıl, ay ve gün sayısına göre kıdem ve ihbar tazminatınızı anında hesaplayın. Damga vergisi kesintili net tazminat tutarınızı öğrenin."
        }
    )

@app.get("/metrekare-hesaplama", response_class=HTMLResponse)
async def metrekare(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="metrekare.html",
        context={
            "title": "Metrekare (m²) Hesaplama | Alan Hesaplama Aracı - Pratik Hesaplar",
            "description": "Oda, arsa, duvar veya yüzey alanları için en ve boy ölçülerini girerek hızlıca metrekare (m2) hesabı yapın. İnşaat ve boya işlemleri için pratik araç."
        }
    )

@app.get("/yol-yakit-hesaplama", response_class=HTMLResponse)
async def yakit(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="yakit.html",
        context={
            "title": "Yol ve Yakıt Hesaplama | Yakıt Tüketim Maliyeti - Pratik Hesaplar",
            "description": "Seyahatleriniz için yol ve yakıt maliyeti hesaplama aracı. Gideceğiniz mesafe ve aracınızın tüketimine göre toplam seyahat masrafınızı hesaplayın."
        }
    )

@app.get("/kalori-hesaplama", response_class=HTMLResponse)
async def kalori(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="kalori.html",
        context={
            "title": "Günlük Kalori İhtiyacı Hesaplama | Pratik Hesaplar",
            "description": "Kilo, boy, yaş ve cinsiyetinize göre bazal metabolizma hızınızı (BMR) ve günlük almanız gereken ortalama kalori miktarını hesaplayın."
        }
    )

@app.get("/vki-hesaplama", response_class=HTMLResponse)
async def vki(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="vki.html",
        context={
            "title": "Vücut Kitle İndeksi (VKİ) Hesaplama ve İdeal Kilo - Pratik Hesaplar",
            "description": "Boy ve kilo oranınıza göre Vücut Kitle Endeksinizi (BMI) anında hesaplayın. Obezite durumunuzu ve olmanız gereken ideal kiloyu öğrenin."
        }
    )

@app.get("/hata-kodlari", response_class=HTMLResponse)
async def ariza_kodlari(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="hata-kodlari.html",
        context={
            "title": "Kombi, Klima ve Beyaz Eşya Arıza Kodları | Geniş Arşiv - Pratik Hesaplar",
            "description": "Vaillant, Demirdöküm, Bosch, Arçelik, Beko ve diğer tüm markalara ait kombi, çamaşır makinesi, bulaşık makinesi, klima ve buzdolabı arıza kodları sözlüğü."
        }
    )

@app.get("/gunluk-su-ihtiyaci-hesaplama", response_class=HTMLResponse)
async def su_ihtiyaci(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="su-ihtiyaci.html",
        context={
            "title": "Günlük Su İhtiyacı Hesaplama (Litre/Bardak) | Pratik Hesaplar",
            "description": "Kilonuza, hareket seviyenize ve mevsim şartlarına göre vücudunuzun günlük su tüketim ihtiyacını ücretsiz hesaplayın."
        }
    )

@app.get("/gebelik-hesaplama", response_class=HTMLResponse)
async def gebelik(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="gebelik.html",
        context={
            "title": "Gebelik ve Tahmini Doğum Tarihi Hesaplama | Pratik Hesaplar",
            "description": "Son adet tarihinize (SAT) göre kaç haftalık hamile olduğunuzu, tahmini doğum tarihinizi ve bebeğinizin burcunu hesaplayın."
        }
    )

@app.get("/enflasyon-hesaplama", response_class=HTMLResponse)
async def enflasyon(request: Request):
    return templates.TemplateResponse(
        request=request, name="enflasyon.html",
        context={"title": "Enflasyon ve Satın Alma Gücü Hesaplama | Pratik Hesaplar", "description": "Geçmişten günümüze enflasyon oranları ile paranızın satın alma gücünü ve değer kaybını hesaplayın."}
    )

@app.get("/mtv-hesaplama", response_class=HTMLResponse)
async def mtv(request: Request):
    return templates.TemplateResponse(
        request=request, name="mtv.html",
        context={"title": "MTV ve Araç Gecikme Zammı Hesaplama | Pratik Hesaplar", "description": "Araç yaşı ve motor hacmine göre Motorlu Taşıtlar Vergisi (MTV) ve muayene gecikme cezasını öğrenin."}
    )

@app.get("/yatirim-hesaplama", response_class=HTMLResponse)
async def yatirim(request: Request):
    return templates.TemplateResponse(
        request=request, name="yatirim.html",
        context={"title": "Bileşik Getiri ve Yatırım Hesaplama | Pratik Hesaplar", "description": "Mevduat, altın, fon birikimleriniz için bileşik faiz getirisini hesaplayarak geleceğinizi planlayın."}
    )

@app.get("/emeklilik-hesaplama", response_class=HTMLResponse)
async def emeklilik(request: Request):
    return templates.TemplateResponse(
        request=request, name="emeklilik.html",
        context={"title": "Emeklilik Yaşı ve Şartları Hesaplama (SSK/Bağkur) | Pratik Hesaplar", "description": "İşe giriş tarihinize ve prim gününüze göre ne zaman emekli olacağınızı ve kalan şartlarınızı sorgulayın."}
    )

@app.get("/hesap-makinesi", response_class=HTMLResponse)
async def hesap_makinesi(request: Request):
    return templates.TemplateResponse(
        request=request, name="hesap-makinesi.html",
        context={"title": "Gelişmiş Online Hesap Makinesi | Pratik Hesaplar", "description": "Dört işlem, karekök, yüzde hesaplama ve bilimsel fonksiyonları bir arada sunan gelişmiş online hesap makinesi."}
    )

@app.get("/yas-hesaplama", response_class=HTMLResponse)
async def yas_hesaplama(request: Request):
    return templates.TemplateResponse(
        request=request, name="yas.html",
        context={"title": "Yaş ve Gün Hesaplama Aracı | Pratik Hesaplar", "description": "Doğum tarihinizi girerek kaç yıl, ay, gün, saat ve dakikadır yaşadığınızı hesaplayın."}
    )

@app.get("/emeklilik-sayaci", response_class=HTMLResponse)
async def emeklilik_sayaci(request: Request):
    return templates.TemplateResponse(
        request=request, name="emeklilik-sayaci.html",
        context={"title": "Emeklilik Geri Sayımı ve Yaş Hesaplama | Pratik Hesaplar", "description": "Emekliliğinize kalan süreyi detaylı bir geri sayım aracı ile hesaplayın."}
    )

@app.get("/saat-farki-hesaplama", response_class=HTMLResponse)
async def saat_farki(request: Request):
    return templates.TemplateResponse(
        request=request, name="saat-farki.html",
        context={"title": "Saat Farkı ve Zaman Dilimi Hesaplama | Pratik Hesaplar", "description": "Dünya şehirleri arasındaki anlık saat farkını ve zaman dilimlerini hesaplayın."}
    )

@app.get("/metin-sayaci", response_class=HTMLResponse)
async def metin_sayaci(request: Request):
    return templates.TemplateResponse(
        request=request, name="metin-sayaci.html",
        context={"title": "Metin ve Kelime Sayacı | Pratik Hesaplar", "description": "Metinlerinizin kelime, karakter (boşluklu/boşluksuz), cümle sayısını ve tahmini okuma süresini anında hesaplayın."}
    )

@app.get("/qr-kod-olusturucu", response_class=HTMLResponse)
async def qr_kod_olusturucu(request: Request):
    return templates.TemplateResponse(
        request=request, name="qr-kod-olusturucu.html",
        context={"title": "Ücretsiz QR Kod (Karekod) Oluşturucu | Pratik Hesaplar", "description": "Bağlantılarınızı ve metinlerinizi saniyeler içinde ücretsiz olarak QR koda (karekoda) dönüştürün ve indirin."}
    )

@app.get("/guvenli-sifre-olustur", response_class=HTMLResponse)
async def guvenli_sifre(request: Request):
    return templates.TemplateResponse(
        request=request, name="sifre-olusturucu.html",
        context={"title": "Güvenli Şifre Oluşturucu (Password Generator) | Pratik Hesaplar", "description": "Kırılması zor ve güvenli şifreler üretin. Büyük harf, küçük harf, rakam ve sembolleri kullanarak rastgele parolalar oluşturun."}
    )

@app.get("/cv-hazirlama", response_class=HTMLResponse)
async def cv_hazirlama(request: Request):
    return templates.TemplateResponse(
        request=request, name="cv-hazirlama.html",
        context={"title": "Ücretsiz Online CV Hazırlama | Pratik Hesaplar", "description": "Adım adım form doldurarak ücretsiz ve profesyonel özgeçmiş (CV) oluşturun. ATS uyumlu formatta PDF olarak anında indirin."}
    )

@app.get("/sitemap.xml", response_class=FileResponse)
async def sitemap():
    return FileResponse("sitemap.xml", media_type="application/xml")

@app.get("/robots.txt", response_class=FileResponse)
async def robots():
    return FileResponse("robots.txt", media_type="text/plain")
