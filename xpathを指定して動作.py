def click_element_by_xpath(driver, xpath, timeout=60, scroll_amount=300):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            raise Exception(f"Timeout on waiting for element with XPath '{xpath}'.")
        try:
            # 指定されたXPathに基づいて要素を見つける
            element = driver.find_element(By.XPATH, xpath)
            element.click()
            break
        except Exception as e:
            # 要素が見つからない場合、ページをスクロールして再試行
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            continue
