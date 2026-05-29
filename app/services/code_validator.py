import re

def clean_code(code: str):

    if not code:
        return ""

    # Remove markdown blocks
    code = re.sub(r"```html", "", code)
    code = re.sub(r"```css", "", code)
    code = re.sub(r"```javascript", "", code)
    code = re.sub(r"```js", "", code)
    code = re.sub(r"```", "", code)

    return code.strip()