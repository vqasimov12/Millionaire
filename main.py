# from model import *  
# from controller import * 
# import random
# import os
# bank=0
# count=0
# jocker50_50=1
# jocker_attenders=1
# def main(questions,bank):
#     os.system("cls")
#     global count
#     global jocker50_50
#     global jocker_attenders
#     print("Jockers:    50/50:       Attenders help:")
#     print(f"Count:        {jocker50_50}                 {jocker_attenders}")
#     print()
#     count+=1
#     print(f"\nQuestion {count}:")
#     question=choicequestion(questions)
#     print(question["i"])
#     print()
#     variant=random.randint(1,4)
#     false_variants=[0,1,2]
#     variants=["a","b","c","d"]
#     if variant==1:
#         b=random.choice(false_variants)
#         false_variants.remove(b)
#         c=random.choice(false_variants)
#         false_variants.remove(c)
#         d=random.choice(false_variants)
#         false_variants.remove(d)
#         print(f"\nA.{question[True]}")
#         print(f"\nB.{question[False][b]}")
#         print(f"\nC.{question[False][c]}")
#         print(f"\nD.{question[False][d]}")
#         remind=[b,c,d]
#         if jocker_attenders==jocker50_50==1:
#             jocker=input("Do you want to use your jockers[y|n]? ")
#             if jockeruse(jocker)=="y":
#                 print("1 -> For 50\\50")
#                 print("2 -> For Auditorium's help")
#                 help=input("Your choice: ")
#                 while True :
#                     if help=="1":                   
#                         os.system("cls")
#                         jocker50_50=0
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"A.{question[True]}\n")
#                         reminder=random.choice(remind)
#                         if reminder==b:
#                             print(f"B.{question[False][b]}\n")
#                             variants=["a","b"]
#                         elif reminder==c:
#                             print(f"C.{question[False][c]}\n")
#                             variants=["a","c"]
#                         elif reminder==d:
#                             print(f"D.{question[False][d]}\n")  
#                             variants=["a","d"]
#                         jocker=input("You can also use Auditorium's help. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                                 jocker_attenders=0
#                                 asnwers_attenders=(attenders())   
#                                 animation()
#                                 attender_answer(asnwers_attenders)
#                                 print(f"\nQuestion {count}:")
#                                 print()    
#                                 print(question["i"])
#                                 print()
#                                 print(f"\nA.{question[True]}")
#                                 print(f"\nB.{question[False][b]}")
#                                 print(f"\nC.{question[False][c]}")
#                                 print(f"\nD.{question[False][d]}")    
#                         break      
#                     elif help=="2":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[True]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[False][d]}")  
#                         jocker=input("You can also use 50\\50. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             os.system("cls")
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()                    
#                             jocker50_50=0
#                             print(f"A.{question[True]}\n")
#                             reminder=random.choice(remind)
#                             if reminder==b:
#                                 print(f"B.{question[False][b]}\n")
#                                 variants=["a","b"]
#                             elif reminder==c:
#                                 print(f"C.{question[False][c]}\n")
#                                 variants=["a","c"]
#                             elif reminder==d:
#                                 print(f"D.{question[False][d]}\n")
#                                 variants=["a","d"]
#                         break     
                            
#                     else:
#                         print(f"You can not select {help}")
#                         print("1 -> For 50\\50")
#                         print("2 -> For Auditorium's help")
#                         help=input("Select \"1\" or \"2\": ")
#                         continue     
      
#         elif jocker50_50==1 and jocker_attenders==0:
#                 jocker=input("You can use 50\\50. Do you want[y|n]? ")     
#                 if  jockeruse(jocker)=="y":
#                     os.system("cls")
#                     print(f"\nQuestion {count}:")
#                     print()    
#                     print(question["i"])
#                     print()                    
#                     jocker50_50=0
#                     print(f"A.{question[True]}\n")
#                     reminder=random.choice(remind)
#                     if reminder==b:
#                         print(f"B.{question[False][b]}\n")
#                         variants=["a","b"]
#                     elif reminder==c:
#                         print(f"C.{question[False][c]}\n")
#                         variants=["a","c"]
#                     elif reminder==d:
#                         variants=["a","d"]
#                         print(f"D.{question[False][d]}\n")
#         elif jocker50_50==0 and jocker_attenders==1:
#                 jocker=input("You can use Auditorium's help. Do you want[y|n]? ")     
#                 if  jockeruse(jocker)=="y":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[True]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[False][d]}")
#         variants.sort()
#         answer=input("\nYour answer:")
#         while True:
#             if answer in variants:
#                 if answer=="a":
#                     os.system("cls")
#                     print("Correct!!!")
#                     bank=cash(bank,count)
#                     print(f"Your balance: {bank}$")
#                     break
#                 else:
#                     print("Wrong answer!!")
#                     print(f"You lose the game. Total amount you earn= {bank}$") 
#                     return
#             else:
#                 print(f"We don't have \"{answer}\" between our variants!") 
#                 print(f"you can select only {variants}")   
#                 answer=input("\nYour answer:")
#     elif variant==2:
#         a=random.choice(false_variants)
#         false_variants.remove(a)
#         c=random.choice(false_variants)
#         false_variants.remove(c)
#         d=random.choice(false_variants)
#         false_variants.remove(d)   
#         print(f"A.{question[False][a]}\n")
#         print(f"B.{question[True]}\n")
#         print(f"C.{question[False][c]}\n")
#         print(f"D.{question[False][d]}\n")
#         print()
#         remind=[a,c,d]
#         if jocker_attenders==jocker50_50==1:
#             jocker=input("Do you want to use your jockers[y|n]? ")
#             if jockeruse(jocker)=="y":
#                 print("1 -> For 50\\50")
#                 print("2 -> For Auditorium's help")
#                 help=input("Your choice: ")
#                 while True :
#                     if help=="1":
#                         os.system("cls")
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         jocker50_50=0
#                         reminder=random.choice(remind)
#                         if reminder==a:
#                             print(f"A.{question[False][a]}\n")
#                             print(f"B.{question[True]}\n")
#                             variants=["b","a"]    
#                         elif reminder==c:
#                             print(f"B.{question[True]}\n")
#                             print(f"C.{question[False][c]}\n")
#                             variants=["b","c"]                            
#                         elif reminder==d:
#                             print(f"B.{question[True]}\n")
#                             print(f"D.{question[False][d]}\n") 
#                             variants=["b","d"]    
#                         jocker=input("You can also use Auditorium's help. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             jocker_attenders=0
#                             asnwers_attenders=(attenders())   
#                             animation()
#                             attender_answer(asnwers_attenders)
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()
#                             print(f"\nA.{question[False][a]}")
#                             print(f"\nB.{question[True]}")
#                             print(f"\nC.{question[False][c]}")
#                             print(f"\nD.{question[False][d]}")
#                         break     
#                     elif help=="2":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[True]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[False][d]}")
#                         jocker=input("You can also use 50\\50. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             os.system("cls")
#                             jocker50_50=0
#                             reminder=random.choice(remind)
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()
#                             if reminder==a:
#                                 print(f"A.{question[False][a]}\n")
#                                 print(f"B.{question[True]}\n")
#                                 variants=["b","a"]    
#                             elif reminder==c:
#                                 print(f"B.{question[True]}\n")
#                                 print(f"C.{question[False][c]}\n")
#                                 variants=["b","c"]    
#                             elif reminder==d:
#                                 print(f"B.{question[True]}\n")
#                                 print(f"D.{question[False][d]}\n")
#                                 variants=["b","d"]    
#                         break    
                            
#                     else:
#                         print(f"You can not select {help}")
#                         help=input("Select \"1\" or \"2\": ")
#                         continue 
                             
#         elif jocker50_50==1 and jocker_attenders==0:
#             jocker=input("You can use 50\\50. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                 os.system("cls")
#                 jocker50_50=0
#                 reminder=random.choice(remind)
#                 print(f"\nQuestion {count}:")
#                 print()    
#                 print(question["i"])
#                 print()
#                 if reminder==a:
#                     print(f"A.{question[False][a]}\n")
#                     print(f"B.{question[True]}\n")
#                     variants=["b","a"]    
#                 elif reminder==c:
#                     print(f"B.{question[True]}\n")
#                     print(f"C.{question[False][c]}\n")
#                     variants=["b","c"]    
#                 elif reminder==d:
#                     print(f"B.{question[True]}\n")
#                     print(f"D.{question[False][d]}\n")
#                     variants=["b","d"]    
#         elif jocker50_50==0 and jocker_attenders==1:
#             jocker=input("You can use Auditorium's help. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[True]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[False][d]}")
#         variants.sort()
#         answer=input("\nYour answer:")
#         while True:
#             if answer in variants:
#                 if answer=="b":
#                     os.system("cls")
#                     print("Correct!!!")
#                     bank=cash(bank,count)
#                     print(f"Your balance: {bank}$")
#                     break
#                 else:
#                     print("Wrong answer!!")
#                     print(f"You lose the game. Total amount you earn= {bank}$") 
#                     return
#             else:
#                 print(f"We don't have \"{answer}\" between our variants!")    
#                 print(f"you can select only {variants}")   
#                 answer=input("\nYour answer:")
#     elif variant==3:
#         a=random.choice(false_variants)
#         false_variants.remove(a)
#         b=random.choice(false_variants)
#         false_variants.remove(b)
#         d=random.choice(false_variants)
#         false_variants.remove(d)   
#         print(f"A.{question[False][a]}\n")
#         print(f"B.{question[False][b]}\n")
#         print(f"C.{question[True]}\n")
#         print(f"D.{question[False][d]}\n")
#         remind=[a,b,d]
#         print()
#         if jocker_attenders==jocker50_50==1:
#             jocker=input("Do you want to use your jockers[y|n]? ")
#             if jockeruse(jocker)=="y":
#                 print("1 -> For 50\\50")
#                 print("2 -> For Auditoria's help")
#                 help=input("Your choice: ")
#                 while True :
#                     if help=="1":
#                         os.system("cls")
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         jocker50_50=0
#                         reminder=random.choice(remind)
#                         if reminder==a:
#                             print(f"A.{question[False][a]}\n")
#                             print(f"C.{question[True]}\n")
#                             variants=["c","a"]    
#                         elif reminder==b:
#                             print(f"B.{question[False][b]}\n")
#                             print(f"C.{question[True]}\n")
#                             variants=["c","b"]    
#                         elif reminder==d:
#                             print(f"C.{question[True]}\n")
#                             print(f"D.{question[False][d]}\n")  
#                             variants=["c","d"]    
#                         jocker=input("You can also use Auditorium's help. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                                     jocker_attenders=0
#                                     asnwers_attenders=(attenders())   
#                                     animation()
#                                     attender_answer(asnwers_attenders)
#                                     print(f"\nQuestion {count}:")
#                                     print()    
#                                     print(question["i"])
#                                     print()
#                                     print(f"\nA.{question[False][a]}")
#                                     print(f"\nB.{question[False][b]}")
#                                     print(f"\nC.{question[True]}")
#                                     print(f"\nD.{question[False][d]}")
#                         break       
#                     elif help=="2":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[True]}")
#                         print(f"\nD.{question[False][d]}")
#                         jocker=input("You can also use 50\\50. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             os.system("cls")
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()
#                             jocker50_50=0  
#                             reminder=random.choice(remind)
#                             if reminder==a:
#                                 print(f"A.{question[False][a]}\n")
#                                 print(f"C.{question[True]}\n")
#                                 variants=["c","a"]    
#                             elif reminder==b:
#                                 print(f"B.{question[False][b]}\n")
#                                 print(f"C.{question[True]}\n")
#                                 variants=["c","b"]    
#                             elif reminder==d:
#                                 print(f"C.{question[True]}\n")
#                                 print(f"D.{question[False][d]}\n")
#                                 variants=["c","d"]    
#                         break     
                            
#                     else:
#                         print(f"You can not select {help}")
#                         help=input("Select \"1\" or \"2\": ")
#                         continue  
#         elif jocker50_50==1 and jocker_attenders==0:
#             jocker=input("You can use 50\\50. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                 os.system("cls")
#                 print(f"\nQuestion {count}:")
#                 print()    
#                 print(question["i"])
#                 print()
#                 jocker50_50=0  
#                 reminder=random.choice(remind)
#                 if reminder==a:
#                     print(f"A.{question[False][a]}\n")
#                     print(f"C.{question[True]}\n")
#                     variants=["c","a"]    
#                 elif reminder==b:
#                     print(f"B.{question[False][b]}\n")
#                     print(f"C.{question[True]}\n")
#                     variants=["c","b"]    
#                 elif reminder==d:
#                     print(f"C.{question[True]}\n")
#                     print(f"D.{question[False][d]}\n") 
#                     variants=["c","d"]    
#         elif jocker50_50==0 and jocker_attenders==1:
#             jocker=input("You can use Auditorium's help. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[True]}")
#                         print(f"\nD.{question[False][d]}")
#         variants.sort()
#         answer=input("\nYour answer:")
#         while True:
#             if answer in variants:
#                 if answer=="c":
#                     os.system("cls")
#                     print("Correct!!!")
#                     bank=cash(bank,count)
#                     print(f"Your balance: {bank}$")
#                     break
#                 else:
#                     print("Wrong answer!!")
#                     print(f"You lose the game. Total amount you earn= {bank}$") 
#                     return
#             else:
#                 print(f"We don't have \"{answer}\" between our variants!")    
#                 print(f"you can select only {variants}")   
#                 answer=input("\nYour answer:")   
#     else:
#         a=random.choice(false_variants)
#         false_variants.remove(a)
#         b=random.choice(false_variants)
#         false_variants.remove(b)
#         c=random.choice(false_variants)
#         false_variants.remove(c)   
#         print(f"A.{question[False][a]}\n")
#         print(f"B.{question[False][b]}\n")
#         print(f"C.{question[False][c]}\n")
#         print(f"D.{question[True]}\n")
#         remind=[a,b,c]
#         print()
#         if jocker_attenders==jocker50_50==1:
#             jocker=input("Do you want to use your jockers[y|n]? ")
#             if jockeruse(jocker)=="y":
#                 print("1 -> For 50\\50")
#                 print("2 -> For Auditoria's help")
#                 help=input("Your choice: ")
#                 while True :
#                     if help=="1":
#                         os.system("cls")
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         jocker50_50=0
#                         reminder=random.choice(remind)
#                         if reminder==a:
#                             print(f"A.{question[False][a]}\n")
#                             print(f"D.{question[True]}\n")
#                             variants=["d","a"]    
#                         elif reminder==b:
#                             print(f"B.{question[False][b]}\n")
#                             print(f"D.{question[True]}\n")
#                             variants=["d","b"]    
#                         elif reminder==c:
#                             print(f"C.{question[False][c]}\n")
#                             print(f"D.{question[True]}\n")
#                             variants=["d","c"]    
#                         jocker=input("You can use Auditorium's help. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             jocker_attenders=0
#                             asnwers_attenders=(attenders())   
#                             animation()
#                             attender_answer(asnwers_attenders)
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()
#                             print(f"\nA.{question[False][a]}")
#                             print(f"\nB.{question[False][b]}")
#                             print(f"\nC.{question[False][c]}")
#                             print(f"\nD.{question[True]}")

#                         break
#                     elif help=="2":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[True]}")
#                         jocker=input("You can use 50\\50. Do you want[y|n]? ")     
#                         if  jockeruse(jocker)=="y":
#                             os.system("cls")
#                             print(f"\nQuestion {count}:")
#                             print()    
#                             print(question["i"])
#                             print()
#                             jocker50_50=0
#                             reminder=random.choice(remind)
#                             if reminder==a:
#                                 print(f"A.{question[False][a]}\n")
#                                 print(f"D.{question[True]}\n")
#                                 variants=["d","a"]    
#                             elif reminder==b:
#                                 print(f"B.{question[False][b]}\n")
#                                 print(f"D.{question[True]}\n")
#                                 variants=["d","b"]    
#                             elif reminder==c:
#                                 print(f"C.{question[False][c]}\n")
#                                 print(f"D.{question[True]}\n")
#                                 variants=["d","c"]    
#                         break     
                            
#                     else:
#                         print(f"You can not select {help}")
#                         help=input("Select \"1\" or \"2\": ")
#                         continue             
#         elif jocker50_50==1 and jocker_attenders==0:
#             jocker=input("You can use 50\\50. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                 os.system("cls")
#                 print(f"\nQuestion {count}:")
#                 print()    
#                 print(question["i"])
#                 print()
#                 jocker50_50=0
#                 reminder=random.choice(remind)
#                 if reminder==a:
#                     print(f"A.{question[False][a]}\n")
#                     print(f"D.{question[True]}\n")
#                     variants=["d","a"]    
#                 elif reminder==b:
#                     print(f"B.{question[False][b]}\n")
#                     print(f"D.{question[True]}\n")
#                     variants=["d","b"]    
#                 elif reminder==c:
#                     print(f"C.{question[False][c]}\n")
#                     print(f"D.{question[True]}\n")
#                     variants=["d","c"]    
#         elif jocker50_50==0 and jocker_attenders==1:
#             jocker=input("You can use Auditorium's help. Do you want[y|n]? ")     
#             if  jockeruse(jocker)=="y":
#                         jocker_attenders=0
#                         asnwers_attenders=(attenders())   
#                         animation()
#                         attender_answer(asnwers_attenders)
#                         print(f"\nQuestion {count}:")
#                         print()    
#                         print(question["i"])
#                         print()
#                         print(f"\nA.{question[False][a]}")
#                         print(f"\nB.{question[False][b]}")
#                         print(f"\nC.{question[False][c]}")
#                         print(f"\nD.{question[True]}")
#         variants.sort()
#         answer=input("\nYour answer:")
#         while True:
#             if answer in variants:
#                 if answer=="d":
#                     os.system("cls")
#                     print("Correct!!!")
#                     bank=cash(bank,count)
#                     print(f"Your balance: {bank}$")
#                     break
#                 else:
#                     print("Wrong answer!!")
#                     print(f"You lose the game. Total amount you earn= {bank}$") 
#                     return
#             else:
#                 print(f"We don't have \"{answer}\" between our variants!")    
#                 print(f"you can select only {variants}")   
#                 answer=input("\nYour answer:")
#     if len(questions)!=0:
#         input("Press \"Enter\" to continue... ")
#         os.system("cls")
#         main(questions,bank)
#     else:
#         os.system("cls")
#         print("Congritulations!!! You are millioner!!!!")
#         print(f"\nYou earn totally {bank}$\n")
# Millionaire()
# input("Are You ready?!!")
# os.system("cls")
# print("Game is Loading...")
# time.sleep(0.7)
# main(questions,bank)    