from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ブラウザのインスタンスを起動する
# ChromeDriverManagerを使用して、最新のChromeDriverを自動的にダウンロード・インストールし、それを使用してChromeのWebDriverインスタンスを起動します。
driver = webdriver.Chrome(ChromeDriverManager().install())

# ページのナビゲーション:
# ページへの移動
driver.get("https://www.example.com")
# ページのリロード
driver.refresh()
# 前後のページへの移動
driver.back()
driver.forward()

# エレメントの取得と操作:
# エレメントの取得
element_by_id = driver.find_element_by_id('sampleId')
element_by_class = driver.find_element_by_class_name('sampleClass')
element_by_xpath = driver.find_element_by_xpath('//div[@class="sampleXpath"]')
# テキストの取得
text = element_by_id.text
# 属性の取得
attribute_value = element_by_id.get_attribute('attrName')

# フォームの操作:
# テキストボックスへの入力
element_by_id.send_keys("Hello, Selenium!")
# フォームの送信
element_by_id.submit()

# アラートやポップアップの操作:
# アラートの受け入れ
driver.switch_to.alert.accept()
# アラートの拒否
driver.switch_to.alert.dismiss()

# ウィンドウやタブの操作:
# 新しいウィンドウ/タブへの切り替え
driver.switch_to.window(driver.window_handles[-1])
# ウィンドウサイズの変更
driver.set_window_size(1024, 768)
# ウィンドウの移動
driver.set_window_position(0, 0)
# スクリーンショットの取得
driver.save_screenshot('screenshot.png')

# クッキーの操作:
# クッキーの追加
driver.add_cookie({"name": "sampleName", "value": "sampleValue"})
# クッキーの取得
cookies = driver.get_cookies()
# クッキーの削除
driver.delete_cookie("sampleName")

# JavaScriptの実行:
driver.execute_script("alert('Hello, World!');")

# 待機処理:
# 明示的な待機
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sampleId")))
# 暗黙的な待機
driver.implicitly_wait(10)

# ブラウザの終了:
# 現在のウィンドウのみ閉じる
driver.close()
# すべてのウィンドウを閉じてブラウザを終了
driver.quit()
