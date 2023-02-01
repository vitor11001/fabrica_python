from mecanica import Mecanica
from seguranca import Seguranca
from acessorios import Acessorios
        
class Esteira(Mecanica, Seguranca, Acessorios):
    
    def __init__(self, modelo):
        self.modelo = modelo


    def start(self):
        self.mechanics()
        self.security()
        self.accessorys()
        
        
    def mechanics(self):
        consumo = str()
        talvez_consumo_tb = str()
        cambio = str()
        qtd_marchas = int()
        tipo_injecao = str()
        amortecedor = str()
        radiador_tubular = bool()
        freios_abs = bool()
        turbo = bool()
        
        while True:
            print('''Escolha a opção que indica qual o consumo
                1 - Gasolina
                2 - Diesel
                3 - Elétrico
                ''')
            
            primeira_escolha = str(input('Digite a opção: '))
            
            if primeira_escolha == '1':
                consumo = 'Gasolina'
                talvez_consumo_tb = 'Elétrico'
                break
                    
            elif primeira_escolha == '2':
                consumo = 'Diesel'
                cambio = 'Manual'
                break
                
            elif primeira_escolha == '3':
                consumo = 'Elétrico'
                cambio = 'Automático'
                talvez_consumo_tb = 'Gasolina'
                break
                
            else:
                print('\nEscolha uma opção valida!\n')
                
        while primeira_escolha != '2':
            segunda_escolha = str(input(f'Ele também é a {talvez_consumo_tb}?[y/n] ')).upper()
            
            if segunda_escolha == 'Y':
                consumo = 'Híbrido'
                break
            elif segunda_escolha == 'N':
                break
            else:
                print('\nEscolha uma opção valida!\n')
        
        Mecanica.write_consup(self, consumo)
        
        if consumo != 'Diesel' and consumo != 'Elétrico':
            while True:
                print('''Escolha a opção que indica o tipo de Câmbio:
                    1 - Manual
                    2 - Automático
                    ''')
                
                escolha = str(input('Sua escolha: '))
                
                if escolha == '1':
                    cambio = 'Manual'
                    break
                    
                elif escolha == '2':
                    cambio = 'Automático'
                    break
                    
                else:
                    print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_exchange(self, cambio)
        
        while True:
            print('''Escolha a Qtd de marcha: 
                  1 - 5 marchas
                  2 - 6 marchas
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                qtd_marchas = 5
                break
                
            elif escolha == '2':
                qtd_marchas = 6
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
        
        Mecanica.write_amount_gears(self, qtd_marchas)
        
        while True:
            print('''Escolha o Tipo de injeção:
                  1 - Eletrônica 
                  2 - Convencional
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                tipo_injecao = 'eletrônica'
                break
                
            elif escolha == '2':
                tipo_injecao = 'convencional'
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_type_injection(self, tipo_injecao)
        
        while True:
            print('''Escolha o tipo de Amortecedores:
                  1 - reforçados
                  2 - comum
                  ''')
            
            escolha = str(input('Sua escolha: '))
            
            if escolha == '1':
                amortecedor = 'reforçados'
                break
                
            elif escolha == '2':
                amortecedor = 'comum'
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_absorver(self, amortecedor)
                
        while True:
            escolha = str(input('O carro possui Radiador tubular?[y/n] ')).upper()
            
            if escolha == 'Y':
                radiador_tubular = True
                break
                
            elif escolha == 'N':
                radiador_tubular = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_tub_radiator(self, radiador_tubular)
        
        while True:
            escolha = str(input('O carro possui Freios ABS?[y/n] ')).upper()
            
            if escolha == 'Y':
                freios_abs = True
                break
                
            elif escolha == 'N':
                freios_abs = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_brakes_abs(self, freios_abs)
        
        while True:
            escolha = str(input('O carro possui Turbo?[y/n] ')).upper()
            
            if escolha == 'Y':
                turbo = True
                break
                
            elif escolha == 'N':
                turbo = False
                break
            
            else:
                print('\nEscolha uma opção valida!\n')
                
        Mecanica.write_turbo(self, turbo)


    def security(self):
        vidros_reforcados = bool()
        cintos_3_pontas = True
        airbag = True
        controle_estabilidade = bool()
        sensor_fadiga = bool()
        sensor_frenagem = bool()
        sensor_p_cego = bool()
        
        if self.consumo != 'Gasolina':
            while True:
                escolha = str(input('O carro terá vidros reforcados?[y/n]')).upper()
                if escolha == 'Y':
                    vidros_reforcados = True
                    break
                elif escolha == 'N':
                    vidros_reforcados = False
                    break
                else:
                    print('\nEscolha uma opção valida!\n')
                    
        else:
            vidros_reforcados = False
            
        Seguranca.write_glass_reforced(self, vidros_reforcados)
        
        Seguranca.write_3_point_belt(self, cintos_3_pontas)
        
        Seguranca.write_airbag(self, airbag)
        
        if self.consumo != 'Diesel':
            while True:
                escolha = str(input('O carro terá controle de estabilidade?[y/n]')).upper()
                if escolha == 'Y':
                    controle_estabilidade = True
                    break
                elif escolha == 'N':
                    controle_estabilidade = False
                    break
                else:
                    print('\nEscolha uma opção valida!\n')
                    
        else:
            controle_estabilidade = False
    
        Seguranca.write_stability_control(self, controle_estabilidade)
    
        while True:
            escolha = str(input('O carro terá sensor de fadiga?[y/n]')).upper()
            if escolha == 'Y':
                sensor_fadiga = True
                break
            elif escolha == 'N':
                sensor_fadiga = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
    
        Seguranca.write_s_fadigue(self, sensor_fadiga)
        
        while True:
            escolha = str(input('O carro terá sensor de frenagem?[y/n]')).upper()
            if escolha == 'Y':
                sensor_frenagem = True
                break
            elif escolha == 'N':
                sensor_frenagem = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
    
        Seguranca.write_s_braking(self, sensor_frenagem)
        
        while True:
            escolha = str(input('O carro terá sensor de ponto cego?[y/n]')).upper()
            if escolha == 'Y':
                sensor_p_cego = True
                break
            elif escolha == 'N':
                sensor_p_cego = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
    
        Seguranca.write_s_blind_spot(self, sensor_p_cego)
    
    def accessorys(self):
        camera_re = bool()
        camera_3d = bool()
        farol_led = True
        farol_milha = bool()
        fechamento_mala = bool()
        sensor_calibragem_pneus = bool()
        ar_condicionado = True
        painel_digital = bool()
        
        while True:
            escolha = str(input('O carro terá camera traseira?[y/n]')).upper()
            if escolha == 'Y':
                camera_re = True
                break
            elif escolha == 'N':
                camera_re = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
                
        Acessorios.write_camera_re(self, camera_re)
        
        while True:
            escolha = str(input('O carro terá camera 3d?[y/n]')).upper()
            if escolha == 'Y':
                camera_3d = True
                break
            elif escolha == 'N':
                camera_3d = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
                
        Acessorios.write_camera_3d(self, camera_3d)
        
        Acessorios.write_headlight_led(self, farol_led)
        
        if self.consumo != 'Diesel':
            while True:
                escolha = str(input('O carro terá farol de milha?[y/n]')).upper()
                if escolha == 'Y':
                    farol_milha = True
                    break
                elif escolha == 'N':
                    farol_milha = False
                    break
                else:
                    print('\nEscolha uma opção valida!\n')
                    
        else:
            farol_milha = True
                
        Acessorios.write_headlight_milha(self, farol_milha)
        
        while True:
            escolha = str(input('O carro terá fechamento de mala?[y/n]')).upper()
            if escolha == 'Y':
                fechamento_mala = True
                break
            elif escolha == 'N':
                fechamento_mala = False
                break
            else:
                print('\nEscolha uma opção valida!\n')
                
        Acessorios.write_close_suitcase(self, fechamento_mala)
        
        if self.consumo != 'Elétrico':        
            while True:
                escolha = str(input('O carro terá sensor de calibragem de pneus?[y/n]')).upper()
                if escolha == 'Y':
                    sensor_calibragem_pneus = True
                    break
                elif escolha == 'N':
                    sensor_calibragem_pneus = False
                    break
                else:
                    print('\nEscolha uma opção valida!\n')
        
        else:
            sensor_calibragem_pneus = True
                
        Acessorios.write_s_calibration_tire(self, sensor_calibragem_pneus)
        
        Acessorios.write_air_conditioner(self, ar_condicionado)
        
        if self.consumo != 'Elétrico':
            while True:
                escolha = str(input('O carro terá painel digital?[y/n]')).upper()
                if escolha == 'Y':
                    painel_digital = True
                    break
                elif escolha == 'N':
                    painel_digital = False
                    break
                else:
                    print('\nEscolha uma opção valida!\n')
                    
        else:
            painel_digital = True
                
        Acessorios.write_digital_panel(self, painel_digital)


##############################################################################################################################################

onix = Esteira('onix')

onix.start()

for key, values in onix.read_all_mechanics().items():
    print(f'{key}: {values}')

for key, values in onix.read_all_security().items():
    print(f'{key}: {values}')