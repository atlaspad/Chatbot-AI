import openai
from pymongo import MongoClient
from my_secrets import CHATGPT_API_KEY

openai.api_key = CHATGPT_API_KEY

# MongoDB bağlantısını oluşturun
try:
    client = MongoClient('mongodb+srv://cuberium:cuberiumm@cluster0.v5kohjk.mongodb.net/')  # MongoDB bağlantı URL'sini güncelleyin
    db = client['ChatCBR_db']  # Veritabanı adını değiştirin (varsa)
except Exception as e:
    print(f"MongoDB bağlantısı oluşturulurken hata oluştu: {str(e)}")

# Konu başlıkları ve cevapları
topic_responses = {
    "blockchain": "",
    "yapay zeka": "",
    "yazılım": "",
    "makine öğrenmesi": "",
    "derin öğrenme": "",
    "software": "",
    "blokzincir": "",
    "zero knowledge": "",
    "artificial intelligence": "", 
    "machine learning": "",
    "deep learning": "", 
    "mina protocol": "",
    "launchpad": "", 
    "kripto": "", 
    "crypto":"",
    "sıfır bilgi ispatı": "", 
    "coin": "",
    "ethereum": "", 
    "solidity":"", 
    "evm":"", 
    "smart contract": "", 
    "akıllı kontrat": "",
}

def get_response(message):
    for topic, response in topic_responses.items():
        if topic in message.lower():
            if response:
                return response
            else:
                # OpenAI'den cevap al
                try:
                    messages = [{"role": "user", "content": message}]
                    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                    reply = chat.choices[0].message.content
                    topic_responses[topic] = reply  # Cevabı önbelleğe al
                    return reply
                except Exception as e:
                    print(f"OpenAI'den cevap alınırken hata oluştu: {str(e)}")
                    return "Üzgünüm, şu anda cevap veremiyorum."

    return "Üzgünüm, bu konuda size yardımcı olamam."

def kaydetSoruCevap(soru, cevap):
    try:
        # Soru ve cevapları veritabanına kaydedin
        sorular_collection = db['sorular']  # Sorular koleksiyonunu kullanın
        cevaplar_collection = db['cevaplar']  # Cevaplar koleksiyonunu kullanın

        sorular_collection.insert_one({"soru": soru})
        cevaplar_collection.insert_one({"cevap": cevap})
        print("Soru ve cevap veritabanına başarıyla kaydedildi.")
    except Exception as e:
        print(f"Veritabanına kayıt yapılırken hata oluştu: {str(e)}")

def chatCevapAl(message):
    try:
        # Özel cevaplar
        if "atlaspad" in message.lower():
            if "atlaspad nedir" in message.lower():
                return "Atlaspad, Mina Protocol'da kullanılan ZK-Launchpad teknolojisidir. Birden fazla blok zincirinde güvenli ve özel işlemlere olanak sağlamak için sıfır bilgi kanıtlarını kullanan ilk ve tek güvenilir Çapraz Zincir ZK Launchpad'i tanıtıyor. Bu son teknoloji platform, kullanıcıların şunları yapmasına olanak tanıyarak DeFi'deki acil gizlilik sorunlarına ve yüksek işlem maliyetlerine çözüm getiriyor."
            elif "atlaspad neden tasarlandı" in message.lower():
                return "Bu başlatma paneli, kullanıcılara varlıkları zincirler arasında gizli ve verimli bir şekilde taşıma özgürlüğünü sağlamak ve gizliliğin ve zincirler arası işlevselliğin sorunsuz bir şekilde bir arada var olduğu DeFi alanında yeni bir paradigmayı teşvik etmek için tasarlandı."
            elif "atlaspad hakkında bilgi ver" in message.lower():
                return "Günümüzün kripto para ekosisteminde, yatırımcılar arasında fırlatma rampalarının kullanımı giderek yaygınlaşarak çapraz ölçekli kripto varlık işlemlerini kolaylaştırıyor. Başlatma rampaları genellikle tek bir ağ tarafından desteklenen merkezi veya merkezi olmayan yapılardır. Kripto-ekonomik üçlemeye göre, eğer bir fırlatma rampası merkezileştirilirse güvenlik pahasına hız kazanabilir; merkezden dağıtılmışsa güvenilirlik sunar ancak işlem hızını olumsuz yönde etkileyebilir. Herhangi bir fırlatma rampası ve kullanıcıları, özellikle de yatırımcılar için temel sorunlar, güvenlik ve gizlilik etrafında dönüyor. Doğrulanmamış işlemler için tercih edilmelerine rağmen fırlatma rampaları, kripto finans sektöründe suiistimallere maruz kalıyor. Ayrıca bunlar doğrulandığında orantısız merkezileşme ve veri güvenliğinin istismar edilmesi gibi sorunlar ortaya çıkıyor. Üstelik MINA ağında herhangi bir zk-Launchpad'in bulunmaması ve MINA'nın auro cüzdanı dışında EVM uyumluluğunun stabil token eksikliği nedeniyle daha az tercih edilmesi, bizi tüm bu sorunları çözecek karar almaya yöneltti. . Bu sorunları geliştirici ekibimiz, deneyimli kadromuz ve tabii ki (zkproof) ile ele alarak, gerçek anlamda çözüm olarak gördüğümüz MINA ağına kullanıcı katılımını arttırırken, tamamen doğrulanabilen ve anonim olabilen bir sistem kurmayı hedefliyoruz.  Atlaspad bir projeden daha fazlasıdır; gizliliğin ölçeklenebilirlik ve birlikte çalışabilirlikle buluştuğu, DeFi'nin geleceğine adanmış, büyüyen bir ekosistemdir. Yolculuğumuz sürekli yenilik, işbirlikçi gelişim ve topluluğumuzun sarsılmaz desteğiyle güçleniyor."
            elif "teşekkürler" in message.lowe():
                return "Rica ederim. Her zaman buradayım..."
            else:
                return "Atlaspad hakkında ne sormak istediğinizi belirtir misiniz?"
            

        # Diğer belirli içeriklere cevap ver
        response = get_response(message)
        
        # Soru ve cevabı veritabanına kaydet
        kaydetSoruCevap(message, response)

        return response
    except Exception as e:
        print(f"ChatCevapAl işlevinde hata oluştu: {str(e)}")
        return None
