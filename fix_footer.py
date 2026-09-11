import re

src = "/home/ubuntu/app/hugo-blog/themes/PaperMod/layouts/_partials/footer.html"
dst = "/home/ubuntu/app/hugo-blog/layouts/_partials/footer.html"

with open(src, 'r') as f:
    content = f.read()



# Remove the hardcoded Powered by Hugo & PaperMod block and its comment
pattern = r'\{\{/\*.*?The "Powered by Hugo" text.*?\}\}\s*<span>\s*Powered by.*?</span>'
new_content = re.sub(pattern, '', content, flags=re.DOTALL)

with open(dst, 'w') as f:
    f.write(new_content)

print("Custom clean footer.html created successfully!")
