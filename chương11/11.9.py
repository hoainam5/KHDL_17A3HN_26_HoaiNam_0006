def party_late(arrivals,name):
    a=int(len(arrivals)/2)+1
    if name in arrivals[:a]:
        return True
    return False 
arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
print(party_late(arrivals,name='Owen'))

