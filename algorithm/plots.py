import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

tls.set_credentials_file(username='bhanujain', api_key='pic17ydt8e')
trace0 = go.Scatter(
    x=[6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994,
        430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999,
        986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112,
        2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001,
        690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111,
        579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928,
        1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112,
        3820.17523, 823.6856205, 4811.060429, 619.6768923999999,
        2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089,
        1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808,
        2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025,
        1056.3801210000001, 1271.211593, 469.70929810000007],
    y=[72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001,
       50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328,
       54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04,
       52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005,
       54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005,
       48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082,
       52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242,
       65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004,
       39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999,
       43.486999999999995],
    mode='markers',
    name='Africa',
    text=['hello', 'Country: Angola<br>Life Expectancy: 42.731<br>GDP per capita: 4797.231267<br>Population: 12420476.0<br>Year: 2007', 'Country: Benin<br>Life Expectancy: 56.728<br>GDP per capita: 1441.284873<br>Population: 8078314.0<br>Year: 2007', 'Country: Botswana<br>Life Expectancy: 50.728<br>GDP per capita: 12569.85177<br>Population: 1639131.0<br>Year: 2007', 'Country: Burkina Faso<br>Life Expectancy: 52.295<br>GDP per capita: 1217.032994<br>Population: 14326203.0<br>Year: 2007', 'Country: Burundi<br>Life Expectancy: 49.58<br>GDP per capita: 430.0706916<br>Population: 8390505.0<br>Year: 2007', 'Country: Cameroon<br>Life Expectancy: 50.43<br>GDP per capita: 2042.09524<br>Population: 17696293.0<br>Year: 2007', 'Country: Central African Republic<br>Life Expectancy: 44.741<br>GDP per capita: 706.016537<br>Population: 4369038.0<br>Year: 2007', 'Country: Chad<br>Life Expectancy: 50.651<br>GDP per capita: 1704.063724<br>Population: 10238807.0<br>Year: 2007', 'Country: Comoros<br>Life Expectancy: 65.152<br>GDP per capita: 986.1478792<br>Population: 710960.0<br>Year: 2007', 'Country: Congo, Dem. Rep.<br>Life Expectancy: 46.462<br>GDP per capita: 277.5518587<br>Population: 64606759.0<br>Year: 2007', 'Country: Congo, Rep.<br>Life Expectancy: 55.322<br>GDP per capita: 3632.557798<br>Population: 3800610.0<br>Year: 2007', "Country: Cote d'Ivoire<br>Life Expectancy: 48.328<br>GDP per capita: 1544.750112<br>Population: 18013409.0<br>Year: 2007", 'Country: Djibouti<br>Life Expectancy: 54.791<br>GDP per capita: 2082.481567<br>Population: 496374.0<br>Year: 2007', 'Country: Egypt<br>Life Expectancy: 71.338<br>GDP per capita: 5581.180998<br>Population: 80264543.0<br>Year: 2007', 'Country: Equatorial Guinea<br>Life Expectancy: 51.579<br>GDP per capita: 12154.08975<br>Population: 551201.0<br>Year: 2007', 'Country: Eritrea<br>Life Expectancy: 58.04<br>GDP per capita: 641.3695236<br>Population: 4906585.0<br>Year: 2007', 'Country: Ethiopia<br>Life Expectancy: 52.947<br>GDP per capita: 690.8055759<br>Population: 76511887.0<br>Year: 2007', 'Country: Gabon<br>Life Expectancy: 56.735<br>GDP per capita: 13206.48452<br>Population: 1454867.0<br>Year: 2007', 'Country: Gambia<br>Life Expectancy: 59.448<br>GDP per capita: 752.7497265<br>Population: 1688359.0<br>Year: 2007', 'Country: Ghana<br>Life Expectancy: 60.022<br>GDP per capita: 1327.60891<br>Population: 22873338.0<br>Year: 2007', 'Country: Guinea<br>Life Expectancy: 56.007<br>GDP per capita: 942.6542111<br>Population: 9947814.0<br>Year: 2007', 'Country: Guinea-Bissau<br>Life Expectancy: 46.388<br>GDP per capita: 579.231743<br>Population: 1472041.0<br>Year: 2007', 'Country: Kenya<br>Life Expectancy: 54.11<br>GDP per capita: 1463.249282<br>Population: 35610177.0<br>Year: 2007', 'Country: Lesotho<br>Life Expectancy: 42.592<br>GDP per capita: 1569.331442<br>Population: 2012649.0<br>Year: 2007', 'Country: Liberia<br>Life Expectancy: 45.678<br>GDP per capita: 414.5073415<br>Population: 3193942.0<br>Year: 2007', 'Country: Libya<br>Life Expectancy: 73.952<br>GDP per capita: 12057.49928<br>Population: 6036914.0<br>Year: 2007', 'Country: Madagascar<br>Life Expectancy: 59.443<br>GDP per capita: 1044.770126<br>Population: 19167654.0<br>Year: 2007', 'Country: Malawi<br>Life Expectancy: 48.303<br>GDP per capita: 759.3499101<br>Population: 13327079.0<br>Year: 2007', 'Country: Mali<br>Life Expectancy: 54.467<br>GDP per capita: 1042.581557<br>Population: 12031795.0<br>Year: 2007', 'Country: Mauritania<br>Life Expectancy: 64.164<br>GDP per capita: 1803.151496<br>Population: 3270065.0<br>Year: 2007', 'Country: Mauritius<br>Life Expectancy: 72.801<br>GDP per capita: 10956.99112<br>Population: 1250882.0<br>Year: 2007', 'Country: Morocco<br>Life Expectancy: 71.164<br>GDP per capita: 3820.17523<br>Population: 33757175.0<br>Year: 2007', 'Country: Mozambique<br>Life Expectancy: 42.082<br>GDP per capita: 823.6856205<br>Population: 19951656.0<br>Year: 2007', 'Country: Namibia<br>Life Expectancy: 52.906<br>GDP per capita: 4811.060429<br>Population: 2055080.0<br>Year: 2007', 'Country: Niger<br>Life Expectancy: 56.867<br>GDP per capita: 619.6768924<br>Population: 12894865.0<br>Year: 2007', 'Country: Nigeria<br>Life Expectancy: 46.859<br>GDP per capita: 2013.977305<br>Population: 135031164.0<br>Year: 2007', 'Country: Reunion<br>Life Expectancy: 76.442<br>GDP per capita: 7670.122558<br>Population: 798094.0<br>Year: 2007', 'Country: Rwanda<br>Life Expectancy: 46.242<br>GDP per capita: 863.0884639<br>Population: 8860588.0<br>Year: 2007', 'Country: Sao Tome and Principe<br>Life Expectancy: 65.528<br>GDP per capita: 1598.435089<br>Population: 199579.0<br>Year: 2007', 'Country: Senegal<br>Life Expectancy: 63.062<br>GDP per capita: 1712.472136<br>Population: 12267493.0<br>Year: 2007', 'Country: Sierra Leone<br>Life Expectancy: 42.568<br>GDP per capita: 862.5407561<br>Population: 6144562.0<br>Year: 2007', 'Country: Somalia<br>Life Expectancy: 48.159<br>GDP per capita: 926.1410683<br>Population: 9118773.0<br>Year: 2007', 'Country: South Africa<br>Life Expectancy: 49.339<br>GDP per capita: 9269.657808<br>Population: 43997828.0<br>Year: 2007', 'Country: Sudan<br>Life Expectancy: 58.556<br>GDP per capita: 2602.394995<br>Population: 42292929.0<br>Year: 2007', 'Country: Swaziland<br>Life Expectancy: 39.613<br>GDP per capita: 4513.480643<br>Population: 1133066.0<br>Year: 2007', 'Country: Tanzania<br>Life Expectancy: 52.517<br>GDP per capita: 1107.482182<br>Population: 38139640.0<br>Year: 2007', 'Country: Togo<br>Life Expectancy: 58.42<br>GDP per capita: 882.9699438<br>Population: 5701579.0<br>Year: 2007', 'Country: Tunisia<br>Life Expectancy: 73.923<br>GDP per capita: 7092.923025<br>Population: 10276158.0<br>Year: 2007', 'Country: Uganda<br>Life Expectancy: 51.542<br>GDP per capita: 1056.380121<br>Population: 29170398.0<br>Year: 2007', 'Country: Zambia<br>Life Expectancy: 42.384<br>GDP per capita: 1271.211593<br>Population: 11746035.0<br>Year: 2007', 'Country: Zimbabwe<br>Life Expectancy: 43.487<br>GDP per capita: 469.7092981<br>Population: 12311143.0<br>Year: 2007'],
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=[29.810746602820924, 18.197149567147044, 14.675557544415877,
              6.610603004351287, 19.543385335458176, 14.956442130894114,
              21.72077890062975, 10.792626698654045, 16.52185943835442,
              4.353683242838546, 41.50240100063496, 10.066092062338873,
              21.91453196050797, 3.6377994860079204, 46.258986486204044,
              3.8334450569607683, 11.437310410545528, 45.16465542353964,
              6.227961099314154, 6.709136738617642, 24.694430700391482,
              16.285386604676816, 6.264612285824508, 30.812100863425822,
              7.325179403286266, 9.227791164226492, 12.68649752933601,
              22.60573984618565, 18.849582296257626, 17.910159625556144,
              9.337109185582111, 5.774872714286052, 29.999726284159046,
              23.063420581238734, 7.40199199438875, 18.54140518159347, 60,
              4.612764339536968, 15.369704446995708, 2.3067029222366395,
              18.084735199216812, 12.79910818701753, 15.592022291528775,
              34.24915519732991, 33.57902844158756, 5.496191404660524,
              31.887651824471956, 12.329112567064463, 16.55196774082315,
              27.887232791984047, 17.696194784090615, 18.11688103909921],
        line=dict(
            width=2
        ),
    )
)

data = [trace0]
layout = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        gridcolor='rgb(255, 255, 255)',
        range=[2.003297660701705, 5.191505530708712],
        type='log',
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        gridcolor='rgb(255, 255, 255)',
        range=[36.12621671352166, 91.72921793264332],
        zerolinewidth=1,
        ticklen=5,
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='life-expectancy-per-GDP-2007')