<html lan="en">
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="mainWebsite.css">
    </head>
    <body>
        <nav>
            <ul class="topnav" id="dropdownclick">
                <li><div class="icon">
                        <img src="fotos/logo.png">
                    </div>
                </li>
                <div class="container">
                    <li><a href="#home">Trainingsplan</a></li>
                    <li><a href="#news">Ernährungsplan</a></li>
                    <li><a href="#about">Produkt Analyse</a></li>
                    <li class="topnav-right"><button class="loginbtn"> <a href="ueberUns.html">Sign in</a></button></li>
                    <li class="dropdownicon"><a href="javascript:void(o);"onclick="dropdownmenu()">&#9776;</a></li>
                </div>
            </ul>
        </nav>    
        <div class="box">
            <div class="row">
                <div class="col-7">
                    <div class="box boxslider">
                        <div class="maindiv"></div>
                    </div>
                </div>
                <div class="col-5">
                    <div class="box boxarticle">
                        <article>
                            <p>Mit unserer App wollen wir den Alltag gesünder Strukturieren. Es soll dem Menschen ermöglichen neue Blickwinkel auf Training und Ernährung zu finden durch unsere Diät-Angebote und Trainingspläne. Ebenso soll es Menschen mit Unverträglickeiten helfen alternativen zu finden.
                            </p>
                        </article>
                    </div>
                </div>
            </div>
        </div>
        <div class="box" id="section-1-gradient">
            <div class="row">
                <div class="col-6">
                    <div class="leftside-col">
                        <h1 class="Large">Weil uns Ihre <br>Gesundheit wichtig ist.</h1>
                    </div>
                </div>
                <div class="rightside-col vidiocontainer">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/z7iWZ24NXQQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>
        </div>
        <div class="box header">
            <header>
                <h1 class="section2header"> The secret for a healthy Life</h1>
            </header>
            <div class="row">
                <div class="col-4">
                    <div class="box qa">
                        <label>Trainingsplan </label>         
                        <p>----------</p>
                        <button class="learnmore">Learn More</button>
                    </div>
                </div>
                <div class="col-4">
                    <div class="box qa">
                        <label>Ernährungsplan</label>         
                        <p>----------</p>
                        <button class="learnmore">Learn More</button>
                    </div>
                </div>
                <div class="col-4">
                    <div class="box qa"> <label>produktanalyse</label>         
                        <p>----------</p>
                        <button class="learnmore">Learn More</button>
                    </div>
                </div>
            </div>
        </div>
    <div class="box footsy">
        <div class="row">
                <div class= "col-3 mobile">
                    <div class="box ahmadbox">
                        <artickle>
                        <h1>Ahmad Gadoura</h1>
                            <ul>
                                <div class="personalfhoto">
                                    <img src="fotos/ahmad%20(4).jpg">
                                </div>
                                <li>Front-end Developer</li>
                                <li>HTML5/CSS/<br>Javascript.</li>
                                <li><a href="Lebenslauf/Ahmad_Gadoura_lebenslauf.html">Lebenslauf</a></li>
                            </ul>
                        </artickle>
                    </div>
                </div>
            <div class= "col-3 mobile">
                <div class="box Ahmadbox">
                    <h1>Ahmad Hazim</h1>
                        <ul>
                            <div class="personalfhoto">
                            <img src="fotos/hazim.jpg">
                            </div>
                            <li>Front-end Developer</li>
                            <li>HTML5/CSS.</li>
                            <li><a href="#le">Lebenslauf</a></li>
                        </ul>
                </div>
            </div>
            <div class= "col-3 mobile">
                <div class="box erginbox">
                    <h1>Ergin<br> Göksu</h1>
                        <ul>
                             <div class="personalfhoto">
                            <img src="fotos/ergin.jpg">
                            </div>
                            <li> Back-end Developer</li> <li>HTML5/CSS/<br>Javascript.</li>
                            <li><a href="#le">Lebenslauf</a></li>
                        </ul>
                </div>
            </div>
            <div class= "col-3 mobile">
                <div class="box michabox">
                    <h1>Michael Volz</h1>
                        <ul>
                            <div class="personalfhoto">
                            <img src="fotos/micha.png">
                            </div>
                            <li>Front-end Developer</li>
                            <li>HTML5/CSS.</li>
                            <li><a href="#le">Lebenslauf</a></li>
                        </ul>
                </div>
            </div>
        </div>    
    </div>
    
    
    
    
  
    
    
    
        <script>
            function dropdownmenu()
            {
                var x= document.getElementById("dropdownclick");
                if(x.className === "topnav")
                    {
                        x.className += " responsive";
                        /*change topnav to topnav.responsive */ 
                    }else
                    {
                        x.className = "topnav"               
                    }
            }    
        </script>  
    </body>
</html>
