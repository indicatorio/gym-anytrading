"""加密货币数据源(来自 binance_module 本地库)。"""
import os
import sys

# 兼底: 让本模块无论从哪个 CWD 运行, 都能找到 QDK 根目录下的 binance_module
_QDK_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if _QDK_ROOT not in sys.path:
    sys.path.insert(0, _QDK_ROOT)

from binance_module.binance_server.backtest import get_local_data


btc_data = get_local_data('btcusdt', 20000)   # BTC/USDT 1小时K线, 2万根, 时间升序
eth_data = get_local_data('ethusdt', 20000)   # ETH/USDT 1小时K线


def crypto_env_df(df):
    """把原始K线 df 适配成 StocksEnv 可用的格式:
    - 列名小写 ohlc → 首字母大写(环境只认 'Close')
    - 丢弃含 NaN 的行, 重置为连续整数索引(frame_bound 按位置切片)
    """
    out = df.rename(columns={'open': 'Open', 'close': 'Close',
                             'high': 'High', 'low': 'Low'}).dropna().reset_index(drop=True)
    return out

if __name__ == '__main__':
    print(btc_data)