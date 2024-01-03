import tkinter as tk
color=['red','blue','green','orange','yellow','cyan','magenta']
r=0
for i in color:    
    tk.Label(text=i,bg=i,relief=tk.SUNKEN,width=60).grid(row=r,column=1)
    r=r+1
tk.mainloop()
