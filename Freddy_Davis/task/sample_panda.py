import pandas as pd
from StyleFrame import StyleFrame, Styler, utils
#defing data frames

df = pd.DataFrame({
    'NO:':[1,2,3,4,5,6,7,8,9,10],
    'Country':['France','Germany','Argentina','Belgium','Brazil','Portugal','Poland','Switzerland','Spain','England'],
    'Goals:':[25,12,90,14,56,46,37,81,69,10]
    })
print(df)

# writer1 =StyleFrame.ExcelWriter('pandas_sample.xlsx')
# sf=StyleFrame(df)
# sf.apply_column_style(cols_to_style=df.columns, styler_obj=Styler(bg_color=utils.colors.white, bold=True, font=utils.fonts.arial,font_size=8),style_header=True)
# sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.blue, bold=True, font_size=8, font_color=utils.colors.white,number_format=utils.number_formats.general, protection=False))
# sf.to_excel(writer1,sheet_name='Sheet1',index=False, startrow=2,startcol=10)
#


writer =pd.ExcelWriter('pandas_sample.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='Sheet1',index=False, startrow=2,startcol=10)


workbook = writer.book
worksheet = writer.sheets['Sheet1']
chart = workbook.add_chart({'type':'column'})

format1 = workbook.add_format({'bg_color': '#FFC7CE',
                               'font_color': '#9C0006'
                               })

# worksheet.conditional_format('K4:K13', {'type':'3_color_scale'})
worksheet.conditional_format('K4:M13', {'type': 'cell',
                                         'criteria': '>=',
                                         'value': 0,
                                         'format': format1})

chart.add_series({
    'values': '=Sheet1!$L$4:$L$13',
    'categories':'=Sheet1!$K$4:$K$13',
    'gap':        20,
    'line':{'color':'red'},
    'fill':{'color':'#00C3FF'}
})

chart.set_y_axis({'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'none'})
chart.set_title({'name':'Goals Scored'})
worksheet.insert_chart('B2', chart)

writer.save()
