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

# Pipenvを使う場合
pipenv install matplotlib-fontja

# Poetryを使う場合
poetry add matplotlib-fontja

# Ryeを使う場合
rye add matplotlib-fontja
rye sync

# Condaを使う場合
conda install conda-forge::matplotlib-fontja
```

## 利用フォント

IPAexゴシック (Ver.004.01) を利用しています。
利用にあたっては[IPAフォントライセンスv1.0](https://github.com/ciffelia/matplotlib-fontja/blob/master/japanize_matplotlib/fonts/IPA_Font_License_Agreement_v1.0.txt)に同意してください。

## FAQ

### `import matplotlib_fontja`したのに日本語表示になりません [#1](https://github.com/uehara1414/japanize-matplotlib/issues/1)

`import matplotlib_fontja`してからmatplotlibでグラフを描画するまでにフォントの設定が変わる処理が入っていると、日本語表示がなされない可能性があります。

例えば、seabornを利用している場合であれば`sns.set()`などで描画フォントが seaborn のデフォルトに上書きされ、日本語表示がされなくなります。

`sns.set(font="IPAexGothic")`のように利用フォントに`IPAexGothic`を設定するか、フォント上書き後に`matplotlib_fontja.japanize()`を利用するなどで日本語表示できるはずです。

### importのみして利用されないコードなのでフォーマッターに消されてしまいます

リンターなどの警告が気になる・コードを消される方向けに`matplotlib_fontja.japanize()`メソッドの実行でもimport時と同じくフォントを設定できるようになっています。
無意味な実行になりますが、時と場合に応じて実行してください。

もしくはリンターごとに無視させる設定をすることで対応できるはずです。`# noqa`などで設定してください。

### なぜインストール時は`matplotlib-fontja`でimport時は`matplotlib_fontja`なのですか？

チェインケースが読みやすく好きだからです。import時にはチェインケースは利用できないのでスネークケースになっています。
