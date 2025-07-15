from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from classes.sheetsClass import sheetsClass
import tempfile

class pageSpeed():
    def __init__(self, pageSpeed, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        user_data_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.pageSpeed = self.driver.get(pageSpeed)
        self.url = url
    
    # privado
    def __pega_dados_mobile(self):
        # pega dados do mobile

        SEO = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[2]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[4]/div[2]'))
        ).text
        boas_praticas = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[2]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[3]/div[2]'))
        ).text
        acessibilidade = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[2]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[2]/div[2]'))
        ).text
        desempenho = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[2]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[1]/div[2]'))
        ).text
        return SEO, boas_praticas, acessibilidade, desempenho

    # privado
    def __pega_dados_desktop(self):
        # pega dados do desktop
        desktop_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/span/button[2]'))
        )
        desktop_btn.click()

        SEO = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[4]/div[2]'))
        ).text
        boas_praticas = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[3]/div[2]'))
        ).text
        acessibilidade = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[2]/div[2]'))
        ).text
        desempenho = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/div[3]/div/div/div[3]/span/div/div[2]/div[2]/div/div/article/div/div[2]/div/div/div/div[2]/a[1]/div[2]'))
        ).text

        return SEO, boas_praticas, acessibilidade, desempenho

    # público
    def aplica_site(self):
        try:
            input = self.driver.find_element(By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/form/div[1]/label/input')
            input.click()
            input.send_keys(self.url)
            btn_input = self.driver.find_element(By.XPATH, '/html/body/c-wiz/div[2]/div/div[2]/form/div[2]/button')
            btn_input.click()

            seo_mobile, bp_mobile, acessibilidade_mobile, desempenho_mobile = self.__pega_dados_mobile()
            seo_desktop, bp_desktop, acessibilidade_desktop, desempenho_desktop = self.__pega_dados_desktop()

            df = sheetsClass()
            try:
                df.adiciona_dados_desktop(int(desempenho_desktop), int(acessibilidade_desktop), int(bp_desktop), int(seo_desktop))
                df.adiciona_dados_mobile(int(desempenho_mobile), int(acessibilidade_mobile), int(bp_mobile), int(seo_mobile))
                return 'Dados cadastrados na planilha'
            except Exception as err:
                return f'Erro ao cadastrar dados na planilha: {err}'
        finally:
            self.driver.quit()