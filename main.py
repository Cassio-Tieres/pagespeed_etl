import schedule
from time import sleep
from classes.pageSpeedClass import pageSpeed
from datetime import datetime

def rodar_auditoria():
    print(f"Rodando auditoria: {datetime.now()}")
    page = pageSpeed('https://pageSpeed.web.dev', '')
    page.aplica_site()
rodar_auditoria()


schedule.every().day.at("08:20").do(rodar_auditoria)

print("⏰ Aguardando execução diária às 08:20...")

while True:
    schedule.run_pending()
    sleep(1)