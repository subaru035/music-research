# Symbolic Feature Design Notes

`symbolic` 研究で先に整理したいのは、「音楽一般が何でできているか」よりも、
「楽譜や MIDI / MusicXML のような記号表現に、何がどう書かれているか」です。

この観点では、`symbolic` の要素は次の 3 層に分けると扱いやすくなります。

## 1. Encoded

ファイルそのものに直接書かれている要素です。

| Domain | Element | What it means | Typical availability | Unit |
| --- | --- | --- | --- | --- |
| Event | note / rest | 音符と休符そのもの | MIDI, MusicXML | event |
| Event | onset / duration | 始点と長さ | MIDI, MusicXML | event |
| Pitch | pitch / spelling | 音高、綴り、オクターブ | MIDI, MusicXML | event |
| Meter | measure / beat / meter | 小節、拍位置、拍子 | MusicXML, MIDI(一部) | beat / measure |
| Part | part / voice / channel | 声部やパートの区別 | MIDI, MusicXML | part / voice |
| Marking | dynamic / articulation / lyric | 強弱、奏法、歌詞 | 主に MusicXML | event / span |

## 2. Derived

直接は書かれていないが、記号同士の関係から計算できる要素です。

| Domain | Element | Derived from | Typical feature examples | Unit |
| --- | --- | --- | --- | --- |
| Melody | interval / contour | 連続する音高列 | 音程分布、順次進行率、輪郭変化数 | part / segment |
| Rhythm | density / pattern | onset と duration の並び | 音符密度、音価エントロピー、休符比率 | measure / piece |
| Verticality | simultaneity / chord slice | 同時発音の集合 | 平均同時発音数、和音変化率 | onset / measure |
| Voice leading | motion between parts | 複数声部の連続関係 | 反行率、平行進行率、声部交差数 | adjacent slice |
| Texture | active voice profile | 声部数と配置 | 平均発声音部数、厚みの変動 | onset / piece |
| Repetition | repeated pattern | n-gram や系列比較 | 反復率、再登場率 | segment / piece |

## 3. Inferred

分析者の理論的判断やルールを加えて推定する要素です。

| Domain | Element | Typical method | Typical feature examples | Unit |
| --- | --- | --- | --- | --- |
| Tonality | key / tonic stability | pitch-class 分布、調推定 | 調、転調回数、終止前の安定度 | segment / piece |
| Harmony | function / cadence | 和音同定、終止ルール | 終止候補数、属和音比率 | phrase / piece |
| Form | phrase / section | 反復、終止、休止、拍節境界 | フレーズ長、節構造の対称性 | phrase / section |
| Expectation | tension / release | 音程・和声・拍節の逸脱 | 不協和率、予測困難度 | segment / piece |

## Ontology v0

研究実装では、各要素に最低でも次の属性を持たせると設計が安定します。

| Field | Meaning |
| --- | --- |
| `name` | 要素名 |
| `status` | `encoded`, `derived`, `inferred` のどれか |
| `available_in` | MIDI / MusicXML / 両方 / 片方優位 |
| `unit_of_analysis` | event, part, measure, phrase, piece など |
| `feature_examples` | その要素から作れそうな特徴量 |
| `extraction_route` | どの順で計算・推定するか |

## How To Turn Elements Into Features

特徴量化では、「何を測るか」より先に「どの単位で観測するか」を固定します。

| Element | Observation unit | Minimal route to a feature |
| --- | --- | --- |
| note / rest | event | 音符数、休符数、平均音価 |
| onset / duration | measure / piece | 音符密度、duration entropy、休符比率 |
| pitch sequence | part | 音域、平均音程、順次進行率 |
| simultaneous notes | onset | 平均同時発音数、和音変化率 |
| part relations | adjacent slice | 反行率、平行 5 度 proxy、声部交差数 |
| pitch-class profile | segment / piece | 調推定、安定音比率 |
| repeated patterns | segment | 反復率、n-gram 再使用率 |
| cadence candidates | phrase end | 終止候補数、終止密度 |

## MVP For Bach Chorales

バッハ・コラールで最初に取るなら、次が現実的です。

- `encoded`: note, rest, onset, duration, part, measure
- `derived`: pitch range, interval size, step ratio, note density, duration entropy, simultaneity, active voice count
- `inferred`: key estimate, simple cadence proxy

`phrase` や `motif` は重要ですが、初手では推定の揺れが大きいので後回しで良いです。

## Example Extraction Route

最小の流れは次の通りです。

1. パースした `symbolic` データを `note events` に落とす
2. 声部ごとに時系列を作る
3. onset ごとに垂直スライスを作る
4. event-level の値を piece-level に集約する
5. 必要なら最後に tonality や cadence のような推定を足す

このリポジトリでは、実装の最小例を次に置いています。

- `symbolic/src/symbolic_lab/features/ontology.py`
- `symbolic/src/symbolic_lab/features/catalog.py`

前者は ontology の雛形、後者は note events から特徴量に落とすデモ実装です。
