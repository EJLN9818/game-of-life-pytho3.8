import pip

def install_packages(packages):
    for package in packages:
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])