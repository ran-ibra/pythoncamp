class customRange:
    startback=None
    endback=None
    stepback=None
    

    def __init__(self,start,end,step=None):
        self.start=start
        self.end=end
        self.step=step
        self.saverange(start,end,step)

    def saverange(self,s, e , st):
        self.startback=s
        self.endback=e
        self.stepback=st


    def __iter__(self):
        return self
    def __next__(self):
        if self.start>0 and (self.start <self.end-1)and  self.step is not None:
            result =self.start
            self.start+=self.step
            return result
        elif self.step is None:
            result =self.start
            self.start+=1
            return result
        elif self.step <0 and self.end >self.start:
            result =self.end
            self.end+=1
            return result
        else:
            raise StopIteration
    def restart(self):
        self.start=self.startback
        self.end=self.endback
        self.step=self.stepback   
        
arr= iter(customRange(10, 13,-1))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))

print(next(arr))
