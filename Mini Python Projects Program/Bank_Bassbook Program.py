class Bank:
    def statement(self):
        import time
        opening=10000.0
        o_bal=10000.0
        cr,dr,tl,st,tm=[],[],[],[],[]
        x=int(input("Enter numbers of transction: "))
        for i in range(1,x+1):
            print('------------------------------------------------')
            print('       Welcome to Indian Overseas Bank          ')
            print('------------------------------------------------')
            print('enter choice for transaction:',i)
            choice=int(input("type:(1.Credit | 2.Debit):"))
            if choice==1:
                c_amt=float(input("Enter the amount to be Deposit:"))
                cr.append(c_amt)
                dr.append(0.0)
                o_bal+=c_amt   # o_bal = o_bal + c_amt 
                tl.append(o_bal)
                st.append('Cr')
                tm.append(str(time.ctime(time.time())))
            elif choice==2:
                d_amt=float(input("Enter the amount to be Withdraw:"))
                dr.append(d_amt)
                cr.append(0.0)
                o_bal-=d_amt  # o_bal = o_bal - d_amt
                tl.append((o_bal))
                st.append('Dr')
                tm.append(str(time.ctime(time.time())))
        print('*****************************************************************************')
        print('                 INDIAN OVERSEAS BANK - PASS BOOK DETAILS                    ')
        print('*****************************************************************************')
        print('opening balance:',opening)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Status       Credit         Debit         Total              Time            ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for a,b,c,d,e in zip(st,cr,dr,tl,tm):
            print('  %s        %s          %s        %s        %s' % (a,b,c,d,e))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
b=Bank()
b.statement() 
        
