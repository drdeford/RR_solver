from tkinter import *
import tkinter.simpledialog
from backtermsinout import *

x=[2,3,4]

global var2

global var3
global var4

global var5
global var6

class App:
    global newt

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.text = Label(frame, text="Select the parameters that you want to enter:")
        #self.text.pack(side=TOP)
        self.text.grid(row=0,column=0)

       

        self.GPS = Button(frame, text="Generalized Power Sum", fg="purple",command=self.GPS)
        #self.GPS.pack(side=LEFT)
        self.GPS.grid(row=1,column=0)

        self.EIGS = Button(frame, text="Eigenvalues and Inital Terms",fg="blue", command=self.EIGS)
        #self.EIGS.pack(side=LEFT)
        self.EIGS.grid(row=2,column=0)

        #self.disp = Button(frame, text="Display Results",fg="orange", command= self.disp)
        #self.disp.grid(row=2,column=2)
        
        self.TERMS = Button(frame, text="Coefficients and Intial Terms",fg="green", command=self.TERMS)
        #self.TERMS.pack(side=LEFT)
        self.TERMS.grid(row=3,column=0)

	#self.num = Entry(frame, text="Order of Recurrence:")

        #self.example = Label(frame, text = "here is ", x, "stuff")
        #self.example.grid(row=2,column=1)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        #self.button.pack(side=BOTTOM)
        self.button.grid(row=4,column=0)
    def disp(self):
        rwin = Toplevel()
        #var1=StringVar()
        l1 = Label(rwin, text="Answer")
        l1.grid(row=0,column=1)
        l2 = Label(rwin, text="Recurrence Coefficients")
        l2.grid(row=1,column = 0)
        l3 = Label(rwin, text= str(newt[3]))
        l3.grid(row=1,column=1)
        b1=Button(rwin, text="Close", command=rwin.destroy)
        b1.grid(row=4,column=4)

    def say_hi(self):
        print ("hi there, everyone!")
        
    #def quitnow():
        #root.destroy()
        
    def GPS (self):
        print("GPS")
        
        class GPSDialog(tkinter.simpledialog.Dialog):

                def body(self, master):

                        Label(master, text="Coefficients (No Spaces):").grid(row=0)
                        Label(master, text="Eigenvalues (No Spaces):").grid(row=1)
                        Label(master, text="Number of Terms:").grid(row=2)
                        self.e1 = Entry(master)
                        self.e2 = Entry(master)
                        self.e3 = Entry(master)
                        self.e1.grid(row=0, column=1)
                        self.e2.grid(row=1, column=1)
                        self.e3.grid(row=2, column=1)
                        return self.e1 # initial focus

                def apply(self):
                        co2=[]
                        ei2=[]
                        coeffs2=[]
                        eigs2=[]
                        #coeffs = string.atoi(self.e1.get())
                        #eigs = string.atoi(self.e2.get())
                        coeffs = self.e1.get()
                        eigs = self.e2.get()
                        num = self.e3.get()
                        num = int(num)
                        for i in range(len(coeffs)):
                                if coeffs[i] == ',':
                                        co2.append(i)
                        temp2=''
                        for k in range(co2[0]):
                                temp2=temp2+coeffs[k]
                        coeffs2.append(float(temp2))
                        for i in range(len(co2)-1):
                                temp=''
                                for j in range((co2[i+1]-co2[i]-1)):
                                        temp=temp+coeffs[co2[i]+j+1]
                                coeffs2.append(float(temp))
                        temp3=''
                        for l in range(len(coeffs)-co2[-1]-1):
                                temp3=temp3+coeffs[co2[-1]+1+l]
                        coeffs2.append(float(temp3))

                        #for j in range(len(eigs)):
                        #	ei2=ei2+eigs[j]
                        #co2=list(co2)
                        for i in range(len(eigs)):
                                if eigs[i] == ',':
                                        ei2.append(i)
                        temp2=''
                        for k in range(ei2[0]):
                                temp2=temp2+eigs[k]
                        eigs2.append(float(temp2))
                        for i in range(len(ei2)-1):
                                temp=''
                                for j in range((ei2[i+1]-ei2[i]-1)):
                                        temp=temp+eigs[ei2[i]+j+1]
                                eigs2.append(float(temp))
                        temp3=''
                        for l in range(len(eigs)-ei2[-1]-1):
                                temp3=temp3+eigs[ei2[-1]+1+l]
                        eigs2.append(float(temp3))
                        print (coeffs2,eigs2,'\n')
                        top=Toplevel()
                       # l1 = Label(top, text="Recurrence Solution")
                       # l1.grid(row=0,column=1)
                        top.title("Recurrence Solution")
                        # or something
                        newt=bothgps(num,eigs2,coeffs2)
                        l2 = Label(top, text="Recurrence Coefficients:",fg="blue")
                        l2.grid(row=1,column = 0)
                        l3 = Label(top, text= str(newt[3])+'\n',fg="blue")
                        l3.grid(row=1,column=3)
                        l4 =Label(top,text="Initial Terms:",fg="blue")
                        l4.grid(row=2,column=0)
                        l5=Label(top,text=str(newt[2])+'\n',fg="blue")
                        l5.grid(row=2,column=3)
                        l6 =Label(top,text="Sequence Values:",fg="blue")
                        l6.grid(row=3,column=0)
                        comma=[]
                        sseq=''
                        #for i in range(len(newt[0])-4):
                        #    if newt[0][i+2] == ',' or newt[0][i+2]=='[' or newt[0][i+2]==']':
                        #        comma.append(i)
                        sseq=sseq+str(newt[0][0])+'\n'+str(newt[0][1])+'\n'+str(newt[0][2])+'\n'
                        #l7=Label(top,text=str(newt[0]),fg="blue")
                        l7=Label(top,text=sseq,fg="blue")#,wraplength=160)
                        l7.grid(row=3,column=3)
                        l8 =Label(top,text="Companion Matrix:",fg="blue")
                        l8.grid(row=4,column=0)
                        test=''
                        for i in range(len(newt[1])):
                                       test=test+str(newt[1][i])+'\n'
                        l9=Label(top,text=str(test),fg="blue")
                        l9.grid(row=4,column=3)
                        l10 =Label(top,text="Eigenvalues:",fg="blue")
                        l10.grid(row=5,column=0)
                        l11=Label(top,text=str(newt[4])+'\n',fg="blue")
                        l11.grid(row=5,column=3)
                        la=Label(top,text="GPS Coefficients:",fg="blue")
                        la.grid(row=6,column=0)
                        lb=Label(top,text=str(newt[5])+'\n',fg="blue")
                        lb.grid(row=6,column=3)
                        l12 =Label(top,text="Generalized Power Sum:",fg="blue")
                        l12.grid(row=7,column=0)
                        test2=str(newt[5][0])+'*('+str(newt[4][0])+')^n\n'
                        for i in range(len(newt[5])-1):
                            test2=test2+'+'+str(newt[5][i+1])+'*('+str(newt[4][i+1])+')^n\n'
                        l13=Label(top,text=test2,fg="blue")
                        #l5=Label(top,text=str(newt[5]),fg="blue")
                        l13.grid(row=7,column=3)
                        b1=Button(top, text="Close", fg="red", command=top.destroy)
                        b1.grid(row=8,column=8)
                        #var1=StringVar()
                       # var1.set(str(newt[3]))
                        #return newt   
        g=GPSDialog(root)
        
        
    def EIGS(self):
        print("EIGS")
        class EIGSDialog(tkinter.simpledialog.Dialog):

                def body(self, master):

                        Label(master, text="Initial Terms (No Spaces):").grid(row=0)
                        Label(master, text="Eigenvalues (No Spaces):").grid(row=1)
                        Label(master, text="Number of Terms:").grid(row=2)
                        self.e1 = Entry(master)
                        self.e2 = Entry(master)
                        self.e3 = Entry(master)
                        self.e1.grid(row=0, column=1)
                        self.e2.grid(row=1, column=1)
                        self.e3.grid(row=2, column=1)
                        return self.e1 # initial focus

                def apply(self):
                        co2=[]
                        ei2=[]
                        coeffs2=[]
                        eigs2=[]
                        #coeffs = string.atoi(self.e1.get())
                        #eigs = string.atoi(self.e2.get())
                        coeffs = self.e1.get()
                        eigs = self.e2.get()
                        num = self.e3.get()
                        num = int(num)
                        for i in range(len(coeffs)):
                                if coeffs[i] == ',':
                                        co2.append(i)
                        temp2=''
                        for k in range(co2[0]):
                                temp2=temp2+coeffs[k]
                        coeffs2.append(float(temp2))
                        for i in range(len(co2)-1):
                                temp=''
                                for j in range((co2[i+1]-co2[i]-1)):
                                        temp=temp+coeffs[co2[i]+j+1]
                                coeffs2.append(float(temp))
                        temp3=''
                        for l in range(len(coeffs)-co2[-1]-1):
                                temp3=temp3+coeffs[co2[-1]+1+l]
                        coeffs2.append(float(temp3))

                        #for j in range(len(eigs)):
                        #	ei2=ei2+eigs[j]
                        #co2=list(co2)
                        for i in range(len(eigs)):
                                if eigs[i] == ',':
                                        ei2.append(i)
                        temp2=''
                        for k in range(ei2[0]):
                                temp2=temp2+eigs[k]
                        eigs2.append(float(temp2))
                        for i in range(len(ei2)-1):
                                temp=''
                                for j in range((ei2[i+1]-ei2[i]-1)):
                                        temp=temp+eigs[ei2[i]+j+1]
                                eigs2.append(float(temp))
                        temp3=''
                        for l in range(len(eigs)-ei2[-1]-1):
                                temp3=temp3+eigs[ei2[-1]+1+l]
                        eigs2.append(float(temp3))
                        initial=coeffs2
                        eigs=eigs2
                        print( initial, eigs,'\n')
                        top=Toplevel()
                     #   l1 = Label(top, text="Recurrence Solution")
                       # l1.grid(row=0,column=1)
                        top.title("Recurrence Solution")
                        # or something
                        newt=botheigs(num,eigs,initial)# or something
                        l2 = Label(top, text="Recurrence Coefficients:",fg="blue")
                        l2.grid(row=1,column = 0)
                        l3 = Label(top, text= str(newt[3]),fg="blue")
                        l3.grid(row=1,column=3)
                        l4 =Label(top,text="Initial Terms:",fg="blue")
                        l4.grid(row=2,column=0)
                        l5=Label(top,text=str(newt[2]),fg="blue")
                        l5.grid(row=2,column=3)
                        l6 =Label(top,text="Sequence Values:",fg="blue")
                        l6.grid(row=3,column=0)
                        comma=[]
                        sseq=''
                        #for i in range(len(newt[0])-4):
                        #    if newt[0][i+2] == ',' or newt[0][i+2]=='[' or newt[0][i+2]==']':
                        #        comma.append(i)
                        sseq=sseq+str(newt[0][0])+'\n'+str(newt[0][1])+'\n'+str(newt[0][2])+'\n'
                        #l7=Label(top,text=str(newt[0]),fg="blue")
                        l7=Label(top,text=sseq,fg="blue")#,wraplength=160)
                        l7.grid(row=3,column=3)
                        l8 =Label(top,text="Companion Matrix:",fg="blue")
                        l8.grid(row=4,column=0)
                        test=''
                        for i in range(len(newt[1])):
                                       test=test+str(newt[1][i])+'\n'
                        l9=Label(top,text=str(test),fg="blue")
                        l9.grid(row=4,column=3)
                        l10 =Label(top,text="Eigenvalues:",fg="blue")
                        l10.grid(row=5,column=0)
                        l11=Label(top,text=str(newt[4]),fg="blue")
                        l11.grid(row=5,column=3)
                        la=Label(top,text="GPS Coefficients:",fg="blue")
                        la.grid(row=6,column=0)
                        lb=Label(top,text=str(newt[5]),fg="blue")
                        lb.grid(row=6,column=3)
                        l12 =Label(top,text="Generalized Power Sum:",fg="blue")
                        l12.grid(row=7,column=0)
                        test2=str(newt[5][0])+'*('+str(newt[4][0])+')^n\n'
                        for i in range(len(newt[5])-1):
                            test2=test2+'+'+str(newt[5][i+1])+'*('+str(newt[4][i+1])+')^n\n'
                        l13=Label(top,text=test2,fg="blue")
                        #l5=Label(top,text=str(newt[5]),fg="blue")
                        l13.grid(row=7,column=3)
                        b1=Button(top, text="Close", fg="red",command=top.destroy)
                        b1.grid(row=8,column=8)
                       
        e=EIGSDialog(root)
    def TERMS(self):
        print("TERMS")
        class TERMSDialog(tkinter.simpledialog.Dialog):

                def body(self, master):

                        Label(master, text="Initial Terms (No Spaces):").grid(row=0)
                        Label(master, text="Coefficients (No Spaces):").grid(row=1)
                        Label(master, text="Number of Terms:").grid(row=2)
                        self.e1 = Entry(master)
                        self.e2 = Entry(master)
                        self.e3 = Entry(master)
                        self.e1.grid(row=0, column=1)
                        self.e2.grid(row=1, column=1)
                        self.e3.grid(row=2, column=1)
                        return self.e1 # initial focus

                def apply(self):
                        co2=[]
                        ei2=[]
                        coeffs2=[]
                        eigs2=[]
                        #coeffs = string.atoi(self.e1.get())
                        #eigs = string.atoi(self.e2.get())
                        coeffs = self.e1.get()
                        eigs = self.e2.get()
                        num = self.e3.get()
                        num = int(num)
                        for i in range(len(coeffs)):
                                if coeffs[i] == ',':
                                        co2.append(i)
                        temp2=''
                        for k in range(co2[0]):
                                temp2=temp2+coeffs[k]
                        coeffs2.append(float(temp2))
                        for i in range(len(co2)-1):
                                temp=''
                                for j in range((co2[i+1]-co2[i]-1)):
                                        temp=temp+coeffs[co2[i]+j+1]
                                coeffs2.append(float(temp))
                        temp3=''
                        for l in range(len(coeffs)-co2[-1]-1):
                                temp3=temp3+coeffs[co2[-1]+1+l]
                        coeffs2.append(float(temp3))

                        #for j in range(len(eigs)):
                        #	ei2=ei2+eigs[j]
                        #co2=list(co2)
                        for i in range(len(eigs)):
                                if eigs[i] == ',':
                                        ei2.append(i)
                        temp2=''
                        for k in range(ei2[0]):
                                temp2=temp2+eigs[k]
                        eigs2.append(float(temp2))
                        for i in range(len(ei2)-1):
                                temp=''
                                for j in range((ei2[i+1]-ei2[i]-1)):
                                        temp=temp+eigs[ei2[i]+j+1]
                                eigs2.append(float(temp))
                        temp3=''
                        for l in range(len(eigs)-ei2[-1]-1):
                                temp3=temp3+eigs[ei2[-1]+1+l]
                        eigs2.append(float(temp3))

                        initial=coeffs2
                        coeffs=eigs2
                        print (initial, coeffs,'n')
                        top=Toplevel()
                       # l1 = Label(top, text="Recurrence Solution")
                        #l1.grid(row=0,column=1)
                        top.title("Recurrence Solution")
                        # or something
                        newt=bothways(num,initial,coeffs)# or something
                        l2 = Label(top, text="Recurrence Coefficients:",fg="blue")
                        l2.grid(row=1,column = 0)
                        l3 = Label(top, text= str(newt[3]),fg="blue")
                        l3.grid(row=1,column=3)
                        l4 =Label(top,text="Initial Terms:",fg="blue")
                        l4.grid(row=2,column=0)
                        l5=Label(top,text=str(newt[2]),fg="blue")
                        l5.grid(row=2,column=3)
                        l6 =Label(top,text="Sequence Values:",fg="blue")
                        l6.grid(row=3,column=0)
                        comma=[]
                        sseq=''
                        #for i in range(len(newt[0])-4):
                        #    if newt[0][i+2] == ',' or newt[0][i+2]=='[' or newt[0][i+2]==']':
                        #        comma.append(i)
                        sseq=sseq+str(newt[0][0])+'\n'+str(newt[0][1])+'\n'+str(newt[0][2])+'\n'
                        #l7=Label(top,text=str(newt[0]),fg="blue")
                        l7=Label(top,text=sseq,fg="blue")#,wraplength=160)
                        l7.grid(row=3,column=3)
                        l8 =Label(top,text="Companion Matrix:",fg="blue")
                        l8.grid(row=4,column=0)
                        test=''
                        for i in range(len(newt[1])):
                                       test=test+str(newt[1][i])+'\n'
                        l9=Label(top,text=str(test),fg="blue")
                        l9.grid(row=4,column=3)
                        l10 =Label(top,text="Eigenvalues:",fg="blue")
                        l10.grid(row=5,column=0)
                        l11=Label(top,text=str(newt[4]),fg="blue")
                        l11.grid(row=5,column=3)
                        la=Label(top,text="GPS Coefficients:",fg="blue")
                        la.grid(row=6,column=0)
                        lb=Label(top,text=str(newt[5]),fg="blue")
                        lb.grid(row=6,column=3)
                        
                        l12 =Label(top,text="Generalized Power Sum:",fg="blue")
                        l12.grid(row=7,column=0)
                        test2=str(newt[5][0])+'*('+str(newt[4][0])+')^n\n'
                        for i in range(len(newt[5])-1):
                            test2=test2+'+'+str(newt[5][i+1])+'*('+str(newt[4][i+1])+')^n\n'
                        l13=Label(top,text=test2,fg="blue")
                        #l5=Label(top,text=str(newt[5]),fg="blue")
                        l13.grid(row=7,column=3)
                        b1=Button(top, text="Close",fg="red", command=top.destroy)
                        b1.grid(row=8,column=8)
                       
        t=TERMSDialog(root)
root = Tk()

app = App(root)


root.mainloop()
