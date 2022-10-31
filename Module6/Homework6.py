import re
import webbrowser

def correct_link(link):
  pattern = re.search(r"[htps:/w*.]+[youtube]+[\.][\w]+[/]+[A-z0-9&=?-]+", link ,re.MULTILINE)
  if pattern is None:
      print("Некорректная ссылка !")
  else:
      print("Корректная ссылка: ", pattern.group(0))
      webbrowser.open(pattern.group(0), new=0, autoraise=True)




test = input("введите ссылку:")
correct_link(test)


# test_str = ["https://www.youtube.com/watch?v=zI48YAa-Jec",
# 	"https://youtu.be/zI48YAa-Jec",
# 	"https://youtu.be/zI48YAa-Jec?t=1",
# 	"https://www.youtube.ru/watch?v=zI48YAa-Jec&t=1",
#             "https://vk.com/feed?w=story-68218830_456239080%2Ffeed"]
# for item in test_str:
#     correct_link(item)