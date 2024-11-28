# Python プロジェクトの静的解析テンプレート (SonarQube + pytest)

このリポジトリは、SonarQube を使用して Python プロジェクトを静的解析するためのテンプレートです。また、pytest を使用してテストカバレッジを測定する方法も示しています。

## 前提条件

このテンプレートを使用する前に、以下の準備が必要です:

1. **SonarQube** と **sonar-scanner** がインストールされていること。
2. SonarQube の Web UI 上で `test_sonar` というプロジェクトが作成済みであること。
3. Python ライブラリ `pytest` と `pytest-cov` がインストールされていること。

インストールがまだの場合は以下のコマンドを実行してください:

```bash
pip install pytest pytest-cov
```

## 使用方法

以下の手順で SonarQube を使用した静的解析とテストカバレッジ測定を行います。

### 1. `sonar-project.properties` の作成

プロジェクトディレクトリ直下に `sonar-project.properties` ファイルを作成し、以下の内容を記述します:

```properties
sonar.projectKey=test_sonar
sonar.projectName=test_sonar
sonar.sources=.
sonar.language=py
sonar.host.url=http://localhost:9000
sonar.token=<your-sonarQube-project-token>
sonar.python.coverage.reportPaths=coverage.xml
sonar.python.version=<your-python-version>
```

- `<your-sonarQube-project-token>` を実際のプロジェクトトークンに置き換えてください。
- `<your-python-version>` を Python のバージョンに置き換えてください (例: `3.8` や `3.10` など)。

### 2. テストケースの実行

プロジェクト内のテストスクリプトを `pytest` を使って実行します。以下のコマンドを使用してください:

```bash
pytest test_functions.py
```

### 3. テストカバレッジレポートの作成

`pytest-cov` を使用してテストカバレッジレポートを生成します。以下のコマンドを実行してください:

```bash
pytest --cov=. --cov-report=xml
```

このコマンドで `coverage.xml` ファイルが生成されます。

### 4. SonarQube スキャンの実行

`sonar-scanner` を使用して SonarQube に解析データを送信します。以下のコマンドを実行してください:

```bash
sonar-scanner
```

### 5. SonarQube Web UI で確認

SonarQube の Web UI にアクセスし、`test_sonar` プロジェクトの解析結果を確認してください。  
デフォルトの URL は以下の通りです:  
[http://localhost:9000](http://localhost:9000)

## 注意事項

- SonarQube サーバが起動していることを確認してください。
- カバレッジ測定を行う際、`pytest-cov` が正しくインストールされていることを確認してください。

以上の手順に従って、Python プロジェクトの静的解析を実施してください。
