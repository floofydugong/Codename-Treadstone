def validate_hello(greetings):
    various_hello = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]

    for word in greetings.split():
        print word
        if word in various_hello:
            print True
            break
        else:
            print False

validate_hello("hallo,")