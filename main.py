def query():
    text = """
1. #MieSarimiKalduAyam
2. #70gr
3. #MieMurah
4. #Shopee
5. #InstantNoodles
6. #ChickenNoodles
7. #AffordableNoodles
8. #QuickMeal
9. #ConvenientFood
10. #NoodleLovers
"""
    title = """
Mie Sarimi Kaldu Ayam @70gr - Mie Murah

https://shope.ee/7KVj4Tpkil

"""

    res = ' '.join(['#' + r.split('#')[1] for r in text.split('\n') if r.strip()])
    print(title+'\n'+res)
    print()


if __name__ == '__main__':
    query()
