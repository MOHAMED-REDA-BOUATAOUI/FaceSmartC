import mysql.connector
import cv2

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="facesmart"
)
cursor = conn.cursor()

# Lecture de l'image
image_path = "C:\Users\pc\Desktop\PFA\images\hamza.jpg"
image = cv2.imread(image_path)

# Conversion de l'image en données binaires
retval, buffer = cv2.imencode('.jpg', image)
image_as_bytes = buffer.tobytes()

# Insertion de l'image dans la base de données
insert_query = "INSERT INTO Employees (name, image) VALUES (%s, %s)"
cursor.execute(insert_query, ("Employee Name", image_as_bytes))
conn.commit()

# Fermeture de la connexion
cursor.close()
conn.close()
