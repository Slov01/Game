rules = [1 < 2,
         2 < 3,
         3 < 4]
# if ALL true, returns TRUE, so breaks
# if ANY statements are not true, returns FALSE, and doesn't break

while True:
    if all(rules):
      print("Break")
      break
    print("Don't break")



