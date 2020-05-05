import pathlib
import shutil
import os
class NODIR_EXCEPTION(Exception):
  pass

def maketarget(path, target_head, target_bottom):
  if target_bottom == "":
    target_bottom_str = target_bottom
  elif target_bottom < 10:
    target_bottom_str = "00" + str(target_bottom)
  elif target_bottom < 100:
    target_bottom_str = "0" + str(target_bottom)
  else:
    target_bottom_str = str(target_bottom)

  target = path + "\\" + target_head + target_bottom_str + "\\"
  return target

def opencode(target):

  dirobj = pathlib.Path(target)
  command = "code " + target
  

  if dirobj.exists():
    os.system(command)
    os.system("exit /b")
  else:
    raise NODIR_EXCEPTION

def prepare(target):
  pass
  dirobj = pathlib.Path(target)
  if not (dirobj.exists()):
    dirobj.mkdir()
  cpp_a = pathlib.Path(target + "A.cpp")
  cpp_b = pathlib.Path(target + "B.cpp")
  cpp_c = pathlib.Path(target + "C.cpp")
  cpp_d = pathlib.Path(target + "D.cpp")
  cpp_e = pathlib.Path(target + "E.cpp")
  cpp_f = pathlib.Path(target + "F.cpp")
  tmppath = pathlib.Path("tmp.cpp")
  if not cpp_a.exists():
    shutil.copy2(tmppath, cpp_a)
  if not cpp_b.exists():
    shutil.copy2(tmppath, cpp_b)
  if not cpp_c.exists():
    shutil.copy2(tmppath, cpp_c)
  if not cpp_d.exists():
    shutil.copy2(tmppath, cpp_d)
  if not cpp_e.exists():
    shutil.copy2(tmppath, cpp_e)
  if not cpp_f.exists():
    shutil.copy2(tmppath, cpp_f)

if __name__ == "__main__":

  path = 'C:\\Users\\A\\Documents\\repos\\Atcoder'
  target_head = 'ABC'
  target_bottom = 141

  target = maketarget(path,target_head,target_bottom)
  prepare(target)
  opencode(target)