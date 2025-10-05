from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- Data dan fungsi dari kode Anda ---
JURUSAN_DB = [
    {
    "nama": "Administrasi Bisnis",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari seluruh proses pengelolaan perusahaan atau organisasi secara komprehensif, mulai dari perencanaan, pengorganisasian, pemasaran, sumber daya manusia, hingga keuangan untuk mencapai tujuan bisnis dan mendorong pertumbuhan.",
    "karier": "Spesialis Pemasaran, Manajer Operasional, Analis Bisnis, Konsultan Manajemen, Staf Sumber Daya Manusia (HRD)"
  },
  {
    "nama": "Administrasi Fiskal",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan keuangan publik (pemerintah) dan perpajakan. Fokusnya pada perencanaan anggaran negara, sistem perpajakan, serta analisis kebijakan fiskal dan keuangan.",
    "karier": "Analis Anggaran, Konsultan Pajak, Auditor Pajak, Akuntan Pajak, Pegawai Direktorat Jenderal Pajak (DJP)"
  },
  {
    "nama": "Administrasi Negara",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manajemen dan implementasi kebijakan publik serta penyelenggaraan pemerintahan di lembaga eksekutif, legislatif, dan yudikatif untuk memberikan pelayanan publik yang efisien dan akuntabel.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Manajer Layanan Publik, Konsultan Pemerintahan, Peneliti"
  },
  {
    "nama": "Administrasi Niaga",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang strategi pengelolaan dan pengorganisasian seluruh aktivitas bisnis dan niaga, termasuk pemasaran, keuangan, produksi, dan sumber daya manusia, untuk menciptakan keuntungan dan keunggulan kompetitif.",
    "karier": "Staf Pemasaran, Manajer Penjualan, Business Development, Staf HRD, Wirausaha (Entrepreneur)"
  },
  {
    "nama": "Administrasi Pendidikan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip manajemen, perencanaan, pengorganisasian, dan evaluasi untuk mengelola lembaga pendidikan secara efektif dan efisien.",
    "karier": "Pelaksana Tata Kelola Satuan Pendidikan, Analis Perencanaan Pendidikan, Staf Administrasi Kementerian Pendidikan, Konsultan Pendidikan, Direktur Lembaga Kependidikan"
  },
  {
    "nama": "Administrasi Perkantoran",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengetahuan dan keterampilan dalam mengelola pekerjaan dan operasional perkantoran, termasuk manajemen kearsipan, teknologi informasi perkantoran, dan pelayanan prima (kesekretariatan).",
    "karier": "Staf Administrasi, Sekretaris, Asisten Manajer, Pegawai Bank, Staf Personalia/HRD"
  },
  {
    "nama": "Administrasi Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang perhitungan, pemungutan, pelaporan, dan sistem administrasi berbagai jenis pajak (Pusat dan Daerah) serta hak dan kewajiban wajib pajak.",
    "karier": "Konsultan Pajak, Pegawai Direktorat Jenderal Pajak (DJP), Staf Perpajakan Perusahaan, Kuasa Hukum Pajak, Akuntan"
  },
  {
    "nama": "Administrasi Publik",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya dan implementasi kebijakan di sektor publik (pemerintahan) untuk memberikan pelayanan dan tata kelola yang baik (good governance) kepada masyarakat.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Manajer Program LSM/NGO, Konsultan Pemerintahan, Pegawai BUMN"
  },
  {
    "nama": "Agribisnis",
    "mata_pelajaran": "Biologi, Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan usaha (bisnis) di bidang pertanian dan pangan secara terpadu, mulai dari pra-produksi, produksi, pascapanen, hingga pemasaran hasil pertanian.",
    "karier": "Manajer Agribisnis, Konsultan Pertanian, Pengembang Produk Pertanian, Analis Pasar Komoditas, Wirausaha Pertanian"
  },
  {
    "nama": "Agroekoteknologi",
    "mata_pelajaran": "Biologi, Fisika",
    "deskripsi": "ilmu yang mempelajari penerapan teknologi dan prinsip ekologi dalam sistem budidaya pertanian untuk menghasilkan produk yang berkualitas sambil menjaga kelestarian lingkungan.",
    "karier": "Agronom, Peneliti Pertanian, Manajer Lahan dan Tanaman, Konsultan Pertanian Berkelanjutan, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Agronomi dan Holtikultura",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari tentang pengelolaan tanaman pangan, perkebunan, dan holtikultura (buah, sayur, dan bunga) secara efisien dan berkelanjutan untuk meningkatkan hasil dan kualitas produksi.",
    "karier": "Agronom, Manajer Kebun/Lahan, Peneliti Tanaman, Konsultan Holtikultura, Wirausaha Pertanian"
  },
  {
    "nama": "Agroteknologi",
    "mata_pelajaran": "Biologi, Fisika",
    "deskripsi": "ilmu yang mempelajari penerapan teknologi, rekayasa, dan mekanisasi untuk mengoptimalkan produksi tanaman dan manajemen sumber daya pertanian secara efisien dan modern.",
    "karier": "Insinyur Pertanian, Pengembang Teknologi Pertanian, Manajer Proyek Pertanian Modern, Peneliti Agroteknologi, Konsultan Pertanian"
  },
  {
    "nama": "Akademi Militer",
    "mata_pelajaran": "Biologi, Kimia, Fisika",
    "deskripsi": "Institusi pendidikan kedinasan yang mendidik dan melatih calon perwira Tentara Nasional Indonesia (TNI) Angkatan Darat, fokus pada ilmu kepemimpinan, strategi militer, dan pengetahuan umum serta teknik militer.",
    "karier": "Perwira TNI Angkatan Darat"
  },
  {
    "nama": "Aktuaria",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang menerapkan teori matematika, probabilitas, dan statistika untuk menganalisis risiko keuangan di industri asuransi, dana pensiun, dan investasi.",
    "karier": "Aktuaris, Analis Risiko, Manajer Risiko, Konsultan Asuransi, Analis Investasi"
  },
  {
    "nama": "Akuakultur",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari budidaya organisme air (ikan, udang, kerang, rumput laut) secara terkontrol, mulai dari pembenihan, pembesaran, hingga pengelolaan kualitas air dan pencegahan penyakit.",
    "karier": "Pembudidaya Perikanan, Manajer Produksi Tambak/Kolam, Peneliti Akuakultur, Konsultan Perikanan, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Akuntansi",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari proses pencatatan, pengklasifikasian, pengolahan, dan penyajian data transaksi keuangan untuk menghasilkan informasi yang relevan dalam pengambilan keputusan bisnis.",
    "karier": "Akuntan Publik, Akuntan Manajemen, Auditor, Konsultan Keuangan, Analis Keuangan"
  },
  {
    "nama": "Akuntansi Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pencatatan dan pelaporan transaksi keuangan dengan fokus pada kepatuhan terhadap peraturan perpajakan, baik untuk pelaporan internal maupun eksternal (pemerintah).",
    "karier": "Akuntan Pajak, Konsultan Pajak, Staf Perpajakan Perusahaan, Auditor Pajak"
  },
  {
    "nama": "Analis Farmasi dan Makanan",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari analisis bahan farmasi dan makanan termasuk kualitas, keamanan, dan standar produksi serta pengujian laboratorium untuk memastikan produk aman dan memenuhi regulasi.",
    "karier": "Analis Laboratorium, Quality Control (QC), Quality Assurance (QA), Peneliti Kualitas Pangan, Pengawas Obat dan Makanan (BPOM)"
  },
  {
    "nama": "Animasi",
    "mata_pelajaran": "Seni Budaya, Matematika",
    "deskripsi": "ilmu yang mempelajari proses pembuatan gambar bergerak (animasi) menggunakan berbagai teknik (2D, 3D, stop motion), termasuk konsep cerita, desain karakter, hingga produksi akhir.",
    "karier": "Animator 2D/3D, Storyboard Artist, Concept Artist, Sutradara Animasi, Desainer Karakter"
  },
  {
    "nama": "Antropologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manusia secara holistik dari aspek budaya, masyarakat, bahasa, dan biologi di berbagai penjuru dunia dari masa lalu hingga kini.",
    "karier": "Peneliti Sosial, Etnografer, Konsultan Budaya, Analis Data Sosial, Pegawai Lembaga Kebudayaan"
  },
  {
    "nama": "Arkeologi",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari kebudayaan masa lalu manusia melalui penelitian sistematis terhadap tinggalan-tinggalan (artefak, situs, monumen) yang dapat digali dan dianalisis.",
    "karier": "Arkeolog, Kurator Museum, Peneliti Sejarah dan Purbakala, Konsultan Peninggalan Budaya"
  },
  {
    "nama": "Arsitektur",
    "mata_pelajaran": "Matematika, Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan dan pembangunan struktur bangunan, baik dari segi fungsi, estetika, konstruksi, maupun aspek lingkungan, dengan menitikberatkan pada ruang dan bentuk.",
    "karier": "Arsitek Perancang, Konsultan Konstruksi, Pengembang Properti, Pengawas Lapangan, Desainer Interior"
  },
  {
    "nama": "Arsitektur Lansekap",
    "mata_pelajaran": "Matematika, Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan, perencanaan, dan pengelolaan ruang terbuka (outdoor) dan lingkungan binaan (taman, kota, kawasan) dengan mempertimbangkan aspek ekologi, sosial, dan estetika.",
    "karier": "Arsitek Lansekap, Desainer Taman Kota, Perencana Wilayah, Konsultan Lingkungan, Pengembang Properti"
  },
  {
    "nama": "Astronomi",
    "mata_pelajaran": "Matematika Tingkat Lanjut, Fisika",
    "deskripsi": "ilmu yang mempelajari benda-benda langit, fenomena alam di luar atmosfer bumi, asal-usul alam semesta, dan hukum-hukum fisika yang mengaturnya.",
    "karier": "Astronom/Peneliti Observatorium, Dosen/Pendidik, Analis Data Sains, Spesialis Penginderaan Jauh"
  },
  {
    "nama": "Bahasa Inggris",
    "mata_pelajaran": "Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari struktur bahasa (linguistik), sastra, dan budaya masyarakat penutur Bahasa Inggris untuk menguasai kemampuan komunikasi, analisis, dan pemahaman lintas budaya.",
    "karier": "Penerjemah/Juru Bahasa, Penulis/Editor, Spesialis Komunikasi Internasional, Staf Kedutaan, Pengajar Bahasa"
  },
  {
    "nama": "Bahasa Jepang",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Jepang untuk menguasai kemampuan komunikasi, terjemahan, dan pemahaman mendalam tentang masyarakat Jepang.",
    "karier": "Penerjemah/Juru Bahasa Jepang, Staf Perusahaan Jepang, Pemandu Wisata, Spesialis Hubungan Internasional, Staf Kedutaan"
  },
  {
    "nama": "Bimbingan & Konseling",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari teori dan praktik membantu individu mengembangkan potensi diri, mengatasi masalah psikologis, sosial, dan karier, serta membuat keputusan yang tepat.",
    "karier": "Guru Bimbingan dan Konseling (BK), Konselor Karier, Konselor Pendidikan, Terapis, Staf Sumber Daya Manusia"
  },
  {
    "nama": "Biokimia",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari proses kimia yang terjadi di dalam organisme hidup, termasuk struktur dan fungsi biomolekul (protein, karbohidrat, lemak, asam nukleat) serta metabolisme.",
    "karier": "Peneliti Biokimia, Analis Laboratorium Klinis, Spesialis Quality Control Farmasi, Teknolog Pangan, Pengembang Produk Bioteknologi"
  },
  {
    "nama": "Biologi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari segala aspek kehidupan dan makhluk hidup, mulai dari struktur sel, fungsi organ, interaksi antar organisme, hingga evolusi dan lingkungan.",
    "karier": "Peneliti Biologi, Staf Konservasi Lingkungan, Analis Laboratorium, Teknisi Bioteknologi, Pengembang Produk Farmasi"
  },
  {
    "nama": "Bisnis Digital",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari strategi bisnis, pemasaran, dan manajemen operasional yang memanfaatkan teknologi digital dan platform online (e-commerce, media sosial, big data).",
    "karier": "Manajer Pemasaran Digital, Analis Data Bisnis, Spesialis E-Commerce, Konsultan Teknologi Bisnis, Wirausaha Digital"
  },
  {
    "nama": "Bisnis Islam/Syariah",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip dan praktik bisnis, manajemen, serta keuangan yang sesuai dengan nilai-nilai dan hukum syariah (Islam).",
    "karier": "Manajer Keuangan Syariah, Spesialis Pemasaran Halal, Konsultan Bisnis Islam, Auditor Syariah, Wirausaha"
  },
  {
    "nama": "Bisnis Kreatif",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang pengembangan dan pengelolaan usaha yang berbasis pada ide, kreativitas, dan kekayaan intelektual (misalnya di bidang seni, desain, media, dan teknologi).",
    "karier": "Manajer Proyek Kreatif, Konsultan Bisnis Kreatif, Desainer Produk, Spesialis Pemasaran Konten, Wirausaha Industri Kreatif"
  },
  {
    "nama": "Budidaya Perairan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari teknik-teknik pengembangan, pemeliharaan, dan panen organisme air (ikan, udang, kerang) dengan fokus pada efisiensi, kualitas, dan keberlanjutan.",
    "karier": "Manajer Budidaya Perairan, Peneliti Kelautan, Quality Control Hasil Perikanan, Konsultan Akuakultur, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Budidaya Peternakan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen dan teknik pemeliharaan ternak (sapi, ayam, kambing, dll.) mulai dari bibit, pakan, kesehatan, hingga pengolahan hasil ternak.",
    "karier": "Manajer Peternakan, Konsultan Ternak, Peneliti Pakan Ternak, Quality Control Produk Hewani, Pegawai Dinas Peternakan"
  },
  {
    "nama": "Desain Komunikasi Visual",
    "mata_pelajaran": "Seni Budaya, Matematika",
    "deskripsi": "ilmu yang mempelajari penyampaian pesan atau informasi melalui media visual (gambar, tipografi, video) untuk tujuan pemasaran, edukasi, atau seni.",
    "karier": "Desainer Grafis, Illustrator, Creative Director, UI/UX Designer, Motion Graphic Artist"
  },
  {
    "nama": "Ekonomi Islam/Syariah",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari prinsip, sistem, dan mekanisme ekonomi serta keuangan yang berlandaskan pada ajaran dan etika Islam.",
    "karier": "Analis Keuangan Syariah, Manajer Bank Syariah, Auditor Syariah, Konsultan Keuangan Islam, Dosen Ekonomi Syariah"
  },
  {
    "nama": "Ekonomi Pembangunan",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari isu-isu pembangunan ekonomi di suatu wilayah atau negara, termasuk perencanaan, kebijakan, pertumbuhan ekonomi, dan kesejahteraan masyarakat.",
    "karier": "Analis Ekonomi, Perencana Pembangunan Daerah (Bappeda), Konsultan Pembangunan, Peneliti Ekonomi, Staf Lembaga Keuangan Internasional"
  },
  {
    "nama": "Ekonomi Sumberdaya & Lingkungan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari hubungan antara aktivitas ekonomi, pengelolaan sumber daya alam, dan pelestarian lingkungan, termasuk analisis kebijakan lingkungan.",
    "karier": "Analis Kebijakan Lingkungan, Konsultan Amdal/EIA, Staf Konservasi, Peneliti Ekonomi Sumber Daya, Pegawai Kementerian Lingkungan Hidup"
  },
  {
    "nama": "Ekowisata",
    "mata_pelajaran": "Biologi, Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan wisata alam yang bertanggung jawab, berfokus pada konservasi lingkungan, pemberdayaan masyarakat lokal, dan edukasi.",
    "karier": "Manajer Ekowisata, Konsultan Pariwisata Berkelanjutan, Pemandu Wisata Alam, Pegawai Dinas Pariwisata, Wirausaha Tour & Travel"
  },
  {
    "nama": "Etnomusikologi",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari musik dalam konteks budaya dan sosial masyarakat, meliputi asal-usul, fungsi, sejarah, dan struktur musik tradisional.",
    "karier": "Peneliti Musik, Kurator Seni Musik, Konsultan Budaya, Komposer, Pengajar Musik Tradisional"
  },
  {
    "nama": "Farmasi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari identifikasi, pengembangan, pembuatan, formulasi, pengujian, dan distribusi obat, serta konseling penggunaan obat yang aman dan efektif.",
    "karier": "Apoteker (di Apotek/Rumah Sakit), Peneliti Obat (R&D), Quality Control/Assurance Farmasi, Staf Produksi Obat, Konsultan Farmasi Klinis"
  },
  {
    "nama": "Filsafat",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari hakikat segala sesuatu dengan menggunakan akal budi untuk mencari kebenaran, mulai dari logika, etika, estetika, hingga metafisika.",
    "karier": "Peneliti/Akademisi, Konsultan Etika Bisnis, Penulis/Editor, Analis Kebijakan, Jurnalis"
  },
  {
    "nama": "Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari sifat dan interaksi materi serta energi dalam ruang dan waktu, termasuk hukum-hukum fundamental alam semesta.",
    "karier": "Fisikawan (Peneliti), Analis Data, Spesialis Instrumentasi, Ahli Metrologi, Dosen/Pendidik"
  },
  {
    "nama": "Gizi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari hubungan antara makanan dan kesehatan, termasuk komposisi gizi, perencanaan menu, dan penanganan masalah gizi individu maupun publik.",
    "karier": "Ahli Gizi (Dietisien) di Rumah Sakit, Konsultan Gizi Masyarakat, Quality Control Pangan, Product Developer Makanan, Tenaga Penyuluh Kesehatan"
  },
  {
    "nama": "Hubungan Internasional",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari interaksi antar negara, aktor non-negara (organisasi internasional, NGO), diplomasi, politik global, dan isu-isu lintas batas.",
    "karier": "Diplomat, Analis Politik Internasional, Staf Organisasi Internasional (PBB, ASEAN), Konsultan Global, Jurnalis Internasional"
  },
  {
    "nama": "Ilmu Biomedis",
    "mata_pelajaran": "Biologi, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari dasar-dasar biologi dan kimia tubuh manusia dalam kaitannya dengan penyakit, termasuk pengembangan teknologi untuk diagnosis dan terapi.",
    "karier": "Peneliti Biomedis, Spesialis Laboratorium Medis, Pengembang Alat Kesehatan, Staf Industri Farmasi/Bioteknologi"
  },
  {
    "nama": "Ilmu Hukum",
    "mata_pelajaran": "Sosiologi, Pancasila",
    "deskripsi": "ilmu yang mempelajari sistem peraturan (hukum) yang berlaku, yurisprudensi, dan proses peradilan untuk menciptakan ketertiban dan keadilan dalam masyarakat.",
    "karier": "Pengacara/Advokat, Notaris, Jaksa, Hakim, Legal Officer Perusahaan, Konsultan Hukum"
  },
  {
    "nama": "Ilmu Kelautan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari ekosistem laut, oseanografi, sumber daya hayati laut, hingga teknologi eksplorasi dan pemanfaatan kekayaan laut secara berkelanjutan.",
    "karier": "Peneliti Kelautan, Konsultan Lingkungan Pesisir, Manajer Kawasan Konservasi Laut, Staf Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Ilmu Keolahragaan",
    "mata_pelajaran": "PJOK, Biologi",
    "deskripsi": "ilmu yang mempelajari aspek ilmiah dari aktivitas fisik, olahraga, dan kesehatan, termasuk biomekanika, fisiologi olahraga, dan psikologi olahraga.",
    "karier": "Fisioterapis Olahraga, Pelatih Fisik (Strength and Conditioning Coach), Manajer Klub Olahraga, Konsultan Kebugaran"
  },
  {
    "nama": "Ilmu Komputer",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari teori komputasi, perancangan perangkat keras (hardware), dan pengembangan perangkat lunak (software) serta algoritma.",
    "karier": "Software Developer, Data Scientist, System Analyst, Konsultan IT, Peneliti Komputasi"
  },
  {
    "nama": "Ilmu Komunikasi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari proses penyampaian pesan dari komunikator kepada komunikan, termasuk media massa, komunikasi interpersonal, dan komunikasi strategis (PR & Marketing).",
    "karier": "Spesialis Hubungan Masyarakat (PR), Jurnalis/Reporter, Content Creator, Manajer Media Sosial, Konsultan Komunikasi Pemasaran"
  },
  {
    "nama": "Ilmu Pemerintahan",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari struktur, fungsi, dan dinamika lembaga pemerintahan, proses kebijakan publik, dan hubungan antara pemerintah dengan masyarakat dan lembaga lainnya.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Staf Legislatif, Peneliti Pemerintahan, Konsultan Politik"
  },
  {
    "nama": "Ilmu Perpustakaan",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari manajemen informasi, sistem pengorganisasian pengetahuan, teknologi perpustakaan, dan pelayanan informasi kepada pengguna.",
    "karier": "Pustakawan, Pengelola Arsip Digital, Kurator Informasi, Konsultan Informasi, Staf Database Perusahaan"
  },
  {
    "nama": "Ilmu Politik",
    "mata_pelajaran": "Sosiologi, Pancasila",
    "deskripsi": "ilmu yang mempelajari teori dan praktik politik, sistem pemerintahan, perilaku politik, serta kekuasaan dan pengambilan keputusan dalam negara.",
    "karier": "Analis Politik, Staf Legislatif/Parlemen, Konsultan Kampanye Politik, Jurnalis Politik, Pegawai Kementerian Luar Negeri"
  },
  {
    "nama": "Ilmu Tanah",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari sifat, genesis, klasifikasi, survei, dan pemetaan tanah serta manajemen kesuburan tanah untuk pertanian dan lingkungan.",
    "karier": "Ahli Konservasi Tanah, Peneliti Tanah, Analis Laboratorium Tanah, Konsultan Pertanian, Pegawai Dinas Pertanian/Lingkungan"
  },
  {
    "nama": "Informatika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan penerapan sistem komputasi untuk mengolah dan menganalisis informasi secara efisien.",
    "karier": "Software Engineer, Data Scientist, Pengembang Aplikasi Mobile, Konsultan IT, Analis Keamanan Siber"
  },
  {
    "nama": "IPDN",
    "mata_pelajaran": "Matematika, Bahasa Indonesia, Fisika, Sejarah",
    "deskripsi": "Institusi pendidikan kedinasan yang mendidik calon Aparatur Sipil Negara (ASN) yang berorientasi pada bidang kepamongprajaan, manajemen pemerintahan, dan administrasi publik, dengan sistem pendidikan berasrama dan disiplin tinggi.",
    "karier": "Aparatur Sipil Negara (ASN) di Pemerintah Pusat dan Daerah (Kementerian Dalam Negeri, Pemerintah Provinsi/Kabupaten/Kota)"
  },
  {
    "nama": "K3 (Kesehatan dan Keselamatan Kerja)",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari identifikasi, evaluasi, dan pengendalian risiko bahaya di tempat kerja untuk mencegah kecelakaan, penyakit akibat kerja, dan meningkatkan kesehatan pekerja.",
    "karier": "Petugas K3 (Safety Officer), Auditor K3, Konsultan K3, Spesialis Higiene Industri, Manajer Lingkungan, Kesehatan, dan Keselamatan (EHS)"
  },
  {
    "nama": "Kebidanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pelayanan kesehatan reproduksi perempuan, mulai dari masa kehamilan, persalinan, nifas, bayi baru lahir, hingga kesehatan seksual.",
    "karier": "Bidan Praktik Mandiri, Bidan Rumah Sakit/Puskesmas, Konsultan Kesehatan Ibu dan Anak, Pengajar Kebidanan"
  },
  {
    "nama": "Kedokteran",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari diagnosis, pengobatan, dan pencegahan penyakit serta peningkatan kesehatan manusia secara komprehensif.",
    "karier": "Dokter Umum, Dokter Spesialis, Peneliti Kesehatan, Staf Medis Lembaga Internasional, Dosen Kedokteran"
  },
  {
    "nama": "Kedokteran Gigi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari kesehatan gigi dan mulut, termasuk diagnosis, pengobatan, pencegahan masalah, dan estetika rongga mulut.",
    "karier": "Dokter Gigi Umum, Dokter Gigi Spesialis (Ortodonti, Bedah Mulut), Peneliti Kesehatan Gigi, Staf Industri Alat Kesehatan"
  },
  {
    "nama": "Kedokteran Hewan",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari pencegahan, diagnosis, dan pengobatan penyakit pada hewan, serta memastikan keamanan pangan asal hewan (Zoo Health dan Public Health).",
    "karier": "Dokter Hewan Praktisi, Dokter Hewan Karantina, Peneliti Hewan, Quality Control Produk Hewani, Staf Industri Pakan Ternak"
  },
  {
    "nama": "Kehutanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan, pelestarian, dan pemanfaatan sumber daya hutan secara berkelanjutan, termasuk konservasi ekosistem dan hasil hutan.",
    "karier": "Rimbawan/Manajer Hutan, Konsultan Konservasi, Analis Kebijakan Kehutanan, Peneliti Kehutanan, Pegawai Kementerian Lingkungan Hidup dan Kehutanan"
  },
  {
    "nama": "Keperawatan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari asuhan keperawatan, perawatan, dan pemulihan kesehatan individu, keluarga, dan masyarakat dengan fokus pada kebutuhan holistik pasien.",
    "karier": "Perawat Klinis (Rumah Sakit/Puskesmas), Perawat Homecare, Perawat Kesehatan Komunitas, Dosen Keperawatan, Manajer Pelayanan Kesehatan"
  },
  {
    "nama": "Kesehatan Masyarakat",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari upaya pencegahan penyakit dan peningkatan kesehatan populasi melalui intervensi, kebijakan, promosi kesehatan, dan manajemen kesehatan lingkungan.",
    "karier": "Epidemiolog, Manajer Administrasi Rumah Sakit, Spesialis Promosi Kesehatan, Analis Kebijakan Kesehatan, Konsultan Kesehatan Lingkungan"
  },
  {
    "nama": "Kesejahteraan Sosial",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari upaya membantu individu, keluarga, dan kelompok masyarakat untuk meningkatkan kemampuan fungsional dan kesejahteraan sosialnya.",
    "karier": "Pekerja Sosial, Konselor Sosial, Fasilitator Pemberdayaan Masyarakat, Analis Kebijakan Sosial, Staf NGO/LSM"
  },
  {
    "nama": "Kewirausahaan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari proses penciptaan dan pengelolaan bisnis baru, termasuk identifikasi peluang, pengembangan ide, manajemen risiko, dan strategi pertumbuhan.",
    "karier": "Wirausaha (Entrepreneur), Konsultan Bisnis Startup, Manajer Inovasi Perusahaan, Business Development, Analis Pasar"
  },
  {
    "nama": "Kimia",
    "mata_pelajaran": "Kimia",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, sifat, dan perubahan zat, serta interaksi materi dan energi pada tingkat molekuler dan atom.",
    "karier": "Kimiawan (Peneliti), Analis Laboratorium (Industri/Klinis), Quality Control Industri, Pengembang Produk Kimia, Dosen/Pendidik"
  },
  {
    "nama": "Konservasi Sumberdaya Hutan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan, perlindungan, dan pemulihan sumber daya alam hutan, termasuk flora dan fauna, untuk menjamin kelestariannya.",
    "karier": "Spesialis Konservasi Alam, Manajer Kawasan Konservasi, Peneliti Kehutanan/Lingkungan, Konsultan Amdal, Pegawai Kementerian Kehutanan"
  },
  {
    "nama": "Kriminologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari sebab-sebab terjadinya kejahatan, pelaku kriminal, respons masyarakat terhadap kejahatan, dan sistem peradilan pidana.",
    "karier": "Analis Kriminalitas, Peneliti Kriminologi, Konsultan Keamanan, Staf Lembaga Pemasyarakatan, Pegawai Kepolisian/BNN"
  },
  {
    "nama": "Kriya Seni",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari penciptaan benda-benda seni terapan (kerajinan) yang memiliki fungsi praktis dan nilai estetika, menggunakan berbagai media (tekstil, keramik, kayu).",
    "karier": "Desainer Produk Kriya, Seniman Kriya, Kurator Seni, Pengajar Seni, Wirausaha Kerajinan"
  },
  {
    "nama": "Manajemen",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengorganisasian, pengarahan, dan pengendalian sumber daya organisasi (manusia, keuangan, material) untuk mencapai tujuan secara efektif dan efisien.",
    "karier": "Manajer Pemasaran, Manajer Keuangan, Manajer Sumber Daya Manusia (HR), Konsultan Manajemen, Analis Bisnis"
  },
  {
    "nama": "Manajemen Agribisnis",
    "mata_pelajaran": "Ekonomi, Biologi",
    "deskripsi": "ilmu yang mempelajari penerapan prinsip-prinsip manajemen dalam rantai nilai bisnis pertanian, mulai dari pengadaan sarana produksi hingga pemasaran produk hasil pertanian.",
    "karier": "Manajer Agribisnis, Analis Pasar Komoditas Pertanian, Konsultan Bisnis Pertanian, Manajer Rantai Pasok Pangan, Wirausaha Pertanian"
  },
  {
    "nama": "Manajemen Pelabuhan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengoperasian, dan pengelolaan fasilitas serta kegiatan logistik dan transportasi di area pelabuhan dan perairan.",
    "karier": "Staf Operasional Pelabuhan, Manajer Logistik Maritim, Analis Rantai Pasok, Staf Bea Cukai, Konsultan Logistik"
  },
  {
    "nama": "Matematika",
    "mata_pelajaran": "Matematika Tingkat Lanjut, Matematika",
    "deskripsi": "ilmu yang mempelajari konsep-konsep seperti kuantitas, struktur, ruang, dan perubahan, menggunakan penalaran logis, aljabar, kalkulus, dan teori.",
    "karier": "Matematikawan (Peneliti), Analis Data, Aktuaris, Analis Kuantitatif, Kriptografer"
  },
  {
    "nama": "Meteorologi & Instrumentasi",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari fenomena atmosfer, cuaca, dan iklim, serta perancangan dan penggunaan instrumen untuk pengukuran data atmosfer.",
    "karier": "Prakirawan Cuaca (BMKG), Peneliti Meteorologi, Spesialis Instrumentasi Geofisika, Konsultan Iklim"
  },
  {
    "nama": "Oseanografi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari samudra dan laut, termasuk sifat fisik dan kimia air laut, pergerakan arus, biologi laut, dan geologi dasar laut.",
    "karier": "Oseanografer (Peneliti), Konsultan Lingkungan Kelautan, Analis Data Kelautan, Staf Industri Perkapalan/Minyak & Gas"
  },
  {
    "nama": "Pariwisata",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengembangan, dan pengelolaan destinasi wisata serta pelayanan yang berkaitan dengan perjalanan dan hospitalitas.",
    "karier": "Manajer Hotel/Resort, Perencana Destinasi Wisata, Konsultan Pariwisata, Pemandu Wisata, Spesialis Pemasaran Pariwisata"
  },
  {
    "nama": "Pemanfaatan Sumberdaya Perikanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari cara-cara penangkapan, pengolahan, dan pemasaran hasil perikanan serta manajemen sumber daya ikan di perairan secara berkelanjutan.",
    "karier": "Manajer Penangkapan Ikan, Quality Control Hasil Perikanan, Konsultan Perikanan Tangkap, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Pemasaran",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari strategi untuk menciptakan, mengkomunikasikan, dan memberikan nilai kepada pelanggan serta mengelola hubungan pelanggan dengan cara yang menguntungkan.",
    "karier": "Manajer Pemasaran (Marketing Manager), Analis Pasar, Spesialis Digital Marketing, Manajer Produk (Product Manager), Konsultan Pemasaran"
  },
  {
    "nama": "Pendidikan Akuntansi",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari konsep akuntansi, auditing, dan perpajakan dengan fokus pada metodologi dan praktik pengajaran untuk profesi guru/dosen.",
    "karier": "Guru/Dosen Akuntansi, Penulis Buku Ajar, Konsultan Pendidikan, Staf Akuntansi Perusahaan"
  },
  {
    "nama": "Pendidikan Bahasa Indonesia",
    "mata_pelajaran": "Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari struktur, sastra, dan budaya Indonesia dengan fokus pada metode pengajaran yang efektif untuk menjadi seorang pendidik.",
    "karier": "Guru/Dosen Bahasa Indonesia, Penulis/Editor, Konsultan Bahasa, Penyunting Naskah"
  },
  {
    "nama": "Pendidikan Bahasa Inggris",
    "mata_pelajaran": "Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Inggris dengan fokus pada metode dan praktik pengajaran bahasa asing.",
    "karier": "Guru/Dosen Bahasa Inggris, Penerjemah, Konsultan Pendidikan, Penulis Materi Ajar"
  },
  {
    "nama": "Pendidikan Biologi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari segala aspek kehidupan dan makhluk hidup dengan fokus pada metode pengajaran dan pendidikan di tingkat sekolah.",
    "karier": "Guru/Dosen Biologi, Peneliti Pendidikan, Pengembang Kurikulum Sains, Staf Laboratorium Pendidikan"
  },
  {
    "nama": "Pendidikan Bisnis",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari konsep bisnis dan manajemen dengan fokus pada pengajaran praktik-praktik kewirausahaan dan keterampilan manajerial di sekolah/vokasi.",
    "karier": "Guru/Dosen Bisnis dan Ekonomi, Konsultan Pendidikan Vokasi, Staf Pelatihan dan Pengembangan (Training & Development) Perusahaan"
  },
  {
    "nama": "Pendidikan Ekonomi",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari teori dan prinsip ekonomi, akuntansi, dan bisnis dengan fokus pada metodologi pengajaran untuk menjadi seorang pendidik.",
    "karier": "Guru/Dosen Ekonomi, Analis Ekonomi (non-teaching), Konsultan Pendidikan, Pengembang Kurikulum"
  },
  {
    "nama": "Pendidikan Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari sifat dan interaksi materi serta energi dengan fokus pada metode pengajaran dan pendidikan Fisika.",
    "karier": "Guru/Dosen Fisika, Peneliti Pendidikan Sains, Pengembang Alat Peraga Sains, Analis Laboratorium"
  },
  {
    "nama": "Pendidikan Geografi",
    "mata_pelajaran": "Geografi",
    "deskripsi": "ilmu yang mempelajari fenomena permukaan bumi, hubungan manusia dan lingkungan, dengan fokus pada metodologi pengajaran Geografi.",
    "karier": "Guru/Dosen Geografi, Ahli Sistem Informasi Geografis (SIG), Konsultan Tata Ruang, Peneliti Wilayah"
  },
  {
    "nama": "Pendidikan Guru PAUD",
    "mata_pelajaran": "Sosiologi, Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari psikologi perkembangan anak usia dini, kurikulum, dan metode pengajaran yang sesuai untuk Pendidikan Anak Usia Dini (PAUD).",
    "karier": "Guru PAUD, Kepala Sekolah PAUD, Konsultan Parenting, Pengembang Mainan Edukasi"
  },
  {
    "nama": "Pendidikan Guru SD",
    "mata_pelajaran": "Sosiologi, Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari berbagai disiplin ilmu dasar (Matematika, Bahasa, IPA, IPS) dengan fokus pada metodologi pengajaran terpadu untuk Sekolah Dasar (SD).",
    "karier": "Guru Sekolah Dasar (SD), Kepala Sekolah SD, Pengembang Kurikulum SD, Konsultan Pendidikan Dasar"
  },
  {
    "nama": "Pendidikan Jasmani",
    "mata_pelajaran": "PJOK",
    "deskripsi": "ilmu yang mempelajari teori dan praktik pendidikan melalui aktivitas fisik, olahraga, dan kesehatan untuk membentuk karakter dan gaya hidup sehat.",
    "karier": "Guru Pendidikan Jasmani, Pelatih Olahraga, Terapis Fisik, Konsultan Kebugaran"
  },
  {
    "nama": "Pendidikan Kepelatihan Olahraga",
    "mata_pelajaran": "PJOK",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip ilmiah pelatihan olahraga, manajemen atlet, dan pengembangan program latihan untuk mencapai prestasi maksimal.",
    "karier": "Pelatih Olahraga Profesional, Analis Kinerja Atlet, Manajer Tim Olahraga, Konsultan Olahraga"
  },
  {
    "nama": "Pendidikan Kesejahteraan Keluarga",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya keluarga, gizi, tata busana, dan tata boga dengan tujuan meningkatkan kualitas dan kesejahteraan keluarga.",
    "karier": "Guru Tata Boga/Busana, Konsultan Kesejahteraan Keluarga, Wirausaha Kuliner/Fashion, Staf NGO Sosial"
  },
  {
    "nama": "Pendidikan Kimia",
    "mata_pelajaran": "Kimia",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, dan perubahan zat dengan fokus pada metode pengajaran dan pendidikan Kimia.",
    "karier": "Guru/Dosen Kimia, Peneliti Pendidikan Sains, Analis Laboratorium, Pengembang Kurikulum Kimia"
  },
  {
    "nama": "Pendidikan Luar Sekolah",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari penyelenggaraan pendidikan di luar jalur formal, seperti kursus, pelatihan, dan pemberdayaan masyarakat, untuk meningkatkan kualitas hidup.",
    "karier": "Fasilitator Pemberdayaan Masyarakat, Manajer Pelatihan (Training Manager), Konsultan Pendidikan Non-formal, Staf NGO Pendidikan"
  },
  {
    "nama": "Pendidikan Matematika",
    "mata_pelajaran": "Matematika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari konsep-konsep Matematika dengan fokus pada metodologi pengajaran yang efektif untuk tingkat sekolah.",
    "karier": "Guru/Dosen Matematika, Peneliti Pendidikan Matematika, Pengembang Kurikulum, Analis Data"
  },
  {
    "nama": "Pendidikan PKN",
    "mata_pelajaran": "Pancasila",
    "deskripsi": "ilmu yang mempelajari konsep kewarganegaraan, demokrasi, hukum, dan hak asasi manusia dengan fokus pada metodologi pengajaran Pendidikan Kewarganegaraan (PKN).",
    "karier": "Guru/Dosen PKN, Analis Kebijakan Publik, Konsultan Pendidikan, Staf Lembaga Pemerintahan"
  },
  {
    "nama": "Pendidikan Sejarah",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari peristiwa masa lalu, analisis sumber sejarah, dan interpretasi kronologis dengan fokus pada metodologi pengajaran Sejarah.",
    "karier": "Guru/Dosen Sejarah, Peneliti Sejarah, Kurator Museum, Penulis Buku Sejarah, Pemandu Wisata Sejarah"
  },
  {
    "nama": "Pendidikan Sendratari Musik",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori dan praktik seni pertunjukan (seni drama, tari, dan musik) dengan fokus pada metodologi pengajaran dan pengembangan seni di sekolah.",
    "karier": "Guru Kesenian, Koreografer, Komposer, Pengelola Sanggar Seni, Seniman Pertunjukan"
  },
  {
    "nama": "Pendidikan Seni Rupa",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, sejarah, dan praktik seni rupa (lukis, patung, grafis) dengan fokus pada metodologi pengajaran seni.",
    "karier": "Guru Seni Rupa, Seniman, Kurator Galeri, Desainer Produk, Konsultan Kreatif"
  },
  {
    "nama": "Pendidikan Tata Boga",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari prinsip dasar pengolahan makanan, gizi, dan manajemen kuliner dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Boga, Chef/Koki Profesional, Konsultan Kuliner, Wirausaha Kuliner"
  },
  {
    "nama": "Pendidikan Tata Busana",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari desain, konstruksi, dan manajemen busana (pakaian) dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Busana, Desainer Fashion, Penjahit/Modiste, Konsultan Fashion, Wirausaha Busana"
  },
  {
    "nama": "Pendidikan Tata Rias",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teknik merias wajah, rambut, dan tubuh, serta manajemen salon/spa dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Rias, Make-up Artist Profesional, Konsultan Kecantikan, Wirausaha Salon/Spa"
  },
  {
    "nama": "Pendidikan Teknik Bangunan",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip teknik sipil, konstruksi, dan perancangan bangunan dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Bangunan, Pengawas Konstruksi (non-Insinyur), Drafter Arsitektur, Konsultan Pendidikan Vokasi"
  },
  {
    "nama": "Pendidikan Teknik Elektro",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip listrik, elektronika, dan sistem kendali dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Elektro, Teknisi Elektronika, Konsultan Pelatihan Industri, Pengembang Materi Vokasi"
  },
  {
    "nama": "Pendidikan Teknik Elektronika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan dan pengaplikasian komponen dan sirkuit elektronika dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Elektronika, Teknisi Instrumentasi, Konsultan Pelatihan, Teknisi Otomasi Industri"
  },
  {
    "nama": "Pendidikan Teknik Otomotif",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari teknologi mesin, sistem kendaraan, dan perawatan otomotif dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Otomotif, Teknisi Bengkel Profesional, Konsultan Pelatihan Otomotif, Pengembang Materi Vokasi"
  },
  {
    "nama": "Pendidikan Teknologi Informasi",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari konsep dasar komputasi, pemrograman, dan jaringan dengan fokus pada metodologi pengajaran di tingkat sekolah.",
    "karier": "Guru/Dosen TIK/Informatika, Pengembang E-learning, Konsultan Teknologi Pendidikan, Staf IT Sekolah/Perusahaan"
  },
  {
    "nama": "Pendidikan Vokasional Teknik Mesin",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip mekanika, perancangan mesin, dan proses manufaktur dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Mesin, Teknisi Manufaktur, Konsultan Pelatihan Industri, Pengembang Materi Vokasi"
  },
  {
    "nama": "Perencanaan Wilayah dan Kota",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari perancangan dan penataan ruang, sumber daya, dan kegiatan di suatu wilayah atau kota untuk mencapai pembangunan yang berkelanjutan.",
    "karier": "Perencana Tata Ruang (PNS/Konsultan), Analis Kebijakan Pembangunan, Konsultan Properti, Ahli Sistem Informasi Geografis (SIG)"
  },
  {
    "nama": "Perikanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya perikanan, teknologi penangkapan, dan pengolahan hasil perikanan serta ekosistem perairan.",
    "karier": "Manajer Perikanan, Peneliti Sumber Daya Ikan, Quality Control Hasil Perikanan, Konsultan Kelautan, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari secara mendalam seluruh aspek hukum, administrasi, dan akuntansi yang berkaitan dengan pajak pusat dan daerah.",
    "karier": "Konsultan Pajak, Pegawai Direktorat Jenderal Pajak (DJP), Staf Perpajakan Perusahaan, Kuasa Hukum Pajak, Akuntan Pajak"
  },
  {
    "nama": "Peternakan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan ternak (sapi, ayam, kambing, dll.) secara ilmiah, termasuk nutrisi, reproduksi, kesehatan, dan manajemen usaha peternakan.",
    "karier": "Manajer Peternakan, Konsultan Ternak, Peneliti Produk Hewani, Quality Control Pakan, Pegawai Dinas Peternakan"
  },
  {
    "nama": "Proteksi Tanaman",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari identifikasi, pencegahan, dan pengendalian hama, penyakit, dan gulma untuk melindungi tanaman budidaya dari kerusakan dan kerugian.",
    "karier": "Ahli Hama dan Penyakit Tanaman, Konsultan Proteksi Tanaman, Peneliti Pertanian, Spesialis Quality Control Produk Pertanian, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Psikologi",
    "mata_pelajaran": "Sosiologi, Matematika",
    "deskripsi": "ilmu yang mempelajari perilaku dan proses mental manusia, termasuk pikiran, emosi, dan motivasi, melalui penelitian dan praktik klinis/industri.",
    "karier": "Psikolog Klinis/Edukasi (setelah S2), Konselor, Staf HRD/Spesialis Rekrutmen, Analis Data Perilaku, Peneliti Psikologi"
  },
  {
    "nama": "Sastra Arab",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari linguistik, sastra, dan kebudayaan yang berasal dari dunia Arab, termasuk kemampuan berbahasa dan penerjemahan.",
    "karier": "Penerjemah/Juru Bahasa Arab, Staf Kedutaan, Editor Naskah, Konsultan Budaya Timur Tengah, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Batak",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra lisan dan tulis, serta budaya etnis Batak untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Belanda",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan Belanda, termasuk sejarahnya di Indonesia, untuk keperluan terjemahan dan penelitian.",
    "karier": "Penerjemah/Juru Bahasa Belanda, Arsiparis, Peneliti Sejarah Kolonial, Staf Kedutaan Belanda"
  },
  {
    "nama": "Sastra Cina",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari linguistik, sastra, dan kebudayaan Cina (Mandarin) untuk menguasai komunikasi, terjemahan, dan pemahaman lintas budaya.",
    "karier": "Penerjemah/Juru Bahasa Mandarin, Staf Perusahaan Cina, Konsultan Bisnis Asia, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Indonesia",
    "mata_pelajaran": "Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari struktur, sastra lisan dan tulis, serta kebudayaan Indonesia untuk menghasilkan karya kreatif dan analisis kritis.",
    "karier": "Penulis/Novelis/Penyair, Editor/Penyunting Naskah, Jurnalis/Reporter, Kritikus Sastra, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Inggris",
    "mata_pelajaran": "Bahasa Inggris, Sastra Inggris",
    "deskripsi": "ilmu yang mempelajari karya-karya sastra (puisi, prosa, drama) dan sejarah sastra dari negara-negara berbahasa Inggris, serta teori-teori kritis.",
    "karier": "Penerjemah/Juru Bahasa, Penulis/Editor, Jurnalis, Analis Kebudayaan, Dosen Sastra"
  },
  {
    "nama": "Sastra Jawa",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra lisan dan tulis, serta kebudayaan Jawa untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Kurator Museum, Penulis/Editor, Konsultan Budaya Lokal, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Jepang",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Jepang untuk menguasai kemampuan komunikasi, terjemahan, dan pemahaman mendalam tentang masyarakat Jepang.",
    "karier": "Penerjemah/Juru Bahasa Jepang, Staf Perusahaan Jepang, Pemandu Wisata, Spesialis Hubungan Internasional, Staf Kedutaan"
  },
  {
    "nama": "Sastra Melayu",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan Melayu di berbagai wilayah, termasuk sejarah dan perkembangannya.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Minangkabau",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan etnis Minangkabau untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sejarah",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari, meneliti, dan menganalisis peristiwa, tokoh, dan perkembangan masa lalu untuk memahami konteks dan implikasinya di masa kini.",
    "karier": "Sejarawan (Peneliti), Arsiparis, Kurator Museum, Penulis Buku Sejarah, Jurnalis/Analis Politik"
  },
  {
    "nama": "Seni Karawitan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, praktik, dan komposisi musik gamelan (karawitan) serta instrumen tradisional Jawa, Sunda, atau Bali.",
    "karier": "Pemusik Karawitan Profesional, Komposer Musik Tradisional, Guru/Dosen Seni, Pengelola Sanggar Seni"
  },
  {
    "nama": "Seni Pertunjukkan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari proses penciptaan, produksi, dan pementasan seni drama, tari, atau musik, serta manajemen pertunjukan.",
    "karier": "Sutradara Teater/Tari, Koreografer, Seniman Pertunjukan, Manajer Produksi Seni, Kurator Seni Pertunjukan"
  },
  {
    "nama": "Seni Rupa Murni",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari penciptaan karya seni rupa (lukis, patung, grafis) dengan penekanan pada nilai estetika dan ekspresi diri, bukan fungsi terapan.",
    "karier": "Seniman Profesional, Kurator Galeri, Kritikus Seni, Dosen Seni, Konsultan Seni"
  },
  {
    "nama": "Seni Tari",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, sejarah, dan praktik tari (tradisional dan kontemporer) serta proses penciptaan karya tari (koreografi).",
    "karier": "Koreografer, Penari Profesional, Guru/Dosen Tari, Pengelola Sanggar Tari, Seniman Pertunjukan"
  },
  {
    "nama": "Seni Teater",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari seni peran, penyutradaraan, penulisan naskah, dan manajemen produksi pementasan drama atau teater.",
    "karier": "Aktor/Aktris, Sutradara Teater, Penulis Naskah Drama, Manajer Produksi Seni, Guru/Dosen Seni Pertunjukan"
  },
  {
    "nama": "Sistem Informasi",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan pengelolaan sistem berbasis komputer untuk mendukung operasional dan pengambilan keputusan bisnis.",
    "karier": "System Analyst, Konsultan ERP, Manajer Proyek IT, Data Analyst, Spesialis Keamanan Informasi"
  },
  {
    "nama": "Sosiologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari masyarakat, interaksi sosial, perilaku kelompok, serta struktur dan perubahan sosial yang terjadi di dalamnya.",
    "karier": "Sosiolog/Peneliti Sosial, Analis Pasar dan Konsumen, Konsultan Pembangunan Masyarakat, Staf NGO/LSM, Analis Kebijakan Sosial"
  },
  {
    "nama": "Statistika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari pengumpulan data, analisis, interpretasi, dan presentasi data secara kuantitatif untuk menarik kesimpulan dan membuat prediksi.",
    "karier": "Statistikawan, Data Scientist, Analis Bisnis/Pasar, Analis Risiko, Peneliti Biostatistika"
  },
  {
    "nama": "Tata Rias dan Kecantikan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teknik merias wajah, rambut, dan tubuh, serta pengelolaan salon/spa dengan fokus pada layanan kecantikan dan estetika.",
    "karier": "Make-up Artist Profesional, Konsultan Kecantikan, Terapis Kecantikan, Wirausaha Salon/Spa, Guru Tata Rias"
  },
  {
    "nama": "Teknik Elektro",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan dan aplikasi sistem yang berkaitan dengan listrik, elektronika, elektromagnetisme, dan sistem kendali.",
    "karier": "Insinyur Elektronika, Insinyur Sistem Tenaga Listrik, Spesialis Otomasi Industri, Konsultan Energi, Peneliti Teknologi Listrik"
  },
  {
    "nama": "Teknik Elektronika",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan pengaplikasian komponen dan sirkuit elektronika untuk sistem komunikasi, kontrol, dan instrumentasi.",
    "karier": "Insinyur Elektronika, Perancang Sistem Embedded, Teknisi Instrumentasi, Spesialis Telekomunikasi, Insinyur Otomasi"
  },
  {
    "nama": "Teknik Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip fisika pada pengembangan teknologi dan instrumentasi di berbagai bidang industri dan rekayasa.",
    "karier": "Insinyur Instrumentasi, Analis Sistem Energi, Konsultan Akustik/Optik, Peneliti Material, Insinyur Quality Control"
  },
  {
    "nama": "Teknik Geofisika",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari struktur, komposisi, dan proses yang terjadi di bawah permukaan bumi menggunakan prinsip-prinsip fisika untuk eksplorasi sumber daya alam.",
    "karier": "Geofisikawan Eksplorasi (Minyak & Gas, Panas Bumi), Analis Bencana Alam, Konsultan Lingkungan, Peneliti Geofisika"
  },
  {
    "nama": "Teknik Geologi",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, dan sejarah bumi, termasuk proses pembentukan batuan, mineral, dan potensi sumber daya geologi.",
    "karier": "Geolog Eksplorasi (Pertambangan/Minyak & Gas), Hidrogeolog, Konsultan Geoteknik, Analis Mitigasi Bencana Geologi"
  },
  {
    "nama": "Teknik Industri",
    "mata_pelajaran": "Fisika, Kimia, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, perbaikan, dan instalasi sistem terintegrasi (manusia, material, informasi, peralatan, dan energi) untuk mengoptimalkan proses produksi dan operasional.",
    "karier": "Manajer Operasional, Konsultan Manajemen, Analis Rantai Pasok (Supply Chain), Spesialis Quality Control/QA, Analis Ergonomi"
  },
  {
    "nama": "Teknik Informatika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip dan praktik perancangan serta pengembangan sistem perangkat lunak, termasuk pemrograman, jaringan, dan keamanan informasi.",
    "karier": "Software Engineer, Network Engineer, Analis Keamanan Siber, Data Scientist, Konsultan IT"
  },
  {
    "nama": "Teknik Kimia",
    "mata_pelajaran": "Fisika, Kimia",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip kimia, fisika, dan matematika untuk merancang, mengoperasikan, dan mengelola proses konversi bahan baku menjadi produk kimia yang bernilai.",
    "karier": "Insinyur Proses (Pabrik Kimia, Minyak & Gas), Peneliti Produk Baru, Spesialis Keselamatan Proses, Konsultan Lingkungan"
  },
  {
    "nama": "Teknik Komputer",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang menggabungkan prinsip teknik elektro dan ilmu komputer untuk merancang dan mengembangkan sistem perangkat keras (hardware) dan perangkat lunak (software).",
    "karier": "Insinyur Perangkat Keras, Insinyur Sistem Tertanam (Embedded Systems), Pengembang Robotika, Analis Jaringan Komputer"
  },
  {
    "nama": "Teknik Lingkungan",
    "mata_pelajaran": "Fisika, Biologi",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip sains dan rekayasa untuk mencegah dan menyelesaikan masalah lingkungan, seperti polusi air, udara, dan pengelolaan limbah.",
    "karier": "Insinyur Lingkungan, Konsultan Amdal, Spesialis Pengelolaan Limbah, Auditor Lingkungan, Pegawai Kementerian Lingkungan Hidup"
  },
  {
    "nama": "Teknik Listrik",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari pembangkitan, transmisi, distribusi, dan pemanfaatan energi listrik, termasuk perancangan sistem instalasi listrik.",
    "karier": "Insinyur Listrik, Teknisi Jaringan Tenaga Listrik, Spesialis Otomasi Bangunan, Konsultan Instalasi Listrik"
  },
  {
    "nama": "Teknik Logistik",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, implementasi, dan pengendalian aliran barang, jasa, dan informasi dari titik asal hingga titik konsumsi secara efisien dan efektif.",
    "karier": "Manajer Logistik, Analis Rantai Pasok (Supply Chain), Manajer Gudang, Konsultan Logistik, Staf Perusahaan Ekspedisi"
  },
  {
    "nama": "Teknik Material",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari struktur, sifat, kinerja, dan pemrosesan berbagai jenis material (logam, polimer, keramik) serta pengembangan material baru.",
    "karier": "Insinyur Material, Peneliti Material, Spesialis Quality Control Logam/Polimer, Konsultan Material Industri"
  },
  {
    "nama": "Teknik Mesin",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, analisis, manufaktur, dan pemeliharaan sistem mekanik, mulai dari mesin sederhana hingga kompleks.",
    "karier": "Insinyur Perancangan Mesin, Insinyur Manufaktur, Manajer Pemeliharaan (Maintenance), Konsultan Mekanikal, Insinyur Otomotif"
  },
  {
    "nama": "Teknik Perkapalan",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan, pembangunan, perbaikan, dan pemeliharaan kapal dan struktur apung lainnya, termasuk sistem propulsi dan stabilitas.",
    "karier": "Insinyur Perancangan Kapal, Manajer Produksi Galangan Kapal, Spesialis Klasifikasi Kapal, Konsultan Maritim"
  },
  {
    "nama": "Teknik Pertambangan",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari eksplorasi, penambangan, pengolahan, dan pemasaran sumber daya mineral secara aman dan efisien, serta rekayasa lingkungan pasca-tambang.",
    "karier": "Insinyur Tambang, Geolog Pertambangan, Spesialis Keselamatan Tambang, Konsultan Lingkungan, Peneliti Mineral"
  },
  {
    "nama": "Teknik Pertanian",
    "mata_pelajaran": "Fisika, Biologi",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip rekayasa dan teknologi pada sistem pertanian untuk meningkatkan efisiensi dan hasil produksi, seperti irigasi, alat mesin pertanian, dan pascapanen.",
    "karier": "Insinyur Pertanian, Manajer Alat Mesin Pertanian, Konsultan Irigasi, Pengembang Teknologi Pertanian, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Teknik Sipil",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pembangunan, dan pemeliharaan infrastruktur seperti gedung, jalan, jembatan, bendungan, dan sistem transportasi.",
    "karier": "Insinyur Sipil Perancangan Struktur, Manajer Proyek Konstruksi, Konsultan Geoteknik, Pengawas Lapangan, Perencana Infrastruktur"
  },
  {
    "nama": "Teknologi Hasil Pertanian",
    "mata_pelajaran": "Kimia, Biologi",
    "deskripsi": "ilmu yang mempelajari tentang pengolahan, pengawetan, dan peningkatan nilai tambah produk-produk hasil pertanian (pangan maupun non-pangan) dengan menerapkan prinsip-prinsip kimia, biokimia, bioteknologi, dan rekayasa proses untuk menghasilkan produk yang aman, bermutu, dan bergizi.",
    "karier": "Manajer Produksi Industri Pangan, Quality Control (QC), Research and Development (R&D), Konsultan Pangan/Pertanian, Pegawai BPOM, Wirausaha Bidang Pangan, Lembaga Penelitian"
  },
    {"nama": "Administrasi Bisnis",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari seluruh proses pengelolaan perusahaan atau organisasi secara komprehensif, mulai dari perencanaan, pengorganisasian, pemasaran, sumber daya manusia, hingga keuangan untuk mencapai tujuan bisnis dan mendorong pertumbuhan.",
    "karier": "Spesialis Pemasaran, Manajer Operasional, Analis Bisnis, Konsultan Manajemen, Staf Sumber Daya Manusia (HRD)"
  },
  {
    "nama": "Administrasi Fiskal",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan keuangan publik (pemerintah) dan perpajakan. Fokusnya pada perencanaan anggaran negara, sistem perpajakan, serta analisis kebijakan fiskal dan keuangan.",
    "karier": "Analis Anggaran, Konsultan Pajak, Auditor Pajak, Akuntan Pajak, Pegawai Direktorat Jenderal Pajak (DJP)"
  },
  {
    "nama": "Administrasi Negara",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manajemen dan implementasi kebijakan publik serta penyelenggaraan pemerintahan di lembaga eksekutif, legislatif, dan yudikatif untuk memberikan pelayanan publik yang efisien dan akuntabel.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Manajer Layanan Publik, Konsultan Pemerintahan, Peneliti"
  },
  {
    "nama": "Administrasi Niaga",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang strategi pengelolaan dan pengorganisasian seluruh aktivitas bisnis dan niaga, termasuk pemasaran, keuangan, produksi, dan sumber daya manusia, untuk menciptakan keuntungan dan keunggulan kompetitif.",
    "karier": "Staf Pemasaran, Manajer Penjualan, Business Development, Staf HRD, Wirausaha (Entrepreneur)"
  },
  {
    "nama": "Administrasi Pendidikan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip manajemen, perencanaan, pengorganisasian, dan evaluasi untuk mengelola lembaga pendidikan secara efektif dan efisien.",
    "karier": "Pelaksana Tata Kelola Satuan Pendidikan, Analis Perencanaan Pendidikan, Staf Administrasi Kementerian Pendidikan, Konsultan Pendidikan, Direktur Lembaga Kependidikan"
  },
  {
    "nama": "Administrasi Perkantoran",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengetahuan dan keterampilan dalam mengelola pekerjaan dan operasional perkantoran, termasuk manajemen kearsipan, teknologi informasi perkantoran, dan pelayanan prima (kesekretariatan).",
    "karier": "Staf Administrasi, Sekretaris, Asisten Manajer, Pegawai Bank, Staf Personalia/HRD"
  },
  {
    "nama": "Administrasi Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang perhitungan, pemungutan, pelaporan, dan sistem administrasi berbagai jenis pajak (Pusat dan Daerah) serta hak dan kewajiban wajib pajak.",
    "karier": "Konsultan Pajak, Pegawai Direktorat Jenderal Pajak (DJP), Staf Perpajakan Perusahaan, Kuasa Hukum Pajak, Akuntan"
  },
  {
    "nama": "Administrasi Publik",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya dan implementasi kebijakan di sektor publik (pemerintahan) untuk memberikan pelayanan dan tata kelola yang baik (good governance) kepada masyarakat.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Manajer Program LSM/NGO, Konsultan Pemerintahan, Pegawai BUMN"
  },
  {
    "nama": "Agribisnis",
    "mata_pelajaran": "Biologi, Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan usaha (bisnis) di bidang pertanian dan pangan secara terpadu, mulai dari pra-produksi, produksi, pascapanen, hingga pemasaran hasil pertanian.",
    "karier": "Manajer Agribisnis, Konsultan Pertanian, Pengembang Produk Pertanian, Analis Pasar Komoditas, Wirausaha Pertanian"
  },
  {
    "nama": "Agroekoteknologi",
    "mata_pelajaran": "Biologi, Fisika",
    "deskripsi": "ilmu yang mempelajari penerapan teknologi dan prinsip ekologi dalam sistem budidaya pertanian untuk menghasilkan produk yang berkualitas sambil menjaga kelestarian lingkungan.",
    "karier": "Agronom, Peneliti Pertanian, Manajer Lahan dan Tanaman, Konsultan Pertanian Berkelanjutan, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Agronomi dan Holtikultura",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari tentang pengelolaan tanaman pangan, perkebunan, dan holtikultura (buah, sayur, dan bunga) secara efisien dan berkelanjutan untuk meningkatkan hasil dan kualitas produksi.",
    "karier": "Agronom, Manajer Kebun/Lahan, Peneliti Tanaman, Konsultan Holtikultura, Wirausaha Pertanian"
  },
  {
    "nama": "Agroteknologi",
    "mata_pelajaran": "Biologi, Fisika",
    "deskripsi": "ilmu yang mempelajari penerapan teknologi, rekayasa, dan mekanisasi untuk mengoptimalkan produksi tanaman dan manajemen sumber daya pertanian secara efisien dan modern.",
    "karier": "Insinyur Pertanian, Pengembang Teknologi Pertanian, Manajer Proyek Pertanian Modern, Peneliti Agroteknologi, Konsultan Pertanian"
  },
  {
    "nama": "Akademi Militer",
    "mata_pelajaran": "Biologi, Kimia, Fisika",
    "deskripsi": "Institusi pendidikan kedinasan yang mendidik dan melatih calon perwira Tentara Nasional Indonesia (TNI) Angkatan Darat, fokus pada ilmu kepemimpinan, strategi militer, dan pengetahuan umum serta teknik militer.",
    "karier": "Perwira TNI Angkatan Darat"
  },
  {
    "nama": "Aktuaria",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang menerapkan teori matematika, probabilitas, dan statistika untuk menganalisis risiko keuangan di industri asuransi, dana pensiun, dan investasi.",
    "karier": "Aktuaris, Analis Risiko, Manajer Risiko, Konsultan Asuransi, Analis Investasi"
  },
  {
    "nama": "Akuakultur",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari budidaya organisme air (ikan, udang, kerang, rumput laut) secara terkontrol, mulai dari pembenihan, pembesaran, hingga pengelolaan kualitas air dan pencegahan penyakit.",
    "karier": "Pembudidaya Perikanan, Manajer Produksi Tambak/Kolam, Peneliti Akuakultur, Konsultan Perikanan, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Akuntansi",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari proses pencatatan, pengklasifikasian, pengolahan, dan penyajian data transaksi keuangan untuk menghasilkan informasi yang relevan dalam pengambilan keputusan bisnis.",
    "karier": "Akuntan Publik, Akuntan Manajemen, Auditor, Konsultan Keuangan, Analis Keuangan"
  },
  {
    "nama": "Akuntansi Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari pencatatan dan pelaporan transaksi keuangan dengan fokus pada kepatuhan terhadap peraturan perpajakan, baik untuk pelaporan internal maupun eksternal (pemerintah).",
    "karier": "Akuntan Pajak, Konsultan Pajak, Staf Perpajakan Perusahaan, Auditor Pajak"
  },
  {
    "nama": "Analis Farmasi dan Makanan",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari analisis bahan farmasi dan makanan termasuk kualitas, keamanan, dan standar produksi serta pengujian laboratorium untuk memastikan produk aman dan memenuhi regulasi.",
    "karier": "Analis Laboratorium, Quality Control (QC), Quality Assurance (QA), Peneliti Kualitas Pangan, Pengawas Obat dan Makanan (BPOM)"
  },
  {
    "nama": "Animasi",
    "mata_pelajaran": "Seni Budaya, Matematika",
    "deskripsi": "ilmu yang mempelajari proses pembuatan gambar bergerak (animasi) menggunakan berbagai teknik (2D, 3D, stop motion), termasuk konsep cerita, desain karakter, hingga produksi akhir.",
    "karier": "Animator 2D/3D, Storyboard Artist, Concept Artist, Sutradara Animasi, Desainer Karakter"
  },
  {
    "nama": "Antropologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari manusia secara holistik dari aspek budaya, masyarakat, bahasa, dan biologi di berbagai penjuru dunia dari masa lalu hingga kini.",
    "karier": "Peneliti Sosial, Etnografer, Konsultan Budaya, Analis Data Sosial, Pegawai Lembaga Kebudayaan"
  },
  {
    "nama": "Arkeologi",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari kebudayaan masa lalu manusia melalui penelitian sistematis terhadap tinggalan-tinggalan (artefak, situs, monumen) yang dapat digali dan dianalisis.",
    "karier": "Arkeolog, Kurator Museum, Peneliti Sejarah dan Purbakala, Konsultan Peninggalan Budaya"
  },
  {
    "nama": "Arsitektur",
    "mata_pelajaran": "Matematika, Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan dan pembangunan struktur bangunan, baik dari segi fungsi, estetika, konstruksi, maupun aspek lingkungan, dengan menitikberatkan pada ruang dan bentuk.",
    "karier": "Arsitek Perancang, Konsultan Konstruksi, Pengembang Properti, Pengawas Lapangan, Desainer Interior"
  },
  {
    "nama": "Arsitektur Lansekap",
    "mata_pelajaran": "Matematika, Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan, perencanaan, dan pengelolaan ruang terbuka (outdoor) dan lingkungan binaan (taman, kota, kawasan) dengan mempertimbangkan aspek ekologi, sosial, dan estetika.",
    "karier": "Arsitek Lansekap, Desainer Taman Kota, Perencana Wilayah, Konsultan Lingkungan, Pengembang Properti"
  },
  {
    "nama": "Astronomi",
    "mata_pelajaran": "Matematika Tingkat Lanjut, Fisika",
    "deskripsi": "ilmu yang mempelajari benda-benda langit, fenomena alam di luar atmosfer bumi, asal-usul alam semesta, dan hukum-hukum fisika yang mengaturnya.",
    "karier": "Astronom/Peneliti Observatorium, Dosen/Pendidik, Analis Data Sains, Spesialis Penginderaan Jauh"
  },
  {
    "nama": "Bahasa Inggris",
    "mata_pelajaran": "Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari struktur bahasa (linguistik), sastra, dan budaya masyarakat penutur Bahasa Inggris untuk menguasai kemampuan komunikasi, analisis, dan pemahaman lintas budaya.",
    "karier": "Penerjemah/Juru Bahasa, Penulis/Editor, Spesialis Komunikasi Internasional, Staf Kedutaan, Pengajar Bahasa"
  },
  {
    "nama": "Bahasa Jepang",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Jepang untuk menguasai kemampuan komunikasi, terjemahan, dan pemahaman mendalam tentang masyarakat Jepang.",
    "karier": "Penerjemah/Juru Bahasa Jepang, Staf Perusahaan Jepang, Pemandu Wisata, Spesialis Hubungan Internasional, Staf Kedutaan"
  },
  {
    "nama": "Bimbingan & Konseling",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari teori dan praktik membantu individu mengembangkan potensi diri, mengatasi masalah psikologis, sosial, dan karier, serta membuat keputusan yang tepat.",
    "karier": "Guru Bimbingan dan Konseling (BK), Konselor Karier, Konselor Pendidikan, Terapis, Staf Sumber Daya Manusia"
  },
  {
    "nama": "Biokimia",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari proses kimia yang terjadi di dalam organisme hidup, termasuk struktur dan fungsi biomolekul (protein, karbohidrat, lemak, asam nukleat) serta metabolisme.",
    "karier": "Peneliti Biokimia, Analis Laboratorium Klinis, Spesialis Quality Control Farmasi, Teknolog Pangan, Pengembang Produk Bioteknologi"
  },
  {
    "nama": "Biologi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari segala aspek kehidupan dan makhluk hidup, mulai dari struktur sel, fungsi organ, interaksi antar organisme, hingga evolusi dan lingkungan.",
    "karier": "Peneliti Biologi, Staf Konservasi Lingkungan, Analis Laboratorium, Teknisi Bioteknologi, Pengembang Produk Farmasi"
  },
  {
    "nama": "Bisnis Digital",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari strategi bisnis, pemasaran, dan manajemen operasional yang memanfaatkan teknologi digital dan platform online (e-commerce, media sosial, big data).",
    "karier": "Manajer Pemasaran Digital, Analis Data Bisnis, Spesialis E-Commerce, Konsultan Teknologi Bisnis, Wirausaha Digital"
  },
  {
    "nama": "Bisnis Islam/Syariah",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip dan praktik bisnis, manajemen, serta keuangan yang sesuai dengan nilai-nilai dan hukum syariah (Islam).",
    "karier": "Manajer Keuangan Syariah, Spesialis Pemasaran Halal, Konsultan Bisnis Islam, Auditor Syariah, Wirausaha"
  },
  {
    "nama": "Bisnis Kreatif",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari tentang pengembangan dan pengelolaan usaha yang berbasis pada ide, kreativitas, dan kekayaan intelektual (misalnya di bidang seni, desain, media, dan teknologi).",
    "karier": "Manajer Proyek Kreatif, Konsultan Bisnis Kreatif, Desainer Produk, Spesialis Pemasaran Konten, Wirausaha Industri Kreatif"
  },
  {
    "nama": "Budidaya Perairan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari teknik-teknik pengembangan, pemeliharaan, dan panen organisme air (ikan, udang, kerang) dengan fokus pada efisiensi, kualitas, dan keberlanjutan.",
    "karier": "Manajer Budidaya Perairan, Peneliti Kelautan, Quality Control Hasil Perikanan, Konsultan Akuakultur, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Budidaya Peternakan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen dan teknik pemeliharaan ternak (sapi, ayam, kambing, dll.) mulai dari bibit, pakan, kesehatan, hingga pengolahan hasil ternak.",
    "karier": "Manajer Peternakan, Konsultan Ternak, Peneliti Pakan Ternak, Quality Control Produk Hewani, Pegawai Dinas Peternakan"
  },
  {
    "nama": "Desain Komunikasi Visual",
    "mata_pelajaran": "Seni Budaya, Matematika",
    "deskripsi": "ilmu yang mempelajari penyampaian pesan atau informasi melalui media visual (gambar, tipografi, video) untuk tujuan pemasaran, edukasi, atau seni.",
    "karier": "Desainer Grafis, Illustrator, Creative Director, UI/UX Designer, Motion Graphic Artist"
  },
  {
    "nama": "Ekonomi Islam/Syariah",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari prinsip, sistem, dan mekanisme ekonomi serta keuangan yang berlandaskan pada ajaran dan etika Islam.",
    "karier": "Analis Keuangan Syariah, Manajer Bank Syariah, Auditor Syariah, Konsultan Keuangan Islam, Dosen Ekonomi Syariah"
  },
  {
    "nama": "Ekonomi Pembangunan",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari isu-isu pembangunan ekonomi di suatu wilayah atau negara, termasuk perencanaan, kebijakan, pertumbuhan ekonomi, dan kesejahteraan masyarakat.",
    "karier": "Analis Ekonomi, Perencana Pembangunan Daerah (Bappeda), Konsultan Pembangunan, Peneliti Ekonomi, Staf Lembaga Keuangan Internasional"
  },
  {
    "nama": "Ekonomi Sumberdaya & Lingkungan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari hubungan antara aktivitas ekonomi, pengelolaan sumber daya alam, dan pelestarian lingkungan, termasuk analisis kebijakan lingkungan.",
    "karier": "Analis Kebijakan Lingkungan, Konsultan Amdal/EIA, Staf Konservasi, Peneliti Ekonomi Sumber Daya, Pegawai Kementerian Lingkungan Hidup"
  },
  {
    "nama": "Ekowisata",
    "mata_pelajaran": "Biologi, Ekonomi",
    "deskripsi": "ilmu yang mempelajari pengelolaan wisata alam yang bertanggung jawab, berfokus pada konservasi lingkungan, pemberdayaan masyarakat lokal, dan edukasi.",
    "karier": "Manajer Ekowisata, Konsultan Pariwisata Berkelanjutan, Pemandu Wisata Alam, Pegawai Dinas Pariwisata, Wirausaha Tour & Travel"
  },
  {
    "nama": "Etnomusikologi",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari musik dalam konteks budaya dan sosial masyarakat, meliputi asal-usul, fungsi, sejarah, dan struktur musik tradisional.",
    "karier": "Peneliti Musik, Kurator Seni Musik, Konsultan Budaya, Komposer, Pengajar Musik Tradisional"
  },
  {
    "nama": "Farmasi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari identifikasi, pengembangan, pembuatan, formulasi, pengujian, dan distribusi obat, serta konseling penggunaan obat yang aman dan efektif.",
    "karier": "Apoteker (di Apotek/Rumah Sakit), Peneliti Obat (R&D), Quality Control/Assurance Farmasi, Staf Produksi Obat, Konsultan Farmasi Klinis"
  },
  {
    "nama": "Filsafat",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari hakikat segala sesuatu dengan menggunakan akal budi untuk mencari kebenaran, mulai dari logika, etika, estetika, hingga metafisika.",
    "karier": "Peneliti/Akademisi, Konsultan Etika Bisnis, Penulis/Editor, Analis Kebijakan, Jurnalis"
  },
  {
    "nama": "Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari sifat dan interaksi materi serta energi dalam ruang dan waktu, termasuk hukum-hukum fundamental alam semesta.",
    "karier": "Fisikawan (Peneliti), Analis Data, Spesialis Instrumentasi, Ahli Metrologi, Dosen/Pendidik"
  },
  {
    "nama": "Gizi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari hubungan antara makanan dan kesehatan, termasuk komposisi gizi, perencanaan menu, dan penanganan masalah gizi individu maupun publik.",
    "karier": "Ahli Gizi (Dietisien) di Rumah Sakit, Konsultan Gizi Masyarakat, Quality Control Pangan, Product Developer Makanan, Tenaga Penyuluh Kesehatan"
  },
  {
    "nama": "Hubungan Internasional",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari interaksi antar negara, aktor non-negara (organisasi internasional, NGO), diplomasi, politik global, dan isu-isu lintas batas.",
    "karier": "Diplomat, Analis Politik Internasional, Staf Organisasi Internasional (PBB, ASEAN), Konsultan Global, Jurnalis Internasional"
  },
  {
    "nama": "Ilmu Biomedis",
    "mata_pelajaran": "Biologi, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari dasar-dasar biologi dan kimia tubuh manusia dalam kaitannya dengan penyakit, termasuk pengembangan teknologi untuk diagnosis dan terapi.",
    "karier": "Peneliti Biomedis, Spesialis Laboratorium Medis, Pengembang Alat Kesehatan, Staf Industri Farmasi/Bioteknologi"
  },
  {
    "nama": "Ilmu Hukum",
    "mata_pelajaran": "Sosiologi, Pancasila",
    "deskripsi": "ilmu yang mempelajari sistem peraturan (hukum) yang berlaku, yurisprudensi, dan proses peradilan untuk menciptakan ketertiban dan keadilan dalam masyarakat.",
    "karier": "Pengacara/Advokat, Notaris, Jaksa, Hakim, Legal Officer Perusahaan, Konsultan Hukum"
  },
  {
    "nama": "Ilmu Kelautan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari ekosistem laut, oseanografi, sumber daya hayati laut, hingga teknologi eksplorasi dan pemanfaatan kekayaan laut secara berkelanjutan.",
    "karier": "Peneliti Kelautan, Konsultan Lingkungan Pesisir, Manajer Kawasan Konservasi Laut, Staf Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Ilmu Keolahragaan",
    "mata_pelajaran": "PJOK, Biologi",
    "deskripsi": "ilmu yang mempelajari aspek ilmiah dari aktivitas fisik, olahraga, dan kesehatan, termasuk biomekanika, fisiologi olahraga, dan psikologi olahraga.",
    "karier": "Fisioterapis Olahraga, Pelatih Fisik (Strength and Conditioning Coach), Manajer Klub Olahraga, Konsultan Kebugaran"
  },
  {
    "nama": "Ilmu Komputer",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari teori komputasi, perancangan perangkat keras (hardware), dan pengembangan perangkat lunak (software) serta algoritma.",
    "karier": "Software Developer, Data Scientist, System Analyst, Konsultan IT, Peneliti Komputasi"
  },
  {
    "nama": "Ilmu Komunikasi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari proses penyampaian pesan dari komunikator kepada komunikan, termasuk media massa, komunikasi interpersonal, dan komunikasi strategis (PR & Marketing).",
    "karier": "Spesialis Hubungan Masyarakat (PR), Jurnalis/Reporter, Content Creator, Manajer Media Sosial, Konsultan Komunikasi Pemasaran"
  },
  {
    "nama": "Ilmu Pemerintahan",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari struktur, fungsi, dan dinamika lembaga pemerintahan, proses kebijakan publik, dan hubungan antara pemerintah dengan masyarakat dan lembaga lainnya.",
    "karier": "Aparat Pemerintah (PNS), Analis Kebijakan Publik, Staf Legislatif, Peneliti Pemerintahan, Konsultan Politik"
  },
  {
    "nama": "Ilmu Perpustakaan",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari manajemen informasi, sistem pengorganisasian pengetahuan, teknologi perpustakaan, dan pelayanan informasi kepada pengguna.",
    "karier": "Pustakawan, Pengelola Arsip Digital, Kurator Informasi, Konsultan Informasi, Staf Database Perusahaan"
  },
  {
    "nama": "Ilmu Politik",
    "mata_pelajaran": "Sosiologi, Pancasila",
    "deskripsi": "ilmu yang mempelajari teori dan praktik politik, sistem pemerintahan, perilaku politik, serta kekuasaan dan pengambilan keputusan dalam negara.",
    "karier": "Analis Politik, Staf Legislatif/Parlemen, Konsultan Kampanye Politik, Jurnalis Politik, Pegawai Kementerian Luar Negeri"
  },
  {
    "nama": "Ilmu Tanah",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari sifat, genesis, klasifikasi, survei, dan pemetaan tanah serta manajemen kesuburan tanah untuk pertanian dan lingkungan.",
    "karier": "Ahli Konservasi Tanah, Peneliti Tanah, Analis Laboratorium Tanah, Konsultan Pertanian, Pegawai Dinas Pertanian/Lingkungan"
  },
  {
    "nama": "Informatika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan penerapan sistem komputasi untuk mengolah dan menganalisis informasi secara efisien.",
    "karier": "Software Engineer, Data Scientist, Pengembang Aplikasi Mobile, Konsultan IT, Analis Keamanan Siber"
  },
  {
    "nama": "IPDN",
    "mata_pelajaran": "Matematika, Bahasa Indonesia, Fisika, Sejarah",
    "deskripsi": "Institusi pendidikan kedinasan yang mendidik calon Aparatur Sipil Negara (ASN) yang berorientasi pada bidang kepamongprajaan, manajemen pemerintahan, dan administrasi publik, dengan sistem pendidikan berasrama dan disiplin tinggi.",
    "karier": "Aparatur Sipil Negara (ASN) di Pemerintah Pusat dan Daerah (Kementerian Dalam Negeri, Pemerintah Provinsi/Kabupaten/Kota)"
  },
  {
    "nama": "K3 (Kesehatan dan Keselamatan Kerja)",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari identifikasi, evaluasi, dan pengendalian risiko bahaya di tempat kerja untuk mencegah kecelakaan, penyakit akibat kerja, dan meningkatkan kesehatan pekerja.",
    "karier": "Petugas K3 (Safety Officer), Auditor K3, Konsultan K3, Spesialis Higiene Industri, Manajer Lingkungan, Kesehatan, dan Keselamatan (EHS)"
  },
  {
    "nama": "Kebidanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pelayanan kesehatan reproduksi perempuan, mulai dari masa kehamilan, persalinan, nifas, bayi baru lahir, hingga kesehatan seksual.",
    "karier": "Bidan Praktik Mandiri, Bidan Rumah Sakit/Puskesmas, Konsultan Kesehatan Ibu dan Anak, Pengajar Kebidanan"
  },
  {
    "nama": "Kedokteran",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari diagnosis, pengobatan, dan pencegahan penyakit serta peningkatan kesehatan manusia secara komprehensif.",
    "karier": "Dokter Umum, Dokter Spesialis, Peneliti Kesehatan, Staf Medis Lembaga Internasional, Dosen Kedokteran"
  },
  {
    "nama": "Kedokteran Gigi",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari kesehatan gigi dan mulut, termasuk diagnosis, pengobatan, pencegahan masalah, dan estetika rongga mulut.",
    "karier": "Dokter Gigi Umum, Dokter Gigi Spesialis (Ortodonti, Bedah Mulut), Peneliti Kesehatan Gigi, Staf Industri Alat Kesehatan"
  },
  {
    "nama": "Kedokteran Hewan",
    "mata_pelajaran": "Biologi, Kimia",
    "deskripsi": "ilmu yang mempelajari pencegahan, diagnosis, dan pengobatan penyakit pada hewan, serta memastikan keamanan pangan asal hewan (Zoo Health dan Public Health).",
    "karier": "Dokter Hewan Praktisi, Dokter Hewan Karantina, Peneliti Hewan, Quality Control Produk Hewani, Staf Industri Pakan Ternak"
  },
  {
    "nama": "Kehutanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan, pelestarian, dan pemanfaatan sumber daya hutan secara berkelanjutan, termasuk konservasi ekosistem dan hasil hutan.",
    "karier": "Rimbawan/Manajer Hutan, Konsultan Konservasi, Analis Kebijakan Kehutanan, Peneliti Kehutanan, Pegawai Kementerian Lingkungan Hidup dan Kehutanan"
  },
  {
    "nama": "Keperawatan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari asuhan keperawatan, perawatan, dan pemulihan kesehatan individu, keluarga, dan masyarakat dengan fokus pada kebutuhan holistik pasien.",
    "karier": "Perawat Klinis (Rumah Sakit/Puskesmas), Perawat Homecare, Perawat Kesehatan Komunitas, Dosen Keperawatan, Manajer Pelayanan Kesehatan"
  },
  {
    "nama": "Kesehatan Masyarakat",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari upaya pencegahan penyakit dan peningkatan kesehatan populasi melalui intervensi, kebijakan, promosi kesehatan, dan manajemen kesehatan lingkungan.",
    "karier": "Epidemiolog, Manajer Administrasi Rumah Sakit, Spesialis Promosi Kesehatan, Analis Kebijakan Kesehatan, Konsultan Kesehatan Lingkungan"
  },
  {
    "nama": "Kesejahteraan Sosial",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari upaya membantu individu, keluarga, dan kelompok masyarakat untuk meningkatkan kemampuan fungsional dan kesejahteraan sosialnya.",
    "karier": "Pekerja Sosial, Konselor Sosial, Fasilitator Pemberdayaan Masyarakat, Analis Kebijakan Sosial, Staf NGO/LSM"
  },
  {
    "nama": "Kewirausahaan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari proses penciptaan dan pengelolaan bisnis baru, termasuk identifikasi peluang, pengembangan ide, manajemen risiko, dan strategi pertumbuhan.",
    "karier": "Wirausaha (Entrepreneur), Konsultan Bisnis Startup, Manajer Inovasi Perusahaan, Business Development, Analis Pasar"
  },
  {
    "nama": "Kimia",
    "mata_pelajaran": "Kimia",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, sifat, dan perubahan zat, serta interaksi materi dan energi pada tingkat molekuler dan atom.",
    "karier": "Kimiawan (Peneliti), Analis Laboratorium (Industri/Klinis), Quality Control Industri, Pengembang Produk Kimia, Dosen/Pendidik"
  },
  {
    "nama": "Konservasi Sumberdaya Hutan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan, perlindungan, dan pemulihan sumber daya alam hutan, termasuk flora dan fauna, untuk menjamin kelestariannya.",
    "karier": "Spesialis Konservasi Alam, Manajer Kawasan Konservasi, Peneliti Kehutanan/Lingkungan, Konsultan Amdal, Pegawai Kementerian Kehutanan"
  },
  {
    "nama": "Kriminologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari sebab-sebab terjadinya kejahatan, pelaku kriminal, respons masyarakat terhadap kejahatan, dan sistem peradilan pidana.",
    "karier": "Analis Kriminalitas, Peneliti Kriminologi, Konsultan Keamanan, Staf Lembaga Pemasyarakatan, Pegawai Kepolisian/BNN"
  },
  {
    "nama": "Kriya Seni",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari penciptaan benda-benda seni terapan (kerajinan) yang memiliki fungsi praktis dan nilai estetika, menggunakan berbagai media (tekstil, keramik, kayu).",
    "karier": "Desainer Produk Kriya, Seniman Kriya, Kurator Seni, Pengajar Seni, Wirausaha Kerajinan"
  },
  {
    "nama": "Manajemen",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengorganisasian, pengarahan, dan pengendalian sumber daya organisasi (manusia, keuangan, material) untuk mencapai tujuan secara efektif dan efisien.",
    "karier": "Manajer Pemasaran, Manajer Keuangan, Manajer Sumber Daya Manusia (HR), Konsultan Manajemen, Analis Bisnis"
  },
  {
    "nama": "Manajemen Agribisnis",
    "mata_pelajaran": "Ekonomi, Biologi",
    "deskripsi": "ilmu yang mempelajari penerapan prinsip-prinsip manajemen dalam rantai nilai bisnis pertanian, mulai dari pengadaan sarana produksi hingga pemasaran produk hasil pertanian.",
    "karier": "Manajer Agribisnis, Analis Pasar Komoditas Pertanian, Konsultan Bisnis Pertanian, Manajer Rantai Pasok Pangan, Wirausaha Pertanian"
  },
  {
    "nama": "Manajemen Pelabuhan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengoperasian, dan pengelolaan fasilitas serta kegiatan logistik dan transportasi di area pelabuhan dan perairan.",
    "karier": "Staf Operasional Pelabuhan, Manajer Logistik Maritim, Analis Rantai Pasok, Staf Bea Cukai, Konsultan Logistik"
  },
  {
    "nama": "Matematika",
    "mata_pelajaran": "Matematika Tingkat Lanjut, Matematika",
    "deskripsi": "ilmu yang mempelajari konsep-konsep seperti kuantitas, struktur, ruang, dan perubahan, menggunakan penalaran logis, aljabar, kalkulus, dan teori.",
    "karier": "Matematikawan (Peneliti), Analis Data, Aktuaris, Analis Kuantitatif, Kriptografer"
  },
  {
    "nama": "Meteorologi & Instrumentasi",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari fenomena atmosfer, cuaca, dan iklim, serta perancangan dan penggunaan instrumen untuk pengukuran data atmosfer.",
    "karier": "Prakirawan Cuaca (BMKG), Peneliti Meteorologi, Spesialis Instrumentasi Geofisika, Konsultan Iklim"
  },
  {
    "nama": "Oseanografi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari samudra dan laut, termasuk sifat fisik dan kimia air laut, pergerakan arus, biologi laut, dan geologi dasar laut.",
    "karier": "Oseanografer (Peneliti), Konsultan Lingkungan Kelautan, Analis Data Kelautan, Staf Industri Perkapalan/Minyak & Gas"
  },
  {
    "nama": "Pariwisata",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, pengembangan, dan pengelolaan destinasi wisata serta pelayanan yang berkaitan dengan perjalanan dan hospitalitas.",
    "karier": "Manajer Hotel/Resort, Perencana Destinasi Wisata, Konsultan Pariwisata, Pemandu Wisata, Spesialis Pemasaran Pariwisata"
  },
  {
    "nama": "Pemanfaatan Sumberdaya Perikanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari cara-cara penangkapan, pengolahan, dan pemasaran hasil perikanan serta manajemen sumber daya ikan di perairan secara berkelanjutan.",
    "karier": "Manajer Penangkapan Ikan, Quality Control Hasil Perikanan, Konsultan Perikanan Tangkap, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Pemasaran",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari strategi untuk menciptakan, mengkomunikasikan, dan memberikan nilai kepada pelanggan serta mengelola hubungan pelanggan dengan cara yang menguntungkan.",
    "karier": "Manajer Pemasaran (Marketing Manager), Analis Pasar, Spesialis Digital Marketing, Manajer Produk (Product Manager), Konsultan Pemasaran"
  },
  {
    "nama": "Pendidikan Akuntansi",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari konsep akuntansi, auditing, dan perpajakan dengan fokus pada metodologi dan praktik pengajaran untuk profesi guru/dosen.",
    "karier": "Guru/Dosen Akuntansi, Penulis Buku Ajar, Konsultan Pendidikan, Staf Akuntansi Perusahaan"
  },
  {
    "nama": "Pendidikan Bahasa Indonesia",
    "mata_pelajaran": "Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari struktur, sastra, dan budaya Indonesia dengan fokus pada metode pengajaran yang efektif untuk menjadi seorang pendidik.",
    "karier": "Guru/Dosen Bahasa Indonesia, Penulis/Editor, Konsultan Bahasa, Penyunting Naskah"
  },
  {
    "nama": "Pendidikan Bahasa Inggris",
    "mata_pelajaran": "Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Inggris dengan fokus pada metode dan praktik pengajaran bahasa asing.",
    "karier": "Guru/Dosen Bahasa Inggris, Penerjemah, Konsultan Pendidikan, Penulis Materi Ajar"
  },
  {
    "nama": "Pendidikan Biologi",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari segala aspek kehidupan dan makhluk hidup dengan fokus pada metode pengajaran dan pendidikan di tingkat sekolah.",
    "karier": "Guru/Dosen Biologi, Peneliti Pendidikan, Pengembang Kurikulum Sains, Staf Laboratorium Pendidikan"
  },
  {
    "nama": "Pendidikan Bisnis",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari konsep bisnis dan manajemen dengan fokus pada pengajaran praktik-praktik kewirausahaan dan keterampilan manajerial di sekolah/vokasi.",
    "karier": "Guru/Dosen Bisnis dan Ekonomi, Konsultan Pendidikan Vokasi, Staf Pelatihan dan Pengembangan (Training & Development) Perusahaan"
  },
  {
    "nama": "Pendidikan Ekonomi",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari teori dan prinsip ekonomi, akuntansi, dan bisnis dengan fokus pada metodologi pengajaran untuk menjadi seorang pendidik.",
    "karier": "Guru/Dosen Ekonomi, Analis Ekonomi (non-teaching), Konsultan Pendidikan, Pengembang Kurikulum"
  },
  {
    "nama": "Pendidikan Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari sifat dan interaksi materi serta energi dengan fokus pada metode pengajaran dan pendidikan Fisika.",
    "karier": "Guru/Dosen Fisika, Peneliti Pendidikan Sains, Pengembang Alat Peraga Sains, Analis Laboratorium"
  },
  {
    "nama": "Pendidikan Geografi",
    "mata_pelajaran": "Geografi",
    "deskripsi": "ilmu yang mempelajari fenomena permukaan bumi, hubungan manusia dan lingkungan, dengan fokus pada metodologi pengajaran Geografi.",
    "karier": "Guru/Dosen Geografi, Ahli Sistem Informasi Geografis (SIG), Konsultan Tata Ruang, Peneliti Wilayah"
  },
  {
    "nama": "Pendidikan Guru PAUD",
    "mata_pelajaran": "Sosiologi, Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari psikologi perkembangan anak usia dini, kurikulum, dan metode pengajaran yang sesuai untuk Pendidikan Anak Usia Dini (PAUD).",
    "karier": "Guru PAUD, Kepala Sekolah PAUD, Konsultan Parenting, Pengembang Mainan Edukasi"
  },
  {
    "nama": "Pendidikan Guru SD",
    "mata_pelajaran": "Sosiologi, Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari berbagai disiplin ilmu dasar (Matematika, Bahasa, IPA, IPS) dengan fokus pada metodologi pengajaran terpadu untuk Sekolah Dasar (SD).",
    "karier": "Guru Sekolah Dasar (SD), Kepala Sekolah SD, Pengembang Kurikulum SD, Konsultan Pendidikan Dasar"
  },
  {
    "nama": "Pendidikan Jasmani",
    "mata_pelajaran": "PJOK",
    "deskripsi": "ilmu yang mempelajari teori dan praktik pendidikan melalui aktivitas fisik, olahraga, dan kesehatan untuk membentuk karakter dan gaya hidup sehat.",
    "karier": "Guru Pendidikan Jasmani, Pelatih Olahraga, Terapis Fisik, Konsultan Kebugaran"
  },
  {
    "nama": "Pendidikan Kepelatihan Olahraga",
    "mata_pelajaran": "PJOK",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip ilmiah pelatihan olahraga, manajemen atlet, dan pengembangan program latihan untuk mencapai prestasi maksimal.",
    "karier": "Pelatih Olahraga Profesional, Analis Kinerja Atlet, Manajer Tim Olahraga, Konsultan Olahraga"
  },
  {
    "nama": "Pendidikan Kesejahteraan Keluarga",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya keluarga, gizi, tata busana, dan tata boga dengan tujuan meningkatkan kualitas dan kesejahteraan keluarga.",
    "karier": "Guru Tata Boga/Busana, Konsultan Kesejahteraan Keluarga, Wirausaha Kuliner/Fashion, Staf NGO Sosial"
  },
  {
    "nama": "Pendidikan Kimia",
    "mata_pelajaran": "Kimia",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, dan perubahan zat dengan fokus pada metode pengajaran dan pendidikan Kimia.",
    "karier": "Guru/Dosen Kimia, Peneliti Pendidikan Sains, Analis Laboratorium, Pengembang Kurikulum Kimia"
  },
  {
    "nama": "Pendidikan Luar Sekolah",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari penyelenggaraan pendidikan di luar jalur formal, seperti kursus, pelatihan, dan pemberdayaan masyarakat, untuk meningkatkan kualitas hidup.",
    "karier": "Fasilitator Pemberdayaan Masyarakat, Manajer Pelatihan (Training Manager), Konsultan Pendidikan Non-formal, Staf NGO Pendidikan"
  },
  {
    "nama": "Pendidikan Matematika",
    "mata_pelajaran": "Matematika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari konsep-konsep Matematika dengan fokus pada metodologi pengajaran yang efektif untuk tingkat sekolah.",
    "karier": "Guru/Dosen Matematika, Peneliti Pendidikan Matematika, Pengembang Kurikulum, Analis Data"
  },
  {
    "nama": "Pendidikan PKN",
    "mata_pelajaran": "Pancasila",
    "deskripsi": "ilmu yang mempelajari konsep kewarganegaraan, demokrasi, hukum, dan hak asasi manusia dengan fokus pada metodologi pengajaran Pendidikan Kewarganegaraan (PKN).",
    "karier": "Guru/Dosen PKN, Analis Kebijakan Publik, Konsultan Pendidikan, Staf Lembaga Pemerintahan"
  },
  {
    "nama": "Pendidikan Sejarah",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari peristiwa masa lalu, analisis sumber sejarah, dan interpretasi kronologis dengan fokus pada metodologi pengajaran Sejarah.",
    "karier": "Guru/Dosen Sejarah, Peneliti Sejarah, Kurator Museum, Penulis Buku Sejarah, Pemandu Wisata Sejarah"
  },
  {
    "nama": "Pendidikan Sendratari Musik",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori dan praktik seni pertunjukan (seni drama, tari, dan musik) dengan fokus pada metodologi pengajaran dan pengembangan seni di sekolah.",
    "karier": "Guru Kesenian, Koreografer, Komposer, Pengelola Sanggar Seni, Seniman Pertunjukan"
  },
  {
    "nama": "Pendidikan Seni Rupa",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, sejarah, dan praktik seni rupa (lukis, patung, grafis) dengan fokus pada metodologi pengajaran seni.",
    "karier": "Guru Seni Rupa, Seniman, Kurator Galeri, Desainer Produk, Konsultan Kreatif"
  },
  {
    "nama": "Pendidikan Tata Boga",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari prinsip dasar pengolahan makanan, gizi, dan manajemen kuliner dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Boga, Chef/Koki Profesional, Konsultan Kuliner, Wirausaha Kuliner"
  },
  {
    "nama": "Pendidikan Tata Busana",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari desain, konstruksi, dan manajemen busana (pakaian) dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Busana, Desainer Fashion, Penjahit/Modiste, Konsultan Fashion, Wirausaha Busana"
  },
  {
    "nama": "Pendidikan Tata Rias",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teknik merias wajah, rambut, dan tubuh, serta manajemen salon/spa dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Tata Rias, Make-up Artist Profesional, Konsultan Kecantikan, Wirausaha Salon/Spa"
  },
  {
    "nama": "Pendidikan Teknik Bangunan",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip teknik sipil, konstruksi, dan perancangan bangunan dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Bangunan, Pengawas Konstruksi (non-Insinyur), Drafter Arsitektur, Konsultan Pendidikan Vokasi"
  },
  {
    "nama": "Pendidikan Teknik Elektro",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip listrik, elektronika, dan sistem kendali dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Elektro, Teknisi Elektronika, Konsultan Pelatihan Industri, Pengembang Materi Vokasi"
  },
  {
    "nama": "Pendidikan Teknik Elektronika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan dan pengaplikasian komponen dan sirkuit elektronika dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Elektronika, Teknisi Instrumentasi, Konsultan Pelatihan, Teknisi Otomasi Industri"
  },
  {
    "nama": "Pendidikan Teknik Otomotif",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari teknologi mesin, sistem kendaraan, dan perawatan otomotif dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Otomotif, Teknisi Bengkel Profesional, Konsultan Pelatihan Otomotif, Pengembang Materi Vokasi"
  },
  {
    "nama": "Pendidikan Teknologi Informasi",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari konsep dasar komputasi, pemrograman, dan jaringan dengan fokus pada metodologi pengajaran di tingkat sekolah.",
    "karier": "Guru/Dosen TIK/Informatika, Pengembang E-learning, Konsultan Teknologi Pendidikan, Staf IT Sekolah/Perusahaan"
  },
  {
    "nama": "Pendidikan Vokasional Teknik Mesin",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip mekanika, perancangan mesin, dan proses manufaktur dengan fokus pada metodologi pengajaran di sekolah vokasi/SMK.",
    "karier": "Guru Teknik Mesin, Teknisi Manufaktur, Konsultan Pelatihan Industri, Pengembang Materi Vokasi"
  },
  {
    "nama": "Perencanaan Wilayah dan Kota",
    "mata_pelajaran": "Ekonomi, Matematika",
    "deskripsi": "ilmu yang mempelajari perancangan dan penataan ruang, sumber daya, dan kegiatan di suatu wilayah atau kota untuk mencapai pembangunan yang berkelanjutan.",
    "karier": "Perencana Tata Ruang (PNS/Konsultan), Analis Kebijakan Pembangunan, Konsultan Properti, Ahli Sistem Informasi Geografis (SIG)"
  },
  {
    "nama": "Perikanan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari manajemen sumber daya perikanan, teknologi penangkapan, dan pengolahan hasil perikanan serta ekosistem perairan.",
    "karier": "Manajer Perikanan, Peneliti Sumber Daya Ikan, Quality Control Hasil Perikanan, Konsultan Kelautan, Pegawai Kementerian Kelautan dan Perikanan"
  },
  {
    "nama": "Perpajakan",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari secara mendalam seluruh aspek hukum, administrasi, dan akuntansi yang berkaitan dengan pajak pusat dan daerah.",
    "karier": "Konsultan Pajak, Pegawai Direktorat Jenderal Pajak (DJP), Staf Perpajakan Perusahaan, Kuasa Hukum Pajak, Akuntan Pajak"
  },
  {
    "nama": "Peternakan",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari pengelolaan ternak (sapi, ayam, kambing, dll.) secara ilmiah, termasuk nutrisi, reproduksi, kesehatan, dan manajemen usaha peternakan.",
    "karier": "Manajer Peternakan, Konsultan Ternak, Peneliti Produk Hewani, Quality Control Pakan, Pegawai Dinas Peternakan"
  },
  {
    "nama": "Proteksi Tanaman",
    "mata_pelajaran": "Biologi",
    "deskripsi": "ilmu yang mempelajari identifikasi, pencegahan, dan pengendalian hama, penyakit, dan gulma untuk melindungi tanaman budidaya dari kerusakan dan kerugian.",
    "karier": "Ahli Hama dan Penyakit Tanaman, Konsultan Proteksi Tanaman, Peneliti Pertanian, Spesialis Quality Control Produk Pertanian, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Psikologi",
    "mata_pelajaran": "Sosiologi, Matematika",
    "deskripsi": "ilmu yang mempelajari perilaku dan proses mental manusia, termasuk pikiran, emosi, dan motivasi, melalui penelitian dan praktik klinis/industri.",
    "karier": "Psikolog Klinis/Edukasi (setelah S2), Konselor, Staf HRD/Spesialis Rekrutmen, Analis Data Perilaku, Peneliti Psikologi"
  },
  {
    "nama": "Sastra Arab",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari linguistik, sastra, dan kebudayaan yang berasal dari dunia Arab, termasuk kemampuan berbahasa dan penerjemahan.",
    "karier": "Penerjemah/Juru Bahasa Arab, Staf Kedutaan, Editor Naskah, Konsultan Budaya Timur Tengah, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Batak",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra lisan dan tulis, serta budaya etnis Batak untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Belanda",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan Belanda, termasuk sejarahnya di Indonesia, untuk keperluan terjemahan dan penelitian.",
    "karier": "Penerjemah/Juru Bahasa Belanda, Arsiparis, Peneliti Sejarah Kolonial, Staf Kedutaan Belanda"
  },
  {
    "nama": "Sastra Cina",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari linguistik, sastra, dan kebudayaan Cina (Mandarin) untuk menguasai komunikasi, terjemahan, dan pemahaman lintas budaya.",
    "karier": "Penerjemah/Juru Bahasa Mandarin, Staf Perusahaan Cina, Konsultan Bisnis Asia, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Indonesia",
    "mata_pelajaran": "Bahasa Indonesia",
    "deskripsi": "ilmu yang mempelajari struktur, sastra lisan dan tulis, serta kebudayaan Indonesia untuk menghasilkan karya kreatif dan analisis kritis.",
    "karier": "Penulis/Novelis/Penyair, Editor/Penyunting Naskah, Jurnalis/Reporter, Kritikus Sastra, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Inggris",
    "mata_pelajaran": "Bahasa Inggris, Sastra Inggris",
    "deskripsi": "ilmu yang mempelajari karya-karya sastra (puisi, prosa, drama) dan sejarah sastra dari negara-negara berbahasa Inggris, serta teori-teori kritis.",
    "karier": "Penerjemah/Juru Bahasa, Penulis/Editor, Jurnalis, Analis Kebudayaan, Dosen Sastra"
  },
  {
    "nama": "Sastra Jawa",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra lisan dan tulis, serta kebudayaan Jawa untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Kurator Museum, Penulis/Editor, Konsultan Budaya Lokal, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Jepang",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari tata bahasa, sastra, dan budaya Jepang untuk menguasai kemampuan komunikasi, terjemahan, dan pemahaman mendalam tentang masyarakat Jepang.",
    "karier": "Penerjemah/Juru Bahasa Jepang, Staf Perusahaan Jepang, Pemandu Wisata, Spesialis Hubungan Internasional, Staf Kedutaan"
  },
  {
    "nama": "Sastra Melayu",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan Melayu di berbagai wilayah, termasuk sejarah dan perkembangannya.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sastra Minangkabau",
    "mata_pelajaran": "Bahasa Indonesia, Bahasa Inggris",
    "deskripsi": "ilmu yang mempelajari bahasa, sastra, dan kebudayaan etnis Minangkabau untuk pelestarian dan pengembangan warisan lokal.",
    "karier": "Peneliti Budaya, Jurnalis Budaya, Konsultan Budaya Lokal, Penulis/Editor, Dosen Bahasa/Sastra"
  },
  {
    "nama": "Sejarah",
    "mata_pelajaran": "Sejarah",
    "deskripsi": "ilmu yang mempelajari, meneliti, dan menganalisis peristiwa, tokoh, dan perkembangan masa lalu untuk memahami konteks dan implikasinya di masa kini.",
    "karier": "Sejarawan (Peneliti), Arsiparis, Kurator Museum, Penulis Buku Sejarah, Jurnalis/Analis Politik"
  },
  {
    "nama": "Seni Karawitan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, praktik, dan komposisi musik gamelan (karawitan) serta instrumen tradisional Jawa, Sunda, atau Bali.",
    "karier": "Pemusik Karawitan Profesional, Komposer Musik Tradisional, Guru/Dosen Seni, Pengelola Sanggar Seni"
  },
  {
    "nama": "Seni Pertunjukkan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari proses penciptaan, produksi, dan pementasan seni drama, tari, atau musik, serta manajemen pertunjukan.",
    "karier": "Sutradara Teater/Tari, Koreografer, Seniman Pertunjukan, Manajer Produksi Seni, Kurator Seni Pertunjukan"
  },
  {
    "nama": "Seni Rupa Murni",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari penciptaan karya seni rupa (lukis, patung, grafis) dengan penekanan pada nilai estetika dan ekspresi diri, bukan fungsi terapan.",
    "karier": "Seniman Profesional, Kurator Galeri, Kritikus Seni, Dosen Seni, Konsultan Seni"
  },
  {
    "nama": "Seni Tari",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teori, sejarah, dan praktik tari (tradisional dan kontemporer) serta proses penciptaan karya tari (koreografi).",
    "karier": "Koreografer, Penari Profesional, Guru/Dosen Tari, Pengelola Sanggar Tari, Seniman Pertunjukan"
  },
  {
    "nama": "Seni Teater",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari seni peran, penyutradaraan, penulisan naskah, dan manajemen produksi pementasan drama atau teater.",
    "karier": "Aktor/Aktris, Sutradara Teater, Penulis Naskah Drama, Manajer Produksi Seni, Guru/Dosen Seni Pertunjukan"
  },
  {
    "nama": "Sistem Informasi",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan pengelolaan sistem berbasis komputer untuk mendukung operasional dan pengambilan keputusan bisnis.",
    "karier": "System Analyst, Konsultan ERP, Manajer Proyek IT, Data Analyst, Spesialis Keamanan Informasi"
  },
  {
    "nama": "Sosiologi",
    "mata_pelajaran": "Sosiologi",
    "deskripsi": "ilmu yang mempelajari masyarakat, interaksi sosial, perilaku kelompok, serta struktur dan perubahan sosial yang terjadi di dalamnya.",
    "karier": "Sosiolog/Peneliti Sosial, Analis Pasar dan Konsumen, Konsultan Pembangunan Masyarakat, Staf NGO/LSM, Analis Kebijakan Sosial"
  },
  {
    "nama": "Statistika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari pengumpulan data, analisis, interpretasi, dan presentasi data secara kuantitatif untuk menarik kesimpulan dan membuat prediksi.",
    "karier": "Statistikawan, Data Scientist, Analis Bisnis/Pasar, Analis Risiko, Peneliti Biostatistika"
  },
  {
    "nama": "Tata Rias dan Kecantikan",
    "mata_pelajaran": "Seni Budaya",
    "deskripsi": "ilmu yang mempelajari teknik merias wajah, rambut, dan tubuh, serta pengelolaan salon/spa dengan fokus pada layanan kecantikan dan estetika.",
    "karier": "Make-up Artist Profesional, Konsultan Kecantikan, Terapis Kecantikan, Wirausaha Salon/Spa, Guru Tata Rias"
  },
  {
    "nama": "Teknik Elektro",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan dan aplikasi sistem yang berkaitan dengan listrik, elektronika, elektromagnetisme, dan sistem kendali.",
    "karier": "Insinyur Elektronika, Insinyur Sistem Tenaga Listrik, Spesialis Otomasi Industri, Konsultan Energi, Peneliti Teknologi Listrik"
  },
  {
    "nama": "Teknik Elektronika",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pengembangan, dan pengaplikasian komponen dan sirkuit elektronika untuk sistem komunikasi, kontrol, dan instrumentasi.",
    "karier": "Insinyur Elektronika, Perancang Sistem Embedded, Teknisi Instrumentasi, Spesialis Telekomunikasi, Insinyur Otomasi"
  },
  {
    "nama": "Teknik Fisika",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip fisika pada pengembangan teknologi dan instrumentasi di berbagai bidang industri dan rekayasa.",
    "karier": "Insinyur Instrumentasi, Analis Sistem Energi, Konsultan Akustik/Optik, Peneliti Material, Insinyur Quality Control"
  },
  {
    "nama": "Teknik Geofisika",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari struktur, komposisi, dan proses yang terjadi di bawah permukaan bumi menggunakan prinsip-prinsip fisika untuk eksplorasi sumber daya alam.",
    "karier": "Geofisikawan Eksplorasi (Minyak & Gas, Panas Bumi), Analis Bencana Alam, Konsultan Lingkungan, Peneliti Geofisika"
  },
  {
    "nama": "Teknik Geologi",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari komposisi, struktur, dan sejarah bumi, termasuk proses pembentukan batuan, mineral, dan potensi sumber daya geologi.",
    "karier": "Geolog Eksplorasi (Pertambangan/Minyak & Gas), Hidrogeolog, Konsultan Geoteknik, Analis Mitigasi Bencana Geologi"
  },
  {
    "nama": "Teknik Industri",
    "mata_pelajaran": "Fisika, Kimia, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, perbaikan, dan instalasi sistem terintegrasi (manusia, material, informasi, peralatan, dan energi) untuk mengoptimalkan proses produksi dan operasional.",
    "karier": "Manajer Operasional, Konsultan Manajemen, Analis Rantai Pasok (Supply Chain), Spesialis Quality Control/QA, Analis Ergonomi"
  },
  {
    "nama": "Teknik Informatika",
    "mata_pelajaran": "Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari prinsip-prinsip dan praktik perancangan serta pengembangan sistem perangkat lunak, termasuk pemrograman, jaringan, dan keamanan informasi.",
    "karier": "Software Engineer, Network Engineer, Analis Keamanan Siber, Data Scientist, Konsultan IT"
  },
  {
    "nama": "Teknik Kimia",
    "mata_pelajaran": "Fisika, Kimia",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip kimia, fisika, dan matematika untuk merancang, mengoperasikan, dan mengelola proses konversi bahan baku menjadi produk kimia yang bernilai.",
    "karier": "Insinyur Proses (Pabrik Kimia, Minyak & Gas), Peneliti Produk Baru, Spesialis Keselamatan Proses, Konsultan Lingkungan"
  },
  {
    "nama": "Teknik Komputer",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang menggabungkan prinsip teknik elektro dan ilmu komputer untuk merancang dan mengembangkan sistem perangkat keras (hardware) dan perangkat lunak (software).",
    "karier": "Insinyur Perangkat Keras, Insinyur Sistem Tertanam (Embedded Systems), Pengembang Robotika, Analis Jaringan Komputer"
  },
  {
    "nama": "Teknik Lingkungan",
    "mata_pelajaran": "Fisika, Biologi",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip sains dan rekayasa untuk mencegah dan menyelesaikan masalah lingkungan, seperti polusi air, udara, dan pengelolaan limbah.",
    "karier": "Insinyur Lingkungan, Konsultan Amdal, Spesialis Pengelolaan Limbah, Auditor Lingkungan, Pegawai Kementerian Lingkungan Hidup"
  },
  {
    "nama": "Teknik Listrik",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari pembangkitan, transmisi, distribusi, dan pemanfaatan energi listrik, termasuk perancangan sistem instalasi listrik.",
    "karier": "Insinyur Listrik, Teknisi Jaringan Tenaga Listrik, Spesialis Otomasi Bangunan, Konsultan Instalasi Listrik"
  },
  {
    "nama": "Teknik Logistik",
    "mata_pelajaran": "Ekonomi",
    "deskripsi": "ilmu yang mempelajari perencanaan, implementasi, dan pengendalian aliran barang, jasa, dan informasi dari titik asal hingga titik konsumsi secara efisien dan efektif.",
    "karier": "Manajer Logistik, Analis Rantai Pasok (Supply Chain), Manajer Gudang, Konsultan Logistik, Staf Perusahaan Ekspedisi"
  },
  {
    "nama": "Teknik Material",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari struktur, sifat, kinerja, dan pemrosesan berbagai jenis material (logam, polimer, keramik) serta pengembangan material baru.",
    "karier": "Insinyur Material, Peneliti Material, Spesialis Quality Control Logam/Polimer, Konsultan Material Industri"
  },
  {
    "nama": "Teknik Mesin",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, analisis, manufaktur, dan pemeliharaan sistem mekanik, mulai dari mesin sederhana hingga kompleks.",
    "karier": "Insinyur Perancangan Mesin, Insinyur Manufaktur, Manajer Pemeliharaan (Maintenance), Konsultan Mekanikal, Insinyur Otomotif"
  },
  {
    "nama": "Teknik Perkapalan",
    "mata_pelajaran": "Fisika",
    "deskripsi": "ilmu yang mempelajari perancangan, pembangunan, perbaikan, dan pemeliharaan kapal dan struktur apung lainnya, termasuk sistem propulsi dan stabilitas.",
    "karier": "Insinyur Perancangan Kapal, Manajer Produksi Galangan Kapal, Spesialis Klasifikasi Kapal, Konsultan Maritim"
  },
  {
    "nama": "Teknik Pertambangan",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari eksplorasi, penambangan, pengolahan, dan pemasaran sumber daya mineral secara aman dan efisien, serta rekayasa lingkungan pasca-tambang.",
    "karier": "Insinyur Tambang, Geolog Pertambangan, Spesialis Keselamatan Tambang, Konsultan Lingkungan, Peneliti Mineral"
  },
  {
    "nama": "Teknik Pertanian",
    "mata_pelajaran": "Fisika, Biologi",
    "deskripsi": "ilmu yang menerapkan prinsip-prinsip rekayasa dan teknologi pada sistem pertanian untuk meningkatkan efisiensi dan hasil produksi, seperti irigasi, alat mesin pertanian, dan pascapanen.",
    "karier": "Insinyur Pertanian, Manajer Alat Mesin Pertanian, Konsultan Irigasi, Pengembang Teknologi Pertanian, Pegawai Kementerian Pertanian"
  },
  {
    "nama": "Teknik Sipil",
    "mata_pelajaran": "Fisika, Matematika Tingkat Lanjut",
    "deskripsi": "ilmu yang mempelajari perancangan, pembangunan, dan pemeliharaan infrastruktur seperti gedung, jalan, jembatan, bendungan, dan sistem transportasi.",
    "karier": "Insinyur Sipil Perancangan Struktur, Manajer Proyek Konstruksi, Konsultan Geoteknik, Pengawas Lapangan, Perencana Infrastruktur"
  },
  {
    "nama": "Teknologi Hasil Pertanian",
    "mata_pelajaran": "Kimia, Biologi",
    "deskripsi": "ilmu yang mempelajari tentang pengolahan, pengawetan, dan peningkatan nilai tambah produk-produk hasil pertanian (pangan maupun non-pangan) dengan menerapkan prinsip-prinsip kimia, biokimia, bioteknologi, dan rekayasa proses untuk menghasilkan produk yang aman, bermutu, dan bergizi.",
    "karier": "Manajer Produksi Industri Pangan, Quality Control (QC), Research and Development (R&D), Konsultan Pangan/Pertanian, Pegawai BPOM, Wirausaha Bidang Pangan, Lembaga Penelitian"
  }
]

def collect_subjects(db):
    s = []
    for item in db:
        parts = [p.strip() for p in item["mata_pelajaran"].split(",") if p.strip()]
        for p in parts:
            if p not in s:
                s.append(p)
    return sorted(s)

ALL_SUBJECTS = collect_subjects(JURUSAN_DB)

WEIGHTS = {"minat":0.05, "mata":0.20, "nilai":0.70, "cita":0.05}

def normalize(t):
    return str(t).strip().lower()

def subject_list(field):
    return [p.strip() for p in str(field).split(",") if p.strip()]

def compute_score(profile, major):
    minat = normalize(profile.get("minat",""))
    cita = normalize(profile.get("cita",""))
    nilai = float(profile.get("nilai",0)) if profile.get("nilai") != "" else 0.0
    prof_subs = [normalize(x) for x in profile.get("mata_pelajaran",[])]
    major_name = normalize(major.get("nama",""))
    major_desc = normalize(major.get("deskripsi",""))
    major_careers = normalize(major.get("karier",""))
    major_subs = [normalize(x) for x in subject_list(major.get("mata_pelajaran",""))]

    minat_comp = 1.0 if (minat and (minat in major_name or minat in major_desc or minat in major_careers)) else 0.0

    if major_subs:
        matched = 0
        for ps in prof_subs:
            for ms in major_subs:
                if ps and (ps == ms or ps in ms or ms in ps):
                    matched += 1
                    break
        mata_comp = min(matched / max(1, len(major_subs)), 1.0)
    else:
        mata_comp = 0.0

    nilai_comp = max(0.0, min(1.0, nilai/100.0))
    cita_comp = 1.0 if (cita and (cita in major_careers or cita in major_name or cita in major_desc)) else 0.0

    total = (WEIGHTS["minat"]*minat_comp + WEIGHTS["mata"]*mata_comp + WEIGHTS["nilai"]*nilai_comp + WEIGHTS["cita"]*cita_comp)
    percent = round(total*100,1)
    breakdown = {
        "minat_pct": round(WEIGHTS["minat"]*minat_comp*100,1),
        "mata_pct": round(WEIGHTS["mata"]*mata_comp*100,1),
        "nilai_pct": round(WEIGHTS["nilai"]*nilai_comp*100,1),
        "cita_pct": round(WEIGHTS["cita"]*cita_comp*100,1)
    }
    return percent, breakdown

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Career Path</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial; background: #eaf7ea; }
        .container { max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 10px; }
        label { display: block; margin-top: 10px; }
        select, input { width: 100%; padding: 8px; margin-top: 4px; }
        .btn { background: #2b8cff; color: #fff; padding: 10px; border: none; width: 100%; margin-top: 16px; border-radius: 5px; }
        .result { background: #f6fff6; margin-top: 20px; padding: 10px; border-radius: 8px; }
    </style>
</head>
<body>
<div class="container">
    <h2>Carier Path — Rekomendasi Jurusan & Karier SMA</h2>
    <form method="post">
        <label>Nama:</label>
        <input name="name" required>
        <label>Minat:</label>
        <input name="minat" required>
        <label>Nilai rata-rata (0-100):</label>
        <input name="nilai" type="number" min="0" max="100" required>
        <label>Cita-cita:</label>
        <input name="cita" required>
        <label>Pilih Mata Pelajaran Favorit (bisa pilih lebih dari satu):</label>
        <select name="mata_pelajaran" multiple size="7" required>
            {% for s in subjects %}
            <option value="{{s}}">{{s}}</option>
            {% endfor %}
        </select>
        <button class="btn" type="submit">Dapatkan Rekomendasi</button>
    </form>
    {% if hasil %}
    <div class="result">
        <b>Hasil Rekomendasi:</b>
        <ul>
        {% for item in hasil %}
            <li>
                <b>{{item['Jurusan']}}</b> (Skor: {{item['Skor']}}%)<br>
                Mata Pendukung: {{item['Mata Pendukung']}}<br>
                Karier: {{item['Karier']}}<br>
                <i>{{item['Deskripsi']}}</i>
            </li>
        {% endfor %}
        </ul>
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = []
    if request.method == "POST":
        name = request.form.get("name","")
        minat = request.form.get("minat","")
        nilai = request.form.get("nilai","")
        cita = request.form.get("cita","")
        mata_pelajaran = request.form.getlist("mata_pelajaran")
        try:
            nilai_float = float(nilai)
        except:
            nilai_float = 0
        profile = {
            "name": name,
            "minat": minat,
            "mata_pelajaran": mata_pelajaran,
            "nilai": nilai_float,
            "cita": cita
        }
        candidates = []
        for major in JURUSAN_DB:
            score, breakdown = compute_score(profile, major)
            if score > 75:
                candidates.append({
                    "Jurusan": major["nama"],
                    "Mata Pendukung": ", ".join(subject_list(major["mata_pelajaran"])),
                    "Deskripsi": major.get("deskripsi","-"),
                    "Karier": major.get("karier","-"),
                    "Skor": score
                })
        candidates.sort(key=lambda x: x["Skor"], reverse=True)
        hasil = candidates[:5]
    return render_template_string(HTML_FORM, subjects=ALL_SUBJECTS, hasil=hasil)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)