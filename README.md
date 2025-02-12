# 比特幣地址生成和檢查工具

![Bitcoin Address Generator and Checker](https://img.shields.io/badge/Bitcoin-Generator-orange)

## 功能簡介

這是一個用於生成和檢查比特幣地址的工具，具有以下特點：

- 使用 BIP39 標準生成助記詞
- 支持壓縮和非壓縮地址格式
- 多個 API 節點備份確保穩定性
- 自動保存進度功能
- 彩色控制台輸出界面

## 安裝需求

需要安裝以下 Python 套件：

```bash
pip install requests base58 bit hdwallet rich pycoin
```

## 使用方法

直接運行主程式：

```bash
python Pro2WordTrial_c.py
```

## 功能特點

1. **多 API 節點支持**
   - Trezor
   - Blockstream
   - BTC.com
   - BlockCypher

2. **進度保存**
   - 每 100 次掃描自動保存
   - 程序中斷時自動保存
   - 啟動時自動加載上次進度

3. **輸出文件**
   - Found.txt: 記錄所有發現的交易地址
   - FoundWithValue.txt: 記錄所有有餘額的地址
   - progress.json: 保存掃描進度

4. **安全特性**
   - 使用標準 BIP39 助記詞
   - 支持 BIP44 路徑
   - 完整的錯誤處理機制

## 輸出示例

程序運行時會顯示：
- 當前掃描次數
- 發現的地址數量
- 發現的有值地址數量
- 當前生成的比特幣地址
- 對應的助記詞

## 注意事項

1. 需要穩定的網絡連接
2. API 可能有請求限制
3. 建議長期運行時使用 screen 或 tmux

## 錯誤處理

- 自動切換 API 節點
- 異常捕獲和記錄
- 進度保存確保數據不丟失

## 開發信息

- 作者：[Achit09]
- 版本：1.0.0
- 授權：MIT
- 2025-02-11 運行正常

## 免責聲明

本工具僅供學習和研究使用，請勿用於非法用途。使用本工具所產生的任何後果由使用者自行承擔。

---

如有問題或建議，歡迎提出 Issue 或 Pull Request。
