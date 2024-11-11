import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Funsi untuk mengirim email
def kirim_email(pengirim, penerima, subject, html_content):
    # konfigurasi server SMTP
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.starttls()
    server.login(pengirim, 'nihy wzkm duax fchy')

    # Membuat object email
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = subject

    # Menyisipkan konten HTML ke dalam email
    msg.attach(MIMEText(html_content, 'html'))

    # Mengirim email
    server.send_message(msg)
    server.quit()

    #Membuat template html untuk email
    html_template = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="project.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Project</title>
    <style>
    body{
    margin: 0;
}

nav{
    background-color: black;
    color: white;
    padding: 2px;
    font-size: 19px;
    text-align: right;
    margin: 0;
}

.H:hover{
    text-decoration: underline;
    
}

.G{
    display: inline;
    padding: 1rem;
    font-family: 'Roboto', sans-serif;
    margin-right: 45rem;

}

.H{
    display: inline;
    padding: 1rem;
    margin-right: 5rem;
    font-family: 'Roboto', sans-serif;
}
.A{
    text-decoration: none;
    color: white;
}
#Home{
    display: flex;
    flex-direction: row;
}
.datang{
    font-size: 75px;
    padding: 2rem;
    width: 39rem;
    margin: 9rem;
    font-family: 'Roboto', sans-serif;
}
.Komputer{
    width: 350px;
    height: 350px;
    margin-top: 8rem;
    
   

}
main{
    display: flex;
    flex-direction: row;
}

    </style>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li class="G">Project Dicoding</li>
                <li class="H">
                    <a href="#" class="A">Home</a>
                </li>
                <li class="H">
                    <a href="#" class="A">About</a>
                </li>
                <li class="H">
                    <a href="#" class="A">Contact</a>
                </li>
            </ul>
        </nav>
    </header>
    <div id="Home">
        <p class="datang">Selamat datang di projek saya untuk dicoding</p>
        <img class="Komputer" src="dicoding-removebg-preview.png" alt="">
      </div>
    <main>
        <article></article>
        <aside></aside>
    </main>
    <footer></footer>
</body>
</html>
"""



pengirim = 'kalenovtakhoirulanwar@gmail.com'
penerima = 'kingnovta@gmail.com'
subject =  'rawrrr'