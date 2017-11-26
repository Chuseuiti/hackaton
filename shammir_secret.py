from secretsharing import PlaintextToHexSecretSharer

shares = PlaintextToHexSecretSharer.split_secret("{'address':'Sainte Catherine' , 'telephone': 524-857-9127}", 2, 3)

print('shares:', shares)

print('Recover information from 1 and 2:' + PlaintextToHexSecretSharer.recover_secret(shares[0:2]))
print('Recover information from 1 and 3:' + PlaintextToHexSecretSharer.recover_secret([shares[0],shares[2]]))
print('Recover information from 2 and 3:' + PlaintextToHexSecretSharer.recover_secret(shares[1:3]))
try:
    print('Recover of information from 2:' + PlaintextToHexSecretSharer.recover_secret(shares[1]))
except:
    print('Not enough available information')
    


