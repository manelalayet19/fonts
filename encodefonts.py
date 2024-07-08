import base64

# Convert Gotham-Medium.ttf to Base64
with open("static/GothamSSm-Medium.ttf", "rb") as font_file:
    gotham_medium_base64 = base64.b64encode(font_file.read()).decode('utf-8')
with open("static/GothamSSm-Medium.ttf.base64", "w") as output_file:
    output_file.write(gotham_medium_base64)

# Convert Gotham-Bold.ttf to Base64
with open("static/GothamBold.ttf", "rb") as font_file:
    gotham_bold_base64 = base64.b64encode(font_file.read()).decode('utf-8')
with open("static/GothamBold.ttf.base64", "w") as output_file:
    output_file.write(gotham_bold_base64)

# Convert Gotham-Book.ttf to Base64
with open("static/GothamSSm-Book.ttf", "rb") as font_file:
    gotham_book_base64 = base64.b64encode(font_file.read()).decode('utf-8')
with open("static/GothamSSm-Book.ttf.base64", "w") as output_file:
    output_file.write(gotham_book_base64)
