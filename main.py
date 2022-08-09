# Projeto Prático I - Jeniffer Macena 

import re

def verificaId(id):
  idAlfabeto = re.findall(r'(?<=([a-zA-Z]))', id)
  idNumero = re.findall(r'(?<=([0-9]))', id)
  #print(idAlfabeto)
  if(len(idNumero)> len(idAlfabeto)):
    return False
  return True

def verificaIP(ip):
  ipRegex = re.findall(r"([\d]{1,3})",ip)
  for i in ipRegex:
    if not (0<=int(i)<=255):
      return False
  return True

try:
  data = input()
  #data = 'Let123 1F.A4.6B.54 126.1.12.34 lbp.7@outlook.com pull biomassa_da_banana 57dad741117fa87011e8d54796133f0e'
  validate = re.match(r'^([a-zA-Z]+[a-zA-Z0-9]+)\s(((?!([0-9])\4{1})([0-9]){2}|([A-F][\d])|([\d][A-F]))\.((?!([0-9])\9{1})[0-9]{2}|([A-F][\d])|([\d][A-F]))\.((?!([0-9])\13{1})[0-9]{2}|([A-F][\d])|([\d][A-F]))\.((?!([0-9])\17{1})[0-9]{2}|([A-F][\d])|([\d][A-F])))\s([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})\s([a-zA-Z]+[\w.+-]*(\.[\w]+)?[@][a-z0-9-.]+\.[a-z]+((\.[a-z]+)*)?)\s(pull|push|stash|fork|pop)\s([a-z0-9_]+([a-z0-9]+)?)\s([a-f\d]{32})$', data)
  #verificaId(validate.group(1))
  #verificaIP(validate.group(20))
  if (validate == None) or (verificaId(validate.group(1)) == False) or (verificaIP(validate.group(20))== False):
    print(False)
  else: 
    print(True)
except EOFError:
  print(False)
