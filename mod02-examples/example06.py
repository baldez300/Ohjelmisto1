import random

# Ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

random_nums1 = random.sample(range(1, 9), 3)
random_nums2 = random.sample(range(1, 6), 4)


print(f"Arvottu numero välillä 1-9: {random_nums1}")
print(f"Arvottu numero välillä 1-6: {random_nums2}")

print(random.randint(0, 9), 3)
print(random.randint(0, 9), 4)