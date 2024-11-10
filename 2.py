
 
gyumolcsok = []

  
gyumolcs = None
while gyumolcs != 'vége':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs == 'vége':
        break
    elif gyumolcsok.count(gyumolcs)<1 :
       gyumolcsok.append(gyumolcs)
    else:
        print("Már van ilyen gyümölcs")
       
       
   
      
  
print(gyumolcsok)  
  