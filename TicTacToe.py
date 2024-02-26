from tkinter import *
import threading
class Game:	
	def __init__(self,master):
		self.root=master
		self.root.title('Tik_Tac_Toe')
		self.p1_sign_var=IntVar()
		self.p2_sign_var=IntVar()
		self.selection_error_var=StringVar()
		self.p1_name_var=StringVar()
		self.p2_name_var=StringVar()
		self.r1_c1_var=StringVar()
		self.r1_c2_var=StringVar()
		self.r1_c3_var=StringVar()
		self.r2_c1_var=StringVar()
		self.r2_c2_var=StringVar()
		self.r2_c3_var=StringVar()
		self.r3_c1_var=StringVar()
		self.r3_c2_var=StringVar()
		self.r3_c3_var=StringVar()	
		self.back_to_players=0
		self.new_game=0
		self.selection_done='no'		
		self.Start()
	
	def Start(self):
		self.image1_canvas=Canvas(self.root,width=1200,height=800)
		welcome_label=Label(self.image1_canvas,text='_ _ _ _ _ _ _ _Welcome  To  Tic  Tec  Toe  Game_ _ _ _ _ _ _ _',width=59,height=2,bg='#24444a',fg='red',bd=10,relief=GROOVE,font=('helvetica',25,'bold italic')).place(x=0,y=2)
		if self.selection_done=='yes':
			self.continue_btn=Button(self.image1_canvas,text='Continue...',width=10,height=1,bg='#24444a',bd=12,font=('helvetica', 17, 'bold italic'),command=self.Names_Signs_Selection).place(x=493,y=240)	
		play_btn=Button(self.image1_canvas,text='New',width=10,height=1,bg='#24444a',bd=12,font=('helvetica', 17, 'bold italic'),command=lambda:self.Names_Signs_Selection('yes')).place(x=493,y=340)
		exit_root_btn=Button(self.image1_canvas,text='Exit',width=10,height=1,bg='#24444a',bd=12,font=('helvetica', 17, 'bold italic'),command=self.Exit).place(x=493,y=450)
		self.image1_canvas.pack()	
		self.photo1=PhotoImage(file='Image1.gif',format='gif -index '+str(0))
		self.image1_canvas_img=self.image1_canvas.create_image(0,0,image=self.photo1,anchor=NW)
		self.image1_canvas.image=self.photo1	
	
	def Names_Signs_Selection(self,new=''):
		if self.back_to_players==0:	
			self.image1_canvas.delete(self.image1_canvas_img)
			self.frame_on_image1_canvas=Frame(self.image1_canvas,width=1200,height=800,bg='white')
			self.frame_on_image1_canvas.pack()
		if new=='yes':
			self.p1_sign_var.set(0)
			self.p2_sign_var.set(0)
			self.p1_name_var.set('')
			self.p2_name_var.set('')
			self.selection_done=='yes'	
		self.image2_canvas=Canvas(self.frame_on_image1_canvas,width=1200,height=800)
		self.photo2=PhotoImage(file='Image2.gif',format='gif')
		self.image2_canvas_img=self.image2_canvas.create_image(0,0,image=self.photo2,anchor=NW)
		self.image2_canvas.pack()
		self.Players()
	
	def Players(self):	
		p1_label=Label(self.image2_canvas,text='Player 1',bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=308,y=160)
		p1_frame=Frame(self.image2_canvas,width=200,height=200,bg='#337AFF',bd=15,relief=GROOVE)
		p1_name_label=Label(p1_frame,text='Enter Your Name',width=14,bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=13,y=5)
		p1_name=Entry(p1_frame,textvariable=self.p1_name_var,bg='#FF6833',bd=5,relief=RAISED,font=('helvetica',10,'bold italic'))
		p1_name.place(x=13,y=45)
		p1_sign_label=Label(p1_frame,text='Choose Sign',width=14,bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=13,y=78)
		p1_r1=Radiobutton(p1_frame,text='X',value=1,bg='#FF6833',variable=self.p1_sign_var,width=2,bd=5,relief=GROOVE,font=('helvetica',10,'bold')).place(x=21,y=125)
		p1_r2=Radiobutton(p1_frame,text='#',value=2,bg='#FF6833',variable=self.p1_sign_var,width=2,bd=5,relief=GROOVE,font=('helvetica',10,'bold')).place(x=85,y=125)
		p1_frame.place(x=240,y=200)
		versus_lbl=Label(self.image2_canvas,text='V/S',fg='white',bg='black',bd=10,relief=GROOVE,font=('helvetica',16,'bold italic'),width=4).place(x=567,y=290)
		p2_label=Label(self.image2_canvas,text='Player 2',bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=837,y=160)
		p2_frame=Frame(self.image2_canvas,width=200,height=200,bg='#337AFF',bd=15,relief=GROOVE)
		p2_name_label=Label(p2_frame,text='Enter Your Name',width=14,bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=13,y=5)
		p2_name=Entry(p2_frame,textvariable=self.p2_name_var,bg='#FF6833',bd=5,relief=RAISED,font=('helvetica',10,'bold italic'))
		p2_name.place(x=13,y=45)
		p2_sign_label=Label(p2_frame,text='Choose Sign',width=14,bg='#FF6833',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=13,y=78)
		p2_r1=Radiobutton(p2_frame,text='O',value=3,bg='#FF6833',width=2,variable=self.p2_sign_var,bd=5,relief=GROOVE,font=('helvetica',10,'bold')).place(x=21,y=125)
		p2_r2=Radiobutton(p2_frame,text='@',value=4,bg='#FF6833',width=2,variable=self.p2_sign_var,bd=5,relief=GROOVE,font=('helvetica',10,'bold')).place(x=85,y=125)
		p2_frame.place(x=770,y=200)
		ok_btn=Button(self.image2_canvas,text='Ok',width=20,bd=12,font=('helvetica', 10, 'bold italic'),command=self.Names_Signs_Checking,bg='#22dd19').place(x=505,y=450)
		back_wlcm_btn=Button(self.image2_canvas,text='Back',width=20,bd=12,font=('helvetica', 10, 'bold italic'),command=self.Back_To_Welcome_Window,bg='#22dd19').place(x=505,y=550)
	
	def Names_Signs_Checking(self):
		if self.p1_sign_var.get()!=0 and self.p2_sign_var.get()!=0 and self.p1_name_var.get()!='' and self.p2_name_var.get()!='':
			self.Game_Structure()
		elif self.p1_sign_var.get()==0 and self.p2_sign_var.get()==0 and self.p1_name_var.get()=='' and self.p2_name_var.get()=='':
			self.Show_Selection_Error()
			self.selection_error_var.set('Enter Name and Choose Sign')
		elif self.p1_sign_var.get()==0 and self.p1_name_var.get()=='' or self.p2_sign_var.get()==0 and self.p2_name_var.get()=='' or self.p1_sign_var.get()==0 and self.p2_name_var.get()=='' or self.p2_sign_var.get()==0 and self.p1_name_var.get()=='':
			self.Show_Selection_Error()
			self.selection_error_var.set('Enter Name and Choose Sign')		
		elif self.p1_name_var.get()=='' and self.p2_name_var.get()==''or self.p1_name_var.get()=='' and self.p2_name_var.get()!='' or self.p1_name_var.get()!='' and self.p2_name_var.get()=='':			
			self.Show_Selection_Error()
			self.selection_error_var.set('Enter Name')
		else:
			self.Show_Selection_Error()
			self.selection_error_var.set('Choose Sign')
	
	def Game_Structure(self):
		if self.new_game==0:
			self.image2_canvas.destroy()
			self.image3_canvas=Canvas(self.frame_on_image1_canvas,width=1200,height=800)
			self.image3_canvas.pack()
			self.photo3=PhotoImage(file='Image3.gif',format='gif -index 0')
			self.image3_canvas_img=self.image3_canvas.create_image(0,0,image=self.photo3,anchor=NW)
		self.game_frame=Frame(self.image3_canvas,width=280,height=245,bg='#FFE933',bd=15,relief=GROOVE)
		self.game_frame.place(x=450,y=200)
		self.l1=Label(self.game_frame,width=6,height=2,textvariable=self.r1_c1_var)
		self.l1.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r1_c1_var))
		self.l1.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r1_c1_var))
		self.l1.place(x=50,y=50)
		self.l2=Label(self.game_frame,width=6,height=2,textvariable=self.r1_c2_var)
		self.l2.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r1_c2_var))
		self.l2.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r1_c2_var))
		self.l2.place(x=101,y=50)
		self.l3=Label(self.game_frame,width=6,height=2,textvariable=self.r1_c3_var)	
		self.l3.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r1_c3_var))
		self.l3.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r1_c3_var))
		self.l3.place(x=152,y=50)
		self.l4=Label(self.game_frame,width=6,height=2,textvariable=self.r2_c1_var)
		self.l4.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r2_c1_var))
		self.l4.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r2_c1_var))
		self.l4.place(x=50,y=90)
		self.l5=Label(self.game_frame,width=6,height=2,textvariable=self.r2_c2_var)
		self.l5.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r2_c2_var))
		self.l5.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r2_c2_var))
		self.l5.place(x=101,y=90)
		self.l6=Label(self.game_frame,width=6,height=2,textvariable=self.r2_c3_var)
		self.l6.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r2_c3_var))
		self.l6.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r2_c3_var))
		self.l6.place(x=152,y=90)
		self.l7=Label(self.game_frame,width=6,height=2,textvariable=self.r3_c1_var)
		self.l7.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r3_c1_var))
		self.l7.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r3_c1_var))
		self.l7.place(x=50,y=130)
		self.l8=Label(self.game_frame,width=6,height=2,textvariable=self.r3_c2_var)
		self.l8.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r3_c2_var))
		self.l8.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r3_c2_var))
		self.l8.place(x=101,y=130)
		self.l9=Label(self.game_frame,width=6,height=2,textvariable=self.r3_c3_var)
		self.l9.bind('<Button-1>',lambda event:self.Mouse_Left_Button(self.r3_c3_var))
		self.l9.bind('<Button-3>',lambda event:self.Mouse_Right_Button(self.r3_c3_var))
		self.l9.place(x=152,y=130)
		self.b_back_to_players=Button(self.image3_canvas,text='Back',width=12,bg='#22dd19',bd=12,font=('helvetica', 10, 'bold italic'),command=self.Back_To_Players_Selection_Window)
		self.b_back_to_players.place(x=526,y=500)					
	
	def Mouse_Left_Button(self,l):
		if self.p1_sign_var.get()==1:
			l.set('X')
		else:
			l.set('#')
		self.Labels_Matching(l)
		self.No_Winner()		
	
	def Mouse_Right_Button(self,l):
		if self.p2_sign_var.get()==3:
			l.set('O')
		else:
			l.set('@')
		self.Labels_Matching(l)
		self.No_Winner()	
	
	def Labels_Matching(self,l):
		if l==self.r1_c1_var:
			if l.get()==self.r1_c2_var.get() and l.get()==self.r1_c3_var.get():
				self.Make_Labels_Red(self.l1,self.l2,self.l3)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l1,self.l5,self.l9)
				self.Winner(l)
			if l.get()==self.r2_c1_var.get() and l.get()==self.r3_c1_var.get():
				self.Make_Labels_Red(self.l1,self.l4,self.l7)
				self.Winner(l)
		elif l==self.r1_c2_var:
			if l.get()==self.r1_c1_var.get() and l.get()==self.r1_c3_var.get():
				self.Make_Labels_Red(self.l2,self.l1,self.l3)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r3_c2_var.get():
				self.Make_Labels_Red(self.l2,self.l5,self.l8)
				self.Winner(l)	
		elif l==self.r1_c3_var:
			if l.get()==self.r1_c2_var.get() and l.get()==self.r1_c1_var.get():
				self.Make_Labels_Red(self.l3,self.l2,self.l1)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r3_c1_var.get():
				self.Make_Labels_Red(self.l3,self.l5,self.l7)
				self.Winner(l)
			if l.get()==self.r2_c3_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l3,self.l6,self.l9)
				self.Winner(l)	
		elif l==self.r2_c1_var:
			if l.get()==self.r1_c1_var.get() and l.get()==self.r3_c1_var.get():
				self.Make_Labels_Red(self.l4,self.l1,self.l7)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r2_c3_var.get():
				self.Make_Labels_Red(self.l4,self.l5,self.l6)
				self.Winner(l)				
		elif l==self.r2_c2_var:
			if l.get()==self.r1_c2_var.get() and l.get()==self.r3_c2_var.get():
				self.Make_Labels_Red(self.l5,self.l2,self.l8)
				self.Winner(l)
			if l.get()==self.r2_c1_var.get() and l.get()==self.r2_c3_var.get():
				self.Make_Labels_Red(self.l5,self.l4,self.l6)
				self.Winner(l)				
			if l.get()==self.r1_c1_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l5,self.l1,self.l9)
				self.Winner(l)
			if l.get()==self.r1_c3_var.get() and l.get()==self.r3_c1_var.get():
				self.Make_Labels_Red(self.l5,self.l3,self.l7)
				self.Winner(l)			
		elif l==self.r2_c3_var:
			if l.get()==self.r1_c3_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l6,self.l3,self.l9)
				self.Winner(l)				
			if l.get()==self.r2_c2_var.get() and l.get()==self.r2_c1_var.get():
				self.Make_Labels_Red(self.l6,self.l5,self.l4)
				self.Winner(l)		
		elif l==self.r3_c1_var:
			if l.get()==self.r2_c1_var.get() and l.get()==self.r1_c1_var.get():
				self.Make_Labels_Red(self.l7,self.l4,self.l1)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r1_c3_var.get():
				self.Make_Labels_Red(self.l7,self.l5,self.l3)
				self.Winner(l)				
			if l.get()==self.r3_c2_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l7,self.l8,self.l9)
				self.Winner(l)	
		elif l==self.r3_c2_var:
			if l.get()==self.r2_c2_var.get() and l.get()==self.r1_c2_var.get():
				self.Make_Labels_Red(self.l8,self.l5,self.l2)
				self.Winner(l)
			if l.get()==self.r3_c1_var.get() and l.get()==self.r3_c3_var.get():
				self.Make_Labels_Red(self.l8,self.l7,self.l9)
				self.Winner(l)	
		elif l==self.r3_c3_var:
			if l.get()==self.r2_c3_var.get() and l.get()==self.r1_c3_var.get():
				self.Make_Labels_Red(self.l9,self.l6,self.l3)
				self.Winner(l)	
			if l.get()==self.r2_c2_var.get() and l.get()==self.r1_c1_var.get():
				self.Make_Labels_Red(self.l9,self.l5,self.l1)
				self.Winner(l)
			if l.get()==self.r3_c2_var.get() and l.get()==self.r3_c1_var.get():
				self.Make_Labels_Red(self.l9,self.l8,self.l7)
				self.Winner(l)
		elif self.r1_c1_var.get()!='' and self.r1_c2_var.get()!='' and self.r1_c3_var.get()!='' and self.r2_c1_var.get()!='' and self.r2_c2_var.get()!='' and self.r2_c3_var.get()!='' and self.r3_c1_var.get()!='' and self.r3_c2_var.get()!='' and self.r3_c3_var.get()!='':		
			self.No_Winner()
	
	def Winner(self,box):
		timer = threading.Timer(0.3,self.Winner_Selection,[box])
		timer.start()			
	
	def No_Winner(self):
		if self.r1_c1_var.get()!='' and self.r1_c2_var.get()!='' and self.r1_c3_var.get()!='' and self.r2_c1_var.get()!='' and self.r2_c2_var.get()!='' and self.r2_c3_var.get()!='' and self.r3_c1_var.get()!='' and self.r3_c2_var.get()!='' and self.r3_c3_var.get()!='':		
			timer = threading.Timer(0.3,self.Winner_Selection,['no_Winner'])
			timer.start()
	
	def Winner_Selection(self,box):
		self.game_frame.destroy()
		self.b_back_to_players.destroy()	
		self.canvas=Canvas(self.image3_canvas,width=350,height=280,bg='black',bd=15,relief=GROOVE)
		self.canvas.place(x=400,y=165)
		self.photo4=PhotoImage(file='Image4.gif')
		self.canvas_image13=self.canvas.create_image(0,0,image=self.photo4,anchor=NW)
		if box=='no_Winner':
			self.Winner_label=Label(self.canvas,text='No One is Winner',bg='#ff00bf',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=10,y=10)
		elif box.get()=='X' or box.get()=='#':
			self.Winner_label=Label(self.canvas,text=self.p1_name_var.get()+' is Winner',bg='#ff00bf',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=10,y=10)
		elif box.get()=='O' or box.get()=='@':
			self.Winner_label=Label(self.canvas,text=self.p2_name_var.get()+' is Winner',bg='#ff00bf',bd=10,relief=GROOVE,font=('helvetica',10,'bold italic')).place(x=10,y=10)	
		self.b_new_game=Button(self.image3_canvas,text='New Game',bg='#22dd19',bd=12,font=('helvetica', 10, 'bold italic'),command=self.New_Game_Structure)
		self.b_new_game.place(x=480,y=540)	 
		self.b_exit=Button(self.image3_canvas,text='Exit',bg='#22dd19',bd=12,font=('helvetica', 10, 'bold italic'),command=self.Exit)
		self.b_exit.place(x=630,y=540)
	
	def Back_To_Welcome_Window(self):
		if self.p1_sign_var.get()!=0 or self.p2_sign_var.get()!=0 or self.p1_name_var.get()!='' or self.p2_name_var.get()!='':
			self.selection_done='yes'
		else:
			self.selection_done='no'	
		self.image1_canvas.destroy()
		self.back_to_players=0
		self.Start()
	
	def Back_To_Players_Selection_Window(self):
		if self.new_game==1:
			self.new_game=0
		self.back_to_players=1
		self.selection_error_var.set('')
		self.image3_canvas.destroy()
		self.Names_Signs_Selection()
	
	def New_Game_Structure(self):
		self.new_game=1
		self.canvas.destroy()
		self.b_new_game.destroy()
		self.b_exit.destroy()
		self.Set_Lbls_Var_Empty()
		self.Game_Structure()
	
	def Set_Lbls_Var_Empty(self):
		self.r1_c1_var.set('')
		self.r1_c2_var.set('')
		self.r1_c3_var.set('')
		self.r2_c1_var.set('')
		self.r2_c2_var.set('')
		self.r2_c3_var.set('')
		self.r3_c1_var.set('')
		self.r3_c2_var.set('')
		self.r3_c3_var.set('')
	
	def Make_Labels_Red(self,l1,l2,l3):
		l1.configure(bg='red')
		l2.configure(bg='red')
		l3.configure(bg='red')			
	
	def Show_Selection_Error(self):
		selection_error_name=Label(self.image2_canvas,textvariable=self.selection_error_var,bg='black',fg='white',relief=GROOVE,bd=10,font=('helvetica', 13, 'bold italic')).place(x=487,y=30)		
	
	def Exit(self):
		self.root.destroy()	
App=Tk()
App.geometry('1200x800')
App.config(bg='black')
Game(App)			
App.mainloop()