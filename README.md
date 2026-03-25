# PDF-Editor

> ## 👏 Overview
> > ### Functions
> > > +  PDF 분할 및 병합 📑
> > > +  마우스 드래그 앤 드롭 🖱
> > > +  PDF 병합 순서 변경 및 선택 삭제 ✂
> > ### Tech
> > > #### Programming Language / Library
> > > + Python, tkinter, PyPDF2, TkinterDnD2  
> > > #### IDE
> > > + Visual Studio Code

<br/>
<hr/>
<br/>

> ## 🛠️ Details
> > ### ① 프로그램 전체 프레임 구성
> > > + 파일 프레임
> > >   +  PDF 파일 추가(디렉토리 조회)
> > >   +  리스트 프레임 상 PDF 파일 순서 변경
> > >   +  리스트 프레임 상 PDF 파일 선택 삭제
> > > + 리스트 프레임
> > >   + 리스트 박스(마우스 드래그 앤 드롭)
> > >   + 세로 스크롤바
> > > + 저장 경로 프레임
> > >   + 저장경로 찾기(디렉토리 조회)
> > >   + 저장경로 입력란 및 가로 스크롤바
> > > + 실행 프레임
> > >   + PDF 파일 분할 및 병합 실행 버튼
> > >   
> > ### ② PDF 병합 순서 변경 및 선택 삭제
> > > 여러 개의 PDF 파일을 병합 시 '↑ ', '↓' 버튼을 클릭하여 병합되는 순서를 변경할 수 있습니다
> > >
> > > #### Features
> > > + 순서 변경 시 해당 파일이 리스트를 벗어나지 않도록 index 제한 설정
> > > + pdf 파일 삭제 시 reversed()를 통해 역순으로 정렬 후 for문을 통해 삭제
> > >   + index 0 ~7의 pdf 파일이 있다고 했을 때, 0을 먼저 삭제 하면 뒤에 있는 pdf 파일이 앞으로 오기 때문에 나중에 7이 삭제되지 않기 때문
> >
> > ### ③ 마우스 드래그 앤 드롭
> > > PDF 파일이 깊은(복잡한) 디렉토리에 존재하는 경우 디렉토리를 타고 PDF 파일을 등록하기 번거로우므로 파일을 끌어다가 프로그램에 직접 등록시킬 수 있습니다.
> > > 
> > > #### Features
> > > + TkinterDnD2 라이브러리의 drag_source_register, dnd_bind 등의 메서드와 widget 속성 활용
> >
> > ### ④ PDF 분할 및 병합
> > > 여러 페이지의 PDF를 분할할 수 있고 여러 개의 PDF 파일을 병합하여 새로운 PDF 파일을 생성할 수 있습니다.
> > > 
> > > #### Features
> > > + PyPDF2 라이브러리의 PdfFileWriter 및 PdfFileReader 객체를 통한 pdf 파일 분할
> > > + PyPDF2 라이브러리의 PdfFileMerger 객체를 통한 pdf 파일 병합

<br/>
<hr/>
<br/>
