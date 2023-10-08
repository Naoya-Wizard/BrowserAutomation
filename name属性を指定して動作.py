import time
from selenium.webdriver.common.by import By


"""
name属性を持つエレメントに対して動作します。
エレメントが見つからない場合や他のエラーが発生した場合、指定したスクロール量（pixel）でページをスクロールします。
指定したタイムアウト時間内にエレメントを見つけることができなかった場合、例外をスローします。

Args:
- driver (WebDriver): 使用するWebDriverのインスタンス。
- name (str): 対象とするエレメントのname属性。
- keys (str): エレメントに送信するキー。
- timeout (int, optional): エレメントを検索する最大時間。デフォルトは60秒。
- scroll_amount (int, optional): 例外が発生した際にページをスクロールする量。デフォルトは300pixel。

Raises:
- Exception: 指定したタイムアウト時間内にエレメントを見つけることができなかった場合。
"""


def send_keys_to_element_by_name(driver, name, keys, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with NAME '{name}'.")
        try:
            element = driver.find_element(By.NAME, name)
            element.send_keys(keys)
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue



def click_to_element_by_name(driver, name, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with NAME '{name}'.")
        try:
            element = driver.find_element(By.NAME, name)
            element.click()
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue



from selenium.webdriver.support.ui import Select

def select_to_element_by_name(driver, name, option_value, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for select box with NAME '{name}'.")
        try:
            select_element = Select(driver.find_element(By.NAME, name))
            select_element.select_by_value(option_value)
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue
