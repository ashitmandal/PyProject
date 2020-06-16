
class open_file():
    
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_info,exc_val,traceback):
        #pass        self.file.close()
        
    with open_file('new.txt','w') as fil:
        f.write("hello")
        

        
    with open_file('sample.txt','w') as f:
        f.write('hello,hor r u')
    
        print(f.closed)

print(help(open_file))




