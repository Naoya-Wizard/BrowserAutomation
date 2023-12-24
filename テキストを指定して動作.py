import time
from selenium.webdriver.common.by import By


"""
指定されたテキストを完全に一致するエレメントに対して動作します。
エレメントが見つからない場合や他のエラーが発生した場合、指定したスクロール量（pixel）でページをスクロールします。
指定したタイムアウト時間内にエレメントを見つけることができなかった場合、例外をスローします。

注意: テキストが複数のエレメントに存在する場合、この関数は最初に見つかったエレメントのみに動作します。

Args:
- driver (WebDriver): 使用するWebDriverのインスタンス。
- text (str): クリックするエレメントの完全なテキスト。
- timeout (int, optional): エレメントを検索する最大時間。デフォルトは60秒。
- scroll_amount (int, optional): 例外が発生した際にページをスクロールする量。デフォルトは300pixel。

Raises:
- Exception: 指定したタイムアウト時間内にエレメントを見つけることができなかった場合。
"""

def click_element_with_exact_text(driver, text, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with text '{text}'.")
        try:
            # normalize-space()を使用して空白を無視
            element = driver.find_element(By.XPATH, f"//*[normalize-space(text()) = '{text}']")
            element.click()
            break
        except NoSuchElementException:
            # 要素が見つからない場合はスクロール
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        except ElementClickInterceptedException:
            # 要素がクリック可能になるまで少し待つ
            time.sleep(1)
        except:
            # その他の例外が発生した場合
            continue


def click_element_by_normalized_text(driver, text, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with text '{text}'.")
        try:
            # normalize-space()を使用して空白を無視
            element = driver.find_element(By.XPATH, f"//*[normalize-space(text()) = '{text}']")
            element.click()
            break
        except NoSuchElementException:
            # 要素が見つからない場合はスクロール
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        except ElementClickInterceptedException:
            # 要素がクリック可能になるまで少し待つ
            time.sleep(1)
        except:
            # その他の例外が発生した場合
            continue
