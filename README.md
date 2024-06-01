# kodakademisipy

EN: This code is an educational application for users who want to learn Python and Ruby programming languages. The application has a graphical user interface (GUI) built using the Tkinter library. Here is the outline of the code and its functions:

Main Class: CodeAcademyApp
This class creates the application's main window and tabs.

Constructor Method: __init__
self.root: Represents the main window.
Window title and dimensions are adjusted.
self.create_widgets(): Allows the creation of widgets.
Creating Widgets: create_widgets
This method creates different tabs and contents of the application.

Creating Tabs: create_tabs
self.tab_control: The main object that controls tabs.
Python, Ruby, Resources, Quiz and Community tabs are created.
Python Tab: populate_python_tab
Contains information and code examples about Python.
Descriptions and codes for code examples are added.
There is a button that takes you to the Python documentation.
Ruby Tab: populate_ruby_tab
Contains information and code examples about Ruby.
Descriptions and codes for code examples are added.
There is a button that takes you to the Ruby documentation.
Resources Tab: populate_resources_tab
Recommended resources for Python and Ruby are listed.
Quiz Tab: populate_quiz_tab
Contains short quizzes and exercises for Python and Ruby.
There are quiz start buttons.
Community Tab: populate_community_tab
Contains community information and forum links.
Quiz Functions
start_python_quiz: Starts the Python quiz.
start_ruby_quiz: Starts the Ruby quiz.
quiz_window: Creates the quiz window and loads the questions.
Auxiliary Functions
create_code_example: Adds code examples and explanations to tabs.
open_link: Used to open a URL.
Sample Python Codes
It contains examples on various topics such as simple function, loop, class and object, JSON processing, recursive function, user input and error handling.
Sample Ruby Codes
It contains examples on various topics such as simple function, loop, class and object, JSON processing, recursive function, user input and error handling.
Quiz Content
Includes short quizzes, multiple choice questions, and true/false feedback for Python and Ruby.
This application provides a comprehensive tool for users to learn and practice Python and Ruby programming languages. It supports the training process with its user-friendly interface and extensive content.


TR: Bu kod, Python ve Ruby programlama dillerini öğrenmek isteyen kullanıcılar için bir eğitim uygulamasıdır. Uygulama, Tkinter kütüphanesi kullanılarak oluşturulmuş bir grafik kullanıcı arayüzüne (GUI) sahiptir. İşte kodun ana hatları ve işlevleri:

Ana Sınıf: CodeAcademyApp
Bu sınıf, uygulamanın ana penceresini ve sekmelerini oluşturur.

Yapıcı Metot: __init__
self.root: Ana pencereyi temsil eder.
Pencere başlığı ve boyutları ayarlanır.
self.create_widgets(): Widget'ların oluşturulmasını sağlar.
Widget'ların Oluşturulması: create_widgets
Bu metot, uygulamanın farklı sekmelerini ve içeriğini oluşturur.

Sekmelerin Oluşturulması: create_tabs
self.tab_control: Sekmeleri kontrol eden ana nesne.
Python, Ruby, Kaynaklar, Quiz ve Topluluk sekmeleri oluşturulur.
Python Sekmesi: populate_python_tab
Python hakkında bilgi ve kod örnekleri içerir.
Kod örnekleri için açıklamalar ve kodlar eklenir.
Python belgelerine yönlendiren bir buton bulunur.
Ruby Sekmesi: populate_ruby_tab
Ruby hakkında bilgi ve kod örnekleri içerir.
Kod örnekleri için açıklamalar ve kodlar eklenir.
Ruby belgelerine yönlendiren bir buton bulunur.
Kaynaklar Sekmesi: populate_resources_tab
Python ve Ruby için önerilen kaynaklar listelenir.
Quiz Sekmesi: populate_quiz_tab
Python ve Ruby için kısa quizler ve egzersizler içerir.
Quiz başlatma butonları bulunur.
Topluluk Sekmesi: populate_community_tab
Topluluk ile ilgili bilgiler ve forum bağlantıları içerir.
Quiz Fonksiyonları
start_python_quiz: Python quizini başlatır.
start_ruby_quiz: Ruby quizini başlatır.
quiz_window: Quiz penceresini oluşturur ve soruları yükler.
Yardımcı Fonksiyonlar
create_code_example: Kod örneklerini ve açıklamalarını sekmelere ekler.
open_link: Bir URL açmak için kullanılır.
Örnek Python Kodları
Basit fonksiyon, döngü, sınıf ve nesne, JSON işleme, rekursif fonksiyon, kullanıcı girişi ve hata yönetimi gibi çeşitli konularda örnekler içerir.
Örnek Ruby Kodları
Basit fonksiyon, döngü, sınıf ve nesne, JSON işleme, rekursif fonksiyon, kullanıcı girişi ve hata yönetimi gibi çeşitli konularda örnekler içerir.
Quiz İçeriği
Python ve Ruby için kısa quizler, çoktan seçmeli sorular ve doğru/yanlış geri bildirimleri içerir.
Bu uygulama, kullanıcıların Python ve Ruby programlama dillerini öğrenmeleri ve pratik yapmaları için kapsamlı bir araç sunar. Kullanıcı dostu arayüzü ve geniş içeriği ile eğitim sürecini destekler.





