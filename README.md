# SISTEMPAKAR
Dian Markuci - 1184095 - D4TI3C 

# ANALISIS BFS
Pertama saya akan menjelaskan analisis Breadth First Search Terlebih dahulu:

Misalnya berikut merupakan daftar nama ruangan yang ada di Rumah Sakit Majenang.
Penerapan ini menggunakan Python dictionary sebagai list/daftar kedekatan dengan struktur data kamus yang mana node memiliki list simpanan dari node yang berdekatan.

    graph = {
    'Anggrek' : ['Mawar','Kamboja'],
    'Mawar' : ['Melati', 'Raflesia'],
    'Kamboja' : ['Teratai'],
    'Melati' : [],
    'Raflesia' : ['Teratai'],
    'Teratai' : []
    }

    visited = []
visited disini merupakan daftar yang digunakan untuk melacak node yang dikunjungi.

    queue = [] 
queue disini merupakan daftar yang digunakan untuk melacak node yang saat ini masih berada dalam antrian.

    def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
        untuk algoritma BFS diatas:

Untuk algoritmanya awalnya akan dilakukan pengecekan setelah itu penambahan node awal ke daftar yg dikunjungi/visited dan queue.
Sedangkan queue yang isinya berupa elemen akan terus mengeluarkan node dari queue, kemudian menambah neighbour dari node ke queue apabila tidak dikunjungi, dan ditandai sebagai telah dikunjungi(visited) dan akan terus dilakukan sampai tidak ada antrian.

    bfs(visited, graph, 'Anggrek')

Fungsi bfs diatas merupakan visited(daftar yang dikunjungi), (grafik dalam bentuk kamus), dan (node awal anggrek).
Untuk penggambaran pohon nya dimulai dari anggrek, dengan menggunakan BFS maka akan mencari berdasarkan level pohon nya sehingga output yang akan dikeluarkan adalah Anggrek-Mawar-Kamboja-Melati-Raflesia-Teratai.

Anggrek berada di level 0, Kamboja dan Mawar berada di level 1 dan melati, raflesia dan teratai berada di level 2.

# ANALISIS DFS
Selanjutnya Analisis Depth First Seacrh :

Untuk Ilustrasi graph/grafik sama diwakili menggunakan daftar kedekatan dengan cara yang digunakan juga struktur data kamus, Setiap node memiliki daftar node yang berdekatan yang disimpan.

    visited = set() 
visited disini merupakan himpunan yang digunakan untuk melacak node yang dikunjungi.

    def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

Jadi, pertama kali node akan diperiksa, apakah node tidak di kunjungi dan jika benar, maka akan ditambahkan di visited set.
Kemudian untuk setiap neighbour dari node saat ini, dfs fungsi tersebut akan dipanggil lagi.

dfs Fungsi ini di panggil dan diberikan visited set, graph dalam bentuk kamus, Anggrek yang merupakan node awal.

Untuk algoritmanya pencarian dimulai dari root tree nya kemudian dilanjutkan sejauh mungkin ke node child sebelum dilakukan backtracking. 
node awal dimulai dari Anggrek kemudian dilanjutkan mengikuti anak panah Mawar kemudian ke Melati kembali lagi di lanjutkan ke Raflesia lalu ke Teratai dan yang terakhir Kamboja  maka output yang dihasilkan adalah 
Anggrek-Mawar-Melati-Raflesia-Teratai-Kamboja

