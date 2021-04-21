clients = []

def showClients(all):
    for i in range(len(all)):
        print(f'{i+1}. {all[i]}')

priority_client = 0

while True:
    print("." * 30)
    name = input("What is your name >>>  ")
    print("." * 40)
    order = int(input("Please enter your order amount (USD) ----- "))
    if order <= 50:
        clients.append(name)
    elif order > 50:
        clients.insert(priority_client, name)
        priority_client += 1
    showClients(clients)
    
   
   


