def query(title: str,text: str) -> None:
    res = ' '.join(['#' + r.split('#')[1] for r in text.split('\n') if r.strip()])
    print(title+'\n'+res)
    print()


if __name__ == '__main__':
    title = """
EIGER MIST FOREST 1.1 WALLET

https://shope.ee/10bgULjrjd

"""
    text = """
1. #EigerMistForest
2. #EigerWallet
3. #MistForestWallet
4. #LeatherWallet
5. #CanvasWallet
6. #CardSlots
7. #MoneyHolder
8. #HiddenPocket
9. #EverydayCarry
10. #MinimalistWallet
"""
    query(title, text)
