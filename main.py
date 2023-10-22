def query():
    text = """
1. #IndofoodBumbuRacikBubuk
2. #BumbuKering
3. #BubukBumbu
4. #NasiGoreng
5. #TempeGoreng
6. #IkanGoreng
7. #SayurLodeh
8. #SayurSop
9. #Tumis
10. #AyamGoreng
"""
    title = """
INDOFOOD Bumbu Racik Bubuk 20g, PER SASET

https://shope.ee/1LEVvplIgu

"""

    res = ' '.join(['#' + r.split('#')[1] for r in text.split('\n') if r.strip()])
    print(title+'\n'+res)
    print()


if __name__ == '__main__':
    query()
