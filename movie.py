from datetime import datetime
name = input("이름 입력 : ")

print("-*"*30)
print("\t\t%s'이의 영화관!"%(name)) #프로그램 제목 출력
print("-*"*30)

def theater():
    print("거리순으로 나열한 결과입니다.\n1. 롯데시네마 시화점\n2. CGV 정왕점\n3. 메가박스 배곧점")
    thea=int(input("영화관을 입력하시오:"))
    if(thea==1):
        M="롯데시네마 시화점"
    elif(thea==2):
        M="CGV 정왕점"
    elif(thea==3):
        M="메가박스 배곧점"
    else:
        print("다른 지점 영화를 찾으시겠습니까?")
    return M

def movie():
    print("-*"*30)
    print("현재 상영중인 영화입니다.\n1. 닥터스트레인지\n2. 마녀배달부키키\n3. 라라랜드\n4. 기생충")
    print("-*"*30)
    while(True):
        mov=int(input("영화를 입력하시오:"))
        if(mov==1):
            m="닥터스트레인지"
            break
        elif(mov==2):
            m="마녀배달부키키"
            break
        elif(mov==3):
            m="라라랜드"
            break
        elif(mov==4):
            m="기생충"
            break
        else:
            print("다시 입력하시오.")
            continue
    return m

def time():
    now=datetime.now()
    nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
    
    print("현재시각 : "+nowDatetime)
    list=[["1회","10:00","12:00"],["2회","12:30","2:30"],["3회","3:00","5:00"],["4회","5:45","7:45"],["5회","8:00","10:30"]]
    today10am=now.replace(hour=10,minute=0,second=0)
    today1230pm=now.replace(hour=12,minute=30,second=0)
   
    today3pm=now.replace(hour=15,minute=0,second=0)
   
    today545pm=now.replace(hour=17,minute=45,second=0)
    today8pm=now.replace(hour=20,minute=0,second=0)
    
    if(now<today10am):
        print(list[0],list[1],list[2],list[3],list[4])
        while(True):
            s=int(input("회차를 입력하세요:"))
            if(s==1):
                S="1회 10:00~12:00"
                break
            elif(s==2):
                S="2회 12:30~2:30"
                break
            elif(s==3):
                S="3회 3:00~5:00"
                break
            elif(s==4):
                S="4회 5:45~7:45"
                break
            elif(s==5):
                S="5회 8:00~10:30"
                break
            else:
                print("다시 입력하세요.")
                continue
        return S

    elif(now>today10am and now<today1230pm):
        print(list[1],list[2],list[3],list[4])
        while(True):
            s=int(input("회차를 입력하세요:"))
            
            if(s==2):
                S="2회 12:30~2:30"
                break
            elif(s==3):
                S="3회 3:00~5:00"
                break
            elif(s==4):
                S="4회 5:45~7:45"
                break
            elif(s==5):
                S="5회 8:00~10:30"
                break
            else:
                print("다시 입력하세요.")
                continue
        return S

    elif(now>today1230pm and now<today3pm):
        print(list[2],list[3],list[4])
        while(True):
            s=int(input("회차를 입력하세요:"))
            
            if(s==3):
                S="3회 3:00~5:00"
                break
            elif(s==4):
                S="4회 5:45~7:45"
                break
            elif(s==5):
                S="5회 8:00~10:30"
                break
            else:
                print("다시 입력하세요.")
                continue
        return S
    elif(now>today3pm and now<today545pm):
        print(list[3],list[4])
        while(True):
            s=int(input("회차를 입력하세요:"))
            
            if(s==4):
                S="4회 5:45~7:45"
                break
            elif(s==5):
                S="5회 8:00~10:30"
                break
            else:
                print("다시 입력하세요.")
                continue
        return S
    elif(now>today8pm):
        print("예매가능한 영화가 없습니다.")
        S=0
        return S

    

def seat():
    r=100
    c=100
    print("1.프리미엄 영화관 2.일반 영화관")
    x=int(input("영화관 종류를 입력하세요:"))
    list=[]
    if(x==1):

        a=[["1열","o","o","o","o","o"],["2열","o","o","o","o","o"],["3열","o","o","o","o","o"],["4열","o","o","o","o","o"],["5열","o","o","o","o","o"],["6열","o","o","o","o","o"],["7열","o","o","o","o","o"],["8열","o","o","o","o","o"]]
   
        for i in a:
            print(i)
        

        while(True):
            q=int(input("1.개인석\n2.단체석\n번호를 입력하세요:"))
            if(q==1):
                print("좌석을 입력하시오.")
                r=int(input("열을 입력하시오:"))
                c=int(input("좌석을 입력하시오:"))

                for i in range(0,6):
                    if(a[r-1][i]=="x"):
                        print("이미 예매된 좌석입니다. 다시 입력하시오.")
                        r=int(input("열을 입력하시오:"))
                        c=int(input("좌석을 입력하시오:"))
                    
                    
                    elif(a[r-1][i]=="o"):
                        print("%d열 %d이 예매되었습니다." %(r,c))
                        a[r-1][c]="x"
                        break

                x="%d열 %d" %(r,c)
                list.append(x)  

                for i in a:
                    print(i)
            

                
                t=input("더 구매하시겠습니까?(Y/N):")
                if(t=="N" or t=="n"):
                    break
                elif(t=="Y" or t=="y"):
                    continue
                else:
                    print("다시 입력하세요")
                    t=input("더 구매하시겠습니까?(Y/N):")
                    if(t=="N" or t=="n"):
                        break
                    elif(t=="Y" or t=="y"):
                        continue

            elif(q==2): 
                r=int(input("열을 입력하세요:"))
                
                for i in range(0,6): 

                    if(a[r-1][i]=="x"):
                        print("이미 예매된 좌석입니다. 다시 입력하시오.")
                        r=int(input("열을 입력하시오:"))
                        
                        
                        
                
                    elif(a[r-1][i]=="o"):
                        
                        a[r-1][i]="x"
                        
                
                    
                    x="%d열 %d" %(r,i+1)
                    list.append(x)
                print("%d열 전체가 예매되었습니다." %(r))
                    
                for i in a:
                    print(i)    

                t=input("더 구매하시겠습니까?(Y/N):")
                if(t=="N" or t=="n"):
                    break
                elif(t=="Y" or t=="y"):
                    continue
                else:
                    print("다시 입력하세요")
                    t=input("더 구매하시겠습니까?(Y/N):")
                    if(t=="N" or t=="n"):
                        break
                    elif(t=="Y" or t=="y"):
                        continue
    

    elif(x==2):
        a=[["1열","o","o","o","o","o"],["2열","o","o","o","o","o"],["3열","o","o","o","o","o"],["4열","o","o","o","o","o"]]
        
        for i in a:
            print(i)
        

        while(True):
            q=int(input("1.개인석\n2.단체석\n번호를 입력하세요:"))
            if(q==1):
                print("좌석을 입력하시오.")
                r=int(input("열을 입력하시오:"))
                c=int(input("좌석을 입력하시오:"))

                for i in range(0,6):
                    if(a[r-1][i]=="x"):
                        print("이미 예매된 좌석입니다. 다시 입력하시오.")
                        r=int(input("열을 입력하시오:"))
                        c=int(input("좌석을 입력하시오:"))
                        
                        
                    elif(a[r-1][i]=="o"):
                        print("%d열 %d이 예매되었습니다." %(r,c))
                        a[r-1][c]="x"
                        break
                x="%d열 %d" %(r,c)
                list.append(x)
                    
                for i in a:
                    print(i)    
                    
                
                t=input("더 구매하시겠습니까?(Y/N):")
                if(t=="N" or t=="n"):
                    break
                elif(t=="Y" or t=="y"):
                    continue
                else:
                    print("다시 입력하세요")
                    t=input("더 구매하시겠습니까?(Y/N):")
                    if(t=="N" or t=="n"):
                        break
                    elif(t=="Y" or t=="y"):
                        continue
            if(q==2):
                r=int(input("열을 입력하세요:"))
                
                for i in range(0,6): 

                    if(a[r-1][i]=="x"):
                        print("이미 예매된 좌석입니다. 다시 입력하시오.")
                        r=int(input("열을 입력하시오:"))
                        
                        
                        
                
                    elif(a[r-1][i]=="o"):
                        
                        a[r-1][i]="x"
                        
                
                    
                    x="%d열 %d" %(r,i+1)
                    list.append(x)
                print("%d열 전체가 예매되었습니다." %(r))

                    
                for i in a:
                    print(i)    

                t=input("더 구매하시겠습니까?(Y/N):")
                if(t=="N" or t=="n"):
                    break
                elif(t=="Y" or t=="y"):
                    continue
                else:
                    print("다시 입력하세요")
                    t=input("더 구매하시겠습니까?(Y/N):")
                    if(t=="N" or t=="n"):
                        break
                    elif(t=="Y" or t=="y"):
                        continue


    money=0
    n=len(list)
    print("%d개의 좌석이 예약되었습니다" %(n))
    
    adult=int(input("성인 명수:"))
    teen=int(input("청소년 명수:"))
    chil=int(input("어린이,노약자 명수:"))
       
    while(adult+teen+chil != n):
        print("다시 입력하세요.")
        adult=int(input("성인 명수:"))
        teen=int(input("청소년 명수:"))
        chil=int(input("어린이,노약자 명수:"))
    
    money=adult*9000
            
        
    money+=teen*7000
            
        
    money+=chil*5000
      
    

    return list,money

def popcorn():
    mon=0
    while(True):
        
        x=input("팝콘을 구매하시겠습니까?(Y/N):")
        if(x=='Y' or x=='y'):
            print("<팝콘 메뉴>\n1.오리지널 팝콘 | 5000원\n2.카라멜 팝콘   | 5500원\n3.어니언맛 팝콘 | 5700원")
            p=int(input("번호를 선택하시오:"))
            if(p==1):
                print("오리지널 팝콘을 구매하였습니다.")
                mon+=5000
            elif(p==2):
                print("카라멜 팝콘을 구매하였습니다.")
                mon+=5500
            elif(p==3):
                print("어니언맛 팝콘을 구매하였습니다.")
                mon+=5700
            else:
                print("다시 입력하세요")
                continue

        elif(x=='N' or x=='n'):
            break
        else:
            print("다시입력하세요")
            continue
   
    return mon
            
        

   


print("1. 영화관으로 검색\n2. 영화로 검색")
x=int(input("숫자를 입력하시오:"))

if(x==1):
    M=theater()
        
    m=movie()
   
    
    S=time()
    
    list,money=seat()
    mon=popcorn()

elif(x==2):
    m=movie()

    M=theater()
    
   
    S=time()
    
    list,money=seat()
    mon=popcorn()


print("="*30)
print("<%s>"%(m)) #영화표 출력
print("%s" %(M))

now=datetime.now()
nowDate=now.strftime('%Y-%m-%d')
print(nowDate)

print("%s" %(S))
print(list)


print("="*30)

print("총 %d원 입니다." %(money+mon))



        
