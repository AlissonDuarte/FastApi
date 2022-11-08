med1 = {"Id":"1" ,"Nome": "Dipirona", "Indicado":["Febre", "Dores no corpo"],
        "Cuidados": "Evitar superdose: 1g", "D_Relacionadas": "Dores em geral",
        "Reage com":["Vacina covid", "Diazepan e derivados de sinasteina",
                     "VitaminaC"]}

def search_name(nome):
    print(f"Gostária de saber algo específico ou uma visão geral sobre {nome}")
    first_step = input("Digite aqui: ")
    if first_step == "Visão geral":
        print(f"Este medicamento ({med1['Nome']}) é indicado para casos gerais de {med1['Indicado']},\n" 
              f" sendo necessário tomar cuidado com {med1['Cuidados']}. Recomendados esta medicação em caso de\n "
              f"{med1['D_Relacionadas']}, quando o paciente estiver medicado com {med1['Reage com']}, deve-se procurar\n"
              f"um substituto para este medicamento ")
    elif first_step == "algo específico":
        print("Selecione alguma dessas informações",
              med1.keys())
        second_step = input(" ")
        print(med1[f"{second_step}: "])
        print("Obrigado !!!!")


search_name("Dipirona")
