trial = 0
while True:                
   try:
      X=int(input('X='))
      Y=int(input('Y='))
      result = X // Y
   except ZeroDivisionError:
      print("ZeroDivisionError!")
      trial +=1  
   except:
      print("Error!")
      trial +=1  
   else:
      print("result={}".format(result))
      trial = 0
      break;
   finally:
      if (trial == 0):
        print("Succeed.")
      else:
        print("This is your {}th trial, try again".format(trial))

print("after while")

