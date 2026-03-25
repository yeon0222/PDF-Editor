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
