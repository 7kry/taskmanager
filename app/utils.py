from flask_login import current_user
from config import translations

def get_translation(key):
    language = current_user.language if current_user.is_authenticated else 'ja'
    return translations.get(language, {}).get(key, key)

# vim:ft=2:ts=2:sts=2:sw=2:et
