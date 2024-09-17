import streamlit as st
import yfinance as yf
import mplfinance as mpf

st.markdown("# 株価チャート")

#パラメータ設定
name = st.sidebar.selectbox('銘柄選択', ['日経平均株価'], index=0)
interval = st.sidebar.selectbox('interval', ['1d'], index=0)
value1 = st.sidebar.slider('period', 0, 300, 30)
period = str(value1)+'d'

title = '## 日経平均株価'
ticker = '^N225'

st.markdown(title)

#データを収集
data = yf.download(ticker , period=period, interval=interval)
data_yesterday = yf.download(ticker , period='2d', interval='1d')

#最新値表示
value = data.iloc[-1,3]
delta = data.iloc[-1,3] - data_yesterday.iloc[0,3]

st.metric(label=data.index[-1].strftime("%Y/%m/%d"), value=f'{value:,.2f}円', delta=f'{delta:,.2f}円')

#グラフ表示
st.write(data.index[0].strftime("%Y/%m/%d")+' - '+data.index[-1].strftime("%Y/%m/%d"))
fig = mpf.plot(data, type="candle",volume=True, mav=(5,21))
st.set_option('deprecation.showPyplotGlobalUse', False)

st.pyplot(fig)

#データ表示
st.dataframe(data.sort_values('Date', ascending=False), height=500)
