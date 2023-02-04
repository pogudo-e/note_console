class User:
    id : int = None
    name : str = None
    body : str = None
    time = None
    
    def us(self, id: int, name: str, body: str, time):
        self.id = id
        self.name = name
        self.body = body
        self.time = time