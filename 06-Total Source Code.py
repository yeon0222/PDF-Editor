from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
import sys
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog # 서브 모듈이기 때문에 별도로 import 필요

from TkinterDnD2 import *

root = TkinterDnD.Tk()
root.title("PDF Editor")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title = "PDF 파일을 선택하세요", \
        filetypes = (("PDF 파일", "*.pdf"), ("모든 파일", "*.*")))
        # 최초에 사용자가 지정한 경로를 보여줌 / r(row string) : 탈출 문자 기능 제거(\ 두 번 할 필요없음)

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 파일 순서 변경
def move_up_file():
    for index in reversed(list_file.curselection()):
        if index > 0:
            list_file.insert(index+1, list_file.get(index-1))
            list_file.delete(index-1)

# 파일 순서 변경
def move_down_file():
    for index in reversed(list_file.curselection()):
        if index + 1 < list_file.index(END):
            list_file.insert(index, list_file.get(index+1))
            list_file.delete(index+2)

# 선택 삭제
def del_file():
    for index in reversed(list_file.curselection()):
        # 거꾸로 지우지 않으면 인덱스 0, 7 삭제 시 0을 먼저 지우면 앞으로 땡겨지기 때문에 당초 삭제하려고 했던 7이 삭제 X
        # reverse는 실제 리스트의 순서를 바꾸나, reversed는 실제 리스트의 순서를 바꾸진 않고 순서를 바꾼 값을 전달하기만 한다.
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    # askdirectory : 사용자가 취소한 경우 (아무것도 없음) 반환
    if folder_selected == '': # 사용자가 취소를 누를 때 folder_selected 값은 (아무것도 없음)
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# PDF 병합
def merge_pdf():
    try:
        fileExt = ".pdf"
        list_pdf = list(list_file.get(0, END))
        filenames = [i for i in list_pdf if i.endswith(fileExt)] # PDF 리스트
        list_pdf.clear()

        if not filenames:
            pass

        else:
            merger = PdfFileMerger()
            for filename in filenames:
                merger.append(filename)
            
            save_name = "merge_" + "1" + "-" + str(len(filenames)) + ".pdf"
            dest_path = os.path.join(txt_dest_path.get(), save_name)
            # os.path.join(path1, path2,...) : 괄호 안 path 순서대로 묶어 하나의 path로 생성
            merger.write(dest_path)
            merger.close()
            msgbox.showinfo("알림", "작업이 완료되었습니다.")
            txt_dest_path.delete(0, END)
            list_file.delete(0, END)

    except Exception as err: # 예외 처리
        msgbox.showerror("에러", err)

# PDF 분할
def split_pdf():
    try:
        list_pdf = list_file.get(0)
        pdf = PdfFileReader(open(list_pdf, 'rb')) # 분할 대상 pdf 파일 경로 설정
        numberPages = pdf.getNumPages()

        for page in range(numberPages):
            
            pdf_writer = PdfFileWriter() # 빈 pdf 생성
            pdf_writer.addPage(pdf.getPage(page)) # pdf의 각페이지(page)를 얻어와서 빈 pdf에 저장

            # 파일명 정하기
            output_filename = "page_{}.pdf".format(page + 1)

            save_path = os.path.join(txt_dest_path.get(), output_filename)

            # 파일 쓰기
            with open(save_path, 'wb') as f:
                pdf_writer.write(f)

        msgbox.showinfo("알림", "작업이 완료되었습니다.")
        txt_dest_path.delete(0, END)
        list_file.delete(0, END)

    except Exception as err: # 예외 처리
        msgbox.showerror("에러", err)

# 병합 시작
def merge_start():
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "PDF 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    merge_pdf()

# 분할 시작
def split_start():
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "PDF 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합 작업
    split_pdf()

# 파일 프레임 (파일 추가, 선택 삭제, 파일 순서 변경)
  # 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill = "x", padx = 10, pady = 10)

  # 파일 추가
btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 10, text = "파일 추가", command = add_file)
btn_add_file.pack(side = "left")

  # 선택 삭제
btn_del_file = Button(file_frame, padx = 5, pady = 5, width = 10, text = "선택 삭제", command = del_file)
btn_del_file.pack(side = "right")

  # 파일 순서 변경(↓)
btn_move_down_file = Button(file_frame, padx = 5, pady = 5, width = 10, text = "순서 변경(↓)", command = move_down_file)
btn_move_down_file.pack(side = "right")

  # 파일 순서 변경(↑)
btn_move_up_file = Button(file_frame, padx = 5, pady = 5, width = 10, text = "순서 변경(↑)", command = move_up_file)
btn_move_up_file.pack(side = "right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill = "both", padx = 5, pady = 5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)
list_file.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = list_file.yview)

text = Text() # 마우스 앤 드래그 설정 영역

def drop_enter(event):
    event.widget.focus_force()
    return event.action

def drop_position(event):
    return event.action

def drop_leave(event):
    return event.action

def drop(event):
    if event.data:
        if event.widget == list_file:
            # event.data is a list of filenames as one string;
            # if one of these filenames contains whitespace characters
            # it is rather difficult to reliably tell where one filename
            # ends and the next begins; the best bet appears to be
            # to count on tkdnd's and tkinter's internal magic to handle
            # such cases correctly; the following seems to work well
            # at least with Windows and Gtk/X11
            files = list_file.tk.splitlist(event.data)
            for f in files:
                if os.path.exists(f):
                    list_file.insert('end', f)
                else:
                    pass
        elif event.widget == text:
            # calculate the mouse pointer's text index
            bd = text['bd'] + text['highlightthickness']
            x = event.x_root - text.winfo_rootx() - bd
            y = event.y_root - text.winfo_rooty() - bd
            index = text.index('@%d,%d' % (x,y))
            text.insert(index, event.data)
        else:
            pass
    return event.action

# now make the Listbox and Text drop targets
list_file.drop_target_register(DND_FILES, DND_TEXT)
text.drop_target_register(DND_TEXT)

for widget in (list_file, text):
    widget.dnd_bind('<<DropEnter>>', drop_enter)
    widget.dnd_bind('<<DropPosition>>', drop_position)
    widget.dnd_bind('<<DropLeave>>', drop_leave)
    widget.dnd_bind('<<Drop>>', drop)
    # widget.dnd_bind('<<Drop:DND_Files>>', drop)
    # widget.dnd_bind('<<Drop:DND_Text>>', drop)

# define drag callbacks

def drag_init_listbox(event):
    
    # use a tuple as file list, this should hopefully be handled gracefully
    # by tkdnd and the drop targets like file managers or text editors
    data = ()
    if list_file.curselection():
        data = tuple([list_file.get(i) for i in list_file.curselection()])
        
    # tuples can also be used to specify possible alternatives for
    # action type and DnD type:
    return ((ASK, COPY), (DND_FILES, DND_TEXT), data)

def drag_init_text(event):
    
    # use a string if there is only a single text string to be dragged
    data = ''
    sel = text.tag_nextrange(SEL, '1.0')
    if sel:
        data = text.get(*sel)
        
    # if there is only one possible alternative for action and DnD type
    # we can also use strings here
    return (COPY, DND_TEXT, data)

def drag_end(event):
    # this callback is not really necessary if it doesn't do anything useful
    event.widget

# finally make the widgets a drag source

list_file.drag_source_register(1, DND_TEXT, DND_FILES)
text.drag_source_register(3, DND_TEXT)

list_file.dnd_bind('<<DragInitCmd>>', drag_init_listbox)
list_file.dnd_bind('<<DragEndCmd>>', drag_end)
text.dnd_bind('<<DragInitCmd>>', drag_init_text)
# skip the useless drag_end() binding for the text widget

# 저장 경로 프레임
path_frame = LabelFrame(root, text = "저장경로")
path_frame.pack(fill = "x", padx = 5, pady = 5, ipady = 5)

path_frame_right = Frame(path_frame)
path_frame_right.pack(side="right", fill = "x", padx = 5, pady = 5, ipady = 5)

path_frame_left = Frame(path_frame)
path_frame_left.pack(side="left", fill = "x", expand = True, padx = 5, pady = 5, ipady = 5)

scrollbar2 = Scrollbar(path_frame_left, orient="horizontal")
scrollbar2.pack(side = "bottom", fill = "x")

txt_dest_path = Entry(path_frame_left, xscrollcommand = scrollbar2.set)
txt_dest_path.pack(fill = "x", expand = True, padx = 5, pady = 5, ipady = 4) # ipad : 엔트리 영역 높이 변경

scrollbar2.config(command = txt_dest_path.xview)

btn_dest_path = Button(path_frame_right, text = "저장경로 찾기", width = 12, height = 3,command = browse_dest_path)
btn_dest_path.pack(padx = 5, pady = 5)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady = 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "닫기", width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5)

btn_merge = Button(frame_run, padx = 5, pady = 5, text = "병합", width = 12, command = merge_start)
btn_merge.pack(side = "right", padx = 5, pady = 5)

btn_split = Button(frame_run, padx = 5, pady = 5, text = "분할", width = 12, command = split_start)
btn_split.pack(side = "right", padx = 5, pady = 5)

root.update_idletasks()
root.deiconify()
root.resizable(False, False) # False : x(너비) / y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()
