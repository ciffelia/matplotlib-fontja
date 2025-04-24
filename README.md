# matplotlib-fontja

[![CI status](https://github.com/ciffelia/matplotlib-fontja/actions/workflows/ci.yaml/badge.svg)](https://github.com/ciffelia/matplotlib-fontja/actions/workflows/ci.yaml)
[![PyPI project](https://badge.fury.io/py/matplotlib-fontja.svg)](https://pypi.org/project/matplotlib-fontja/)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/matplotlib-fontja.svg)](https://anaconda.org/conda-forge/matplotlib-fontja)

matplotlibを日本語表示に対応させます。

[uehara1414](https://github.com/uehara1414)さんの[japanize-matplotlib](https://github.com/uehara1414/japanize-matplotlib)をフォークし、Python 3.12以降でも動作するよう修正したものです。変更点の詳細については[CHANGELOG](https://github.com/ciffelia/matplotlib-fontja/blob/master/CHANGELOG.md)をお読みください。

## 利用方法

matplotlibをimportした後、matplotlib_fontjaをimportします。

```python
import matplotlib.pyplot as plt
import matplotlib_fontja

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()
```

![demo](https://raw.githubusercontent.com/ciffelia/matplotlib-fontja/master/demo.png)

## インストール

```sh
# pipを使う場合
pip install matplotlib-fontja

# uvを使う場合
uv add matplotlib-fontja

# Ryeを使う場合
rye add matplotlib-fontja

# Pipenvを使う場合
pipenv install matplotlib-fontja

# Poetryを使う場合
poetry add matplotlib-fontja

# Condaを使う場合
conda install conda-forge::matplotlib-fontja
```

## 動作確認環境

以下のPythonとMatplotlibのバージョンの組み合わせで動作を確認しています。

- Python 3.7: Matplotlib 3.0 - 3.5
- Python 3.8: Matplotlib 3.3 - 3.7
- Python 3.9: Matplotlib 3.3 - 3.9
- Python 3.10: Matplotlib 3.3 - 3.10
- Python 3.11: Matplotlib 3.3 - 3.10
- Python 3.12: Matplotlib 3.5 - 3.10
- Python 3.13: Matplotlib 3.5 - 3.10

## 利用フォント

IPAexゴシック (Ver.004.01) を利用しています。
利用にあたっては[IPAフォントライセンスv1.0](https://github.com/ciffelia/matplotlib-fontja/blob/master/src/matplotlib_fontja/fonts/IPA_Font_License_Agreement_v1.0.txt)に同意してください。

## FAQ

### `import matplotlib_fontja`したのに日本語が表示されません

`import matplotlib_fontja`してからグラフを描画するまでにフォントの設定が変わる処理が入っている可能性があります。

例えば、seabornを使用していると`sns.set_theme()`などでフォントがseabornのデフォルトに上書きされてしまいます。

以下のように、フォント上書き後に`matplotlib_fontja.japanize()`を実行してください。

```python
sns.set_theme()
matplotlib_fontja.japanize()
```

seabornの場合は、`sns.set_theme(font="IPAexGothic")`として`IPAexGothic`を使用するよう設定することもできます。

### `import matplotlib_fontja`に対してリンターの警告(F401)が出ます/フォーマッターに消されてしまいます

importした`matplotlib_fontja`を使用していないため、不要なimportと誤判定されています。以下のように`noqa`で無効化してください。

```python
import matplotlib_fontja  # noqa: F401
```

あるいは、`matplotlib_fontja.japanize()`を使用すれば未使用と判定されません。無意味な実行になりますが、import直後などに追加して警告を消すこともできます。

```python
import matplotlib_fontja

matplotlib_fontja.japanize()
```

### IPAexゴシック以外のフォントを使いたいです

matplotlibの標準機能で任意のフォントを使用できます。matplotlib-fontjaは不要です。以下はNoto Sans Japaneseを使う例です。

```python
import matplotlib.font_manager
import matplotlib.pyplot as plt

# フォントファイルを読み込み
matplotlib.font_manager.fontManager.addfont(
    "/path/to/NotoSansJP-Regular.ttf"
)

# 読み込んだフォントを使用するよう設定
matplotlib.rc("font", family="Noto Sans JP")

plt.plot([1, 2, 3, 4])
plt.xlabel('簡単なグラフ')
plt.show()
```
