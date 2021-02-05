Spin = str(input())
Charge = str(input())
if Spin == '1/2' and Charge == '-1/3':
    print('Strange Quark')
elif Spin == '1/2' and Charge == '2/3':
    print('Charm Quark')
elif Spin == '1/2' and Charge == '-1':
    print('Electron Lepton')
elif Spin == '1/2' and Charge == '0':
    print('Neutrino Lepton')
else:
    print('Photon Boson')
