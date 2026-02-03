# SleepSupportApp - 睡眠支援アプリ

照度センサーを活用した睡眠環境をサポートするAndroidアプリです。

## 機能

- 照度センサーによるリアルタイム照度計測
- 睡眠環境スコアの算出
- 睡眠に最適な環境かどうかの判定
- 改善アドバイスの表示

## 技術スタック

- React Native (Expo)
- TypeScript
- expo-sensors (照度センサー)

## セットアップ

### 前提条件

- Node.js 18以上
- npm または yarn
- Android Studio（エミュレーター使用時）
- Expo Go アプリ（実機テスト用）

### Android SDK 環境変数の設定

エミュレーターや実機デバッグを使用する場合、Android SDKの環境変数設定が必要です。

#### Mac / Linux

`~/.zshrc` または `~/.bashrc` に以下を追加：

```bash
# Android SDK
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

設定後、ターミナルを再起動するか `source ~/.zshrc` を実行。

#### Windows

1. **設定** → **システム** → **詳細情報** → **システムの詳細設定** → **環境変数**
2. **ユーザー環境変数** で **新規**：
   - 変数名: `ANDROID_HOME`
   - 値: `C:\Users\<ユーザー名>\AppData\Local\Android\Sdk`
3. **Path** を編集して以下を追加：
   - `%ANDROID_HOME%\platform-tools`
   - `%ANDROID_HOME%\emulator`

#### 設定確認

```bash
adb --version
```

バージョンが表示されればOKです。

### インストール

```bash
# 依存関係のインストール
npm install

# Huskyの初期化（初回のみ）
npm run prepare
```

### 開発サーバーの起動

```bash
# Expo開発サーバーを起動
npm start

# Androidで実行
npm run android

# iOSで実行（Macのみ）
npm run ios
```

## プロジェクト構成

```
SleepSupportApp/
├── src/
│   ├── components/     # 再利用可能なUIコンポーネント
│   ├── screens/        # 画面コンポーネント
│   ├── hooks/          # カスタムフック
│   ├── utils/          # ユーティリティ関数
│   ├── constants/      # 定数定義
│   ├── types/          # TypeScript型定義
│   └── services/       # 外部サービス連携
├── assets/             # 画像・フォントなどの静的ファイル
├── App.tsx             # アプリのエントリーポイント
└── app.json            # Expo設定ファイル
```

## 開発ルール

### コーディング規約

- ESLintとPrettierで自動フォーマット
- TypeScriptの厳格モード有効
- コミット前にlint-stagedで自動チェック

### ブランチ戦略

- `main` - 本番環境用
- `develop` - 開発統合ブランチ
- `feature/*` - 機能開発ブランチ
- `fix/*` - バグ修正ブランチ

### コミットメッセージ規約

```
<type>: <subject>

例:
feat: 照度センサーのリアルタイム表示機能を追加
fix: センサー停止時のメモリリークを修正
docs: READMEにセットアップ手順を追加
```

タイプ:

- `feat` - 新機能
- `fix` - バグ修正
- `docs` - ドキュメント
- `style` - フォーマット変更
- `refactor` - リファクタリング
- `test` - テスト追加
- `chore` - ビルド・設定変更

## 利用可能なスクリプト

| コマンド            | 説明                   |
| ------------------- | ---------------------- |
| `npm start`         | Expo開発サーバーを起動 |
| `npm run android`   | Androidで実行          |
| `npm run ios`       | iOSで実行              |
| `npm run lint`      | ESLintでコードチェック |
| `npm run lint:fix`  | ESLintで自動修正       |
| `npm run format`    | Prettierでフォーマット |
| `npm run typecheck` | TypeScriptの型チェック |

## 照度の目安

| 照度（lux） | 環境                 |
| ----------- | -------------------- |
| 0-10        | 睡眠に最適           |
| 10-50       | 睡眠準備に適している |
| 50-300      | 通常の室内           |
| 300以上     | 明るすぎる           |

## 注意事項

- 照度センサーはAndroidデバイスでのみ利用可能です
- iOSおよびWebでは照度センサーは動作しません
- 実機でテストすることを推奨します

## ライセンス

Private

## チームメンバー

- （チームメンバーを追加してください）
