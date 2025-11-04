from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText

amazon_page = 'https://www.amazon.com.br/Encordoamento-Guitarra-Ernie-Ball-P02221/dp/B0002M6CVC/ref=asc_df_B0002M6CVC?mcid=110b3a57d6c83e39b8dd46f4376bc54e&tag=googleshopp00-20&linkCode=df0&hvadid=709964503115&hvpos=&hvnetw=g&hvrand=5438358542595568917&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9100442&hvtargid=pla-406644542335&language=pt_BR&gad_source=1&th=1'
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
           "Accept-Encoding": "gzip, deflate, br, zstd",
           "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,pt-PT;q=0.5",
           "Priority": "u=0, i",
           "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
           "Sec-Ch-Ua-Mobile": "?0",
           "Sec-Ch-Ua-Platform": "\"Windows\"",
           "Sec-Fetch-Dest": "document",
           "Sec-Fetch-Mode": "navigate",
           "Sec-Fetch-Site": "cross-site",
           "Sec-Fetch-User": "?1",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
           }

response = requests.get(amazon_page, headers=headers)
web_page = response.text
print(web_page)
soup = BeautifulSoup(web_page, 'html.parser')
scrapy_price = soup.find('span', class_='a-offscreen')
print(scrapy_price)
preco = scrapy_price.getText()

preco_float = float(preco)

#-----------------------------------------------------------------

smtp_server = 'smtp.gmail.com'
smtp_port = 465
smtp_password = ''
from_addr = 'renato.asterio2@gmail.com'
to_addr = 'renato.asterio2@gmail.com'
subject = 'Amazon Price Alert'
body = f'ta barato: {preco_float}'

def send_email(subject, body, sender, recipients , password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    with smtplib.SMTP_SSL(host=smtp_server, port=smtp_port) as server:
        server.login(user=sender, password=password)
        server.sendmail(from_addr=sender, to_addrs=recipients, msg=msg.as_string())
    print('mensagem mandada')

if preco_float <= 100:
    send_email(subject,body,from_addr,to_addr,smtp_password)
