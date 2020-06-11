from tkinter import *
from tkinter import filedialog
import io

def vistaPrevia():
    archivo=open(ruta.cget("text"), "r")
    vistaArchivo.config(state=NORMAL)
    vistaArchivo.delete('1.0', END)
    for linea in archivo:
        datos=""
        if(("lw" in linea) or ("sw" in linea)):
            linea=linea.replace(' ', '')
            linea=linea.replace('#', ',')
            linea=linea.replace('$', ',')
            linea=linea.replace('(', '')
            linea=linea.replace(')', '')
            numeros=linea.split(',')
            numeros.pop(0)
        else:
            linea=linea.replace(',', '')
            linea=linea.replace('#', ',')
            linea=linea.replace('$', ',')
            numeros=linea.split(',')
            numeros.pop(0)
        #addi
        if("addi" in linea):
            linea=linea.replace('addi', '')
            datos+="001000"
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioI(int(numeros[2]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #add
        if("add" in linea):
            linea=linea.replace('add', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx100000\n"
            vistaArchivo.insert(INSERT, datos)
        #resta
        if("sub" in linea):
            linea=linea.replace('sub', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx100010\n"
            vistaArchivo.insert(INSERT, datos)
        #multiplicacion
        if("mul" in linea):
            linea=linea.replace('mul', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx011000\n"
            vistaArchivo.insert(INSERT, datos)
        #division
        if("div" in linea):
            linea=linea.replace('div', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx011010\n"
            vistaArchivo.insert(INSERT, datos)
        #andi
        if("andi" in linea):
            linea=linea.replace('andi', '')
            datos+="001100"
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioI(int(numeros[2]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #and
        if("and" in linea):
            linea=linea.replace('and', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx100100\n"
            vistaArchivo.insert(INSERT, datos)
        #ori
        if("ori" in linea):
            linea=linea.replace('ori', '')
            datos+="001101"
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioI(int(numeros[2]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #or
        if("or" in linea):
            linea=linea.replace('or', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx100101\n"
            vistaArchivo.insert(INSERT, datos)
        #xor
        if("xor" in linea):
            linea=linea.replace('xor', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx100110\n"
            vistaArchivo.insert(INSERT, datos)
        #slti
        if("slti" in linea):
            linea=linea.replace('slti', '')
            datos+="001010"
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioI(int(numeros[2]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #slt
        if("slt" in linea):
            linea=linea.replace('slt', '')
            datos+="000000"
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+="xxxxx101010\n"
            vistaArchivo.insert(INSERT, datos)
        #beq
        if("beq" in linea):
            linea=linea.replace('beq', '')
            datos+="000100"
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioR(int(numeros[1]))
            datos+=convertirBinarioI(int(numeros[2]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #jump
        if("j" in linea):
            linea=linea.replace('j', '')
            datos+="000010"
            datos+=convertirBinarioJ(int(numeros[0]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #sw
        if("sw" in linea):
            linea=linea.replace('sw', '')
            datos+="101011"
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioI(int(numeros[1]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        #lw
        if("lw" in linea):
            linea=linea.replace('lw', '')
            datos+="100011"
            datos+=convertirBinarioR(int(numeros[2]))
            datos+=convertirBinarioR(int(numeros[0]))
            datos+=convertirBinarioI(int(numeros[1]))
            datos+="\n"
            vistaArchivo.insert(INSERT, datos)
        if("nop" in linea):
             datos+="00000000000000000000000000000000\n"
             vistaArchivo.insert(INSERT, datos) 
    archivo.close()
    vistaArchivo.config(state=DISABLED)

def devolverRuta():
    direccion=filedialog.askopenfilename(initialdir="",
                                        title="Selecciona un archivo asm",
                                         filetypes=(("Texto", "*.txt"),
                                                    ("Todos", "*.*")))
    if(direccion=="" and ruta.cget("text")=="Ruta del archivo"):
        ruta.config(text="Ruta del archivo")
    elif(direccion!=""):
        ruta.config(text=direccion)
        vistaPrevia()
    

def convertirArchivo():
    archivoBinario=open("instruccionesBinarias.txt", "w")
    texto=vistaArchivo.get('1.0', END).splitlines()
    contador=0
    for line in texto:
        entero=0
        for i in line:
            if(contador==8):
                contador=0
                archivoBinario.write("\n")
            contador+=1
            archivoBinario.write(line[entero])
            entero+=1
    vistaArchivo.config(state=NORMAL)
    vistaArchivo.delete('1.0', END)
    vistaArchivo.insert(INSERT, 'Tu archivo se creo con exito\n')
    vistaArchivo.config(state=DISABLED)
    archivoBinario.close()
    

def convertirBinarioR(num):
    if(num>31):
        print("Tu numero excede el limite\n")
        return '11111'
    elif(num==0):
        return '00000'
    binario=''
    while num-1 != 0:
        if(num%2 ==0):
            binario+='0'
            num=num/2
        else:
            binario+='1'
            num=int(num/2)
    binario+='1'
    while(len(binario)<5):
        binario+='0'
    return binario[::-1]

def convertirBinarioI(num):
    if(num>65535):
        print("Tu numero excede el limite\n")
        return '1111111111111111'
    elif(num==0):
        return '0000000000000000'
    binario=''
    while num-1 != 0:
        if(num%2 ==0):
            binario+='0'
            num=num/2
        else:
            binario+='1'
            num=int(num/2)
    binario+='1'
    while(len(binario)<16):
        binario+='0'
    return binario[::-1]

def convertirBinarioJ(num):
    if(num==0):
        return '00000000000000000000000000'
    binario=''
    while num-1 != 0:
        if(num%2 ==0):
            binario+='0'
            num=num/2
        else:
            binario+='1'
            num=int(num/2)
    binario+='1'
    while(len(binario)<26):
        binario+='0'
    return binario[::-1]

ventana=Tk()
ventana.title("Decodificador")
ventana.resizable(False, False)

frame=Frame(ventana)
frame.pack()

titulo=Label(frame, text="Busca el archivo para convertir", width="45")
titulo.grid(row=0, column=0, columnspan=3)
titulo.config(fg="blue", font="12")
titulo.config(padx=10, pady=10)

selector=Button(frame, text="Buscar archivo", command=devolverRuta, width="15")
selector.grid(row=1,column=0, sticky="ne")
selector.config(activeforeground="blue", bd="5")

ruta=Label(frame, text="Ruta del archivo", width="37")
ruta.grid(row=1, column=1, columnspan=2, sticky="w")
ruta.config(bg="lightgrey", fg="blue")

aplicar=Button(frame, text="Exportar", command=convertirArchivo, width="15")
aplicar.grid(row=2, column=0, sticky="ne")
aplicar.config(activeforeground="red", bd="5")

vistaArchivo=Text(frame, width="35", height="10")
vistaArchivo.grid(row=2, column=1)
vistaArchivo.config(bg="lightgrey")

scroll=Scrollbar(frame, command=vistaArchivo.yview)
scroll.grid(row=2, column=2, sticky="nsew")

vistaArchivo.config(yscrollcommand=scroll.set)

ventana.mainloop()
