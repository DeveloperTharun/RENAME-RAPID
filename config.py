import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "8754146")

API_HASH = os.environ.get("API_HASH", "8b56a6989f6d04f6f4fe78133ade02fd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6872825009:AAETLKD9mHVQKS_SDxLa_Udfdl3OUK_dQXU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Rapid_Bots") 

DB_NAME = os.environ.get("DB_NAME","Skmedia")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://SkMedia:Tharunraj1828@cluster0.vbdxs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "100"))

START_PIC = os.environ.get("START_PIC", "https://www.linkpicture.com/q/IMG_20221209_092716_970.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1632597748').split()]
