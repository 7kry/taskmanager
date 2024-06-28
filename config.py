import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

translations = {
  'ja': {
    'Welcome': 'ようこそ',
    'Sign In': 'サインイン',
    'Register': '登録',
    'Home': 'ホーム',
    'My Page': 'マイページ',
    'Logout': 'ログアウト',
    'Language Preference': '言語設定',
    'Select Language': '言語を選択',
    'Update Language': '言語を更新',
    'User Information': 'ユーザー情報',
    'Username': 'ユーザー名',
    'Password': 'パスワード',
    'Search users': 'ユーザーを検索',
    'Go to My Page': 'マイページに行く',
    'Back to Home': 'ホームに戻る',
    'Welcome to your page': 'あなたのページへようこそ'
  },
  'en': {
    'Welcome': 'Welcome',
    'Sign In': 'Sign In',
    'Register': 'Register',
    'Home': 'Home',
    'My Page': 'My Page',
    'Logout': 'Logout',
    'Language Preference': 'Language Preference',
    'Select Language': 'Select Language',
    'Update Language': 'Update Language',
    'User Information': 'User Information',
    'Username': 'Username',
    'Password': 'Password',
    'Search users': 'Search users',
    'Go to My Page': 'Go to My Page',
    'Back to Home': 'Back to Home',
    'Welcome to your page': 'Welcome to your page'
  }
}

# vim:ft=2:ts=2:sts=2:sw=2:et
