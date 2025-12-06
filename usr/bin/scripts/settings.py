#!/usr/bin/env python3.13
import tkinter as tk
from tkinter import ttk
import subprocess
import threading

class FilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Настройки")
        self.root.geometry("400x550")
        
        # Настройка полностью черной темы
        self.setup_dark_theme()
        
        # Черный фон для главного окна
        self.root.configure(bg='#000000')
        
        # Создаём фрейм для кнопок
        main_frame = ttk.Frame(root, style="Dark.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок фильтров
        title_label = ttk.Label(main_frame, text="Выберите фильтр:", 
                                style="Title.TLabel")
        title_label.grid(row=0, column=0, pady=15)
        
        # Кнопка "Фильтр синего"
        blue_button = ttk.Button(main_frame, text="🔵 Фильтр синего", 
                                 command=self.run_blue_filter, 
                                 style="Dark.TButton")
        blue_button.grid(row=1, column=0, pady=10, padx=20, sticky='ew')
        
        # Кнопка "Монохром"
        mono_button = ttk.Button(main_frame, text="⚫ Монохром", 
                                command=self.run_monochrome, 
                                style="Dark.TButton")
        mono_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')
        
        # Разделитель
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.grid(row=3, column=0, pady=15, padx=20, sticky='ew')
        
        # Заголовок режимов питания
        power_label = ttk.Label(main_frame, text="Режимы питания:", 
                                style="Title.TLabel")
        power_label.grid(row=4, column=0, pady=15)
        
        # Кнопка "PowerSave"
        powersave_button = ttk.Button(main_frame, text="🔋 PowerSave", 
                                     command=self.set_powersave, 
                                     style="Power.TButton")
        powersave_button.grid(row=5, column=0, pady=5, padx=20, sticky='ew')
        
        # Кнопка "Balance"
        balance_button = ttk.Button(main_frame, text="⚖️ Balance", 
                                   command=self.set_balance, 
                                   style="Power.TButton")
        balance_button.grid(row=6, column=0, pady=5, padx=20, sticky='ew')
        
        # Кнопка "Medium"
        medium_button = ttk.Button(main_frame, text="⚡ Medium", 
                                  command=self.set_medium, 
                                  style="Power.TButton")
        medium_button.grid(row=7, column=0, pady=5, padx=20, sticky='ew')
        
        # Кнопка "Performance"
        performance_button = ttk.Button(main_frame, text="🚀 Performance", 
                                       command=self.set_performance, 
                                       style="Power.TButton")
        performance_button.grid(row=8, column=0, pady=5, padx=20, sticky='ew')
        
        # Метка статуса
        self.status_label = ttk.Label(main_frame, text="Готов к работе", 
                                     style="Status.TLabel")
        self.status_label.grid(row=9, column=0, pady=20)
        
        # Кнопка выхода
        exit_button = ttk.Button(main_frame, text="Выход", 
                                command=root.quit, 
                                style="Exit.TButton")
        exit_button.grid(row=10, column=0, pady=10, padx=20, sticky='ew')
    
    def setup_dark_theme(self):
        """Настройка полностью черной темы"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Общие настройки - черный фон, белый текст
        style.configure(".", 
                       background="#000000",
                       foreground="#FFFFFF",
                       fieldbackground="#000000")
        
        # Настройка фрейма
        style.configure("Dark.TFrame",
                       background="#000000")
        
        # Настройка заголовка
        style.configure("Title.TLabel",
                       background="#000000",
                       foreground="#FFFFFF",
                       font=("Arial", 16, "bold"))
        
        # Настройка кнопок
        style.configure("Dark.TButton",
                       background="#1a1a1a",
                       foreground="#FFFFFF",
                       bordercolor="#333333",
                       lightcolor="#1a1a1a",
                       darkcolor="#000000",
                       font=("Arial", 12))
        
        style.map("Dark.TButton",
                 background=[('active', '#2a2a2a'), ('pressed', '#0a0a0a')],
                 foreground=[('active', '#FFFFFF')])
        
        # Настройка кнопок режимов питания
        style.configure("Power.TButton",
                       background="#0a1a0a",
                       foreground="#88FF88",
                       bordercolor="#1a331a",
                       lightcolor="#0a1a0a",
                       darkcolor="#000000",
                       font=("Arial", 11))
        
        style.map("Power.TButton",
                 background=[('active', '#1a2a1a'), ('pressed', '#050a05')],
                 foreground=[('active', '#AAFFAA')])
        
        # Настройка кнопки выхода (красноватый оттенок)
        style.configure("Exit.TButton",
                       background="#1a0000",
                       foreground="#FF6666",
                       bordercolor="#330000",
                       lightcolor="#1a0000",
                       darkcolor="#000000",
                       font=("Arial", 11))
        
        style.map("Exit.TButton",
                 background=[('active', '#2a0000'), ('pressed', '#0a0000')],
                 foreground=[('active', '#FF8888')])
        
        # Настройка метки статуса
        style.configure("Status.TLabel",
                       background="#000000",
                       foreground="#00FF00",
                       font=("Arial", 10, "italic"))
    
    def run_blue_filter(self):
        """Выполнить bash-скрипт для синего фильтра"""
        self.update_status("Выполняется синий фильтр...", "#4444FF")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("bluefilter",))
        thread.start()
    
    def run_monochrome(self):
        """Выполнить bash-скрипт для монохрома"""
        self.update_status("Выполняется монохром...", "#AAAAAA")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("monochrome",))
        thread.start()
    
    def set_powersave(self):
        """Установить режим PowerSave"""
        self.update_status("Установка режима PowerSave...", "#88FF88")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("powersave",))
        thread.start()
    
    def set_balance(self):
        """Установить режим Balance"""
        self.update_status("Установка режима Balance...", "#88FF88")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("balance",))
        thread.start()
    
    def set_medium(self):
        """Установить режим Medium"""
        self.update_status("Установка режима Medium...", "#88FF88")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("medium",))
        thread.start()
    
    def set_performance(self):
        """Установить режим Performance"""
        self.update_status("Установка режима Performance...", "#88FF88")
        
        thread = threading.Thread(target=self._execute_script, 
                                 args=("performance",))
        thread.start()
    
    def update_status(self, text, color):
        """Обновить текст и цвет статуса"""
        style = ttk.Style()
        style.configure("Status.TLabel", foreground=color)
        self.status_label.config(text=text)
        self.root.update()
    
    def _execute_script(self, script_path):
        """Выполнить bash-скрипт"""
        try:
            result = subprocess.run([script_path], 
                                  shell=True, 
                                  executable="/bin/bash",
                                  capture_output=True, 
                                  text=True, 
                                  timeout=30)
            
            if result.returncode == 0:
                self.update_status("✓ Успешно выполнено", "#00FF00")
            else:
                self.update_status(f"✗ Ошибка: код {result.returncode}", "#FF0000")
        except subprocess.TimeoutExpired:
            self.update_status("✗ Превышено время ожидания", "#FF0000")
        except Exception as e:
            self.update_status(f"✗ Ошибка: {str(e)[:30]}", "#FF0000")

def main():
    root = tk.Tk()
    app = FilterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
