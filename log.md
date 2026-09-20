# 日常練習：每天 add → commit → push 三步即可

階段 1：開啟終端機（Windows）

終端機（Terminal，用文字下指令的視窗）開法：

1. 按鍵盤 Win 鍵（微軟圖示鍵）
2. 輸入 powershell
3. 按 Enter，出現藍底或黑底視窗即成功



階段 2：安裝 Git（5 分鐘，只做一次）

1. 瀏覽器到 git-scm.com → 點 Downloads → Windows 版
2. 安裝時一路按 Next（全用預設值，不用改任何選項）
* 回終端機驗證：輸入 git --version 按 Enter
* 顯示 git version 2.x.x＝安裝成功

提醒（否則日後重裝照「全預設」會裝到 Vim＋master）

注意：有 2 頁不改預設：

* 編輯器頁選 Use Visual Studio Code
* 分支名稱頁選 Override 並填 main



階段 3：設定身份（2 行指令，只做一次）

* 作用：每個 commit 會蓋上你的名字與信箱
* 注意：信箱必須與 GitHub 帳號註冊信箱一致，貢獻圖才會計入

Windows Powershell Command:

git config --global user.name "Axan533"

git config --global user.email "xzanlee@gmail.com"



##### 階段 2、3：已完成，可跳過



階段 4：建練習儲存庫（網頁操作）

* GitHub 右上角 ＋ → New repository
* 名稱填：git-practice
* 選 Public 或 Private 皆可
* 勾選「Add a README file」（重要：讓庫非空白，clone 才順暢）
* 點 Create repository



階段 5：clone 到桌面（3 行指令）

* cd Desktop＝移動到桌面，資料夾會出現在桌面上
* clone 公開庫不用登入

Windows Powershell Command:

cd \~

git clone https://github.com/Axan533/git-practice.git

cd git-practice

涵蓋選 Private 的情況:

* 若建 Private 庫：第一次 clone 會彈登入視窗，選 GitHub 授權即可



階段 6：第一次完整三步（4 行指令）

1. 第 1 行：記事本會問「是否建立新檔案」→ 點是 → 輸入 年-月-日(執行當天的實際日期) day 1 → Ctrl+S 儲存 → 關閉記事本
2. 執行 git push 時會彈出登入視窗：選 GitHub → 瀏覽器授權登入 → 之後自動記住（這就是認證設定，不用額外操作）

Windows Powershell Command:                                   Windows Powershell Command:每日循環(約 1 分鐘，從 day 2 開始)

notepad log.md (儲存在--C:\\Users\\xzan\\git-practice\\log.md)    cd \~\\git-practice

git add .                                                     notepad log.md → 末尾加一行「日期 + 當天學習一句話」→ Ctrl+S → 關閉 (種開啟方式--notepad \~\\git-practice\\log.md)

git commit -m "day 1: 第一次設定完成"                          git add .

git push                                                      git commit -m "day N: 一句話描述"

按 Ctrl+` VS Code 開終端機(command 窗)                         git push

cd \~\\git-practice                     第 1 行：\~ 自動等於你的家目錄，不用手打用户名，不會走錯

dir                                   第 2 行：dir 列出內容＝裁判。看到 log.md、README.md＝真庫確認；若沒這兩個檔案＝停下來截圖給我

code .                                第 3 行：把「這個資料夾」開成 VS Code 工作區＝保證開對

終於正確狀態 ✓（三件套齊了）

* Message 輸入框 ✓、Commit 按鈕 ✓、Changes 列出 log.md（M、徽章 1） ✓
* Graph 顯示 Initial＋day 1～5＝倉庫連線正常

GUI 收下（四次點擊）

1. 滑鼠移到 log.md → 點 + → 檔案移入 Staged Changes（＝git add）
2. 點 Message 輸入框 → 輸入 day 6: 每日練習 VS Code
3. 點藍色 ✓ Commit（＝git commit）
4. 點 Sync Changes 按鈕（或左下狀態列 main\* 旁的 ⟳／1↑ 圖示）（＝git push）若彈確認視窗：點 OK



成功驗證（3 個檢查點）

* 終端機顯示 main -> main 字樣
* 重新整理 GitHub 網頁的 git-practice → 看到 log.md 出現
* 個人主頁貢獻圖「今天的格子」變綠（最多延遲幾分鐘）
* 自己驗證歷史完整性 Windows Powershell Command: git log --oneline



兩個常見錯誤:

fatal: not a git repository...＝不在儲存庫資料夾內：先執行 cd git-practice 再打 git 指令

* git : 無法辨識...＝Git 沒裝好：重開終端機再試，仍失敗就重裝
* push 顯示 authentication failed＝彈窗時登錯帳號：重新彈窗登入正確帳號



下一步三選一（上題未答）

1. 先穩一週每日循環：把三步練成肌肉記憶
2. 繼續學 Branch → PR → CI：補完協作四件套
3. VS Code 圖形界面操作 Git：左側 Source Control 面板，滑鼠完成 add/commit/push
4. 開始寫 Python 練習檔：放進 git-practice，一邊練 Python 一邊練 Git



2026/09/21 Day 9: 第九天的每日練習 Windows Powershell

