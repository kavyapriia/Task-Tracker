num=int(input("give the number of tasks you need:"))
d={}
for i in range(num):
  key=input("enter task: ")
  value=input("enter progress:")
  d[key]=value
print(d)
action=input("add or mark or update or delete or list:")
if action=="add":
  key=input("enter task: ")
  value=input("enter progress:")
  d[key]=value
  print(d)

elif action=="update":
  keys_list=list(d.keys())
  n1=int(input("enter the task number you want to update:"))
  old_key=keys_list[n1]
  new_key=input("enter updated task")
  d.pop(old_key)
  d[new_key]=value
  print(d)

elif action=="mark":
  keys_list=list(d.keys())
  n2=int(input("enter the taskk number you want to mark:"))
  #old_value=keys_list[n]
  new_value=input("enter updated progress:")
  d[keys_list[n2]]=new_value
  print(d)

elif action=="delete":
  keys_list=list(d.keys())
  n3=int(input("enter the task number you want to delete:"))
  del_key=keys_list[n3]
  d.pop(del_key)
  print(d)

elif action=="list":
  keys_list=list(d.keys())
  print(d)
else:
  print("enter add or mark or delete or list or update")
