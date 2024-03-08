from setuptools import setup
# //////////////////////////////////////
APP=["graphique.py"]
OPTIONS ={
    'argv_emulation': True,
    'excludes': ['rubicon'],
    'iconfile': 'Hellbotlogo.png'
}
setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"], install_requires=['customtkinter', 'selenium', 'pygame']
)
