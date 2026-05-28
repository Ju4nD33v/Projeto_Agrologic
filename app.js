const app = {
    charts: { dashboard: null, safras: null, analise: null },
    
    // Auth Actions
    login: function(event, type) {
        event.preventDefault();
        const inputs = event.target.querySelectorAll('input');
        let name = '';
        if (type === 'cadastro') {
            name = inputs[0].value + ' ' + inputs[1].value;
        } else {
            name = inputs[0].value.split('@')[0];
            if (!name) name = 'Usuário';
        }
        localStorage.setItem('agrologic_user', name);
        window.location.href = type === 'cadastro' ? 'login.html' : 'dashboard.html';
    },

    loadUserData: function() {
        const userNameEl = document.querySelector('.user-name');
        if (userNameEl) {
            const savedName = localStorage.getItem('agrologic_user');
            if (savedName) userNameEl.innerText = savedName;
        }
    },

    // UI Actions
    toggleNotifications: function(event) {
        const drop = document.getElementById('notif-dropdown');
        if (drop) {
            if (drop.style.display === 'flex') drop.style.display = 'none';
            else {
                drop.style.display = 'flex';
                drop.innerHTML = `
                    <div class="notif-header">Notificações</div>
                    <div class="notif-item"><i class="fa-solid fa-triangle-exclamation text-red"></i> Umidade baixa no Talhão 3</div>
                    <div class="notif-item"><i class="fa-solid fa-cloud-bolt text-gray"></i> Previsão de chuva para amanhã</div>
                    <div class="notif-item"><i class="fa-solid fa-chart-line text-green"></i> Relatório semanal gerado</div>
                `;
            }
        }
        event.stopPropagation();
    },

    // Safra Actions
    changeSafra: function(type) {
        // Atualiza a visualização da safra direita
        const header = document.querySelector('.details-header h2');
        const heroTitle = document.querySelector('.hero-title');
        const cardInfos = document.querySelectorAll('.basic-info div');
        const safraCards = document.querySelectorAll('.safra-item-card');
        
        if (!header || !heroTitle) return;

        if (type === 'soja') {
            header.innerText = 'Safra de soja 2026';
            heroTitle.innerHTML = '<i class="fa-solid fa-leaf text-green"></i> Soja';
            if(cardInfos.length > 2) {
                cardInfos[0].innerHTML = '<i class="fa-solid fa-location-dot"></i> 120 Hectares';
                cardInfos[1].innerHTML = '<i class="fa-regular fa-calendar"></i> Inicio do plantio: 01/04/2026';
                cardInfos[2].innerHTML = '<i class="fa-regular fa-clock"></i> Previsão de colheita: 15/02/2027';
            }
            // Update sementes e grafite
            this.updateQuantidadesSafra();
        } else if (type === 'milho') {
            header.innerText = 'Safra de milho 2025';
            heroTitle.innerHTML = '<i class="fa-solid fa-seedling text-yellow"></i> Milho';
            if(cardInfos.length > 2) {
                cardInfos[0].innerHTML = '<i class="fa-solid fa-location-dot"></i> 80 Hectares';
                cardInfos[1].innerHTML = '<i class="fa-regular fa-calendar"></i> Inicio do plantio: 01/04/2025';
                cardInfos[2].innerHTML = '<i class="fa-regular fa-clock"></i> Previsão de colheita: 15/06/2026';
            }
            // Update sementes e grafite
            this.updateQuantidadesSafra();
        } else if (type === 'algodao') {
            header.innerText = 'Safra de algodão 2024';
            heroTitle.innerHTML = '<i class="fa-solid fa-fan text-gray"></i> Algodão';
            if(cardInfos.length > 2) {
                cardInfos[0].innerHTML = '<i class="fa-solid fa-location-dot"></i> 200 Hectares';
                cardInfos[1].innerHTML = '<i class="fa-regular fa-calendar"></i> Inicio do plantio: 10/02/2024';
                cardInfos[2].innerHTML = '<i class="fa-regular fa-clock"></i> Previsão de colheita: 15/10/2024';
            }
            // Update sementes e grafite
            this.updateQuantidadesSafra();
        }
        
        // Atualizar active state dos cards
        if (safraCards.length > 0) {
            safraCards.forEach(card => card.classList.remove('active'));
            safraCards.forEach((card, idx) => {
                if ((type === 'soja' && idx === 0) || (type === 'milho' && idx === 1) || (type === 'algodao' && idx === 2)) {
                    card.classList.add('active');
                }
            });
        }
        
        // Randomizar o grafico da safra ao clicar tbm
        if (this.charts.safras) {
            let limit = this.charts.safras.data.labels.length;
            this.charts.safras.data.datasets[0].data = Array.from({length: limit}, () => Math.floor(Math.random() * 5000 + 1000));
            this.charts.safras.update();
        }
    },

    updateQuantidadesSafra: function() {
        const sementesEl = document.getElementById('qtd-sementes');
        const grafiteEl = document.getElementById('qtd-grafite');
        
        if (sementesEl) {
            sementesEl.innerText = (Math.floor(Math.random() * 15) + 10).toFixed(2);
        }
        if (grafiteEl) {
            grafiteEl.innerText = (Math.floor(Math.random() * 20) + 5).toFixed(2);
        }
    },

    changeAnaliseChart: function(type) {
        // Update button active state
        const tabs = document.querySelectorAll('.tabs button');
        tabs.forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
        
        if (!this.charts.analise) return;
        
        let newData = [];
        let title = '';
        
        if (type === 'produtividade') {
            newData = [50, 55, 62, 70, 75, 80, 82];
            title = 'Evolução';
            this.charts.analise.data.datasets[0].borderColor = '#4CAF50';
            this.charts.analise.data.datasets[0].backgroundColor = 'rgba(76,175,80,0.15)';
        } else if (type === 'solo') {
            newData = [65, 62, 70, 68, 75, 72, 80];
            title = 'Umidade do Solo';
            this.charts.analise.data.datasets[0].borderColor = '#2196F3';
            this.charts.analise.data.datasets[0].backgroundColor = 'rgba(33,150,243,0.15)';
        } else if (type === 'mercado') {
            newData = [40, 45, 55, 60, 65, 70, 75];
            title = 'Tendência de Preço';
            this.charts.analise.data.datasets[0].borderColor = '#FF9800';
            this.charts.analise.data.datasets[0].backgroundColor = 'rgba(255,152,0,0.15)';
        }
        
        this.charts.analise.data.datasets[0].label = title;
        this.charts.analise.data.datasets[0].data = newData;
        this.charts.analise.update();
    },
    
    updateResumoSafra: function() {
        const cult = document.getElementById('cultura-atual');
        const area = document.getElementById('area-plantada');
        const loc = document.getElementById('localizacao');
        const dt = document.getElementById('data-plantio');
        
        if (!cult || !area) return;

        const resumoItems = document.querySelectorAll('.resumo-side .resumo-item strong');
        if (resumoItems.length >= 4) {
            resumoItems[0].innerText = cult.value || 'Não informado';
            // area may be a numeric input now; normalize and append unit
            let areaVal = area.value ? area.value.toString().trim() : '';
            if (areaVal) {
                if (areaVal.toLowerCase().includes('ha') || areaVal.toLowerCase().includes('hectar')) {
                    resumoItems[1].innerText = areaVal;
                } else {
                    resumoItems[1].innerText = areaVal + ' hectares';
                }
            } else {
                resumoItems[1].innerText = 'Não informado';
            }
            resumoItems[2].innerText = loc.value || 'Não informado';
            
            if (dt && dt.value) {
                let d = new Date(dt.value);
                d.setMonth(d.getMonth() + 6); // Add 6 months for harvest
                resumoItems[3].innerText = d.toLocaleDateString('pt-BR');
            }
        }
    },

    finalizarPlantio: function() {
        const today = new Date().toISOString().slice(0,10);
        this.showModal('Finalizar Plantio', 'Selecione a data em que o plantio foi finalizado:', [
            { text: 'Cancelar', class: 'btn-outline-gray', action: 'app.closeModal()' },
            { text: 'Confirmar', class: 'btn-primary-yellow', action: 'app.confirmarFinalizarPlantio()' }
        ], `
            <div class="form-row mt-10">
                <label>Data de finalização</label>
                <input type="date" id="finalizar-data" class="form-input" value="${today}">
            </div>
        `);
    },

    confirmarFinalizarPlantio: function() {
        const dateInput = document.getElementById('finalizar-data');
        let dateVal = '';
        if (dateInput && dateInput.value) {
            dateVal = new Date(dateInput.value).toLocaleDateString('pt-BR');
        } else {
            dateVal = new Date().toLocaleDateString('pt-BR');
        }
        // update basic-info on safra details
        const basicInfoDivs = document.querySelectorAll('.basic-info div');
        if (basicInfoDivs && basicInfoDivs.length > 1) {
            basicInfoDivs[1].innerHTML = '<i class="fa-regular fa-calendar"></i> Plantio finalizado: ' + dateVal;
        }
        // update resumo if present
        const resumoItems = document.querySelectorAll('.resumo-side .resumo-item strong');
        if (resumoItems.length >= 4) {
            resumoItems[3].innerText = dateVal;
        }
        this.closeModal();
        this.showModal('Plantio finalizado', `Plantio marcado como finalizado em ${dateVal}.`, [
            { text: 'OK', class: 'btn-primary-yellow', action: 'app.closeModal()' }
        ]);
    },


    salvarSafra: function() {
        const culturaAtual = document.getElementById('cultura-atual').value;
        const culturaAnterior = document.getElementById('cultura-anterior').value;
        
        if (culturaAnterior === 'Cana-de-açúcar' && culturaAtual === 'Soja') {
            this.showModal('Aviso de Risco', 'Tem certeza que deseja cadastrar esta cultura? Os defensivos utilizados anteriormente podem causar impactos nocivos na soja.', [
                { text: 'Cancelar', class: 'btn-outline-gray', action: 'app.closeModal()' },
                { text: 'Confirmar Cadastro', class: 'btn-primary-yellow', action: 'window.location.href="safras.html"' }
            ]);
        } else {
            this.showModal('Sucesso', 'Safra registrada com sucesso!', [
                { text: 'OK', class: 'btn-primary-yellow', action: 'window.location.href="safras.html"' }
            ]);
        }
    },
    
    deleteSafra: function() {
        this.showModal('Excluir Safra', 'Tem certeza que deseja excluir a Safra de Soja 2026? Esta ação não pode ser desfeita.', [
            { text: 'Cancelar', class: 'btn-outline-gray', action: 'app.closeModal()' },
            { text: 'Excluir', class: 'btn-outline-gray text-red', action: 'app.closeModal()' }
        ]);
    },
    
    editarSafra: function() {
        this.showModal('Editar Dados do Solo', 'Atualize as informações do solo para melhor monitoramento.', [
            { text: 'Cancelar', class: 'btn-outline-gray', action: 'app.closeModal()' },
            { text: 'Salvar', class: 'btn-primary-yellow', action: 'app.closeModal()' }
        ], `
            <div class="form-row mt-15">
                <label>Umidade Atual (%)</label>
                <input type="text" class="form-input" value="55">
            </div>
            <div class="form-row mt-10">
                <label>Nível NPK</label>
                <input type="text" class="form-input" value="10-30-20">
            </div>
            <div class="form-row mt-10">
                <label>pH do Solo</label>
                <input type="text" class="form-input" value="6.2">
            </div>
            <div class="form-row mt-10">
                <label>Observações do solo</label>
                <textarea class="form-input" rows="3">Umidade em leve queda. Necessário acompanhamento diário.</textarea>
            </div>
        `);
    },
    
    editPermissions: function() {
        this.showModal('Editar Permissões', 'Gerencie quem tem acesso a esta safra.', [
            { text: 'Fechar', class: 'btn-outline-gray', action: 'app.closeModal()' }
        ], `
            <div style="margin-top: 15px;">
                <div class="form-row">
                    <input type="text" class="form-input" placeholder="Adicionar por e-mail ou ID...">
                    <button class="btn-outline-green mt-10 full-width">Adicionar Usuário</button>
                </div>
                <ul class="alerts-list mt-15">
                    <li><i class="fa-solid fa-user"></i> Pedro ID(4354) Agrônomo <i class="fa-solid fa-trash text-red float-right" style="cursor:pointer"></i></li>
                </ul>
            </div>
        `);
    },

    // Relatorios Actions
    showRelatorioA4: function() {
        let container = document.getElementById('modal-container');
        if (!container) return;
        container.innerHTML = `
            <div class="modal-content" style="max-width: 650px; width: 95%;">
                <div class="modal-header">
                    <h3>Visualização de Impressão (A4)</h3>
                    <i class="fa-solid fa-xmark" onclick="app.closeModal()" style="cursor:pointer;"></i>
                </div>
                <div style="background: #e0e0e0; padding: 20px; border-radius: 4px; max-height: 55vh; overflow-y: auto; margin-top: 10px;">
                    <div style="background: white; width: 100%; min-height: 842px; padding: 40px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); margin: 0 auto; color: #333; font-family: Arial, sans-serif;">
                        <div style="border-bottom: 2px solid #003C1F; padding-bottom: 10px; margin-bottom: 20px; display: flex; justify-content: space-between;">
                            <div>
                                <h2 style="color: #003C1F; margin:0; font-family: Poppins;">RELATÓRIO DE SAFRA</h2>
                                <p style="margin: 5px 0 0; color: #666; font-family: Poppins;">AgroLogic Systems</p>
                            </div>
                            <div style="text-align: right; color: #666; font-size: 12px;">
                                <p style="margin:0;">Data: 28/05/2026</p>
                                <p style="margin:0;">Ref: SAFRA-SOJA-2026</p>
                            </div>
                        </div>
                        <div style="margin-bottom: 30px;">
                            <h4 style="margin: 0 0 10px; color: #333; font-family: Poppins;">1. DADOS GERAIS</h4>
                            <table style="width: 100%; border-collapse: collapse; font-size: 14px;">
                                <tr style="border-bottom: 1px solid #ddd;">
                                    <td style="padding: 8px 0; font-weight: bold; width: 40%;">Cultura:</td>
                                    <td style="padding: 8px 0;">Soja (Glycine max)</td>
                                </tr>
                                <tr style="border-bottom: 1px solid #ddd;">
                                    <td style="padding: 8px 0; font-weight: bold;">Área Plantada:</td>
                                    <td style="padding: 8px 0;">120 Hectares - Talhão 3</td>
                                </tr>
                                <tr style="border-bottom: 1px solid #ddd;">
                                    <td style="padding: 8px 0; font-weight: bold;">Estágio Atual:</td>
                                    <td style="padding: 8px 0;">Desenvolvimento Vegetativo (V4)</td>
                                </tr>
                            </table>
                        </div>
                        <div style="margin-bottom: 30px;">
                            <h4 style="margin: 0 0 10px; color: #333; font-family: Poppins;">2. ANÁLISE DE SOLO E CLIMA</h4>
                            <p style="font-size: 14px; line-height: 1.6;">O monitoramento atual indica umidade relativa do solo na faixa de <strong>55%</strong>, levemente abaixo da média ideal para a região neste período. O pH se mantém estabilizado em <strong>6.2</strong>, garantindo boa absorção foliar de micro e macronutrientes. Níveis de NPK (10-30-20) mostram excelente fixação de potássio na base.</p>
                        </div>
                        <div style="margin-bottom: 30px;">
                            <h4 style="margin: 0 0 10px; color: #333; font-family: Poppins;">3. MÉTRICAS DE DESEMPENHO</h4>
                            <div style="background: #f9f9f9; padding: 15px; border: 1px solid #ddd;">
                                <p style="margin:0; font-size: 14px;">▶ Produtividade Estimada: <strong>78% (65 sacas/ha)</strong></p>
                                <p style="margin: 5px 0 0; font-size: 14px;">▶ Risco Detectado: <strong>Baixo</strong> (Nenhuma anomalia severa detectada)</p>
                                <p style="margin: 5px 0 0; font-size: 14px;">▶ Custo Inicial Gasto: <strong>R$ 315.000,00</strong></p>
                            </div>
                        </div>
                        <div style="margin-top: 80px; text-align: center;">
                            <div style="border-top: 1px solid #999; width: 250px; margin: 0 auto; padding-top: 10px;">
                                <strong>Assinatura do Agrônomo Responsável</strong><br>
                                <span style="font-size: 12px; color: #666;">CREA-SP 123456/D</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-actions mt-15" style="display:flex; justify-content:flex-end; gap:10px;">
                    <button class="btn-outline-gray" onclick="app.closeModal()">Fechar</button>
                    <button class="btn-primary-yellow" onclick="app.exportar('PDF')"><i class="fa-solid fa-download"></i> Baixar PDF</button>
                </div>
            </div>
        `;
        container.style.display = 'flex';
    },
    
    aplicarFiltros: function() {
        const btn = document.querySelector('.filter-actions .btn-primary-yellow');
        if(btn) {
            btn.innerText = "Filtrando...";
            // Randomize chart.js bar data on relatorios
            if (this.charts.relatorios) {
                this.charts.relatorios.data.datasets[0].data = [
                    Math.floor(Math.random() * 30 + 60),
                    Math.floor(Math.random() * 30 + 55),
                    Math.floor(Math.random() * 30 + 60),
                    Math.floor(Math.random() * 30 + 50)
                ];
                this.charts.relatorios.update();
            }
            setTimeout(() => { btn.innerText = "Aplicar filtros"; }, 500);
        }
    },
    
    exportar: function(formato) {
        this.showModal('Exportação Concluída', `O relatório foi exportado com sucesso no formato ${formato}.`, [
            { text: 'OK', class: 'btn-primary-yellow', action: 'app.closeModal()' }
        ]);
    },

    // Analise Actions
    gerarAnalise: function() {
        const btn = document.querySelector('.form-header .btn-primary-yellow');
        if(btn) {
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Gerando...';
            setTimeout(() => {
                btn.innerHTML = originalText;
                this.showModal('Análise Gerada', 'Nova análise processada e atualizada nos gráficos abaixo.', [
                    { text: 'OK', class: 'btn-primary-yellow', action: 'app.closeModal()' }
                ]);
            }, 800);
        }
    },
    
    aplicarAnalise: function() {
        const btn = document.querySelector('.filter-actions-col .btn-primary-yellow');
        if(btn) {
            btn.innerText = "Aplicando...";
            setTimeout(() => { btn.innerText = "Aplicar análise"; }, 500);
        }
    },

    // Suporte Actions
    abrirModalChamado: function() {
        this.showModal('Novo Chamado', 'Descreva o seu problema detalhadamente.', [
            { text: 'Cancelar', class: 'btn-outline-gray', action: 'app.closeModal()' },
            { text: 'Enviar', class: 'btn-primary-yellow', action: 'app.closeModal(); app.showModal("Sucesso", "Chamado aberto com sucesso!", [{text:"OK", class:"btn-primary-yellow", action:"app.closeModal()"}]);' }
        ], `
            <div class="form-row mt-15">
                <input type="text" class="form-input" placeholder="Assunto do chamado">
            </div>
            <div class="form-row mt-10">
                <textarea class="form-input" rows="4" placeholder="Descrição detalhada"></textarea>
            </div>
        `);
    },
    
    enviarChamado: function() {
        this.showModal('Sucesso', 'Seu chamado foi enviado e será respondido em breve.', [
            { text: 'OK', class: 'btn-primary-yellow', action: 'app.closeModal()' }
        ]);
    },
    
    abrirChat: function() {
        const chatWidget = document.getElementById('chat-widget');
        if(chatWidget) chatWidget.style.display = 'flex';
    },
    
    fecharChat: function() {
        const chatWidget = document.getElementById('chat-widget');
        if(chatWidget) chatWidget.style.display = 'none';
    },
    
    enviarMensagemChat: function() {
        const input = document.getElementById('chat-input');
        if(!input) return;
        const msg = input.value.trim();
        if (msg) {
            const body = document.getElementById('chat-messages');
            const userDiv = document.createElement('div');
            userDiv.className = 'message user';
            userDiv.innerText = msg;
            body.appendChild(userDiv);
            
            input.value = '';
            body.scrollTop = body.scrollHeight;
            
            setTimeout(() => {
                const sysDiv = document.createElement('div');
                sysDiv.className = 'message system';
                sysDiv.innerText = "Um de nossos especialistas já está analisando o seu caso.";
                body.appendChild(sysDiv);
                body.scrollTop = body.scrollHeight;
            }, 1000);
        }
    },

    // Global Modal System
    showModal: function(title, text, buttons, extraHtml = '') {
        let container = document.getElementById('modal-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'modal-container';
            container.className = 'modal-overlay';
            document.body.appendChild(container);
        }
        
        let btnsHtml = buttons.map(b => `<button class="${b.class}" onclick="${b.action}">${b.text}</button>`).join(' ');
        
        container.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>${title}</h3>
                    <i class="fa-solid fa-xmark" onclick="app.closeModal()" style="cursor:pointer;"></i>
                </div>
                <p style="font-size: 14px; color: var(--text-muted);">${text}</p>
                ${extraHtml}
                <div class="modal-actions mt-15" style="display:flex; justify-content:flex-end; gap:10px;">
                    ${btnsHtml}
                </div>
            </div>
        `;
        container.style.display = 'flex';
    },
    
    closeModal: function() {
        const container = document.getElementById('modal-container');
        if (container) container.style.display = 'none';
    },

    // Charts & Updates
    updateChart: function(type, el) {
        // Handle active class
        let siblings = el.parentElement.children;
        for(let i=0; i<siblings.length; i++) {
            siblings[i].classList.remove('active');
            if (siblings[i].classList.contains('green-bg')) {
                siblings[i].classList.remove('green-bg');
            }
        }
        
        if (el.innerText.includes('ano')) {
            if(type === 'dashboard') el.classList.add('green-bg');
            else el.classList.add('active');
        } else {
            el.classList.add('active');
        }

        // Generate Fake Data for presentation
        if (type === 'dashboard' && this.charts.dashboard) {
            let limit = el.innerText.includes('7') ? 7 : (el.innerText.includes('30') ? 11 : 12);
            let d1 = Array.from({length: limit}, () => Math.floor(Math.random() * 1000 + 1500));
            let d2 = Array.from({length: limit}, () => Math.floor(Math.random() * 500 + 400));
            let d3 = Array.from({length: limit}, () => Math.floor(Math.random() * 500 + 1000));
            
            this.charts.dashboard.data.labels = Array.from({length: limit}, (_, i) => 'Dia ' + (i+1));
            this.charts.dashboard.data.datasets[0].data = d1;
            this.charts.dashboard.data.datasets[1].data = d2;
            this.charts.dashboard.data.datasets[2].data = d3;
            this.charts.dashboard.update();
        }
        else if (type === 'safras' && this.charts.safras) {
            let limit = el.innerText.includes('7') ? 7 : (el.innerText.includes('30') ? 10 : 12);
            let d = Array.from({length: limit}, () => Math.floor(Math.random() * 5000 + 1000));
            this.charts.safras.data.labels = Array.from({length: limit}, (_, i) => 'Ref ' + (i+1));
            this.charts.safras.data.datasets[0].data = d;
            this.charts.safras.update();
        }
    },

    initDashboardChart: function() {
        const ctx = document.getElementById('cotacaoChart');
        if (ctx) {
            Chart.defaults.color = '#fff';
            this.charts.dashboard = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Nov', 'Dez'],
                    datasets: [
                        { label: 'Café Ara', data: [1500, 1600, 1500, 1700, 1800, 2000, 2200, 1800, 1900, 2500, 2300], borderColor: '#4CAF50', tension: 0.4 },
                        { label: 'Soja', data: [500, 600, 550, 700, 600, 500, 450, 400, 600, 700, 800], borderColor: '#F44336', tension: 0.4 },
                        { label: 'Milho', data: [1000, 1100, 1050, 1200, 1150, 1300, 1400, 1200, 1300, 1500, 1450], borderColor: '#00BCD4', tension: 0.4 }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { 
                        y: { grid: { color: 'rgba(255,255,255,0.1)' } },
                        x: { grid: { display: false } }
                    }
                }
            });
        }
    },
    
    initSafrasChart: function() {
        const ctx = document.getElementById('evolucaoChart');
        if (ctx) {
            Chart.defaults.color = '#757575';
            this.charts.safras = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Jan', 'Fev', 'Mar', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Nov', 'Dez'],
                    datasets: [{
                        label: 'Produtividade',
                        data: [1000, 2000, 3000, 4000, 4500, 5000, 6000, 7000, 8000, 9000],
                        borderColor: '#7CB342',
                        backgroundColor: '#7CB342',
                        tension: 0.1,
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: true } }
                }
            });
        }
    },
    
    initAnaliseChart: function() {
        const ctx = document.getElementById('analiseChart');
        if (ctx) {
            Chart.defaults.color = '#757575';
            this.charts.analise = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul'],
                    datasets: [{
                        label: 'Evolução',
                        data: [50, 55, 62, 70, 75, 80, 82],
                        borderColor: '#4CAF50',
                        backgroundColor: 'rgba(76,175,80,0.15)',
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { min: 0, max: 100 } }
                }
            });
        }
    },

    initRelatoriosChart: function() {
        const ctx = document.getElementById('desempenhoChart');
        if (!ctx) return;
        Chart.defaults.color = '#757575';
        this.charts.relatorios = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Soja 2026', 'Milho 2025', 'Café 2024', 'Algodão 2024'],
                datasets: [{
                    label: 'Produtividade (%)',
                    data: [80, 75, 82, 68],
                    backgroundColor: ['#7CB342','#FBC02D','#4CAF50','#90A4AE'],
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    y: { min: 0, max: 100, grid: { color: '#eee' } },
                    x: { grid: { display: false } }
                }
            }
        });
    }
};

// Initialize things on load
document.addEventListener('DOMContentLoaded', () => {
    app.loadUserData();
    
    // Accordions
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', function() {
            this.parentElement.classList.toggle('active');
            const icon = this.querySelector('i');
            if(this.parentElement.classList.contains('active')) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            } else {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
        });
    });

    // Close notifications dropdown on outside click
    document.addEventListener('click', () => {
        const drop = document.getElementById('notif-dropdown');
        if (drop && drop.style.display === 'flex') drop.style.display = 'none';
    });

    // Init charts based on current page
    if(window.location.pathname.includes('dashboard.html')) app.initDashboardChart();
    if(window.location.pathname.includes('safras.html')) {
        app.initSafrasChart();
        app.updateQuantidadesSafra();
    }
    if(window.location.pathname.includes('analise.html')) app.initAnaliseChart();
    if(window.location.pathname.includes('relatorios.html')) app.initRelatoriosChart();
});
