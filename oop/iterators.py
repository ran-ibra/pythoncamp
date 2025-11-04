class customRange:
    startback=None
    endback=None
    stepback=None
    

    def __init__(self,start,end=None,step=None):
        if end == None:
            self.start =0
            self.end=start
        else:
            self.start=start
            self.end=end
            self.step=step
            self.current=start
        self.saverange(start,end,step)

    def saverange(self,s, e , st):
        self.startback=s
        self.endback=e
        self.stepback=st


    def __iter__(self):
        return self
    def __next__(self):
        if (self.current>=self.end and self.step>0)or \
        (self.current<=self.end and self.step<0):
            raise StopIteration
        
        elif self.step is None:
            result =self.current
            self.current+=1
            return result
        else:
            result =self.current
            self.current+=self.step
            return result
    def reset(self):
        self.current=self.start

        
      

    def restart(self):
        self.start=self.startback
        self.end=self.endback
        self.step=self.stepback   
        
arr= iter(customRange(10, 1,-2))
print(next(arr))
print(next(arr))
print(next(arr))
print(next(arr))

print(next(arr))
