import os


def add_new(filename:str):
    last_name = input("Введите фамилию :")
    first_name = input("Введите имя :")
    patrinimyc_name = input("Введите отчество :")
    phone_number = input ("Введите номер телефона :")
    with open (filename, 'a', encoding="utf-8") as fd :
        fd.write (f'{last_name}, {first_name}, {patrinimyc_name}, {phone_number}\n')

def show_all(filename : str):
    with open(filename , 'r', encoding ="utf-8") as fd:
        data = fd.read()
        print (data)

def remove_1(filename :str):
    last_name = input ("Введите фамилию :")
    first_name = input ("Введите имя :")
    patrinimyc_name = input ("Введите отчество :")
    phone_number = input ("Введите номер телефона :")
    with open(filename, 'r', encoding ="utf-8") as f :
        data = f.readlines()
        s=f'{last_name}, {first_name}, {patrinimyc_name}, {phone_number}\n'
        data.remove(s)
    with open (filename,'w', encoding ="utf-8") as f :
        f.writelines(data)

def correct_1(filename :str):
    old_data = find_by_attribute(filename, True)
    print ("Введите новые данные :")
    last_name_ = input ("Введите фамилию :")
    first_name_ = input ("Введите имя :")
    patrinimyc_name_ = input ("Введите отчество :")
    phone_number_ = input ("Введите номер телефона :")
    with open(filename, 'r', encoding ="utf-8") as f :
        data = f.readlines()
        s = data.index (old_data)
        data[s] = f'{last_name_}, {first_name_}, {patrinimyc_name_}, {phone_number_}\n'
    with open (filename,'w', encoding ="utf-8") as f :
        f.writelines(data)

def copy_string (filename :str , filename2: str):
    number_string = int ( input("Ввведите номер строки , который необходимо перенести из дополнительного справочника\n"))
    data =[]
    with open (filename2, 'r', encoding ='utf-8') as f :
        data = list(f.readlines())
        if number_string > len(data):
            print ("В дополнительном справочнике нет такой строки")
            return
        else:
            copy_str = data[number_string-1]
            data.remove(copy_str) 
    with open (filename2, 'w', encoding ='utf-8') as f :  
        f.writelines(data)
            
    with open (filename,'a', encoding ='utf-8') as fd:
        fd.write (copy_str)

def main():
    os.system ("cls")
    Flag_Exit = False
    while Flag_Exit==False:
        print ( "1 Добавление новой записи")
        print ( "2 Вывести все записи")
        print ( "3 Удалить запись")
        print ( "4 Изменить запись")
        print ( "5 Поиск по имени\фамилии")
        print ( "6 Скопировать из одного файла в другой")
        a = input("Введите операцию или x для выхода :")  
        if a == "1" :
            choice = input ("Введите 1 для добавления в основной справочник, 2 для добавления в дополнительный\n")
            if choice == '1': add_new("Phone_Number.txt")
            elif choice == '2': add_new("Phone_Number2.txt")
        elif a == "2" :
            choice = input ("Введите 1 для демонстрации основного справочника, 2 дополнительного\n")
            if choice == '1' : show_all("Phone_Number.txt")
            elif choice == '2' : show_all ("Phone_Number2.txt")
        elif a == "3" : remove_1("Phone_Number.txt")
        elif a == "4" : correct_1("Phone_Number.txt")
        elif a == "5" : find_by_attribute("Phone_Number.txt", False)
        elif a == "6" : copy_string("Phone_Number.txt", "Phone_Number2.txt")
        elif a =="x" : Flag_Exit=True

def find_by_attribute (filename :str, option:bool ):
    op=0
    c=input ("Введите 1 для поиска по фамилии или 2 для поиска по имени :\n")
    print ("")
    if c=='1' :op=0
    elif c=='2' : op=1
    attr = input("Введите имя\фамилию для поиска\n ")
    print ("")
    with open(filename, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[op]== attr,data))
        result = (list(zip (range(1,len(data)+1),data)))
        if result == [] : 
            print ("                  Такой записи нет в справочнике")
            print (" ")
            return  
        else :
            a = str(result).split ("), (")
            print ('\n'.join(map(str, a)))
            
        if option:
            id=int ( input ("Введите номер записи , которую следует изменить "))
            return data[id-1]
        
main()