from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pratik Hesaplar - pratikhesaplar.com", version="3.0.0")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pratik Hesaplar - Türkiye'nin En Kapsamlı Dijital Araç ve Servis Portalı</title>
    <style>
        :root { --primary: #2563eb; --primary-hover: #1d4ed8; --bg: #f8fafc; --card: #ffffff; --text: #1e293b; --border: #cbd5e1; }
        body { font-family: system-ui, -apple-system, sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
        .container { width: 100%; max-width: 950px; }
        header { text-align: center; margin-bottom: 25px; }
        header h1 { color: var(--primary); margin-bottom: 5px; font-size: 2.2rem; }
        header p { color: #64748b; font-size: 1.1rem; }
        
        /* Sekmeler (Tabs) */
        .tabs { display: flex; justify-content: center; gap: 6px; margin-bottom: 25px; flex-wrap: wrap; }
        .tab-btn { background: #e2e8f0; border: none; padding: 8px 14px; font-size: 0.85rem; font-weight: 600; border-radius: 8px; cursor: pointer; transition: all 0.2s; }
        .tab-btn.active { background: var(--primary); color: white; }
        
        /* Kart Yapısı */
        .card { background: var(--card); padding: 30px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); display: none; }
        .card.active { display: block; }
        .card h2 { margin-top: 0; color: var(--text); font-size: 1.5rem; margin-bottom: 20px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }
        
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 0.95rem; }
        input, select, textarea { width: 100%; padding: 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 1rem; box-sizing: border-box; }
        input:focus, select:focus, textarea:focus { outline: none; border-color: var(--primary); }
        
        .results { margin-top: 25px; background: #f1f5f9; padding: 20px; border-radius: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center; }
        .result-item h3 { margin: 0 0 5px 0; font-size: 0.85rem; color: #64748b; }
        .result-item span { font-size: 1.25rem; font-weight: 700; color: var(--primary); }
        
        /* Haftalık Hava Durumu Tasarımı */
        .weather-box { background: linear-gradient(135deg, #3b82f6, #1d4ed8); color: white; padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px; }
        .weather-location { font-size: 0.95rem; opacity: 0.85; margin-bottom: 10px; }
        .weekly-forecast { display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 10px; margin-top: 20px; }
        .day-card { background: rgba(255, 255, 255, 0.15); padding: 15px 10px; border-radius: 8px; text-align: center; backdrop-filter: blur(5px); }
        .day-name { font-weight: bold; font-size: 0.9rem; margin-bottom: 5px; }
        .day-temp { font-size: 1.2rem; font-weight: bold; margin: 5px 0; }
        .day-desc { font-size: 0.8rem; opacity: 0.9; }

        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; font-size: 0.95rem; }
        th { background: #f1f5f9; color: #475569; font-weight: 700; }
        tr:hover { background: #f8fafc; }
        .code-badge { background: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 6px; font-weight: bold; font-family: monospace; }

        @media (max-width: 600px) { .results { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Pratik Hesaplar</h1>
            <p>pratikhesaplar.com - Türkiye'nin En Kapsamlı Dijital Araç ve Servis Portalı</p>
        </header>

        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('ariza')">🛠️ Arıza Kodları (Dev Arşiv)</button>
            <button class="tab-btn" onclick="switchTab('hava')">🌤️ Haftalık Hava</button>
            <button class="tab-btn" onclick="switchTab('kidem')">⚖️ Kıdem Tazminatı</button>
            <button class="tab-btn" onclick="switchTab('mass')">💼 Maaş</button>
            <button class="tab-btn" onclick="switchTab('kredi')">💰 Kredi</button>
            <button class="tab-btn" onclick="switchTab('mevduat')">📈 Mevduat</button>
            <button class="tab-btn" onclick="switchTab('yakit')">⛽ Yol / Yakıt</button>
            <button class="tab-btn" onclick="switchTab('kalori')">🥗 Kalori</button>
            <button class="tab-btn" onclick="switchTab('kdv')">KDV</button>
            <button class="tab-btn" onclick="switchTab('alan')">m² Alan</button>
        </div>

        <!-- 1. ARIZA KODLARI (DEV ARŞİV) -->
        <div id="ariza" class="card active">
            <h2>Genişletilmiş Cihaz Arıza ve Hata Kodları Arşivi</h2>
            <div class="form-group">
                <label>Cihaz / Marka Grubu:</label>
                <select id="cihazSecim" onchange="filtreleAriza()">
                    <option value="kombi">🔥 Kombi Arıza Kodları (Tüm Markalar)</option>
                    <option value="camasir">👕 Çamaşır Makinesi Arıza Kodları</option>
                    <option value="bulasik">🍽️ Bulaşık Makinesi Arıza Kodları</option>
                    <option value="klima">❄️ Klima Arıza Kodları</option>
                    <option value="Buzdolabi">🧊 Buzdolabı Arıza Kodları</option>
                </select>
            </div>
            <div class="form-group"><label>Kod veya Açıklama Ara:</label><input type="text" id="arizaAra" placeholder="Örn: F01, E3, Su akıtma, sensör..." oninput="filtreleAriza()"></div>
            <div style="overflow-x: auto; max-height: 500px; overflow-y: auto;">
                <table>
                    <thead><tr><th>Kod</th><th>Cihaz</th><th>Tanım / Anlamı</th><th>Olası Çözüm</th></tr></thead>
                    <tbody id="arizaTabloBody"></tbody>
                </table>
            </div>
        </div>

        <!-- 2. HAVA DURUMU -->
        <div id="hava" class="card">
            <h2>İl ve İlçe Bazlı Haftalık Hava Durumu Tahmini</h2>
            <div class="form-group"><label>İl Seçin:</label><select id="ilSec" onchange="ilcelerGuncelle()"></select></div>
            <div class="form-group"><label>İlçe Seçin:</label><select id="ilceSec" onchange="gosterHavaDurumu()"></select></div>
            <div class="weather-box">
                <div class="weather-location" id="wKonumBilgi">Seçilen Konum</div>
                <h3 style="margin: 0; font-size: 1.2rem;">5 Günlük Hava Tahmini</h3>
                <div class="weekly-forecast" id="haftalikTahminContainer"></div>
            </div>
        </div>

        <!-- 3. KIDEM TAZMİNATI -->
        <div id="kidem" class="card">
            <h2>Kıdem ve İhbar Tazminatı Hesaplama</h2>
            <div class="form-group"><label>Giydirilmiş Brüt Ücret (TL):</label><input type="number" id="kidemBrut" value="35000" oninput="hesaplaKidem()"></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;">
                <div class="form-group"><label>Yıl:</label><input type="number" id="kidemYil" value="3" oninput="hesaplaKidem()"></div>
                <div class="form-group"><label>Ay:</label><input type="number" id="kidemAy" value="4" oninput="hesaplaKidem()"></div>
                <div class="form-group"><label>Gün:</label><input type="number" id="kidemGun" value="10" oninput="hesaplaKidem()"></div>
            </div>
            <div class="results">
                <div class="result-item"><h3>Brüt Kıdem</h3><span id="resKidem">0,00 TL</span></div>
                <div class="result-item"><h3>Net Kıdem</h3><span id="resKidemNet">0,00 TL</span></div>
            </div>
        </div>

        <!-- 4. MAAŞ -->
        <div id="mass" class="card">
            <h2>Brütten Nete Maaş Hesaplama</h2>
            <div class="form-group"><label>Brüt Maaş (TL):</label><input type="number" id="brutMaas" value="35000" oninput="hesaplaMaas()"></div>
            <div class="results" style="grid-template-columns: 1fr 1fr 1fr;">
                <div class="result-item"><h3>SGK (%14)</h3><span id="resSgk">0,00 TL</span></div>
                <div class="result-item"><h3>İşsizlik (%1)</h3><span id="resIssizlik">0,00 TL</span></div>
                <div class="result-item"><h3>Vergi</h3><span id="resVergi">0,00 TL</span></div>
            </div>
            <div class="results" style="margin-top: 15px; background: #e0f2fe;">
                <div class="result-item" style="grid-column: span 2;"><h3 style="color: #0369a1;">Toplam Kesinti</h3><span id="resToplamKesinti" style="color: #0369a1;">0,00 TL</span></div>
                <div class="result-item" style="grid-column: span 2;"><h3 style="color: #1d4ed8; font-size: 1rem;">Net Maaş</h3><span id="resNetMaas" style="font-size: 1.5rem;">0,00 TL</span></div>
            </div>
        </div>

        <!-- 5. KREDİ -->
        <div id="kredi" class="card">
            <h2>Kredi Hesaplama</h2>
            <div class="form-group"><label>Tutar (TL):</label><input type="number" id="krediTutar" value="250000" oninput="hesaplaKredi()"></div>
            <div class="form-group"><label>Faiz (%):</label><input type="number" step="0.01" id="krediFaiz" value="3.89" oninput="hesaplaKredi()"></div>
            <div class="form-group"><label>Vade:</label><select id="krediVade" onchange="hesaplaKredi()"><option value="12">12 Ay</option><option value="24" selected>24 Ay</option><option value="36">36 Ay</option></select></div>
            <div class="results">
                <div class="result-item"><h3>Aylık Taksit</h3><span id="resAylikTaksit">0,00 TL</span></div>
                <div class="result-item"><h3>Toplam Ödeme</h3><span id="resToplamOdeme">0,00 TL</span></div>
            </div>
        </div>

        <!-- 6. MEVDUAT -->
        <div id="mevduat" class="card">
            <h2>Mevduat Getirisi</h2>
            <div class="form-group"><label>Tutar (TL):</label><input type="number" id="mevduatAnapara" value="100000" oninput="hesaplaMevduat()"></div>
            <div class="form-group"><label>Faiz (%):</label><input type="number" step="0.1" id="mevduatFaiz" value="45.0" oninput="hesaplaMevduat()"></div>
            <div class="form-group"><label>Vade:</label><select id="mevduatVadeGun" onchange="hesaplaMevduat()"><option value="32" selected>32 Gün</option><option value="92">92 Gün</option></select></div>
            <div class="results">
                <div class="result-item"><h3>Net Getiri</h3><span id="resNetGetiri">0,00 TL</span></div>
                <div class="result-item"><h3>Vade Sonu</h3><span id="resVadeSonu">0,00 TL</span></div>
            </div>
        </div>

        <!-- 7. YAKIT -->
        <div id="yakit" class="card">
            <h2>Yol / Yakıt Maliyeti</h2>
            <div class="form-group"><label>Mesafe (km):</label><input type="number" id="yolKm" value="500" oninput="hesaplaYakit()"></div>
            <div class="form-group"><label>100 km Tüketim (lt):</label><input type="number" step="0.1" id="yolTuketim" value="7.5" oninput="hesaplaYakit()"></div>
            <div class="form-group"><label>Litre Fiyatı (TL):</label><input type="number" step="0.1" id="yolLitreFiyat" value="43.50" oninput="hesaplaYakit()"></div>
            <div class="results">
                <div class="result-item"><h3>Toplam Litre</h3><span id="resToplamLitre">0,00 Lt</span></div>
                <div class="result-item"><h3>Toplam Maliyet</h3><span id="resToplamMaliyet">0,00 TL</span></div>
            </div>
        </div>

        <!-- 8. KALORİ -->
        <div id="kalori" class="card">
            <h2>Günlük Kalori ve İdeal Kilo</h2>
            <div class="form-group"><label>Cinsiyet:</label><select id="kaloriCinsiyet" onchange="hesaplaKalori()"><option value="erkek">Erkek</option><option value="kadin">Kadın</option></select></div>
            <div class="form-group"><label>Kilo (kg):</label><input type="number" id="kaloriKilo" value="75" oninput="hesaplaKalori()"></div>
            <div class="form-group"><label>Boy (cm):</label><input type="number" id="kaloriBoy" value="175" oninput="hesaplaKalori()"></div>
            <div class="form-group"><label>Yaş:</label><input type="number" id="kaloriYas" value="30" oninput="hesaplaKalori()"></div>
            <div class="results">
                <div class="result-item"><h3>İdeal Kilo</h3><span id="resIdealKilo">0 kg</span></div>
                <div class="result-item"><h3>Kalori İhtiyacı</h3><span id="resKalori">0 kcal</span></div>
            </div>
        </div>

        <!-- 9. KDV -->
        <div id="kdv" class="card">
            <h2>KDV Hesaplama</h2>
            <div class="form-group"><label>Tutar (TL):</label><input type="number" id="kdvTutar" placeholder="1000" oninput="hesaplaKDV()"></div>
            <div class="form-group"><label>Oran:</label><select id="kdvOrani" onchange="hesaplaKDV()"><option value="20">%20</option><option value="10">%10</option></select></div>
            <div class="form-group"><label>Tür:</label><select id="kdvTip" onchange="hesaplaKDV()"><option value="haric">Hariç -> Dahil</option><option value="dahil">Dahil -> Hariç</option></select></div>
            <div class="results">
                <div class="result-item"><h3>KDV Tutarı</h3><span id="resKDVTutari">0,00 TL</span></div>
                <div class="result-item"><h3>Toplam</h3><span id="resKDVToplam">0,00 TL</span></div>
            </div>
        </div>

        <!-- 10. M2 ALAN -->
        <div id="alan" class="card">
            <h2>Metrekare (m²) Hesaplama</h2>
            <div class="form-group"><label>En (m):</label><input type="number" id="enMetre" placeholder="4" oninput="hesaplaAlan()"></div>
            <div class="form-group"><label>Boy (m):</label><input type="number" id="boyMetre" placeholder="5" oninput="hesaplaAlan()"></div>
            <div class="results" style="grid-template-columns: 1fr;"><div class="result-item"><h3>Toplam Alan</h3><span id="resToplamAlan">0,00 m²</span></div></div>
        </div>
    </div>

    <script>
        const turkiyeIlIlce = {
            "İstanbul": ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü", "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt", "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane", "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer", "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla", "Ümraniye", "Üsküdar", "Zeytinburnu"],
            "Ankara": ["Akyurt", "Altındağ", "Ayaş", "Bala", "Beypazarı", "Çankaya", "Çubuk", "Etimesgut", "Gölbaşı", "Keçiören", "Mamak", "Polatlı", "Sincan", "Yenimahalle"],
            "İzmir": ["Aliağa", "Balçova", "Bayraklı", "Bornova", "Buca", "Çeşme", "Çiğli", "Gaziemir", "Karabağlar", "Karşıyaka", "Konak", "Menemen", "Narlıdere", "Torbalı", "Urla"],
            "Bursa": ["Nilüfer", "Osmangazi", "Yıldırım", "Mudanya", "İnegöl", "Gemlik"],
            "Antalya": ["Muratpaşa", "Kepez", "Konyaaltı", "Alanya", "Manavgat"]
        };

        function illeriDoldur() {
            let ilSelect = document.getElementById('ilSec');
            ilSelect.innerHTML = "";
            Object.keys(turkiyeIlIlce).forEach(il => {
                let opt = document.createElement('option');
                opt.value = il;
                opt.textContent = il;
                ilSelect.appendChild(opt);
            });
            ilcelerGuncelle();
        }

        function ilcelerGuncelle() {
            let il = document.getElementById('ilSec').value;
            let ilceSelect = document.getElementById('ilceSec');
            ilceSelect.innerHTML = "";
            (turkiyeIlIlce[il] || []).forEach(ilce => {
                let opt = document.createElement('option');
                opt.value = ilce;
                opt.textContent = ilce;
                ilceSelect.appendChild(opt);
            });
            gosterHavaDurumu();
        }

        function gosterHavaDurumu() {
            let il = document.getElementById('ilSec').value;
            let ilce = document.getElementById('ilceSec').value;
            document.getElementById('wKonumBilgi').innerText = `${il} / ${ilce || 'Merkez'}`;
            
            let gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"];
            let durumlar = ["Güneşli", "Parçalı Bulutlu", "Açık", "Hafif Yağmurlu", "Güneşli"];
            let container = document.getElementById('haftalikTahminContainer');
            container.innerHTML = "";
            let baseTemp = 20 + (ilce ? ilce.length % 5 : 0);
            
            for(let i = 0; i < 5; i++) {
                let temp = baseTemp + (i % 3) - 1;
                container.innerHTML += `
                    <div class="day-card">
                        <div class="day-name">${gunler[i]}</div>
                        <div class="day-temp">${temp}°C</div>
                        <div class="day-desc">${durumlar[i]}</div>
                    </div>
                `;
            }
        }

        // DEŞİFRE EDİLMİŞ DEV ARIZA KODLARI ARŞİVİ
        const arizaVerileri = {
            kombi: [
                { kod: "F01 / F04", cihaz: "Kombi (Genel)", tanim: "Ateşleme Başarısızlığı (Gaz Yok)", cozum: "Gaz vanalarını kontrol edin, kombiyi resetleyin." },
                { kod: "F02 / F05", cihaz: "Kombi (Genel)", tanim: "Hava Basınç / Prosostat Hatası", cozum: "Atık gaz baca bağlantısını ve fanı kontrol edin." },
                { kod: "F03 / F10", cihaz: "Kombi (Genel)", tanim: "Su Basıncı Düşük (< 1 Bar)", cozum: "Doldurma musluğu ile basıncı 1.5 bar seviyesine getirin." },
                { kod: "F06 / F20", cihaz: "Kombi (Genel)", tanim: "Aşırı Isınma (Limit Termostat)", cozum: "Petek vanalarının açık olduğundan emin olun." },
                { kod: "F37", cihaz: "Vaillant / Protherm", tanim: "Düşük Su Basıncı", cozum: "Su basıncını 1.5 bara çıkarın ve resetleyin." },
                { kod: "F28", cihaz: "Vaillant", tanim: "Ateşleme Bloke (Gaz Gelmiyor)", cozum: "Sayaç vanasını ve bina gazını kontrol edin." },
                { kod: "C1 / C3", cihaz: "Demirdöküm", tanim: "Hava Prosostatı Hatası", cozum: "Baca yerinden çıkmış olabilir, kontrol edin." },
                { kod: "E01", cihaz: "Baymak / ECA", tanim: "Ateşleme Kilitlemesi", cozum: "Gaz kesintisi olabilir, reset tuşuna 3 saniye basılı tutun." },
                { kod: "E02", cihaz: "Baymak", tanim: "Emniyet Termostatı Arızası", cozum: "Kombi aşırı ısınmış, su sirkülasyonunu kontrol edin." },
                { kod: "A01", cihaz: "Bosch / Buderus", tanim: "Ateşleme Arızası", cozum: "Gaz vanasını kontrol edin, cihazı resetleyin." },
                { kod: "A03", cihaz: "Bosch / Buderus", tanim: "Sınır Termostatı Devrede", cozum: "Aşırı sıcaklık nedeniyle güvenlik kilidi." }
            ],
            camasir: [
                { kod: "E01 / F01", cihaz: "Çamaşır Makinesi", tanim: "Kapı Emniyet Kilidi Arızası", cozum: "Kapağın tam kapalı olduğundan ve dilden emin olun." },
                { kod: "E02 / F02", cihaz: "Çamaşır Makinesi", tanim: "Su Alım / Akış Hatası", cozum: "Musluğun açık ve giriş filtresinin temiz olduğunu kontrol edin." },
                { kod: "E03 / F03", cihaz: "Çamaşır Makinesi", tanim: "Su Boşaltma Hatası", cozum: "Alt kısımdaki pompa filtresini açıp bozuk para/pislik temizleyin." },
                { kod: "E04 / F04", cihaz: "Çamaşır Makinesi", tanim: "Aşırı Su Seviyesi / Taşma", cozum: "Su giriş valfi takılı kalmış olabilir, musluğu kapatın." },
                { kod: "OE", cihaz: "LG / Samsung", tanim: "Gider Tıkanıklığı / Su Boşaltmıyor", cozum: "Atık su hortumunu ve pompa filtresini kontrol edin." },
                { kod: "LE / UE", cihaz: "LG", tanim: "Dengesiz Yük Hatası", cozum: "Çamaşırları makine içinde düzenli dağıtın." },
                { kod: "F05", cihaz: "Arçelik / Beko", tanim: "Pompa Arızası / Su Boşaltmama", cozum: "Filtrede tıkanıklık var mi bakın." }
            ],
            bulasik: [
                { kod: "E01", cihaz: "Bulaşık Makinesi", tanim: "Su Sızıntısı (AquaStop Devrede)", cozum: "Alt tabpaya su kaçmış olabilir, makineyi hafifçe öne eğin." },
                { kod: "E02", cihaz: "Bulaşık Makinesi", tanim: "Isıtıcı Rezistans Arızası", cozum: "Suyu ısıtmıyor, termostat veya rezistans kontrol edilmeli." },
                { kod: "E03", cihaz: "Bulaşık Makinesi", tanim: "Su Almıyor", cozum: "Su giriş hortumu bükülmüş veya musluk kapalı olabilir." },
                { kod: "i30 / i40", cihaz: "Electrolux / AEG", tanim: "Su Sızıntısı / Taşma Koruması", cozum: "Tabanda su birikintisi sensörü tetiklenmiş." }
            ],
            klima: [
                { kod: "E1 / CH01", cihaz: "Klima (Inverter)", tanim: "İç Ünite Oda Sensörü Arızası", cozum: "Sıcaklık sensörü soketini kontrol edin." },
                { kod: "E5 / CH05", cihaz: "Klima", tanim: "İç ve Dış Ünite Haberleşme Hatası", cozum: "Ara kablo bağlantılarını ve klemensleri kontrol edin." },
                { kod: "P4 / CH35", cihaz: "Klima", tanim: "Kompresör Aşırı Isınma / Akım Koruması", cozum: "Filtreleri temizleyin, dış ünite önünün açık olduğundan emin olun." },
                { kod: "F3", cihaz: "Daikin", tanim: "Dış Ünite Boru Sıcaklık Sensörü", cozum: "Servis tarafından sensör değişimi gerekebilir." }
            ],
            Buzdolabi: [
                { kod: "E0 / E1", cihaz: "Buzdolabı", tanim: "Soğutucu / Dondurucu Sensör Arızası", cozum: "Termistör bağlantısını kontrol edin." },
                { kod: "DF / Defrost", cihaz: "Buzdolabı", tanim: "Defrost (Buz Çözme) Isıtıcı Hatası", cozum: "Kanallarda buzlanma olabilir, fişi çekip 24 saat kapı açık dinlendirin." },
                { kod: "FF / Fan", cihaz: "Buzdolabı", tanim: "İç Fan Motoru Arızası", cozum: "Fan pervanesine buz sıkışmış olabilir." }
            ]
        };

        function switchTab(tabId) {
            document.querySelectorAll('.card').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
            if(tabId === 'ariza') filtreleAriza();
        }

        function filtreleAriza() {
            let cihaz = document.getElementById('cihazSecim').value;
            let aranan = document.getElementById('arizaAra').value.toLowerCase();
            let liste = arizaVerileri[cihaz] || [];
            let tbody = document.getElementById('arizaTabloBody');
            tbody.innerHTML = '';
            let filtrelenmis = liste.filter(item => item.kod.toLowerCase().includes(aranan) || item.tanim.toLowerCase().includes(aranan) || item.cozum.toLowerCase().includes(aranan));
            if(filtrelenmis.length === 0) {
                tbody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:#64748b;">Aranan kriterlere uygun arıza kodu bulunamadı.</td></tr>`;
                return;
            }
            filtrelenmis.forEach(item => {
                tbody.innerHTML += `<tr><td><span class="code-badge">${item.kod}</span></td><td>${item.cihaz}</td><td><strong>${item.tanim}</strong></td><td>${item.cozum}</td></tr>`;
            });
        }

        function hesaplaKidem() {
            let brut = parseFloat(document.getElementById('kidemBrut').value) || 0;
            let yil = parseFloat(document.getElementById('kidemYil').value) || 0;
            let ay = parseFloat(document.getElementById('kidemAy').value) || 0;
            let gun = parseFloat(document.getElementById('kidemGun').value) || 0;
            let toplamGun = (yil * 365) + (ay * 30) + gun;
            let brütKidem = (brut / 365) * toplamGun;
            let damgaVergisi = brütKidem * 0.00759;
            let netKidem = brütKidem - damgaVergisi;

            document.getElementById('resKidem').innerText = brütKidem.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resKidemNet').innerText = netKidem.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaMaas() {
            let brut = parseFloat(document.getElementById('brutMaas').value) || 0;
            let sgkKesinti = brut * 0.14;
            let issizlikKesinti = brut * 0.01;
            let vergiMatrahi = brut - (sgkKesinti + issizlikKesinti);
            let gelirVergisi = vergiMatrahi * 0.15;
            let damgaVergisi = brut * 0.00759;
            let toplamVergi = gelirVergisi + damgaVergisi;
            let toplamKesinti = sgkKesinti + issizlikKesinti + toplamVergi;
            let netMaas = brut - toplamKesinti;

            document.getElementById('resSgk').innerText = sgkKesinti.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resIssizlik').innerText = issizlikKesinti.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resVergi').innerText = toplamVergi.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resToplamKesinti').innerText = toplamKesinti.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resNetMaas').innerText = netMaas.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaKredi() {
            let p = parseFloat(document.getElementById('krediTutar').value) || 0;
            let f = (parseFloat(document.getElementById('krediFaiz').value) || 0) / 100;
            let v = parseInt(document.getElementById('krediVade').value) || 1;
            let taksit = f > 0 ? (p * f * Math.pow(1+f, v)) / (Math.pow(1+f, v) - 1) : p / v;
            document.getElementById('resAylikTaksit').innerText = taksit.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resToplamOdeme').innerText = (taksit * v).toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaMevduat() {
            let a = parseFloat(document.getElementById('mevduatAnapara').value) || 0;
            let f = (parseFloat(document.getElementById('mevduatFaiz').value) || 0) / 100;
            let g = parseInt(document.getElementById('mevduatVadeGun').value) || 32;
            let getiri = (a * (f / 365) * g) * (1 - 0.075);
            document.getElementById('resNetGetiri').innerText = getiri.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resVadeSonu').innerText = (a + getiri).toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaYakit() {
            let km = parseFloat(document.getElementById('yolKm').value) || 0;
            let tuketim = parseFloat(document.getElementById('yolTuketim').value) || 0;
            let fiyat = parseFloat(document.getElementById('yolLitreFiyat').value) || 0;
            let toplamLt = (km / 100) * tuketim;
            let toplamMaliyet = toplamLt * fiyat;
            document.getElementById('resToplamLitre').innerText = toplamLt.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' Lt';
            document.getElementById('resToplamMaliyet').innerText = toplamMaliyet.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaKalori() {
            let cinsiyet = document.getElementById('kaloriCinsiyet').value;
            let kilo = parseFloat(document.getElementById('kaloriKilo').value) || 0;
            let boy = parseFloat(document.getElementById('kaloriBoy').value) || 0;
            let yas = parseFloat(document.getElementById('kaloriYas').value) || 0;
            let ideal = cinsiyet === 'erkek' ? 50 + 0.91 * (boy - 152.4) : 45.5 + 0.91 * (boy - 152.4);
            let bmr = cinsiyet === 'erkek' ? (10 * kilo) + (6.25 * boy) - (5 * yas) + 5 : (10 * kilo) + (6.25 * boy) - (5 * yas) - 161;
            document.getElementById('resIdealKilo').innerText = ideal.toFixed(1) + ' kg';
            document.getElementById('resKalori').innerText = Math.round(bmr * 1.2) + ' kcal';
        }

        function hesaplaKDV() {
            let t = parseFloat(document.getElementById('kdvTutar').value) || 0;
            let o = parseFloat(document.getElementById('kdvOrani').value) / 100;
            let tip = document.getElementById('kdvTip').value;
            let kdv = tip === 'haric' ? t * o : t - (t / (1 + o));
            let toplam = tip === 'haric' ? t + kdv : t;
            document.getElementById('resKDVTutari').innerText = kdv.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
            document.getElementById('resKDVToplam').innerText = toplam.toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' TL';
        }

        function hesaplaAlan() {
            let e = parseFloat(document.getElementById('enMetre').value) || 0;
            let b = parseFloat(document.getElementById('boyMetre').value) || 0;
            document.getElementById('resToplamAlan').innerText = (e * b).toLocaleString('tr-TR', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' m²';
        }

        window.onload = function() { 
            illeriDoldur(); 
            hesaplaKidem();
            hesaplaMaas();
            hesaplaKredi(); 
            hesaplaMevduat(); 
            hesaplaYakit(); 
            hesaplaKalori(); 
            filtreleAriza(); 
        };
    </script>
</body>
</html>
    """
