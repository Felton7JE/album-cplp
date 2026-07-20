# Álbum Geográfico da CPLP 🌍📖

Um projeto de código aberto nascido na **Imersão IA da Alura**! Este é um tributo interativo à riqueza geográfica, turística e cultural de todos os países membros da Comunidade dos Países de Língua Portuguesa (CPLP).

O projeto consiste num **álbum de figurinhas 3D interativo**, onde cada "página" representa as regiões dos 9 países, e as "figurinhas" são locais, províncias e arquipélagos notáveis. Ao clicar nas figurinhas, descobre-se uma riqueza de informações demográficas (capital, população, curiosidades e distritos).

## 🤝 Como Contribuir

A grande novidade é que **toda a estrutura HTML das 30 páginas já está montada** para os 9 países! No entanto, precisamos da força da comunidade para reunir as fotografias, dados curiosos e "colar" as figurinhas. 

A ideia é que cada desenvolvedor lusófono possa escolher o seu país ou região e ajudar a mapeá-lo!

### Países da CPLP a mapear:
- [ ] 🇦🇴 Angola
- [x] 🇧🇷 Brasil (Estrutura Completa)
- [ ] 🇨🇻 Cabo Verde
- [ ] 🇬🇼 Guiné-Bissau
- [ ] 🇬🇶 Guiné Equatorial
- [x] 🇲🇿 Moçambique (Completo com Dados)
- [ ] 🇵🇹 Portugal
- [ ] 🇸🇹 São Tomé e Príncipe
- [ ] 🇹🇱 Timor-Leste

### Passos para colaborar:

1. **Faça um Fork** deste repositório para o seu GitHub.
2. **Adicione as Imagens**: Salve as fotografias da sua região na pasta `i-arq-ia-alura-album-main/figurinhas` (nomeie-as com uma lógica simples, ex: `pt-norte.jpg`).
3. **Atualize a Base de Dados**: Abra o ficheiro `main.py` (Backend em FastAPI) e adicione os dados ao dicionário `figurinhas_db`. Preencha a `capital`, `populacao`, `curiosidade` e `distritos`.
4. **Vincule no Frontend**: Abra o `index.html`, procure a página referente ao seu país, e adicione as divs `.sticker-slot` correspondentes apontando para as novas imagens.
5. **Abra um Pull Request**: Submeta o PR para juntarmos tudo num gigantesco álbum lusófono!

## 🚀 Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript Nativo (Vanilla JS) + Efeitos de virada de página em 3D.
- **Backend:** Python + FastAPI para gerir os dados das províncias e quebrar cache dinamicamente.
- **Automação:** Script Python (`update_html_30.py`) para gestão estrutural das páginas HTML.

## 🛠️ Como rodar o projeto localmente

1. Clone o repositório e navegue até o diretório raiz.
2. Instale as dependências necessárias:
   ```bash
   pip install fastapi uvicorn
   ```
3. Inicie o servidor Backend:
   ```bash
   uvicorn main:app --reload
   ```
4. Abra o ficheiro `index.html` (pasta `i-arq-ia-alura-album-main`) diretamente no seu navegador, ou usando a extensão *Live Server* do VSCode.
5. Pressione as setas laterais ou arraste com o rato para folhear as páginas do álbum!

---

## 👨‍💻 Autor e Agradecimentos

**Autor:** Felton da Silva  
**LinkedIn:** [linkedin.com/in/estevafelton](https://www.linkedin.com/in/estevafelton/)

Os conhecimentos aplicados para o desenvolvimento deste projeto inovador foram adquiridos e consolidados durante a **Imersão IA da Alura**. Feito com 🩵 pela e para a Comunidade Lusófona de Tecnologia!
