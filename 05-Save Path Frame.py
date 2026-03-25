# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    # askdirectory : 사용자가 취소한 경우 (아무것도 없음) 반환
    if folder_selected == '': # 사용자가 취소를 누를 때 folder_selected 값은 (아무것도 없음)
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)
