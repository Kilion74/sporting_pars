import bs4
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.headless = True

while True:
    print('Нажмите ENTER для продолжения...')
    input()
    print('Выберите вид спорта: футбол, хоккей, баскетюол, волейбол')
    name = input().lower()
    sport_name = ''
    if name == 'футбол':
        sport_name = 'football'
    elif name == 'хоккей':
        sport_name = 'hockey'
    elif name == 'баскетюол':
        sport_name = 'basketball'
    elif name == 'волейбол':
        sport_name = 'volleyball'
    else:
        print('Введите корректные данные...')

    print('Введите дату результатов в формате: гггг-мм-дд')
    time_result = input()
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) as driver:  # Открываем хром
        driver.get(f"https://www.championat.com/stat/{sport_name}/#{time_result}")  # Открываем страницу
        time.sleep(3)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        names = soup.find_all('a', class_='title__link')
        name_1 = names[0].text.strip()
        print(name_1)
        results = soup.find_all('div', class_='mc-sport-tournament__drop-block')
        for des in results[0].find_all('a'):
            result_1 = des.find_next('div', class_='results-item__title-date')
            print(result_1.text.strip())
            commands = des.find_next('div', class_='results-item__title-name')
            print(commands.text.strip())
            status = des.find_next('div', class_='results-item__status')
            print(status.text.strip())
            itog = des.find_next('div', class_='results-item__result')
            print(itog.text.strip())
            print('\n')
        name_2 = names[1].text.strip()
        print(name_2)
        for des in results[1].find_all('a'):
            result_1 = des.find_next('div', class_='results-item__title-date')
            print(result_1.text.strip())
            commands = des.find_next('div', class_='results-item__title-name')
            print(commands.text.strip())
            status = des.find_next('div', class_='results-item__status')
            print(status.text.strip())
            itog = des.find_next('div', class_='results-item__result')
            print(itog.text.strip())
            print('\n')
        name_3 = names[2].text.strip()
        print(name_3)
        for des in results[2].find_all('a'):
            result_1 = des.find_next('div', class_='results-item__title-date')
            print(result_1.text.strip())
            commands = des.find_next('div', class_='results-item__title-name')
            print(commands.text.strip())
            status = des.find_next('div', class_='results-item__status')
            print(status.text.strip())
            itog = des.find_next('div', class_='results-item__result')
            print(itog.text.strip())
            print('\n')
        try:
            name_4 = names[3].text.strip()
            print(name_4)
            for des in results[3].find_all('a'):
                result_1 = des.find_next('div', class_='results-item__title-date')
                print(result_1.text.strip())
                commands = des.find_next('div', class_='results-item__title-name')
                print(commands.text.strip())
                status = des.find_next('div', class_='results-item__status')
                print(status.text.strip())
                itog = des.find_next('div', class_='results-item__result')
                print(itog.text.strip())
                print('\n')
        except:
            print('Результаты отсутствуют')



