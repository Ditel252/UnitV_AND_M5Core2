# UnitV_AND_M5Core2
## 説明
UnitV AI Cameraで撮影した写真を, そのままM5Stack Core2に表示するプログラム.
## 環境
|項目|内容|
|----|----|
|OS|Ubuntu 22.04.4 LTS x86_64|
|エディタ(M5stack Core2)|Visual Studio Code|
|エディタ(UnitV AI Camera)|MaixPyIDE|

## プログラムについて
### M5stack Core2側
特に留意するべき点なし.
### UnitV AI Camera側
以下の部分については, ユーザーの用途によって要変更.
|該当部分|説明|
|--------|----|
|`MAGE_QUALITY = 25`|画像の圧縮率を設定する. (100になるほど高画質)|
|`IMAGE_UPDATE_RATE = 20`|画像の更新速度を設定する. (単位:ms)|

## 参考文献  
https://qiita.com/Nabeshin/items/9268dc88927123319549  
https://logikara.blog/lovyangfx_m5stack/