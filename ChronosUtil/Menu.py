'''
ChronosUtil.Menu contains the menus to be used by the main class.

@author  Jose Efraim Aguilar Escamilla
@version v0.01
@since   2019-06-29
'''

class BaseMenu():
    
    def __init__(self, title: str, ):
        pass

    def setup(self, choiceList=("Option 1", "Option 2")):
        pass

    def run(self, choice=0):
        pass

    


class ChronosMainMenu(BaseMenu):
    def __init__(self):
