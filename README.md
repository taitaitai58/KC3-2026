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
- pnpm（Node.js 16.13+ では `corepack enable` で有効化。または `npm install -g pnpm` でインストール）
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
# pnpmを有効化（初回のみ、Node.jsに同梱のCorepackを使用）
corepack enable

# 依存関係のインストール
pnpm install

# 環境チェック（初回におすすめ）
pnpm run setup

# Huskyの初期化（初回のみ）
pnpm run prepare
```

### 開発サーバーの起動

```bash
# Expo開発サーバーを起動
pnpm start

# Androidで実行
pnpm run android

# iOSで実行（Macのみ）
pnpm run ios
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
- **Push前にpre-pushフックでブランチチェック**（`main`/`master`へのpush時や他人のコミットがある場合に警告し、任意でpush可能。現在のブランチとpush対象の一致を確認）

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

| コマンド                  | 説明                                           |
| ------------------------- | ---------------------------------------------- |
| `pnpm start` / `pnpm dev` | Expo開発サーバーを起動                         |
| `pnpm run android`        | Androidで実行                                  |
| `pnpm run ios`            | iOSで実行                                      |
| `pnpm run setup`          | 環境チェック（初心者向け）                     |
| `pnpm run check`          | lint + 型チェック + フォーマット確認を一括実行 |
| `pnpm run reset`          | 詰まったときのリセット（node_modules 再構築）  |
| `pnpm run start:clear`    | キャッシュをクリアして起動（挙動が怪しいとき） |
| `pnpm run lint`           | ESLintでコードチェック                         |
| `pnpm run lint:fix`       | ESLintで自動修正                               |
| `pnpm run format`         | Prettierでフォーマット                         |
| `pnpm run typecheck`      | TypeScriptの型チェック                         |

## 照度の目安

| 照度（lux） | 環境                 |
| ----------- | -------------------- |
| 0-10        | 睡眠に最適           |
| 10-50       | 睡眠準備に適している |
| 50-300      | 通常の室内           |
| 300以上     | 明るすぎる           |

## 困ったときは

| 症状                         | 対処法                                                        |
| ---------------------------- | ------------------------------------------------------------- |
| `pnpm` が動かない            | `corepack enable` を実行                                      |
| Node のバージョンが合わない  | `.nvmrc` 参照。nvm なら `nvm use`                             |
| 起動がおかしい・エラーが出る | `pnpm run reset` でリセット                                   |
| Metro のキャッシュが怪しい   | `pnpm run start:clear` でキャッシュクリア起動                 |
| コミットが通らない           | `pnpm run lint:fix` と `pnpm run format` を実行               |
| push がブロックされる        | 保護ブランチや他人のコミットがある場合は確認して `y` で続行可 |

## 注意事項

- 照度センサーはAndroidデバイスでのみ利用可能です
- iOSおよびWebでは照度センサーは動作しません
- 実機でテストすることを推奨します

## ライセンス

Private

## チームメンバー

- （チームメンバーを追加してください）
