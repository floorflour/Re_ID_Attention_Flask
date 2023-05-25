from models.Employee import Employee


def generateEmp(employee: Employee):

    names = input('Enter names separated by /: ')
    names = names.split('/')

    id_cards = input('Enter ID cards separated by /: ')
    id_cards = id_cards.split('/')

    emails = input('Enter emails separated by /: ')
    emails = emails.split('/')

    for i in range(len(names)):
        emp_id = 100000 + i
        result = employee.create(
            name=names[i], personid=id_cards[i], mailaddress=emails[i])
        print(f'Add record {result} success!')
