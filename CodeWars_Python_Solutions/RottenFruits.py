def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        print("empty")
    else:
        final_list = []
        for i in bag_of_fruits:
            if i[0:6] == 'rotten':
                final_list.append(i[6:].lower())
            else:
                final_list.append(i)
        print(final_list)


remove_rotten(["apple","rottenBanana","apple"])