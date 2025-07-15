import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class sheetsClass():
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(os.environ["JSON_FILE_SHEETS"], self.scope)
        self.client = gspread.authorize(self.creds)
        self.spreadsheet = self.client.open_by_key(os.environ["ID_SHEETS"])
        self.sheet = self.spreadsheet.worksheet("dados")

    def adiciona_dados_desktop(self, desempenho, acessibilidade, boas_praticas, seo):
        novos_dados = [
            datetime.now().strftime("%Y-%m-%d"),
            desempenho,
            acessibilidade,
            boas_praticas,
            seo,
            "desktop"
        ]
        self.sheet.append_row(novos_dados)

    def adiciona_dados_mobile(self, desempenho, acessibilidade, boas_praticas, seo):
        novos_dados = [
            datetime.now().strftime("%Y-%m-%d"),
            desempenho,
            acessibilidade,
            boas_praticas,
            seo,
            "mobile"
        ]
        self.sheet.append_row(novos_dados)
