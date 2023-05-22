class ErrorTemplate(Exception):
    message = ""
    infotemp = "\nDetailed information: %s"
    def __init__(self, info:str = None):
        if info != None:
            self.message = self.message + self.infotemp%info
    def __str__(self) -> str:
        return(self.message)
