# kojo-fan-art

これは『[かがみの孤城](https://movies.shochiku.co.jp/kagaminokojo/)』のファンアートプロジェクトです。

## インストール

```sh
$ pip install kojo-fan-art
```

## 使い方

『かがみの孤城』の登場人物それぞれのパラレルワールドで、今日が何曜日かをJSON形式で表示します。

```sh
$ kojo-day kokoro aki fuka
{"kokoro": "Friday", "aki": "Monday", "fuka": "Monday"}

$ # jqコマンドに渡せば、見やすく表示できます
$ kojo-day kokoro aki fuka | jq .
{
  "kokoro": "Friday",
  "aki": "Monday",
  "fuka": "Monday"
}
```

`kojo-day -h`でヘルプメッセージを表示します。

## 開発環境構築

```sh
$ git clone git@github.com:ftnext/the-solitary-castle-in-the-mirror-cli.git
$ cd the-solitary-castle-in-the-mirror-cli

$ python3.11 -m venv venv --upgrade-deps
$ source venv/bin/activate

(venv) $ pip install -e '.[dev]'
(venv) $ task test
```

⚠️実装には『かがみの孤城』のネタバレを含みます
