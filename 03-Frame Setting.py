root = TkinterDnD.Tk()
root.title("PDF Editor")

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

label2 = Label(frame_run, image = photo)
label2.pack(side="left")

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
