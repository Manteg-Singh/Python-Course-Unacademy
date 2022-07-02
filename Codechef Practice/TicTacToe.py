board = {'T1' : '','T2':'','T3':'',
         'M1': '','M2':'','M3':'',
         'D1':'','D2':'','D3':'' }
Cross_or_O= {1:'X',2:'O'}
Turn=1
No_of_places=0
symbol=None
print("What symbol do u want to use : X or O ?")
while True:
    symbol=input()
    if symbol!='X' or symbol!='O':
        print("Please Enter Valid Input")
    else:
        break
if symbol='X':
    pc_symbol='O'
else:
    pc_symbol='X'

while No_of_places!=9:
    

