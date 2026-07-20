from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

app = FastAPI()

# 1. Configurar CORS para aceitar requisições de qualquer origem (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Definir caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Criar a lista chamada figurinhas apontando para o endpoint próprio de imagem
# Atualizado para bater exatamente com os slots e as regiões do frontend!
figurinhas = [
    {
        "id": 1, "nome": "Cabo Delgado", "categoria": "Norte", "imagem_url": "/figurinhas/1/imagem?v=3",
        "capital": "Pemba", "populacao": "~2.3 milhões (Censo 2017)",
        "curiosidade": "Conhecida pelas praias paradisíacas e o Arquipélago das Quirimbas. A arte maconde é um forte marco cultural.",
        "distritos": ["Ancuabe", "Balama", "Chiúre", "Ibo", "Macomia", "Mecúfi", "Meluco", "Metuge", "Mocímboa da Praia", "Montepuez", "Mueda", "Muidumbe", "Namuno", "Nangade", "Palma", "Pemba", "Quissanga"]
    },
    {
        "id": 2, "nome": "Niassa", "categoria": "Norte", "imagem_url": "/figurinhas/2/imagem?v=3",
        "capital": "Lichinga", "populacao": "~1.8 milhões (Censo 2017)",
        "curiosidade": "A maior província de Moçambique, abriga a vasta Reserva do Niassa e partes do impressionante Lago Niassa.",
        "distritos": ["Chimbonila", "Cuamba", "Lago", "Lichinga", "Majune", "Mandimba", "Marrupa", "Maúa", "Mavago", "Mecanhelas", "Mecula", "Metarica", "Muembe", "N'gauma", "Nipepe", "Sanga"]
    },
    {
        "id": 3, "nome": "Nampula", "categoria": "Norte", "imagem_url": "/figurinhas/3/imagem?v=3",
        "capital": "Nampula", "populacao": "~5.7 milhões (Censo 2017)",
        "curiosidade": "Província mais populosa do país. A histórica Ilha de Moçambique foi a primeira capital do país e é Património Mundial.",
        "distritos": ["Angoche", "Eráti", "Ilha de Moçambique", "Lalaua", "Larde", "Liúpo", "Malema", "Meconta", "Mecubúri", "Memba", "Mogincual", "Mogovolas", "Moma", "Monapo", "Mossuril", "Muecate", "Murrupula", "Nacala-a-Velha", "Nacala Porto", "Nacarôa", "Nampula", "Rapale", "Ribaué"]
    },
    {
        "id": 4, "nome": "Zambézia", "categoria": "Centro", "imagem_url": "/figurinhas/4/imagem?v=3",
        "capital": "Quelimane", "populacao": "~5.1 milhões (Censo 2017)",
        "curiosidade": "Famosa pelas vastas plantações de chá em Gurué e pelos imensos palmares costeiras.",
        "distritos": ["Alto Molócue", "Chinde", "Derre", "Gilé", "Gurué", "Ile", "Inhassunge", "Luabo", "Lugela", "Maganja da Costa", "Milange", "Mocuba", "Mocubela", "Molumbo", "Mopeia", "Morrumbala", "Mulevala", "Namacurra", "Namarroi", "Nicoadala", "Pebane", "Quelimane"]
    },
    {
        "id": 5, "nome": "Tete", "categoria": "Centro", "imagem_url": "/figurinhas/5/imagem?v=3",
        "capital": "Tete", "populacao": "~2.6 milhões (Censo 2017)",
        "curiosidade": "Província muito quente e cortada pelo Rio Zambeze, onde está a grandiosa Barragem de Cahora Bassa.",
        "distritos": ["Angónia", "Cahora-Bassa", "Changara", "Chifunde", "Chiuta", "Dôa", "Macanga", "Magoé", "Marara", "Marávia", "Moatize", "Mutarara", "Tete", "Zumbo"]
    },
    {
        "id": 6, "nome": "Manica", "categoria": "Centro", "imagem_url": "/figurinhas/6/imagem?v=3",
        "capital": "Chimoio", "populacao": "~1.9 milhões (Censo 2017)",
        "curiosidade": "Destaca-se pelo seu relevo montanhoso (Monte Binga) e o icónico perfil rochoso conhecido como Cabeça do Velho.",
        "distritos": ["Bárue", "Chimoio", "Gondola", "Guro", "Macate", "Machaze", "Macossa", "Manica", "Mossurize", "Sussundenga", "Tambara", "Vanduzi"]
    },
    {
        "id": 7, "nome": "Sofala", "categoria": "Centro", "imagem_url": "/figurinhas/7/imagem?v=3",
        "capital": "Beira", "populacao": "~2.2 milhões (Censo 2017)",
        "curiosidade": "Abriga a cidade costeira da Beira e o famoso Parque Nacional da Gorongosa, um ícone de biodiversidade.",
        "distritos": ["Beira", "Búzi", "Caia", "Chemba", "Cheringoma", "Chibabava", "Dondo", "Gorongosa", "Machanga", "Maringué", "Marromeu", "Muanza", "Nhamatanda"]
    },
    {
        "id": 8, "nome": "Inhambane", "categoria": "Sul", "imagem_url": "/figurinhas/8/imagem?v=3",
        "capital": "Inhambane", "populacao": "~1.4 milhões (Censo 2017)",
        "curiosidade": "A 'Terra de Boa Gente'. Destino turístico de excelência devido a Tofo, Bazaruto e aos seus recifes maravilhosos.",
        "distritos": ["Funhalouro", "Govuro", "Homoíne", "Inhambane", "Inharrime", "Inhassoro", "Jangamo", "Mabote", "Massinga", "Maxixe", "Morrumbene", "Panda", "Vilanculos", "Zavala"]
    },
    {
        "id": 9, "nome": "Gaza", "categoria": "Sul", "imagem_url": "/figurinhas/9/imagem?v=3",
        "capital": "Xai-Xai", "populacao": "~1.4 milhões (Censo 2017)",
        "curiosidade": "Conhecida pela praia do Bilene, Xai-Xai e por albergar o extenso Parque Nacional do Limpopo.",
        "distritos": ["Bilene", "Chibuto", "Chicualacuala", "Chigubo", "Chókwè", "Chongoene", "Guijá", "Limpopo", "Mabalane", "Manjacaze", "Mapai", "Massangena", "Massingir", "Xai-Xai"]
    },
    {
        "id": 10, "nome": "Maputo", "categoria": "Sul", "imagem_url": "/figurinhas/10/imagem?v=3",
        "capital": "Maputo", "populacao": "~3.0 milhões (Província + Cidade)",
        "curiosidade": "Reúne a capital vibrante de Moçambique (com os seus arranha-céus) e áreas naturais como a Reserva Especial de Maputo.",
        "distritos": ["Boane", "Magude", "Manhiça", "Marracuene", "Matola", "Matutuíne", "Moamba", "Namaacha", "Maputo Cidade"]
    }
]

# 4. Criar o endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# 5. Criar o endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao_busca = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos_encontrados = glob.glob(padrao_busca)
    
    # Retorna 404 se não encontrar a imagem
    if not arquivos_encontrados:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Retorna FileResponse com o arquivo encontrado sem usar cache
    return FileResponse(
        arquivos_encontrados[0],
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

# 6. Criar o endpoint GET "/figurinhas/{id}" para retornar os detalhes da província
@app.get("/figurinhas/{id}")
def obter_detalhes_figurinha(id: int):
    for figurinha in figurinhas:
        if figurinha["id"] == id:
            return figurinha
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")

# O Frontend é agora servido nativamente pelo Vercel via vercel.json
