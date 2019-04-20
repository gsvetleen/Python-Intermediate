# serialization  = allow objects to be saved into a file,
# so they can be stored or restored from the file later

# Python has a way of doing this using pickling
# Only use pickling when the data can be trusted
import pickle

imelda = ('More Mayhem', 'Imelda May', '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))
# EXAMPLE 1
# deserialize
with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# serializing the object
with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

# assigning from tuple
album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

# EXAMPLE 2

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle2","wb") as pickle_file:
    pickle.dump(imelda,pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2998302, pickle_file)

with open("imelda.pickle2","rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_List = pickle.load(imelda_pickled) # returns list
    odd_list = pickle.load(imelda_pickled) # returns list


print(imelda2)