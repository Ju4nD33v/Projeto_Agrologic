import os

base_dir = r"c:\Users\JUAN\Desktop\reconhecimento-imagem-eng-Juan-Pedro-Ribeiro\agrologic_1"

head_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgroLogic</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
"""

tail_html = """
    <!-- Modals & Overlays -->
    <div id="modal-container" class="modal-overlay" style="display: none;"></div>
    
    <!-- Chat Widget -->
    <div id="chat-widget" class="chat-widget" style="display: none;">
        <div class="chat-header">
            <div><i class="fa-solid fa-headset"></i> Suporte AgroLogic</div>
            <i class="fa-solid fa-xmark" style="cursor:pointer;" onclick="app.fecharChat()"></i>
        </div>
        <div class="chat-body" id="chat-messages">
            <div class="message system">Seu atendimento foi iniciado</div>
            <div class="message system">Nossa equipe responderá em breve</div>
        </div>
        <div class="chat-footer">
            <input type="text" placeholder="Digite sua mensagem..." id="chat-input" onkeypress="if(event.key === 'Enter') app.enviarMensagemChat()">
            <button onclick="app.enviarMensagemChat()"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

landing_nav = """
        <header class="landing-header">
            <div class="logo">AGROLOGIC</div>
            <nav class="landing-nav">
                <a href="index.html" class="nav-link">Início</a>
                <a href="#" class="nav-link">Sobre o projeto</a>
                <a href="#" class="nav-link">Funcionalidades</a>
                <button class="btn-outline-yellow" onclick="window.location.href='login.html'">Login</button>
            </nav>
        </header>
"""

pages = {}

pages['index.html'] = f"""{head_html}
    <div class="auth-bg">
{landing_nav}
        <main class="landing-main">
            <div class="landing-content">
                <h1>Mais eficiência no<br>campo, mais lucro<br>no seu bolso</h1>
                <ul class="features-list">
                    <li>Acompanhamento da safra</li>
                    <li>Monitoramento do Solo</li>
                    <li>Relatorios inteligentes</li>
                </ul>
                <button class="btn-primary-yellow btn-large" onclick="window.location.href='cadastro.html'">
                    <span class="icon-circle"></span> CADASTRE-SE AGORA
                </button>
            </div>
            <div class="landing-graphics">
                <div class="leaf-logo">
                    <img src="https://cdn-icons-png.flaticon.com/512/628/628283.png" alt="Leaf" class="main-leaf" style="filter: hue-rotate(90deg) brightness(1.2);">
                </div>
                <div class="decorative-circle small-top"></div>
                <div class="decorative-circle large-bottom-left"></div>
                <div class="decorative-circle medium-bottom-right"></div>
                <div class="decorative-swoosh"></div>
            </div>
        </main>
    </div>
{tail_html}"""

pages['login.html'] = f"""{head_html}
    <div class="auth-bg">
{landing_nav}
        <div class="auth-container">
            <div class="auth-card">
                <div class="auth-logo">
                    <i class="fa-solid fa-seedling"></i> AGROLOGIC
                </div>
                <h2>Bem Vindo de volta</h2>
                <p class="auth-subtitle">Entre utilizando<br>Google | Apple | Microsoft</p>
                <div class="social-logins">
                    <i class="fa-brands fa-google" style="color: #DB4437;"></i>
                    <span class="divider">|</span>
                    <i class="fa-brands fa-apple" style="color: #000;"></i>
                    <span class="divider">|</span>
                    <i class="fa-brands fa-windows" style="color: #00A4EF;"></i>
                </div>
                <div class="separator">
                    <span>Entre com seu login e senha</span>
                </div>
                <form class="auth-form" onsubmit="app.login(event, 'login')">
                    <div class="form-group">
                        <input type="text" placeholder="e-mail ou Telefone" required>
                    </div>
                    <div class="form-group password-group">
                        <input type="password" placeholder="senha" required>
                        <i class="fa-solid fa-eye-slash"></i>
                    </div>
                    <button type="submit" class="btn-green-solid">Entrar</button>
                </form>
                <div class="auth-footer">
                    <a href="#">Esqueci minha senha</a>
                    <a href="cadastro.html">Cadastre-se</a>
                </div>
            </div>
        </div>
    </div>
{tail_html}"""

pages['cadastro.html'] = f"""{head_html}
    <div class="auth-bg">
{landing_nav}
        <div class="auth-container">
            <div class="auth-card">
                <div class="auth-logo">
                    <i class="fa-solid fa-seedling"></i> AGROLOGIC
                </div>
                <h2>Bem Vindo</h2>
                <p class="auth-subtitle">Crie utilizando<br>Google | Apple | Microsoft</p>
                <div class="social-logins">
                    <i class="fa-brands fa-google" style="color: #DB4437;"></i>
                    <span class="divider">|</span>
                    <i class="fa-brands fa-apple" style="color: #000;"></i>
                    <span class="divider">|</span>
                    <i class="fa-brands fa-windows" style="color: #00A4EF;"></i>
                </div>
                <div class="separator">
                    <span>ou<br>Insira suas credenciais</span>
                </div>
                <form class="auth-form dual-col" onsubmit="app.login(event, 'cadastro')">
                    <div class="form-group"><input type="text" placeholder="Nome:" required></div>
                    <div class="form-group"><input type="text" placeholder="Sobrenome:" required></div>
                    <div class="form-group"><input type="text" placeholder="e-mail ou Telefone:" required></div>
                    <div class="form-group">
                        <select required>
                            <option value="" disabled selected>Profissão:</option>
                            <option>Agrônomo</option>
                            <option>Produtor</option>
                        </select>
                    </div>
                    <div class="form-group password-group">
                        <input type="password" placeholder="senha:" required>
                        <i class="fa-solid fa-eye-slash"></i>
                    </div>
                    <div class="form-group"><input type="password" placeholder="Confirme sua senha:" required></div>
                    
                    <button type="submit" class="btn-green-solid full-width" style="grid-column: span 2;">Cadastrar</button>
                </form>
                <div class="auth-footer center">
                    <a href="login.html" class="login-link-large">Login</a>
                </div>
            </div>
        </div>
    </div>
{tail_html}"""

def get_app_layout(active_page, title, content):
    menus = [
        ('dashboard.html', 'Painel', 'fa-table-cells-large'),
        ('safras.html', 'Safras', 'fa-wheat-awn'),
        ('registrar-safra.html', 'Registrar Safra', 'fa-plant-wilt'),
        ('relatorios.html', 'Relatórios', 'fa-clipboard-list'),
        ('analise.html', 'Análise', 'fa-chart-line')
    ]
    
    menu_html = ""
    for url, text, icon in menus:
        active_class = "active" if active_page == text else ""
        menu_html += f"""
                <a href="{url}" class="menu-item {active_class}">
                    <i class="fa-solid {icon}"></i><span>{text}</span>
                </a>"""
                
    sup_active = "active" if active_page == "SUPORTE" else ""
    
    return f"""{head_html}
    <div class="app-layout">
        <aside class="sidebar">
            <div class="sidebar-logo">
                <div class="icon-bg"><i class="fa-solid fa-leaf"></i></div>
            </div>
            <nav class="sidebar-menu">
                {menu_html}
            </nav>
            <div class="sidebar-footer">
                <a href="suporte.html" class="menu-item {sup_active}">
                    <i class="fa-solid fa-circle-question"></i><span>Suporte</span>
                </a>
            </div>
        </aside>

        <header class="topbar">
            <div class="search-bar">
                <input type="text" placeholder="Procurar">
                <i class="fa-solid fa-magnifying-glass"></i>
            </div>
            <h1 class="page-title">{title}</h1>
            <div class="topbar-actions">
                <i class="fa-regular fa-comment-dots"></i>
                <div style="position:relative; display:inline-block;">
                    <i class="fa-regular fa-bell" style="cursor:pointer;" onclick="app.toggleNotifications(event)"></i>
                    <div id="notif-dropdown" class="notif-dropdown"></div>
                </div>
                <span class="user-name">Nome</span>
                <div class="user-avatar"></div>
            </div>
        </header>

        <main class="app-content">
            <div class="sub-view active">
                {content}
            </div>
        </main>
    </div>
{tail_html}"""

dashboard_content = """
                <div class="dashboard-grid">
                    <div class="weather-widget dark-panel">
                        <div class="weather-header">
                            <span><i class="fa-solid fa-location-dot"></i> Franca - SP</span>
                            <a href="#">Escolher região</a>
                            <i class="fa-solid fa-ellipsis-vertical"></i>
                        </div>
                        <div class="weather-current">
                            <i class="fa-solid fa-sun weather-icon"></i>
                            <div class="temp">23<span>°C|°F</span></div>
                            <div class="details">
                                Chuva: 0%<br>Umidade: 55%<br>Vento: 5 km/h
                            </div>
                        </div>
                        <div class="weather-forecast">
                            <div class="day"><span>sex.</span><i class="fa-solid fa-cloud-sun"></i><span>27° 16°</span></div>
                            <div class="day"><span>sáb.</span><i class="fa-solid fa-sun"></i><span>28° 18°</span></div>
                            <div class="day"><span>dom.</span><i class="fa-solid fa-cloud-sun"></i><span>28° 17°</span></div>
                            <div class="day"><span>seg.</span><i class="fa-solid fa-sun"></i><span>28° 17°</span></div>
                            <div class="day"><span>ter.</span><i class="fa-solid fa-sun"></i><span>28° 17°</span></div>
                            <div class="day"><span>qua.</span><i class="fa-solid fa-sun"></i><span>28° 17°</span></div>
                            <div class="day"><span>qui.</span><i class="fa-solid fa-sun"></i><span>28° 17°</span></div>
                            <div class="day"><span>sex.</span><i class="fa-solid fa-cloud-sun"></i><span>28° 18°</span></div>
                        </div>
                    </div>

                    <div class="chart-card card">
                        <div class="card-header">
                            <h2><i class="fa-solid fa-chart-simple"></i> Cotação de grãos:</h2>
                            <div class="time-filters">
                                <span style="cursor:pointer;" onclick="app.updateChart('dashboard', this)">7 dias</span>
                                <span style="cursor:pointer;" class="active" onclick="app.updateChart('dashboard', this)">30 dias</span>
                                <span style="cursor:pointer;" class="green-bg" onclick="app.updateChart('dashboard', this)">1 ano</span>
                            </div>
                        </div>
                        <div class="chart-legend">
                            <span class="dot green"></span> Café Ara
                            <span class="dot red"></span> Soja
                            <span class="dot cyan"></span> Milho
                            <span class="dot white"></span> Algodão
                        </div>
                        <div class="chart-container dark-chart-bg">
                            <canvas id="cotacaoChart"></canvas>
                        </div>
                    </div>

                    <div class="alerts-card card">
                        <div class="card-header">
                            <h2><i class="fa-solid fa-bell text-yellow"></i> Alertas:</h2>
                        </div>
                        <ul class="alerts-list">
                            <li><i class="fa-solid fa-triangle-exclamation text-red"></i> Baixa umidade no solo</li>
                            <li><i class="fa-solid fa-arrow-trend-down text-gray"></i> Queda no preço do café</li>
                            <li><i class="fa-solid fa-cloud-bolt text-gray"></i> Previsão de chuva</li>
                        </ul>
                        <div class="text-right"><strong>Ver todos</strong></div>
                    </div>

                    <div class="summary-card card">
                        <h3><i class="fa-solid fa-wheat-awn text-yellow"></i> Resumo da Safra de soja 2026:</h3>
                        <div class="summary-row"><i class="fa-solid fa-leaf"></i> Cultura: <span>Soja</span></div>
                        <div class="summary-row"><i class="fa-solid fa-location-dot"></i> Área: <span>13 Hectares</span></div>
                        <div class="summary-row"><i class="fa-solid fa-clipboard-check"></i> Status: <span><span class="dot-status green"></span> Crescimento</span></div>
                        <div class="summary-row"><i class="fa-solid fa-stopwatch"></i> Previsão: <span>17/04/2027</span></div>
                    </div>

                    <div class="summary-card card">
                        <h3><i class="fa-solid fa-wheat-awn text-yellow"></i> Resumo da safra de milho 2025:</h3>
                        <div class="summary-row"><i class="fa-solid fa-leaf"></i> Cultura: <span>Milho</span></div>
                        <div class="summary-row"><i class="fa-solid fa-location-dot"></i> Área: <span>13 Hectares</span></div>
                        <div class="summary-row"><i class="fa-solid fa-clipboard-check"></i> Status: <span><span class="dot-status green"></span> Crescimento</span></div>
                        <div class="summary-row"><i class="fa-solid fa-stopwatch"></i> Previsão: <span>15/06/2026</span></div>
                    </div>
                </div>
"""
pages['dashboard.html'] = get_app_layout('Painel', 'Painel', dashboard_content)

safras_content = """
                <div class="safras-layout">
                    <div class="safras-list-panel">
                        <button class="btn-primary-yellow full-width mb-15" onclick="window.location.href='registrar-safra.html'">
                            <i class="fa-solid fa-plus"></i> Nova safra
                        </button>
                        
                        <div class="safra-item-card active">
                            <div class="safra-item-title">Safra de soja 2026 <i class="fa-solid fa-chevron-right float-right"></i></div>
                            <div class="safra-item-cultura"><i class="fa-solid fa-leaf text-green"></i> Soja</div>
                            <div class="progress-bar-container"><div class="progress-bar green" style="width: 70%"></div></div>
                            <div class="safra-item-date"><i class="fa-regular fa-calendar"></i> Plantio: 01/04/2026</div>
                            <div class="safra-item-date"><i class="fa-regular fa-clock"></i> Previsão: 15/02/2027</div>
                        </div>

                        <div class="safra-item-card" onclick="app.changeSafra('milho')" style="cursor:pointer;">
                            <div class="safra-item-title">Safra de milho 2025 <i class="fa-solid fa-chevron-right float-right"></i></div>
                            <div class="safra-item-cultura"><i class="fa-solid fa-seedling text-yellow"></i> Milho</div>
                            <div class="progress-bar-container"><div class="progress-bar green" style="width: 85%"></div></div>
                            <div class="safra-item-date"><i class="fa-regular fa-calendar"></i> Plantio: 01/04/2025</div>
                            <div class="safra-item-date"><i class="fa-regular fa-clock"></i> Previsão: 15/06/2026</div>
                        </div>

                        <div class="safra-item-card" onclick="app.changeSafra('algodao')" style="cursor:pointer;">
                            <div class="safra-item-title">Safra de algodão 2024 <i class="fa-solid fa-chevron-right float-right"></i></div>
                            <div class="safra-item-cultura"><i class="fa-solid fa-fan text-gray"></i> Algodão</div>
                            <div class="progress-bar-container"><div class="progress-bar dark-green" style="width: 100%"></div></div>
                            <div class="safra-item-date"><i class="fa-regular fa-calendar"></i> Plantio: 10/02/2024</div>
                            <div class="safra-item-date"><i class="fa-regular fa-clock"></i> Previsão: 15/10/2024</div>
                        </div>
                    </div>
                    
                    <div class="safras-details-panel">
                        <div class="details-header">
                            <h2>Safra de soja 2026</h2>
                            <div class="details-actions">
                                <button class="btn-outline-gray" onclick="app.editarSafra()"><i class="fa-solid fa-pen"></i> Editar</button>
                                <button class="btn-outline-gray" onclick="app.showRelatorioA4()"><i class="fa-solid fa-file-invoice"></i> Relatório</button>
                                <button class="btn-outline-gray text-red" onclick="app.deleteSafra()"><i class="fa-regular fa-trash-can"></i> Excluir</button>
                            </div>
                        </div>

                        <div class="card info-hero">
                            <div class="hero-title"><i class="fa-solid fa-leaf text-green"></i> Soja</div>
                            <div class="permissions">
                                <div>Permissões: <br><strong>Pedro ID(4354) Agrônomo</strong></div>
                                <i class="fa-solid fa-user"></i>
                                <i class="fa-solid fa-pen" style="cursor:pointer;" onclick="app.editPermissions()"></i>
                            </div>
                        </div>

                        <div class="details-grid">
                            <div class="card basic-info">
                                <div><i class="fa-solid fa-location-dot"></i> 120 Hectares</div>
                                <div><i class="fa-regular fa-calendar"></i> Inicio do plantio: 01/04/2026</div>
                                <div><i class="fa-regular fa-clock"></i> Previsão de colheita: 15/02/2027</div>
                            </div>

                            <div class="card evolution-chart-container" style="grid-row: span 2;">
                                <div class="card-header">
                                    <h3>Evolução da safra</h3>
                                    <div class="time-filters">
                                        <span style="cursor:pointer;" onclick="app.updateChart('safras', this)">7 Dias</span>
                                        <span style="cursor:pointer;" class="active" onclick="app.updateChart('safras', this)">30 Dias</span>
                                        <span style="cursor:pointer;" onclick="app.updateChart('safras', this)">1 Ano</span>
                                    </div>
                                </div>
                                <div style="height: 160px; position: relative;">
                                    <canvas id="evolucaoChart"></canvas>
                                </div>
                                <div class="chart-legend-center"><span class="dot green"></span> Produtividade estimada</div>
                            </div>

                            <div class="card dados-solo">
                                <h3>Dados do solo</h3>
                                <div class="solo-widgets">
                                    <div class="solo-widget">
                                        <div class="solo-icon blue"><i class="fa-solid fa-droplet"></i> %</div>
                                        <div><strong>55%</strong><br>Umidade <i class="fa-solid fa-arrow-up text-green"></i></div>
                                    </div>
                                    <div class="solo-widget">
                                        <div class="solo-icon dark"><i class="fa-solid fa-flask"></i> NPK</div>
                                        <div><strong>10-30-20</strong></div>
                                    </div>
                                    <div class="solo-widget full-width">
                                        <div class="solo-icon light-blue"><i class="fa-solid fa-droplet"></i> pH</div>
                                        <div><strong>pH 6.2</strong> <i class="fa-solid fa-arrow-up text-green float-right mt-10"></i></div>
                                    </div>
                                </div>
                            </div>

                            <div class="card alertas-safra">
                                <div class="card-header">
                                    <h3>Alertas da safra</h3>
                                    <span class="text-green small">Ver todos</span>
                                </div>
                                <ul class="alerts-list">
                                    <li><i class="fa-solid fa-triangle-exclamation text-red"></i> Baixa umidade do solo <span class="text-green float-right">!</span></li>
                                    <li><i class="fa-solid fa-cloud-bolt text-gray"></i> Previsão de chuva <span class="text-green float-right">!</span></li>
                                    <li><i class="fa-solid fa-arrow-trend-down text-red"></i> Queda no preço da soja <span class="text-green small float-right">Ver todos</span></li>
                                </ul>
                            </div>

                            <div class="card gastos-iniciais">
                                <div class="card-header">
                                    <h3>Gastos iniciais</h3>
                                    <span class="text-green small">Ver mais</span>
                                </div>
                                <div class="mt-15"><strong>Qtd sementes nescessarias:</strong></div>
                                <div class="mt-10"><strong>Qtd de grafite nescessario:</strong></div>
                                <button class="btn-outline-gray float-right mt-15">Finalizar plantio</button>
                            </div>
                        </div>
                    </div>
                </div>
"""
pages['safras.html'] = get_app_layout('Safras', 'Safras', safras_content)


registrar_safra_content = """
                <div class="card form-header mb-15">
                    <div class="icon-circle-large"><i class="fa-solid fa-leaf text-green"></i></div>
                    <div>
                        <h2>Nova Safra</h2>
                        <p>Preencha os dados para iniciar o acompanhamento produtivo.</p>
                    </div>
                </div>

                <div class="registrar-grid">
                    <div class="registrar-form-col">
                        <div class="card">
                            <h3><i class="fa-solid fa-clipboard-list text-green"></i> Informações da Safra</h3>
                            <div class="form-row">
                                <label>Cultura</label>
                                <select id="cultura-atual" class="form-input" onchange="app.updateResumoSafra()">
                                    <option value="Soja">Soja</option>
                                    <option value="Milho">Milho</option>
                                    <option value="Algodão">Algodão</option>
                                </select>
                            </div>
                            <div class="form-row">
                                <label>Qtd de semente por Pé</label>
                                <input type="text" class="form-input" placeholder="Ex:3 Und">
                            </div>
                            <div class="form-row">
                                <label>Distancia fileiras</label>
                                <input type="text" class="form-input" placeholder="Ex: 102cm">
                            </div>
                            <div class="form-row">
                                <label>Distancia pés</label>
                                <input type="text" class="form-input" placeholder="Ex: 56cm">
                            </div>
                        </div>

                        <div class="card mt-15">
                            <h3><i class="fa-solid fa-mound text-brown"></i> Dados iniciais do solo</h3>
                            <div class="form-row">
                                <label>Cultura anterior</label>
                                <select id="cultura-anterior" class="form-input">
                                    <option value="Milho">Milho</option>
                                    <option value="Cana-de-açúcar">Cana-de-açúcar</option>
                                </select>
                            </div>
                            <div class="form-row">
                                <label>pH</label>
                                <input type="text" class="form-input" value="6.2">
                            </div>
                            <div class="form-row">
                                <label>NPK</label>
                                <input type="text" class="form-input" value="10-30-20">
                            </div>
                            <div class="form-row">
                                <label>Umidade</label>
                                <input type="text" class="form-input" value="55%">
                            </div>
                        </div>
                    </div>

                    <div class="registrar-form-col">
                        <div class="card">
                            <h3><i class="fa-solid fa-seedling text-green"></i> </h3>
                            <div class="form-row">
                                <label>Área plantada</label>
                                <input type="text" id="area-plantada" class="form-input" value="13 ha" oninput="app.updateResumoSafra()">
                            </div>
                            <div class="form-row">
                                <label>Talhão</label>
                                <input type="text" class="form-input" value="13 ha">
                            </div>
                            <div class="form-row">
                                <label>Data do plantio</label>
                                <input type="date" id="data-plantio" class="form-input" value="2025-04-01" onchange="app.updateResumoSafra()">
                            </div>
                            <div class="form-row">
                                <label>Localização</label>
                                <div class="input-with-icon">
                                    <input type="text" id="localizacao" class="form-input" placeholder="Opcional:" oninput="app.updateResumoSafra()">
                                    <i class="fa-solid fa-location-dot"></i>
                                </div>
                            </div>
                        </div>

                        <div class="card mt-15">
                            <h3><i class="fa-regular fa-file-lines text-green"></i> Observações</h3>
                            <textarea class="form-input" rows="4">Área preparada para plantio. Monitorar umidade nos proximos 7 dias</textarea>
                        </div>
                    </div>

                    <div class="registrar-summary-col">
                        <div class="card resumo-side">
                            <div class="ribbon"><i class="fa-solid fa-bookmark"></i></div>
                            <h3>Resumo da safra</h3>
                            <div class="resumo-item">
                                <div class="icon-circle-bg"><i class="fa-solid fa-leaf text-green"></i></div>
                                <div>
                                    <span class="label">Cultura</span><br>
                                    <strong>Soja</strong>
                                </div>
                            </div>
                            <div class="resumo-item border-top">
                                <div class="icon-circle-bg"><i class="fa-solid fa-tree text-green"></i></div>
                                <div>
                                    <span class="label">Area plantada</span><br>
                                    <strong>13 ha</strong>
                                </div>
                            </div>
                            <div class="resumo-item border-top">
                                <div class="icon-circle-bg"><i class="fa-solid fa-tractor text-green"></i></div>
                                <div>
                                    <span class="label">Localização</span><br>
                                    <strong>Não informado</strong>
                                </div>
                            </div>
                            <div class="resumo-item border-top">
                                <div class="icon-circle-bg"><i class="fa-regular fa-calendar-check text-green"></i></div>
                                <div>
                                    <span class="label">Previsão de colheita</span><br>
                                    <strong>15/06/2025</strong>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="registrar-actions card mt-15">
                    <button class="btn-outline-gray" onclick="window.location.href='safras.html'">Cancelar</button>
                    <button class="btn-primary-yellow" onclick="app.salvarSafra()">Salvar safra</button>
                </div>
"""
pages['registrar-safra.html'] = get_app_layout('Registrar Safra', 'Registro de safras', registrar_safra_content)

relatorios_content = """
                <div class="card form-header mb-15 space-between">
                    <div class="flex-row">
                        <div class="icon-circle-large"><i class="fa-solid fa-clipboard-check text-green"></i></div>
                        <div>
                            <h2>Relatórios</h2>
                            <p>Visualize e exporte informações estratégias das suas safras.</p>
                        </div>
                    </div>
                    <button class="btn-primary-yellow" onclick="app.showRelatorioA4()"><i class="fa-solid fa-plus"></i> Novo relatório</button>
                </div>

                <div class="stats-grid mb-15">
                    <div class="card stat-item">
                        <div class="icon"><i class="fa-solid fa-file-lines text-green"></i></div>
                        <div class="info">Total de relatórios<br><strong>12</strong></div>
                    </div>
                    <div class="card stat-item">
                        <div class="icon"><i class="fa-solid fa-seedling text-green"></i></div>
                        <div class="info">safras analisadas<br><strong>4</strong></div>
                    </div>
                    <div class="card stat-item">
                        <div class="icon"><i class="fa-solid fa-chart-line text-green"></i></div>
                        <div class="info">Produtividade média<br><strong>78%</strong></div>
                    </div>
                    <div class="card stat-item">
                        <div class="icon"><i class="fa-regular fa-calendar-days text-green"></i></div>
                        <div class="info">Último relatório<br><strong>17/04/2027</strong></div>
                    </div>
                </div>

                <div class="card mb-15">
                    <h3><i class="fa-solid fa-filter"></i> Filtrar relatórios</h3>
                    <div class="filters-row">
                        <div class="filter-group">
                            <label>Tipo de relatório</label>
                            <select><option>safra</option></select>
                        </div>
                        <div class="filter-group">
                            <label>safra</label>
                            <select><option>safra de soja 2025</option></select>
                        </div>
                        <div class="filter-group">
                            <label>Período</label>
                            <select><option>Últimos 30 dias</option></select>
                        </div>
                        <div class="filter-group">
                            <label>Status</label>
                            <select><option>Gerado</option></select>
                        </div>
                        <div class="filter-actions">
                            <button class="btn-primary-yellow" onclick="app.aplicarFiltros()">Aplicar filtros</button>
                            <button class="btn-outline-gray">Limpar</button>
                        </div>
                    </div>
                </div>

                <div class="relatorios-charts-grid mb-15">
                    <div class="card">
                        <h3>Desempenho das Safras</h3>
                        <div style="height: 150px; position: relative; margin-top: 10px;">
                            <canvas id="desempenhoChart"></canvas>
                        </div>
                    </div>
                    <div class="card">
                        <h3>Exportações</h3>
                        <p class="small text-gray">Escolha o formato para exportar seus relatórios</p>
                        <div class="export-buttons">
                            <button class="btn-export" onclick="app.exportar('PDF')"><i class="fa-solid fa-file-pdf text-red"></i> PDF</button>
                            <button class="btn-export" onclick="app.exportar('Excel')"><i class="fa-solid fa-file-excel text-green"></i> EXCEL</button>
                            <button class="btn-export" onclick="app.exportar('CSV')"><i class="fa-solid fa-file-csv text-green"></i> CSV</button>
                        </div>
                        <div class="mt-15 pt-15 border-top">
                            <strong>Arquivos exportados: 8</strong>
                            <button class="btn-primary-yellow full-width mt-10" onclick="app.exportar('Tudo')"><i class="fa-solid fa-download"></i> Exportar tudo</button>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <h3>Relatórios Recentes</h3>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Relatório</th><th>Safra</th><th>Tipo</th><th>Data</th><th>Status</th><th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Relatório da Safra de Soja</strong></td><td>Soja 2025</td><td>Safra</td><td>17/04/2027</td>
                                <td><span class="badge green">Gerado</span></td>
                                <td>
                                    <button class="btn-sm" onclick="app.showRelatorioA4()"><i class="fa-solid fa-eye"></i> Ver</button>
                                    <button class="btn-sm" onclick="app.exportar('PDF')"><i class="fa-solid fa-file-pdf text-red"></i> PDF</button> <i class="fa-solid fa-ellipsis-vertical"></i>
                                </td>
                            </tr>
                            <tr>
                                <td><strong>Análise do solo</strong></td><td>Soja 2025</td><td>Solo</td><td>10/04/2027</td>
                                <td><span class="badge blue">Exportado</span></td>
                                <td>
                                    <button class="btn-sm"><i class="fa-solid fa-eye"></i> Ver</button>
                                    <button class="btn-sm" onclick="app.exportar('Excel')"><i class="fa-solid fa-file-excel text-green"></i> Excel</button> <i class="fa-solid fa-ellipsis-vertical"></i>
                                </td>
                            </tr>
                            <tr>
                                <td><strong>Cotação de Grãos</strong></td><td>Geral</td><td>Mercado</td><td>05/04/2027</td>
                                <td><span class="badge green">Gerado</span></td>
                                <td>
                                    <button class="btn-sm"><i class="fa-solid fa-eye"></i> Ver</button>
                                    <button class="btn-sm" onclick="app.exportar('PDF')"><i class="fa-solid fa-file-pdf text-red"></i> PDF</button> <i class="fa-solid fa-ellipsis-vertical"></i>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
"""
pages['relatorios.html'] = get_app_layout('Relatórios', 'Relatórios', relatorios_content)

analise_content = """
                <div class="card form-header mb-15 space-between">
                    <div class="flex-row">
                        <div class="icon-circle-large"><i class="fa-solid fa-magnifying-glass-chart text-green"></i></div>
                        <div>
                            <h2>Análise</h2>
                            <p>Compare dados das safras e acompanhe indicadores para tomar decisões mais inteligentes</p>
                        </div>
                    </div>
                    <button class="btn-primary-yellow" onclick="app.gerarAnalise()"><i class="fa-solid fa-chart-column"></i> Gerar análise</button>
                </div>

                <div class="card mb-15">
                    <h3><i class="fa-solid fa-filter"></i> Filtros de análise</h3>
                    <div class="filters-row">
                        <div class="filter-group">
                            <label>Safra</label><input type="text" value="Safra de soja 2025" class="form-input">
                        </div>
                        <div class="filter-group">
                            <label>Indicador</label><input type="text" value="Produtividade" class="form-input">
                        </div>
                        <div class="filter-group">
                            <label>Periodo</label><input type="text" value="Ultimos 30 dias" class="form-input">
                        </div>
                        <div class="filter-group">
                            <label>Comparar com</label><input type="text" value="Safra anterior" class="form-input">
                        </div>
                        <div class="filter-actions-col">
                            <button class="btn-primary-yellow" onclick="app.aplicarAnalise()">Aplicar análise</button>
                            <button class="btn-outline-gray mt-5">Limpar</button>
                        </div>
                    </div>
                </div>

                <div class="stats-grid mb-15">
                    <div class="card stat-item-large">
                        <div class="icon-circle-bg"><i class="fa-solid fa-chart-line text-green"></i></div>
                        <div class="info">Produtividade estimada<br><strong>78%</strong></div>
                    </div>
                    <div class="card stat-item-large">
                        <div class="icon-circle-bg"><i class="fa-solid fa-droplet text-green"></i></div>
                        <div class="info">Umidade média<br><strong>55%</strong></div>
                    </div>
                    <div class="card stat-item-large">
                        <div class="icon-circle-bg"><i class="fa-solid fa-brazilian-real-sign text-green"></i></div>
                        <div class="info">Preço médio da soja<br><strong>R$145,00</strong></div>
                    </div>
                    <div class="card stat-item-large">
                        <div class="icon-circle-bg"><i class="fa-solid fa-shield-halved text-green"></i></div>
                        <div class="info">Risco atual<br><strong class="text-yellow">Médio</strong></div>
                    </div>
                </div>

                <div class="analise-grid mb-15">
                    <div class="card">
                        <div class="card-header">
                            <h3><i class="fa-solid fa-chart-line text-green"></i> Evolução da safra</h3>
                            <div class="tabs"><button class="active">Produtividade</button><button>Solo</button><button>Mercado</button></div>
                        </div>
                        <div style="height: 150px; position: relative;">
                            <canvas id="analiseChart"></canvas>
                        </div>
                    </div>
                    <div class="card">
                        <h3><i class="fa-regular fa-lightbulb text-green"></i> Insights inteligentes</h3>
                        <ul class="insights-list">
                            <li><i class="fa-solid fa-arrow-trend-up text-green"></i> A produtividade estimada subiu 12% em relação ao mês anterior</li>
                            <li><i class="fa-solid fa-droplet text-green"></i> A umidade do solo está abaixo do ideal</li>
                            <li><i class="fa-solid fa-chart-simple text-green"></i> O preço da soja apresenta tendência de alta</li>
                            <li><i class="fa-solid fa-leaf text-green"></i> Recomenda-se monitorar irrigação nos próximos dias</li>
                        </ul>
                    </div>
                </div>

                <div class="analise-grid">
                    <div class="card">
                        <h3><i class="fa-regular fa-calendar"></i> Comparativo de Safras</h3>
                        <table class="data-table">
                            <thead><tr><th>Safra</th><th>Cultura</th><th>Produtividade</th><th>Umidade</th><th>Status</th></tr></thead>
                            <tbody>
                                <tr><td>Soja 2025</td><td>Soja</td><td>78%</td><td>55%</td><td><span class="badge light-green"><span class="dot-status green"></span> Crescimento</span></td></tr>
                                <tr><td>Milho 2024</td><td>Milho</td><td>65%</td><td>48%</td><td><span class="badge light-blue"><span class="dot-status blue"></span> Finalizada</span></td></tr>
                                <tr><td>Café 2024</td><td>Café</td><td>72%</td><td>61%</td><td><span class="badge light-blue"><span class="dot-status blue"></span> Finalizada</span></td></tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="card">
                        <h3><i class="fa-solid fa-gear"></i> A definir</h3>
                        <ul class="tasks-list">
                            <li><i class="fa-solid fa-droplet"></i> Ajustar irrigação da área 01</li>
                            <li><i class="fa-solid fa-chart-line"></i> Acompanhar variação do preço da soja</li>
                            <li><i class="fa-solid fa-file-invoice"></i> Gerar relatório semanal da safra</li>
                            <li><i class="fa-solid fa-seedling"></i> Revisar condição do solo nos proximos 7 dias</li>
                        </ul>
                        <button class="btn-outline-green full-width mt-10" onclick="app.exportar('PDF')"><i class="fa-solid fa-trophy"></i> Exportar análise</button>
                    </div>
                </div>
"""
pages['analise.html'] = get_app_layout('Análise', 'Análise', analise_content)

suporte_content = """
                <div class="card form-header mb-15">
                    <div class="icon-circle-large"><i class="fa-solid fa-headset text-green"></i></div>
                    <div>
                        <h2>Suporte</h2>
                        <p>Encontre ajuda para usar Agrologic ou envie uma solicitação para nossa equipe.</p>
                    </div>
                    <button class="btn-primary-yellow ml-auto" onclick="app.abrirModalChamado()"><i class="fa-solid fa-plus"></i> Novo Chamado</button>
                </div>

                <div class="suporte-cards-grid mb-15">
                    <div class="card support-action-card">
                        <div class="icon-circle-bg"><i class="fa-regular fa-file-lines text-green"></i></div>
                        <div>
                            <h3>Abrir chamado</h3>
                            <p>Informe seu problema e acompanhe o atendimento.</p>
                        </div>
                        <button class="btn-outline-green full-width mt-15" onclick="app.abrirModalChamado()">Criar Chamado</button>
                    </div>
                    <div class="card support-action-card">
                        <div class="icon-circle-bg"><i class="fa-regular fa-comments text-green"></i></div>
                        <div>
                            <h3>Chat com suporte</h3>
                            <p>Tire dúvidas rápidas sobre o sistema.</p>
                        </div>
                        <button class="btn-outline-green full-width mt-15" onclick="app.abrirChat()">Iniciar conversa</button>
                    </div>
                    <div class="card support-action-card">
                        <div class="icon-circle-bg"><i class="fa-solid fa-book-open text-green"></i></div>
                        <div>
                            <h3>Central de ajuda</h3>
                            <p>Consulte tutoriais e perguntas frequentes.</p>
                        </div>
                        <button class="btn-outline-green full-width mt-15">Ver artigos</button>
                    </div>
                </div>

                <div class="suporte-content-grid">
                    <div class="card">
                        <div class="card-header mb-15">
                            <div class="icon-circle-bg small"><i class="fa-regular fa-comments text-green"></i></div>
                            <h3>Enviar solicitação</h3>
                        </div>
                        <div class="form-row triple">
                            <div>
                                <label>Assunto</label>
                                <input type="text" class="form-input" value="Erro ao resgitrar safra">
                            </div>
                            <div>
                                <label>Categoria</label>
                                <select class="form-input"><option>Registro de safra</option></select>
                            </div>
                            <div>
                                <label>Prioridade</label>
                                <select class="form-input"><option>Alta</option></select>
                            </div>
                        </div>
                        <div class="form-row mt-15">
                            <label>Descrição</label>
                            <textarea class="form-input" rows="4">Ao tentar registrar uma nova safra de soja, o sistema apresenta uma mensagem de erro e não salva as informações. Ocorre ao preencher os dados da área e clica em salvar.</textarea>
                        </div>
                        <div class="form-row mt-15">
                            <label>Anexar arquivo</label>
                            <div class="file-upload-box">
                                <i class="fa-solid fa-paperclip"></i> Selecionar arquivos
                            </div>
                        </div>
                        <div class="actions-row mt-15">
                            <button class="btn-outline-green">Limpar campos</button>
                            <button class="btn-primary-yellow" onclick="app.enviarChamado()">Enviar chamado</button>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-header mb-15">
                            <div class="icon-circle-bg small"><i class="fa-solid fa-question text-green"></i></div>
                            <h3>Duvidas frequentes</h3>
                        </div>
                        <div class="accordion">
                            <div class="accordion-item active">
                                <div class="accordion-header">Como registrar uma nova safra? <i class="fa-solid fa-chevron-up"></i></div>
                                <div class="accordion-content">Acesse o menu Registrar Safra e clique em Nova Safra. Preencha as informações da área, cultura, talhão e periodo, e clique em Salvar Safra.</div>
                            </div>
                            <div class="accordion-item">
                                <div class="accordion-header">Como gerar um relatório? <i class="fa-solid fa-chevron-down"></i></div>
                                <div class="accordion-content">No menu Relatórios, clique em "Novo relatório", selecione os filtros e clique em Exportar.</div>
                            </div>
                            <div class="accordion-item">
                                <div class="accordion-header">Como acompanhar os alertas? <i class="fa-solid fa-chevron-down"></i></div>
                                <div class="accordion-content">Acesse o Painel para ver todos os alertas.</div>
                            </div>
                            <div class="accordion-item">
                                <div class="accordion-header">Como atualizar dados do solo? <i class="fa-solid fa-chevron-down"></i></div>
                                <div class="accordion-content">Na tela de Safras, selecione a safra e clique em Editar. Atualize os campos de NPK, Umidade ou pH.</div>
                            </div>
                            <div class="accordion-item">
                                <div class="accordion-header">Como alterar meus dados de acesso? <i class="fa-solid fa-chevron-down"></i></div>
                                <div class="accordion-content">Clique no seu perfil no canto superior direito e selecione Configurações.</div>
                            </div>
                        </div>
                    </div>
                </div>
"""
pages['suporte.html'] = get_app_layout('SUPORTE', 'SUPORTE', suporte_content)

for filename, content in pages.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filename}")
