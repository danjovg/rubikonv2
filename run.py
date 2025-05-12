from app import create_app

app = create_app()  # 👈 Define globalmente sin condición

# El bloque siguiente es solo para desarrollo local
if __name__ == '__main__':
    app.run(debug=True)
