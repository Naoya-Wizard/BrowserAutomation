from bs4 import BeautifulSoup
import requests

def get_nodes_by_class(search_url, class_names):
  # リクエストを送信
  response = requests.get(search_url)
  # HTML を解析
  soup = BeautifulSoup(response.content, "html.parser")
  # 要素を取得
  elements = soup.find_all(class_=class_names)
  # 結果を返却
  return elements

# 例
search_url = "https://www.google.com/"
class_names = "title"

elements = get_nodes_by_class(search_url, class_names)

for element in elements:
  print(element.text)
