#!/usr/bin/env python3
# import ttkbootstrap as ttk
import tkinter as tk
import tkinter.font as font
import time
import datetime




button_ipadx = 0
button_ipady = 0

button_width=10
button_height=1

class PomoTimerApp(tk.Tk):

    def __init__(self,  **kwargs):
        tk.Tk.__init__(self,  **kwargs)
        self.resizable(0,0)


        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.run_timer_flag = tk.BooleanVar()
        self.run_timer_flag.set(False)

        self.overtime_flag = tk.BooleanVar()
        self.overtime_flag.set(False)

        self.timer_flash_flag = tk.IntVar()
        self.timer_flash_flag.set(0)

        self.last_timer_fg = '#000000'


        #default time set for pomo
        self.pomo_hrs = tk.IntVar()
        self.pomo_min = tk.IntVar()
        self.pomo_sec = tk.IntVar()
        self.pomo_hrs.set(0)
        self.pomo_min.set(25)
        self.pomo_sec.set(0)


        #default time set for break
        self.break_hrs = tk.IntVar()
        self.break_min = tk.IntVar()
        self.break_sec = tk.IntVar()
        self.break_hrs.set(0)
        self.break_min.set(5)
        self.break_sec.set(0)


        #current time on timer
        self.hrs_var = tk.IntVar()
        self.min_var = tk.IntVar()
        self.sec_var = tk.IntVar()
        self.hrs_var.set(0)
        self.min_var.set(0)
        self.sec_var.set(0)



        # string for timer display
        self.timer_str_var = tk.StringVar()
        self.timer_str_var.set(self.set_time_str())


        #current time
        self.dt_timer_start = datetime.datetime.now()



        self.title("Pomo")



        self.button_font = font.Font(size=30)
        self.timer_font = font.Font(size=45)

        self.root_cont = tk.Frame()
        self.root_cont.grid(row=0, column=0)
        self.timer_label = tk.Label(self.root_cont, textvariable=self.timer_str_var, fg=self.last_timer_fg)
        self.timer_label.grid(row=0, column=0, columnspan=2, sticky='EW')
        self.timer_label['font']=self.timer_font




        self.pomo_butt = tk.Button(self.root_cont, text='Pomo', command=self.set_pomo, bg='#0052cc', fg='#ffffff', width=button_width, height=button_height)

        self.pomo_butt.grid(row=1, column=0, sticky='NSEW', ipadx=button_ipadx, ipady=button_ipady)
        self.pomo_butt['font']=self.button_font

        self.break_butt = tk.Button(self.root_cont, text='Break', command=self.set_break, bg='#00cc52', fg='#ffffff', width=button_width, height=button_height)
        self.break_butt.grid(row=1, column=1, sticky='NSEW', ipadx=button_ipadx, ipady=button_ipady)
        self.break_butt['font']=self.button_font

        self.sp_butt = tk.Button(self.root_cont, text='Start', command=self.start_timer, bg='#cc5252', fg='#ffffff', width=button_width, height=button_height)
        self.sp_butt.grid(row=2, column=0, columnspan=2, sticky='NSEW', ipadx=button_ipadx, ipady=button_ipady)
        self.sp_butt['font'] = self.button_font

        # self.set_butt =  tk.Button(self.root_cont, text='Settings', command=None, bg='#cccc52', fg='#ffffff', width=button_width, height=button_height)
        # self.set_butt.grid(row=2, column=1, sticky='NSEW', ipadx=button_ipadx, ipady=button_ipady)
        # self.set_butt['font'] = self.button_font
        


        self.set_pomo()
        self.pause_timer()



    def set_pomo(self):
        self.overtime_flag.set(False)
        self.hrs_var.set(self.pomo_hrs.get())
        self.min_var.set(self.pomo_min.get())
        self.sec_var.set(self.pomo_sec.get())
        self.timer_label['fg'] ='#0052cc'
        self.last_timer_fg =self.timer_label['fg']
        self.timer_str_var.set(self.set_time_str())
        # self.start()

    def set_break(self):
        self.overtime_flag.set(False)
        self.hrs_var.set(self.break_hrs.get())
        self.min_var.set(self.break_min.get())
        self.sec_var.set(self.break_sec.get())
        self.timer_label['fg'] ='#00cc52'
        self.last_timer_fg =self.timer_label['fg']
        self.timer_str_var.set(self.set_time_str())


        # self.start()



    def start_timer(self):
        self.timer_flash_flag.set(0)
        self.timer_label['fg'] = self.last_timer_fg

        self.sp_butt['command'] = self.pause_timer
        self.sp_butt['text'] = 'Pause'

        self.pomo_butt['state']='disable'
        self.pomo_butt['bg'] = '#cccccc'
        self.break_butt['state']='disable'
        self.break_butt['bg'] = '#cccccc'

        if not self.overtime_flag.get():
            self.dt_timer_start = datetime.datetime.now() + datetime.timedelta(hours=self.hrs_var.get(), minutes=self.min_var.get(), seconds=self.sec_var.get())
        else:
            self.dt_timer_start = datetime.datetime.now() - datetime.timedelta(hours=self.hrs_var.get(), minutes=self.min_var.get(), seconds=self.sec_var.get())

        self.run_timer_flag.set(True)
        self.update_timer()


    def update_timer(self):
        dt_now = datetime.datetime.now()

        if not self.dt_timer_start > dt_now:
            self.overtime_flag.set(True)


        delta = max(dt_now-self.dt_timer_start, self.dt_timer_start-dt_now)

        m, s = divmod(delta.seconds, 60)
        h, m = divmod(m, 60)
        print(h, m, s)


        self.hrs_var.set(h)
        self.min_var.set(m)
        self.sec_var.set(s)

        self.timer_str_var.set(self.set_time_str())

        if self.run_timer_flag.get():
            self.after(200, self.update_timer)



    def pause_timer(self):
        self.run_timer_flag.set(False)
        self.sp_butt['command'] = self.start_timer
        self.sp_butt['text'] = 'Start'

        self.pomo_butt['state']='normal'
        self.pomo_butt['bg'] = '#0052cc'
        self.break_butt['state']='normal'
        self.break_butt['bg'] = '#00cc52'
        self.timer_flash_flag.set(1)
        self.last_timer_fg =self.timer_label['fg']
        self.flash_timer()



    def set_time_str(self):

        sign ='+' if self.overtime_flag.get() else ''

        if self.hrs_var.get() == 0:
            return f'{sign}{self.min_var.get():02d}:{self.sec_var.get():02d}'
        else:
            return f'{sign}{self.hrs_var.get():02d}:{self.min_var.get():02d}:{self.sec_var.get():02d}'

    def flash_timer(self):
        if self.timer_flash_flag.get()==1:
            self.timer_flash_flag.set(-1)
            self.timer_label['fg'] = self.last_timer_fg
        elif self.timer_flash_flag.get()==-1:
            self.timer_flash_flag.set(1)
            self.timer_label['fg'] = "#999999"

        if abs(self.timer_flash_flag.get())>0:
            self.after(500, self.flash_timer)



if __name__=='__main__':

    app = PomoTimerApp()
    app.mainloop()
























