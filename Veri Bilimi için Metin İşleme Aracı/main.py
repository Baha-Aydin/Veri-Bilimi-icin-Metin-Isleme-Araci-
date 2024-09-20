import json
import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Metinleri içeren bir txt dosyasını oku
with open('metinler.txt', 'r', encoding='utf-8') as file:
    metinler = file.readlines()

print("Metinler dosyası okundu.")

# Veri seti oluştur
veri_seti = []

for i, metin in enumerate(metinler):
    metin = metin.strip()
    
    # Cümlenin özelliklerini hesapla
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    karakter_sayisi = len(metin)
    ortalama_kelime_uzunlugu = karakter_sayisi / kelime_sayisi if kelime_sayisi > 0 else 0

    # Bit değerlerini oluştur
    bit_degerleri = []
    toplam_bit = 0

    for karakter in metin:
        bit_degeri = format(ord(karakter), '08b')
        bit_degerleri.append({"karakter": karakter, "bit_degeri": bit_degeri})
        toplam_bit += len(bit_degeri)

    # Cümle verisini oluştur
    cümle_verisi = {
        "id": i + 1,
        "metin": metin,
        "kelime_sayisi": kelime_sayisi,
        "karakter_sayisi": karakter_sayisi,
        "ortalama_kelime_uzunlugu": ortalama_kelime_uzunlugu,
        "toplam_bit": toplam_bit,
        "bit_degerleri": bit_degerleri
    }

    veri_seti.append(cümle_verisi)

print(f"Veri seti oluşturuldu: {len(veri_seti)} metin.")

# Özellikleri ve etiketleri hazırlama
metinler = [item['metin'] for item in veri_seti]
etiketler = [random.choice([0, 1]) for _ in metinler]  # Rastgele etiketler

# Eğitim ve doğrulama seti oluştur
X_train, X_val, y_train, y_val = train_test_split(metinler, etiketler, test_size=0.2, random_state=42)

# Özellikleri çıkar
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_val_counts = vectorizer.transform(X_val)

# Modeli eğit
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Doğrulama seti ile değerlendirme
y_pred = model.predict(X_val_counts)
dogruluk = accuracy_score(y_val, y_pred)

print(f"Model Doğruluğu: {dogruluk:.2f}")

# JSON formatında çıktı al
json_veri_seti = {"veri_seti": veri_seti}
json_str = json.dumps(json_veri_seti, ensure_ascii=False, indent=4)

# Sonucu ekrana yazdır
print("JSON formatında veri seti:")
print(json_str)

# JSON verisini bir dosyaya kaydet
with open('veri_seti.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_veri_seti, json_file, ensure_ascii=False, indent=4)
print("JSON verisi 'veri_seti.json' dosyasına kaydedildi.")

# Çıkmak için bir tuşa basın
input("Çıkmak için bir tuşa basın...")
