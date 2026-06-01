import base64
import re

img_path  = r'C:\Users\Danto\desktop\reconai-website\DOC Socket Mascot nobg.png'
html_path = r'C:\Users\Danto\desktop\reconai-website\index.html.html'

# 1. Encode new PNG as base64
with open(img_path, 'rb') as f:
    new_b64 = base64.b64encode(f.read()).decode('ascii')

new_src = 'data:image/png;base64,' + new_b64
print(f'New image encoded, length: {len(new_b64)} chars')

# 2. Read HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 3. Replace every src="data:image/jpeg;base64,..." with the new PNG src
pattern = r'data:image/jpeg;base64,[^"]+'
matches = re.findall(pattern, html)
count = len(matches)
print(f'Found {count} instance(s) of the old base64 Socket image')

html_new = re.sub(pattern, new_src, html)

# 4. Save
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_new)

print(f'Done. {count} instance(s) replaced and file saved.')
