import re

import log.logging
from loguru import logger



# ===============ПРОВЕРКА SQL НА ИНЪЕКЦИИ============================
def text_check(text):
    regex = re.compile(r'[\'\"]')
    if regex.search(text):
        logger.error("SQL injection detected")
        return True
    else:
        return False


