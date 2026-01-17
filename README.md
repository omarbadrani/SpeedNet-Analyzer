# ⚡ NetSpeed Analyzer

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.4%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

A modern, intuitive GUI application to test and analyze your internet speed with detailed graphs and complete history.

## ✨ Features

### 🚀 Complete Speed Test
- **📥 Download**: Accurate download speed measurement
- **📤 Upload**: Upload speed testing
- **⏱️ Ping/Latency**: Server response time measurement
- **🌍 Global Servers**: Access to hundreds of servers worldwide

### 📊 Advanced Visualization
- **Real-time Graphs**: Visual performance history
- **3 Separate Charts**: Download, Upload, and Ping
- **Detailed Statistics**: Averages, maximums, minimums, trends
- **Automatic Evaluation**: Connection quality classification

### 🔧 Modern Interface
- **Qt6 Design**: Smooth professional interface
- **Multi-tabs**: Testing and system information
- **Emojis & Icons**: Visual intuitive interface
- **Flexible Configuration**: Adjustable timeout, server selection

### 📁 Data Management
- **💾 Auto Save**: History preserved between sessions
- **📤 CSV Export**: Exportable data for external analysis
- **🗑️ Cleanup**: Option to clear history
- **📊 Comparison**: Performance tracking over time

## 🚀 Quick Installation

```bash
# Clone repository
git clone https://github.com/username/netspeed-analyzer.git
cd netspeed-analyzer

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
```txt
PySide6>=6.4.0
speedtest-cli>=2.1.3
matplotlib>=3.5.0
```

## 🎮 Usage Guide

### Launch Application
```bash
python main.py
```

### Step-by-Step Usage

1. **Configure Test**
   - Select specific server or leave "Auto"
   - Adjust timeout if needed (10 seconds recommended)
   - Click "🔄 Refresh" to update server list

2. **Start Test**
   - Click "🚀 Start Test"
   - Track progress in bar and messages
   - Stop anytime with "⏹️ Stop"

3. **Analyze Results**
   - Check Download/Upload speeds and ping
   - View evolution charts
   - Check average statistics

4. **Manage Data**
   - "📊 History": Shows last 10 tests
   - "💾 Export": Save as CSV file
   - "🗑️ Clear": Delete test history

## 📊 Performance Rating

Application automatically rates your connection:

| Category | Download | Upload | Ping |
|----------|----------|--------|------|
| **Excellent** | > 100 Mbps | > 50 Mbps | < 20 ms |
| **Good** | 50-100 Mbps | 20-50 Mbps | 20-50 ms |
| **Average** | 10-50 Mbps | 5-20 Mbps | 50-100 ms |
| **Poor** | < 10 Mbps | < 5 Mbps | > 100 ms |

## 🔧 Troubleshooting

### Common Issues:
- **"Module speedtest not found"**: Run `pip install speedtest-cli`
- **Interface won't launch**: Check PySide6: `pip install PySide6`
- **No servers available**: Check internet connection and firewall
- **Charts not displaying**: `pip install matplotlib`
- **Test too slow**: Increase timeout or change server

## 📁 Project Structure
```
netspeed-analyzer/
├── main.py              # Main application
├── requirements.txt     # Dependencies
├── history.json        # Test history (auto-generated)
├── speedtest_*.csv    # CSV exports (auto-generated)
└── README.md          # Documentation
```

## 📄 License
MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author
**Omar Badrani**  
- GitHub: https://github.com/omarbadrani  
- Email: omarbadrani770@gmail.com

---

⭐ **If you like this project, please star the repository!** ⭐

---

**Version**: 1.2.0  
**Python**: 3.7+  
**OS**: Windows, Linux, macOS

*NetSpeed Analyzer - Because your connection deserves precise analysis* 🚀
