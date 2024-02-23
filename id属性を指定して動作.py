import time
from selenium.webdriver.common.by import By


"""
id属性を持つエレメントに対して動作します。
エレメントが見つからない場合や他のエラーが発生した場合、指定したスクロール量（pixel）でページをスクロールします。
指定したタイムアウト時間内にエレメントを見つけることができなかった場合、例外をスローします。

Args:
- driver (WebDriver): 使用するWebDriverのインスタンス。
- element_id (str): 対象とするエレメントのid属性。
- keys (str, optional): エレメントに送信するキー（テキストやファイルパスなど）。send_keys関数のみに適用。
- option_value (str, optional): 選択するセレクトボックスのオプションの値。select関数のみに適用。
- timeout (int, optional): エレメントを検索する最大時間。デフォルトは60秒。
- scroll_amount (int, optional): 例外が発生した際にページをスクロールする量。デフォルトは300pixel。

Raises:
- Exception: 指定したタイムアウト時間内にエレメントを見つけることができなかった場合。
"""


# テキストやファイル、画像などをアップロードする
def send_keys_to_element_by_id(driver, element_id, keys, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with ID '{element_id}'.")
        try:
            element = driver.find_element(By.ID, element_id)
            element.send_keys(keys)
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue


# エレメントをクリックする
def click_to_element_by_id(driver, element_id, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with ID '{element_id}'.")
        try:
            element = driver.find_element(By.ID, element_id)
            element.click()
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue


from selenium.webdriver.support.ui import Select

# セレクトボックスの特定のオプションを選択する
def select_to_element_by_id(driver, element_id, option_value, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for select box with ID '{element_id}'.")
        try:
            select_element = Select(driver.find_element(By.ID, element_id))
            select_element.select_by_value(option_value)
            break
        except:
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue

# テキストをreturn
def get_text_by_id(driver, element_id, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with ID '{element_id}'.")
        try:
            # 指定されたIDを持つ要素を見つける
            element = driver.find_element(By.ID, element_id)
            # 要素のテキストを取得して返す
            return element.text
        except:
            # 要素が見つからない場合は指定された量だけスクロールして再試行
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
