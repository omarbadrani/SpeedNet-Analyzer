import sys
import os
import json
import platform
from datetime import datetime
import matplotlib

matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QComboBox, QProgressBar, QMessageBox, QTabWidget, QGroupBox, QSizePolicy
)
from PySide6.QtCore import Qt, QThread, Signal, QSize
from PySide6.QtGui import QFont

# Fix pour la compatibilité Python 2/3
try:
    import builtins  # Python 3
except ImportError:
    import builtins as builtins  # Python 2

# Fix pour PyInstaller
if getattr(sys, 'frozen', False):
    sys.stdin = open(os.devnull)
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

try:
    import speedtest
except ImportError:
    raise ImportError("Veuillez installer la bibliothèque speedtest : pip install speedtest")


class SpeedTestThread(QThread):
    progress_update = Signal(int, str)
    results_ready = Signal(float, float, float, str)
    error_occurred = Signal(str)
    server_info = Signal(dict)

    def __init__(self, server_id=None, timeout=10):
        super().__init__()
        self.server_id = server_id
        self.timeout = timeout
        self.abort = False

    def run(self):
        try:
            self.progress_update.emit(10, "Initialisation du test...")
            st = speedtest.Speedtest(timeout=self.timeout)

            self.progress_update.emit(20, "Recherche du meilleur serveur...")
            server = st.get_best_server()

            if not isinstance(server, dict):
                raise ValueError("Format de réponse du serveur invalide")

            self.server_info.emit(server)

            if self.abort:
                return

            self.progress_update.emit(50, "Test de download en cours...")
            download = round(st.download() / 10 ** 6, 2)

            if self.abort:
                return

            self.progress_update.emit(70, "Test d'upload en cours...")
            upload = round(st.upload() / 10 ** 6, 2)

            ping = round(st.results.ping, 2)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.progress_update.emit(100, "Test terminé!")
            self.results_ready.emit(download, upload, ping, timestamp)

        except Exception as e:
            self.error_occurred.emit(str(e))

    def stop_test(self):
        self.abort = True


class SpeedTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetSpeed Analyzer")
        self.setMinimumSize(800, 600)
        self.servers = {}
        self.current_test_count = 0
        self.max_tests = 10
        self.test_history = []
        self.current_server_info = {}
        self.timeout = 10
        self.speed_thread = None

        self.init_ui()
        self.load_history()

    def init_ui(self):
        self.setup_styles()
        self.create_widgets()
        self.setup_layout()
        self.refresh_server_list()

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget { background-color: #f5f5f5; font-family: Arial; }
            QPushButton {
                background-color: #4CAF50; color: white; border: none;
                padding: 8px 16px; font-size: 14px; border-radius: 4px;
            }
            QPushButton:hover { background-color: #45a049; }
            QPushButton:disabled { background-color: #cccccc; }
            QLabel { font-size: 14px; }
            QProgressBar {
                border: 1px solid #ccc; border-radius: 3px; text-align: center;
                height: 20px;
            }
            QProgressBar::chunk { background-color: #4CAF50; width: 10px; }
            QComboBox { padding: 5px; border: 1px solid #ccc; border-radius: 3px; }
            QGroupBox {
                border: 1px solid #ddd; border-radius: 5px;
                margin-top: 10px; padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin; left: 10px; padding: 0 3px;
            }
        """)

    def create_widgets(self):
        # Titre
        self.title_label = QLabel("NetSpeed Analyzer")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))

        # Configuration
        self.config_group = QGroupBox("Configuration")
        self.server_label = QLabel("Serveur:")
        self.server_combo = QComboBox()
        self.server_combo.setToolTip("Sélectionnez un serveur ou laissez automatique")

        self.timeout_label = QLabel("Timeout (s):")
        self.timeout_combo = QComboBox()
        self.timeout_combo.addItems(["5", "10", "15", "20", "30"])
        self.timeout_combo.setCurrentIndex(1)
        self.timeout_combo.currentTextChanged.connect(self.set_timeout)

        # Boutons
        self.test_button = QPushButton("Lancer le Test")
        self.test_button.clicked.connect(self.start_test)

        self.stop_button = QPushButton("Arrêter")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_test)

        self.refresh_button = QPushButton("Rafraîchir")
        self.refresh_button.clicked.connect(self.refresh_server_list)

        self.history_button = QPushButton("Historique")
        self.history_button.clicked.connect(self.show_history)

        self.export_button = QPushButton("Exporter")
        self.export_button.clicked.connect(self.export_results)

        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        # Affichage résultats
        self.result_label = QLabel("Prêt à tester")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)

        self.server_info_label = QLabel("Serveur: Non sélectionné")
        self.server_info_label.setAlignment(Qt.AlignCenter)
        self.server_info_label.setWordWrap(True)

        self.stats_label = QLabel("")
        self.stats_label.setAlignment(Qt.AlignCenter)

        # Graphique - Version corrigée
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumHeight(300)
        self.canvas.setMinimumWidth(400)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Onglets
        self.tabs = QTabWidget()

    def setup_layout(self):
        main_layout = QVBoxLayout(self)

        # Configuration
        config_layout = QHBoxLayout()
        config_layout.addWidget(self.server_label)
        config_layout.addWidget(self.server_combo, 1)
        config_layout.addWidget(self.timeout_label)
        config_layout.addWidget(self.timeout_combo)
        self.config_group.setLayout(config_layout)

        # Boutons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.test_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.history_button)
        button_layout.addWidget(self.export_button)

        # Onglet principal
        main_tab = QWidget()
        main_tab_layout = QVBoxLayout(main_tab)
        main_tab_layout.addWidget(self.title_label)
        main_tab_layout.addWidget(self.config_group)
        main_tab_layout.addLayout(button_layout)
        main_tab_layout.addWidget(self.progress_bar)
        main_tab_layout.addWidget(self.result_label)
        main_tab_layout.addWidget(self.server_info_label)
        main_tab_layout.addWidget(self.stats_label)
        main_tab_layout.addWidget(self.canvas)

        # Onglet système
        sys_tab = QWidget()
        sys_layout = QVBoxLayout(sys_tab)
        sys_info = QLabel(self.get_system_info())
        sys_info.setAlignment(Qt.AlignLeft)
        sys_layout.addWidget(sys_info)

        # Ajout des onglets
        self.tabs.addTab(main_tab, "Test")
        self.tabs.addTab(sys_tab, "Système")

        main_layout.addWidget(self.tabs)

    def set_timeout(self, timeout):
        self.timeout = int(timeout)

    def get_system_info(self):
        return f"""
        <b>Informations Système:</b><br>
        Développé par: Omar Badrani<br>
        Système: {platform.system()} {platform.release()}<br>
        Processeur: {platform.processor()}<br>
        Speedtest-cli: {speedtest.__version__}
        """

    def start_test(self):
        self.test_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.result_label.setText("Initialisation...")
        self.progress_bar.setValue(0)

        server_id = self.server_combo.currentData()

        # Initialize the thread properly
        self.speed_thread = SpeedTestThread(server_id, self.timeout)
        self.speed_thread.progress_update.connect(self.update_progress)
        self.speed_thread.results_ready.connect(self.show_results)
        self.speed_thread.error_occurred.connect(self.show_error)
        self.speed_thread.server_info.connect(self.update_server_info)
        self.speed_thread.finished.connect(self.test_finished)

        # Start the thread
        self.speed_thread.start()

    def stop_test(self):
        if hasattr(self, 'speed_thread') and self.speed_thread is not None:
            self.speed_thread.stop_test()
            if self.speed_thread.isRunning():
                self.speed_thread.terminate()
                self.speed_thread.wait()
            self.speed_thread = None
        self.result_label.setText("Test arrêté")
        self.progress_bar.setValue(0)
        self.reset_buttons()

    def test_finished(self):
        self.reset_buttons()
        if hasattr(self, 'speed_thread') and self.speed_thread is not None:
            self.speed_thread.deleteLater()
            self.speed_thread = None
    def reset_buttons(self):
        self.test_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def test_finished(self):
        self.reset_buttons()
        if self.speed_thread:
            self.speed_thread.deleteLater()
            self.speed_thread = None

    def update_progress(self, value, message):
        self.progress_bar.setValue(value)
        self.result_label.setText(message)

    def update_server_info(self, server_info):
        self.current_server_info = server_info
        info = f"""
        Serveur: {server_info['sponsor']} ({server_info['name']})<br>
        Pays: {server_info['country']}<br>
        Distance: {server_info['d']:.2f} km | Latence: {server_info['latency']:.2f} ms
        """
        self.server_info_label.setText(info)

    def show_results(self, download, upload, ping, timestamp):
        test_data = {
            'download': download,
            'upload': upload,
            'ping': ping,
            'timestamp': timestamp,
            'server': f"{self.current_server_info.get('sponsor', '?')} ({self.current_server_info.get('name', '?')})",
            'server_info': self.current_server_info
        }

        self.save_test_result(test_data)
        self.update_stats()

        result_text = f"""
        <b>Résultats:</b><br>
        Download: <b>{download} Mbps</b><br>
        Upload: <b>{upload} Mbps</b><br>
        Ping: <b>{ping} ms</b><br>
        <small>Testé à {timestamp}</small>
        """
        self.result_label.setText(result_text)
        self.plot_history()

    def save_test_result(self, test_data):
        self.current_test_count += 1
        test_data['count'] = self.current_test_count
        self.test_history.append(test_data)

        if len(self.test_history) > self.max_tests:
            self.test_history.pop(0)

        self.save_history()

    def update_stats(self):
        if not self.test_history:
            return

        avg_dl = sum(t['download'] for t in self.test_history) / len(self.test_history)
        avg_ul = sum(t['upload'] for t in self.test_history) / len(self.test_history)
        avg_ping = sum(t['ping'] for t in self.test_history) / len(self.test_history)

        stats = f"""
        Moyennes ({len(self.test_history)} tests):<br>
        Download: {avg_dl:.2f} Mbps | Upload: {avg_ul:.2f} Mbps | Ping: {avg_ping:.1f} ms
        """
        self.stats_label.setText(stats)

    def save_history(self):
        try:
            with open("history.json", "w") as f:
                json.dump(self.test_history, f, indent=2)
        except Exception as e:
            self.show_error(f"Erreur sauvegarde: {e}")

    def load_history(self):
        try:
            with open("history.json", "r") as f:
                self.test_history = json.load(f)
                if self.test_history:
                    self.current_test_count = max(t['count'] for t in self.test_history)
        except (FileNotFoundError, json.JSONDecodeError):
            self.test_history = []

    def plot_history(self):
        if not self.test_history:
            return

        self.figure.clear()
        ax = self.figure.add_subplot(111)

        dates = [datetime.strptime(t['timestamp'], "%Y-%m-%d %H:%M:%S") for t in self.test_history]
        dl = [t['download'] for t in self.test_history]
        ul = [t['upload'] for t in self.test_history]
        ping = [t['ping'] for t in self.test_history]

        ax.plot(dates, dl, 'g-', label='Download (Mbps)')
        ax.plot(dates, ul, 'b-', label='Upload (Mbps)')
        ax.plot(dates, ping, 'r-', label='Ping (ms)')

        ax.set_title("Historique des tests")
        ax.set_xlabel("Date")
        ax.set_ylabel("Valeur")
        ax.legend()
        ax.grid(True)

        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        self.figure.tight_layout()
        self.canvas.draw()

    def refresh_server_list(self):
        try:
            self.refresh_button.setEnabled(False)
            self.result_label.setText("Recherche des serveurs...")
            QApplication.processEvents()

            st = speedtest.Speedtest()
            servers = st.get_servers()

            current = self.server_combo.currentData()
            self.server_combo.clear()
            self.server_combo.addItem("Auto", None)
            self.servers = {}

            # Trier par pays/nom
            sorted_servers = []
            for country, server_list in servers.items():
                for server in server_list:
                    server['country'] = country
                    sorted_servers.append(server)

            sorted_servers.sort(key=lambda x: (x['country'], x['name']))

            for server in sorted_servers:
                server_id = server['id']
                name = f"{server['sponsor']} ({server['name']}, {server['country']})"
                self.servers[server_id] = name
                self.server_combo.addItem(name, server_id)

            if current in self.servers:
                idx = self.server_combo.findData(current)
                if idx >= 0:
                    self.server_combo.setCurrentIndex(idx)

            self.result_label.setText(f"{len(self.servers)} serveurs trouvés")

        except Exception as e:
            self.show_error(f"Erreur recherche serveurs: {e}")
        finally:
            self.refresh_button.setEnabled(True)

    def show_history(self):
        if not self.test_history:
            QMessageBox.information(self, "Historique", "Aucun test enregistré")
            return

        history = "<html><table border='1'><tr><th>#</th><th>Date</th><th>Download</th><th>Upload</th><th>Ping</th></tr>"

        for test in reversed(self.test_history):
            history += f"""
            <tr>
                <td>{test['count']}</td>
                <td>{test['timestamp']}</td>
                <td>{test['download']} Mbps</td>
                <td>{test['upload']} Mbps</td>
                <td>{test['ping']} ms</td>
            </tr>
            """

        history += "</table></html>"

        msg = QMessageBox()
        msg.setWindowTitle("Historique")
        msg.setTextFormat(Qt.RichText)
        msg.setText(history)
        msg.exec()

    def export_results(self):
        if not self.test_history:
            QMessageBox.information(self, "Export", "Aucun résultat à exporter")
            return

        try:
            filename = f"speedtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Numéro;Date;Download (Mbps);Upload (Mbps);Ping (ms);Serveur\n")
                for test in self.test_history:
                    f.write(
                        f"{test['count']};{test['timestamp']};{test['download']};{test['upload']};{test['ping']};{test['server']}\n")

            QMessageBox.information(self, "Export", f"Résultats exportés dans {filename}")
        except Exception as e:
            self.show_error(f"Erreur export: {e}")

    def show_error(self, message):
        QMessageBox.critical(self, "Erreur", message)
        self.result_label.setText("Erreur")
        self.progress_bar.setValue(0)
        self.reset_buttons()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = SpeedTestApp()
    window.show()
    sys.exit(app.exec())