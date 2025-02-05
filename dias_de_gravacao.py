# Dias de Gravação
import pandas as pd
dias_gravados = pd.date_range(start='2023-01-01', end='2026-01-01',freq='10D')
manipulador_txt = open('dias_gravados.txt', 'a', encoding = 'utf-8')
for d in dias_gravados:
    manipulador_txt.write(str(d.date())+'\n')
manipulador_txt.close()
