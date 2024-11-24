import streamlit as st
import pandas as pd
from collections import Counter
from datetime import datetime

data_array = [
  ['2022-12-09 18:00:00', '5486'],
  ['2022-12-12 18:00:00', '5641'],
  ['2022-12-13 18:00:00', '1500'],
  ['2022-12-14 18:00:00', '5369'],
  ['2022-12-15 18:00:00', '3692'],
  ['2022-12-16 18:00:00', '9428'],
  ['2022-12-19 18:00:00', '9184'],
  ['2022-12-20 18:00:00', '9853'],
  ['2022-12-21 18:00:00', '3522'],
  ['2022-12-22 18:00:00', '7879'],
  ['2022-12-23 18:00:00', '6694'],
  ['2022-12-26 18:00:00', '3898'],
  ['2022-12-27 18:00:00', '2131'],
  ['2022-12-28 18:00:00', '5953'],
  ['2022-12-29 18:00:00', '0335'],
  ['2022-12-30 18:00:00', '2572'],
  ['2023-01-04 18:00:00', '5409'],
  ['2023-01-05 18:00:00', '3592'],
  ['2023-01-06 18:00:00', '2652'],
  ['2023-01-09 18:00:00', '0395'],
  ['2023-01-10 18:00:00', '4608'],
  ['2023-01-11 18:00:00', '1751'],
  ['2023-01-12 18:00:00', '9702'],
  ['2023-01-13 18:00:00', '6233'],
  ['2023-01-16 18:00:00', '5925'],
  ['2023-01-17 18:00:00', '0525'],
  ['2023-01-18 18:00:00', '4462'],
  ['2023-01-19 18:00:00', '3013'],
  ['2023-01-20 18:00:00', '2203'],
  ['2023-01-23 18:00:00', '1349'],
  ['2023-01-24 18:00:00', '8428'],
  ['2023-01-25 18:00:00', '5224'],
  ['2023-01-26 18:00:00', '7248'],
  ['2023-01-27 18:00:00', '5238'],
  ['2023-01-30 18:00:00', '9034'],
  ['2023-01-31 18:00:00', '0457'],
  ['2023-02-01 18:00:00', '1781'],
  ['2023-02-02 18:00:00', '1766'],
  ['2023-02-03 18:00:00', '0534'],
  ['2023-02-06 18:00:00', '4509'],
  ['2023-02-07 18:00:00', '2697'],
  ['2023-02-08 18:00:00', '0990'],
  ['2023-02-09 18:00:00', '4810'],
  ['2023-02-10 18:00:00', '9414'],
  ['2023-02-13 18:00:00', '2577'],
  ['2023-02-14 18:00:00', '1137'],
  ['2023-02-15 18:00:00', '3489'],
  ['2023-02-16 18:00:00', '9168'],
  ['2023-02-17 18:00:00', '8414'],
  ['2023-02-20 18:00:00', '9127'],
  ['2023-02-21 18:00:00', '0018'],
  ['2023-02-22 18:00:00', '7517'],
  ['2023-02-23 18:00:00', '1156'],
  ['2023-02-24 18:00:00', '3307'],
  ['2023-02-27 18:00:00', '3107'],
  ['2023-02-28 18:00:00', '7188'],
  ['2023-03-01 18:00:00', '4985'],
  ['2023-03-02 18:00:00', '8568'],
  ['2023-03-03 18:00:00', '2006'],
  ['2023-03-06 18:00:00', '9748'],
  ['2023-03-07 18:00:00', '8386'],
  ['2023-03-08 18:00:00', '3482'],
  ['2023-03-09 18:00:00', '2140'],
  ['2023-03-10 18:00:00', '8682'],
  ['2023-03-13 18:00:00', '3588'],
  ['2023-03-14 18:00:00', '7497'],
  ['2023-03-15 18:00:00', '7052'],
  ['2023-03-16 18:00:00', '6366'],
  ['2023-03-17 18:00:00', '2046'],
  ['2023-03-20 18:00:00', '8344'],
  ['2023-03-21 18:00:00', '4163'],
  ['2023-03-22 18:00:00', '0932'],
  ['2023-03-23 18:00:00', '4439'],
  ['2023-03-24 18:00:00', '4243'],
  ['2023-03-27 18:00:00', '1614'],
  ['2023-03-28 18:00:00', '9526'],
  ['2023-03-29 18:00:00', '2389'],
  ['2023-03-30 18:00:00', '3025'],
  ['2023-03-31 18:00:00', '9631'],
  ['2023-04-03 18:00:00', '7815'],
  ['2023-04-04 18:00:00', '8705'],
  ['2023-04-05 18:00:00', '7211'],
  ['2023-04-06 18:00:00', '0317'],
  ['2023-04-07 18:00:00', '1962'],
  ['2023-04-10 18:00:00', '4855'],
  ['2023-04-11 18:00:00', '2617'],
  ['2023-04-12 18:00:00', '6651'],
  ['2023-04-13 18:00:00', '3959'],
  ['2023-04-14 18:00:00', '9788'],
  ['2023-04-17 18:00:00', '8297'],
  ['2023-04-18 18:00:00', '3466'],
  ['2023-04-19 18:00:00', '6655'],
  ['2023-04-20 18:00:00', '0120'],
  ['2023-04-21 18:00:00', '2371'],
  ['2023-04-24 18:00:00', '1679'],
  ['2023-04-25 18:00:00', '6602'],
  ['2023-04-26 18:00:00', '2613'],
  ['2023-04-27 18:00:00', '2784'],
  ['2023-04-28 18:00:00', '6083'],
  ['2023-05-01 18:00:00', '2806'],
  ['2023-05-02 18:00:00', '3159'],
  ['2023-05-03 18:00:00', '5658'],
  ['2023-05-04 18:00:00', '3084'],
  ['2023-05-05 18:00:00', '2558'],
  ['2023-05-08 18:00:00', '2954'],
  ['2023-05-09 18:00:00', '8977'],
  ['2023-05-10 18:00:00', '3712'],
  ['2023-05-11 18:00:00', '0048'],
  ['2023-05-12 18:00:00', '2494'],
  ['2023-05-15 18:00:00', '7211'],
  ['2023-05-16 18:00:00', '5158'],
  ['2023-05-17 18:00:00', '6987'],
  ['2023-05-18 18:00:00', '9262'],
  ['2023-05-19 18:00:00', '8990'],
  ['2023-05-22 18:00:00', '7143'],
  ['2023-05-23 18:00:00', '9826'],
  ['2023-05-24 18:00:00', '4645'],
  ['2023-05-25 18:00:00', '9918'],
  ['2023-05-26 18:00:00', '1742'],
  ['2023-05-29 18:00:00', '0247'],
  ['2023-05-30 18:00:00', '7906'],
  ['2023-05-31 18:00:00', '1246'],
  ['2023-06-01 18:00:00', '7494'],
  ['2023-06-02 18:00:00', '1880'],
  ['2023-06-05 18:00:00', '8034'],
  ['2023-06-06 18:00:00', '1308'],
  ['2023-06-07 18:00:00', '6843'],
  ['2023-06-08 18:00:00', '0503'],
  ['2023-06-09 18:00:00', '2776'],
  ['2023-06-12 18:00:00', '1360'],
  ['2023-06-13 18:00:00', '7421'],
  ['2023-06-14 18:00:00', '9894'],
  ['2023-06-15 18:00:00', '6776'],
  ['2023-06-16 18:00:00', '2362'],
  ['2023-06-19 18:00:00', '0299'],
  ['2023-06-20 18:00:00', '8127'],
  ['2023-06-21 18:00:00', '1170'],
  ['2023-06-22 18:00:00', '4952'],
  ['2023-06-23 18:00:00', '7452'],
  ['2023-06-26 18:00:00', '4586'],
  ['2023-06-27 18:00:00', '5103'],
  ['2023-06-28 18:00:00', '1899'],
  ['2023-06-29 18:00:00', '9098'],
  ['2023-06-30 18:00:00', '2774'],
  ['2023-07-03 18:00:00', '8164'],
  ['2023-07-04 18:00:00', '3899'],
  ['2023-07-05 18:00:00', '8446'],
  ['2023-07-06 18:00:00', '8092'],
  ['2023-07-07 18:00:00', '2903'],
  ['2023-07-10 18:00:00', '2799'],
  ['2023-07-11 18:00:00', '8766'],
  ['2023-07-12 18:00:00', '0179'],
  ['2023-07-13 18:00:00', '4647'],
  ['2023-07-14 18:00:00', '2175'],
  ['2023-07-17 18:00:00', '9760'],
  ['2023-07-18 18:00:00', '5241'],
  ['2023-07-19 18:00:00', '3416'],
  ['2023-07-20 18:00:00', '2247'],
  ['2023-07-21 18:00:00', '9334'],
  ['2023-07-24 18:00:00', '1121'],
  ['2023-07-25 18:00:00', '9793'],
  ['2023-07-26 18:00:00', '5867'],
  ['2023-07-27 18:00:00', '2882'],
  ['2023-07-28 18:00:00', '8071'],
  ['2023-07-31 18:00:00', '8549'],
  ['2023-08-01 18:00:00', '7169'],
  ['2023-08-02 18:00:00', '3090'],
  ['2023-08-03 18:00:00', '3805'],
  ['2023-08-04 18:00:00', '0369'],
  ['2023-08-07 18:00:00', '5294'],
  ['2023-08-08 18:00:00', '9566'],
  ['2023-08-09 18:00:00', '5069'],
  ['2023-08-10 18:00:00', '3793'],
  ['2023-08-11 18:00:00', '1226'],
  ['2023-08-14 18:00:00', '5897'],
  ['2023-08-15 18:00:00', '5677'],
  ['2023-08-16 18:00:00', '5054'],
  ['2023-08-17 18:00:00', '1697'],
  ['2023-08-18 18:00:00', '7425'],
  ['2023-08-21 18:00:00', '5517'],
  ['2023-08-22 18:00:00', '4537'],
  ['2023-08-23 18:00:00', '3295'],
  ['2023-08-24 18:00:00', '7780'],
  ['2023-08-25 18:00:00', '8597'],
  ['2023-08-28 18:00:00', '0855'],
  ['2023-08-29 18:00:00', '1308'],
  ['2023-08-30 18:00:00', '8393'],
  ['2023-08-31 18:00:00', '4044'],
  ['2023-09-01 18:00:00', '5286'],
  ['2023-09-04 18:00:00', '1434'],
  ['2023-09-05 18:00:00', '1115'],
  ['2023-09-06 18:00:00', '2988'],
  ['2023-09-07 18:00:00', '9398'],
  ['2023-09-08 18:00:00', '6470'],
  ['2023-09-11 18:00:00', '1134'],
  ['2023-09-12 18:00:00', '1108'],
  ['2023-09-13 18:00:00', '6372'],
  ['2023-09-14 18:00:00', '0402'],
  ['2023-09-15 18:00:00', '7219'],
  ['2023-09-18 18:00:00', '8587'],
  ['2023-09-19 18:00:00', '3914'],
  ['2023-09-20 18:00:00', '0003'],
  ['2023-09-21 18:00:00', '3400'],
  ['2023-09-22 18:00:00', '7384'],
  ['2023-09-25 18:00:00', '5563'],
  ['2023-09-26 18:00:00', '2668'],
  ['2023-09-27 18:00:00', '5367'],
  ['2023-09-28 18:00:00', '5662'],
  ['2023-09-29 18:00:00', '8286'],
  ['2023-10-02 18:00:00', '6183'],
  ['2023-10-03 18:00:00', '5384'],
  ['2023-10-04 18:00:00', '2959'],
  ['2023-10-05 18:00:00', '8461'],
  ['2023-10-06 18:00:00', '8305'],
  ['2023-10-09 18:00:00', '6283'],
  ['2023-10-10 18:00:00', '5048'],
  ['2023-10-11 18:00:00', '6301'],
  ['2023-10-12 18:00:00', '2277'],
  ['2023-10-13 18:00:00', '5997'],
  ['2023-10-16 18:00:00', '9304'],
  ['2023-10-17 18:00:00', '7379'],
  ['2023-10-18 18:00:00', '1598'],
  ['2023-10-19 18:00:00', '2762'],
  ['2023-10-20 18:00:00', '3302'],
  ['2023-10-23 18:00:00', '8282'],
  ['2023-10-24 18:00:00', '3461'],
  ['2023-10-25 18:00:00', '7059'],
  ['2023-10-26 18:00:00', '1954'],
  ['2023-10-27 18:00:00', '1763'],
  ['2023-10-30 18:00:00', '1487'],
  ['2023-10-31 18:00:00', '0945'],
  ['2023-11-01 18:00:00', '0469'],
  ['2023-11-02 18:00:00', '3388'],
  ['2023-11-03 18:00:00', '5764'],
  ['2023-11-06 18:00:00', '3933'],
  ['2023-11-07 18:00:00', '3861'],
  ['2023-11-08 18:00:00', '1559'],
  ['2023-11-09 18:00:00', '0231'],
  ['2023-11-10 18:00:00', '7197'],
  ['2023-11-13 18:00:00', '6154'],
  ['2023-11-14 18:00:00', '7277'],
  ['2023-11-15 18:00:00', '6562'],
  ['2023-11-16 18:00:00', '3989'],
  ['2023-11-17 18:00:00', '2111'],
  ['2023-11-20 18:00:00', '8867'],
  ['2023-11-21 18:00:00', '2930'],
  ['2023-11-22 18:00:00', '6977'],
  ['2023-11-23 18:00:00', '1239'],
  ['2023-11-24 18:00:00', '9198'],
  ['2023-11-27 18:00:00', '0271'],
  ['2023-11-28 18:00:00', '4077'],
  ['2023-11-29 18:00:00', '2317'],
  ['2023-11-30 18:00:00', '1184'],
  ['2023-12-01 18:00:00', '5892'],
  ['2023-12-04 18:00:00', '7648'],
  ['2023-12-05 18:00:00', '1304'],
  ['2023-12-06 18:00:00', '5235'],
  ['2023-12-07 18:00:00', '6529'],
  ['2023-12-08 18:00:00', '5751'],
  ['2023-12-11 18:00:00', '3872'],
  ['2023-12-12 18:00:00', '0959'],
  ['2023-12-13 18:00:00', '2487'],
  ['2023-12-14 18:00:00', '1228'],
  ['2023-12-15 18:00:00', '8284'],
  ['2023-12-18 18:00:00', '9116'],
  ['2023-12-19 18:00:00', '8696'],
  ['2023-12-20 18:00:00', '6147'],
  ['2023-12-21 18:00:00', '2870'],
  ['2023-12-22 18:00:00', '2986'],
  ['2023-12-25 18:00:00', '9134'],
  ['2023-12-26 18:00:00', '2473'],
  ['2023-12-27 18:00:00', '0942'],
  ['2023-12-28 18:00:00', '8104'],
  ['2023-12-29 18:00:00', '0377'],
  ['2024-01-04 18:00:00', '7405'],
  ['2024-01-05 18:00:00', '5170'],
  ['2024-01-08 18:00:00', '4587'],
  ['2024-01-09 18:00:00', '1610'],
  ['2024-01-10 18:00:00', '7124'],
  ['2024-01-11 18:00:00', '9214'],
  ['2024-01-12 18:00:00', '0944'],
  ['2024-01-15 18:00:00', '0080'],
  ['2024-01-16 18:00:00', '8895'],
  ['2024-01-17 18:00:00', '2293'],
  ['2024-01-18 18:00:00', '2864'],
  ['2024-01-19 18:00:00', '8095'],
  ['2024-01-22 18:00:00', '2651'],
  ['2024-01-23 18:00:00', '8913'],
  ['2024-01-24 18:00:00', '2199'],
  ['2024-01-25 18:00:00', '3648'],
  ['2024-01-26 18:00:00', '4108'],
  ['2024-01-29 18:00:00', '9353'],
  ['2024-01-30 18:00:00', '2137'],
  ['2024-01-31 18:00:00', '6806'],
  ['2024-02-01 18:00:00', '9358'],
  ['2024-02-02 18:00:00', '4692'],
  ['2024-02-05 18:00:00', '6724'],
  ['2024-02-06 18:00:00', '3003'],
  ['2024-02-07 18:00:00', '9372'],
  ['2024-02-08 18:00:00', '0006'],
  ['2024-02-09 18:00:00', '5389'],
  ['2024-02-12 18:00:00', '0045'],
  ['2024-02-13 18:00:00', '0710'],
  ['2024-02-14 18:00:00', '7229'],
  ['2024-02-15 18:00:00', '7029'],
  ['2024-02-16 18:00:00', '4208'],
  ['2024-02-19 18:00:00', '7390'],
  ['2024-02-20 18:00:00', '0042'],
  ['2024-02-21 18:00:00', '2361'],
  ['2024-02-22 18:00:00', '7519'],
  ['2024-02-23 18:00:00', '5651'],
  ['2024-02-26 18:00:00', '6864'],
  ['2024-02-27 18:00:00', '5868'],
  ['2024-02-28 18:00:00', '0825'],
  ['2024-02-29 18:00:00', '9550'],
  ['2024-03-01 18:00:00', '3560'],
  ['2024-03-04 18:00:00', '4511'],
  ['2024-03-05 18:00:00', '9892'],
  ['2024-03-06 18:00:00', '9482'],
  ['2024-03-07 18:00:00', '6822'],
  ['2024-03-08 18:00:00', '8763'],
  ['2024-03-11 18:00:00', '7468'],
  ['2024-03-12 18:00:00', '9146'],
  ['2024-03-13 18:00:00', '0017'],
  ['2024-03-14 18:00:00', '6599'],
  ['2024-03-15 18:00:00', '3988'],
  ['2024-03-18 18:00:00', '5004'],
  ['2024-03-19 18:00:00', '5961'],
  ['2024-03-20 18:00:00', '6496'],
  ['2024-03-21 18:00:00', '3237'],
  ['2024-03-22 18:00:00', '5485'],
  ['2024-03-25 18:00:00', '0224'],
  ['2024-03-26 18:00:00', '2814'],
  ['2024-03-27 18:00:00', '4360'],
  ['2024-03-28 18:00:00', '3918'],
  ['2024-03-29 18:00:00', '8399'],
  ['2024-04-01 18:00:00', '3489'],
  ['2024-04-02 18:00:00', '4591'],
  ['2024-04-03 18:00:00', '8640'],
  ['2024-04-04 18:00:00', '6280'],
  ['2024-04-05 18:00:00', '3364'],
  ['2024-04-08 18:00:00', '2743'],
  ['2024-04-09 18:00:00', '1002'],
  ['2024-04-10 18:00:00', '4170'],
  ['2024-04-11 18:00:00', '2518'],
  ['2024-04-12 18:00:00', '8158'],
  ['2024-04-15 18:00:00', '0597'],
  ['2024-04-16 18:00:00', '5845'],
  ['2024-04-17 18:00:00', '3563'],
  ['2024-04-18 18:00:00', '3690'],
  ['2024-04-19 18:00:00', '0207'],
  ['2024-04-22 18:00:00', '1459'],
  ['2024-04-23 18:00:00', '9319'],
  ['2024-04-24 18:00:00', '7874'],
  ['2024-04-25 18:00:00', '6118'],
  ['2024-04-26 18:00:00', '7210'],
  ['2024-04-29 18:00:00', '0040'],
  ['2024-04-30 18:00:00', '3275'],
  ['2024-05-01 18:00:00', '6135'],
  ['2024-05-02 18:00:00', '7987'],
  ['2024-05-03 18:00:00', '1323'],
  ['2024-05-06 18:00:00', '9100'],
  ['2024-05-07 18:00:00', '3360'],
  ['2024-05-08 18:00:00', '1361'],
  ['2024-05-09 18:00:00', '8593'],
  ['2024-05-10 18:00:00', '6965'],
  ['2024-05-13 18:00:00', '2064'],
  ['2024-05-14 18:00:00', '7167'],
  ['2024-05-15 18:00:00', '7965'],
  ['2024-05-16 18:00:00', '6877'],
  ['2024-05-17 18:00:00', '1380'],
  ['2024-05-20 18:00:00', '8588'],
  ['2024-05-21 18:00:00', '4677'],
  ['2024-05-22 18:00:00', '8006'],
  ['2024-05-23 18:00:00', '4656'],
  ['2024-05-24 18:00:00', '5201'],
  ['2024-05-27 18:00:00', '5737'],
  ['2024-05-28 18:00:00', '3618'],
  ['2024-05-29 18:00:00', '3644'],
  ['2024-05-30 18:00:00', '5782'],
  ['2024-05-31 18:00:00', '1469'],
  ['2024-06-03 18:00:00', '9947'],
  ['2024-06-04 18:00:00', '5930'],
  ['2024-06-05 18:00:00', '9656'],
  ['2024-06-06 18:00:00', '2384'],
  ['2024-06-07 18:00:00', '9143'],
  ['2024-06-10 18:00:00', '0348'],
  ['2024-06-11 18:00:00', '9400'],
  ['2024-06-12 18:00:00', '4011'],
  ['2024-06-13 18:00:00', '1691'],
  ['2024-06-14 18:00:00', '5505'],
  ['2024-06-17 18:00:00', '5640'],
  ['2024-06-18 18:00:00', '2045'],
  ['2024-06-19 18:00:00', '2646'],
  ['2024-06-20 18:00:00', '2322'],
  ['2024-06-21 18:00:00', '6593'],
  ['2024-06-24 18:00:00', '2049'],
  ['2024-06-25 18:00:00', '8337'],
  ['2024-06-26 18:00:00', '7556'],
  ['2024-06-27 18:00:00', '2552'],
  ['2024-06-28 18:00:00', '7285'],
  ['2024-07-01 18:00:00', '6836'],
  ['2024-07-02 18:00:00', '5240'],
  ['2024-07-03 18:00:00', '4896'],
  ['2024-07-04 18:00:00', '4365'],
  ['2024-07-05 18:00:00', '6715'],
  ['2024-07-08 18:00:00', '2208'],
  ['2024-07-09 18:00:00', '9108'],
  ['2024-07-10 18:00:00', '7132'],
  ['2024-07-11 18:00:00', '5209'],
  ['2024-07-12 18:00:00', '9345'],
  ['2024-07-15 18:00:00', '8023'],
  ['2024-07-16 18:00:00', '7487'],
  ['2024-07-17 18:00:00', '2710'],
  ['2024-07-18 18:00:00', '6232'],
  ['2024-07-19 18:00:00', '4044'],
  ['2024-07-22 18:00:00', '9282'],
  ['2024-07-23 18:00:00', '2827'],
  ['2024-07-24 18:00:00', '6533'],
  ['2024-07-25 18:00:00', '2254'],
  ['2024-07-26 18:00:00', '4387'],
  ['2024-07-29 18:00:00', '0780'],
  ['2024-07-30 18:00:00', '3787'],
  ['2024-07-31 18:00:00', '1417'],
  ['2024-08-01 18:00:00', '9118'],
  ['2024-08-02 18:00:00', '0793'],
  ['2024-08-05 18:00:00', '1951'],
  ['2024-08-06 18:00:00', '7007'],
  ['2024-08-07 18:00:00', '5624'],
  ['2024-08-08 18:00:00', '8115'],
  ['2024-08-09 18:00:00', '8424'],
  ['2024-08-12 18:00:00', '9533'],
  ['2024-08-13 18:00:00', '4167'],
  ['2024-08-14 18:00:00', '1770'],
  ['2024-08-15 18:00:00', '3966'],
  ['2024-08-16 18:00:00', '1799'],
  ['2024-08-19 18:00:00', '2057'],
  ['2024-08-20 18:00:00', '0358'],
  ['2024-08-21 18:00:00', '8412'],
  ['2024-08-22 18:00:00', '4618'],
  ['2024-08-23 18:00:00', '1604'],
  ['2024-08-26 18:00:00', '7237'],
  ['2024-08-27 18:00:00', '2390'],
  ['2024-08-28 18:00:00', '6008'],
  ['2024-08-29 18:00:00', '1491'],
  ['2024-08-30 18:00:00', '9909'],
  ['2024-09-02 18:00:00', '0205'],
  ['2024-09-03 18:00:00', '9141'],
  ['2024-09-04 18:00:00', '7828'],
  ['2024-09-05 18:00:00', '1910'],
  ['2024-09-06 18:00:00', '7889'],
  ['2024-09-09 18:00:00', '5705'],
  ['2024-09-10 18:00:00', '5740'],
  ['2024-09-11 18:00:00', '4835'],
  ['2024-09-12 18:00:00', '1130'],
  ['2024-09-13 18:00:00', '7056'],
  ['2024-09-16 18:00:00', '3232'],
  ['2024-09-17 18:00:00', '4601'],
  ['2024-09-18 18:00:00', '3848'],
  ['2024-09-19 18:00:00', '2796'],
  ['2024-09-20 18:00:00', '6411'],
  ['2024-09-23 18:00:00', '2095'],
  ['2024-09-24 18:00:00', '5794'],
  ['2024-09-25 18:00:00', '3119'],
  ['2024-09-26 18:00:00', '4488'],
  ['2024-09-27 18:00:00', '5225'],
  ['2024-09-30 18:00:00', '5211'],
  ['2024-10-01 18:00:00', '0605'],
  ['2024-10-02 18:00:00', '9563'],
  ['2024-10-03 18:00:00', '9299'],
  ['2024-10-04 18:00:00', '0784'],
  ['2024-10-07 18:00:00', '5812'],
  ['2024-10-08 18:00:00', '8903'],
  ['2024-10-09 18:00:00', '1319'],
  ['2024-10-10 18:00:00', '0946'],
  ['2024-10-11 18:00:00', '5126'],
  ['2024-10-14 18:00:00', '3661'],
  ['2024-10-15 18:00:00', '5667'],
  ['2024-10-16 18:00:00', '8407'],
  ['2024-10-17 18:00:00', '2004'],
  ['2024-10-18 18:00:00', '8921'],
  ['2024-10-21 18:00:00', '9546'],
  ['2024-10-22 18:00:00', '7178'],
  ['2024-10-23 18:00:00', '5665'],
  ['2024-10-24 18:00:00', '4428'],
  ['2024-10-25 18:00:00', '7675'],
  ['2024-10-28 18:00:00', '2405'],
  ['2024-10-29 18:00:00', '1995'],
  ['2024-10-30 18:00:00', '1133'],
  ['2024-10-31 18:00:00', '4059'],
  ['2024-11-01 18:00:00', '5709'],
  ['2024-11-04 18:00:00', '4412'],
  ['2024-11-05 18:00:00', '2667'],
  ['2024-11-06 18:00:00', '7143'],
  ['2024-11-07 18:00:00', '0313'],
  ['2024-11-08 18:00:00', '8888'],
  ['2024-11-11 18:00:00', '3369'],
  ['2024-11-12 18:00:00', '0206'],
  ['2024-11-13 18:00:00', '3005'],
  ['2024-11-14 18:00:00', '3952'],
  ['2024-11-15 18:00:00', '3631'],
  ['2024-11-18 18:00:00', '5730'],
  ['2024-11-19 18:00:00', '1088'],
  ['2024-11-20 18:00:00', '7649'],
  ['2024-11-21 18:00:00', '3340'],
  ['2024-11-22 18:00:00', '2532'],
]

# データをDataFrameに変換
df = pd.DataFrame(data_array, columns=['timestamp', 'number'])
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 4桁の数字を個別の数字に分解
df['digits'] = df['number'].astype(str).str.zfill(4).apply(list)

st.title('4桁数字解析アプリ')

# 4つの数字の検索機能
if st.button('4つの数字を検索'):
    st.write(df[['timestamp', 'number']])

# 各数字のtimestampごとの出現回数
if st.button('各数字のtimestampごとの出現回数'):
    for timestamp, group in df.groupby('timestamp'):
        st.write(f"Timestamp: {timestamp}")
        digit_counts = Counter([int(digit) for digits in group['digits'] for digit in digits])
        st.write(dict(digit_counts))
        st.write("---")

# 各数字のトータルの出現回数
if st.button('各数字のトータルの出現回数'):
    total_counts = Counter([int(digit) for digits in df['digits'] for digit in digits])
    st.write(dict(total_counts))

# ユーザーが指定した数字の重複回数の割合
selected_digit = st.selectbox('数字を選択してください', range(10))

if st.button('選択した数字の重複割合'):
    results = []
    for timestamp, group in df.groupby('timestamp'):
        digit_counts = Counter([int(digit) for digits in group['digits'] for digit in digits])
        total_digits = sum(digit_counts.values())
        selected_count = digit_counts[selected_digit]
        percentage = (selected_count / total_digits) * 100 if total_digits > 0 else 0
        results.append({
            'timestamp': timestamp,
            'count': selected_count,
            'percentage': percentage
        })
    
    result_df = pd.DataFrame(results)
    st.write(result_df)

    # 結果をグラフで表示
    st.line_chart(result_df.set_index('timestamp')['percentage'])