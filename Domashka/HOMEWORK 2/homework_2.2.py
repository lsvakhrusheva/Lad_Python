is_published = True
is_premium = False
subscription = True
text = "Тоша ездил в Казахстан и видел там горы, степи и пустыни"

if is_published and (subscription or is_premium) and len(text) > 0:
    print(text)
