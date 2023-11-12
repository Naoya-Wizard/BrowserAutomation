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

#テキストやファイル、画像などをアップロードする
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


# クリックする
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

# indexを指定してクリックする
def click_element_by_name_and_index(driver, name, index, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element(s) with NAME '{name}'.")
        try:
            # 指定されたname属性を持つ全ての要素を取得
            elements = driver.find_elements(By.NAME, name)
            # 指定されたインデックスの要素をクリック
            elements[index].click()
            break
        except IndexError:
            # 指定されたインデックスの要素が存在しない場合
            raise Exception(f"No element found at index {index} with NAME '{name}'.")
        except Exception as e:
            # 要素が見つからない場合、ページをスクロールして再試行
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue


from selenium.webdriver.support.ui import Select

# セレクトボックスを選択する（option_value）
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

# セレクトボックスを選択する（option_text）
def select_option_by_name_and_visible_text(driver, name, option_text, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for select box with NAME '{name}'.")
        try:
            # 指定されたname属性を持つselect要素を見つける
            select_element = Select(driver.find_element(By.NAME, name))
            # 表示されているテキストに基づいてオプションを選択
            select_element.select_by_visible_text(option_text)
            break
        except Exception as e:
            # 要素が見つからない場合、ページをスクロールして再試行
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue
