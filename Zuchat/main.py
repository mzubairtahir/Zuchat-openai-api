import tkinter as tk
import customtkinter
from get import Getclass
import pyperclip


class MainWindow(Getclass):
    geometry_size='1080x680'

    
    def __init__(self) -> None:
        self.root=tk.Tk()

        
        
       

        self.root.geometry(self.geometry_size)
        self.root.resizable(False,False)
        self.root.configure(bg='black')
        self.error_connection_on_screen=False

        
        







    def inserting_result_in_text_box(self,text=None,generated_sucss=False):
        if generated_sucss is True:
            


            self.text_box.configure(state=tk.NORMAL)
            self.text_box.delete(1.0,tk.END)

            self.wait_message.destroy()
            self.text_box.insert('end',text.strip())
            self.text_box.configure(state=tk.DISABLED)
            self.submit_button.configure(state=tk.NORMAL)
        else:
            self.submit_button.configure(state=tk.NORMAL)
            self.wait_message.destroy()

            self.error_connection=customtkinter.CTkLabel(self.root,text='oops! could not connect to server',font=('Courier New',17,'bold'),fg_color='black',text_color='white')
            self.error_connection.place(x=33,y=190)
            self.error_connection_on_screen=True
            self.wait_message.destroy()




    def get_text_from_entrybox(self,entrywidget):
        if self.error_connection_on_screen:
            self.error_connection.destroy()
            self.error_connection_on_screen=False
        
        

        self.input_text=(entrywidget.get()).strip()
        
        entrywidget.delete(0, tk.END)

        


        if len(str(self.input_text))>3:
            self.wait_message= customtkinter.CTkLabel(self.root,text='Please wait\nyour text is being generated...',font=('Courier New',15,'bold'),fg_color='black',text_color='white')
            self.wait_message.place(x=55,y=190)
            self.text_box.delete(0,tk.END)


            self.submit_button.configure(state=tk.DISABLED)
            super().__init__(self.input_text,self.inserting_result_in_text_box)

            self.start_threading()
        else:
            self.wait_message= customtkinter.CTkLabel(self.root,text='prompt should not be empty',font=('Courier New',17,'bold'),fg_color='black',text_color='white')
            self.wait_message.place(x=55,y=190)

            

    
    def othergui(self):
        self.text_box=customtkinter.CTkTextbox(self.root,wrap=tk.WORD,width=630,height=450,font=('arial',18),fg_color='white',border_width=5,text_color='black',corner_radius=10,border_color='cyan',border_spacing=1)
        self.text_box.configure(state=tk.DISABLED)
        self.text_box.place(x=380,y=140)

        entryw=customtkinter.CTkEntry(self.root,height=40,width=300,fg_color='skyblue',font=('arial',20))
        entryw.place(x=303,y=60)


        def xyz():
            self.get_text_from_entrybox(entryw)
        

        self.submit_button=customtkinter.CTkButton(self.root,width=20,text='submit',height=25,font=('arial',18,'bold'),hover_color='indigo',command=xyz)
        self.submit_button.place(y=65,x=623)


        def copygeneratedtext():
            pyperclip.copy(self.generatedtext)
            tk.messagebox.showinfo('copy','text copied to clipboard!')
            
        
        label=customtkinter.CTkLabel(self.root,text='Zuchat',font=('lexend',30,'bold'),text_color='white',corner_radius=15)
        label.place(x=5,y=8)
        

        button=customtkinter.CTkButton(self.root,text='Copy Text',corner_radius=10,font=('arial',20,'bold'),text_color='white',fg_color=("indigo", "yellow"),command=copygeneratedtext)
        button.place(x=100,y=450)




if __name__=='__main__':
    mainwindow=MainWindow()

    mainwindow.othergui()
    mainwindow.root.mainloop()
