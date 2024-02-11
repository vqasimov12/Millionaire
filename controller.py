# import os
# import random
# import time
# def cash(bank,count):
    
#     if count==1:
#         bank=1000
#     elif count==2:    
#         bank=10000
#     elif count==3:    
#         bank=50000
#     elif count==4:    
#         bank=100000
#     elif count==5:    
#         bank=1000000
#     return bank    

# def choicequestion(questions):
#     question=random.choice(questions)
#     questions.remove(question)
#     return question

# def jockeruse(jocker):
#     while True:
#         if jocker=="y" or jocker=="n":
#             break
#         else:
#             print(f"You can not select \" {jocker}\" ")    
#             print("Do you want to use joker?")
#             jocker=input("Select \"y\" or \"n\" ")
#     return jocker        

# def attenders():
#     a=0
#     b=0
#     c=0
#     d=0
#     while (a+b+c+d)!=100:    
#         a=random.randint(1,10)*10  
#         b=random.randint(1,10)*10
#         c=random.randint(1,10)*10
#         d=random.randint(1,10)*10
#     return a,b,c,d

# def animation():
#     os.system("cls")
#     for i in range(3):
#         print("A. **********     100%")
#         print("B.                  0%")
#         print("C.                  0%")
#         print("D.                  0%")
#         time.sleep(0.2)  
#         os.system("cls")                             
#         print("A. ******          60%")
#         print("B. ***             30%")
#         print("C. *               10%")
#         print("D.                  0%")
#         time.sleep(0.2)                                                              
#         os.system("cls")                             
#         print("A. **              20%")
#         print("B. *****           50%")
#         print("C. **              20%")
#         print("D. *               10%")
#         time.sleep(0.2)                               
#         os.system("cls")
#         print("A.                  0%")
#         print("B. ****            40%")
#         print("C. *****           50%")
#         print("D. *               10%")                             
#         time.sleep(0.2)                               
#         os.system("cls")
#         print("A.                  0%")
#         print("B. **              20%")
#         print("C. ******          60%")
#         print("D. **              20%")
#         time.sleep(0.2)                               
#         os.system("cls")
#         print("A. *               10%")
#         print("B.                  0%")
#         print("C. ****            40%")
#         print("D. *****           50%")
#         time.sleep(0.2)                               
#         os.system("cls")

# def attender_answer(asnwers_attenders):
#     (x,y,z,v)=asnwers_attenders
  
#     if   x==0:                        
#         print(f"A.              {x}%")
#     elif x==10:
#         print(f"A.*             {x}%")
#     elif x==20:
#         print(f"A.**            {x}%")
#     elif x==30:
#         print(f"A.***           {x}%")
#     elif x==40:                      
#         print(f"A.****          {x}%")
#     elif x==50:
#         print(f"A.*****         {x}%")
#     elif x==60:                      
#         print(f"A.******        {x}%")
#     elif x==70:
#         print(f"A.*******       {x}%")
#     elif x==80:
#         print(f"A.********      {x}%")
#     elif x==90:
#         print(f"A.*********     {x}%")
#     else:
#         print(f"A.**********   {x}%")
    
#     if   y==0:
#         print(f"B.              {y}%")
#     elif y==10:
#         print(f"B.*             {y}%")
#     elif y==20:
#         print(f"B.**            {y}%")
#     elif y==30:
#         print(f"B.***           {y}%")
#     elif y==40:                       
#         print(f"B.****          {y}%")
#     elif y==50:
#         print(f"B.*****         {y}%")
#     elif y==60:                      
#         print(f"B.******        {y}%")
#     elif y==70:
#         print(f"B.*******       {y}%")
#     elif y==80:
#         print(f"B.********      {y}%")
#     elif y==90:
#         print(f"B.*********     {y}%")
#     else:
#         print(f"B.**********   {y}%")
    
#     if   z==0:
#         print(f"C.              {z}%")
#     elif z==10:
#         print(f"C.*             {z}%")
#     elif z==20:
#         print(f"C.**            {z}%")
#     elif z==30:
#         print(f"C.***           {z}%")
#     elif z==40:                       
#         print(f"C.****          {z}%")
#     elif z==50:
#         print(f"C.*****         {z}%")
#     elif z==60:                      
#         print(f"C.******        {z}%")
#     elif z==70:
#         print(f"C.*******       {z}%")
#     elif z==80:
#         print(f"C.********      {z}%")
#     elif z==90:
#         print(f"C.*********     {z}%")
#     else:
#         print(f"C.**********   {z}%")    
    
#     if   v==0:
#         print(f"D.              {v}%")
#     elif v==10:
#        print(f"D.*             {v}%")
#     elif v==20:
#        print(f"D.**            {v}%")
#     elif v==30:
#        print(f"D.***           {v}%")
#     elif v==40:                      
#        print(f"D.****          {v}%")
#     elif v==50:
#        print(f"D.*****         {v}%")
#     elif v==60:                      
#        print(f"D.******        {v}%")
#     elif v==70:
#        print(f"D.*******       {v}%")
#     elif v==80:
#        print(f"D.********      {v}%")
#     elif v==90:
#        print(f"D.**********    {v}%")
#     else:
#         print(f"D.**********   {v}%")

# def Millionaire():
#     for i in range(2):
#         os.system("cls")
#         print("\n")
#         print("                     |\        /|     (*)    |\      |\       (*)                                                (*)                                                 ")         
#         print("                     | \      / |            | \     | \               ______          __          ______                    ___                                     ")         
#         print("                     |  \    /  |      |     |  \    |  \      |      /      \     |  /  \        /      \|       |      |  /   \      |\                            ")         
#         print("                     |   \  /   |      |     |  /    |  /      |      |      |     | /   |        |      ||       |      | /           | \                           ")         
#         print("                     |    \/    |      |     | /     | /       |      |      |     |/    |        |      ||       |      |/            | /                           ")         
#         print("                     |          |      |     |/      |/        |      |      |     |     |        |      ||       |      |             |/                            ")         
#         print("                     |          |      |     |       |         |      |      |     |     | /      |      || /     |      |             |                             ")         
#         print("                     |          |      |     |__/    |__/      |      \______/     |     |/       \______/|/      |      |             |__/                          ")         
#         time.sleep(0.5)
#         os.system("cls")
#         print("\n")
#         print("                       |\        /|     (*)    |\      |\       (*)                                                (*)                                                 ")         
#         print("                       | \      / |            | \     | \               ______          __          ______                    ___                                     ")         
#         print("                       |  \    /  |      |     |  \    |  \      |      /      \     |  /  \        /      \|       |      |  /   \      |\                            ")         
#         print("                       |   \  /   |      |     |  /    |  /      |      |      |     | /   |        |      ||       |      | /           | \                           ")         
#         print("                       |    \/    |      |     | /     | /       |      |      |     |/    |        |      ||       |      |/            | /                           ")         
#         print("                       |          |      |     |/      |/        |      |      |     |     |        |      ||       |      |             |/                            ")         
#         print("                       |          |      |     |       |         |      |      |     |     | /      |      || /     |      |             |                             ")         
#         print("                       |          |      |     |__/    |__/      |      \______/     |     |/       \______/|/      |      |             |__/                          ")         
#         time.sleep(0.5)

