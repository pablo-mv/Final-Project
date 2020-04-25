import sys
sys.path.append('../')
from AmazonManagement import AmazonManagement
from srs.collection.DSMembers import DSMembers
from srs.collection.DoublyLinkedList import DList
from srs.collection.DSMember import DSMember
from srs.collection.Package import Packet
from random import randint


def compleateTest():
    print('Creating instance of Amazon')
    amazon = AmazonManagement()
    
    num_packets = int(input('How many packets you want to simulate?: '))
    num_members = int(input('How many members you want to simulate?: '))
    
    # Creating the orders
    names_direction = ('Jose', 'George', 'Michael', 'Jackson', 'Jordan',
                       'Christopher', 'First', 'Second', 'Ana', 'Isabel',
                       'Colombus', 'America', 'Equator', 'Spain', 'Europe')
    ## Creating the postal codes
    postal_codes = []
    for _ in range(10):
        postal_codes.append(randint(10000, 99999))
    
    ## The data needed to save a packet
    ## (num1,num2,num3,address_name, street_number, postal_code, errors)  
    orders = DList()
    
    for _ in range(num_packets):
        n1 = randint(100, 999)
        n2 = randint(100000, 999999)
        n3 = randint(100000, 999999)
        direction =  names_direction[randint(0, 14)] + ' ' + names_direction[randint(0, 14)]
        num = randint(1, 50)
        pcode = postal_codes[randint(0,9)]
        err = 0
        orders.addLast(Packet(n1,n2,n3,direction,num,pcode, err))
        
    
    # Creating the members
    names_members = ('Paco', 'Maria', 'Paulina', 'Rubi', 'Paola', 'Miossothy', 
                     'Franchesco', 'Benito', 'Pancracio', 'Segismundo')
    lastnames_members = ('Fernandez', 'Pacheco', 'Smith', 'Jackson', 'Castillo',
                         'Mantilla', 'Milos', 'Naranjo', 'Manzano', 'Garcia')
    status = ('Active', 'Active', 'Inactive') # THe probability of being inactive is 1/3
    
    
    
    members = DList()
    for _ in range(num_members):
        name = names_members[randint(0,9)]
        surname = lastnames_members[randint(0,9)]
        stat = status[randint(0,2)]
        identifier = randint(0, 999999)
        members.addLast(DSMember(identifier, name, surname, stat))
    testing_member = members.getAt(randint(0,num_members-1))   
    
    
    input('Excecuting loadOrders(), pulse enter to continue')
    amazon.loadOrders(orders)

    input('Excecuting loadDSMembers(), pulse enter to continue')
    amazon.loadDSMembers(members)
    # input('Showing Members. Press enter to continue')
    
    print('')
    amazon.showDSMember()
    
    input('Assigning packets to members. Pulse enter to continue')
    amazon.assignDistribution()
    input('Showing Members. Press enter to continue')
    amazon.showDSMember()
    
    input('Testing removeDSMmber, press enter to continue')
    input('Info of the member, press enter')
    print(testing_member)
    input('Excecuting removeDSMember, press enter to continue')
    amazon.removeDSMember(testing_member.identifier)
    
    input('Showing Members. Press enter to continue')
    amazon.showDSMember()
    
    input('Delivering packets. Pulse enter to continue')
    amazon.deliver()
    
    input('Showing Members. Press enter to continue')
    amazon.showDSMember()

