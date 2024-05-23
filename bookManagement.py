# FUNCTION ORDER
## display_user
## add_user
## user_register
## display_book
## add_book
## book_register
## rent_book
## rent_register
## return_book
## return_register
## display_rent

import pymssql
from tkinter import *
from tkinter import messagebox, Entry
from PIL import ImageTk, Image
from datetime import *

# MSSQL 데이터베이스에 접속
con = pymssql.connect(server='localhost', database='BookDB', user='SQLMaster', password='kang1010', charset='utf8')
cur = con.cursor()

# Tkinter를 이용한 GUI 프로그램 시작
root = Tk()
root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
root.minsize(width=700, height=800)
root.geometry("600x500")

# 배경 이미지 크기 조정 변수
same = True
n = 1.3

# 배경 이미지 불러오기
background_image = Image.open("C:\\Users\\kang\\OneDrive\\Desktop\\DB_Final\\lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

# 새로운 이미지 크기 계산
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

# 이미지 크기 조정
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)

# 캔버스 위젯 생성
Canvas1 = Canvas(root)

# 캔버스에 이미지 추가
Canvas1.create_image(365, 400, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

# 헤딩 프레임 생성
headingFrame1 = Frame(root, bg="#FFBB00", bd=10)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

# 헤딩 레이블 생성
headingLabel = Label(headingFrame1, text="도서 대여 시스템", bg='black', fg='white', font=('Courier', 25))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Tkinter 메인 루프 실행
root.mainloop()

## 회원 정보를 표시하는 함수
def display_user():
    # Tkinter 윈도우 생성 및 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=1200, height=800)
    root.geometry("600x500")
    
    # 데이터베이스 커서 생성
    cur = con.cursor()

    # 캔버스 위젯 생성 및 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lemon chiffon")
    Canvas1.pack(expand=True, fill=BOTH)

    # 헤딩 프레임 생성 및 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="회원 정보", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 회원 정보가 표시될 레이블 프레임 생성 및 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, height=420)
    y = 0.25
    
    # 컬럼명 레이블 생성
    Label(labelFrame, text=('회원 아이디'+'\t'+'이름'+'\t\t' +'생년월일'+'\t\t'+'주소'+'\t\t'+'전화번호'+'\t\t\t'+
                            '회원등록일'+'\t\t'+'대여권수'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    
    # 구분선 레이블 생성
    Label(labelFrame, text="--------------------------------------------------------------------------------------"
                           "---------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    # 회원 정보를 데이터베이스에서 가져와 표시
    cur.execute('SELECT * FROM userTbl ORDER BY userTbl.USER_NAME')
    row = cur.fetchone()
    while row:
        Label(labelFrame, text=(row[0]+'\t\t'+'{0:<8}'.format(row[1])+'\t'+'{0:<10}'.format(str(row[2]))+
                    '\t'+row[3]+'\t\t'+str(row[4])+'\t\t'+str(row[5])+'\t\t'+str(row[6])),
              bg='black', fg='white').place(relx=0.07, rely=y)
        y += 0.1
        row = cur.fetchone()
    
    # 스크롤바 추가
    scrollbar = Scrollbar(labelFrame)
    Listbox(labelFrame, yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    # 종료 버튼 생성 및 설정
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

## 회원 추가 함수
def Add_User():
    global UserInfo1, UserInfo2, UserInfo3, UserInfo4, UserInfo5, UserInfo6
    
    # Tkinter 윈도우 생성 및 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=400, height=650)
    root.geometry("600x500")

    # 캔버스 위젯 생성 및 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lemon chiffon")
    Canvas1.pack(expand=True, fill=BOTH)

    # 헤딩 프레임 생성 및 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="회원 등록", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 회원 정보 입력 프레임 생성 및 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # 회원 아이디 입력
    lb1 = Label(labelFrame, text="회원아이디: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.14, relheight=0.08)
    UserInfo1 = Entry(labelFrame)
    UserInfo1.place(relx=0.3, rely=0.14, relwidth=0.62, relheight=0.08)

    # 이름 입력
    lb2 = Label(labelFrame, text="이름\t: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.28, relheight=0.08)
    UserInfo2 = Entry(labelFrame)
    UserInfo2.place(relx=0.3, rely=0.28, relwidth=0.62, relheight=0.08)

    # 생년월일 입력
    lb3 = Label(labelFrame, text="생년월일\t: ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.42, relheight=0.08)
    UserInfo3 = Entry(labelFrame)
    UserInfo3.place(relx=0.3, rely=0.42, relwidth=0.62, relheight=0.08)

    # 지역 입력
    lb4 = Label(labelFrame, text="지역\t: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.56, relheight=0.08)
    UserInfo4 = Entry(labelFrame)
    UserInfo4.place(relx=0.3, rely=0.56, relwidth=0.62, relheight=0.08)

    # 전화번호 입력
    lb5 = Label(labelFrame, text="전화번호\t: ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.70, relheight=0.08)
    UserInfo5 = Entry(labelFrame)
    UserInfo5.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    # 등록 버튼 생성 및 설정
    SubmitBtn = Button(root, text="등록", bg='#d1ccc0', fg='black', command=userRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    # 종료 버튼 생성 및 설정
    quitBtn = Button(root, text="종료", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # Tkinter 메인 루프 실행
    root.mainloop()

## 회원 등록 처리 함수
def userRegister():
    # 현재 날짜와 시간을 가져옴
    now = datetime.now()
    cur = con.cursor()
    
    # 사용자 입력값을 가져옴
    USER_ID = UserInfo1.get()
    allUID = []
    USER_NAME = UserInfo2.get()
    USER_BIRTH = UserInfo3.get()
    USER_ADDR = UserInfo4.get()
    USER_PHONE = UserInfo5.get()
    USER_REG_DATE = now.date()
    cnt = 0

    # 모든 회원 ID를 데이터베이스에서 가져옴
    cur.execute('SELECT USER_ID FROM userTbl')
    row = cur.fetchone()
    while row:
        allUID.append((row[0]))
        
        # 입력된 ID가 이미 등록된 ID와 일치하는지 확인
        if '{0:<10}'.format(row[0]) == '{0:<10}'.format(USER_ID):
            messagebox.showinfo("등록 실패", '이미 등록된 회원입니다!')
            break
        else:
            row = cur.fetchone()
            cnt += 1

    # 입력된 ID가 기존 회원 ID와 중복되지 않는 경우
    if cnt == len(allUID):
        # 새 회원 정보를 데이터베이스에 삽입
        query = "INSERT INTO userTbl VALUES(%s, %s, %s, %s, %s, %s, '0')"
        cur.execute(query, (USER_ID, USER_NAME, USER_BIRTH, USER_ADDR, USER_PHONE, USER_REG_DATE))
        con.commit()
        messagebox.showinfo("등록 완료", '회원이 등록 완료되었습니다!')

## 도서 목록을 표시하는 함수
def display_book():
    # Tkinter 윈도우 생성 및 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=1000, height=700)
    root.geometry("600x500")
    cur = con.cursor()

    # 캔버스 위젯 생성 및 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lavender")
    Canvas1.pack(expand=True, fill=BOTH)

    # 헤딩 프레임 생성 및 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="도서 목록", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 도서 정보가 표시될 레이블 프레임 생성 및 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25
    
    # 컬럼명 레이블 생성
    Label(labelFrame, text=('도서 번호'+'\t\t'+'제목'+'\t\t\t\t'+'저자'+'\t\t'+'가격'+'\t\t'+'대여가능여부'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)
    
    # 구분선 레이블 생성
    Label(labelFrame, text="--------------------------------------------------------------------" +
                           "----------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    # 도서 정보를 데이터베이스에서 가져와 표시
    cur.execute('SELECT * FROM bookTbl')

    row = cur.fetchone()
    while row:
        # 도서 제목의 길이에 따라 탭 간격 조절
        if len(str(row[1])) >= 13:
            textTab1 = '\t\t'
        else:
            textTab1 = '\t\t\t'
        
        # 도서 정보를 레이블에 표시
        label1 = Label(labelFrame, text=(str(row[0]) + '\t\t' + str(row[1]) + textTab1
                                         + format(row[2]) + '\t\t' + str(row[3]) + '\t\t' + row[4]),
                       bg='black', fg='white').place(relx=0.07, rely=y)
        y += 0.1
        row = cur.fetchone()
    
    # 스크롤바 추가
    scrollbar = Scrollbar(labelFrame)
    Listbox(labelFrame, yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # 종료 버튼 생성 및 설정
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

## 도서 등록 창을 여는 함수
def Add_Book():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4

    # Tkinter 윈도우 생성 및 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # 캔버스 위젯 생성 및 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lavender")
    Canvas1.pack(expand=True, fill=BOTH)

    # 헤딩 프레임 생성 및 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="도서 등록", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 도서 정보 입력을 위한 레이블 프레임 생성 및 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # 도서 번호 입력 레이블 및 입력 필드 생성
    lb1 = Label(labelFrame, text="도서번호\t: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # 제목 입력 레이블 및 입력 필드 생성
    lb2 = Label(labelFrame, text="제목\t: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # 저자 입력 레이블 및 입력 필드 생성
    lb3 = Label(labelFrame, text="저자\t: ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # 가격 입력 레이블 및 입력 필드 생성
    lb4 = Label(labelFrame, text="가격\t: ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # 도서 등록 버튼 생성 및 설정
    SubmitBtn = Button(root, text="등록", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # 종료 버튼 생성 및 설정
    quitBtn = Button(root, text="종료", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

## 도서 등록 처리 함수
def bookRegister():
    # 데이터베이스 커서 생성
    cur = con.cursor()

    # 입력 필드에서 도서 정보 가져오기
    ID = bookInfo1.get()
    allBID = []  # 이미 등록된 도서 ID들을 저장할 리스트
    TITLE = bookInfo2.get()
    AUTHOR = bookInfo3.get()
    PRICE = bookInfo4.get()
    cnt = 0  # 도서 ID 비교를 위한 카운터

    # 데이터베이스에서 모든 도서 ID 가져오기
    cur.execute('SELECT BOOK_ID FROM bookTbl')
    row = cur.fetchone()

    # 모든 도서 ID를 리스트에 추가하고 중복 확인
    while row:
        allBID.append((row[0]))
        if '{0:<10}'.format(row[0]) == '{0:<10}'.format(ID):
            # 이미 등록된 도서 ID가 존재하면 메시지 박스를 띄움
            messagebox.showinfo("등록 실패", '이미 등록된 책입니다!')
            break
        else:
            row = cur.fetchone()
            cnt += 1

    # 중복된 도서 ID가 없으면 도서 정보 삽입
    if cnt == len(allBID):
        # 도서 정보를 데이터베이스에 삽입하는 쿼리
        query = "INSERT INTO bookTbl VALUES(%s,%s,%s, %s ,'Y')"
        cur.execute(query, (ID, TITLE, AUTHOR, PRICE))
        con.commit()  # 변경 사항 커밋
        # 성공 메시지 표시
        messagebox.showinfo("등록 완료", '책이 등록 완료되었습니다!')

## 도서 대여 처리 함수
def rent_book():
    global RentInfo1, RentInfo2, RentInfo3, RentInfo4

    # Tkinter 윈도우 생성 및 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=200, height=200)
    root.geometry("500x400")

    # 배경 캔버스 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lavender")
    Canvas1.pack(expand=True, fill=BOTH)

    # 헤딩 프레임 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    # 헤딩 라벨 설정
    headingLabel = Label(headingFrame1, text="도서 대여", bg='black', fg='white', font=('Courier', 16, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 입력 라벨 프레임 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # 회원 아이디 라벨 및 입력 필드
    lb1 = Label(labelFrame, text="회원 ID \t\t:  ", font=('Courier', 10), bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    RentInfo1 = Entry(labelFrame)
    RentInfo1.place(relx=0.4, rely=0.2, relwidth=0.3, relheight=0.08)

    # 도서번호 라벨 및 입력 필드
    lb2 = Label(labelFrame, text="대여할 도서 번호 \t: ", font=('Courier', 10), bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    RentInfo2 = Entry(labelFrame)
    RentInfo2.place(relx=0.4, rely=0.35, relwidth=0.3, relheight=0.08)

    # 대여 버튼
    SubmitBtn = Button(root, text="대여", bg='#d1ccc0', fg='black', command=rentRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # 종료 버튼
    quitBtn = Button(root, text="종료", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # Tkinter 메인 루프 시작
    root.mainloop()

## 도서 대여 등록 함수
def rentRegister():
    # 현재 날짜 및 시간 가져오기
    now = datetime.now()
    cur = con.cursor()
    
    # 사용자 입력값 가져오기
    UID = RentInfo1.get()  # 회원 ID
    BID = RentInfo2.get()  # 도서 ID
    
    # 대여 날짜 및 반납 예정 날짜 설정
    RENT_DATE = now.date()  # 대여 날짜: 오늘 날짜
    RENT_RETURN_DATE = RENT_DATE + timedelta(weeks=2)  # 반납 예정 날짜: 2주 후

    # 도서의 대여 가능 여부 확인
    query = "SELECT BOOK_RENT_YN FROM bookTbl WHERE BOOK_ID = %s"
    cur.execute(query, BID)
    RENT_YN = cur.fetchone()

    if RENT_YN[0] == "Y":  # 도서가 대여 가능할 때
        # 대여 정보 rentTbl 테이블에 추가
        query = "INSERT INTO rentTbl VALUES(%s, %s, %s, %s, 'X')"
        cur.execute(query, (UID, BID, RENT_DATE, RENT_RETURN_DATE))
        con.commit()

        # bookTbl 테이블에서 해당 도서의 대여 가능 여부를 'N'으로 업데이트
        query = "UPDATE bookTbl SET BOOK_RENT_YN = 'N' WHERE BOOK_ID = %s"
        cur.execute(query, BID)
        con.commit()

        # userTbl 테이블에서 해당 사용자의 대여 권수 증가
        query = "UPDATE userTbl SET USER_RENT_COUNT = USER_RENT_COUNT + 1 WHERE USER_ID = %s"
        cur.execute(query, UID)
        con.commit()

        # 대여 완료 메시지 박스 표시
        messagebox.showinfo("대여 완료", "대여가 완료되었습니다!")

    elif RENT_YN[0] == 'N':  # 도서가 이미 대여 중일 때
        # 대여 실패 메시지 박스 표시
        messagebox.showinfo("대여 실패", '대여할 수 없습니다!')

    else:  # 기타 오류 발생 시
        # 대여 실패 메시지 박스 표시
        messagebox.showinfo("대여 실패", '대여할 수 없습니다!')

## 도서 반납 함수
def return_book():
    global ReturnInfo1  # 도서 번호 입력값을 저장할 전역 변수

    # GUI 창 설정
    root = Tk()
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")
    root.minsize(width=300, height=150)  # 최소 창 크기 설정
    root.geometry("600x500")  # 창 크기 설정

    # Canvas 설정
    Canvas1 = Canvas(root)
    Canvas1.config(bg="lavender")  # 배경 색상 설정
    Canvas1.pack(expand=True, fill=BOTH)  # 창 크기에 맞게 확장

    # 헤딩 프레임 설정
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="도서 반납", bg='black', fg='white', font=('Courier', 16, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 라벨 프레임 설정
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # 도서번호 입력 라벨 및 입력창 설정
    lb1 = Label(labelFrame, text="반납할 도서 번호 \t: ", font=('Courier', 10), bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.35, relheight=0.08)
    ReturnInfo1 = Entry(labelFrame)
    ReturnInfo1.place(relx=0.4, rely=0.35, relwidth=0.3, relheight=0.08)

    # 반납 버튼 설정
    SubmitBtn = Button(root, text="반납", bg='#d1ccc0', fg='black', command=returnRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # 종료 버튼 설정
    quitBtn = Button(root, text="종료", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.58, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

## 반납 등록 함수
def returnRegister():
    cur = con.cursor()  # 데이터베이스 커서 객체 생성
    UID = ReturnInfo1.get()  # 반납할 도서 번호를 가져옴
    allUID = []  # 모든 도서 번호를 저장할 리스트

    # 대여 목록에서 반납 확인이 'X'인 도서 조회
    cur.execute("SELECT BOOK_ID, RENT_RETURN_CHECK FROM rentTbl WHERE RENT_RETURN_CHECK='X'")
    row = cur.fetchone()  # 조회 결과에서 첫 번째 행을 가져옴

    cnt = 0  # 반납할 도서 번호가 없을 경우를 확인하기 위한 카운터
    while row:
        allUID.append(row[0])  # 조회된 도서 번호를 리스트에 추가
        if str(row[0]) == UID:  # 반납할 도서 번호를 찾은 경우
            # 대여 목록에서 해당 도서의 반납 확인을 'O'로 업데이트
            query = "UPDATE rentTbl SET RENT_RETURN_CHECK='O' FROM rentTbl WHERE BOOK_ID = %s AND RENT_RETURN_CHECK='X'"
            cur.execute(query, UID)  # SQL 쿼리 실행
            con.commit()  # 변경 내용을 데이터베이스에 반영
            break  # 반납 처리가 완료되었으므로 반복문 탈출
        else:
            print("반납실패")  # 잘못된 도서 번호를 입력한 경우를 출력
            row = cur.fetchone()  # 다음 행을 가져옴
            cnt += 1  # 카운터를 증가시킴

    # 반납할 도서 번호가 없는 경우
    if cnt == len(allUID):
        messagebox.showinfo("반납 실패", '도서 번호를 다시 입력해주세요!')  # 메시지 박스를 통해 알림
        return  # 함수 종료

    # 대여 목록에서 반납이 완료된 도서를 검색하여 처리
    cur2 = con.cursor()  # 새로운 데이터베이스 커서 객체 생성
    query = "SELECT * FROM rentTbl WHERE BOOK_ID = %s AND RENT_RETURN_CHECK = 'O'"  # 대여 목록에서 반납이 완료된 도서 검색 쿼리
    cur2.execute(query, UID)  # SQL 쿼리 실행
    row2 = cur2.fetchone()  # 조회된 결과에서 첫 번째 행을 가져옴
    cnt = 0  # 반납할 도서 번호가 없을 경우를 확인하기 위한 카운터 초기화
    while row2:
        if str(row2[1]) == UID:  # 반납이 완료된 도서를 찾은 경우
            # 해당 사용자의 대여 횟수를 1 감소시킴
            query = "UPDATE userTbl SET USER_RENT_COUNT -= 1 FROM userTbl WHERE USER_ID = %s "
            cur2.execute(query, str(row2[0]))  # SQL 쿼리 실행
            con.commit()  # 변경 내용을 데이터베이스에 반영

            # 해당 도서의 대여 가능 여부를 'Y'로 업데이트
            query = "UPDATE bookTbl SET BOOK_RENT_YN='Y' FROM bookTbl WHERE BOOK_ID = %s "
            cur.execute(query, UID)  # SQL 쿼리 실행
            con.commit()  # 변경 내용을 데이터베이스에 반영

            messagebox.showinfo("반납 완료", '반납이 완료되었습니다!')  # 메시지 박스를 통해 반납 완료를 알림
            break  # 반납 처리가 완료되었으므로 반복문 탈출
        else:
            row2 = cur2.fetchone()  # 다음 행을 가져옴
            cnt += 1  # 카운터를 증가시킴

    # 반납할 도서 번호가 없는 경우
    if cnt == len(allUID):
        messagebox.showinfo("반납 실패", '도서 번호를 다시 입력해주세요!')  # 메시지 박스를 통해 알림

# 대여 현황 표시 함수
def display_rent():
    root = Tk()  # Tkinter 윈도우 생성
    root.title("도서대여 프로그램(데이터베이스 기말과제_2019E8003)")  # 윈도우 제목 설정
    root.minsize(width=1100, height=700)  # 윈도우 최소 크기 설정
    root.geometry("600x500")  # 윈도우 크기 설정
    cur = con.cursor()  # 데이터베이스 커서 생성

    Canvas1 = Canvas(root)  # 캔버스 위젯 생성
    Canvas1.config(bg="lightblue")  # 캔버스 배경색 설정
    Canvas1.pack(expand=True, fill=BOTH)  # 캔버스 크기 조정

    # 헤딩 프레임 생성
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    # 헤딩 레이블 생성
    headingLabel = Label(headingFrame1, text="대여 현황", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # 레이블 프레임 생성
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # 헤더 레이블 생성
    Label(labelFrame, text=('회원 번호'+'\t\t'+'이름'+'\t\t' +'제목'+'\t\t\t\t'+'도서 대출일'+'\t'+'반납 예정일'+
                            '\t'+'반납 여부'), bg='black', fg='white').place(relx=0.07, rely=0.1)

    # 구분선 레이블 생성
    Label(labelFrame, text="---------------------------------------------------------------------------"
                           + "--------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    # 데이터베이스에서 대여 목록 조회
    cur.execute('SELECT rentTbl.USER_ID, USER_NAME, BOOK_TITLE, RENT_DATE, RENT_RETURN_DATE, RENT_RETURN_CHECK '+
                'FROM rentTbl '+
                'JOIN userTbl ON rentTbl.USER_ID=userTbl.USER_ID '+
                'JOIN bookTbl ON rentTbl.BOOK_ID=bookTbl.BOOK_ID '+
                'WHERE rentTbl.USER_ID=userTbl.USER_ID '+
                'ORDER BY RENT_RETURN_CHECK, RENT_RETURN_DATE')

    row = cur.fetchone()  # 조회 결과에서 첫 번째 행 가져오기
    while row:
        if len(str(row[2])) >= 13:
            textTab2='\t\t'
        else:
            textTab2='\t\t\t'
        # 각 대여 정보를 레이블로 표시
        label1 = Label(labelFrame,
                      text=(str(row[0])+'\t\t'+'{0:<10}'.format(row[1])+'\t'+'{0:<10}'.format(row[2])+
                             textTab2+'{0:<10}'.format(str(row[3]))+'\t'+'{0:<10}'.format(str(row[4]))+'\t'+row[5]),
                       bg='black', fg='white').place(relx=0.07, rely=y)
        y += 0.1  # 다음 행에 표시하기 위해 y 좌표 증가
        row = cur.fetchone()  # 다음 행 가져오기

    scrollbar = Scrollbar(labelFrame)  # 스크롤바 위젯 생성
    Listbox(labelFrame, yscrollcommand=scrollbar.set)  # 리스트박스 위젯 생성
    scrollbar.pack(side="right", fill="y")  # 스크롤바 배치

    # 종료 버튼 생성
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

# 회원 정보 버튼
btn1 = Button(root, text="회원 정보", bg='lemon chiffon', fg='black', font=('Courier', 12, 'bold'),
              command=lambda: display_user())  # display_user 함수를 호출하여 회원 정보를 표시합니다.
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.08)

# 회원 등록 버튼
btn2 = Button(root, text="회원 등록", bg='lemon chiffon', font=('Courier', 12, 'bold'), fg='black',
              command=lambda: Add_User())  # Add_User 함수를 호출하여 새 회원을 등록합니다.
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.08)

# 도서 목록 버튼
btn3 = Button(root, text="도서 목록", bg='lavender', font=('Courier', 12, 'bold'), fg='black',
              command=lambda: display_book())  # display_book 함수를 호출하여 도서 목록을 표시합니다.
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.08)

# 도서 등록 버튼
btn4 = Button(root, text="도서 등록", bg='lavender', fg='black', font=('Courier', 12, 'bold'),
              command=lambda: Add_Book())  # Add_Book 함수를 호출하여 새 도서를 등록합니다.
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.08)

# 도서 대여 버튼
btn5 = Button(root, text="도서 대여", bg='lavender', fg='black', font=('Courier', 12, 'bold'),
              command=lambda: rent_book())  # rent_book 함수를 호출하여 도서를 대여합니다.
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.08)

# 도서 반납 버튼
btn5 = Button(root, text="도서 반납", bg='lavender', fg='black', font=('Courier', 12, 'bold'),
              command=lambda: return_book())  # return_book 함수를 호출하여 도서를 반납합니다.
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.08)

# 대여 현황 버튼
btn6 = Button(root, text="대여 현황", bg='lightblue', fg='black', font=('Courier', 12, 'bold'),
              command=lambda: display_rent())  # display_rent 함수를 호출하여 대여 현황을 표시합니다.
btn6.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.08)

root.mainloop()
