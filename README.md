# Static Site Generator

The following project is a static site generator made in Python. It converts markdown files to HTML creating static pages of content. 

## 🚀 Demonstration
Page [here](https://luis-octavius.github.io/static-site-generator/)

  
## 🛠️ Technologies

- **Languages:** Python
- **Bibliotecas:** sys, os, re, Path 
- **Ferramentas:** bash, http.server

## 🔧 Instalation

Clone it.
```bash 
git clone https://github.com/luis-octavius/static-site-generator.git && cd static-site-generator
```
## ⚙ How to use

```bash
# give build.sh and main.sh permission to execute
chmod +x build.sh && chmod +x main.sh

# run it
./build.sh

# host page onto a server
./main.sh
```

> **ℹ️ Important:**  
> To use it with your own files and assets, just change the content/ and static/ folders to your own like  

## 🧪 Tests
```bash
# execute unit tests
chmod +x test.sh
./test.sh
```

## 📁 Folder Structure

```bash
── build.sh
├── content
│   ├── blog
│   │   ├── glorfindel
│   │   │   └── index.md
│   │   ├── majesty
│   │   │   └── index.md
│   │   └── tom
│   │       └── index.md
│   ├── contact
│   │   └── index.md
│   └── index.md
├── main.sh
├── README.md
├── src
│   ├── blocks.py
│   ├── extract.py
│   ├── generate_page.py
│   ├── htmlnode.py
│   ├── inline_markdown.py
│   ├── main.py
│   ├── split_nodes.py
│   ├── test_blocks.py
│   ├── test_extract.py
│   ├── test_htmlnode.py
│   ├── test_inline_markdown.py
│   ├── test_split_nodes.py
│   ├── test_textnode.py
│   └── textnode.py
├── static
│   ├── images
│   │   ├── glorfindel.png
│   │   ├── rivendell.png
│   │   ├── tolkien.png
│   │   └── tom.png
│   └── index.css
├── template.html
└── test.sh
```

## 🤝 How to contribute
1. Fork the project
2. Create a branch to your feature (git checkout -b feature/SomeFeature)
3. Commit your changes (git commit -m 'Add some SomeFeature')
4. Push to branch (git push origin feature/SomeFeature)
5. Open a pull request

## 📝 License
This project is under MIT License.

👥 Autores
Nome - @usuario
