class ConnectionError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Error in The Connection'
        super().__init__(*args)
   

class NoResults(Exception):
    def __init__(self, search_term):
        self.search_term = search_term
        self.message = 'No Results Found For %s'%(str(self.search_term))
        super().__init__(self.message)