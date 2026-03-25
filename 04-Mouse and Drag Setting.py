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
