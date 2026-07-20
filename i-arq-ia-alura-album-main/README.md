# Álbum Geográfico & Cultural - Moçambique & Brasil 🇲🇿🇧🇷

Um álbum de figurinhas digital e interativo desenvolvido para celebrar as **Regiões e Províncias de Moçambique** e as **5 Regiões Oficiais do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste e Sul)**, proporcionando um mapa cultural com navegação rápida e transição animada de virada de página.

---

## 🎯 Objetivo do Projeto

O objetivo do **Álbum Geográfico** é oferecer uma experiência imersiva e interativa no navegador, apresentando a riqueza e diversidade cultural de dois países irmãos:
- **Índice Interativo (Página 1)**: Atalhos diretos para cada uma das províncias de Moçambique e regiões oficiais do Brasil.
- **Transição Animada de Virada de Página**: Efeito 3D fluido com animações de destaque visual via `St.PageFlip` e CSS.
- **Design Temático & Responsivo**: Visual moderno com badges regionais dedicados, cores oficiais 🇲🇿/🇧🇷 e cards organizados por províncias/estados.

---

## 📌 Estrutura do Álbum

1. **Página 0 (Capa)**: Apresentação principal do Álbum Geográfico Moçambique & Brasil.
2. **Página 1 (Índice Interativo)**: Menu interativo com botões para Moçambique e para cada uma das 5 Regiões do Brasil.
3. **Página 2 (Moçambique - Região Norte)**: Províncias de Cabo Delgado, Niassa e Nampula.
4. **Página 3 (Moçambique - Região Centro)**: Províncias de Zambézia, Tete, Manica e Sofala.
5. **Página 4 (Moçambique - Região Sul)**: Províncias de Inhambane, Gaza, Maputo Província e Maputo Cidade.
6. **Página 5 (Brasil - Região Norte)**: Amazonas, Pará, Amapá, Roraima, Acre, Rondônia e Tocantins.
7. **Página 6 (Brasil - Região Nordeste)**: Maranhão, Piauí, Ceará, RN, Paraíba, Pernambuco, Alagoas, Sergipe e Bahia.
8. **Página 7 (Brasil - Região Centro-Oeste)**: Distrito Federal, Goiás, Mato Grosso e Mato Grosso do Sul.
9. **Página 8 (Brasil - Região Sudeste)**: São Paulo, Rio de Janeiro, Minas Gerais e Espírito Santo.
10. **Página 9 (Brasil - Região Sul)**: Paraná, Santa Catarina e Rio Grande do Sul.
11. **Página 10 (Contracapa)**: Tributo à união e riqueza cultural dos dois países.

---

## 📁 Estrutura de Arquivos e Funcionalidades

| Arquivo | Descrição / Funcionalidades |
| :--- | :--- |
| **`index.html`** | **Estrutura HTML5:** Define a marcação completa do álbum, separando cada uma das 5 Regiões Oficiais do Brasil em páginas individuais dedicadas. |
| **`style.css`** | **Estilização Visual (CSS3):** Define as cores dos badges regionais de Moçambique e do Brasil, layout do índice compacto e animações de clique. |
| **`app.js`** | **Lógica e Interatividade (JavaScript):** Controla a biblioteca `St.PageFlip`, gerencia cliques no índice para `pageFlip.flip(targetPage)` e som de folheamento. |

---

## 🚀 Como Executar o Projeto

1. Abra o arquivo `index.html` diretamente em seu navegador ou utilize a extensão **Live Server** (no VS Code) para rodar a aplicação localmente.
2. Utilização do **Índice na Página 1**: clique em qualquer uma das 5 regiões do Brasil ou regiões de Moçambique para ir direto à página desejada!
