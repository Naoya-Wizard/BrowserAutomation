
import psutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#ChromeDriverが別のプロセスによりロックされて開かないことがあるから作った。

# 指定したプロセス名のすべてのプロセスを終了します。
def kill_process_by_name(process_name):
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        if process_name in proc.info["name"]:
            psutil.Process(proc.info["pid"]).terminate()

# ChromeのWebDriverのインスタンスを生成します。
# もしエラーが発生した場合、"chromedriver"プロセスを終了して再度試みます。
def create_chrome_driver():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver
    except Exception as e:
        kill_process_by_name("chromedriver")
        return webdriver.Chrome(ChromeDriverManager().install())


#使用例
driver = create_chrome_driver()
driver.get("https://www.google.com")
#driver.quit()
