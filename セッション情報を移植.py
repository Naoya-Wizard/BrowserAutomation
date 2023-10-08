# ログイン後のブラウザのセッションを保存して後で再利用する。
# chromeは動かし続けるとメモリエラーでクラッシュするので、こまめにchromeを再起動したいので作った。

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
指定されたWebDriverのインスタンスからブラウザのデータを取得します。
これには、クッキー、セッションストレージ、ローカルストレージのデータが含まれます。

Args:
- driver (WebDriver): データを取得するWebDriverのインスタンス。

Returns:
- tuple: クッキーのリスト、セッションストレージの辞書、ローカルストレージの辞書。
"""

def get_browser_data(driver):
    # クッキーを取得
    selenium_cookies = driver.get_cookies()
    # セッションストレージとローカルストレージの情報を取得
    session_storage = driver.execute_script("let data = {}; for (let i = 0; i < sessionStorage.length; i++) { data[sessionStorage.key(i)] = sessionStorage.getItem(sessionStorage.key(i)); } return data;")
    local_storage = driver.execute_script("let data = {}; for (let i = 0; i < localStorage.length; i++) { data[localStorage.key(i)] = localStorage.getItem(localStorage.key(i)); } return data;")
    return selenium_cookies, session_storage, local_storage



"""
指定されたWebDriverのインスタンスにブラウザのデータを設定します。
これには、クッキー、セッションストレージ、ローカルストレージのデータが含まれます。

Args:
- driver (WebDriver): データを設定するWebDriverのインスタンス。
- selenium_cookies (list): クッキーのリスト。
- session_storage (dict): セッションストレージのデータ。
- local_storage (dict): ローカルストレージのデータ。
"""

def set_browser_data(driver, selenium_cookies, session_storage, local_storage):

    # クッキーをセット
    for cookie in selenium_cookies:
        driver.add_cookie(cookie)
    # セッションストレージとローカルストレージの情報をセット
    for key, value in session_storage.items():
        driver.execute_script(f"sessionStorage.setItem('{key}', '{value}');")
    for key, value in local_storage.items():
        driver.execute_script(f"localStorage.setItem('{key}', '{value}');")



# 使用例

# WebDriverのインスタンスを起動します。
driver = webdriver.Chrome(ChromeDriverManager().install())

# 例として、ログインページにアクセスします。
driver.get("https://www.example.com/login")

# ログイン処理 (実際のセレクタや値は適宜変更してください)
username_elem = driver.find_element_by_id("username")
username_elem.send_keys("your_username")
password_elem = driver.find_element_by_id("password")
password_elem.send_keys("your_password")
login_btn = driver.find_element_by_id("login_button")
login_btn.click()

# 少し待ち、ログインが完了するのを確認します。
time.sleep(5)

# ログイン後のブラウザのデータを取得します。
cookies, session_storage_data, local_storage_data = get_browser_data(driver)

# 現在のブラウザを終了します。
driver.quit()

# 新しいWebDriverのインスタンスを起動します。
driver = webdriver.Chrome()

# 同じページ（または異なるページ）にアクセスします。
driver.get("https://www.example.com/")

# 先ほど取得したブラウザのデータを新しいブラウザセッションに設定します。
set_browser_data(driver, cookies, session_storage_data, local_storage_data)

# ここからログイン状態を維持したまま操作を続けることができます。

# 最後に、ブラウザを終了します。
driver.quit()
