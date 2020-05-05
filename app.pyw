import starter
import tkinter
import pathlib
import threading
from tkinter import filedialog
from tkinter import messagebox


class Button(tkinter.Button):
    def __init__(self):
        super().__init__(
            master=None,
            text="Go",
            width=85,
            command=self.Button_click
        )

    def Button_click(self):
        action(self)


class Switch(tkinter.Button):
  def __init__(self):
    super().__init__(
      master=None,
      text="switch R and B",
      width=20,
      command=self.Button_swap
    )

  def Button_swap(self):
    EditBox_sw['state'] = "normal"
    if EditBox_sw.get() == "ABC":
      EditBox_sw.delete(0, tkinter.END)
      EditBox_sw.insert(tkinter.END, "ARC")
    else:
      EditBox_sw.delete(0, tkinter.END)
      EditBox_sw.insert(tkinter.END, "ABC")
    EditBox_sw['state'] = "readonly"
    EditBox_num['state'] = "normal"


class Button_dir(tkinter.Button):
  def __init__(self):
    super().__init__(
      master=None,
      text="select dir",
      width=20,
      command=self.Button_click
    )

  def Button_click(self):
    EditBox_dir_ex["state"] = "normal"
    EditBox_dir_ex.delete(0, tkinter.END)
    file_dir = filedialog.askdirectory()
    EditBox_dir_ex.insert(tkinter.END, file_dir)
    EditBox_dir_ex["state"] = "readonly"


class Button_number(tkinter.Button):
  def __init__(self):
    super().__init__(
      master=None,
      text="non numbered contests",
      width=20,
      command=self.Button_num_clicked
    )

  def Button_num_clicked(self):
    EditBox_sw['state'] = "normal"
    EditBox_sw.delete(0, tkinter.END)
    EditBox_num.delete(0, tkinter.END)
    EditBox_num['state'] = "readonly"




def tmp():
  savepath =pathlib.Path("data.txt")
  if savepath.exists:
    savepath.write_text(EditBox_dir_ex.get())
  path = EditBox_dir_ex.get()
  target_head = EditBox_sw.get()
  try:
    target_bottom = int(EditBox_num.get())
  except :
    if EditBox_num.get() == "":
      target_bottom = EditBox_num.get()
    else :
      pass
      


  target = starter.maketarget(path, target_head, target_bottom)
  starter.prepare(target)
  starter.opencode(target)

def action(event):
  text_message.set("スタート！")
  thread = threading.Thread(target=tmp)
  thread.start()
  return


if __name__ == "__main__":
  print("Hello, this is log console")


  root = tkinter.Tk()
  root.title(u"Atcoder Starter")
  # root.geometry("1000x300")
  # root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(data=img_binary))


  ##ABC##
  EditBox_sw = tkinter.Entry(width=100)
  EditBox_sw.insert(tkinter.END,  "ABC")
  EditBox_sw["state"] = "readonly"
  EditBox_sw.grid(row=0, column=0, padx=10, pady=10)
  Button_sw = Switch()
  Button_sw.grid(row=0, column=1, padx=10, pady=10)

  ##num##
  EditBox_num = tkinter.Entry(width = 100)
  EditBox_num.grid(row=1, column=0, padx=10, pady=10)
  EditBox_num.bind('<Return>', action)
  Button_other = Button_number()
  Button_other.grid(row=1, column=1, padx=10, pady=10)



  ##dir##
  EditBox_dir_ex = tkinter.Entry(width=100)
  EditBox_dir_ex.insert(tkinter.END,  "None")
  EditBox_dir_ex["state"] = "readonly"
  EditBox_dir_ex.grid(row=2, column=0, padx=10, pady=10)
  Button_dir_ex = Button_dir()
  Button_dir_ex.grid(row=2, column=1, padx=10, pady=10)

  ##button##
  Button_do = Button()
  Button_do.grid(row=3, column=0, padx=10, pady=10)

  ##label##
  text_message = tkinter.StringVar()
  text_message.set(u"入力を行い、Goを押してください。")
  label_info = tkinter.Label(textvariable=text_message,
                            font=("", 10, "bold"), justify="left")
  label_info.grid(row=4, column=0, padx=10, pady=10)

  savepath = pathlib.Path("data.txt")
  if (savepath.exists()):
    EditBox_dir_ex["state"] = "normal"
    EditBox_dir_ex.delete(0, tkinter.END)
    EditBox_dir_ex.insert(tkinter.END,savepath.read_text())
    EditBox_dir_ex["state"] = "readonly"
  EditBox_num.focus_set()
  EditBox_num.icursor(0)
  root.mainloop()
