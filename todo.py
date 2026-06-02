add=[]
i=0
while True:
    print("1.Show task")
    print("2.Add task")
    print("3.Remove task")
    print("4.Exit")
    c=input("enter your choice[1-4]:")
    if c=='1':
        i=0
        while i<len(add):
            print(add[i])
            i+=1
    elif c=='2':
        act=input("enter activity:")
        add.append(act)
    elif c=='3':
        if len(add) == 0:
            print("no activity to remove.")
        else:
            rem=input("enter the activity to remove:")
            add.remove(rem)
    else:
        break



    

