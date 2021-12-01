# オープンキャンパス自動案内AI”Salieri”

人間を検出し、自動で研究室案内をしてくれるAI

紹介ページ:https://tdu-ai-lab.github.io/activity/labai/

デモ動画: https://youtu.be/UJvwLCZXqPE

![salieri](https://user-images.githubusercontent.com/63311737/140689071-1c1dc696-a987-4f77-964c-75eaf11d2df2.png)

## 使用方法

### パッケージのインストール(Anaconda環境)
以下のコマンドを入力してください．

```
conda env create -n Salieri -f Salieri.yml
conda activate Salieri
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install git+https://github.com/openai/CLIP.git
```

音声入力コマンド
```
「人の画像を生成　　　：音声で指定した人の画像を生成します．
「会話モードを開始」　：雑談をすることができます．
「会話モードを終了」　：会話モードを終了します．
「ありがとう」　　　　：来客検出モードに戻ります．
「終了」　　　　　　　：プログラムを終了します．
```



顔画像生成参考コード
https://github.com/cedro3/StyleCLIP_G

チャットボット参考(未使用)
http://suriyadeepan.github.io/2016-12-31-practical-seq2seq/
