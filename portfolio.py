"""
SISTEMA DE GERENCIAMENTO DE VENDAS
Interface gráfica para adicionar vendas e gerar relatórios
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv
import os
from tkinter import font as tkfont

class SistemaVendas:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("📊 SISTEMA DE GERENCIAMENTO DE VENDAS")
        self.janela.geometry("1200x700")
        self.janela.configure(bg='#0a1929')
        
        # Dados
        self.vendas = []
        self.carregar_dados()
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Criar interface
        self.criar_interface()
        
        self.janela.mainloop()
    
    def configurar_estilo(self):
        """Configurar cores e estilos"""
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
            'amarelo': '#f59e0b'
        }
    
    def criar_interface(self):
        """Criar toda a interface"""
        
        # ============ HEADER ============
        header = tk.Frame(self.janela, bg=self.cores['bg_principal'], height=80)
        header.pack(fill='x', padx=20, pady=(20, 10))
        
        titulo = tk.Label(header, 
                         text="SISTEMA DE VENDAS",
                         font=('Arial', 28, 'bold'),
                         bg=self.cores['bg_principal'],
                         fg=self.cores['azul'])
        titulo.pack(side='left')
        
        subtitulo = tk.Label(header,
                           text="Cadastro e Relatórios",
                           font=('Arial', 14),
                           bg=self.cores['bg_principal'],
                           fg=self.cores['texto_secundario'])
        subtitulo.pack(side='left', padx=(20, 0))
        
        # ============ FRAME PRINCIPAL ============
        main_container = tk.Frame(self.janela, bg=self.cores['bg_principal'])
        main_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Dividir em 2 colunas
        coluna_esquerda = tk.Frame(main_container, bg=self.cores['bg_principal'], width=400)
        coluna_esquerda.pack(side='left', fill='both', padx=(0, 10))
        coluna_esquerda.pack_propagate(False)
        
        coluna_direita = tk.Frame(main_container, bg=self.cores['bg_principal'])
        coluna_direita.pack(side='right', fill='both', expand=True)
        
        # ============ CARD DE CADASTRO ============
        card_cadastro = tk.Frame(coluna_esquerda, bg=self.cores['bg_secundario'], 
                                relief='ridge', bd=0)
        card_cadastro.pack(fill='x', pady=(0, 20))
        
        # Título do card
        titulo_card = tk.Label(card_cadastro, 
                              text="📝 CADASTRAR VENDA",
                              font=('Arial', 14, 'bold'),
                              bg=self.cores['bg_secundario'],
                              fg=self.cores['texto'])
        titulo_card.pack(pady=(15, 10), padx=15, anchor='w')
        
        # Linha divisória
        tk.Frame(card_cadastro, bg=self.cores['azul'], height=2).pack(fill='x', padx=15)
        
        # Formulário
        form = tk.Frame(card_cadastro, bg=self.cores['bg_secundario'])
        form.pack(pady=20, padx=20, fill='x')
        
        # Data
        tk.Label(form, text="Data:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=0, column=0, sticky='w', pady=5)
        
        self.data_entry = tk.Entry(form, font=('Arial', 11), width=25)
        self.data_entry.grid(row=0, column=1, pady=5, padx=(10, 0), sticky='w')
        self.data_entry.insert(0, datetime.now().strftime('%d/%m/%Y'))
        
        # Vendedor
        tk.Label(form, text="Vendedor:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=1, column=0, sticky='w', pady=5)
        
        self.vendedor_entry = tk.Entry(form, font=('Arial', 11), width=25)
        self.vendedor_entry.grid(row=1, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Produto
        tk.Label(form, text="Produto:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=2, column=0, sticky='w', pady=5)
        
        self.produto_combo = ttk.Combobox(form, 
                                          values=['Notebook', 'Smartphone', 'Tablet', 'Monitor', 
                                                  'Mouse', 'Teclado', 'Fone', 'Webcam'],
                                          font=('Arial', 11), width=23)
        self.produto_combo.grid(row=2, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Quantidade
        tk.Label(form, text="Quantidade:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=3, column=0, sticky='w', pady=5)
        
        self.quantidade_entry = tk.Entry(form, font=('Arial', 11), width=25)
        self.quantidade_entry.grid(row=3, column=1, pady=5, padx=(10, 0), sticky='w')
        self.quantidade_entry.insert(0, "1")
        
        # Preço
        tk.Label(form, text="Preço Unitário:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=4, column=0, sticky='w', pady=5)
        
        self.preco_entry = tk.Entry(form, font=('Arial', 11), width=25)
        self.preco_entry.grid(row=4, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Região
        tk.Label(form, text="Região:",
                font=('Arial', 11),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto_secundario']).grid(row=5, column=0, sticky='w', pady=5)
        
        self.regiao_combo = ttk.Combobox(form,
                                         values=['Norte', 'Sul', 'Leste', 'Oeste', 'Centro'],
                                         font=('Arial', 11), width=23)
        self.regiao_combo.grid(row=5, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Botão Cadastrar
        btn_cadastrar = tk.Button(card_cadastro,
                                 text="✅ CADASTRAR VENDA",
                                 font=('Arial', 12, 'bold'),
                                 bg=self.cores['verde'],
                                 fg='white',
                                 relief='flat',
                                 cursor='hand2',
                                 command=self.cadastrar_venda)
        btn_cadastrar.pack(pady=(0, 20), padx=20, fill='x')
        
        # ============ CARD DE ESTATÍSTICAS ============
        card_stats = tk.Frame(coluna_esquerda, bg=self.cores['bg_secundario'])
        card_stats.pack(fill='x')
        
        tk.Label(card_stats,
                text="📊 RESUMO RÁPIDO",
                font=('Arial', 14, 'bold'),
                bg=self.cores['bg_secundario'],
                fg=self.cores['texto']).pack(pady=(15, 10), padx=15, anchor='w')
        
        tk.Frame(card_stats, bg=self.cores['roxo'], height=2).pack(fill='x', padx=15)
        
        self.stats_frame = tk.Frame(card_stats, bg=self.cores['bg_secundario'])
        self.stats_frame.pack(pady=15, padx=15, fill='x')
        
        self.atualizar_stats()
        
        # ============ TABELA DE VENDAS ============
        # Título
        titulo_tabela = tk.Label(coluna_direita,
                                text="📋 VENDAS CADASTRADAS",
                                font=('Arial', 16, 'bold'),
                                bg=self.cores['bg_principal'],
                                fg=self.cores['texto'])
        titulo_tabela.pack(anchor='w', pady=(0, 10))
        
        # Frame da tabela
        tabela_container = tk.Frame(coluna_direita, bg=self.cores['bg_secundario'])
        tabela_container.pack(fill='both', expand=True)
        
        # Scrollbars
        scroll_y = tk.Scrollbar(tabela_container)
        scroll_y.pack(side='right', fill='y')
        
        scroll_x = tk.Scrollbar(tabela_container, orient='horizontal')
        scroll_x.pack(side='bottom', fill='x')
        
        # Treeview (tabela)
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
        
        # ============ BOTÕES DE AÇÃO ============
        botoes_frame = tk.Frame(coluna_direita, bg=self.cores['bg_principal'])
        botoes_frame.pack(fill='x', pady=(20, 0))
        
        # Botão Relatório
        btn_relatorio = tk.Button(botoes_frame,
                                 text="📊 GERAR RELATÓRIO COMPLETO",
                                 font=('Arial', 12, 'bold'),
                                 bg=self.cores['azul'],
                                 fg='white',
                                 relief='flat',
                                 cursor='hand2',
                                 command=self.gerar_relatorio)
        btn_relatorio.pack(side='left', padx=(0, 10))
        
        # Botão Exportar CSV
        btn_exportar = tk.Button(botoes_frame,
                                text="💾 EXPORTAR CSV",
                                font=('Arial', 12, 'bold'),
                                bg=self.cores['roxo'],
                                fg='white',
                                relief='flat',
                                cursor='hand2',
                                command=self.exportar_csv)
        btn_exportar.pack(side='left')
        
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
        
        # Atualizar tabela
        self.atualizar_tabela()
    
    def cadastrar_venda(self):
        """Cadastrar nova venda"""
        try:
            # Validar campos
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
            
            messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")
            
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e Preço devem ser números válidos!")
    
    def atualizar_tabela(self):
        """Atualizar tabela de vendas"""
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adicionar vendas
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
        # Limpar stats
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
        
        if not self.vendas:
            tk.Label(self.stats_frame,
                    text="Nenhuma venda cadastrada",
                    font=('Arial', 11),
                    bg=self.cores['bg_secundario'],
                    fg=self.cores['texto_secundario']).pack(pady=10)
            return
        
        # Calcular métricas
        total_vendas = len(self.vendas)
        valor_total = sum(v['total'] for v in self.vendas)
        ticket_medio = valor_total / total_vendas
        
        # Exibir métricas
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
    
    def gerar_relatorio(self):
        """Gerar relatório completo"""
        if not self.vendas:
            messagebox.showwarning("Aviso", "Nenhuma venda cadastrada!")
            return
        
        # Criar janela de relatório
        relatorio = tk.Toplevel(self.janela)
        relatorio.title("📊 RELATÓRIO DE VENDAS")
        relatorio.geometry("800x600")
        relatorio.configure(bg=self.cores['bg_principal'])
        
        # Área de texto
        texto = tk.Text(relatorio, bg=self.cores['bg_secundario'],
                       fg=self.cores['texto'], font=('Courier', 10))
        texto.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Gerar relatório
        texto.insert('1.0', "="*70 + "\n")
        texto.insert('end', "RELATÓRIO DE VENDAS\n")
        texto.insert('end', "="*70 + "\n\n")
        
        # Métricas principais
        total_vendas = len(self.vendas)
        valor_total = sum(v['total'] for v in self.vendas)
        ticket_medio = valor_total / total_vendas
        
        texto.insert('end', "MÉTRICAS PRINCIPAIS:\n")
        texto.insert('end', "-"*50 + "\n")
        texto.insert('end', f"Vendas Totais:    R$ {valor_total:>12,.2f}\n")
        texto.insert('end', f"Total de Vendas:  {total_vendas:>12}\n")
        texto.insert('end', f"Ticket Médio:     R$ {ticket_medio:>12,.2f}\n\n")
        
        # Vendas por vendedor
        texto.insert('end', "VENDAS POR VENDEDOR:\n")
        texto.insert('end', "-"*50 + "\n")
        
        vendas_vendedor = {}
        for v in self.vendas:
            nome = v['vendedor']
            vendas_vendedor[nome] = vendas_vendedor.get(nome, 0) + v['total']
        
        for nome, valor in sorted(vendas_vendedor.items(), key=lambda x: x[1], reverse=True):
            percentual = (valor / valor_total) * 100
            texto.insert('end', f"{nome:<20} R$ {valor:>12,.2f}  ({percentual:.1f}%)\n")
        
        texto.insert('end', "\n")
        
        # Vendas por produto
        texto.insert('end', "PRODUTOS MAIS VENDIDOS:\n")
        texto.insert('end', "-"*50 + "\n")
        
        vendas_produto = {}
        for v in self.vendas:
            prod = v['produto']
            vendas_produto[prod] = vendas_produto.get(prod, 0) + v['total']
        
        for i, (prod, valor) in enumerate(sorted(vendas_produto.items(), key=lambda x: x[1], reverse=True)[:5], 1):
            texto.insert('end', f"{i}. {prod:<20} R$ {valor:>12,.2f}\n")
        
        texto.insert('end', "\n")
        
        # Vendas por região
        texto.insert('end', "VENDAS POR REGIÃO:\n")
        texto.insert('end', "-"*50 + "\n")
        
        vendas_regiao = {}
        for v in self.vendas:
            reg = v['regiao']
            vendas_regiao[reg] = vendas_regiao.get(reg, 0) + v['total']
        
        for reg, valor in sorted(vendas_regiao.items(), key=lambda x: x[1], reverse=True):
            percentual = (valor / valor_total) * 100
            texto.insert('end', f"{reg:<20} R$ {valor:>12,.2f}  ({percentual:.1f}%)\n")
        
        texto.insert('end', "\n")
        texto.insert('end', "="*70 + "\n")
        texto.insert('end', "RELATÓRIO GERADO EM: " + datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")
        texto.insert('end', "="*70 + "\n")
        
        texto.config(state='disabled')
        
        # Botão salvar
        btn_salvar = tk.Button(relatorio,
                              text="💾 SALVAR RELATÓRIO",
                              font=('Arial', 12, 'bold'),
                              bg=self.cores['verde'],
                              fg='white',
                              command=lambda: self.salvar_relatorio(texto.get('1.0', 'end')))
        btn_salvar.pack(pady=(0, 20))
    
    def salvar_relatorio(self, conteudo):
        """Salvar relatório em arquivo"""
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivo de texto", "*.txt"), ("Todos os arquivos", "*.*")],
            initialfile=f"relatorio_vendas_{datetime.now().strftime('%Y%m%d_%H%M')}"
        )
        
        if arquivo:
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            messagebox.showinfo("Sucesso", f"Relatório salvo em:\n{arquivo}")
    
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
            if os.path.exists('vendas_salvas.csv'):
                with open('vendas_salvas.csv', 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    self.vendas = list(reader)
                    # Converter tipos
                    for v in self.vendas:
                        v['quantidade'] = int(v['quantidade'])
                        v['preco'] = float(v['preco'])
                        v['total'] = float(v['total'])
        except:
            self.vendas = []
    
    def salvar_dados(self):
        """Salvar dados em arquivo"""
        with open('vendas_salvas.csv', 'w', newline='', encoding='utf-8') as f:
            if self.vendas:
                writer = csv.DictWriter(f, fieldnames=self.vendas[0].keys())
                writer.writeheader()
                writer.writerows(self.vendas)

# ============ EXECUTAR ============
if __name__ == "__main__":
    SistemaVendas()