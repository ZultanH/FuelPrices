commandList = {}

class CmdNotFound(Exception):
    pass

class Command:
    def __init__(self, cmdName, cmdFunc):
        self.cmdName = cmdName
        self.cmdFunc = cmdFunc
        self.save()
    
    def save(self):
        cmdName = self.cmdName
        cmdFunc = self.cmdFunc

        commandList[cmdName] = cmdFunc
    
    @staticmethod
    def doCmd(cmdName, config):
        if not commandList[cmdName]:
            raise CmdNotFound()
        
        func = commandList[cmdName]
        func(config)