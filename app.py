import requests                                                                                  
import pandas as pd


def info_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    resposta = requests.get(url)                                                                

    if resposta.status_code == 200:                                                             
        dados = resposta.json()                                                                 
        id_pokemon = dados['id']                                                                
        nome_pokemon = dados['name']                                                           

        url_areas = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}/encounters"      
        resposta_areas = requests.get(url_areas)                                                

        if resposta_areas.status_code == 200:                                                   
            dados_areas = resposta_areas.json()                                                 
            areas = [local['location_area']['name'] for local in dados_areas]                   
            nome_area = ", ".join(areas)                                                        
        else:                                                                                   
            nome_area = "Área desconhecida"

        return id_pokemon, nome_pokemon, nome_area                                              
    else:                                                                                       
        return None

def salvar_csv_pandas(dados_resultado):                                                         
    df = pd.DataFrame([dados_resultado], columns=["ID", "Nome","Áreas"])
    df.to_csv('pokedex.csv', index=False)


def main():                                                                                     
    nome_pokemon = input("Digite o nome do Pokémon: ")                                          
    dados_resultado = info_pokemon(nome_pokemon)                                                

    if dados_resultado:                                                                         
        print("ID:", dados_resultado[0])                                                        
        print("Nome:", dados_resultado[1])                                                      
        print("Áreas:", dados_resultado[2])                                                     
        salvar_csv_pandas(dados_resultado)                                                      
        print("Dados salvos no arquivo pokedex.csv")                                            
    else:                                                                                       
        print("Pokémon não encontrado na pokedex")                                              


if __name__ == "__main__":                                                                      
    main()                                                                                      
    