import os
try:
    import requests
except:
    os.system("pip install requests")
print(requests.get('http://artii.herokuapp.com/make?text=engineer').text)
name = input("What's you'r website name ? : ")
bio = input("you'r bio ? : ")
html = '<!DOCTYPE html>' + "\n" + '<html lang="en">' + "\n" + '<head>' + "\n" + '  <meta charset="UTF-8">' + "\n" + '  <meta http-equiv="X-UA-Compatible" content="IE=Edge">' + "\n" + '  <meta name="viewport" content="width=device-width, initial-scale=1">' + "\n" + '  <title></title>' + "\n" + '</head>'+ "\n" + '<body>' + "\n" + '  <div id="name">' + "\n" + f'    <h1>{name}</h1>' + "\n" + '    </div>' + "\n" + '  <div id="programmer">' + "\n" + '    <img src="https://i.pinimg.com/736x/b4/6f/85/b46f8521d36cd5e9c25007946710820c.jpg" width="300px"></div>' + "\n" + '  <fieldset>' + "\n" + '    <legend>Biography</legend>' + "\n" +f'    {bio}' + "\n" +'  </fieldset>' + "\n" +'  <style>' + "\n" +'    body{' + "\n" +'      background: #E8E8E8;' + "\n" + '    }' + "\n" +'    *{' + "\n" +'      padding: 0;' + "\n" +'      margin: 0;' + "\n" +'    }' + "\n" +'    #name{' + "\n" +'     background:white;' + "\n" +'     height: 45px;' + "\n" + '     box-shadow: 0px 0px 0px 3px #D2D2D2;' + "\n" + '    }' + "\n" + '    #name h1{' + "\n" + "      font-family: 'Brush Script MT', cursive;" + "\n" + '      color: #FF7E04;' + "\n" + '      text-align: center;' + "\n" + '      font-size: 40px;' + "\n" +'    }' + "\n" + '    #programmer{' + "\n" + '      text-align: center;' + "\n" + '      padding-top: 20px;' + "\n" + '    }' + "\n" + '    #programmer img{' + "\n" +'      border-radius: 50%;' + "\n" + '    }' + "\n" + '    fieldset{' + "\n" + '      text-align: center;' + "\n" + '      overflow: hidden;' + "\n" + '      padding: 10px;' + "\n" + '      margin: 10px;' + "\n" + '      border: 5px solid gray;' + "\n" + '      color: #45018D;' + "\n" + '      font-size: 18px;' + "\n" + '      font-family: serif;' + "\n" + '    }' + "\n" + '    fieldset legend{' + "\n" + '      color: #FF7E04;' + "\n" + '      font-size: 25px;' + "\n" + '    }' + "\n" + '  </style>' + "\n" + '</body>' + "\n" + '</html>'
with open("index.html", "a") as save:
    save.write(html)
