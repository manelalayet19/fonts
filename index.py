from flask import Flask, render_template
from flask_mail import Mail, Message
import datetime
app = Flask(__name__)
import base64

from premailer import transform

mailSettings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USE_SSL': False,
    'MAIL_USERNAME': 'geoimpact.ai@gmail.com',
    'MAIL_PASSWORD': 'gchmtvopncojnome',

}
app.config.update(mailSettings)




mail = Mail(app)

def read_base64_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
@app.route("/")
@app.route('/send-mail/')
def send_mail():
    gotham_bold_base64 = read_base64_file('static/GothamBold.ttf.base64')
    gotham_medium_base64 = read_base64_file('static/GothamSSm-Medium.ttf.base64')
    gotham_book_base64 = read_base64_file('static/GothamSSm-Book.ttf.base64')
    html_content ="""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Launch event </title>
</head>
 <style>
      @font-face {{
          font-family: "Gotham-Medium";
          src: url(data:font/truetype;charset=utf-8;base64,{gotham_medium_base64}) format("truetype");
      }}
      @font-face {{
          font-family: "Gotham-Bold";
          src: url(data:font/truetype;charset=utf-8;base64,{gotham_bold_base64}) format("truetype");
      }}
      @font-face {{
          font-family: "Gotham-Book";
          src: url(data:font/truetype;charset=utf-8;base64,{gotham_book_base64}) format("truetype");
      }}
  </style>
<body
  style=" font-family: Gotham-Medium; margin: 0; padding: 0; box-sizing: border-box; color: #092540; text-align: justify; font-family: Gotham-Medium; line-height: 2; font-size: 12px !important;">
  <table class="content" style="margin: 115px auto 60px auto; width: 80%;">
    <tr>
      <td class="header" style="font-weight: bold; padding-bottom: 20px;">

    <img src="https://i.postimg.cc/7L7VS1wn/geoimpact-logo-2-lignes-bicolore-RGB.png" alt="logo"
           style="width: 414px; height: 120px;">
       
      </td>
      <td class="header" style="font-weight: bold; text-align: right;  font-family :Gotham-Medium; ">
        Canada, le 30/04/2024
      </td>
    </tr>
    <tr>
      <td colspan="2" style="padding: 20px 0;">
        <hr style="background-color: #DCDC1E; height: 10px; border-radius: 25px; border: none;">
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: justify; font-style: normal; font-weight: 400;">
        Nous sommes ravis de vous présenter <span style="color: #DCDC1E; font-weight: 800;">GeoImpact</span>, un produit
        d'ApexMachina. <span style="color: #91CED4; font-weight: 800;">GeoImpact</span> est une plateforme de base de
        données de pointe qui permet de rassembler des données géographiques et économiques provenant de diverses
        sources. La plateforme est conçue pour offrir aux utilisateurs des outils de visualisation, d'analyse et de
        partage des données. Avec GeoImpact, vous pouvez obtenir des informations précieuses et prendre des décisions
        éclairées sur la base de sources de données complètes et d'analyses en temps réel. Désormais, vous pouvez nous
        confier le travail sur les données et commencer votre analyse immédiatement ! Après un développement et des
        tests approfondis, nous sommes confiants que <span style="color: #91CED4; font-weight: 800;">GeoImpact</span>
        sera un outil indispensable, offrant une précision incomparable et des interactions conviviales.
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <!-- Replace the flexbox structure with a table-based layout -->
        <table class="sikillset" style="width: 100%;">
          <tr>
            <td>
              <div style="font-size: 24px ;font-weight: bolder;">
              Pourquoi  <span style="color: #91CED4;">GeoImpact</span> ?
            </div></td>
          </tr>
          <tr>
            <td class="elements" style="vertical-align: top; width: 50%;">
              <ul style="margin: 0; padding: 0;     margin-right: 20px; list-style: none;">
                <li style="line-height: 2;"> - <strong>Visualiser les données sur une carte:</strong> Visualisez
                  facilement un large éventail d'indicateurs et d'ensembles de données sur une interface cartographique
                  interactive, comme illustré à droite. Des variables socio-économiques aux données environnementales,
                  GeoImpact vous permet d'explorer l'information sans effort.</li>
                <li style="line-height: 2;"> - <strong>Créer des projets :</strong> Créez et gérez des projets en toute
                  transparence dans votre espace utilisateur. Que vous meniez des recherches, planifiez des initiatives
                  ou analysiez des tendances, GeoImpact fournit une plateforme centralisée pour tous vos projets.</li>
                <li style="line-height: 2;"> - <strong>Ajoutez vos propres données:</strong> Améliorez votre analyse en
                  incorporant vos propres jeux de données dans GeoImpact. Qu'il s'agisse de fichiers de forme,
                  d'identifiants uniques ou de couches de données personnalisées, vous avez la possibilité d'enrichir
                  votre analyse et de l'adapter à vos besoins spécifiques.</li>
                <li style="line-height: 2;"> - <strong>Simulations avancées :</strong> Profitez du module CiSim pour
                  réaliser des simulations et des modélisations avancées. De la planification urbaine aux études
                  d'impact sur l'environnement, CiSim vous permet de simuler différents scénarios et d'évaluer les
                  résultats de manière efficace.</li>
                <li style="line-height: 2;"> - <strong>Partagez vos projets :</strong> Collaborez avec vos collègues,
                  parties prenantes et partenaires en partageant facilement vos projets et résultats. GeoImpact facilite
                  la collaboration et le partage des connaissances, garantissant ainsi l'accès à toutes les parties
                  prenantes.</li>
                <li style="line-height: 2;"> - <strong>Interface conviviale :</strong> Grâce à son interface intuitive
                  et conviviale, GeoImpact rend l'analyse des données accessible aux utilisateurs de tous niveaux. Que
                  vous soyez un professionnel chevronné ou un novice, vous trouverez GeoImpact facile à utiliser et à
                  naviguer.</li>
              </ul>
            </td>
            <td class="imges" style="vertical-align: top; width: 50%;">
              <img src="https://c.animaapp.com/R75bDWcm/img/rectangle-6.png" alt=""
                style="border-radius: 10px; background: url(<path-to-image>) lightgray 50% / cover no-repeat; width: 100%; height: auto;">
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center; font-size: 18px; font-weight: bold; padding-top: 20px;">Participez à
        l'événement de lancement officiel</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;  line-height: 2.5;">
        <p>
          Retenez cette date dans votre calendrier ! Nous vous invitons à nous rejoindre lors de notre événement de
          lancement virtuel le <b>02/05/2024</b>, où nous présenterons les capacités de GeoImpact et partagerons des idées sur
          l'avenir de la technologie géospatiale. <br> Inscrivez-vous dès maintenant pour réserver votre place et participer
          avec nous à cette aventure passionnante.  <br> Rejoignez-nous et explorez la puissance des informations géospatiales
          avec <span style="color: #91CED4; font-weight: 800;">GeoImpact</span>.
        </p>
      </td>
      <tr>
        <td colspan="2" style="text-align: center;">
          <a style="border-radius: 50px; background-color: #092540; color: white; text-decoration: none; padding: 20px 100px; text-align: center; font-size: 14px; font-weight: 600; display: inline-block; margin-top: 20px;"
            href="http://geopovnet.com:5000/">Rejoindre l'événement</a>
        </td>
      </tr>
      <tr>
        <td colspan="2" style="text-align: center; line-height: 2.5;">
          <p>
            Nous sommes très enthousiastes à l'idée de voir comment <span
              style="color: #DCDC1E; font-size: 14px; font-weight: 800;">GeoImpact</span> soutiendra vos projets et
            favorisera l'innovation dans vos opérations. Nous vous remercions de votre soutien continu et de la confiance
            que vous accordez à nos solutions. <br>
            Nous sommes impatients de recevoir vos commentaires et d'atteindre de nouveaux sommets ensemble.<br>
            Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées, <br>
            <span style="font-size: 14px; font-weight: bolder;">Damien Echevin</span> <br>
            <span style="font-size: 14px; font-weight: bolder;">fondateur et directeur général, GeoImpact</span> <br>
            N'hésitez pas à nous contacter pour toute question ou pour organiser une démonstration personnalisée de
            GeoImpact. Inventons l'avenir ensemble !
          </p>
        </td>
      </tr>
    </tr>
   
    <tr>
      <td colspan="2" style="text-align: center;">
        <div class="imgDemo"
          style="width: 1046px; height: 595px; border-radius: 10px; margin: 20px auto; box-shadow: rgba(145, 206, 212, 0.1) 0px 12px 28px 25px, rgba(145, 206, 212, 0.1) 0px 2px 4px 25px, rgba(145, 206, 212, 0.1) 0px 0px 0px 25px inset;">
          <img src="https://c.animaapp.com/R75bDWcm/img/ps-viztool1-1.png" alt=""
            style="border-radius: 10px; width: 100%; height: auto;">
        </div>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;">
        <a style="border-radius: 50px; background-color: #092540; color: white; text-decoration: none;
         padding: 20px 100px; text-align: center; font-size: 14px; font-weight: 600; display: inline-block; margin: 20px;"
          href="http://geopovnet.com:5000/">Demandez une démonstration</a>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center; line-height: 2.5;">
        <div style="margin-bottom: 20px;">Copyright © 2024 GeoImpact</div>
        <div class="logosmall">
          <img src="https://c.animaapp.com/R75bDWcm/img/image-7.png" alt="" style="width: 60px; height: 58px;">
        </div>
        <div>GeoImpact , 1, boul. de l'Université , Sherbrooke QC , J1J1J1 Canada</div>
        <div>Cet e-mail a été envoyé parce que vous avez indiqué que vous souhaitiez recevoir des informations et des
          mises à jour sur GeoImpact.</div>
        <div>Si vous ne souhaitez pas recevoir d'autres communications de <span
            style="color: #DCDC1E; font-weight: 800;">GeoImpact</span>, veuillez consulter cette page -> <span
            style="color: #91CED4; font-weight: 800;">se désinscrire</span></div>
      </td>
    </tr>
  </table>
</body>

</html>"""
 

    msg = Message('Launch Event', sender="geoimpact.ai@gmail.com",
                  recipients=["alayet.manel@gmail.com" ])
    
    msg.html = html_content

    with app.open_resource("franch-version.pdf") as fp:
        msg.attach("french_version.pdf", "application/pdf", fp.read())

    mail.send(msg)

    return 'Mail sent!'





@app.route("/tmp")
def tmf():

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

