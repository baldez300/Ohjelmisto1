# 2 Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
# ympyrä pinta-ala laskeminen
# Kaava: Pii (3.14) * r*r
# Säde r
import math

print(math.pi)

r_string = input("Anna ympyrän säde (m): ")
r = float(r_string)
area = math.pi * r * r
print(f"{r} (m) säteisen ympyrän pinta-ale on {area:13.3f} neliömetriä")