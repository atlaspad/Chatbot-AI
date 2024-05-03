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
    "blockchain": "", "blokzincir": "",
    "yazılım": "", "software": "",
    "zero knowledge": "", "sıfır bilgi ispatı": "", 
    "artificial intelligence": "", "yapay zeka": "", "machine learning": "", "deep learning": "", "derin öğrenme": "", "makine öğrenmesi": "",
    "mina protocol": "", "launchpad": "", 
    "kripto": "", "crypto":"", "coin": "",
    "ethereum": "", "solidity":"", "evm":"", 
    "smart contract": "", "akıllı kontrat": "",
    "merhaba": "","greetings": "", 
    "hi": "", "hello": "",
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
        print("Please note, while the Atlaspad Ai aims to be helpful, it is currently in its beta phase. We encourage you to explore its capabilities, but remind you that it may not always provide perfect answers. Your feedback during this beta phase is invaluable and will help us improve its accuracy and functionality. Enjoy the conversation and let us know your thoughts!")
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
            elif "what is atlaspad" in message.lower():
                return "AtlasPad is a cross-chain ZK Launchpad platform that enables secure and private transactions across multiple blockchain networks."
            elif "what is the main purpose of atlasPad" in message.lower():
                return "AtlasPad aims to solve the urgent privacy issues and high transaction costs in DeFi by using zero-knowledge proofs, allowing secure and private transactions across multiple blockchain networks."
            elif "give information about atlaspad" in message.lower():
                return "In today's cryptocurrency ecosystem, the use of launch pads is becoming increasingly common among investors, facilitating cross-scale crypto asset transactions. Launchpads are generally centralized or decentralized structures supported by a single network. According to the crypto-economic trilogy, if a launchpad is centralized it can gain momentum at the expense of security; If decentralized, it offers reliability but may negatively impact transaction speed. The key issues for any launchpad and its users, especially investors, revolve around security and privacy. Although preferred for unverified transactions, launchpads are subject to abuses in the crypto finance industry. Additionally, when these are verified, problems such as disproportionate centralization and abuse of data security arise. Moreover, the absence of any zk-Launchpad on the MINA network and the fact that EVM compatibility other than MINA's auro wallet is less preferred due to the lack of stable tokens, led us to make a decision to solve all these problems. . By addressing these problems with our developer team, experienced staff and of course (zkproof), we aim to establish a system that can be fully verified and anonymous while increasing user participation in the MINA network, which we see as a real solution. Atlaspad is more than a project; is a growing ecosystem dedicated to the future of DeFi, where privacy meets scalability and interoperability. Our journey is fueled by continuous innovation, collaborative development, and the unwavering support of our community."
            elif "how can users utilize atlasPad" in message.lower():
                return "Users can participate in upcoming projects' pre-sales by staking on the platform across multiple blockchain networks."
            elif "what are the security features of AtlasPad" in message.lower():
                return "AtlasPad is recognized as the gold standard for security and reliability in the crypto industry. It employs stringent security measures such as smart contracts and zero-knowledge-based technology."
            elif "how can  join the community" in message.lower():
                return "You can join our community through our Linktree: https://linktr.ee/atlaspad"
            elif "atlaspad neden tasarlandı" in message.lower():
                return "Bu başlatma paneli, kullanıcılara varlıkları zincirler arasında gizli ve verimli bir şekilde taşıma özgürlüğünü sağlamak ve gizliliğin ve zincirler arası işlevselliğin sorunsuz bir şekilde bir arada var olduğu DeFi alanında yeni bir paradigmayı teşvik etmek için tasarlandı."
            elif "atlaspad hakkında bilgi ver" in message.lower():
                return "Günümüzün kripto para ekosisteminde, yatırımcılar arasında fırlatma rampalarının kullanımı giderek yaygınlaşarak çapraz ölçekli kripto varlık işlemlerini kolaylaştırıyor. Başlatma rampaları genellikle tek bir ağ tarafından desteklenen merkezi veya merkezi olmayan yapılardır. Kripto-ekonomik üçlemeye göre, eğer bir fırlatma rampası merkezileştirilirse güvenlik pahasına hız kazanabilir; merkezden dağıtılmışsa güvenilirlik sunar ancak işlem hızını olumsuz yönde etkileyebilir. Herhangi bir fırlatma rampası ve kullanıcıları, özellikle de yatırımcılar için temel sorunlar, güvenlik ve gizlilik etrafında dönüyor. Doğrulanmamış işlemler için tercih edilmelerine rağmen fırlatma rampaları, kripto finans sektöründe suiistimallere maruz kalıyor. Ayrıca bunlar doğrulandığında orantısız merkezileşme ve veri güvenliğinin istismar edilmesi gibi sorunlar ortaya çıkıyor. Üstelik MINA ağında herhangi bir zk-Launchpad'in bulunmaması ve MINA'nın auro cüzdanı dışında EVM uyumluluğunun stabil token eksikliği nedeniyle daha az tercih edilmesi, bizi tüm bu sorunları çözecek karar almaya yöneltti. . Bu sorunları geliştirici ekibimiz, deneyimli kadromuz ve tabii ki (zkproof) ile ele alarak, gerçek anlamda çözüm olarak gördüğümüz MINA ağına kullanıcı katılımını arttırırken, tamamen doğrulanabilen ve anonim olabilen bir sistem kurmayı hedefliyoruz.  Atlaspad bir projeden daha fazlasıdır; gizliliğin ölçeklenebilirlik ve birlikte çalışabilirlikle buluştuğu, DeFi'nin geleceğine adanmış, büyüyen bir ekosistemdir. Yolculuğumuz sürekli yenilik, işbirlikçi gelişim ve topluluğumuzun sarsılmaz desteğiyle güçleniyor."
            else:
                return "Could you please specify what you want to ask about Atlaspad?"
        elif "teşekkürler" in message.lower():
            return "Rica ederim. Her zaman buradayım..."
        elif "thanks" in message.lower():
            return "You're welcome I'm always here..."    

        # Diğer belirli içeriklere cevap ver
        response = get_response(message)
        
        # Soru ve cevabı veritabanına kaydet
        kaydetSoruCevap(message, response)

        return response
    except Exception as e:
        print(f"ChatCevapAl işlevinde hata oluştu: {str(e)}")
        return None
