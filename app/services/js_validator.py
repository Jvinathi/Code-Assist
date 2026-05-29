import esprima


def validate_javascript(code):

    try:
        esprima.parseScript(code)
        return True, None

    except Exception as e:
        return False, str(e)