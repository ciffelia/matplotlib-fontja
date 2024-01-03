# リリース手順

1. `pyproject.toml`と`CHANGELOG.md`を更新します。
2. `Release x.y.z`というメッセージでコミットを作成し、masterにプッシュします。
3. CIが通っていることを確認します。
4. [リリースを作成](https://github.com/ciffelia/matplotlib-fontja/releases/new)します。その際、タグ`x.y.z`を作成します。
5. [Publish package to PyPI workflow](https://github.com/ciffelia/matplotlib-fontja/actions/workflows/publish.yaml)を、作成したタグに対してdispatchします。
