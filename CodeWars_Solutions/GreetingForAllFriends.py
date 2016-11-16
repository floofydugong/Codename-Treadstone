def greeting_for_all_friends(friends):
    greeting_list = []
    if not friends:
      None
    elif friends:
       for i, friend in enumerate(friends):
           greeting_list.append(("Hello, "+friends[i] +"!"))
       return greeting_list