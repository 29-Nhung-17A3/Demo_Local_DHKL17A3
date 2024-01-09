def party_late(arrivals, name):
    total_guests = len(arrivals)
    guest_index = arrivals.index(name)
    return guest_index >= total_guests // 2 and guest_index != total_guests - 1
arrivals = ["Adela", "Fleda", "Owen", "Mona", "May", "Gilbert", "Ford"]
print(party_late(arrivals, name = 'Gilbert'))
print(party_late(arrivals, name = 'Mona'))
print(party_late(arrivals, name = 'Owen'))

