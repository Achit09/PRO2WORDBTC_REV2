#███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
#████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
#██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
#██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
#██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
#╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
# This Script Has Trial / Can Order For Pro version Follow https://mmdrza.com
######################################################################################

import requests, json, base58, random, os, binascii, codecs, time
from hdwallet import HDWallet
from hdwallet.symbols import BTC
from hdwallet.utils import generate_mnemonic
from rich import print
from rich.console import Console
from bit import Key
from bit.format import bytes_to_wif
from pycoin.symbols.btc import network as BTC_network
from pycoin.encoding.hexbytes import b2h

# API 節點列表
API_ENDPOINTS = [
    "https://btc4.trezor.io/api/v2/address/",
    "https://blockstream.info/api/address/",
    "https://chain.api.btc.com/v3/address/",
    "https://api.blockcypher.com/v1/btc/main/addrs/"
]

console = Console()

def get_balance_and_txs(address):
    """從多個API節點獲取餘額和交易數據"""
    for api in API_ENDPOINTS:
        try:
            if "trezor" in api:
                response = requests.get(f"{api}{address}").json()
                return dict(response)['balance'], dict(response)['txs']
            elif "blockstream" in api:
                txs = requests.get(f"{api}{address}/txs/count").json()
                balance = requests.get(f"{api}{address}").json()['chain_stats']['funded_txo_sum']
                return balance, txs
            elif "btc.com" in api:
                response = requests.get(f"{api}{address}").json()
                data = response['data']
                return data['balance'], data['tx_count']
            elif "blockcypher" in api:
                response = requests.get(f"{api}{address}").json()
                return response['final_balance'], response['n_tx']
        except Exception as e:
            continue
    return 0, '0'

def save_progress(z, fo, vo):
    """保存進度到文件"""
    with open("progress.json", "w") as f:
        json.dump({"scans": z, "found": fo, "value": vo}, f)

def load_progress():
    """從文件加載進度"""
    try:
        with open("progress.json", "r") as f:
            data = json.load(f)
            return data.get("scans", 0), data.get("found", 0), data.get("value", 0)
    except:
        return 0, 0, 0

def main():
    # 加載保存的進度
    z, fo, vo = load_progress()
    
    console.print("[cyan]開始運行比特幣地址生成和檢查...[/cyan]")
    console.print(f"[green]已加載進度 - 掃描: {z}, 發現: {fo}, 有值: {vo}[/green]")

    while True:
        try:
            # 生成新的助記詞
            mnemonic = generate_mnemonic(language="english", strength=128)
            
            z += 1
            if z % 100 == 0:  # 每100次保存一次進度
                save_progress(z, fo, vo)
            
            # 創建錢包
            hdwallet = HDWallet(symbol=BTC)
            hdwallet.from_mnemonic(mnemonic=mnemonic)
            hdwallet.from_path(path="m/44'/0'/0'/0/0")
            
            # 獲取私鑰和地址
            private_key = hdwallet.private_key()
            bytePrivate = codecs.decode(private_key, 'hex_codec')
            wifCompressed = bytes_to_wif(bytePrivate, compressed=True)
            wifUnCompressed = bytes_to_wif(bytePrivate, compressed=False)
            
            bit_com = Key(wifCompressed)
            bit_uncom = Key(wifUnCompressed)
            compressedAddr = bit_com.address
            uncompressedAddr = bit_uncom.address
            
            # 檢查餘額和交易
            balance_compressed, txs_Compressed = get_balance_and_txs(compressedAddr)
            balance_uncompressed, txs_unCompressed = get_balance_and_txs(uncompressedAddr)
            
            if int(txs_Compressed) > 0 or int(txs_unCompressed) > 0:
                fo += 1
                with open("Found.txt", "a") as f:
                    f.write(f"""
Compressed Address: {compressedAddr} TXS: {txs_Compressed}
unCompressed Address: {uncompressedAddr} TXS: {txs_unCompressed}
Mnemonic: {mnemonic}
Private Key: {private_key}
WIF Compressed: {wifCompressed}
WIF Uncompressed: {wifUnCompressed}
{'-' * 50}
""")
                
                if int(balance_compressed) > 0 or int(balance_uncompressed) > 0:
                    vo += 1
                    with open("FoundWithValue.txt", "a") as f:
                        f.write(f"""
Compressed Address: {compressedAddr} Balance: {balance_compressed}
unCompressed Address: {uncompressedAddr} Balance: {balance_uncompressed}
Mnemonic: {mnemonic}
Private Key: {private_key}
WIF Compressed: {wifCompressed}
WIF Uncompressed: {wifUnCompressed}
{'-' * 50}
""")
            
            # 輸出狀態
            console.print(f"[red1]掃描:[white]{z}[/white] 發現:[white]{fo}[/white] 有值:[white]{vo}[/white]")
            console.print(f"地址: [cyan]{compressedAddr}[/cyan]")
            console.print(f"助記詞: [white]{mnemonic}[/white]")
            
        except KeyboardInterrupt:
            console.print("[red]程序被用戶中斷[/red]")
            save_progress(z, fo, vo)
            break
        except Exception as e:
            console.print(f"[red]錯誤: {str(e)}[/red]")
            continue

if __name__ == "__main__":
    main()
