# 이미지 삽입을 위한 자원 경로 설정
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
