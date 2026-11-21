# outdoor-weather-pool

户外展演转场观察、天气读数、互助条款和赔付凭据。 其中人物代号、机构、交易及历史回执均为合成资料。

## 数据约定

`data/layout.json` 逐一解释业务表及 CSV 列顺序，`data/rules.json` 记录运营口径。CSV 使用 UTF-8、首行为列名；空白字段表示未提供或不适用，`+` 隔开多值字段。历史记录的业务时刻与送交时刻含义不同，按各表说明解释。

- `rain.csv`：每次站点读数及后收更正，缺测以空白表示；同编号取可见的最终修订。
- `performances.csv`：原定节目窗、已知实际完成分钟、场地转移和原本承担的费用。
- `recoveries.csv`：票务、场地等已经追回的费用，不与演出替代重复扣回。
- `policy_options.csv`：候选主站、事先批准的备用站和触发阈值；minutes 是连续阈值覆盖时长。
- `agreements.csv`：已生效文书、给付状态及拟签条款。日界与节目时间均用当地日期。
- `settlements.csv`：共享池历史回执；amount 为空表示金额仍未核定。

## 本地检查

使用 Python 3.11 及标准库。`python3 inspect_inputs.py` 读取原始资料并列出记录数；`python3 -m unittest discover -s tests` 检查输入资料。检查不计算或发布业务结论。
