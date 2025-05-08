from werkzeug.security import generate_password_hash, check_password_hash

# passwords from employees

employees = {
    'admin': {'user': 'admin', 'password': generate_password_hash('Admin123.')},
    'employee1': {'user': 'Eparedesm', 'password': generate_password_hash('Epar123.')},
    'employee2': {'user': 'Jnavarrof', 'password': generate_password_hash('Janv123.')},
    'employee3': {'user': 'Lpereirat', 'password': generate_password_hash('Lper123.')},
    'employee4': {'user': 'Mesquivelt', 'password': generate_password_hash('Mesq123.')},
    'employee5': {'user': 'Nfloreza', 'password': generate_password_hash('Nflo123.')},
    'employee6': {'user': 'Sroldang', 'password': generate_password_hash('Srol123.')}, # leaders
    'employee7': {'user': 'Darvant', 'password': generate_password_hash('Darv123.')},
    'employee8': {'user': 'Emontesird', 'password': generate_password_hash('Emon123.')},
    'employee9': {'user': 'Jvaldekt', 'password': generate_password_hash('Jval123.')},
    'employee10': {'user': 'Kdrovicn', 'password': generate_password_hash('Kdro123.')},
    'employee11': {'user': 'Lmalzario', 'password': generate_password_hash('Lmal123.')},
    'employee12': {'user': 'Nbeltrenz', 'password': generate_password_hash('Nbel123.')},
    'employee13': {'user': 'Rtreviskd', 'password': generate_password_hash('Rtre123.')},
    'employee14': {'user': 'Strevallesm', 'password': generate_password_hash('Stre123.')},
    'employee15': {'user': 'Tmostike', 'password': generate_password_hash('Tmos123.')},
    'employee16': {'user': 'Ydesmondv', 'password': generate_password_hash('Ydes123.')},  # architects and engineers
    'employee17': {'user': 'Aravoshm', 'password': generate_password_hash('Arav123.')},
    'employee18': {'user': 'Belorikt', 'password': generate_password_hash('Belo123.')},
    'employee19': {'user': 'Dormarak', 'password': generate_password_hash('Dorm123.')},
    'employee20': {'user': 'Djorenzk', 'password': generate_password_hash('Djor123.')},
    'employee21': {'user': 'Evolekt', 'password': generate_password_hash('Evol123.')},
    'employee22': {'user': 'Jnorellt', 'password': generate_password_hash('Jnor123.')},
    'employee23': {'user': 'Lkrevezd', 'password': generate_password_hash('Lkre123.')},
    'employee24': {'user': 'Lfoskarid', 'password': generate_password_hash('Lfos123.')},
    'employee25': {'user': 'Ldarsikf', 'password': generate_password_hash('Ldar123.')},
    'employee26': {'user': 'Msolvend', 'password': generate_password_hash('Msol123.')},
    'employee27': {'user': 'Mhaspelv', 'password': generate_password_hash('Mhas123.')},
    'employee28': {'user': 'Mdrevikz', 'password': generate_password_hash('Mdre123.')},
    'employee29': {'user': 'Mvankorl', 'password': generate_password_hash('Mvan123.')},
    'employee30': {'user': 'Nelvanicz', 'password': generate_password_hash('Nelv123.')},
    'employee31': {'user': 'Storrelo', 'password': generate_password_hash('Stor123.')},
    'employee32': {'user': 'Sdrovenk', 'password': generate_password_hash('Sdro123.')},
    'employee33': {'user': 'Tvalvend', 'password': generate_password_hash('Tval123.')},
    'employee34': {'user': 'Tjalvend', 'password': generate_password_hash('Tjal123.')},
    'employee35': {'user': 'Ykardeta', 'password': generate_password_hash('Ykar123.')}
}

# password for clients

clients = {
    'client1': {'user': 'Hector Parrilla', 'password': generate_password_hash('Hector123.')},
    'client2': {'user': 'Juan Garcia', 'password': generate_password_hash('Juan123.')},
    'client3': {'user': 'Valentina Florez', 'password': generate_password_hash('Valentina123.')},
    'client4': {'user': 'Gabriel Parejo', 'password': generate_password_hash('Gabriel123.')},
    'client5': {'user': 'José Sastre', 'password': generate_password_hash('Jose123.')},
    'client6': {'user': 'Tomeu Moll', 'password': generate_password_hash('Tomeu123.')},
    'client7': {'user': 'William Gutierrez', 'password': generate_password_hash('William123.')},
    'client8': {'user': 'Paula Garcia', 'password': generate_password_hash('Paula123.')},
    'client9': {'user': 'Andrea Gonzales', 'password': generate_password_hash('Andrea123.')},
    'client10': {'user': 'David Villanueva', 'password': generate_password_hash('David123.')}
}
print(clients)