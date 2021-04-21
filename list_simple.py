clients = ["John","Marry","Kate"]
clientsHighPriority = ["Tob","Pete"]
clientsLowPriority = ["Vicky","Lessly"]


def showClients(all, high = None, low = None):
    if high != None:
        for i in range(len(high)):
            all.insert(i, high[i])
    if low != None:
        for i in range(len(low)):
            all.append(low[i])
    for i in range(len(all)):
        print(f'{i+1}. {all[i]}')


showClients(clients, clientsHighPriority, clientsLowPriority)
   
   


