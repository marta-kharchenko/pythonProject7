with open('guest_book.txt', 'w') as file_write:
    guest_name = ''
    while guest_name != 'Stop':
        guest_name = input('Please enter your name, or if you want to finish entering - enter "Stop":')
        if guest_name != 'Stop':
            print(f'Hello {guest_name}, welcome to us!')
            file_write.write(guest_name + '\n')