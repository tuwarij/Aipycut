import customtkinter
from PIL import Image, ImageDraw, ImageTk

customtkinter.set_appearance_mode("dark")


class Page1(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
    
        frame = customtkinter.CTkFrame(master=self , bg_color="transparent", fg_color="#111111")
        frame.pack(fill="both", expand=True )

        inner1 = customtkinter.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent")      
        inner1.pack(side = "top",fill="both", expand=True )
        
        hidden = customtkinter.CTkLabel(master=inner1, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack( padx=50, side="top", anchor="nw")

        label = customtkinter.CTkLabel(master=inner1, text="Frame Rate & Resize Video", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#4CC9F0"))
        label.pack( padx=50, side="top", anchor="n")
        
        frame2 = customtkinter.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        #Progression bar
        progressbar = customtkinter.CTkProgressBar(frame2, width=600,height= 20,fg_color="#262626",progress_color = "#4CC9F0",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 20,side="top", anchor="n")
        progressbar.set(0.20)
        
        hidden1 = customtkinter.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        #Progession Label bar
        label1 = customtkinter.CTkButton(frame2, width=100,text='Frame Rate',   font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color="white",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = customtkinter.CTkButton(frame2, width=100,text='Upload',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color='#262626',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = customtkinter.CTkButton(frame2, width=100,text='Cut time',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = customtkinter.CTkButton(frame2, width=100,text='Add song',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = customtkinter.CTkButton(frame2, width=100,text='Export',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label1.place(x=5,y=50)
        label2.place(x=135,y=60)
        label3.place(x=250,y=60)
        label4.place(x=370,y=60)
        label5.place(x=495,y=60)
        
        infoText = customtkinter.CTkLabel(master=inner1, text="เลือก Frame rate และ Size video ตามต้องการ", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.27, rely = 0.22, anchor="n")

        label2 = customtkinter.CTkFrame(master=inner1, bg_color="transparent", fg_color="#181818", corner_radius = 5,border_width=1,border_color="#474747")
        label2.pack(pady=50 ,padx=250, side="top",fill="both", expand=True ,anchor="nw")

        hidden1 = customtkinter.CTkLabel(master=label2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( padx=50, side="top", anchor="n")
        
        selectF = customtkinter.CTkLabel(master=label2, text="Select a frame rate          ", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#ffffff"))
        selectF.pack(padx=50, side="top",anchor="n")

        frameratelist = ["option 1", "option 2"]
        combobox = customtkinter.CTkComboBox(label2, values=frameratelist,height=50,width=200,font=("Tahoma", 15),fg_color="#262626", corner_radius = 3,border_width=0,button_color="#262626",button_hover_color="#2C748A",dropdown_hover_color="#2C748A",justify="center")
        combobox.pack(padx=50, side="top",anchor="n")
        
        hidden2 = customtkinter.CTkLabel(master=label2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden2.pack( padx=50, side="top", anchor="n")

        selectS = customtkinter.CTkLabel(master=label2, text="Select a size video          ", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#ffffff"))
        selectS.pack(padx=50, side="top",anchor="n")

        sizevideolist = ["option 1", "option 2"]
        combobox2 = customtkinter.CTkComboBox(label2, values=sizevideolist,height=50,width=200,font=("Tahoma", 15),fg_color="#262626", corner_radius = 3,border_width=0,button_color="#262626",button_hover_color="#2C748A",dropdown_hover_color="#2C748A",justify="center")
        combobox2.pack(padx=50, side="top",anchor="n")

        #next button
        button = customtkinter.CTkButton(master=self, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,border_width=1,border_color="#4CC9F0",fg_color="#262626",hover_color="#4CC9F0",command=lambda: controller.show_frame("Page2"))
        button.place(x=1080,y=640)

        # #picture
        # image_path = "filmroll.png" 
        # image = Image.open(image_path)
        # image = image.resize((600, 300))  
        # image_tk = ImageTk.PhotoImage(image)
        # label_with_image = customtkinter.CTkFrame(label2, image=image_tk, text="") 
        # label_with_image.place(x=50,y=50)
        