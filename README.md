# kojo-fan-art

[日本語版 (In Japanese)](./README.ja.md)

This is a fan art project for "Lonely Castle in the Mirror."

## Installation

```sh
$ pip install kojo-fan-art
```

## Usage

This tool shows what day of the week it is in each character's parallel world from "Lonely Castle in the Mirror" in JSON format.

```sh
$ kojo-day kokoro aki fuka
{"kokoro": "Friday", "aki": "Monday", "fuka": "Monday"}

$ # pretty print with jq
$ kojo-day kokoro aki fuka | jq .
{
  "kokoro": "Friday",
  "aki": "Monday",
  "fuka": "Monday"
}
```

For help message, type `kojo-day -h`.


## Development environment

```sh
$ git clone git@github.com:ftnext/the-solitary-castle-in-the-mirror-cli.git
$ cd the-solitary-castle-in-the-mirror-cli

$ python3.11 -m venv venv --upgrade-deps
$ source venv/bin/activate

(venv) $ pip install -e '.[dev]'
(venv) $ task test
```

⚠️The implementation reveals the secrets of "Lonely Castle in the Mirror."
