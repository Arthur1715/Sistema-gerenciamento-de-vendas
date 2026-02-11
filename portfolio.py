"""
SISTEMA DE GERENCIAMENTO DE VENDAS
Arquitetura: HTML + CSS + Python separados

Estrutura:
├── sistema_vendas_separado.py  # Este arquivo
├── templates/                  # HTML templates
│   └── relatorio.html         # Estrutura HTML
├── static/                    # Arquivos estáticos
│   └── css/
│       └── estilo.css        # Estilos CSS
└── relatorios/               # Relatórios gerados
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv
import os
import webbrowser
from pathlib import Path

class SistemaVendasProfissional:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("📊 SISTEMA DE VENDAS - PORTFÓLIO PROFISSIONAL")
        self.janela.geometry("1300x750")
        self.janela.configure(bg='#0a1929')
        
        # Base path
        self.base_path = Path(__file__).parent
        
        # Dados
        self.vendas = []
        self.carregar_dados()
        
        # Configurar estrutura de pastas
        self.configurar_pastas()
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Criar interface
        self.criar_interface()
        
        self.janela.mainloop()
    
    def configurar_pastas(self):
        """Criar estrutura de pastas do projeto"""
        # Pastas necessárias
        pastas = [
            self.base_path / 'templates',
            self.base_path / 'static',
            self.base_path / 'static/css',
            self.base_path / 'relatorios'
        ]
        
        for pasta in pastas:
            pasta.mkdir(exist_ok=True)
            print(f"📁 Pasta verificada/criada: {pasta}")
        
        # Verificar se o template HTML existe
        template_path = self.base_path / 'templates' / 'relatorio.html'
        css_path = self.base_path / 'static/css/estilo.css'
        
        if not template_path.exists():
            messagebox.showwarning(
                "Template HTML não encontrado", 
                f"Crie o arquivo:\n{template_path}\n\nO sistema continuará, mas relatórios HTML não funcionarão."
            )
        
        if not css_path.exists():
            messagebox.showwarning(
                "CSS não encontrado", 
                f"Crie o arquivo:\n{css_path}\n\nO sistema continuará, mas relatórios HTML não funcionarão."
            )
    
    def configurar_estilo(self):
        """Configurar cores e estilos do Tkinter"""
        self.cores = {
            'bg_principal': '#0a1929',
            'bg_secundario': '#1e293b',
            'bg_card': '#2d3748',
            'texto': '#ffffff',
            'texto_secundario': '#94a3b8',
            'azul': '#3b82f6',
            'verde': '#22c55e',
            'vermelho': '#ef4444',
            'roxo': '#a855f7',
            'amarelo': '#f59e0b',
            'ciano': '#06b6d4'
        }
    
    def criar_interface(self):
        """Criar interface Tkinter"""
        
        # ============ HEADER ============
        header = tk.Frame(self.janela, bg=self.cores['bg_principal'], height=100)
        header.pack(fill='x', padx=30, pady=(20, 10))
        
        # Título
        titulo = tk.Label(header, 
                         text="SISTEMA DE VENDAS",
                         font=('Arial', 32, 'bold'),
                         bg=self.cores['bg_principal'],
                         fg=self.cores['azul'])
        titulo.pack(anchor='w')
        
        # Subtítulo
        subtitulo = tk.Label(header,
                           text="Cadastro • Relatórios HTML • CSS Profissional",
                           font=('Arial', 14),
                           bg=self.cores['bg_principal'],
                           fg=self.cores['texto_secundario'])
        subtitulo.pack(anchor='w')
        
        # Badges de tecnologia
        badges_frame = tk.Frame(header, bg=self.cores['bg_principal'])
        badges_frame.pack(anchor='w', pady=(10, 0))
        
        techs = [
            ("🐍 Python", self.cores['azul']),
            ("🖥️ Tkinter", self.cores['verde']),
            ("🌐 HTML5", self.cores['roxo']),
            ("🎨 CSS3", self.cores['amarelo']),
            ("📊 CSV", self.cores['ciano'])
        ]
        
        for tech, cor in techs:
            badge = tk.Label(badges_frame, text=tech,
                           bg=self.cores['bg_secundario'],
                           fg=cor,
                           font=('Arial', 10, 'bold'),
                           padx=12, pady=5,
                           relief='flat')
            badge.pack(side='left', padx=(0, 10))
        
        # ============ FRAME PRINCIPAL ============
        main_container = tk.Frame(self.janela, bg=self.cores['bg_principal'])
        main_container.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Dividir em 2 colunas (esquerda 30%, direita 70%)
        coluna_esquerda = tk.Frame(main_container, bg=self.cores['bg_principal'], width=400)
        coluna_esquerda.pack(side='left', fill='both', padx=(0, 20))
        coluna_esquerda.pack_propagate(False)
        
        coluna_direita = tk.Frame(main_container, bg=self.cores['bg_principal'])
        coluna_direita.pack(side='right', fill='both', expand=True)
        
        # ============ CARD CADASTRO ============
        self.criar_card_cadastro(coluna_esquerda)
        
        # ============ CARD ESTATÍSTICAS ============
        self.criar_card_estatisticas(coluna_esquerda)
        
        # ============ CARD RELATÓRIOS HTML ============
        self.criar_card_relatorios(coluna_esquerda)
        
        # ============ TABELA DE VENDAS ============
        self.criar_tabela_vendas(coluna_direita)
        
        # ============ BOTÕES DE AÇÃO ============
        self.criar_botoes_acao(coluna_direita)
        
        # Atualizar dados iniciais
        self.atualizar_tabela()
        self.atualizar_stats()
    
    def criar_card_cadastro(self, parent):
        """Criar card de cadastro de vendas"""
        card = tk.Frame(parent, bg=self.cores['bg_secundario'])
        card.pack(fill='x', pady=(0, 20))
        
        # Título
        tk.Label(card, 
                text="📝 CADASTRAR VENDA",
                font=('Arial', 14, 'bold'),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto']).pack(pady=(15, 10), padx=20, anchor='w')
        
        tk.Frame(card, bg=self.cores['azul'], height=2).pack(fill='x', padx=20)
        
        # Formulário
        form = tk.Frame(card, bg=self.cores['bg_secundario'])
        form.pack(pady=20, padx=20, fill='x')
        
        # Data
        tk.Label(form, text="Data:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=0, column=0, sticky='w', pady=5)
        
        self.data_entry = tk.Entry(form, font=('Arial', 11), width=25,
                                  bg=self.cores['bg_card'], fg=self.cores['texto'],
                                  relief='flat')
        self.data_entry.grid(row=0, column=1, pady=5, padx=(10, 0), sticky='w')
        self.data_entry.insert(0, datetime.now().strftime('%d/%m/%Y'))
        
        # Vendedor
        tk.Label(form, text="Vendedor:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=1, column=0, sticky='w', pady=5)
        
        self.vendedor_entry = tk.Entry(form, font=('Arial', 11), width=25,
                                      bg=self.cores['bg_card'], fg=self.cores['texto'],
                                      relief='flat')
        self.vendedor_entry.grid(row=1, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Produto
        tk.Label(form, text="Produto:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=2, column=0, sticky='w', pady=5)
        
        self.produto_combo = ttk.Combobox(form, 
                                         values=['Notebook', 'Smartphone', 'Tablet', 'Monitor', 
                                                 'Mouse', 'Teclado', 'Fone', 'Webcam', 'SSD', 'Memória'],
                                         font=('Arial', 11), width=23)
        self.produto_combo.grid(row=2, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Quantidade
        tk.Label(form, text="Quantidade:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=3, column=0, sticky='w', pady=5)
        
        self.quantidade_entry = tk.Entry(form, font=('Arial', 11), width=25,
                                        bg=self.cores['bg_card'], fg=self.cores['texto'],
                                        relief='flat')
        self.quantidade_entry.grid(row=3, column=1, pady=5, padx=(10, 0), sticky='w')
        self.quantidade_entry.insert(0, "1")
        
        # Preço
        tk.Label(form, text="Preço Unitário:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=4, column=0, sticky='w', pady=5)
        
        self.preco_entry = tk.Entry(form, font=('Arial', 11), width=25,
                                   bg=self.cores['bg_card'], fg=self.cores['texto'],
                                   relief='flat')
        self.preco_entry.grid(row=4, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Região
        tk.Label(form, text="Região:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=5, column=0, sticky='w', pady=5)
        
        self.regiao_combo = ttk.Combobox(form,
                                        values=['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'],
                                        font=('Arial', 11), width=23)
        self.regiao_combo.grid(row=5, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Botão Cadastrar
        btn_cadastrar = tk.Button(card,
                                 text="✅ CADASTRAR VENDA",
                                 font=('Arial', 12, 'bold'),
                                 bg=self.cores['verde'],
                                 fg='white',
                                 relief='flat',
                                 cursor='hand2',
                                 command=self.cadastrar_venda)
        btn_cadastrar.pack(pady=(0, 20), padx=20, fill='x')
    
    def criar_card_estatisticas(self, parent):
        """Criar card de estatísticas rápidas"""
        card = tk.Frame(parent, bg=self.cores['bg_secundario'])
        card.pack(fill='x', pady=(0, 20))
        
        tk.Label(card,
                text="📊 RESUMO RÁPIDO",
                font=('Arial', 14, 'bold'),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto']).pack(pady=(15, 10), padx=20, anchor='w')
        
        tk.Frame(card, bg=self.cores['roxo'], height=2).pack(fill='x', padx=20)
        
        self.stats_frame = tk.Frame(card, bg=self.cores['bg_secundario'])
        self.stats_frame.pack(pady=15, padx=20, fill='x')
    
    def criar_card_relatorios(self, parent):
        """Criar card de relatórios HTML"""
        card = tk.Frame(parent, bg=self.cores['bg_secundario'])
        card.pack(fill='x')
        
        tk.Label(card,
                text="🌐 RELATÓRIOS HTML + CSS",
                font=('Arial', 14, 'bold'),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto']).pack(pady=(15, 10), padx=20, anchor='w')
        
        tk.Frame(card, bg=self.cores['ciano'], height=2).pack(fill='x', padx=20)
        
        # Botões
        btn_frame = tk.Frame(card, bg=self.cores['bg_secundario'])
        btn_frame.pack(pady=20, padx=20, fill='x')
        
        # Botão Gerar Relatório
        btn_relatorio = tk.Button(btn_frame,
                                 text="📊 GERAR RELATÓRIO HTML",
                                 font=('Arial', 11, 'bold'),
                                 bg=self.cores['ciano'],
                                 fg='white',
                                 relief='flat',
                                 cursor='hand2',
                                 height=2,
                                 command=self.gerar_relatorio_html)
        btn_relatorio.pack(fill='x', pady=(0, 10))
        
        # Botão Visualizar
        btn_visualizar = tk.Button(btn_frame,
                                  text="👁️ VISUALIZAR ÚLTIMO RELATÓRIO",
                                  font=('Arial', 11, 'bold'),
                                  bg=self.cores['azul'],
                                  fg='white',
                                  relief='flat',
                                  cursor='hand2',
                                  height=2,
                                  command=self.visualizar_ultimo_relatorio)
        btn_visualizar.pack(fill='x')
    
    def criar_tabela_vendas(self, parent):
        """Criar tabela de vendas"""
        tk.Label(parent,
                text="📋 VENDAS CADASTRADAS",
                font=('Arial', 16, 'bold'),
                bg=self.cores['bg_principal'],
                fg=self.cores['texto']).pack(anchor='w', pady=(0, 15))
        
        # Frame da tabela
        tabela_container = tk.Frame(parent, bg=self.cores['bg_secundario'])
        tabela_container.pack(fill='both', expand=True)
        
        # Scrollbars
        scroll_y = tk.Scrollbar(tabela_container)
        scroll_y.pack(side='right', fill='y')
        
        scroll_x = tk.Scrollbar(tabela_container, orient='horizontal')
        scroll_x.pack(side='bottom', fill='x')
        
        # Treeview
        self.tree = ttk.Treeview(tabela_container,
                                columns=('data', 'vendedor', 'produto', 'qtd', 'preco', 'total', 'regiao'),
                                show='headings',
                                yscrollcommand=scroll_y.set,
                                xscrollcommand=scroll_x.set)
        
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        
        # Configurar colunas
        colunas = [
            ('data', 'Data', 100),
            ('vendedor', 'Vendedor', 120),
            ('produto', 'Produto', 120),
            ('qtd', 'Qtd', 60),
            ('preco', 'Preço', 100),
            ('total', 'Total', 120),
            ('regiao', 'Região', 100)
        ]
        
        for col, nome, largura in colunas:
            self.tree.heading(col, text=nome)
            self.tree.column(col, width=largura, anchor='center')
        
        self.tree.pack(fill='both', expand=True, padx=1, pady=1)
    
    def criar_botoes_acao(self, parent):
        """Criar botões de ação"""
        botoes_frame = tk.Frame(parent, bg=self.cores['bg_principal'])
        botoes_frame.pack(fill='x', pady=(20, 0))
        
        # Botão Exportar CSV
        btn_exportar = tk.Button(botoes_frame,
                                text="💾 EXPORTAR CSV",
                                font=('Arial', 12, 'bold'),
                                bg=self.cores['roxo'],
                                fg='white',
                                relief='flat',
                                cursor='hand2',
                                command=self.exportar_csv)
        btn_exportar.pack(side='left', padx=(0, 10))
        
        # Botão Limpar
        btn_limpar = tk.Button(botoes_frame,
                              text="🗑️ LIMPAR VENDAS",
                              font=('Arial', 12, 'bold'),
                              bg=self.cores['vermelho'],
                              fg='white',
                              relief='flat',
                              cursor='hand2',
                              command=self.limpar_vendas)
        btn_limpar.pack(side='right')
    
    def cadastrar_venda(self):
        """Cadastrar nova venda"""
        try:
            # Validações
            if not self.vendedor_entry.get():
                messagebox.showerror("Erro", "Preencha o nome do vendedor!")
                return
            
            if not self.produto_combo.get():
                messagebox.showerror("Erro", "Selecione um produto!")
                return
            
            if not self.regiao_combo.get():
                messagebox.showerror("Erro", "Selecione uma região!")
                return
            
            qtd = int(self.quantidade_entry.get())
            preco = float(self.preco_entry.get())
            total = qtd * preco
            
            venda = {
                'data': self.data_entry.get(),
                'vendedor': self.vendedor_entry.get(),
                'produto': self.produto_combo.get(),
                'quantidade': qtd,
                'preco': preco,
                'total': total,
                'regiao': self.regiao_combo.get()
            }
            
            self.vendas.append(venda)
            self.salvar_dados()
            
            # Limpar campos
            self.vendedor_entry.delete(0, tk.END)
            self.produto_combo.set('')
            self.quantidade_entry.delete(0, tk.END)
            self.quantidade_entry.insert(0, "1")
            self.preco_entry.delete(0, tk.END)
            self.regiao_combo.set('')
            
            # Atualizar interface
            self.atualizar_tabela()
            self.atualizar_stats()
            
            messagebox.showinfo("Sucesso", "✅ Venda cadastrada com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e Preço devem ser números válidos!")
    
    def atualizar_tabela(self):
        """Atualizar tabela de vendas"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for venda in self.vendas:
            self.tree.insert('', 'end', values=(
                venda['data'],
                venda['vendedor'],
                venda['produto'],
                venda['quantidade'],
                f"R$ {venda['preco']:.2f}",
                f"R$ {venda['total']:.2f}",
                venda['regiao']
            ))
    
    def atualizar_stats(self):
        """Atualizar estatísticas rápidas"""
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
        
        if not self.vendas:
            tk.Label(self.stats_frame,
                    text="Nenhuma venda cadastrada",
                    font=('Arial', 11),
                    bg=self.cores['bg_secundario'],
                    fg=self.cores['texto_secundario']).pack(pady=10)
            return
        
        total_vendas = len(self.vendas)
        valor_total = sum(v['total'] for v in self.vendas)
        ticket_medio = valor_total / total_vendas
        
        metrics = [
            ("💰 Vendas Totais:", f"R$ {valor_total:,.2f}", self.cores['verde']),
            ("📦 Quantidade:", f"{total_vendas} vendas", self.cores['azul']),
            ("🎫 Ticket Médio:", f"R$ {ticket_medio:,.2f}", self.cores['roxo'])
        ]
        
        for label, valor, cor in metrics:
            frame = tk.Frame(self.stats_frame, bg=self.cores['bg_secundario'])
            frame.pack(fill='x', pady=2)
            
            tk.Label(frame, text=label,
                    font=('Arial', 10),
                    bg=self.cores['bg_secundario'],
                    fg=self.cores['texto_secundario']).pack(side='left')
            
            tk.Label(frame, text=valor,
                    font=('Arial', 10, 'bold'),
                    bg=self.cores['bg_secundario'],
                    fg=cor).pack(side='right')
    
    def gerar_relatorio_html(self):
        """Gerar relatório HTML com CSS separado"""
        if not self.vendas:
            messagebox.showwarning("Aviso", "Nenhuma venda cadastrada!")
            return
        
        try:
            # Caminhos dos arquivos
            template_path = self.base_path / 'templates' / 'relatorio.html'
            css_path = self.base_path / 'static/css/estilo.css'
            
            # Verificar se os arquivos existem
            if not template_path.exists():
                messagebox.showerror("Erro", 
                    f"Template HTML não encontrado!\nCrie o arquivo: {template_path}")
                return
            
            if not css_path.exists():
                messagebox.showerror("Erro",
                    f"Arquivo CSS não encontrado!\nCrie o arquivo: {css_path}")
                return
            
            # Carregar template HTML
            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read()
            
            # Calcular métricas
            total_vendas = len(self.vendas)
            valor_total = sum(v['total'] for v in self.vendas)
            ticket_medio = valor_total / total_vendas
            
            # Análises
            vendas_vendedor = {}
            for v in self.vendas:
                nome = v['vendedor']
                vendas_vendedor[nome] = vendas_vendedor.get(nome, 0) + v['total']
            
            vendas_produto = {}
            quant_produto = {}
            for v in self.vendas:
                prod = v['produto']
                vendas_produto[prod] = vendas_produto.get(prod, 0) + v['total']
                quant_produto[prod] = quant_produto.get(prod, 0) + v['quantidade']
            
            vendas_regiao = {}
            qtd_regiao = {}
            for v in self.vendas:
                reg = v['regiao']
                vendas_regiao[reg] = vendas_regiao.get(reg, 0) + v['total']
                qtd_regiao[reg] = qtd_regiao.get(reg, 0) + 1
            
            # Gerar HTML dinâmico
            ranking_html = self.gerar_ranking_vendedores(vendas_vendedor, valor_total)
            produtos_html = self.gerar_top_produtos(vendas_produto, quant_produto, valor_total)
            regiao_html = self.gerar_analise_regiao(vendas_regiao, qtd_regiao, valor_total)
            vendas_html = self.gerar_ultimas_vendas()
            
            # Insights
            melhor_vendedor = max(vendas_vendedor.items(), key=lambda x: x[1])
            melhor_produto = max(vendas_produto.items(), key=lambda x: x[1])
            melhor_regiao = max(vendas_regiao.items(), key=lambda x: x[1])
            pior_regiao = min(vendas_regiao.items(), key=lambda x: x[1])
            
            # Substituir variáveis no template
            html = template
            html = html.replace('{{DATA_GERACAO}}', datetime.now().strftime('%d/%m/%Y às %H:%M'))
            html = html.replace('{{VALOR_TOTAL}}', f"{valor_total:,.2f}")
            html = html.replace('{{TOTAL_VENDAS}}', str(total_vendas))
            html = html.replace('{{TICKET_MEDIO}}', f"{ticket_medio:,.2f}")
            html = html.replace('{{TOTAL_VENDEDORES}}', str(len(vendas_vendedor)))
            html = html.replace('{{RANKING_VENDEDORES}}', ranking_html)
            html = html.replace('{{TOP_PRODUTOS}}', produtos_html)
            html = html.replace('{{VENDAS_REGIAO}}', regiao_html)
            html = html.replace('{{ULTIMAS_VENDAS}}', vendas_html)
            html = html.replace('{{MELHOR_VENDEDOR}}', melhor_vendedor[0])
            html = html.replace('{{MELHOR_VENDEDOR_VALOR}}', f"{melhor_vendedor[1]:,.2f}")
            html = html.replace('{{MELHOR_PRODUTO}}', melhor_produto[0])
            html = html.replace('{{MELHOR_PRODUTO_VALOR}}', f"{melhor_produto[1]:,.2f}")
            html = html.replace('{{MELHOR_REGIAO}}', melhor_regiao[0])
            html = html.replace('{{MELHOR_REGIAO_PERC}}', f"{(melhor_regiao[1]/valor_total)*100:.1f}%")
            html = html.replace('{{OPORTUNIDADE}}', f"Expandir na região {pior_regiao[0]}")
            html = html.replace('{{OPORTUNIDADE_DETALHE}}', f"R$ {pior_regiao[1]:,.2f} em vendas")
            html = html.replace('{{ASSINATURA}}', "Analista de Dados • Python • HTML • CSS")
            
            # Salvar relatório
            nome_arquivo = f"relatorio_vendas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            caminho_arquivo = self.base_path / 'relatorios' / nome_arquivo
            
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(html)
            
            self.ultimo_relatorio = caminho_arquivo
            
            messagebox.showinfo(
                "Sucesso", 
                f"✅ Relatório HTML gerado com sucesso!\n\n📁 {caminho_arquivo}\n\n🎨 CSS: {css_path}"
            )
            
            # Perguntar se quer visualizar
            if messagebox.askyesno("Visualizar", "Deseja visualizar o relatório no navegador?"):
                self.visualizar_relatorio(caminho_arquivo)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar relatório:\n{str(e)}")
    
    def gerar_ranking_vendedores(self, vendas_vendedor, valor_total):
        """Gerar HTML do ranking de vendedores"""
        html = ""
        for i, (nome, valor) in enumerate(sorted(vendas_vendedor.items(), key=lambda x: x[1], reverse=True), 1):
            qtd_vendas = len([v for v in self.vendas if v['vendedor'] == nome])
            ticket = valor / qtd_vendas
            percentual = (valor / valor_total) * 100
            
            cor_posicao = "#3b82f6" if i == 1 else "#94a3b8"
            
            html += f"""
            <tr>
                <td><strong style="color: {cor_posicao};">#{i}</strong></td>
                <td>{nome}</td>
                <td style="color: #22c55e; font-weight: bold;">R$ {valor:,.2f}</td>
                <td>{percentual:.1f}%</td>
                <td>R$ {ticket:,.2f}</td>
            </tr>
            """
        return html
    
    def gerar_top_produtos(self, vendas_produto, quant_produto, valor_total):
        """Gerar HTML do top produtos"""
        html = ""
        for i, (prod, valor) in enumerate(sorted(vendas_produto.items(), key=lambda x: x[1], reverse=True)[:10], 1):
            qtd = quant_produto[prod]
            percentual = (valor / valor_total) * 100
            
            html += f"""
            <tr>
                <td><strong>#{i}</strong></td>
                <td>{prod}</td>
                <td>{qtd} unidades</td>
                <td style="color: #22c55e;">R$ {valor:,.2f}</td>
                <td>{percentual:.1f}%</td>
            </tr>
            """
        return html
    
    def gerar_analise_regiao(self, vendas_regiao, qtd_regiao, valor_total):
        """Gerar HTML da análise por região"""
        html = ""
        for reg, valor in sorted(vendas_regiao.items(), key=lambda x: x[1], reverse=True):
            qtd = qtd_regiao[reg]
            ticket = valor / qtd
            percentual = (valor / valor_total) * 100
            
            html += f"""
            <tr>
                <td><strong>{reg}</strong></td>
                <td>{qtd} vendas</td>
                <td style="color: #f59e0b;">R$ {valor:,.2f}</td>
                <td>{percentual:.1f}%</td>
                <td>R$ {ticket:,.2f}</td>
            </tr>
            """
        return html
    
    def gerar_ultimas_vendas(self):
        """Gerar HTML das últimas vendas"""
        ultimas_vendas = sorted(self.vendas, key=lambda x: x['data'], reverse=True)[:20]
        html = ""
        for v in ultimas_vendas:
            html += f"""
            <tr>
                <td>{v['data']}</td>
                <td>{v['vendedor']}</td>
                <td>{v['produto']}</td>
                <td>{v['quantidade']}</td>
                <td>R$ {v['preco']:.2f}</td>
                <td style="color: #22c55e;">R$ {v['total']:.2f}</td>
                <td>{v['regiao']}</td>
            </tr>
            """
        return html
    
    def visualizar_relatorio(self, caminho):
        """Visualizar relatório no navegador"""
        webbrowser.open(f"file://{caminho.absolute()}")
    
    def visualizar_ultimo_relatorio(self):
        """Visualizar último relatório gerado"""
        if hasattr(self, 'ultimo_relatorio') and self.ultimo_relatorio.exists():
            self.visualizar_relatorio(self.ultimo_relatorio)
        else:
            relatorios = list((self.base_path / 'relatorios').glob('*.html'))
            if relatorios:
                ultimo = max(relatorios, key=lambda x: x.stat().st_mtime)
                self.visualizar_relatorio(ultimo)
            else:
                messagebox.showwarning("Aviso", "Nenhum relatório encontrado!")
    
    def exportar_csv(self):
        """Exportar dados para CSV"""
        if not self.vendas:
            messagebox.showwarning("Aviso", "Nenhuma venda para exportar!")
            return
        
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivo CSV", "*.csv"), ("Todos os arquivos", "*.*")],
            initialfile=f"vendas_{datetime.now().strftime('%Y%m%d_%H%M')}"
        )
        
        if arquivo:
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['data', 'vendedor', 'produto', 
                                                       'quantidade', 'preco', 'total', 'regiao'])
                writer.writeheader()
                writer.writerows(self.vendas)
            
            messagebox.showinfo("Sucesso", f"Dados exportados para:\n{arquivo}")
    
    def limpar_vendas(self):
        """Limpar todas as vendas"""
        if messagebox.askyesno("Confirmar", "Deseja realmente limpar todas as vendas?"):
            self.vendas = []
            self.salvar_dados()
            self.atualizar_tabela()
            self.atualizar_stats()
            messagebox.showinfo("Sucesso", "Todas as vendas foram removidas!")
    
    def carregar_dados(self):
        """Carregar dados salvos"""
        try:
            arquivo = self.base_path / 'vendas_salvas.csv'
            if arquivo.exists():
                with open(arquivo, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    self.vendas = list(reader)
                    for v in self.vendas:
                        v['quantidade'] = int(v['quantidade'])
                        v['preco'] = float(v['preco'])
                        v['total'] = float(v['total'])
        except:
            self.vendas = []
    
    def salvar_dados(self):
        """Salvar dados em arquivo"""
        arquivo = self.base_path / 'vendas_salvas.csv'
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            if self.vendas:
                writer = csv.DictWriter(f, fieldnames=self.vendas[0].keys())
                writer.writeheader()
                writer.writerows(self.vendas)

# ===== EXECUTAR =====
if __name__ == "__main__":
    print("🚀 Iniciando Sistema de Vendas Profissional...")
    print("📁 Estrutura:")
    print("   ├── templates/relatorio.html  (HTML)")
    print("   ├── static/css/estilo.css    (CSS)")
    print("   └── sistema_vendas_separado.py (Python)")
    print()
    
    app = SistemaVendasProfissional()