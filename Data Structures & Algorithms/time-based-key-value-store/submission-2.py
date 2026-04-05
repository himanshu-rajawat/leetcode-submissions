class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            index = len(self.store[key])-1
            while index>0 and self.store[key][index][1]>timestamp:
                index-=1
            return self.store[key][index][0] if self.store[key][index][1]<=timestamp else ""
        return ""
        
