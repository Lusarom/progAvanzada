KPascal = float(input('Ingresa presion en KPascales:'))

PSI = KPascal * 0.14508
mmHg = KPascal * 0.13332
atm = KPascal / 101.325


print('\n lb in^2: %.3f'%(PSI),'(PSI)')
print('\n mmHg: %.3f'%(mmHg),'(mmHg)')
print('\n atm: %.3f'%(atm),'(atm)')
