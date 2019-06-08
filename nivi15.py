x1,x2=input().split()
if(x1.isdigit() and x2.isdigit()):
              x1,x2=int(x1),int(x2)
              if(x2==1):
                  print("1 2")
              else:
                 print("1 "+str(x1-x2))
