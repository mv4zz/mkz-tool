import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import socket
import threading
import json
import pygame
import os
from datetime import datetime

class PhoneController:
    def __init__(self, root):
        self.root = root
        self.root.title("PHONE CONTROLLER")
        self.root.geometry("600x800")
        self.root.configure(bg="#121212")

        # Initialize mixer
        pygame.mixer.init()

        # Networking
        self.host_ip = self.get_local_ip()
        self.port = 12345
        self.server_socket = None
        self.client_socket = None
        self.connection_active = False

        # UI Setup
        self.setup_ui()

        # Start server
        self.start_server()

    def get_local_ip(self):
        """Get actual local IP (not 127.0.0.1)"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#121212", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = tk.Label(
            main_frame,
            text="PHONE CONTROLLER",
            font=("Helvetica", 24, "bold"),
            fg="white",
            bg="#121212"
        )
        header.pack(pady=(0, 20))

        # QR Code Section
        qr_frame = tk.Frame(main_frame, bg="#1E1E1E", padx=10, pady=10)
        qr_frame.pack(fill=tk.X, pady=10)

        # Make QR code larger and clearer
        self.qr_label = tk.Label(qr_frame, bg="white", width=300, height=300)
        self.qr_label.pack()

        # Generate PROPERLY formatted QR code
        self.generate_working_qr()

        # Status
        self.status_var = tk.StringVar(value="🔴 DISCONNECTED")
        status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Helvetica", 12),
            fg="white",
            bg="#121212"
        )
        status_label.pack(pady=10)

        # Control Buttons (disabled until connection)
        self.controls_frame = tk.Frame(main_frame, bg="#121212")
        self.controls_frame.pack(fill=tk.BOTH, expand=True)

        self.buttons = [
            ("🔊 PLAY SOUND", self.play_sound),
            ("🔒 LOCK DEVICE", self.lock_device),
            ("📍 LOCATE PHONE", self.locate_phone),
            ("☢ FACTORY RESET", self.factory_reset)
        ]

        self.button_widgets = []
        for text, command in self.buttons:
            btn = tk.Button(
                self.controls_frame,
                text=text,
                font=("Helvetica", 14),
                bg="#333333",
                fg="white",
                activebackground="#444444",
                activeforeground="white",
                bd=0,
                padx=20,
                pady=15,
                command=command,
                state=tk.DISABLED
            )
            btn.pack(fill=tk.X, pady=5)
            self.button_widgets.append(btn)

    def generate_working_qr(self):
        """Generate PROPERLY formatted QR code that actually scans"""
        connection_info = {
            "type": "phone_controller",
            "ip": self.host_ip,
            "port": self.port,
            "timestamp": datetime.now().isoformat()
        }
        
        # Use simpler QR format that scanners can read reliably
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(connection_info))  # Remove indentation for compact size
        qr.make(fit=True)
        
        # Create high-contrast QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to Tkinter PhotoImage (with proper sizing)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.qr_label.config(image=img_tk)
        self.qr_label.image = img_tk

    def start_server(self):
        """Start TCP server with proper error handling"""
        def server_thread():
            try:
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind((self.host_ip, self.port))
                self.server_socket.listen(1)
                
                self.root.after(0, lambda: self.status_var.set(
                    f"🟡 WAITING AT {self.host_ip}:{self.port} "
                ))
                
                self.client_socket, addr = self.server_socket.accept()
                self.connection_active = True
                self.root.after(0, lambda: self.status_var.set(
                    f"🟢 CONNECTED: {addr[0]}"
                ))
                self.root.after(0, self.enable_buttons)
                
                # Keep connection alive
                while self.connection_active:
                    try:
                        data = self.client_socket.recv(1024)
                        if not data:
                            break
                    except:
                        break
                
                self.disconnect()
                
            except Exception as e:
                self.root.after(0, lambda: self.status_var.set(
                    f"🔴 ERROR: {str(e)}"
                ))

        threading.Thread(target=server_thread, daemon=True).start()

    def enable_buttons(self):
        """Enable all control buttons"""
        for btn in self.button_widgets:
            btn.config(state=tk.NORMAL)

    def send_command(self, command):
        """Send command with proper error handling"""
        if not self.connection_active:
            messagebox.showerror("Error", "No device connected!")
            return
            
        try:
            self.client_socket.sendall(
                json.dumps({"command": command}).encode() + b"\n"
            )
        except Exception as e:
            self.status_var.set(f"🔴 CONNECTION LOST")
            self.connection_active = False
            self.disable_buttons()

    def play_sound(self):
        self.send_command("play_sound")

    def lock_device(self):
        self.send_command("lock_device")

    def locate_phone(self):
        self.send_command("locate_phone")

    def factory_reset(self):
        if messagebox.askyesno(
            "WARNING", 
            "ERASE ALL DATA ON DEVICE?",
            icon="warning"
        ):
            self.send_command("factory_reset")

    def disconnect(self):
        """Proper connection cleanup"""
        try:
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()
        except:
            pass
            
        self.connection_active = False
        self.status_var.set("🔴 DISCONNECTED")
        self.disable_buttons()

    def disable_buttons(self):
        """Disable all control buttons"""
        for btn in self.button_widgets:
            btn.config(state=tk.DISABLED)

    def on_close(self):
        """Cleanup on window close"""
        self.disconnect()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneController(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
