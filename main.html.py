<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyWallet - Expense Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-orange: #FF5722;
            --primary-orange-hover: #E64A19;
            --bg-color: #F4F6F9;
            --card-bg: #FFFFFF;
            --text-main: #1E293B;
            --text-muted: #64748B;
            --border-color: #E2E8F0;
            --income-green: #10B981;
            --expense-red: #EF4444;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 24px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 480px; /* Lebar ala mobile app / clean dashboard */
        }

        /* Header Style */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }
        .header h1 {
            font-size: 20px;
            font-weight: 700;
            color: var(--text-main);
        }
        .profile-badge {
            background-color: #FFE0D6;
            color: var(--primary-orange);
            font-weight: 600;
            font-size: 12px;
            padding: 6px 12px;
            border-radius: 20px;
        }

        /* Main Balance Card (SeaBank Style Orange Banner) */
        .balance-card {
            background: linear-gradient(135deg, #FF5722 0%, #FF8A65 100%);
            color: white;
            padding: 24px;
            border-radius: 20px;
            box-shadow: 0 10px 25px -5px rgba(255, 87, 34, 0.3);
            margin-bottom: 20px;
        }
        .balance-title {
            font-size: 13px;
            opacity: 0.9;
            margin-bottom: 6px;
            font-weight: 500;
        }
        .balance-amount {
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 20px;
        }
        .balance-stats {
            display: flex;
            justify-content: space-between;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            padding-top: 14px;
        }
        .stat-item span {
            display: block;
            font-size: 11px;
            opacity: 0.8;
        }
        .stat-item strong {
            font-size: 14px;
            font-weight: 600;
        }

        /* Quick Action Button */
        .btn-add {
            display: block;
            width: 100%;
            background-color: var(--text-main);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 14px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            text-align: center;
            margin-bottom: 24px;
            transition: background 0.2s;
        }
        .btn-add:hover {
            background-color: #0F172A;
        }

        /* Section Styling */
        .section {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 18px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            margin-bottom: 16px;
            border: 1px solid var(--border-color);
        }
        .section-header {
            font-size: 14px;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Category List */
        .category-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 0;
            border-bottom: 1px solid #F1F5F9;
            font-size: 13px;
        }
        .category-item:last-child {
            border-bottom: none;
        }
        .category-name {
            color: var(--text-muted);
        }
        .category-value {
            font-weight: 600;
            color: var(--text-main);
        }

        /* Transaction List */
        .transaction-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #F1F5F9;
        }
        .transaction-item:last-child {
            border-bottom: none;
        }
        .t-info h4 {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 2px;
        }
        .t-info p {
            font-size: 11px;
            color: var(--text-muted);
        }
        .t-amount {
            font-size: 13px;
            font-weight: 600;
            text-align: right;
        }
        .t-income { color: var(--income-green); }
        .t-expense { color: var(--expense-red); }

        .footer {
            text-align: center;
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 24px;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Top App Bar -->
        <div class="header">
            <h1>MyWallet</h1>
            <div class="profile-badge">Nov 2026</div>
        </div>

        <!-- Main Balance Card (SeaBank Style) -->
        <div class="balance-card">
            <div class="balance-title">Sisa Saldo Dompet</div>
            <div class="balance-amount">Rp 7.560.000</div>
            <div class="balance-stats">
                <div class="stat-item">
                    <span>Pemasukan</span>
                    <strong>+Rp 8.700.000</strong>
                </div>
                <div class="stat-item" style="text-align: right;">
                    <span>Pengeluaran</span>
                    <strong>-Rp 1.140.000</strong>
                </div>
            </div>
        </div>

        <!-- Quick Action -->
        <button class="btn-add">+ Catat Transaksi Baru</button>

        <!-- Kategori Pengeluaran -->
        <div class="section">
            <div class="section-header">Pengeluaran Berdasarkan Kategori</div>
            <div class="category-item">
                <span class="category-name">🍽️ Makanan & Minuman</span>
                <span class="category-value">Rp 685.000</span>
            </div>
            <div class="category-item">
                <span class="category-name">💡 Tagihan & Utilitas</span>
                <span class="category-value">Rp 350.000</span>
            </div>
            <div class="category-item">
                <span class="category-name">🛵 Transportasi</span>
                <span class="category-value">Rp 50.000</span>
            </div>
            <div class="category-item">
                <span class="category-name">🎮 Hiburan</span>
                <span class="category-value">Rp 45.000</span>
            </div>
        </div>

        <!-- Riwayat Transaksi -->
        <div class="section">
            <div class="section-header">
                <span>Riwayat Transaksi</span>
                <span style="font-size: 11px; color: var(--primary-orange); cursor: pointer;">Lihat Semua</span>
            </div>
            
            <div class="transaction-item">
                <div class="t-info">
                    <h4>Freelance Desain</h4>
                    <p>10 Nov 2026 • Income</p>
                </div>
                <div class="t-amount t-income">+Rp 1.200.000</div>
            </div>

            <div class="transaction-item">
                <div class="t-info">
                    <h4>Makan Siang Kantin</h4>
                    <p>10 Nov 2026 • Food</p>
                </div>
                <div class="t-amount t-expense">-Rp 35.000</div>
            </div>

            <div class="transaction-item">
                <div class="t-info">
                    <h4>Bayar Listrik & Air</h4>
                    <p>07 Nov 2026 • Bills</p>
                </div>
                <div class="t-amount t-expense">-Rp 350.000</div>
            </div>

            <div class="transaction-item">
                <div class="t-info">
                    <h4>Nongkrong Kopi</h4>
                    <p>05 Nov 2026 • Entertainment</p>
                </div>
                <div class="t-amount t-expense">-Rp 45.000</div>
            </div>

            <div class="transaction-item">
                <div class="t-info">
                    <h4>Bensin Motor</h4>
                    <p>03 Nov 2026 • Transport</p>
                </div>
                <div class="t-amount t-expense">-Rp 50.000</div>
            </div>
        </div>

        <div class="footer">
            MyWallet App &bull; Dibuat dengan gaya modern & bersih
        </div>
    </div>

</body>
</html>