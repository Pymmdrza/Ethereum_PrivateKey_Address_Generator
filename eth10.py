# ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
# ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
# ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
# ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
# ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
# ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================                                                     


from hdwallet import HDWallet
from hdwallet.symbols import ETH as SYMBOL
from hexer import mHash
import requests
import json
from colorama import Fore,Style
from lxml import html,etree


def ethtx(addr):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx2(addr2):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr2
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx3(addr3):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr3
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx4(addr4):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr4
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx5(addr5):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr5
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx6(addr6):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr6
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx7(addr7):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr7
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx8(addr8):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr8
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx9(addr9):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr9
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol


def ethtx10(addr10):
    urlblock = "https://ethereum.atomicwallet.io/address/" + addr10
    respone_block = requests.get(urlblock)
    byte_string = respone_block.content
    source_code = html.fromstring(byte_string)
    xpatch_txid = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
    treetxid = source_code.xpath(xpatch_txid)
    xVol = str(treetxid[0].text_content())
    return xVol



z = 1
while True:
    def priv():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv5():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv6():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv7():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv8():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv9():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def priv10():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv



    def addr():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr5():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr6():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr7():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr8():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr9():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def addr10():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def priv2():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def addr2():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def priv3():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def addr3():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    def priv4():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        priv = hdwallet.private_key()
        return priv


    def addr4():
        privv = mHash()
        PRIVATE_KEY = str(privv)
        hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
        hdwallet.from_private_key(private_key=PRIVATE_KEY)
        ads = hdwallet.p2pkh_address()
        return ads


    priv = priv()
    addr = addr()
    addr5 = addr5()
    addr6 = addr6()
    addr7 = addr7()
    addr8 = addr8()
    addr9 = addr9()
    addr10 = addr10()
    priv2 = priv2()
    priv3 = priv3()
    priv4 = priv4()
    priv5 = priv5()
    priv6 = priv6()
    priv7 = priv7()
    priv8 = priv8()
    priv9 = priv9()
    priv10 = priv10()
    addr2 = addr2()
    addr3 = addr3()
    addr4 = addr4()
    xtxid = ethtx(addr)
    xtxid2 = ethtx2(addr2)
    xtxid3 = ethtx3(addr3)
    xtxid4 = ethtx4(addr4)
    xtxid5 = ethtx5(addr5)
    xtxid6 = ethtx6(addr6)
    xtxid7 = ethtx7(addr7)
    xtxid8 = ethtx8(addr8)
    xtxid9 = ethtx9(addr9)
    xtxid10 = ethtx10(addr10)
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.RED,'Address =',Fore.YELLOW,str(addr2),Fore.BLUE,'|',Fore.WHITE,' txid =',Fore.MAGENTA,str(xtxid2),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr3),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid3),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.RED,'Address =',Fore.YELLOW,str(addr4),Fore.BLUE,'|',Fore.WHITE,' txid =',Fore.MAGENTA,str(xtxid4),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr5),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid5),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.RED,'Address =',Fore.YELLOW,str(addr6),Fore.BLUE,'|',Fore.WHITE,' txid =',Fore.MAGENTA,str(xtxid6),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr7),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid7),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.RED,'Address =',Fore.YELLOW,str(addr8),Fore.BLUE,'|',Fore.WHITE,' txid =',Fore.MAGENTA,str(xtxid8),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.YELLOW,'Address =',Fore.RED,str(addr9),Fore.BLUE,'|',Fore.GREEN,' txid =',Fore.WHITE,str(xtxid9),Style.RESET_ALL)
    z += 1
    print(Fore.WHITE,str(z),Fore.RED,'Address =',Fore.YELLOW,str(addr10),Fore.BLUE,'|',Fore.WHITE,' txid =',Fore.MAGENTA,str(xtxid10),Style.RESET_ALL)
    z += 1
    if int(xtxid) or int(xtxid2) or int(xtxid3) or int(xtxid4) or int(xtxid5) or int(xtxid6) or int(xtxid7) or int(xtxid8) or int(xtxid9) or int(xtxid10) > 0:
        print('Winer Wallet Doge Now \nInformation Wallet :\n\n\n ADDRESS = ',str(addr),'PRIVATE KEY = ',str(priv),'\nBALANCE',str(xtxid))
        f = open("WalletWinnerInfoETH.txt","a")
        f.write("\nADDRESS P2PKH = " + str(addr) + "  BALANCE = " + str(xtxid))
        f.write("\nADDRESS P2PKH = " + str(addr2) + "  BALANCE = " + str(xtxid2))
        f.write("\nADDRESS P2PKH = " + str(addr3) + "  BALANCE = " + str(xtxid3))
        f.write("\nADDRESS P2PKH = " + str(addr4) + "  BALANCE = " + str(xtxid4))
        f.write("\nADDRESS P2PKH = " + str(addr5) + "  BALANCE = " + str(xtxid5))
        f.write("\nADDRESS P2PKH = " + str(addr6) + "  BALANCE = " + str(xtxid6))
        f.write("\nADDRESS P2PKH = " + str(addr7) + "  BALANCE = " + str(xtxid7))
        f.write("\nADDRESS P2PKH = " + str(addr8) + "  BALANCE = " + str(xtxid8))
        f.write("\nADDRESS P2PKH = " + str(addr9) + "  BALANCE = " + str(xtxid9))
        f.write("\nADDRESS P2PKH = " + str(addr10) + "  BALANCE = " + str(xtxid10))
        f.write("\nPRIVATE KEY1 = " + str(priv))
        f.write("\nPRIVATE KEY2 = " + str(priv2))
        f.write("\nPRIVATE KEY3 = " + str(priv3))
        f.write("\nPRIVATE KEY4 = " + str(priv4))
        f.write("\nPRIVATE KEY5 = " + str(priv5))
        f.write("\nPRIVATE KEY6 = " + str(priv6))
        f.write("\nPRIVATE KEY7 = " + str(priv7))
        f.write("\nPRIVATE KEY8 = " + str(priv8))
        f.write("\nPRIVATE KEY9 = " + str(priv9))
        f.write("\nPRIVATE KEY10 = " + str(priv10))
        f.write("\n================[MMDRZA.CoM]================\n")
        f.close()
        print('\nSaved Information Complate ...[ ------- Mmdrza.Com ------- ]\n')
        continue

# ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗ 
# ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗
# ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║
# ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║
# ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║
# ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
# =====================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# =====================================================                                                     
