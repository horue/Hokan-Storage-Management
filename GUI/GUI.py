import customtkinter as ct
from CTkMenuBar import *
from  CustomTkinterMessagebox  import  *
from customtkinter import filedialog
from CTkSpinbox import *

def get_command(value):
    print("segmented button clicked:", value)
    o1.set("")

def show_image(new_image):
    ph = ct.CTkImage(light_image=new_image, dark_image=new_image, size=(744/2, 1039/2))
    i1.configure(image=ph)


def bar1(fm):
    #f0=ct.CTkFrame(fm, width=99, height=20)
    #f0.grid(row=0, padx=0, pady=(0,30), sticky='ew', columnspan=True)

    global o1
    o1 = ct.CTkSegmentedButton(fm, values=["", "Adicionar novo cliente", "Adicionar vendedor"],corner_radius=50,fg_color='#dbdbdb', selected_color='#dbdbdb',unselected_color='#dbdbdb', text_color='black',selected_hover_color='#c0c0c0',command=get_command)
    o1.set("")
    selected_value = o1.get()
    o1.delete(selected_value)
    o1.grid(row=2, column=0, pady=10, padx=10)

def novo_produto(f2):
    for widget in f2.winfo_children():
        widget.destroy()

    l1 = ct.CTkLabel(f2, text='Nome do Produto')
    l1.pack(pady=10)

    e1 = ct.CTkEntry(f2)
    e1.pack()

    l2 =ct.CTkLabel(f2, text='Quantidade do Produto')
    l2.pack(pady=10)

    global s1
    s1 = ct.IntVar()
    s1 = CTkSpinbox(f2,
          start_value = 1,
          min_value = 1,
          max_value = 99,
          scroll_value = 1,
          variable = s1)
    s1.pack()


def frame1(f1):
    b1 = ct.CTkButton(f1, text='Nova Venda')
    b1.pack(pady=10)

    b4 = ct.CTkButton(f1, text='Adicionar Produto', command=lambda:novo_produto(f2))
    b4.pack(pady=10)
    
    b2 = ct.CTkButton(f1, text='Verificar Vendas')
    b2.pack(pady=10)

    b3 = ct.CTkButton(f1, text='Consultar Estoque')
    b3.pack(pady=10)


def frame2(f2):
    global i1
    i1 = ct.CTkLabel(f2, text='')
    i1.pack(pady=15)





def initial(root):
    fh=ct.CTkFrame(root)
    fh.pack(fill='x', anchor='n')

    fm=ct.CTkFrame(root, height=20, fg_color='#ffffff')
    fm.pack(fill='both', expand=True, anchor='s')
    
    bar1(fh)

    f1=ct.CTkScrollableFrame(fm, width=400, height=620, label_text='Menu de Opções')
    f1.grid(column=0, row=1, padx=30, pady=(30,0))

    frame1(f1)

    global f2
    f2=ct.CTkScrollableFrame(fm, width=950, height=620, label_text='Menu')
    f2.grid(column=1, row=1, padx=30, pady=(30,0))

    frame2(f2)


def main_screen():
    root = ct.CTk()
    root.geometry("400x500")
    root.title("Hokan - Gerenciador de Vendas")
    root.rowconfigure(index=3)
    root.columnconfigure((0, 1, 2), weight=0)
    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main_screen()