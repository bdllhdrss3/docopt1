'''
making a module with methods of andela dojo space allocator
to create offices and livingspaces as files and allocate 
staff and fellows to office files and only fellows to 
livinspaces
'''
'creating an office'
def create_office(room_name):
    print('\n')
    print(str(room_name)+ '  office has been created ')
    print('\n')
    room_name = open('office.txt','w')
    room_name.close()
'creating livingspace'
def livingspace(room_name):
    print('\n')
    print(str(room_name)+ '  livingspace has been created ')
    print('\n')
    room_name = open('livingspace.txt','w')
    room_name.close()
'#for adding a fellow to office'
def add_felllow(name):
        print('\n')
        print(name + ' as a fellow has been added to dojo')
        
        add_felllow = open('office.txt','a')
        add_felllow.write('\n'+ name +' -FELLOW')
        add_felllow.close()
        add_felllowL = open('livingspace.txt' , 'a')
        add_felllowL.write('\n'+ name +' -FELLOW')
        add_felllowL.close()
'adding staff to office'
def add_staff(name):
        print('\n')
        print(name + ' as a staff has been added to dojo')
        print('\n')
        add_staff = open('office.txt','a')
        add_staff.write('\n'+ name +'- STAFF')
        add_staff.close()
'printing office'
def print_office(name):
        print('\n')
        print('this is office  ' + name)
        
        room_name = open('office.txt','r')
        print(room_name.read())
        room_name.close()
        print('\n')
        
'printing livinspaces'
def living(name):
         print('\n')
         print('this is livingspace  ')
         
         file = open('livingspace.txt','r')
         print(file.read())
         file.close()
         print('\n')
