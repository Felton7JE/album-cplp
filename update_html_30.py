import re

with open('i-arq-ia-alura-album-main/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate the new inner pages (30 pages total -> 28 inner + 2 covers)
new_pages = """
            <!-- PAGINA 1: ÍNDICE INTERATIVO (VERTICAL) -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-index">NAVEGAÇÃO RÁPIDA</span>
                        <h3 class="page-title">Índice CPLP</h3>
                    </div>
                    
                    <div class="index-scroll-wrapper">
                        <div class="index-container">
                            <!-- Moçambique Section -->
                            <div class="index-section">
                                <h4 class="index-country-title"><img src="bandeiramz.jpeg" alt="🇲🇿" style="height: 16px; vertical-align: text-bottom; margin-right: 4px; border-radius: 2px;"> Moçambique</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-mocambique" data-page="2"><span class="idx-region">Norte</span></button>
                                    <button class="index-btn btn-mocambique" data-page="3"><span class="idx-region">Centro</span></button>
                                    <button class="index-btn btn-mocambique" data-page="4"><span class="idx-region">Sul</span></button>
                                </div>
                            </div>

                            <!-- Brasil Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇧🇷 Brasil</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-brasil" data-page="5"><span class="idx-region">Norte</span></button>
                                    <button class="index-btn btn-brasil" data-page="6"><span class="idx-region">Nordeste</span></button>
                                    <button class="index-btn btn-brasil" data-page="7"><span class="idx-region">Centro-Oeste</span></button>
                                    <button class="index-btn btn-brasil" data-page="8"><span class="idx-region">Sudeste</span></button>
                                    <button class="index-btn btn-brasil" data-page="9"><span class="idx-region">Sul</span></button>
                                </div>
                            </div>
                            
                            <!-- Angola Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇦🇴 Angola</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-angola" data-page="10"><span class="idx-region">Norte</span></button>
                                    <button class="index-btn btn-angola" data-page="11"><span class="idx-region">Centro</span></button>
                                    <button class="index-btn btn-angola" data-page="12"><span class="idx-region">Leste</span></button>
                                    <button class="index-btn btn-angola" data-page="13"><span class="idx-region">Sul</span></button>
                                </div>
                            </div>
                            
                            <!-- Portugal Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇵🇹 Portugal</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-portugal" data-page="14"><span class="idx-region">Norte</span></button>
                                    <button class="index-btn btn-portugal" data-page="15"><span class="idx-region">Centro & Tejo</span></button>
                                    <button class="index-btn btn-portugal" data-page="16"><span class="idx-region">Sul</span></button>
                                    <button class="index-btn btn-portugal" data-page="17"><span class="idx-region">Ilhas Autónomas</span></button>
                                </div>
                            </div>

                            <!-- Guiné-Bissau Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇬🇼 Guiné-Bissau</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-gb" data-page="18"><span class="idx-region">Norte e Leste</span></button>
                                    <button class="index-btn btn-gb" data-page="19"><span class="idx-region">Sul e Bissau</span></button>
                                </div>
                            </div>
                            
                            <!-- Cabo Verde Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇨🇻 Cabo Verde</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-cv" data-page="20"><span class="idx-region">Barlavento</span></button>
                                    <button class="index-btn btn-cv" data-page="21"><span class="idx-region">Sotavento</span></button>
                                </div>
                            </div>

                            <!-- São Tomé e Príncipe Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇸🇹 São Tomé e Príncipe</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-stp" data-page="22"><span class="idx-region">São Tomé</span></button>
                                    <button class="index-btn btn-stp" data-page="23"><span class="idx-region">Príncipe</span></button>
                                </div>
                            </div>
                            
                            <!-- Guiné Equatorial Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇬🇶 Guiné Equatorial</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-gq" data-page="24"><span class="idx-region">Insular</span></button>
                                    <button class="index-btn btn-gq" data-page="25"><span class="idx-region">Continental</span></button>
                                </div>
                            </div>
                            
                            <!-- Timor-Leste Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🇹🇱 Timor-Leste</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn btn-tl" data-page="26"><span class="idx-region">Costas Norte e Sul</span></button>
                                    <button class="index-btn btn-tl" data-page="27"><span class="idx-region">Interior & Especiais</span></button>
                                </div>
                            </div>
                            
                            <!-- Extra Community Section -->
                            <div class="index-section">
                                <h4 class="index-country-title">🚀 Comunidade Alura</h4>
                                <div class="index-grid index-grid-compact">
                                    <button class="index-btn" data-page="28" style="border-left-color: #1F53E5;"><span class="idx-region" style="color: #1F53E5;">Comunidade & Projeto</span></button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 1</div>
                </div>
            </div>

            <!-- PAGINA 2: MOÇAMBIQUE - REGIÃO NORTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-mocambique-norte"><img src="bandeiramz.jpeg" alt="🇲🇿" style="height: 12px; vertical-align: middle; margin-bottom: 2px; margin-right: 4px; border-radius: 2px;"> MOÇAMBIQUE</span>
                        <h3 class="page-title">Região Norte</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-01">
                            <div class="slot-number">#01</div>
                            <div class="slot-name">Cabo Delgado</div>
                            <div class="slot-role">Pemba • Praias e Cultura Makonde</div>
                        </div>
                        <div class="sticker-slot" id="slot-02">
                            <div class="slot-number">#02</div>
                            <div class="slot-name">Niassa</div>
                            <div class="slot-role">Lichinga • Lago Niassa e Reservas</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-03">
                            <div class="slot-number">#03</div>
                            <div class="slot-name">Nampula</div>
                            <div class="slot-role">Nampula • Ilha de Moçambique & Patrimônio</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 2</div>
                </div>
            </div>

            <!-- PAGINA 3: MOÇAMBIQUE - REGIÃO CENTRO -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-mocambique-centro"><img src="bandeiramz.jpeg" alt="🇲🇿" style="height: 12px; vertical-align: middle; margin-bottom: 2px; margin-right: 4px; border-radius: 2px;"> MOÇAMBIQUE</span>
                        <h3 class="page-title">Região Centro</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-04">
                            <div class="slot-number">#04</div>
                            <div class="slot-name">Zambézia</div>
                            <div class="slot-role">Quelimane • Coqueirais e Plantações de Chá</div>
                        </div>
                        <div class="sticker-slot" id="slot-05">
                            <div class="slot-number">#05</div>
                            <div class="slot-name">Tete</div>
                            <div class="slot-role">Tete • Rio Zambeze & Cahora Bassa</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-06">
                            <div class="slot-number">#06</div>
                            <div class="slot-name">Manica</div>
                            <div class="slot-role">Chimoio • Cabeça do Velho e Serras</div>
                        </div>
                        <div class="sticker-slot" id="slot-07">
                            <div class="slot-number">#07</div>
                            <div class="slot-name">Sofala</div>
                            <div class="slot-role">Beira • Parque Nacional do Gorongosa</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 3</div>
                </div>
            </div>

            <!-- PAGINA 4: MOÇAMBIQUE - REGIÃO SUL -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-mocambique-sul"><img src="bandeiramz.jpeg" alt="🇲🇿" style="height: 12px; vertical-align: middle; margin-bottom: 2px; margin-right: 4px; border-radius: 2px;"> MOÇAMBIQUE</span>
                        <h3 class="page-title">Região Sul</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-08">
                            <div class="slot-number">#08</div>
                            <div class="slot-name">Inhambane</div>
                            <div class="slot-role">Inhambane • Baía dos Golfinhos e Praia do Tofo</div>
                        </div>
                        <div class="sticker-slot" id="slot-09">
                            <div class="slot-number">#09</div>
                            <div class="slot-name">Gaza</div>
                            <div class="slot-role">Xai-Xai • Parque Transfronteiriço do Limpopo</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-10">
                            <div class="slot-number">#10</div>
                            <div class="slot-name">Maputo</div>
                            <div class="slot-role">Reserva Especial de Maputo e Capital</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 4</div>
                </div>
            </div>

            <!-- PAGINA 5: BRASIL - REGIÃO NORTE -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-brasil">🇧🇷 BRASIL</span>
                        <h3 class="page-title">Região Norte</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-12">
                            <div class="slot-number">#12</div>
                            <div class="slot-name">Amazônia</div>
                            <div class="slot-role">Floresta Amazônica e Biodiversidade</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-13">
                            <div class="slot-number">#13</div>
                            <div class="slot-role">Belém • Cultura Marajoara e Culinária</div>
                            <div class="slot-name">Pará</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 5</div>
                </div>
            </div>

            <!-- PAGINA 6: BRASIL - REGIÃO NORDESTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-brasil">🇧🇷 BRASIL</span>
                        <h3 class="page-title">Região Nordeste</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-14">
                            <div class="slot-number">#14</div>
                            <div class="slot-name">Bahia</div>
                            <div class="slot-role">Salvador • História, Axé e Praias</div>
                        </div>
                        <div class="sticker-slot" id="slot-15">
                            <div class="slot-number">#15</div>
                            <div class="slot-name">Pernambuco</div>
                            <div class="slot-role">Recife/Olinda • Frevo e Fernando de Noronha</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-16">
                            <div class="slot-number">#16</div>
                            <div class="slot-name">Ceará</div>
                            <div class="slot-role">Fortaleza • Dunas e Praias Paradisíacas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 6</div>
                </div>
            </div>

            <!-- PAGINA 7: BRASIL - CENTRO-OESTE -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-brasil">🇧🇷 BRASIL</span>
                        <h3 class="page-title">Centro-Oeste</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-17">
                            <div class="slot-number">#17</div>
                            <div class="slot-name">Distrito Federal</div>
                            <div class="slot-role">Brasília • Arquitetura Moderna e Poder</div>
                        </div>
                        <div class="sticker-slot" id="slot-18">
                            <div class="slot-number">#18</div>
                            <div class="slot-name">Goiás</div>
                            <div class="slot-role">Goiânia • Cerrado e Chapada dos Veadeiros</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-19">
                            <div class="slot-number">#19</div>
                            <div class="slot-name">Mato Grosso</div>
                            <div class="slot-role">Pantanal • Vida Selvagem e Natureza</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 7</div>
                </div>
            </div>

            <!-- PAGINA 8: BRASIL - SUDESTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-brasil">🇧🇷 BRASIL</span>
                        <h3 class="page-title">Região Sudeste</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-20">
                            <div class="slot-number">#20</div>
                            <div class="slot-name">São Paulo</div>
                            <div class="slot-role">Metrópole • Centro Financeiro e Gastronomia</div>
                        </div>
                        <div class="sticker-slot" id="slot-21">
                            <div class="slot-number">#21</div>
                            <div class="slot-name">Rio de Janeiro</div>
                            <div class="slot-role">Cristo Redentor, Pão de Açúcar e Praias</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-22">
                            <div class="slot-number">#22</div>
                            <div class="slot-name">Minas Gerais</div>
                            <div class="slot-role">Cidades Históricas, Montanhas e Culinária</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 8</div>
                </div>
            </div>

            <!-- PAGINA 9: BRASIL - SUL -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge badge-brasil">🇧🇷 BRASIL</span>
                        <h3 class="page-title">Região Sul</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-30">
                            <div class="slot-number">#30</div>
                            <div class="slot-name">Paraná</div>
                            <div class="slot-role">Curitiba • Cataratas do Iguaçu</div>
                        </div>
                        <div class="sticker-slot" id="slot-31">
                            <div class="slot-number">#31</div>
                            <div class="slot-name">Santa Catarina</div>
                            <div class="slot-role">Florianópolis • Praias, Ilha da Magia</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-32">
                            <div class="slot-number">#32</div>
                            <div class="slot-name">Rio Grande do Sul</div>
                            <div class="slot-role">Porto Alegre • Gramado, Serra Gaúcha</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 9</div>
                </div>
            </div>

            <!-- PAGINA 10: ANGOLA - NORTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇦🇴 ANGOLA</span>
                        <h3 class="page-title">Região Norte</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-101">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Luanda</div>
                            <div class="slot-role">Capital • Marginal e Ilha do Cabo</div>
                        </div>
                        <div class="sticker-slot" id="slot-102">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Cabinda</div>
                            <div class="slot-role">Exclave Maiombe</div>
                        </div>
                        <div class="sticker-slot" id="slot-103">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Zaire e Uíge</div>
                            <div class="slot-role">Rio Zaire e Cultura Kikongo</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 10</div>
                </div>
            </div>
            
            <!-- PAGINA 11: ANGOLA - CENTRO -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇦🇴 ANGOLA</span>
                        <h3 class="page-title">Região Centro</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-104">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Benguela</div>
                            <div class="slot-role">Praia da Baía Azul</div>
                        </div>
                        <div class="sticker-slot" id="slot-105">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Huambo</div>
                            <div class="slot-role">Planalto Central</div>
                        </div>
                        <div class="sticker-slot" id="slot-106">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Cuanza Sul & Bié</div>
                            <div class="slot-role">Cachoeiras e Coração de Angola</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 11</div>
                </div>
            </div>
            
            <!-- PAGINA 12: ANGOLA - LESTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇦🇴 ANGOLA</span>
                        <h3 class="page-title">Região Leste</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-107">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Lunda Norte e Sul</div>
                            <div class="slot-role">Diamantes e Cultura Lunda-Tchokwe</div>
                        </div>
                        <div class="sticker-slot" id="slot-108">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Moxico & Moxico Leste</div>
                            <div class="slot-role">A Maior Região Extensiva</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 12</div>
                </div>
            </div>

            <!-- PAGINA 13: ANGOLA - SUL -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇦🇴 ANGOLA</span>
                        <h3 class="page-title">Região Sul</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-109">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Namibe</div>
                            <div class="slot-role">Deserto e Welwitschia</div>
                        </div>
                        <div class="sticker-slot" id="slot-110">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Huíla</div>
                            <div class="slot-role">Fenda da Tundavala</div>
                        </div>
                        <div class="sticker-slot" id="slot-111">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Cunene e Cuando Cubango</div>
                            <div class="slot-role">Rio Cunene e Savanas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 13</div>
                </div>
            </div>

            <!-- PAGINA 14: PORTUGAL - NORTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #006600 0%, #004d00 100%); color: #ffffff; border-left: 3px solid #FF0000;">🇵🇹 PORTUGAL</span>
                        <h3 class="page-title">Região Norte</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-112">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Porto</div>
                            <div class="slot-role">Ribeira e Vinho do Porto</div>
                        </div>
                        <div class="sticker-slot" id="slot-113">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Braga & Guimarães</div>
                            <div class="slot-role">Berço da Nação</div>
                        </div>
                        <div class="sticker-slot" id="slot-114">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Trás-os-Montes</div>
                            <div class="slot-role">Douro e Paisagens Vinhateiras</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 14</div>
                </div>
            </div>

            <!-- PAGINA 15: PORTUGAL - CENTRO -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #006600 0%, #004d00 100%); color: #ffffff; border-left: 3px solid #FF0000;">🇵🇹 PORTUGAL</span>
                        <h3 class="page-title">Centro & Vale do Tejo</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-115">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Coimbra</div>
                            <div class="slot-role">Universidade Histórica e Fado</div>
                        </div>
                        <div class="sticker-slot" id="slot-116">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Aveiro</div>
                            <div class="slot-role">A Veneza de Portugal e Ovos Moles</div>
                        </div>
                        <div class="sticker-slot" id="slot-117">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Leiria & Viseu</div>
                            <div class="slot-role">Castelos e Centro Histórico</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 15</div>
                </div>
            </div>

            <!-- PAGINA 16: PORTUGAL - SUL -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #006600 0%, #004d00 100%); color: #ffffff; border-left: 3px solid #FF0000;">🇵🇹 PORTUGAL</span>
                        <h3 class="page-title">Região Sul</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-118">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Lisboa e Setúbal</div>
                            <div class="slot-role">Capital • Torre de Belém e Arrábida</div>
                        </div>
                        <div class="sticker-slot" id="slot-119">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Alentejo</div>
                            <div class="slot-role">Planícies, Évora e Costa Vicentina</div>
                        </div>
                        <div class="sticker-slot" id="slot-120">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Faro (Algarve)</div>
                            <div class="slot-role">Praias Paradisíacas e Falésias</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 16</div>
                </div>
            </div>
            
            <!-- PAGINA 17: PORTUGAL - ILHAS -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #006600 0%, #004d00 100%); color: #ffffff; border-left: 3px solid #FF0000;">🇵🇹 PORTUGAL</span>
                        <h3 class="page-title">Ilhas Autónomas</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-121">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Região Autónoma dos Açores</div>
                            <div class="slot-role">Sete Cidades e Vulcanismo</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-122">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Região Autónoma da Madeira</div>
                            <div class="slot-role">Funchal e Floresta Laurissilva</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 17</div>
                </div>
            </div>

            <!-- PAGINA 18: GUINÉ-BISSAU - NORTE/LESTE -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇬🇼 GUINÉ-BISSAU</span>
                        <h3 class="page-title">Norte e Leste</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-131">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Província do Norte</div>
                            <div class="slot-role">Cacheu, Oio e Biombo</div>
                        </div>
                        <div class="sticker-slot" id="slot-132">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Província do Leste</div>
                            <div class="slot-role">Gabu e Bafatá • Savanas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 18</div>
                </div>
            </div>

            <!-- PAGINA 19: GUINÉ-BISSAU - SUL -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #CE1126 0%, #9e0d1d 100%); color: #ffffff; border-left: 3px solid #FCD116;">🇬🇼 GUINÉ-BISSAU</span>
                        <h3 class="page-title">Sul e Bissau</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-133">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Bissau</div>
                            <div class="slot-role">Capital • Centro Histórico</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-134">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Província do Sul & Bijagós</div>
                            <div class="slot-role">Arquipélago dos Bijagós</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 19</div>
                </div>
            </div>

            <!-- PAGINA 20: CABO VERDE - BARLAVENTO -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #003893 0%, #00225c 100%); color: #ffffff; border-left: 3px solid #CF2027;">🇨🇻 CABO VERDE</span>
                        <h3 class="page-title">Ilhas de Barlavento</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-141">
                            <div class="slot-number">#</div>
                            <div class="slot-name">São Vicente e Santo Antão</div>
                            <div class="slot-role">Mindelo • Cultura e Montanhas</div>
                        </div>
                        <div class="sticker-slot" id="slot-142">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Sal e Boa Vista</div>
                            <div class="slot-role">Praias, Salinas e Dunas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 20</div>
                </div>
            </div>
            
            <!-- PAGINA 21: CABO VERDE - SOTAVENTO -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #003893 0%, #00225c 100%); color: #ffffff; border-left: 3px solid #CF2027;">🇨🇻 CABO VERDE</span>
                        <h3 class="page-title">Ilhas de Sotavento</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-143">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Santiago</div>
                            <div class="slot-role">Capital Praia • Cidade Velha</div>
                        </div>
                        <div class="sticker-slot" id="slot-144">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Fogo, Brava e Maio</div>
                            <div class="slot-role">Vulcão do Fogo e Ilhas Isoladas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 21</div>
                </div>
            </div>

            <!-- PAGINA 22: SÃO TOMÉ E PRÍNCIPE - SÃO TOMÉ -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #12AD2B 0%, #0d7a1e 100%); color: #ffffff; border-left: 3px solid #FFCE00;">🇸🇹 SÃO TOMÉ E PRÍNCIPE</span>
                        <h3 class="page-title">Ilha de São Tomé</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-151">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Água Grande (Capital)</div>
                            <div class="slot-role">São Tomé • Arquitetura Colonial</div>
                        </div>
                        <div class="sticker-slot" id="slot-152">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Pico Cão Grande</div>
                            <div class="slot-role">Lembá • Natureza Selvagem</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 22</div>
                </div>
            </div>

            <!-- PAGINA 23: SÃO TOMÉ E PRÍNCIPE - PRÍNCIPE -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #12AD2B 0%, #0d7a1e 100%); color: #ffffff; border-left: 3px solid #FFCE00;">🇸🇹 SÃO TOMÉ E PRÍNCIPE</span>
                        <h3 class="page-title">Ilha do Príncipe</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-153">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Região Autónoma do Príncipe</div>
                            <div class="slot-role">Santo António • Biosfera da UNESCO</div>
                        </div>
                        <div class="sticker-slot" id="slot-154">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Praia Banana</div>
                            <div class="slot-role">Praias Paradisíacas e Virgens</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 23</div>
                </div>
            </div>

            <!-- PAGINA 24: GUINÉ EQUATORIAL - INSULAR -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #3E9A00 0%, #2b6b00 100%); color: #ffffff; border-left: 3px solid #E32118;">🇬🇶 GUINÉ EQUATORIAL</span>
                        <h3 class="page-title">Região Insular</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-161">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Bioco (Malabo)</div>
                            <div class="slot-role">Capital • Ilha Vulcânica</div>
                        </div>
                        <div class="sticker-slot" id="slot-162">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Annobón</div>
                            <div class="slot-role">A Ilha Mais a Sul do Equador</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 24</div>
                </div>
            </div>

            <!-- PAGINA 25: GUINÉ EQUATORIAL - CONTINENTAL -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #3E9A00 0%, #2b6b00 100%); color: #ffffff; border-left: 3px solid #E32118;">🇬🇶 GUINÉ EQUATORIAL</span>
                        <h3 class="page-title">Região Continental</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-163">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Litoral (Bata)</div>
                            <div class="slot-role">Maior Cidade e Centro Econômico</div>
                        </div>
                        <div class="sticker-slot" id="slot-164">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Rio Muni Interior</div>
                            <div class="slot-role">Florestas Tropicais Densas</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 25</div>
                </div>
            </div>

            <!-- PAGINA 26: TIMOR-LESTE - NORTE/SUL -->
            <div class="page page-right">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #FF0000 0%, #cc0000 100%); color: #ffffff; border-left: 3px solid #000000;">🇹🇱 TIMOR-LESTE</span>
                        <h3 class="page-title">Costas Norte e Sul</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot special-slot" id="slot-171">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Díli e Costa Norte</div>
                            <div class="slot-role">Capital • Cristo Rei e Baucau</div>
                        </div>
                        <div class="sticker-slot" id="slot-172">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Costa Sul</div>
                            <div class="slot-role">Viqueque e Ainaro • Mar de Timor</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 26</div>
                </div>
            </div>
            
            <!-- PAGINA 27: TIMOR-LESTE - INTERIOR/ESPECIAIS -->
            <div class="page page-left">
                <div class="page-content">
                    <div class="page-header">
                        <span class="tech-badge" style="background: linear-gradient(135deg, #FF0000 0%, #cc0000 100%); color: #ffffff; border-left: 3px solid #000000;">🇹🇱 TIMOR-LESTE</span>
                        <h3 class="page-title">Interior & Especiais</h3>
                    </div>
                    <div class="stickers-grid">
                        <div class="sticker-slot" id="slot-173">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Interior Montanhoso</div>
                            <div class="slot-role">Aileu e Ermera • Plantações de Café</div>
                        </div>
                        <div class="sticker-slot special-slot" id="slot-174">
                            <div class="slot-number">#</div>
                            <div class="slot-name">Regiões Especiais</div>
                            <div class="slot-role">Enclave de Oe-Cusse e Ilha de Ataúro</div>
                        </div>
                    </div>
                    <div class="page-footer">Pág. 27</div>
                </div>
            </div>

            <!-- PAGINA 28: COMUNIDADE E PROJETO -->
            <div class="page page-right">
                <div class="page-content" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; height:100%; padding: 30px;">
                    <h2 style="font-family: 'Outfit', sans-serif; color: var(--color-deep-blue); font-size: 2.1rem; margin-bottom: 15px;">Ajude a Completar!</h2>
                    <p style="color: #444; font-size: 1rem; line-height: 1.4; max-width: 95%;">
                        Este projeto é Open Source e aberto a contribuições! Estudantes da Alura e membros de toda a CPLP podem fazer um Fork e ajudar com fotos e dados.
                    </p>
                    <div style="margin-top: 15px; padding: 15px; background: rgba(31, 83, 229, 0.1); border-radius: 12px; border: 2px dashed var(--color-dev-blue); width: 100%;">
                        <ul style="text-align: left; font-size: 0.9rem; color: #555; padding-left: 20px; line-height: 1.4; margin: 0;">
                            <li>Abra o `README.md` no GitHub</li>
                            <li>Adicione fotos na pasta `/figurinhas`</li>
                            <li>Insira os dados no `main.py`</li>
                            <li>Submeta o Pull Request</li>
                        </ul>
                    </div>
                    
                    <div style="margin-top: 25px; text-align: left; width: 100%;">
                        <h4 style="color: var(--color-tech-blue); font-family: 'Outfit', sans-serif; font-size: 1.4rem; margin-bottom: 8px; border-bottom: 1px solid #ddd; padding-bottom: 4px;">Sobre o Projeto</h4>
                        <p style="color: #555; font-size: 0.85rem; line-height: 1.4; margin-bottom: 10px;">
                            Desenvolvido para fortalecer laços entre desenvolvedores lusófonos e partilhar a cultura e geografia da CPLP.
                        </p>
                        <p style="color: #444; font-size: 0.85rem; line-height: 1.4; margin-bottom: 10px; padding-left: 10px; border-left: 3px solid var(--color-dev-blue);">
                            <strong>Agradecimentos:</strong> Os conhecimentos aplicados para o desenvolvimento deste projeto foram adquiridos na Imersão IA da Alura.
                        </p>
                        <p style="color: #555; font-size: 0.85rem; line-height: 1.4; margin: 0;">
                            <strong>Autor:</strong> Felton da Silva<br>
                            <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/estevafelton/" target="_blank" style="color: var(--color-tech-blue); text-decoration: none;">linkedin.com/in/estevafelton</a>
                        </p>
                    </div>

                    <div class="page-footer" style="width: 100%; position:absolute; bottom: 45px; left:0; padding: 0 40px; box-sizing: border-box;">Pág. 28</div>
                </div>
            </div>
"""

# Try to find the start marker. We will search for "<!-- PAGINA 1" to cover both variants.
start_idx = content.find("<!-- PAGINA 1:")
end_idx = content.find('<div class="page page-cover-back"')

if start_idx != -1 and end_idx != -1:
    comment_end_idx = content.rfind('<!--', start_idx, end_idx)
    
    new_content = content[:start_idx] + new_pages + "\n            " + content[comment_end_idx:]
    with open('i-arq-ia-alura-album-main/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Sucesso HTML gerado 30 páginas e Índice restaurado!")
else:
    print(f"Padrão não encontrado. start={start_idx}, end={end_idx}")
