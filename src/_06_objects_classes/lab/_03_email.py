class Email:
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'




if __name__ == '__main__':
    a = input().split(' ')

    b = []
    
    while a[0] != 'Stop':
        b += [a]  # sender, receiver, content
        a = input().split(' ')

    c = list(map(int, input().split(', '))) # is_sent index

    for i, x in enumerate(b):
        o = Email(x[0], x[1], x[2])
        if i in c:
            o.send()
            print(o.get_info())
        else:
            print(o.get_info())
