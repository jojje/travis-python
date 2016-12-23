import os


def get_version(default='0.0.0'):
    file = os.path.join(os.path.dirname(__file__), 'VERSION')
    if os.path.exists(file):
        with open(file) as f:
            return f.read().strip()
    else:
        return default


VERSION = get_version()
