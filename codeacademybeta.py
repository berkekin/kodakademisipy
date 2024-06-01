import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import pygments
from pygments.lexers import PythonLexer, RubyLexer
from pygments.formatters import HtmlFormatter
from tkinterweb import HtmlFrame
import subprocess
import tempfile

class CodeAcademyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kod Akademisi: Python ve Ruby")
        self.root.geometry("1200x900")
        self.create_tabs()
        self.populate_tabs()

    def create_tabs(self):
        """Create tab control and add tabs."""
        self.tab_control = ttk.Notebook(self.root)

        self.python_tab = ttk.Frame(self.tab_control)
        self.ruby_tab = ttk.Frame(self.tab_control)
        self.resources_tab = ttk.Frame(self.tab_control)
        self.quiz_tab = ttk.Frame(self.tab_control)
        self.community_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.python_tab, text="Python")
        self.tab_control.add(self.ruby_tab, text="Ruby")
        self.tab_control.add(self.resources_tab, text="Kaynaklar")
        self.tab_control.add(self.quiz_tab, text="Quiz ve Egzersizler")
        self.tab_control.add(self.community_tab, text="Topluluk")

        self.tab_control.pack(expand=1, fill="both")

    def populate_tabs(self):
        """Populate each tab with content."""
        self.populate_python_tab()
        self.populate_ruby_tab()
        self.populate_resources_tab()
        self.populate_quiz_tab()
        self.populate_community_tab()

    def open_link(self, url):
        """Open a URL in a web browser."""
        webbrowser.open_new(url)

    def copy_to_clipboard(self, code):
        """Copy given code to clipboard."""
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("Kopyalandı", "Kod panoya kopyalandı.")

    def run_code(self, code, language):
        """Run the provided code in the specified language."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{language}') as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file.close()
            try:
                if language == 'py':
                    result = subprocess.run(['python', temp_file.name], capture_output=True, text=True)
                elif language == 'rb':
                    result = subprocess.run(['ruby', temp_file.name], capture_output=True, text=True)
                else:
                    raise ValueError("Unsupported language")
                output = result.stdout if result.stdout else result.stderr
            except Exception as e:
                output = str(e)
            finally:
                return output

    def create_code_example(self, tab, example, description, language):
        """Create a code example block with copy and run buttons."""
        lexer = PythonLexer() if language == 'py' else RubyLexer()
        formatted_code = pygments.highlight(example, lexer, HtmlFormatter(full=True, style="colorful"))
        code_display = HtmlFrame(tab)
        code_display.load_html(formatted_code)
        code_display.pack(pady=10)

        copy_button = tk.Button(tab, text="Kodu Kopyala", command=lambda e=example: self.copy_to_clipboard(e))
        copy_button.pack(pady=5)

        description_label = tk.Label(tab, text=description, font=("Arial", 10, "italic"))
        description_label.pack(pady=5)

        run_button = tk.Button(tab, text="Kodu Çalıştır", command=lambda e=example: messagebox.showinfo("Çıktı", self.run_code(e, language)))
        run_button.pack(pady=5)

    def populate_python_tab(self):
        """Populate Python tab with content."""
        python_label = tk.Label(self.python_tab, text="Python Tanıtımı", font=("Arial", 16))
        python_label.pack(pady=10)

        python_description = tk.Text(self.python_tab, wrap="word", height=15, width=100)
        python_description.pack(pady=10)
        python_description.insert(tk.END, """
Python, Guido van Rossum tarafından 1991 yılında geliştirilen yüksek seviyeli bir programlama dilidir.
Özellikleri:
- Kolay okunabilir ve yazılabilir sözdizimi
- Dinamik tür kontrolü
- Geniş standart kütüphane
- Bilimsel hesaplamalar, veri analizi, web geliştirme gibi birçok alanda kullanılır.

Python'un popüler kitaplıkları ve araçları:
- NumPy, Pandas: Veri analizi ve bilimsel hesaplamalar için
- Django, Flask: Web geliştirme için
- TensorFlow, Keras: Makine öğrenmesi ve yapay zeka için

Python'un Temel Konuları:
- Değişkenler ve Veri Türleri
- Koşul İfadeleri ve Döngüler
- Fonksiyonlar ve Modüller
- Dosya İşlemleri
- Hata Yönetimi
- Nesne Yönelimli Programlama (OOP)

İleri Seviye Python Konuları:
- Dekoratörler
- Jeneratörler
- İleri Düzey Veri Yapıları (List Comprehensions, Dictionaries)
- Çoklu İşlem (Multiprocessing)
- Asenkron Programlama

Python Kodlama İpuçları:
- Anlamlı değişken isimleri kullanın
- Kısa ve öz fonksiyonlar yazın
- Tekrar eden kodları fonksiyonlara ayırın
- Geniş projelerde modüler yapı kullanın
        """)
        python_description.config(state="disabled")

        python_examples = [
            ("""
def merhaba():
    print("Merhaba Dünya")

merhaba()
            """, "Basit bir fonksiyon ve çağrısı."),
            ("""
for i in range(5):
    print(i)
            """, "Bir döngü örneği."),
            ("""
class Insan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Benim adım {self.isim} ve ben {self.yas} yaşındayım.")

ahmet = Insan("Ahmet", 30)
ahmet.tanit()
            """, "Basit bir sınıf ve nesne kullanımı."),
            ("""
import numpy as np

a = np.array([1, 2, 3])
print(a)
            """, "NumPy ile bilimsel hesaplama."),
            ("""
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

print(faktoriyel(5))
            """, "Rekursif fonksiyon kullanarak faktöriyel hesaplama."),
            ("""
try:
    x = int(input("Bir sayı girin: "))
    print(f"Girdiğiniz sayı: {x}")
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")
            """, "Kullanıcı girişi ve hata yönetimi."),
            ("""
import random

sayi = random.randint(1, 100)
print(f"Rastgele sayı: {sayi}")
            """, "Rastgele sayı üretimi."),
            ("""
def ters_cevir(s):
    return s[::-1]

print(ters_cevir("Python"))
            """, "Bir string'i ters çevirme."),
            ("""
with open("ornek.txt", "w") as dosya:
    dosya.write("Merhaba, bu bir deneme dosyasıdır.")
            """, "Dosya yazma işlemi."),
            ("""
def toplama(a, b):
    return a + b

print(toplama(3, 5))
            """, "Basit toplama fonksiyonu."),
        ]

        for example, description in python_examples:
            self.create_code_example(self.python_tab, example, description, 'py')

        python_resource_button = tk.Button(self.python_tab, text="Python Belgeleri", command=lambda: self.open_link("https://docs.python.org/3/"))
        python_resource_button.pack(pady=5)

    def populate_ruby_tab(self):
        """Populate Ruby tab with content."""
        ruby_label = tk.Label(self.ruby_tab, text="Ruby Tanıtımı", font=("Arial", 16))
        ruby_label.pack(pady=10)

        ruby_description = tk.Text(self.ruby_tab, wrap="word", height=15, width=100)
        ruby_description.pack(pady=10)
        ruby_description.insert(tk.END, """
Ruby, Yukihiro Matsumoto tarafından 1995 yılında geliştirilen dinamik, nesne yönelimli bir programlama dilidir.
Özellikleri:
- Nesne yönelimli tasarım
- Esnek sözdizimi
- Geniş standart kütüphane
- Web geliştirme (Rails ile) ve otomasyon gibi alanlarda kullanılır.

Ruby'nin popüler kitaplıkları ve araçları:
- Rails: Web geliştirme için güçlü bir framework
- Sinatra: Basit ve esnek bir web uygulama kitaplığı
- RSpec: Test etme araçları için

Ruby'nin Temel Konuları:
- Değişkenler ve Veri Türleri
- Koşul İfadeleri ve Döngüler
- Fonksiyonlar ve Bloklar
- Dosya İşlemleri
- Hata Yönetimi
- Nesne Yönelimli Programlama (OOP)

İleri Seviye Ruby Konuları:
- Modüller ve Miksinler
- Metaprogramlama
- İleri Düzey Veri Yapıları (Array, Hash)
- Eşzamanlı Programlama (Threading)
- DSL (Domain Specific Language) Oluşturma

Ruby Kodlama İpuçları:
- Temiz ve okunabilir kod yazın
- Ruby topluluğunun en iyi uygulamalarını takip edin
- Projelerde RSpec ile test yazın
- RubyGems ile mevcut çözümleri kullanın
        """)
        ruby_description.config(state="disabled")

        ruby_examples = [
            ("""
def merhaba
  puts 'Merhaba Dünya'
end

merhaba
            """, "Basit bir fonksiyon ve çağrısı."),
            ("""
5.times do |i|
  puts i
end
            """, "Bir döngü örneği."),
            ("""
class Insan
  def initialize(isim, yas)
    @isim = isim
    @yas = yas
  end

  def tanit
    puts "Benim adım #{@isim} ve ben #{@yas} yaşındayım."
  end
end

ahmet = Insan.new("Ahmet", 30)
ahmet.tanit
            """, "Basit bir sınıf ve nesne kullanımı."),
            ("""
require 'json'

json_string = '{"isim": "Ahmet", "yas": 30}'
veri = JSON.parse(json_string)
puts veri['isim']
            """, "JSON işleme örneği."),
            ("""
def faktoriyel(n)
  return 1 if n == 0
  n * faktoriyel(n - 1)
end

puts faktoriyel(5)
            """, "Rekursif fonksiyon kullanarak faktöriyel hesaplama."),
            ("""
begin
  x = Integer(gets)
  puts "Girdiğiniz sayı: #{x}"
rescue ArgumentError
  puts "Geçersiz giriş! Lütfen bir sayı girin."
end
            """, "Kullanıcı girişi ve hata yönetimi."),
            ("""
def ters_cevir(s)
  s.reverse
end

puts ters_cevir("Ruby")
            """, "Bir string'i ters çevirme."),
            ("""
File.open("ornek.txt", "w") do |dosya|
  dosya.puts "Merhaba, bu bir deneme dosyasıdır."
end
            """, "Dosya yazma işlemi."),
            ("""
def toplama(a, b)
  a + b
end

puts toplama(3, 5)
            """, "Basit toplama fonksiyonu."),
        ]

        for example, description in ruby_examples:
            self.create_code_example(self.ruby_tab, example, description, 'rb')

        ruby_resource_button = tk.Button(self.ruby_tab, text="Ruby Belgeleri", command=lambda: self.open_link("https://www.ruby-lang.org/en/documentation/"))
        ruby_resource_button.pack(pady=5)

    def populate_resources_tab(self):
        """Populate Resources tab with content."""
        resources_label = tk.Label(self.resources_tab, text="Önerilen Kaynaklar", font=("Arial", 16))
        resources_label.pack(pady=10)

        resources_text = tk.Text(self.resources_tab, wrap="word", height=25, width=100)
        resources_text.pack(pady=10)
        resources_text.insert(tk.END, """
Python:
- Python Belgeleri: https://docs.python.org/3/
- Real Python: https://realpython.com/
- Python for Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/
- Automate the Boring Stuff with Python: https://automatetheboringstuff.com/

Ruby:
- Ruby Belgeleri: https://www.ruby-lang.org/en/documentation/
- Ruby on Rails Guides: https://guides.rubyonrails.org/
- Learn Ruby the Hard Way: https://learnrubythehardway.org/book/
- The Ruby Programming Language: https://www.amazon.com/Ruby-Programming-Language-David-Flanagan/dp/0596516177
        """)
        resources_text.config(state="disabled")

    def populate_quiz_tab(self):
        """Populate Quiz tab with content."""
        quiz_label = tk.Label(self.quiz_tab, text="Quiz ve Egzersizler", font=("Arial", 16))
        quiz_label.pack(pady=10)

        quiz_description = tk.Text(self.quiz_tab, wrap="word", height=10, width=100)
        quiz_description.pack(pady=10)
        quiz_description.insert(tk.END, """
Bu bölümde Python ve Ruby ile ilgili kısa quizler ve kodlama egzersizleri bulabilirsiniz.
Her konunun sonunda öğrendiklerinizi pekiştirmek için quizleri çözün ve egzersizleri tamamlayın.
        """)
        quiz_description.config(state="disabled")

        quiz_frame = tk.Frame(self.quiz_tab)
        quiz_frame.pack(pady=10)

        python_quiz_button = tk.Button(quiz_frame, text="Python Quizine Başla", command=self.start_python_quiz)
        python_quiz_button.pack(side="left", padx=10)

        ruby_quiz_button = tk.Button(quiz_frame, text="Ruby Quizine Başla", command=self.start_ruby_quiz)
        ruby_quiz_button.pack(side="left", padx=10)

    def start_python_quiz(self):
        """Start Python quiz."""
        self.quiz_window("Python")

    def start_ruby_quiz(self):
        """Start Ruby quiz."""
        self.quiz_window("Ruby")

    def quiz_window(self, language):
        """Create a new window for quiz."""
        quiz_win = tk.Toplevel(self.root)
        quiz_win.title(f"{language} Quiz")
        quiz_win.geometry("800x600")

        quiz_label = tk.Label(quiz_win, text=f"{language} Quiz", font=("Arial", 16))
        quiz_label.pack(pady=10)

        questions = {
            "Python": [
                ("Python'da bir listeyi nasıl ters çevirebilirsiniz?", [
                    "list.reverse()", 
                    "reversed(list)", 
                    "list[::-1]", 
                    "list.reverse(:)"
                ], 2),
                ("Python'da hangi veri türü değiştirilemez?", [
                    "List", 
                    "Tuple", 
                    "Dictionary", 
                    "Set"
                ], 1),
                ("Python'da bir değişkenin tipini nasıl kontrol edersiniz?", [
                    "type(var)", 
                    "typeof(var)", 
                    "var.type()", 
                    "checktype(var)"
                ], 0),
            ],
            "Ruby": [
                ("Ruby'de bir dizi nasıl ters çevrilir?", [
                    "array.reverse", 
                    "reversed(array)", 
                    "array[::-1]", 
                    "reverse(array)"
                ], 0),
                ("Ruby'de hangi veri türü değiştirilemez?", [
                    "Array", 
                    "String", 
                    "Hash", 
                    "Symbol"
                ], 3),
                ("Ruby'de bir nesnenin tipini nasıl kontrol edersiniz?", [
                    "type(object)", 
                    "typeof(object)", 
                    "object.type", 
                    "object.class"
                ], 3),
            ],
        }

        self.current_question = 0
        self.score = 0

        def load_question():
            question, options, correct_option = questions[language][self.current_question]
            question_label.config(text=question)
            for idx, option in enumerate(options):
                option_buttons[idx].config(text=option, command=lambda idx=idx: check_answer(idx, correct_option))

        def check_answer(selected, correct):
            if selected == correct:
                self.score += 1
                messagebox.showinfo("Doğru!", "Cevabınız doğru!")
            else:
                messagebox.showerror("Yanlış!", "Yanlış cevap.")
            self.current_question += 1
            if self.current_question < len(questions[language]):
                load_question()
            else:
                messagebox.showinfo("Quiz Bitti", f"Quiz bitti! Skorunuz: {self.score}/{len(questions[language])}")
                quiz_win.destroy()

        question_label = tk.Label(quiz_win, text="", font=("Arial", 14))
        question_label.pack(pady=10)

        option_buttons = [tk.Button(quiz_win) for _ in range(4)]
        for button in option_buttons:
            button.pack(pady=5, fill="x")

        load_question()

    def populate_community_tab(self):
        """Populate Community tab with content."""
        community_label = tk.Label(self.community_tab, text="Topluluk", font=("Arial", 16))
        community_label.pack(pady=10)

        community_description = tk.Text(self.community_tab, wrap="word", height=10, width=100)
        community_description.pack(pady=10)
        community_description.insert(tk.END, """
Kod Akademisi Topluluğu'na hoş geldiniz! Burada diğer programcılarla iletişim kurabilir, sorular sorabilir ve bilgi paylaşabilirsiniz.
- Forumlar: Programlama ile ilgili her türlü konuda tartışma başlatın.
- Etkinlikler: Yaklaşan kodlama etkinlikleri ve buluşmaları hakkında bilgi alın.
- Projeler: Diğer kullanıcılarla birlikte projeler geliştirin.

Bağlantılar:
- Python Forum: https://www.python.org/community/forums/
- Ruby Forum: https://www.ruby-forum.com/
        """)
        community_description.config(state="disabled")

        forum_button = tk.Button(self.community_tab, text="Python Forumuna Git", command=lambda: self.open_link("https://www.python.org/community/forums/"))
        forum_button.pack(pady=5)

        forum_button = tk.Button(self.community_tab, text="Ruby Forumuna Git", command=lambda: self.open_link("https://www.ruby-forum.com/"))
        forum_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeAcademyApp(root)
    root.mainloop()
