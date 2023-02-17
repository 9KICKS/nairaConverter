import requests

url = "https://api.exchangerate-api.com/v4/latest/NGN"

response = requests.get(url)
data = response.json()

usd = data["rates"]["USD"]
eur = data["rates"]["EUR"]
jpy = data["rates"]["JPY"]
gbp = data["rates"]["GBP"]
aud = data["rates"]["AUD"]
cad = data["rates"]["CAD"]
zar = data["rates"]["ZAR"]

ngn = float(input("Enter the amount of naira you want to convert: "))

usd = ngn * usd
eur = ngn * eur
jpy = ngn * jpy
gbp = ngn * gbp
aud = ngn * aud
cad = ngn * cad
zar = ngn * zar

print(f"₦{ngn} = USD ${usd}")
print(f"₦{ngn} = EURO €{eur}")
print(f"₦{ngn} = JAPANESE YEN ¥{jpy}")
print(f"₦{ngn} = GREAT BRITISH POUND £{gbp}")
print(f"₦{ngn} = AUSTRALIAN DOLLAR ${aud}")
print(f"₦{ngn} = CANADIAN DOLLAR ${cad}")
print(f"₦{ngn} = SOUTH AFRICAN RAND R{zar}")
