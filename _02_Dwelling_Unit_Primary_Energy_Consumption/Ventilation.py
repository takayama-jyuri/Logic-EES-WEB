
# coding: utf-8

# In[1]:

import math
from enum import Enum
import Life_Schedule as LS


# # Chapter V Ventilation System / 換気設備の計算方法

# ## 1. Introduction

# This calculation depends on the specification of "Chapter V Ventilation System" in BRI.

# ## 2. Enum Type

# In[2]:

class VentilationType(Enum):
    Duct1_HEX = "Duct1_HEX" # ダクト式第一種換気設備（熱交換型換気設備）
    Duct1     = "Duct1"     # ダクト式第一種換気設備
    Duct2     = "Duct2"     # ダクト式第二種換気設備
    Duct3     = "Duct3"     # ダクト式第三種換気設備
    Wall1_HEX = "Wall1_HEX" # 壁付け式第一種換気設備（熱交換型換気設備）
    Wall1     = "Wall1"     # 壁付け式第一種換気設備
    Wall2     = "Wall2"     # 壁付け式第二種換気設備
    Wall3     = "Wall3"     # 壁付け式第三種換気設備


# In[3]:

class EnergySavingMethod(Enum):
    Over75mm_DC = "Over75mm_DC" # 内径75mm以上のダクトのみ使用、直流
    Over75mm_AC = "Over75mm_AC" # 内径75mm以上のダクトのみ使用、交流、又は直流と交流の併用
    Others      = "Others"      # 上記以外


# ## 3. Functions

# ### 3.1. Electric Power of Mechanical Ventilation System / 機械換気設備の消費電力量

# $$
# \displaystyle E_{E,V} = E_{E,VG} + E_{E,VL}
# $$

# Where  
# $ E_{E,V} $ is the horly electric power of mechanical ventilation system / 1時間当たりの機械換気設備の消費電力量 (kWh/h);  
# $ E_{E,VG} $ is the hourly electric power of general mecanical ventilation system / 1時間当たりの全般換気設備の消費電力量 (kWh/h);    
# $ E_{E,VL} $ is the hourly electric power of local mechanical ventilation system / 1時間当たりの局所換気設備の消費電力量 (kWh/h).

# In[4]:

def get_E_E_V(E_E_VG, E_E_VL):
    return E_E_VG + E_E_VL


# #### Example

# $ E_{E,VG} $ = 0.3 (kWh/h)  
# $ E_{E,VL} $ = 0.1 (kWh/h)

# In[5]:

get_E_E_V(0.3, 0.1)


# ### 3.2 Electric Power of General Mechanical Ventilation System / 全般換気設備の消費電力量

# $$
# E_{E,VG} = f_{SFP} \times V_R \times 10^{-3}
# $$

# Where  
# $ E_{E,VG} $ is the hourly electric power of general mecanical ventilation system / 1時間当たりの全般換気設備の消費電力量 (kWh/h);    
# $ f_{SFP} $ is the SFP ( specific Fan Power ) of general mechanical ventilation system / 全般換気設備の比消費電力 (W/(m<sup>3</sup>/h));  
# $ V_R $ is the referenced ventilation amount of general mechanical ventilation system / 全般換気設備の参照機械換気量 (m<sup>3</sup>/h).

# In[6]:

def get_E_E_VG(f_SFP, V_R):
    return f_SFP * V_R * 10**(-3)


# #### Example

# $ f_{SFP} $ = 0.3 (W/(m<sup>3</sup>/h))  
# $ V_R $ = 3.5 (m<sup>3</sup>/h)

# In[7]:

get_E_E_VG(0.3, 3.5)


# ### 3.3 Referenced Amount of Mechanical Ventilation System / 全般換気設備の参照機械換気量

# $$
# V_R = A_A \times H_R \times N \times a \div e
# $$

# Where  
# $ V_R $ is the referenced ventilation amount of general mechanical ventilation system / 全般換気設備の参照機械換気量 (m<sup>3</sup>/h):  
# $ A_A $ is the floor area / 床面積の合計 (m<sup>2</sup>);  
# $ H_R $ is the referenced ceiling height / 参照天井高さ (m)(=2.4m);  
# $ N $ is the ventilation rate / 換気回数 (1/h);  
# $ a $ is the allowance ratio of the ventilation amount of the general mechanical ventilation system / 全般換気設備の換気量の余裕率 (=1.1);  
# $ e $ is the effective ventilation ratio / 有効換気量率.

# In[8]:

def get_V_R(A_A, N, e):
    H_R = 2.4 # 参照天井高さ(m)
    a = 1.1 # 全般換気設備の換気量の余裕率
    return A_A * H_R * N * a / e


# #### Example

# $A_A$ = 10.0 (m<sup>2</sup>)  
# $N$ = 5.0 (1/h)  
# $e$ = 1.0

# In[9]:

get_V_R(10.0, 5.0, 1.0)


# ### 3.4 Specific Fan Power / 比消費電力

# The specific fan power is calculated based on the following (a) and (b).  

# #### (a) Calculation based on Specification / 仕様により計算する方法

# #### (a-1) Ventilation System with Duct / ダクト式換気設備の場合

# $$ f_{SFP} = f_{SFP,basic} \times r_{ES} $$

# $ f_{SFP,basic} $ is the basic SFP, and defined on the table below according to the type of the general mechanical ventilation system.
# 

# | Type of General Ventilation System | Basic SFP |
# | ------------------ | -------------------- |
# | Balanced ventilation system with duct and heat exchanger <br> ダクト式第一種換気設備(熱交換型換気設備) | 0.70 |
# | Balanced ventilation system with duct <br> ダクト式第一種換気設備 | 0.50 |
# | Supply only or exhaust only ventilation system with duct <br> ダクト式第二種換気設備又はダクト式第三種換気設備 | 0.40 |
# 

# In[10]:

def get_basicalSFP_with_Duct_Type(t):
    # t : VentilationType enum型
    return {
        VentilationType.Duct1_HEX : 0.70,
        VentilationType.Duct1     : 0.50, 
        VentilationType.Duct2     : 0.40, 
        VentilationType.Duct3     : 0.40,
    }[t]


# $ r_{ES} $ is the ratio of the effect on the energy saving technique(s) and defined on the table below according to the type of the general mechanical ventilation, the inside diameter of the duct and the type of the moter.
# 

# <table>
# <tr>
#     <th>Type of Ventilation System</th>
#     <th>Inside Diameter of Duct</th>
#     <th>Type of Moter</th>
#     <th>Ratio</th>
# </tr>
# <tr>
#     <td rowspan=3>Balanced ventilation system with duct <br> ダクト式第一種換気設備</td>
#     <td rowspan=2>Use the duct with the inside diameter of more than 75mm <br> 内径75mm以上のダクトのみ使用</td>
#     <td>DC <br> 直流</td>
#     <td>0.455</td>
# </tr>
# <tr>
#     <td>AC or Combined Use of AC and DC <br> 交流、又は直流と交流の併用</td>
#     <td>0.700</td>
# </tr>
# <tr>
#     <td>Others <br> 上記以外</td>
#     <td>DC or AC <br> 直流あるいは交流</td>
#     <td>1.000</td>
# </tr>
# <tr>
#     <td rowspan=3>Supply only or exhaust only ventilation system with duct <br> ダクト式第二種換気設備又はダクト式第三種換気設備</td>
#     <td rowspan=2>Use the duct with the inside diameter of more than 75mm <br> 内径75mm以上のダクトのみ使用</td>
#     <td>DC <br> 直流</td>
#     <td>0.360</td>
# </tr>
# <tr>
#     <td>AC or Combined Use of AC and DC <br> 交流、又は直流と交流の併用</td>
#     <td>0.600</td>
# </tr>
# <tr>
#     <td>Others <br> 上記以外</td>
#     <td>DC or AC <br> 直流あるいは交流</td>
#     <td>1.000</td>
# </tr>
# </table>

# In[11]:

def get_EnergySavingTechniquesEffectRatio(t, s):
    # t : VentilationType enum型
    # s : EnergySavingMethod enum型
    if t == VentilationType.Duct1 or t == VentilationType.Duct1_HEX:
        EnergySavingDuct1  = { EnergySavingMethod.Over75mm_DC : 0.455,
                               EnergySavingMethod.Over75mm_AC : 0.700,
                               EnergySavingMethod.Others      : 1.000 }
        return EnergySavingDuct1[s]
    elif t == VentilationType.Duct2 or t == VentilationType.Duct3:
        EnergySavingDuct23 = { EnergySavingMethod.Over75mm_DC : 0.360,
                               EnergySavingMethod.Over75mm_AC : 0.600,
                               EnergySavingMethod.Others      : 1.000 }
        return EnergySavingDuct23[s]
    else:
        raise Exception


# #### (a-2) Wall-mounted Ventilation Unit / 壁付け式換気設備の場合

# $ f_{SFP} $ is defined in the table below.
# 
# | Type of Ventilation | SFP |
# | ------------------ | ---------- |
# | Balanced ventilation system with duct and heat exchanger <br> ダクト式第一種換気設備(熱交換型換気設備) | 0.70 |
# | Balanced ventilation system with duct <br> ダクト式第一種換気設備 | 0.40 |
# | Supply onlyventilation system with duct <br> ダクト式第二種換気設備 | 0.30 |
# | Exhaust only ventilation system with duct <br> ダクト式第三種換気設備 | 0.30 |

# In[12]:

def get_SFP_with_Wall_Mounted_Type(t):
    # t : VentilationType enum型
    return {
        VentilationType.Wall1_HEX : 0.70, 
        VentilationType.Wall1     : 0.40, 
        VentilationType.Wall2     : 0.30, 
        VentilationType.Wall3     : 0.30 
    }[t]    


# #### (b) Calculation based on Power and Designed Ventilation Amount / 消費電力と設計風量により求める方法

# $$
# f_{SFP} = P \div V_d
# $$

# Where  
# $ f_{SFP} $ is the SFP ( specific Fan Power ) of general mechanical ventilation system / 全般換気設備の比消費電力 (W/(m<sup>3</sup>/h));  
# $ P $ is the power of the mechanical general ventilation system (W);  
# $ V_d $ is the designed ventilation amount of the mechanical general ventilation system (m<sup>3</sup>/h).  

# In this program, the calculated SFP is as the input. User shall calculate SFP by the another calculation sheet or program.

# In[13]:

def get_SFP(DoesInputSFP, SFP, t, s):
    if DoesInputSFP:
        return SFP
    else:
        if t == VentilationType.Duct1 or t == VentilationType.Duct1_HEX or t == VentilationType.Duct2 or t == VentilationType.Duct3:
            return get_basicalSFP_with_Duct_Type(t) * get_EnergySavingTechniquesEffectRatio(t, s)
        elif t == VentilationType.Wall1 or t == VentilationType.Wall1_HEX or t == VentilationType.Wall2 or t == VentilationType.Wall3:
            return get_SFP_with_Wall_Mounted_Type(t)
        else:
            raise Exception


# #### Example

# SFP = 0.2

# In[14]:

get_SFP(True, 0.2, None, None)


# Type = The supply only ventilation system with duct  
# Inside Diameter of Duct = Use the duct with the inside diameter of more than 75mm  
# Type of Motor = DC

# In[15]:

get_SFP(False, None, VentilationType.Duct2, EnergySavingMethod.Over75mm_DC)


# ### 3.5 Electric Power of Local Mechanical Ventilation System / 局所換気設備の消費電力量

# $$
# E_{E,VL} = \left\{
# \begin{array}{ll}
# E_{E,VL,p} \mid _{p=1} \times \frac{2 - n_p}{2 - 1} + E_{E,VL,p} \mid _{p=2} \times \frac{n_p - 1}{2 - 1} & (1 \leq n_p < 2 )\\
# E_{E,VL,p} \mid _{p=2} \times \frac{3 - n_p}{3 - 2} + E_{E,VL,p} \mid _{p=3} \times \frac{n_p - 2}{3 - 2} & (2 \leq n_p < 3)\\
# E_{E,VL,p} \mid _{p=3} \times \frac{4 - n_p}{4 - 3} + E_{E,VL,p} \mid _{p=3} \times \frac{n_p - 3}{4 - 3} & (3 \leq n_p \leq 4)
# \end{array}
# \right.
# $$

# Where  
# $ E_{E,VL} $ is the hourly electric power of the local ventilation system / 1時間当たりの局所換気設備の消費電力量 (kWh/h);  
# $ E_{E,VL,p} $ is the houlr electric power of the local ventilation system consumed by the p person(s) / 1時間当たりの居住人数がp人における局所換気設備の消費電力量 (kWh/h);  
# $ n_p $ is the vertical number of the ocupant(s) / 仮想居住人数.

# In[16]:

def get_E_E_VL(get_E_E_VL_p, n_p, day, hour):
    if n_p < 1:
        raise Exception('Number of person should not be less than 1 person.')
    elif n_p == 1:
        return get_E_E_VL_p('p1', day, hour)
    elif 1 < n_p < 2:
        return get_E_E_VL_p('p1', day, hour) * (2 - n_p) / (2 - 1) + get_E_E_VL_p('p2', day, hour)  * (n_p - 1) / (2 - 1)
    elif n_p == 2:
        return get_E_E_VL_p('p2', day, hour)
    elif  2 < n_p < 3:
        return get_E_E_VL_p('p2', day, hour) * (3 - n_p) / (3 - 2) + get_E_E_VL_p('p3', day, hour)  * (n_p - 2) / (3 - 2)
    elif n_p == 3:
        return get_E_E_VL_p('p3', day, hour)
    elif  3 < n_p < 4:
        return get_E_E_VL_p('p3', day, hour) * (4 - n_p) / (4 - 3) + get_E_E_VL_p('p4', day, hour)  * (n_p - 3) / (4 - 3)
    elif n_p == 4:
        return get_E_E_VL_p('p4', day, hour)
    else:
        raise Exception('Number of person should not be over 4 persons.')


# #### Example

# get_E_E_VL_p is dummy function
# $n_p$ = 1.4 (persons)  

# In[17]:

get_E_E_VL( lambda p, d, h : { 'p1': 1.0, 'p2': 2.0, 'p3': 3.0, 'p4': 4.0 }[p], 1.4, '1/2', 23)


# Out of range of the number of person ERROR

# In[18]:

def f():
    try:
        get_E_E_VL( lambda p, d, h : { 'p1': 1.0, 'p2': 2.0, 'p3': 3.0, 'p4': 4.0 }[p], 0.9, '1/2', 23)
    except:
        return "ERROR"
f()


# ### 3.6 Houly electric power of the local ventilation system consumed by the p person(s) / 1時間当たりの居住人数がp人における局所換気設備の消費電力量

# The houly electric power of the local ventilation system consumed by the p person(s) $ E_{E,VL,p} $ is defined on the table below acording to the number of the ocupant(s), weekday/holiday and in/not home.  

# <div style="text-align: center;">
#     **table.  the hourly electric power of the local ventilation system(Wh/h)**
# </div>  
# 
# | time <br> (hr) | 1 person<br>weekday　　 | 1 person<br>holiday, not home | 1 person<br>holiday, in home | 2 persons<br>weekday　　 | 2 person<br>holiday, not home | 2 person<br>holiday, in home | 3 person<br>weekday　　 | 3 person<br>holiday, not home | 3 person<br>holiday, in home | 4 person<br>weekday　　 | 4 person<br>holiday, not home | 4 person<br>holiday, in home |
# | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
# | 0:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 1:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 2:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 3:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 4:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 5:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 6:00 | 3.38 | 0.33 | 0.13 | 6.75 | 0.67 | 0.25 | 10.13 | 1.00 | 0.38 | 13.51 | 1.33 | 0.50 |
# | 7:00 | 0.54 | 0.33 | 0.54 | 1.08 | 0.67 | 1.08 | 1.63 | 1.00 | 1.63 | 2.17 | 1.33 | 2.17 |
# | 8:00 | 0.54 | 7.05 | 3.79 | 1.08 | 14.09 | 7.59 | 1.63 | 21.14 | 11.38 | 2.17 | 28.18 | 15.18 |
# | 9:00 | 0.13 | 0.13 | 0.33 | 0.25 | 0.25 | 0.67 | 0.38 | 0.38 | 1.00 | 0.50 | 0.50 | 1.33 |
# | 10:00 | 0.33 | 0.13 | 0.54 | 0.67 | 0.25 | 1.08 | 1.00 | 0.38 | 1.63 | 1.33 | 0.50 | 2.17 |
# | 11:00 | 0.13 | 0.13 | 0.33 | 0.25 | 0.25 | 0.67 | 0.38 | 0.38 | 1.00 | 0.50 | 0.50 | 1.33 |
# | 12:00 | 3.38 | 0.13 | 3.38 | 6.75 | 0.25 | 6.75 | 10.13 | 0.38 | 10.13 | 13.51 | 0.50 | 13.51 |
# | 13:00 | 0.33 | 0.13 | 0.33 | 0.67 | 0.25 | 0.67 | 1.00 | 0.38 | 1.00 | 1.33 | 0.50 | 1.33 |
# | 14:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 15:00 | 0.13 | 0.13 | 0.13 | 0.25 | 0.25 | 0.25 | 0.38 | 0.38 | 0.38 | 0.50 | 0.50 | 0.50 |
# | 16:00 | 0.33 | 0.13 | 0.54 | 0.67 | 0.25 | 1.08 | 1.00 | 0.38 | 1.63 | 1.33 | 0.50 | 2.17 |
# | 17:00 | 0.33 | 0.13 | 6.42 | 0.67 | 0.25 | 12.84 | 1.00 | 0.38 | 19.26 | 1.33 | 0.50 | 25.68 |
# | 18:00 | 6.42 | 0.13 | 6.42 | 12.84 | 0.25 | 12.84 | 19.26 | 0.38 | 19.26 | 25.68 | 0.50 | 25.68 |
# | 19:00 | 6.42 | 0.13 | 0.13 | 12.84 | 0.25 | 0.25 | 19.26 | 0.38 | 0.38 | 25.68 | 0.50 | 0.50 |
# | 20:00 | 0.33 | 0.54 | 0.33 | 0.67 | 1.08 | 0.67 | 1.00 | 1.63 | 1.00 | 1.33 | 2.17 | 1.33 | 
# | 21:00 | 0.33 | 0.33 | 6.28 | 0.67 | 0.67 | 12.56 | 1.00 | 1.00 | 18.84 | 1.33 | 1.33 | 25.12 |
# | 22:00 | 6.28 | 3.52 | 6.49 | 12.56 | 7.03 | 12.98 | 18.84 | 10.55 | 19.47 | 25.12 | 14.06 | 25.95 |
# | 23:00 | 6.70 | 6.28 | 3.31 | 13.39 | 12.56 | 6.61 | 20.09 | 18.84 | 9.92 | 26.79 | 25.12 | 13.23 |

# In[19]:

data = {
         'p1' : {
             LS.SKD_V.W  : [ 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 3.38, 0.54, 0.54, 0.13, 0.33, 0.13, 3.38, 0.33, 0.13, 0.13, 0.33, 0.33, 6.42, 6.42, 0.33, 0.33, 6.28, 6.7 ],
             LS.SKD_V.HA : [ 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.33, 0.33, 7.05, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.54, 0.33, 3.52, 6.28],
             LS.SKD_V.HH : [ 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.54, 3.79, 0.33, 0.54, 0.33, 3.38, 0.33, 0.13, 0.13, 0.54, 6.42, 6.42, 0.13, 0.33, 6.28, 6.49, 3.31]
         },
         'p2' : {
             LS.SKD_V.W  : [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 6.75, 1.08, 1.08, 0.25, 0.67, 0.25, 6.75, 0.67, 0.25, 0.25, 0.67, 0.67,12.84,12.84, 0.67, 0.67,12.56,13.39], 
             LS.SKD_V.HA : [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.67, 0.67,14.09, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1.08, 0.67, 7.03,12.56], 
             LS.SKD_V.HH : [ 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1.08, 7.59, 0.67, 1.08, 0.67, 6.75, 0.67, 0.25, 0.25, 1.08,12.84,12.84, 0.25, 0.67,12.56,12.98, 6.61] 
         },
         'p3' : {
             LS.SKD_V.W  : [ 0.38, 0.38, 0.38, 0.38, 0.38, 0.38,10.13, 1.63, 1.63, 0.38, 1.00, 0.38,10.13, 1.00, 0.38, 0.38, 1.00, 1.00,19.26,19.26, 1.00, 1.00,18.84,20.09],
             LS.SKD_V.HA : [ 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 1.00, 1.00,21.14, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 1.63, 1.00,10.55,18.84],
             LS.SKD_V.HH : [ 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 1.63,11.38, 1.00,10.63, 1.00,10.13, 1.00, 0.38, 0.38, 1.63,19.26,19.26, 0.38, 1.00,18.84,19.47, 9.92]
         },
         'p4' : { 
             LS.SKD_V.W  : [ 0.50, 0.50, 0.50, 0.50, 0.50, 0.50,13.51, 2.17, 2.17, 0.50, 1.33, 0.50,13.51, 1.33, 0.50, 0.50, 1.33, 1.33,25.68,25.68, 1.33, 1.33,25.12,26.79], 
             LS.SKD_V.HA : [ 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 1.33, 1.33,28.18, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 2.17, 1.33,14.06,25.12], 
             LS.SKD_V.HH : [ 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 2.17,15.18, 1.33, 2.17, 1.33,13.51, 1.33, 0.50, 0.50, 2.17,25.68,25.68, 0.50, 1.33,25.12,25.95,13.23] }
       }


# The daily schedule of Ventilation is defined on the table below at chpter 11 section 3.

# In[20]:

def get_E_E_VL_p(person, day, hour):
 
    return data[person][LS.get_Schedule('Ventilation',day)][hour] / 1000


# #### Examples

# 1/2 22:00, 1 person

# In[21]:

get_E_E_VL_p(person = 'p1', day = '1/2', hour = 22 )


# 1/2 22:00, 2 persons

# In[22]:

get_E_E_VL_p(person = 'p2', day = '1/2', hour = 22 )


# ## 4. Integrated Function

# ### 4.1 Input Data

# #### General

# <table>
# <tr>
#     <th>item 1</th>
#     <th>item 2</th>
#     <th>item 3</th>
#     <th>option</th>
# </tr>
# <tr>
#     <td>Basic Information<br>基本情報</td>
#     <td colspan=2>Sum of Floor Area / 床面積の合計</td>
#     <td>(Decimal Value)</td>
# </tr>
# </table>

# #### Input Data

# ````
# DataGeneral = {
#     'AllFloorArea': '' # Decimal Value represented as string
# }
# ````

# #### Ventilation

# <table>
# <tr>
#     <th>item 1</th>
#     <th>item 2</th>
#     <th>item 3</th>
#     <th>option</th>
# </tr>
# <tr>
#     <td rowspan=6>Ventilation System<br>換気設備</td>
#     <td colspan=2>Type / 換気設備の方式</td>
#     <td>1: Duct Type 1 / ダクト式第1種換気設備<br>2: Duct Type 2 or 3 / ダクト式第2種または第3種換気設備<br>3: Wall-mounted Type 1 / 壁付け式第1種換気設備<br>4: Wall-mounted Type 2 or 3 / 壁付け式第2種または第3種換気設備</td>
# </tr>
# <tr>
#     <td rowspan=3>Duct Type / ダクト式</td>
#     <td>Adoption of Energy Saving Method / 省エネルギー対策の有無および種類</td>
#     <td>1: None / 特に省エネルギー対策をしていない<br>2: Evaluate by Selecting Specification / 採用した省エネルギー手法を選択する<br>3: Evaluate by SFP / 比消費電力を入力することにより省エネルギー効果を評価する</td>
# </tr>
# <tr>
#     <td>Energy Saving Method / 採用する省エネルギー手法</td>
#     <td>1: Use Duct with Large Diameter / 径の太いダクトを使用する<br>2: Use Duct with Large Diameter and DC Moter / 径の太いダクトを採用し、かつDCモーターを採用する</td>
# </tr>
# <tr>
#     <td>SFP / 比消費電力を入力する</td>
#     <td>(Decimal Value)</td>
# </tr>
# <tr>
#     <td rowspan=2>Wall-mounted Type / 壁付け式</td>
#     <td>Adoption of Energy Saving Method / 省エネルギー対策の有無および種類</td>
#     <td>1: None / 特に省エネルギー対策をしていない<br>2: Evaluate by SFP / 比消費電力を入力することにより省エネルギー効果を評価する</td>
# </tr>
# <tr>
#     <td>SFP / 比消費電力を入力する</td>
#     <td>(Decimal Value)</td>
# </tr>
# <tr>
#     <td colspan=3>Ventilation Rate / 換気階数</td>
#     <td>1: 0.5 time/h<br>2: 0.7 time/h<br>3: 0.0 time/h</td>
# </tr>
# <tr>
#     <td colspan=3>Effective Ventilation Rate for Type 1 / 第一種換気設備の場合における有効換気量率</td>
#     <td>(Decimal Value)</td>
# </tr>
# <tr>
#     <td rowspan=4>Heat Exchanger / 熱交換型換気</td>
#     <td colspan=2>Apply / 熱交換型換気の採用</td>
#     <td>1: Apply / 熱交換型換気を採用する<br>2: Not Apply / 熱交換型換気を採用しない</td>
# </tr>
# <tr>
#     <td colspan=2>Temperature Exchange Rate / 温度交換効率</td>
#     <td>(Decimal Value)</td>
# </tr>
# <tr>
#     <td colspan=2>Correct Coefficient for Temperature Exchange Rate for Balance of Supply and Exhaust Air Amount / 給気と排気の比率による温度交換効率の補正係数</td>
#     <td>(Decimal Value)</td>
# </tr>
# <tr>
#     <td colspan=2>Correct Coefficient for Temperature Exchange Rate for Air Leak when Exhaust Air is larger than Supply Air / 排気過多時における住宅外皮経由の漏気による温度交換効率の補正係数</td>
#     <td>(Decimal Value)</td>
# </tr>
# </table>

# #### Input Data

# ````
# DataVentilation = {
#     'Ventilation': {  
#         'VentilationType': '',          # 'DuctType1', 'DuctType2', 'DuctType3', 'WallType1', 'WallType2', 'WallType3'
#         'DuctTypeSpec' : {
#             'EnergySavingType'   : '',  # 'None', 'Specification', 'SFP'
#             'EnergySavingMethod' : '',  # 'LargeDuct', 'LargeDuctAndDCMoter'
#             'SFP'                : ''   # Decimal Value represented as string
#         },
#         'WallMountedTypeSpec' : {
#             'EnergySavingType' : '',    # 'None', 'SFP'
#             'SFP'              : ''     # Decimal Value represented as string
#         }
#     },
#     'VentirationRate'          : '',    # '0.5', '0.7', '0.0'
#     'EffectiveVentilationRate' : '',    # Decimal Value represented as string
#     'HeatExchanger' : {
#         'Apply'                   : '', # 'Apply', 'NotApply'
#         'TemperatureExchangeRate' : '', # Decimal Value represented as string
#         'BalanceCorrectCoeff'     : '', # Decimal Value represented as string
#         'AirLeakCorrectCoeff'     : ''  # Decimal Value represented as string
#     }
# }
# ````

# ### 4.2 Function

# In[23]:

def getHoerlyElectricPower(DataGeneral, DataVentilation, day, hour ):
    
    def Spec(d):
        
        def Spec_Type(d):
            if d['Ventilation']['VentilationType'] == 'DuctType1':
                if d['HeatExchanger']['Apply']  == 'Apply':
                    return VentilationType.Duct1_HEX
                elif d['HeatExchanger']['Apply']  == 'NotApply':
                    return VentilationType.Duct1
                else:
                    raise Exception('Wrong Parameter about [Apply] in [Heat Exchanger].')
            elif d['Ventilation']['VentilationType'] == 'DuctType2':
                return VentilationType.Duct2
            elif d['Ventilation']['VentilationType'] == 'DuctType3':
                return VentilationType.Duct3
            elif d['Ventilation']['VentilationType'] == 'WallType1':
                if d['HeatExchanger']['Apply']  == 'Apply':
                    return VentilationType.Wall1_HEX
                elif d['HeatExchanger']['Apply']  == 'NotApply':
                    return VentilationType.Wall1
                else:
                    raise Exception('Wrong Parameter about [Apply] in [Heat Exchanger].')
            elif d['Ventilation']['VentilationType'] == 'WallType2':
                return VentilationType.Wall2
            elif d['Ventilation']['VentilationType'] == 'WallType3':
                return VentilationType.Wall3
            else:
                raise Exception('Wrong Parameter about [VentilationType].')     
            
        if Spec_Type(d) == VentilationType.Duct1_HEX or Spec_Type(d) == VentilationType.Duct1 or Spec_Type(d) == VentilationType.Duct2 or Spec_Type(d) == VentilationType.Duct3:
            if d['Ventilation']['DuctTypeSpec']['EnergySavingType']  == 'None':
                return (False, None, Spec_Type(d), EnergySavingMethod.Others)
            elif d['Ventilation']['DuctTypeSpec']['EnergySavingType']  == 'Specification':
                if d['Ventilation']['DuctTypeSpec']['EnergySavingMethod'] == 'LargeDuct':
                    return (False, None, Spec_Type(d), EnergySavingMethod.Over75mm_AC)
                elif d['Ventilation']['DuctTypeSpec']['EnergySavingMethod'] == 'LargeDuctAndDCMoter':
                    return (False, None, Spec_Type(d), EnergySavingMethod.Over75mm_DC)
                else:
                    raise Exception('Wrong Parameter about [EnergySavingMethod] in [DuctTypeSpec] in [Ventilation]')
            elif d['Ventilation']['DuctTypeSpec']['EnergySavingType']  == 'SFP':
                return (True, float(d['Ventilation']['DuctTypeSpec']['SFP']), None, None)
            else:
                raise Exception('Wrong Parameter about [EnergySavingType] in [DuctTypeSpec] in [Ventilation]')
        elif Spec_Type(d) == VentilationType.Wall1_HEX or Spec_Type(d) == VentilationType.Wall1 or Spec_Type(d) == VentilationType.Wall2 or Spec_Type(d) == VentilationType.Wall3:
            if d['Ventilation']['WallMountedTypeSpec']['EnergySavingType']  == 'None':
                return (False, None, Spec_Type(d), None)
            elif d['Ventilation']['WallMountedTypeSpec']['EnergySavingType']  == 'SFP':
                return (True, float(d['Ventilation']['WallMountedTypeSpec']['SFP']), None, None)
            else:
                raise Exception('Wrong Parameter about [EnergySavingType] in [WallMountedTypeSpec] in [Ventilation]')
    
    def getPerson(A_A):
        if A_A <= 30: # 床面積が30m2未満の場合は居住人数は1人とみなす
            return 1
        elif A_A >= 120: # 床面積が120m2以上の場合は居住人数は4人とみなす
            return 4
        else:
            return A_A / 30.0

    # Set vertual person based on sum of the floor area.
    _person = getPerson(float(DataGeneral['AllFloorArea']))  
    
    # Convert the data from 'DataVentilation' as dictionary into 4 variants as 'does inputS FP', 'SFP', 'ventilation type' and 'energy saving method'.
    (_DoesInputSFP, _SFP, _t, _s) = Spec(DataVentilation)

    # Calculate SFP (W/(m3/h))
    _SFP = get_SFP(_DoesInputSFP, _SFP, _t, _s)
    
    # Calculate referenced ventilation amount (m3/h)
    _V_R = get_V_R( float(DataGeneral['AllFloorArea']), float(DataVentilation['VentilationRate']), float(DataVentilation['EffectiveVentilationRate']) )
    
    # Calculate power of general ventilation system (kWh/h)
    _E_E_VG = get_E_E_VG( _SFP ,_V_R )
    
    # Calculate power of local ventilation system (kWh/h)
    _E_E_VL = get_E_E_VL( get_E_E_VL_p, _person, day, hour )
    
    # Calculate power of all ventilation system (kWh/h)
    E_E_V = get_E_E_V( _E_E_VG, _E_E_VL ) 
    
    return E_E_V


# #### Example

# In[24]:

DataVentilation = {
    'Ventilation': {  
        'VentilationType': 'DuctType1',          # 'DuctType1', 'DuctType2', 'DuctType3', 'WallType1', 'WallType2', 'WallType3'
        'DuctTypeSpec' : {
            'EnergySavingType'   : 'None',  # 'None', 'Specification', 'SFP'
            'EnergySavingMethod' : '',  # 'LargeDuct', 'LargeDuctAndDCMoter'
            'SFP'                : ''   # Decimal Value represented as string
        },
        'WallMountedTypeSpec' : {
            'EnergySavingType' : '',    # 'None', 'SFP'
            'SFP'              : ''     # Decimal Value represented as string
        }
    },
    'VentilationRate'          : '0.5',    # '0.5', '0.7', '0.0'
    'EffectiveVentilationRate' : '1.0',    # Decimal Value represented as string
    'HeatExchanger' : {
        'Apply'                   : 'Apply', # 'Apply', 'NotApply'
        'TemperatureExchangeRate' : '65', # Decimal Value represented as string
        'BalanceCorrectCoeff'     : '0.90', # Decimal Value represented as string
        'AirLeakCorrectCoeff'     : '1.00'  # Decimal Value represented as string
    }
}
DataGeneral = {
    'AllFloorArea' : '120.08' # m2
}


# In[25]:

getHoerlyElectricPower(DataGeneral, DataVentilation, day = '1/1', hour = 23 )

