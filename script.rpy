# Definieren von Charakter Aussehen.
# Hauptcharakter
#image Thomas normal = "thomas_normal.png"
#image Thomas happy = "thomas_happy.png"
#image Thomas questioningly = "thomas_questioningly.png"

#image Thomas normal = "charakter/thomas_normal.png"
#image Howard normal = "charakter/howard_normal.png"
#image Cameron normal = "charakter/cameron_normal.png"
#image Towers normal = "charakter/towers_normal.png"
#image Stratter normal = "charakter/stratter_normal.png"
#image Scientist normal = "charakter/scientist_normal.png"

# Definieren von Charakteren.
# Terrestrians = BLAU
# Kworrhonians = GELB
# Charaktere aus dem Jahr 2017
define how = Character('Howard', color="#87cefa")
define cam = Character('Cameron', color="#e0ffff")
define us1 = Character('Junger Wissenschaftler', color="#aeeeee")
define us2 = Character('Archäologe', color="#4876ff")

# Charaktere aus dem Jahr 2217
define of1 = Character('Offizier', color="#87ceeb")
define of2 = Character('Offizier', color="#6ca6cd")

define pil = Character('Pilot', color="#191970")
define cop = Character('Copilot', color="#bcd2ee")

define stu = Character('Student', color="#668b8b")

# Hauptcharaktere
define kat = Character('Kathrin Stratter', color="#22ffff")
define tow = Character('Major Towers', color="#4682b4")

define jav = Character('Ja´Vhoc', color="#cdad00")
define nev = Character('N´Evac', color="#ffc125")
define anj = Character('An´Jhot', color="#fffacd")

define mit = Character('Lieutenant Mitchel', color="#20b2aa")
define reg = Character('Lieutenant Commander Reagan', color="#c6e2ff")
define eva = Character('Offizier', color="#7ecoee")
define nak = Character('Lieutenant Nakamura', color="#afeeee")

define har = Character('Paxton Harris', color="#b0e0e6")
define ens = Character('Offizier', color="#9ac0cd")
define sol = Character('Chefingenieur Solano', color="#7ac5cd")

# Hauptcharakter Captain Thomas
define cap = Character('Ich', color="#8b4789")


# Hier beginnt das Spiel.
label start:

    # Musik einspielen: Spannung im Prolog aufbauen
    play music "audio/ambience_music.mp3"

    # Prolog
    scene black
    with fade

    "{b}Wir schreiben das Jahr 2217 nach Christus.{/b}"

    scene ship_1
    with dissolve

    "Die Menschen (Terrestrians) gündeten zusammen mit einer außerirdischen Spezies, den Kworrhonians eine gemeinsame Föderation."
    "Den ersten Krieg hat unsere Föderation soeben überstanden."
    "Inmitten der Spannungen der Allierten, die aus Territoriumsstreitfragen nach dem Krieg hervorgehen, taucht eine Botschaft aus dem Jahre 2017 auf."
    "Diese zeigt wie die gesamte Erde von einem schwarzen Loch verschlungen wird."
    "Um das Rätsel der mysteriösen Botschaft zu entschlüssel, werden 2 Schiffe, die Phoenix und die S'Epazit, mithilfe der fortgeschrittenen Technologie der Kworrhonians in die Vergangenheit geschickt."
    "Dort stößt man auf archäologische Ausgrabungen unter einer bekannten Kultstätte."
    "Mein Name ist Christopher Thomas."
    "Ich bin Captain der Phoenix und bin auf Befehl der Föderation für diese Mission auserwählt worden."
    "Als sich in der Vergangenheit das Geheimnis um die vollkommene Vernichtung der Erde zu offenbaren scheint, sieht sich meine Crew einem technisch überlegenden, skrupellosen Feind gegenüber."

    # Teil 1: 3000 v.Ch.
    scene black
    with fade

    "{b}Cira 3000 Jahre vor Christus.{/b}"

    scene ufo_1
    with dissolve

    "Unter dem sternklaren Nachthimmel erstreckt sich eine weite Anhöhe in der Nähe von Amesbury in England."
    "Vom Fuße der Anhöhe ist zu sehen, dass irgendetwas oben auf der Anhöhe das Dunkel der Nacht in langsam wechselnden Farben erhellt."
    "Wie ein großer, immer wieder seine Lichtfarbe ändernder Flutscheinwerfer."
    "Aus einem im dunklen Hintergrund in einiger Entfernung noch zu erahnenden Dorf strömen Menschen geblendet auf die Anhöhe hinauf."
    "Die Menschen laufen, bereits außer Atem, über die weiten Wiesenflächen hin zu der hellen Lichtquelle."
    "Die Gesichter der Menschen werden zunehmend erhellt, indem die Farben immer wieder wechseln."
    "Schließlich erreicht die erste Welle an Herbeilaufenden den höchsten Punkt der Anhöhe, und, wie vom Blitz getroffen, bleiben alle auf einmal stehen."
    "Ihre in wechselndem Bunt gleißend erhellten Gesichter zeigen eine unbeschreibliche Mischung aus schierem Unglauben, einschüchternder Ehrfurcht und überirdischer Begeisterung!"


    # Teil 2: Das Jahr 2017
    scene black
    with fade

    "{b}2017 nach Christus{/b}."

    scene oxford_1
    with dissolve

    #show howard
    "Der imposante Anblick der University of Oxford:"
    "In einem großen und beeindruckend gebauten Hörsaal steht der Dozent, der offensichtlich gerade seine Vorlesung beendet hat, noch hinter dem Rednerpult und packt seine Unterlagen zusammen."
    "Als ein zweiter Mann durch einen seitlichen Eingang, unweit des Rednerpultes, den Hörsaal betritt und auf den Dozenten zu tritt."

    #show cameron
    cam "Professor Howard, ich freue mich, Sie noch anzutreffen!"
    how "Dekan Cameron, die Freude ist ganz auf meiner Seite – danke, dass Sie noch die Zeit für mich gefunden haben!"

    "Die beiden Männer schütteln einander die Hand."

    cam "Sie belieben zu scherzen, Professor. In Anbetracht der Tragweite Ihrer Forschungen für die Wissenschaft und den Beitrag zu unserer Kultur gehört die Unterredung mit Ihnen zu meinen Top-Prioritäten."
    how "Das ist sehr großzügig von Ihnen, Dekan."

    scene oxford
    with dissolve

    "Die beiden begeben sich durch den Seiteneingang nach draußen."
    "Zwischen den alten Mauern der Gebäude gehen beide durch die schöne, parkähnliche Anlage."

    cam "Bezüglich der Erbauung sind sich die Historiker sehr uneinig."
    cam "Neueste Forschungen legen ein Alter von möglicherweise mindestens 11 000 Jahren nahe, während man noch vor Jahrzehnten von nur 5 000 Jahren ausging."
    #show howard happy
    how "Es ist immer wieder unser Problem, dass wir in der Geschichte nur erforschen können, worüber es Aufzeichnungen gibt."
    #show cameron happy
    cam "Solange Sie mich nicht um finanzielle Mittel zur Unterstützung einer Zeitreise fragen wollen, Professor."
    #show howard laught
    how "Nein, nein, Dekan: ich bitte Sie nur um finanzielle Unterstützung für seriöse Unterfangen."
    #show cameron laught
    cam "Also, Professor, worum geht es Ihnen genau?"

    scene office_1
    with dissolve

    "Sie betreten das Büro des Professors in einem anderen Gebäudeflügel auf dem Campus."

    #show howard normal
    #show cameron normal
    how "Seit der Entdeckung der unterirdischen Steinreihe unter einem Teil der Durrington Walls ist die Ebene von Salisbury erneut in den Fokus historischer Forschungsinteressen gerückt."
    cam "Was brauchen Sie, Professor: Bodenradar, Magnetometer? Bekommen Sie finanziert – kein Problem!"
    #show howard happy
    how "Nun, Dekan, eigentlich dachten meine Arbeitsgruppe und ich da an ein etwas invasiveres Vorgehen."
    #show cameron laught
    cam "Sie wollen selbst da rein? Grabungen? Im Ernst?"
    #show howard laught
    how "Zurück zu den Ursprüngen der Archäologie!"


    # Teil 3: Das Jahr 2017, 6 Monate später
    scene black
    with dissolve

    "{b}6 Erdenmonate später, Ebene von Salisbury, England:{/b}."

    scene camp
    with dissolve

    "Inmitten der weiten Wiesenflächen ist ein großes Lager aus Zelten, Wohnwagen und Blechhütten aufgeschlagen."
    "Es herrscht unruhiges, aber geordnetes Treiben unter den Archäologen."

    #show howard
    #show user1
    "Aus einem der Zelte tritt gerade Professor Howard zusammen mit einem jungen Wissenschaftler heraus, dem er folgt."

    us1 "Gemäß unseren neu gewonnenen Datierungen gehen die unterirdischen Bauten auf ca. 3 000 Jahre vor Christus zurück, Professor."
    how "Das bestätigt unsere bisherige überarbeitete Theorie."
    us1 "Die ganze Architektur ist um diese zentrale Kammer ausgelegt."

    "Der junge Mann weist auf dem Tablet, das er mit sich trägt, auf die schematische Skizze der unterirdischen Gänge."

    how "Ja, was auch immer darin verborgen sein mag, hat die Menschen offensichtlich zum Bau dieser gesamten Kultstätte bewegt."

    "Indem die beiden in einen offenkundig in den Boden gebohrten Tunnel steigen, sind im Hintergrund auf den Wiesenflächen etwas weiter weg einige große Steinformationen zu erahnen."

    #show howard
    how "Und heute werden wir endlich sehen, was sich in der Kammer befindet!"
    #show user1
    us1 "Die Infraschall-Emitter sind gemäß den Berechnungen mit absoluter Präzision justiert und platziert, Professor."
    how "Dann lassen Sie uns damit beginnen, erneut Geschichte zu schreiben!"

    "Sie gelangen durch die ausgeleuchteten Bohrtunnel vorbei an imposanten Steinbildnissen und Monolithanordnungen hin zu einem schweren Felsen, der das Ende des Bohrtunnels markiert."
    "Rings herum sind verschiedene Geräte und Instrumente angebracht worden."

    us2 "Alles ist genauestens vorbereitet, Professor. Die wiederholten Simulationen waren alle erfolgreich."

    "Howard und der Archäologe, der ihn hergeleitet hat, bekommen Ohrschützer und Atemschutzmasken entgegen gereicht."

    how "Lassen Sie uns in die Vergangenheit ans Licht bringen!"

    "Die Archäologen nehmen den markierten Sicherheitsabstand zu dem großen Felsblock ein, und dann werden auf Professor Howards Nicken hin die angebrachten Infraschall-Emitter synchron aktiviert."
    "Ein kurzes Brummen, das sogleich so tief wird, dass man es nicht mehr hören kann, und Augenblicke später beginnt das Gestein rund um den Felsblock herum zu Boden zu rieseln."
    "Schließlich bekommt der Felsblock zahlreiche Risse und bricht dann sachte in Form unendlich vieler kleiner Steinchen völlig in sich zusammen."
    "Als sich der Staub gelegt hat, treten Professor Howard und die anderen Archäologen langsam durch die entstandene Öffnung, aus der nach wie vor zahlreiche kleine Steinchen zu Boden rieseln."
    "Sie betreten einen großen unterirdischen Hohlraum, in dessen Wänden teilweise Metallstücke stecken."
    "Howard bleibt ungläubig wie erstarrt stehen, indem er weiter nach vorn in den Hohlraum hinein blickt: sein Gesicht wird von sich fließend verändernden Farben geblendet."

    #show howard shocked
    scene black
    with fade

    how "Oh, mein..."

    "Inmitten der großen Monolithen des Stonehenge tut sich plötzlich ein Loch im Boden auf, in das immer mehr Erdreich nachrutscht, so dass sich der Rand des Loches zunehmend ausbreitet."
    "Schließlich stürzen die gewaltigen Steinblöcke des Stonehenge in der Mitte zusammen und werden ebenfalls in das sich immer noch vergrößernde Loch gerissen."

    scene blackhole
    with dissolve
    # ??? kürzen
    "Aus dem Weltraum ist das gewaltige, alles verschlingende Loch zu erkennen, das sich von Großbritannien ausbreitet und in weniger als zehn Sekunden den gesamten Planeten Erde vollständig verschlingt."
    "Bis nur noch ein schwarzes Nichts an dieser Stelle im Sonnensystem übrig bleibt, und der die Erde eigentlich umkreisende Mond im zunehmend enger kreisenden Spiralflug immer weiter beschleunigt wird."
    "Bis er zerberstend in das schwarze Nichts hinein stürzt und plötzlich vollkommen verschwunden ist!"
    "Ein metallenes, kugelförmiges Objekt mit mehreren Antennen, das vor dem Hintergrund des nachtschwarzen Sternenhimmels im Weltraum schwebt, blinkt an einer Stelle in regelmäßigen Intervallen grün auf."

    scene black
    with fade

    # Teil 4: Das Jahr 2217
    scene spaceship
    with dissolve

    "{b}2217 nach Christus{/b}."

    "Inmitten der absoluten Leere des Weltalls schwebt eine langsam rotierende Raumstation mit einem zylindrischen Rumpf, der sich über etliche Decks erstreckt, und mehreren Ausläufern, die vom zylindrischen Rumpf weg ragen"
    "Auf der Außenhülle ist groß die Registratur Science Base D12 zu lesen."
    "In der Kommunikationszentrale der Raumstation sitzen zwei Offiziere in dunklen Uniformen vor den zahlreichen futuristischen Computerterminals, Kontrollen und Monitoren."

    #show officer1 normal
    #show officer2 normal
    of1 "Ich empfange hier ein eingehendes Signal."
    of2 "Registrierungscode des Senders?"
    of1 "Kein Registrierungscode?"
    of2 "Negativ: es wird auf einer Hyperspace-Trägerwelle gesendet."
    of1 "Negativ: die Transmission scheint sogar sehr tief aus dem Hyperspace gesendet worden zu sein."
    of2 "Na gut, sehen wir´s uns mal an!"
    #show officer1 shocked
    #show officer2 shocked

    "Die beiden drehen sich zu einem der holografischen Bildschirme, auf dem in dieser Sekunde die Bildübertragung von der vollständigen Implosion der Erde ins scheinbare Nichts mitzuverfolgen ist."

    scene black
    with fade

    # Teil 5: Das Jahr 2217, eine Woche später
    scene speed_of_light
    with dissolve

    "{b}Eine Erdenwoche später{/b}."

    "Ein kleines Raumschiff, dessen Form an ein Space Shuttle erinnert, fliegt durch eine Art von hochenergetischem Tunnel, dessen schnell vorbei rasende Wände aus grünen Blitzen zu bestehen scheinen."
    "In der Steuerzentrale sitzen ein Mann und eine Frau in zweiter Reihe hinter dem Piloten und Copiloten: ihre Uniformen und Rangabzeichen zeigen, dass sie aus verschiedenen Teilstreitkräften stammen."

    #show pilot normal
    pil "Wir werden Kworrhonian Starbase Rha´Acul in zehn Minuten erreichen, Commander, Major."

    "Beide nehmen dies mit einem Blick zur Kenntnis."

    #show stratter normal
    #show tower normal
    kat "Dann werden wir eine fundierte Einschätzung erhalten."
    tow "Ja, wir profitieren sehr von den uns überlegenen wissenschaftlichen Fertigkeiten der Kworrhonians."
    kat "In der Tat. Ich wünsche mir sehr, dass die aktuellen Territoriumsstreitfragen in einem beide Seiten zufriedenstellenden Kompromiss gelöst werden."
    tow "Das werden sie mit Sicherheit, Commander."
    tow "Nach einem als Alliierte geführten und gemeinsam gewonnen Krieg sind derartige Territoriumsstreitfragen eine natürliche Konsequenz – wir werden sie mit der Zeit klären."
    kat "Das wünsche ich mir sehr, Major – im Geiste unserer Föderation."


    "Ein paar Minuten später verlässt das Raumschiff den hochenergetischen Tunnel und tritt in den Weltraum aus."

    scene base
    with dissolve

    "Es befindet sich im Anflug auf eine überdimensional große, düster erscheinende Raumstation."
    "Diese besteht aus zwei großen Segmenten oben und unten, die hauptsächlich aus dunklen Panzerplatten bestehen, zwischen denen in einigen Abständen blaues Licht erstrahlt."
    "Beide Segmente werden durch einen langen Teil miteinander verbunden, der an eine unregelmäßig verformte Dreieckssäule aus dunklen Panzerplatten erinnert."


    pil "Wir haben den Hyperspace verlassen und befinden uns im Anflug auf Kworrhonian Starbase Rha´Acul"
    #show copilot normal
    cop "Wir haben von den Kworrhonians soeben Landeerlaubnis in Hangar 3 erhalten."

    "Das Raumschiff bewegt sich langsam auf ein Schott am unteren Segment der Raumbasis zu, als dieses sich öffnet und das Raumschiff ins Innere schweben kann"

    pil "Wir treten jetzt in die künstliche Gravitation ein."

    "Das Raumschiff hat beim Eintritt in den Hangar die senkrecht ausgerichteten Positionstriebwerke gezündet, die es zunächst stabilisiert haben und nun langsam auf den Boden des Hangars sinken lassen."
    "Im Hintergrund schließt sich das Schott in den Weltraum wieder, und mit einem Zischen wird der Hangar wieder mit Luft gefüllt."
    "Mit zunehmendem Druckanstieg wird das Zischen immer lauter hörbar, bis es dann langsam wieder abebbt."

    scene hangar
    with dissolve

    pil "Atmosphäre im Hangar ist wiederhergestellt."

    "Auf ein Nicken hin, wird die hintere Wand des Schiffes ähnlich wie eine antike Zugbrücke langsam nach außen geöffnet und sinkt als kleine Rampe bis auf den Boden des Hangars."
    "Indem die beiden Offiziere das Schiff über die kurze Rampe verlassen, öffnet sich am gegenüberliegenden Ende die doppelt versiegelte Drucktür zum Hangar, und vier Offiziere der Kworrhonians betreten den Hangar."
    "Zwei bleiben links und rechts von der Tür stehen, während die beiden anderen zum gelandeten Raumschiff weitergehen."
    "Die Kworrhonians gleichen beinahe den Terrestrians, außer dass von ihrer Stirn aus ein grüner Bogen senkrecht nach unten läuft."
    "Der Bogen der sich oberhalb der Nase in zwei Bögen aufgabelt."
    "Welcher sich nach links und rechts unterhalb der Augen bis zu den Ohren weiter verlaufen und anschließnd in einem weiteren Bogen zurück unter dem Mund wieder zusammenlaufen."

    #show javhoc normal
    #show nevac normal
    jav "Commander Stratter, Major Towers, willkommen an Bord von Kworrhonian Starbase Rha´Acul."
    jav "Ich bin Captain Ja´Vhoc, der Stationskommandant, und dies ist mein leitender Wissenschaftsoffizier, Lieutenant Commander N´Evac."
    tow "Wir danken Ihnen, Captain Ja´Vhoc."
    kat "Ebenso für Ihre Unterstützung bei der Auswertung, Captain."
    jav "Meine Wissenschaftsabteilung hat gern bei der Auswertung geholfen, Commander, Major. Das ist wohl die beste Gelegenheit, gleich in medias res zu gehen."

    "Towers und Stratter nicken zustimmend."

    nev "Wenn Sie mir bitte folgen wollen, Commander, Major."

    "N´Evac hat Commander Stratter und Major Towers in ein großes wissenschaftliches Labor geführt, dessen eher dunkle Atmosphäre durch leuchtend grünes Neonlicht aus verschiedenen Röhren, Leitungen und Apparaturen erhellt wird."

    scene comander
    with dissolve

    #show N´Evac normal
    nev "Wir stufen die Hyperspace-Nachricht als authentisch ein."
    nev "Dafür sprechen die harmonische Schwingungsanalyse der Hyperspace-Trägerwelle sowie die spektografische Analyse der elektromagnetischen Hintergrundschwingungen aus der Bildmitteilung selbst."
    nev "Der mitgesendete Time-Index stuft den Sender des Signals im Jahre 2017 ein."

    #show Stratter _
    #show Towers _
    nev "Es spricht nichts mehr dagegen, dass, wer auch immer diese Nachricht geschickt hat, Zeuge davon war, wie die Erde im Jahre 2017 von einer Quantensingularität verschlungen wird, die offensichtlich in ihr selbst erzeugt worden ist."
    tow "Wie um alles in der Welt kann inmitten eines Planeten ein schwarzes Loch erzeugt werden?"
    kat "Und wer filmt das Ganze und schickt es zu uns?"
    nev "Die Art und Weise, wie die Nachricht auf einer Hyperspace-Trägerwelle zu uns gesendet worden ist, lässt mit großer Sicherheit darauf schließen, dass beabsichtigt worden ist, dass wir sie empfangen sollten."
    tow "Wie kann man denn in der Vergangenheit beabsichtigen, eine Nachricht 200 Jahre in die Zukunft zu schicken?"

    "Wie kann man denn in der Vergangenheit beabsichtigen, eine Nachricht 200 Jahre in die Zukunft zu schicken?"

    nev "Stellen wir uns den Weltraum vereinfacht als diese Fläche vor. Nehmen wir an, Sie wollen von dem Punkt links unten zum Punkt links oben gelangen."
    nev "Bei einer Reise durch den Weltraum müssten Sie so reisen."

    "N´Evac veranschaulicht den Kurs im holografischen Bild durch eine senkrechte rote Linie von links unten nach links oben."

    nev "Reisen Sie dagegen durch den Hyperspace, haben Sie eine deutliche Abkürzung genommen."

    "Das holografische Rechteck wird zu einem Zylinder gekrümmt, sodass die beiden Ecken links unten beziehungsweise links oben jetzt genau aneinander liegen."

    tow "Ja, ja, uns ist das Prinzip der Hyperspace-Reisen bekannt, Commander, aber wir reden hier ja übe reine Zeitreise der Nachricht."
    nev "Ganz recht, Major. Stellen Sie sich vor, die Hochachse dieses Rechtecks beschreibt Ihre Reise im Raum und die Rechtsachse Ihre Reise in der Zeit!"
    #Towers´ Gesichtsausdruck zeigt, dass er zu verstehen beginnt.
    nev "Eine Reise von links unten nach rechts oben beschreibt eine zurückzulegende Entfernung im Raum und eine Reise in die Zukunft."
    nev "Im normalen Weltall sind Raum und Zeit aneinander gekoppelt, aber reisen nun Sie hier durch den Hyperspace..."

    "Im holografischen Bild werden nun die Ecke links unten und die Ecke rechts oben aneinander gelegt."

    kat "... dann gelangen wir nicht nur innerhalb kürzester Zeit an einen anderen Ort, sondern auch in eine andere Zeit."
    #N´Evac grinst vor offenkundiger wissenschaftlicher Begeisterung
    nev "Wenn Sie den Terminus innerhalb kürzester Zeit hier überhaupt noch sinnvoll verwenden dürften – jedenfalls wird es Ihnen als Reisender exakt so vorkommen."
    kat "Ich erinnere mich, von dieser Theorie in der Schule einmal gehört zu haben."
    tow "Den Weltraum mit einem Rechteck zu vergleichen, kennen wir wohl alle aus der Schule."
    kat "Unser Science Teacher verwendete damals ein Blatt Papier."
    tow "Ihre Schule hat noch mit Papier gearbeitet?"
    kat "Ich war an einer Biosphären-Habitats-Schule."
    tow "Verstehe – sehr naturverbunden. Ich hoffe nur, Sie haben kein Problem mit orthoplanaren Hyperwinkeln!"
    kat "Sehr amüsant, Major."
    tow "Entschuldigen Sie bitte."
    kat "Aber da ist immer noch ein Fehler in der Theorie, Commander."
    kat "Wenn die Erde im Jahre 2017 vernichtet wurde und das Signal uns dies bestätigt, wie kann es sein, dass wir von der Erde aus hierher gekommen sind? Sie existiert noch!"
    tow "Genau, daran erinnere ich mich jetzt: dieses verflixte Paradoxon bei jeglicher Art von Zeitreise. Es läuft immer auf so etwas hinaus!"
    nev "Eigentlich überhaupt nicht, das hatte man nur sehr lang in der Temporalphysik geglaubt."
    nev "Es führte dazu, dass die Wissenschaft sogar ernsthaft die Möglichkeit von Zeitreisen anzweifelte – eben aus exakt diesem Grunde."
    nev "Die Lösung für dieses vermeintliche Paradoxon lieferte die Multiversum-Theorie."

    "Abermals tippt N´Evac etwas in die Tastatur, woraufhin in dem holografischen Bild die rechteckige Fläche vervielfacht wird."
    "Alle diese identisch aussehenden Rechtecke sind wie ein Büschel aus Papierseiten in der linken unteren und rechten oberen Ecke miteinander verbunden."

    nev "Angenommen, es gibt für jede einzelne Sekunde unendlich viele Möglichkeiten, was als nächstes passieren kann, und jede einzelne Möglichkeit existiert in einem aus der vorherigen Überlagerung hervorgehenden Universum."
    nev "Nun wird im Jahre 2017 bei der Zerstörung der Erde eine Nachricht durch den Hyperspace gesendet."
    kat "Dann könnte es passieren, dass die Nachricht den Hyperspace an Ort und Zeitpunkt verlässt wie vorgesehen, allerdings in einem anderen, parallel existierenden Universum."

    "Die rote Linie in der Projektion, die den Raum-Zeit-Kurs der Nachricht darstellt, verläuft von der linken unteren Ecke des einen Rechtecks in die rechte obere Ecke eines anderen Rechtecks."
    "Beide Ecken sind direkt miteinander verbunden sind."

    nev "Exakt: nämlich hier bei uns, wo die Erde eben nicht zerstört worden ist."
    tow "Okay, okay, das kann ich soweit nachvollziehen, Commander. Aber wenn ich das jetzt richtig verstanden habe, stammt die Nachricht aus einem anderen Universum und betrifft uns eigentlich gar nicht."
    nev "Wie gesagt, legt alles die Schlussfolgerung nahe, dass beabsichtigt wurde, dass wir diese Nachricht empfangen sollten."
    kat "Ein Hilferuf... aus unserer eigenen Vergangenheit."
    #Towers runzelt seine Stirn, indem sich langsam sein Blick mit dem von Stratter trifft.
    tow "Sie denken auch an den Darwin-Zwischenfall?"
    kat "Es ist nie vollständig aufgeklärt worden, was mit dem Schiff geschehen ist."
    #Towers und Stratter wenden beide ihre fragenden Blicke an N´Evac.
    nev "Leider lässt die Nachricht keine weiteren Rückschlüsse auf ihren Sender zu, allerdings wäre die Hypothese, dass sie von der Darwin geschickt worden ist, die einzige, die wir erklären könnten."
    kat "Also eine Nachricht aus unserer eigenen Vergangenheit von jemandem in einer parallelen Zeitlinie, der Zeuge war, wie die komplette Erde ausgelöscht wird."
    kat "Eine Nachricht, die allem Anschein nach absichtlich an uns gerichtet worden ist und vielleicht von der verschollenen Darwin stammt."
    tow "Wir sollten die Nachricht als Hilferuf auffassen, der gezielt an uns gerichtet worden ist."

    "N´Evac nickt Towers und Stratter langsam zu."

    #Teil 7: Zwei Erdentage später, Planet Erde
    scene city_1
    with dissolve

    "{b}Zwei Erdentage später, Planet Erde{/b}."

    #show Thomas normal
    "Inmitten der Skyline einer futuristischen Metropole erhebt sich ein Gebäude mit zahlreichen Stockwerken, das die umliegenden Häuser um ein Vielfaches überragt und sich inmitten einer verzweigten Anlage befindet, die aus weiteren Gebäuden, Parks, einem offenkundigen Landeplatz für Raumfähren, Energieversorgungsstationen und -leitungen sowie zahlreichen Verbindungsstraßen dazwischen verfügt."
    "Ein dunkelhaariger Mann mit gepflegtem Vollbart überquert den großen Platz vor dem Gebäude und verschwindet durch eine große, sich automatisch öffnende Glasschiebetür."
    #show Ensign normal
    "Im Erdgeschoss des Gebäudes tritt dem Mann ein Offizier in Uniform entgegen."

    ens "Willkommen zurück in den Terrestrian Federation Headquarters, Captain Thomas! Wenn Sie mir bitte folgen – der Admiral erwartet Sie bereits."

    "Die beiden Männer gelangen zu einem Aufzug, mit dem sie einige Stockwerke hinauffahren, um anschließend in einen Gang zu gelangen, von dem viele geschlossene Türen abgehen."
    "Zur Zierde stehen in den Ecken tropisch oder zum Teil nicht irdisch anmutende Pflanzen sowie Gemälde verschiedener Planeten und offensichtlich deren fremdartig erscheinender Flora und Fauna."
    "Am Ende des Ganges klopft der Offizier an einer Tür an und betritt zusammen mit Captain Thomas das große Büro."
    "Ein hochgewachsener, kräftiger Mann mit blondem Haar dreht sich hinter einem großen, futuristischen Schreibtisch zu den beiden Eingetretenen um."

    scene office
    with dissolve

    ens "Admiral Harris, Sir: Captain Thomas ist eingetroffen."
    #show Harris normal
    har "Vielen Dank, Ensign."
    "Der Offizier verlässt das Büro des Admirals wieder."
    "Captain Thomas und Admiral Harris treten aufeinander zu und strecken einander die Hände entgegen."
    #show Harris laught
    har "Es tut gut, Sie zurück im Dienst zu sehen, Christopher."
    #show Thomas normal
    cap "Leider habe ich kaum eine Wahl gehabt, Paxton."
    #show Harris normal
    har "Ich habe gehofft, Ihnen hiermit Ihre Entscheidung abzunehmen."
    cap "Sie sind immer davon ausgegangen, dass ich zurückkehren werde."
    har "Natürlich, Christopher, wir beide wissen doch, dass Sie Ihr Kommando nicht auf Dauer an den Nagel hängen wollten."
    cap "Ehrlich gesagt, bin ich mir da nicht so sicher, Paxton."

    "Admiral Harris bietet Captain Thomas den Stuhl auf dieser Seite des Schreibtisches an, während der Admiral in seinem eigenen Stuhl auf der anderen Seite des Tisches Platz nimmt."

    har "Der Krieg ist eine schwierige Zeit gewesen, aber jetzt muss es weitergehen."
    #show Thomas laught
    cap "Wie ich sehe, sind Sie in Ihren alten Rang zurückgekehrt, Admiral."
    #show Harris laught
    har "Auch ich hatte mich um den Posten als General während des Krieges nicht gerissen – und, wie gesagt, jetzt muss es weitergehen."
    #show Thomas normal
    #show Harris normal
    cap "Ich hatte damals die Offizierslaufbahn eingeschlagen, um meinen Dienst auf Forschungsschiffen auszuüben, nicht um Kampfeinsätze zu kommandieren."
    har "Sie sind ein verdammt guter Kommandant, Christopher! Sie haben sich den Rang des Captains zurecht erworben. Das qualifizierte Sie im Krieg ebenso dazu, Kampfeinsätze zu kommandieren – mit Erfolg!"
    cap "Aber danach hatte ich die Nase voll, Paxton."
    har "Uns allen ging es so, Christopher. Aber jetzt, wo der Krieg vorbei ist, haben wir die Gelegenheit, wieder dort weiterzumachen, wo wir zu Kriegsbeginn aufhören mussten. Jetzt können wir wieder forschen! Und dazu benötigen wir die richtigen Leute auf den richtigen Posten!"
    cap "Ich werd´s wohl nie herausfinden, wenn ich´s nicht einfach tue – nicht wahr, Paxton."
    #show Harris laught
    har "Genau so ist es, Christopher!"
    cap "Also, worum geht es in meinem nächsten Einsatz, Admiral?"
    har "Um eine Aufklärungsmission in unsere Vergangenheit – es geht um das Fortbestehen der Erde!"
    cap "Welches Schiff werde ich kommandieren?"
    har "Es gibt nur ein Schiff, das für Sie in Frage kommt, Captain!"

    scene station_2
    with dissolve

    "Ein Space Shuttle steigt in den Erdorbit auf, in dessen transparenter Cockpitscheibe die blau strahlende Reflexion der überdimensional groß anmutenden Erde vom Spiegelbild einer ebenfalls im Erdorbit befindlichen Raumstation überlagert wird."
    "Die Station sieht aus wie ein großes Rad, in dessen Zentrum sich die Zentrale befindet und dessen peripherer Bereich aus zahlreichen Andockbuchten besteht."
    "Indem nun die Reflexion eines bestimmten der angedockten Schiffe allmählich heranwächst, ist in Christopher Thomas´ Augen – wenn auch seine Mimik reglos bleibt – ein Glänzen zu erkennen."

    #show Harris normal
    har "Hätten Sie etwa an ein anderes Schiff gedacht, Christopher?"

    scene ship_6
    with dissolve

    "Das angedockte Schiff, dem sich das Shuttle genähert hat, hat eine langgezogene, pfeilähnliche und extrem aerodynamische Form, obwohl diese im luftleeren Weltraum gar nicht erforderlich wäre, und weist weitestgehend eine glänzend weiße Farbe auf und an einigen Stellen blaugrüne Segmente."
    "An seiner vorderen Spitze befindet sich eine große Sensorphalanx mit zwei langen Antennenstäben in Flugrichtung, bevor eine großflächige transparente Scheibe anstatt des undurchsichtigen Metalls einen großen Bereich des Schiffes überdeckt."
    "Links und rechts davon zeigen seitlich zwei kleinere Flügel mit Raketentriebwerken weg, bevor der noch größere hintere Teil des Schiffes beginnt, der beinahe Quaderform hat und viele Decks umfassen muss."
    "Von ihm aus ragen links und rechts zwei weitere große Flügel weg, an denen sich große und imposant erscheinende Triebwerke befinden."
    "Beim Überfliegen des Schiffes erscheint auf seiner Oberseite seine Registratur: Federation Star Ship Phoenix."
    "Zwei metallene Schleusentüren gleiten automatisch beiseite, als Captain Thomas und Admiral Harris dahinter eines der Decks an Bord der Phoenix erblicken."
    "Eine junge, rothaarige Frau salutiert sogleich."

    scene comander_4
    with dissolve

    #show Reagan normal
    reg "Admiral Harris, Captain Thomas, willkommen an Bord der Phoenix. Ich bin Lieutenant Commander Reagan, Chefin der Sicherheit."
    #show Harris normal
    har "Vielen Dank, Commander."
    #show Thomas normal
    cap "Rühren, Commander. Ich danke Ihnen."
    reg "Ich vermute, Sie möchten umgehend der Brückencrew vorgestellt werden und Ihr Kommando antreten, Captain?"
    cap "So ist es, Commander."
    reg "Dann folgen Sie mir bitte, Captain, Admiral!"

    "Ein zufriedenes Lächeln umspannt Paxtons Lippen, indem er Christopher und Reagan zum nächsten Aufzug folgt: von diesem Korridor aus hat man keinerlei Blick nach draußen, alles ist lediglich von metallen Wänden umgeben."
    "Ebenso sieht es in der Aufzugkabine aus, bis auf die Wandsteuerkonsole."

    reg "Ihr erster Offizier Commander Stratter befindet sich bereits an Bord von Kworrhonian Starbase Rha´Acul, Captain."
    har "Commander Stratter hatte Major Towers begleitet, um die Auswertung der Kworrhonians entgegenzunehmen."

    scene spaceship_2
    with dissolve

    "Der Aufzug hält an, und die automatischen Türen öffnen sich erneut."
    "Dahinter bietet sich der Anblick der imponierenden Brücke der Phoenix: Die gesamte Decke besteht aus einer großen transparenten Scheibe, durch die man einen überwältigenden Blick in den Weltraum hinaus hat."
    "Am vorderen Ende der Brücke befindet sich ein großer holografischer Bildschirm, vor dem sich die Station des Steuermanns befindet."
    "In der Mitte der Brücke befinden sich zwei Kommandositze mit Schaltkonsolen in den Armlehnen."
    "Links und rechts befinden sich in jeweils einer Nische mit zahlreichen Bedienelementen die Wissenschaftsstation und die taktische Station."
    "Von der Brücke gehen vier Türen ab: vorne in Blickrichtung links in ein kleines Büro für den kommandierenden Offizier."
    "Vorne rechts befindet sich eine kleine Andockschleuse für Notfälle."
    "Auf der Rückseite der Brücke befindet sich zentral eine Tür, die auf demselben Deck nach Achtern führt."
    "Die Tür zum horizontalen Aufzug, mit dem Reagan, Harris und Thomas zur Brücke gebracht hat, befindet sich, von den Kommandositzen aus betrachtet, hinten links in einer kleinen Seitennische."

    reg "Willkommen auf der Brücke, Admiral, Captain!!"

    "Die übrigen zwei Offiziere auf der Brücke stehen sofort stramm an ihren Stationen, der Wissenschaftsstation links von Christopher beziehungsweise der Steuerkonsole im vorderen Teil der Brücke."

    cap "Ich bin Captain Christopher Thomas. Ich übernehme mit sofortiger Wirkung das Kommando über die F.S.S. Phoenix."
    cap "Admiral Harris wird uns zur Kworrhonian Starbase Rha´Acul begleiten."

    "Paxton nickt der Brückencrew in einer kurzen Begrüßungsgeste zu."
    "Lieutenant Commander Reagan fordert mit ihrem Blick die Brückenoffiziere auf, sich vorzustellen."

    #show Nakamura normal
    nak "Lieutenant Nakamura, leitender Wissenschaftsoffizier der Phoenix, Sir."

    #show Mitchel normal
    mit "Lieutenant Mitchel, Sir. Steuermann der Phoenix."

    "Christopher signalisiert seinen Offizieren, wieder an ihren Stationen Platz zu nehmen, während er selbst und Paxton sich auf die beiden Kommandositze in der Mitte der Brücke setzen."

    mit "Lösen der Andockklammern und Aktivieren der Triebwerke auf Ihr Kommando, Captain."
    cap "Kommando hiermit erteilt, Lieutenant."
    mit "Aye, Sir."

    scene speed_of_light
    with dissolve

    "Die Phoenix dockt von der Raumstation ab und beschleunigt auf ihren Kurs von der Erde weg: auf ein helles Aufleuchten der Achtertriebwerke hin wird das komplette Raumschiff von einem urplötzlich auftauchenden hochenergetischen Tunnel verschlungen, der genauso abrupt und ohne eine Spur zu hinterlassen wieder verschwindet."
    "Über der Brücke bietet sich überall durch die transparente Decke hindurch der Anblick des von grünen Blitzen durchzogenen hochenergetischen Tunnels."

    mit "Eintritt in den Hyperraum erfolgreich, steuern die programmierten Koordinaten wie vorherberechnet an, Captain."
    cap "Verstanden, Lieutenant."

    #show Thomas normal
    #show Harris normal
    cap "Paxton, wie ist unser Verhältnis zu den Kworrhonians jetzt nach Ende des Krieges?"
    har "Es gibt ein paar Territoriumsstreitfragen, die nach einem Krieg natürlich nicht ausbleiben – aber das werden unsere Politiker zur beiderseitigen Zufriedenheit regeln."
    cap "So ungern ich an den Krieg zurückdenke, so wertvoll sind aber die Kworrhonians als unsere Alliierten gewesen."
    har "Definitiv: Ohne ihren technologischen Vorsprung, den sie uns zuteil werden ließen, hätten wir den Krieg voraussichtlich nicht gewinnen können."
    cap "Oder zumindest hätte er sich noch deutlich länger hingezogen."

    "Paxton steht auf und wechselt nun das Thema."

    har "Captain Thomas, ich werde Sie und Ihre Brückencrew jetzt über die genauen Parameter unserer Mission instruieren."
    #"Während Christopher in seinem Sitz gespannt die Hände faltet, drehen sich Mitchel, Nakamura und Reagan aufmerksam an ihren Stationen zu Admiral Harris."
    har "Vor neun Tagen hat Science Base D12 ein nicht registriertes Signal auf einer Hyperspace-Trägerwelle empfangen, das eine Bildaufzeichnung aus dem Jahre 2016 beinhaltete, das zeigt, wie die Erde vollständig von einer Quantensingularität verschlungen wird!"
    #"Nakamura, Mitchel und Reagan zeigen erschrockene Blicke, während Christopher Paxton, als dieser sich wieder ihm zuwendet, gefasst fest in die Augen sieht: Christophers vergangene Kriegseinsätze haben ihn auf traurige Weise gelehrt, Schreckensnachrichten unbeeindruckt zur Kenntnis zu nehmen und stattdessen strategische Entscheidungen abzuwägen, um Schlimmeres zu verhindern..."


    #Teil 10:

    scene base_2
    with dissolve

    "Kurze Zeit später öffnet sich frontal vor der Phoenix der hochenergetische Tunnel, und der dunkle Weltraum mit den zahlreichen Sternen kehrt zurück: rasendschnell schießt Kworrhonian Starbase Rha´Acul von vorn auf die Phoenix zu und wächst innerhalb von Sekundenbruchteilen von der Größe eines unscheinbaren Punktes im dunklen All in ihre volle imponierende und in gewisser Weise einschüchternde Größe heran."
    "Doch noch vor dem Verstreichen einer Sekunde hat die Phoenix ihre Geschwindigkeit bei Austritt aus dem grün blitzenden Tunnel auf unglaubliche Art und Weise derart verlangsamt, dass sie jetzt mit zum Manövrieren angepasster Geschwindigkeit die Rha´Acul ansteuert."

    #show Reagan normal
    reg "Wir erhalten Andockerlaubnis an Kworrhonian Starbase Rha´Acul, Sir."

    #show Mitchel normal
    mit "Ich bestätige die empfangenen Koordinaten, Captain."

    #show Thomas normal
    cap "In Ordnung, Lieutenant – führen Sie das Andockmanöver aus!"
    mit "Aye, Sir: Andockmanöver wird initiiert."

    "Auf ein Zunicken hin stehen Captain Thomas, Admiral Harris und Lieutenant Nakamura von ihren Sitzen auf und, nachdem Christopher das Kommando an Lieutenant Mitchel übergeben hat, verlassen die drei die Brücke durch die Tür, die anstatt in den Lift auf demselben Deck weiter nach Achtern führt."
    "Der Gang führt mittig über das Deck, so dass keinerlei Fenster nach draußen zeigen, sondern sich stattdessen immer wieder Türen auf beiden Seiten des Korridors befinden."
    "Schließlich biegen die drei durch eine der Türen seitlich ab, die mit der Beschriftung Andockeinheit versehen ist."
    "Die drei gelangen so zunächst in die Andockkontrollkabine, wo zwei diensthabende Offiziere den Andockvorgang vor Ort überwachen und anschließend die Luftschleuse auf korrektes Funktionieren hin überprüfen."
    "Dann wird die Innentür zur Luftschleuse geöffnet, so dass Thomas, Harris und Nakamura die geräumige Luftschleuse betreten können."
    "Die doppelte Schleusentür nach draußen wird unmittelbar darauf entriegelt und unter routinemäßigem Sicherheitsalarm geöffnet, worauf hin auf der anderen Seite ein etwas weniger beleuchteter Korridor an Bord von Kworrhonian Starbase Rha´Acul zum Vorschein kommt."
    "Captain Ja´Vhoc und Major Towers treten Captain Thomas, Admiral Harris und Lieutenant Nakamura hier sogleich entgegen."

    #Captain Ja´Vhoc stellt sich vor, und anschließend begrüßen Towers, Thomas, Harris und Nakamura einander.

    #show Ja´Vhoc normal
    jav "Willkommen an Bord von Starbase Rha´Acul. Ich denke, es ist in Ihrem Interesse, wenn wir uns sofort zum Labor begeben."
    #show Harris normal
    har "Sehr gern, Captain."

    scene labor
    with dissolve

    "In dem dunklen, von blauem Neonlicht spärlich erleuchteten Labor hat Lieutenant Commander N´Evac soeben Admiral Harris, Captain Thomas und Lieutenant Nakamura unterrichtet."
    "Major Towers und Commander Stratter, die sich inzwischen mit den drei Offizieren von der Phoenix bekannt gemacht hat, haben N´Evacs Ausführungen ein zweites Mal mitangehört."

    #show Thomas normal
    cap "Ich habe Ben Dawson, den Captain der Darwin, sehr gut gekannt. Wenn eine Chance besteht, dass wir etwas über den Verbleib der Darwin herausfinden, bin ich der erste, der sich freiwillig meldet!"
    har "Ich bin vom obersten Kommando der Federation bevollmächtigt worden, das von Ihnen vorgeschlagene Vorgehen zu befürworten, Captain Ja´Vhoc."

    "Ja´Vhoc nickt bestätigend und verweist sofort an N´Evac."

    #show NÉvac normal
    nev "Dann werde ich unser Ingenieur-Team damit beauftragen, den Antrieb der Phoenix mit den Timecore-kompatiblen Komponenten auszustatten – mit Ihrer Genehmigung, Captain Thomas?"
    cap "Selbstverständlich – Genehmigung erteilt, Commander."
    jav "Ich stelle Ihnen das Kworrhonian Starship S´Epazit unter dem Kommando von Captain An´Jhot für diese Mission zur Verfügung, Lieutenant Commander N´Evac."

    scene spaceship_1
    with dissolve

    "Während Chefingenieur Solano den Einbau der für den Zeitsprung benötigten Elemente am Hyperspacedrive der Phoenix überwacht, haben sich Captain Thomas und Commander Stratter zurück auf die Brücke der Phoenix begeben, wo sie nebeneinander in den beiden Kommandositzen Platz genommen haben."

    #show Stratter normal
    kat "Die Aufklärung des Darwin-Zwischenfalls hat für Sie eine große Bedeutung, Captain? Falls mir diese Frage gestattet ist, Sir."
    #show Thomas normal
    cap "Ben Dawson, der Captain der Darwin, war einer meiner besten Freunde, Commander. Wir waren zusammen auf der Akademie und haben die ersten Jahre auf demselben Schiff gedient."
    cap "Ich habe mich sehr für ihn gefreut, als er mit der Darwin die erste Zeitreise unternehmen sollte."
    cap "Er wusste natürlich, mit welchem Risiko dies verbunden war, aber ich habe ihn so beneidet für dieses einzigartige Kommando."
    cap "Als die Darwin dann spurlos verschwunden war und es nie wieder eine Rückkehr gab, mussten wir zu akzeptieren lernen, dass möglicherweise die gesamte Crew auf immer in der Vergangenheit bleiben wird oder sogar bei dem Zeitsprung gestorben ist."
    cap "So oder so sind sie mit großer Wahrscheinlichkeit in unserer heutigen Zeit alle schon lang gestorben."
    kat "Und wenn wir endlich einen Hinweis darauf erhielten, was genau mit der Darwin geschehen ist, hätten Sie zumindest Gewissheit."

    "Thomas nickt wiederholt, indem er stumm vor sich hin sieht."

    cap "Kommen Sie mit den Änderungen in der Manövrierkontrolle zurecht, Lieutenant Mitchel?"
    #show Mitchel normal
    mit "Aye, Sir – zumindest habe ich allmählich den Eindruck."
    mit "Da die Phoenix und die S´Epazit, wie ich es verstanden habe, nur passiv manövrieren, indem wir vom Timecore der Rha´Acul mit einem Impuls versehen werden, gibt es gar nicht so viele Änderungen in der Steuerung."
    mit "Hauptsächlich die Neukalibrierung unserer Orientierungssensoren muss natürlich exakt ausgeführt werden, sobald wir in der Vergangenheit sind und uns an den abgeänderten Sternenkonstellationen interstellar lokalisieren müssen."
    cap "Sehr gut, Lieutenant."
    cap "Lieutenant Nakamura, wie tiefgehend ist Ihr Verständnis über den Timecore-Impuls?"
    #show Nakamura normal
    nak "Dafür, dass ich mich erst seit einem Tag mit dieser Physik befasse, schon sehr fortgeschritten, möchte ich behaupten, Captain."
    #"Thomas hebt eine Augenbraue."
    nak "Ich verstehe noch nicht jedes Detail der Theorie, die hinter dem Funktionsprinzip steht, aber ich weiß auf jeden Fall, wie die Kworrhonians den Impuls ausführen und wie er auf uns wirkt."
    nak "Und wie wir bei etwaigen Komplikationen gegensteuern könnten."
    cap "Das klingt doch perfekt vorbereitet, Lieutenant."

    sol "Solano an Brücke, Captain Thomas?"
    cap "Thomas hier."
    sol "Captain, der Umbau unseres Antriebes ist beendet. Lieutenant Commander N´Evac würde gern noch ein paar letzte Instruktionen mit Ihnen besprechen, Sir."
    cap "Verstanden, Commander. Ich komme zu Ihnen in den Maschinenraum."
    sol "Verstanden, Sir."

    "Thomas überträgt das Kommando an Commander Stratter und nickt Lieutenant Nakamura zu, ihn zu begleiten."
    "Über den Lift im hinteren Teil der Brücke gelangen die beiden ein paar Decks tiefer auf das Maschinendeck."
    "Wo Lieutenant Commander N´Evac den abgeschlossenen Umbau am Antrieb noch einmal bestätigt und eine Reihe zusätzlicher Hinweise auf die Funktion und Gegenmaßnahmen bei etwaigen Fehlfunktionen gibt."
    "Die Abteilung des Maschinendecks, in der sich der Hyperdrive befindet, ist durch halb geöffnete Panzerschotts gegen das restliche Maschinendeck ein wenig abgegrenzt."
    "Über zwei Leitern links und rechts vom Hyperdrive beziehungsweise einen offenen Lift hinter ihm kann man noch drei weitere offene Etagen erreichen, von denen aus man den Antrieb auf verschiedenen Höhen inspizieren kann."
    "Captain Thomas lässt N´Evac die Hinweise in erster Linie an Solano und Nakamura weitergeben, da diese beiden den bevorstehenden Zeitsprung verantwortlich überwachen werden."
    "Anschließend kehrt N´Evac auf die Rha´Acul zurück und begibt sich von dort aus zu Captain An´Jhot auf die S´Epazit."

    "Während Major Towers sich an Bord der Phoenix begibt, bleibt Admiral Harris bei Captain Ja´Vhoc auf der Rha´Acul."

    har "Viel Erfolg Ihnen und Ihren Crews, Captains!"

    "Captain Thomas und Captain An´Jhot danken dem Admiral und starten dann auf Freigabe hin ihre gemeinsame Zeitreisemission."

    scene ship_6
    with dissolve

    "Indem die Phoenix von der Rha´Acul abdockt, kommt die S´Epazit von der Rückseite der Kworrhonian Starbase aus in die Ansicht gesteuert."
    "Ihre sich von der Phoenix deutlich unterscheidende Bauart erinnert mit Fantasie an einen großen grauen Raubvogel mit bedrohlich geöffnetem Schnabel."
    "In Wirklichkeit sind hier an der Frontseite des Raumschiffes lediglich die große Hauptbrücke oben und das Maschinendeck unten deutlich durch den Freiraum dazwischen vertikal voneinander getrennt."
    "Links und rechts verfügt die S´Epazit über zwei zylindrische, überdimensional groß erscheinende, tiefblaue Antriebssegmente."
    "Lieutenant Commander N´Evac betritt gerade die Brücke der S´Epazit, die in spärliches Licht gehüllt ist und daher bedrückend dunkel wirkt."
    "N´Evac nimmt auf dem zweiten Kommandositz direkt neben Captain An´Jhot Platz, die beide halbkreisförmig von Konsolen umschlossen sind und hinter denen sich imposant aussehende holografische Emitter für den dreidimensionalen Bild-Funkkontakt befinden."

    anj "Bereithalten für den temporalen Impuls!"

    "Auf der im Kontrast dazu angenehm hell erleuchteten Brücke der Phoenix hat Captain Thomas gerade noch einen bestätigenden Kontrollblick mit Commander Stratter und Lieutenant Commander Reagan sowie mit den Lieutenants Mitchel und Nakamura gewechselt"
    "Aus dem unteren Segment der großen Starbase Rha´Acul wächst ein violett leuchtender und von roten Blitzen durchzuckter Wirbel nach draußen heran, der die Phoenix und die S´Epazit vollständig einhüllt."
    "Dann scheinen beide Raumschiffe plötzlich in den Wirbel hinein zu driften und von den rot blitzenden turbulenten Strömungen in sein Inneres gezogen zu werden."
    "Indem sie scheinbar ins Unendliche schrumpfen, verschwinden beide Raumschiffe im Zentrum des Wirbels, in dem grau-blau wirbelnde, temporale Strömungen zu herrschen scheinen."
    "Anschließend schrumpft der Wirbel am unteren Segment der Rha´Acul wieder zusammen, bis er spurlos verschwunden ist."
    "In der ebenfalls relativ dunklen Einsatzzentrale von Kworrhonian Starbase Rha´Acul wechselt Admiral Harris einen Blick mit Captain Ja´Vhoc: beider Gesichter werden im Halbdunkel neongrün angestrahlt."

    #show Harris normal
    #show Ja´Vhoc normal
    har "Das ist das zweite Mal, das Schiffe der Federation sich auf eine Zeitreise-Mission begeben – ich hoffe, diesmal werden wir wieder von ihnen hören!"
    jav "Ich bin sehr zuversichtlich, Admiral. Mit dem Timecode von der Vernichtung der Erde als Ziel kann mithilfe des Timecore eine sichere und orientierte Reise durch den Hyperspace gewährleistet werden."
    har "In der Theorie zumindest."
    jav "In der Geschichte unserer beiden Völker hat jede große neue Errungenschaft immer mit einer Theorie begonnen."

    scene planet
    with dissolve

    "Im Schatten des terrestrischen Mondes blitzt es im leeren Weltall auf, und urplötzlich wächst derselbe violett schimmernde, hochenergetische Wirbel wie bei Starbase Rha´Acul zu seiner vollen Größe heran."
    "Aus seinem turbulenten Zentrum des grau-blau erscheinenden temporalen Flusses wachsen innerhalb von Sekundenbruchteilen die Phoenix und die S´Epazit zu ihrer vollen Größe heran."
    "Als der Wirbel inmitten roter, hochenergetisch zuckender Blitze schon wieder ins Unendliche zusammenschrumpft und vollständig verschwindet."
    "Christopher Thomas und Kathrin Stratter blicken fasziniert durch die große transparente Kuppel über ihren Köpfen, wo das Bild des Hauptschirms vervollständigt wird."
    "Die Phoenix überfliegt gerade die Tag-Nacht-Grenze des irdischen Mondes, und am Mond-Horizont taucht im rot glühenden Lichte der aufgehenden Sonne in imponierendem Anblick die Erde auf!"

    #show Thomas faszinated
    #show Nakamura faszinated
    #show mitchel faszinated
    mit "Einfach nur fantastisch!"
    nak "Vor allem, wenn man bedenkt, dass wir gerade auf die Vergangenheit der Erde blicken!"

    "Lieutenant Commander Reagan blickt von den taktischen Kontrollen auf."

    #show Reagan normal
    reg "Unser elektromagnetisches Störfeld ist intakt."
    kat "Dann lassen Sie uns nahe genug rangehen, um unsere eigene Geschichte zu beobachten, Lieutenant."
    mit "Aye, Commander – Kurs in einen Erdorbit ist programmiert."
    cap "Öffnen Sie bitte einen Kanal zur S´Epazit!"

    reg "Aye, Captain."

    scene comander_4
    with dissolve

    "In einem kurzen Gefühl der Desorientierung und des Déjà-Vu findet sich die Crew der Phoenix plötzlich erneut beim Austritt aus dem Wirbel des Timecore wieder, und das gerade Geschehene erfolgt gefühlt innerhalb von nur einer Sekunde erneut."
    "Da erscheinen die Gesichter Lieutenant Commander N´Evacs und Major Towers´ auf dem Bildschirm, als sich der angeforderte Kanal zur S´Epazit geöffnet hat."

    cap "Was war das gerade?"

    "Seine übrigen Brückenoffiziere zeigen ebenfalls verwirrte Blicke."

    nev "Wir haben soeben einen relativistischen Timeloop erfahren, Captain."
    #show thomas questioningly
    nev "Auch wenn wir durch den Hyperspace gereist sind, so können wir die klassischen Gesetzmäßigkeiten der Relativitätstheorie doch nicht ganz aushebeln."

    "Nicht wirklich verstehend, wechselt Thomas einen Blick mit Nakamura, die ansatzweise zu verstehen scheint, was N´Evac gemeint hat, und gerade eine schnelle Folge von Berechnungen mit der Konsole der Wissenschaftstation durchführt."

    nev "Ich denke, wir sollten nun mit der Ursachenanalyse auf der Erde beginnen."
    cap "Das ist mein eigentlicher Grund für den Funkspruch gewesen, Commander."
    nev "Dann schlage ich vor, dass Major Towers und ich wieder zu Ihnen an Bord kommen, um unser Vorgehen zu koordinieren."

    "N´Evac wechselt einen bestätigenden Blick mit Towers in der relativ dunklen Atmosphäre auf der Brücke der S´Epazit."

    cap "Wir freuen uns, Sie erneut an Bord der Phoenix begrüßen zu dürfen, Major, Commander!"

    "N´Evac nickt in einer deutlichen Geste, bevor der Funkkanal geschlossen wird."
    "Thomas blickt fragend zu Nakamura."

    #show thomas questioningly
    nak "Ich glaube, ich bin auf dem Weg zu verstehen, was Commander N´Evac meinte, Captain."
    cap "Sehr gut, Lieutenant."
    kat "Stellen Sie bitte für das Außenteam ein Wissenschaftsteam zusammen, Lieutenant Nakamura. Commander Reagan, außerdem wird ein begleitender Sicherheitstrupp benötigt."
    nak "Aye, Ma´am."

    "Thomas nicke Stratter bestätigend zu."

    scene ship_6
    with dissolve

    "Die Phoenix und die S´Epazit schwenken langsam in einen hohen Erdorbit ein, während ihre elektromagnetischen Störfelder sie für die terrestrischen Satelliten unsichtbar machen."
    "Auf ihren metallenen Oberflächen spiegelt sich glänzend das Licht der irdischen Sonne wider."
    "In einem der Science-Laboratorien an Bord der Phoenix, das über einen eigenen Besprechungsraum verfügt, leitet Lieutenant Nakamura gerade die auswertende Besprechung mit dem von ihr zusammengestellten Wissenschaftsteam."

    nak "Die vergleichenden Aufnahmen der Sternenkonstellationen haben bestätigt, dass wir uns im Jahre 2017 befinden."

    "Eine andere Wissenschaftsoffizieren fährt auf Nakamuras Nicken hin fort, während sie vor einem Wandschirm steht, der die Aufnahme von der Implosion der Erde immer wieder abspielt."
    "Nach einer 3-D Spektralanalyse konnte mein Team das Zentrum der Implosion auf den nordwestlichen Teil des europäischen Kontinents einengen."

    of1 "Also das Entstehungszentrum der Quantensingularität?"
    nak "Exakt. Als wir mit der Phoenix im Erdorbit die entsprechende Position erreicht hatten, haben wir weitere Scans vorgenommen und eine anomale Energieemission auf diesen Koordinaten detektiert."

    "Sie weist auf den Wandschirm hinter sich, auf dem jetzt die dargestellte Erde nicht länger implodiert, sondern sich, wieder im Ausgangszustand befindlich, um etwa 100° dreht, sodass jetzt der Blick auf die britischen Inseln aus dem Weltraum frei liegt und vergrößert wird."

    nak "Die Emissionsquelle liegt irgendwo zwischen dem 50. und 52. nördlichen Breitengrad, ziemlich genau auf Höhe des 2. westlichen Längengrades gemäß dem in diesem Jahrhundert gültigen Koordinatensystem."
    nak "In der Ebene von Salisbury haben wir auf den Überwachungsaufnahmen irreguläre Aktivitäten ausmachen können, die auf archäologische Ausgrabungsarbeiten hinweisen."

    "Auf dem Wandschirm ist das Bild erneut extrem vergrößert worden, sodass jetzt eine Luftaufnahme aus großer Höhe auf das Ausgrabungscamp der Archäologen erkennbar wird."

    nak "Was auch immer die Wissenschaftler dort unten ausgraben – es wird offenbar in Kürze die Vernichtung der gesamten Erde hervorrufen!"

    "In der Waffenkammer an Bord der Phoenix hat Lieutenant Commander Reagan gerade ihr komplettes Sicherheitsteam für den Außeneinsatz mit Elektroimpulswaffen aus dem abgesicherten Schrank mit der Aufschrift Electric Pulse Rifles ausgestattet."

    reg "Gemäß unseren historischen Aufzeichnungen müssen wir in dieser Zeit weniger mit Strahlenwaffen rechnen, dafür aber mit Schusswaffen auf Hochgeschwindigkeitsprojektilbasis und vereinzelt vielleicht auch Laserwaffen."
    reg "Wir verwenden unsere EPR daher zunächst ausschließlich auf Betäubungsniveau. Nur im extremen Notfall werden wir sie höher kalibrieren."
    of2 "Aye, Ma´am."
    reg "Dann passen Sie gut auf unser Außenteam auf!"

    "Etwa eine Stunde später verlässt ein Shuttle den Hangar der Phoenix, der sich achtern geöffnet hat."
    "Auf der Brücke verfolgen Captain Thomas, Commander Stratter und Lieutenant Mitchel den Landeanflug des Shuttles auf den europäischen Kontinent."

    mit "Das elektromagnetische Störfeld des Shuttles wird autonom aufrecht erhalten."

    "Thomas und Stratter beobachten auf dem Hauptschirm wie gebannt die Ankunft des Shuttles in der Vergangenheit ihres Heimatplaneten Erde."
    "Das Shuttle überfliegt den nächtlichen Ärmelkanal und gleitet dann über das Land hinweg."
    "In der Ebene von Salisbury setzt es schließlich in einer kleinen Talsenke zwischen ein paar Felsen zur Landung an."
    "Das Außenteam läuft von hier aus zu Fuß weiter hin zur nächtlichen Ausgrabungsstelle."
    "Lieutenant Commander N´Evac und Major Towers befinden sich inzwischen wieder an Bord der Phoenix, wo sie gerade zusammen mit Captain Thomas und Chief Solano über das Maschinendeck gehen."

    nev "Selbstverständlich ist die unmittelbare Nähe zu einer entstehenden Quantensingularität generell eine große Gefährdung für unsere Raumschiffe, jedoch ist die kritischste Komponente hierbei unser Timecore."
    tow "Schlagen Sie vor, dass wir besser den Erdorbit verlassen, Commander?"
    nev "Das wäre offengestanden die ungünstigere Option."

    "Towers wechselt mit Thomas ein einvernehmlich zustimmendes Nicken."

    sol "Die andere Option wäre, den Hyperdrive der Phoenix wieder vom Timecore zu entkoppeln, Commander?"
    nev "Genau das, Chief Engineer."
    cap "Besteht ein Risiko für meine Besatzung, Commander?"
    nev "Nicht mehr als generell während unserer gesamten Zeitreise-Mission, Captain. Das Risiko, einen intakten Timecore dem Entstehungsprozess einer Quantensingularität auszusetzen, ist beträchtlich größer."
    tow "Ihre Entscheidung, Captain Thomas."

    menu:
        "Wir werden den Timecore intakt lassen.":
            jump intakt
        "In Ordnung, Commander N´Evac. Ich denke, Sie haben recht.":
            jump entkoppeln

label intakt:
    cap "Wir werden den Timecore intakt lassen bevor wir in der Vergangenheit feststecken."
    tow "Captain, sind sie sich ..."
    cap "Commander N´Evac, wie hoch ist das Risiko?"
    nev "Wir kennen die Konsequenzen nicht, den Timecore intakt zu lassen wäre Torheit."
    cap "In Ordnung, Commander N´Evac. Diese Entscheidung werde ich nicht alleine treffen, wir stimmen ab."
    menu:
        "intakt lassen":
            jump vote
        "demontieren":
            jump vote

label vote:
    "Die Crew stimmt dafür den Timecore zu demontieren!"

    jump timecore

label entkoppeln:
    cap "In Ordnung, Commander N´Evac. Ich denke, Sie haben recht."

    jump timecore

label timecore:
    nev "Dann werde ich eine Technik-Crew von der S´Epazit herüber kommen lassen."
    sol "Ich werde Ihnen beim Entkoppeln des Hyperdrive wieder assistieren."
    cap "In Ordnung, machen Sie es so!"

    # Ausgrabungsstelle
    "Die Ausgrabungsstelle ist inzwischen vom Tageslicht erhellt, und das Außenteam der Phoenix hat sich unter die Archäologen verteilt: da die Freilegung der unterirdischen Kammer kurz bevorsteht, sind alle so in ihre Arbeit vertieft, dass das verteilte Außenteam niemandem fremd vorkommt."
    "Reagan, Nakamura und zwei weitere Offiziere der Phoenix sind Professor Howard und dem Studenten neben ihm über den Zeltplatz gefolgt."

    stu "Gemäß unseren neu gewonnenen Datierungen gehen die unterirdischen Bauten auf ca. 3 000 Jahre vor Christus zurück, Professor."
    how "Das bestätigt unsere bisherige überarbeitete Theorie."
    stu "Die ganze Architektur ist um diese zentrale Kammer ausgelegt."

    "Das Außenteam sieht, wie der junge Mann auf dem Tablet, das er mit sich trägt, auf die schematische Skizze der unterirdischen Gänge weist."

    how "Ja, was auch immer darin verborgen sein mag, hat die Menschen offensichtlich zum Bau dieser gesamten Kultstätte bewegt."

    "Indem die beiden in einen offenkundig in den Boden gebohrten Tunnel steigen, folgen Reagan, Nakamura und die beiden weiteren Offiziere ihnen unerkannt zusammen mit ein paar weiteren Wissenschaftlern."
    "Howard strahlt begeistert beim Einstieg in den mit Lampen ausgeleuchteten Bohrtunnel"

    how "Und heute werden wir endlich sehen, was sich in der Kammer befindet!"

    "Auf dem Maschinendeck der Phoenix tritt Major Towers gerade wieder zu Lieutenant Commander N´Evacs Team, das in dem vom restlichen Maschinendeck durch Metallschotten separierten Bereich mit der Entkopplung des Hyperdrives vom Timecore fast fertig ist."

    tow "Ist die Entkopplung abgeschlossen, Commander?"
    nev "In den nächsten Minuten, Major."

    "Towers bemerkt einen Unterton in N´Evacs Stimme, den er aber nicht richtig zu interpretieren weiß."

    tow "Ich wollte Sie nicht unter Druck setzen, Commander."

    #show Nevac happy
    nev "Das tun Sie nicht, Major."

    menu:
        "N´Evac vertrauen.":
            jump vertrauen
        "N´Evac misstrauen.":
            jump misstrauen

label vertrauen:
    nev "Ich bestätige den planmäßigen Status der Abkopplung.."
    cap "In Ordnung, Commander N´Evac."

    "Commander N´Evac stiehlt ein wichtiges Teil des Timecore und verschwindet mit dem anderen Schiff aus der Vergangenheit."
    "Sie Sitzen fest, die Mission ist gescheitert!"
    jump ende



label misstrauen:
    tow "Dann würde ich gern für meinen Rapport an Captain Thomas einen abschließenden Blick auf den Hyperdrive werfen."
    nev "Das wird nicht nötig sein, Major. Ich bestätige den planmäßigen Status der Abkopplung."
    #show Tower happy
    tow "Selbstverständlich wissen Sie, Commander, dass ich einen Abschluss-Rapport nur erstatten werde, wenn ich mich persönlich vom Status überzeugt habe – Sicherheitsprotokolle."

    "Chief Solano tritt gerade in das halboffene Metallschott und bekommt mit, dass hier etwas nicht stimmt. Major Towers tritt zielstrebig an N´Evac vorbei Richtung Hyperdrive, als zwei der kworrhonianischen Ingenieure von beiden Seiten aus Towers abrupt festhalten."

    tow "Was soll das denn, Commander?!"

    nev "Tut mir leid, Major, aber ich fürchte, wir werden bezüglich Ihrer Sicherheitsprotokolle umdisponieren müssen!"
    #show Solano normal
    sol "Chief Solano an Brücke, Captain Thomas wir haben hier..."

    "N´Evac bringt Solano mit einem metallenen Werkstück zum Schweigen, das er diesem brutal gegen den Kopf geworfen hat: Solano fällt zur Seite und bleibt mit blutverschmierter Schläfe regungslos auf dem Boden liegen."
    "Reaktionsschnell schlägt Towers dem Kworrhonian links hinter ihm mit dem Hinterkopf genau ins Gesicht und nutzt seinen somit frei gewordenen Arm, um den anderen Kworrhonian einmal über sich auf den Boden des Maschinendecks zu werfen."

    #show brücke
    #show Thomas scared
    #show Stratter scared
    "Auf der Brücke sehen Thomas und Stratter einander verwirrt und zugleich beunruhigt an."

    cap "Was ist mit der Verbindung geschehen, Lieutenant?"

    "Mitchel versucht, die Funkverbindung zum Maschinendeck wiederherzustellen."

    mit "Es ist kein technischer Defekt, Captain. Die Verbindung scheint vom Maschinendeck aus beendet worden zu sein."
    cap "Öffnen Sie den Kanal erneut!"
    mit "Aye, Sir – Kanal zum Maschinendeck ist offen."
    cap "Thomas an Maschinendeck, Chief Solano, erstatten Sie Bericht!"

    "Mitchel, Thomas und Stratter wechseln abwartende, rätselnde Blicke."

    cap "Chief Solano, erstatten Sie Bericht!"
    kat "Stratter an Sicherheit, schicken Sie ein Team auf´s Maschinendeck – möglicherweise gibt es dort ein Problem!"

    "Stratter und Thomas wechseln einen einvernehmlichen Blick miteinander."
    "Auf dem Maschinendeck hat Major Towers beide Kworrhonians, die ihn festgehalten hatten, niedergestreckt und eine zweite Bordfunkanlage betätigt."

    tow "Towers hier, Captain – N´Evac hat Solano niedergestreckt, und auch ich wurde von den Kworrhonians angegriffen. Ich kann nicht weiter reden!"

    "Ein dritter der kworrhonianischen Techniker geht gerade auf Towers los, dem der Major aber reaktionsschnell ausweichen kann."

    cap "Thomas an Sicherheit, es gibt eine bestätigte Eskalation auf dem Maschinendeck! Major Towers und Chief Solano werden von Commander N´Evacs Techniker-Team angegriffen."
    mit "Das Sicherheitsteam bestätigt seinen Einsatz und postiert sich, Captain."

    "Thomas wendet sich an Stratter"

    menu:
        "Selbst zum Maschinendeck gehen.":
            jump maschinendeck
        "Weiter die Brücke kommandieren.":
            jump go

label maschinendeck:
    cap "Ich gehe hin – übernehmen Sie die Brücke, Commander!"
    kat "Captain, es besteht ein offenkundiges Sicherheitsrisiko, und daher ist es nicht empfehlenswert, dass Sie als Captain die Brücke verlassen und sich zudem in eine Gefahrensituation bringen!"
    cap "Da haben Sie recht, Commander, aber es sind meine Leute, die da auf dem Maschinendeck angegriffen werden, und ich habe N´Evacs Techniker-Team den Zugang zu unserem Antrieb genehmigt. Ich will sie da unten nicht allein lassen!"
    jump go

label go:
    "Stratter erkennt in Thomas´ Blick den Ausdruck des Verlustes und der Hilflosigkeit, die er wohl zu oft im vergangenen Krieg erleben musste, wenn er von einer Kommandobrücke aus nichts weiter tun konnte, als Befehle zu erteilen, während seine Offiziere in den angeordneten Einsätzen ums Überleben kämpften."
    "Stratter versteht Thomas und lässt ihn daher mit einem Nicken gewähren, obwohl sein Verhalten nicht den Sicherheitsvorschriften entspricht."
    "Thomas´ antwortender Blick signalisiert Stratter, dass er sie ebenfalls verstanden hat."

    "N´Evac schlägt mit dem Ellenbogen gegen die Kontrollen, so dass sich das Panzerschott komplett schließt und so die Abteilung mit dem Hyperdrive gegen das restliche Maschiendeck abgeschottet wird."
    "N´Evac sieht, wie Towers den dritten seiner Offiziere überwältigt hat, und betätigt seinen tragbaren Funktransmitter."

    nev"Phase_2 ist etwas früher als geplant in Kraft getreten, Captain. Halten Sie sich bereit!"
    anj "Verstanden, wir halten uns bereit, Colonel."

    "Mit funkelndem Blick nimmt N´Evac die Verfolgung Towers´ auf, der gerade über die rechte Leiter zu einer der höheren offenen Etagen klettert."

    #show comander_3
    anj "Setzen Sie zum Eröffnungsmanöver von Phase 2 an, Lieutenant!"
    of1 "Aye, Captain."

    "Von der Brücke der Phoenix aus sehen Commander Stratter und Lieutenant Mitchel durch die große transparente Kuppel, wie die S´Epazit plötzlich zu einem nicht abgesprochenen Manöver ansetzt und im Vorbeifluge die Phoenix mit gezielten Energieemissionen beschießt."
    "Im Lift, mit dem er zum Maschinendeck fährt, wird Christopher Thomas plötzlich von einem brutalen Ruck erst gegen die Wand und dann auf den Boden geworfen."

    kat "Alarm Rot, Lieutenant – aktivieren Sie die Defensivsysteme!"

    "Die Brücke wird von rotem Schimmern intervallweise durchflutet, während sich außen eine panzerartige Jalousie über die gesamte transparente Kuppel zieht, sodass von der Brücke aus nur noch der Blick auf den Hauptschirm die Sicht in den Weltraum ermöglicht."

    mit "Deflektorschild ist aktiviert, Commander."

    "In Außenansicht beendet die S´Epazit ihren Angriff auf die Phoenix, die sie einmal umrundet hat: die letzten Energiestrahlen sind am Deflektorschild der Phoenix gestreut worden, sodass sie keinen Schaden mehr anrichten konnten."
    "Allerdings sind an der Außenhülle der Phoenix, wo die ersten Energiestraheln eingeschlagen sind, einige Brandspuren, Beschädigungen und Kurzschlussreaktionen zu sehen, deren Funkenregen schnell im Vakuum erlischt."

    mit "Die S´Epazit hat ihr Angriffsmanöver beendet."
    kat "Commander Stratter an Captain Thomas – Sir, wir sind soeben von der S´Epazit angegriffen worden..."

    "Funkstille"

    kat "Sir, hören Sie mich?"
    mit "Commander, der Beschuss durch die S´Epazit hat unter anderem unsere Kommunikationskontrolle beschädigt sowie ein paar interne Kontrollsysteme."
    kat "Verdammt – sie wussten genau, worauf sie zielen!"
    mit "Ich habe den Captain mit den Bordsensoren detektiert – er befindet sich bereits im Lift."
    kat "Können Sie den Lift anhalten und wieder zurückschicken, Lieutenant?"

    #show mitchel shocked
    mit "Leider gehört die Liftkontrolle mit zu den beschädigten Systemen, Commander."

    "Christopher Thomas hat sich im Lift inzwischen wieder aufgerappelt und ebenfalls festgestellt, dass weder die Bordfunkanlage noch die manuelle Liftkontrolle funktionieren."
    "Da fällt sein Blick auf das Fach in der Liftwand, das Ausrüstung für Notfälle beinhaltet."
    "Christopher öffnet es und erblickt einen Raumanzug im Inneren. Christopher blickt anschließend unter die Decke zur Notfall-Ausstiegsluke des Liftes."

    mit "Commander, laut den Sensoren ist soeben eine Notfallausstiegsluke des Liftschachtes geöffnet worden."

    "Stratter blickt mit einer Vermutung auf."


    "Christopher ist über die Notfallleiter ein Stück weit den Lift hinaufgeklettert zur kleinen Ausstiegsschleuse."
    "Nach dem hermetischen Verschließen der Innenluke und dem rapiden Druckabfall, gegen den er sich vorschriftsmäßig festgurten musste, klettert er nun durch das Außenschott, deaktiviert die elektromagnetischen Stiefel seines Raumanzuges und stößt sich ab, sodass er, schwerelos schwebend, an der Außenhülle der Phoenix entlang weiter nach unten Richtung Maschinendeck gleitet."
    "Auf einer der höheren Etagen läuft Major Towers zu den Kontrollsystemen des Hyperdrive, um diesen vorsorglich zu deaktivieren. N´Evac klettert hastig die zweite Leiter empor."
    "Auf der anderen Seite des geschlossenen Panzerschotts haben ein paar Ingenieure Chief Solano wieder auf die Beine geholfen: zwar blutet er am Kopf, jedoch macht er sich sofort daran, die Panzerabschottung manuell zu überbrücken."
    "Draußen erreicht Christopher soeben im Gleitflug das Außenschott zum Maschinendeck, an dem er sich krampfhaft festklammert und seine Magnetstiefel reaktiviert."
    "Durch die Luftschleuse gelangt er auf die höchste Etage im Maschinendeck rund um den Hyperdrive. Den Raumanzug hastig ausziehend, eilt er zum Geländer, um den Überblick über diese jetzt abgeschottete Sektion des Decks zu bekommen: er sieht Towers auf der tieferen Etage und N´Evac auf der gegenüberliegenden Leiter, der gerade auf Towers´ Deck angelangt ist."

    #show Tower normal
    #show Nevac normal
    tow "In Zukunft wird es wohl einige Spannungen in den kworrhonian-terrestrian Beziehungen geben!"

    nev "Dann sollten wir etwas Druck ablassen, Major!"

    "N´Evac ergreift plötzlich eine spitze Konverterzange aus einem bereitstehenden Reparatur-Kit, wirft diese gekonnt kurz hoch, so dass sie sich um 180 Grad dreht, fängt sie noch einmal kurz auf und schmettert sie dann mit voller Wucht direkt neben Towers in einen Plasmakonverter."
    "Durch diese Wucht kann die schwere Zange mit der Spitze voran das Sicherheitsglas durchschlagen, und mit gewaltigem Druck faucht eine Stichflamme aus purem Plasma auf Major Towers zu, der noch kurz aufschreit, aber bereits innerhalb von Sekundenbruchteilen schwer verbrannt wird, indem die quer über die Etage fauchende Stichflamme die gesamte Sicht versperrt."
    menu:
        "Angreifen.":
            jump angriff
        "Zu Towers rennen.":
            jump retten

label retten:
    #show Thomas shocked
    cap "Nein, Towers!"
    "Völlig verzweifelt rennt Christopher zu Towers, nur um zu sehen dass dieser nicht mehr zu retten ist."
    "N´Evac nutzt die Unachtsamkeit und überwältigt Christopher von hinten."
    "Die Mission ist gescheitert"
    jump ende

label angreifen:
    "Entsetzt und voller Wut nimmt Christopher Anlauf und springt mit lautem Aufschrei über die Brüstung nach unten."

    cap "Verräter!!"

    "Durch die wieder erlöschende Plasmaflamme sieht N´Evac plötzlich von weiter oben Christopher auf sich zu gestürzt kommen, als Christopher schon mit vollem Tempo gegen N´Evac prallt und diesen brutal von den Beinen reißt und gegen die Wand schmettert."

    "Im unterirdischen Tunnel der archäologischen Ausgrabungsstätte hat sich soeben der Staub gelegt, sodass der Blick in die große Hohlkammer frei wird: Professor Howards Gesicht wird aus dem Innern der Kammer heraus von sich fließend verändernden Farben geblendet."
    "Nakamura und Reagan blicken fassungslos in die Hohlkammer hinein: Im Innern befindet sich das komplette Segment eines Maschinenraums, in dessen Mitte der Hyperdrive aufragt und von ähnlichen Zusatzaggregaten bestückt ist wie aktuell der Hyperdrive der Phoenix durch die Verbindungssegmente zum Timecore der Kworrhonians."
    "Die Anordnung einiger Konsolen und offensichtlich zusammengestürzten Wand- und Stützsegmenten des ursprünglichen Maschinendecks gleicht mit etwas Fantasie der Monolithstruktur des oberirdischen Stonehenge."

    nak "Das ist der Hyperdrive der Darwin!"
    reg "Unglaublich! Aber wo ist der Rest des Schiffes geblieben? Offensichtlich ist es hier abgestürzt!"
    nak "Und wie lang muss der Absturz schon her sein, wenn die Menschen damals hierdurch inspiriert wurden, die Kultstätte zu erbauen?!"


    #show dark_comad
    of1 "Sie haben soeben den Hyperdrive der Darwin freigelegt, wir empfangen das Ortungssignal, Captain."
    anj " Colonel, Phase 3 ist soeben angelaufen."
    nev "Machen Sie weiter, Captain!"
    anj "Aktivieren Sie die Tachyon-Emission, Lieutenant!"
    of1 "Aye, Captain."

    "Aus dem unteren Segment des augenscheinlich geöffneten Raubvogelschnabels der S´Epazit wird der kurz aufblitzende Tachyon-Impuls abgefeuert, der überlichtschnell auf die Erdoberfläche, genau auf Stonehenge zu schießt."
    "In der unterirdischen Hohlkammer leuchten die Höhlenwände blau auf, und augenblicklich beginnen heftige Blitze den ursprünglichen Timecore der Darwin zu durchzucken – allmählich scheint er aktiv zu werden: erste Erschütterungen durchziehen den Bohrtunnel und werden nach und nach heftiger."

    nak "Tscherenkow-Strahlung! Ein Tachyon-Impuls von außen hat soeben dazu geführt, dass der Timecore irgendeine Art von temporaler Verzerrung erzeugt!"

    "Reagan brüllt einfach in das Archäologenteam hinein."
    reg "Raus hier!"

    "Professor Howard und sein Team ergreifen die Flucht, obwohl sie zugleich völlig entgeistert sind von dem imponierenden Szenario."
    "Das Außenteam der Phoenix rennt voran aus dem unterirdischen Gang hinaus, indem die Erschütterungen zunehmend heftiger werden."
    "Am Ausgang angekommen, springen die Fliehenden Hals über Kopf aus dem Tunnel, als schon hinter ihnen eine Druckwelle etliche Felsentrümmer aus dem Gang schleudert."
    "Inmitten der Megalithstruktur klafft der Erdboden auf und wird augenscheinlich von einem schwarzen Abgrund in unendliche Tiefen verschlungen: der Schlund breitet sich kreisrund immer weiter aus, und während Reagan und Nakamura mit den übrigen Offizieren aus dem Lager der Archäologen wegrennen, stürzt im Hintergrund auf der Anhöhe das beeindruckende Stonehenge völlig in sich zusammen."
    "Um das wegrennende Außenteam herum beginnt der Erdboden ebenfalls an zahlreichen Stellen aufzubrechen, und tiefe Risse durchziehen immer wieder mit rasendem Wachstum den Boden."
    "Entsetzt bekommen Reagan und Nakamura mit, wie ihr Außenteam um einige Mitglieder dezimiert wird: Unter einem Offizier tut sich urplötzlich ein Erdspalt auf, so dass der Mann in die finstere Tiefe stürzt; unter einem anderen erhebt sich plötzlich der Erdboden und wächst zu einem an die zehn Meter hohen Wall heran, der den Offizier einfach mit in die Höhe katapultiert und irgendwo auf die andere, nicht mehr zu sehende Seite schleudert."
    "Zwei weitere Offiziere werden von durch die Luft geschmetterten Felsbrocken erfasst und mitgerissen."
    "Auch dicht neben den rennenden Nakamura und Reagan schlagen mehrere Felsbrocken, den Boden unkontrolliert erschütternd, wie ein Bombenhagel ein: ein Wunder, dass sie beim Rennen noch das Gleichgewicht behalten können."

    "Nachdem Christopher mit voller Wucht aus dem freien Fall gegen N´Evac gesprungen ist, sind beide gegen die Wand am Rande des großen Hyperdrive geprallt und haben dabei einen der Bildschirme zerschmettert."
    "N´Evac landet, auf dem Rücken liegend, auf dem Boden, springt jedoch sofort zurück in den Stand. Christopher hat sich von dem Geländer, gegen das er geprallt ist, wieder zurück gestoßen, um N´Evac erneut anzugreifen."
    "Dieser blockt Christophers Faustschlag ab und schlägt Christopher seine Stirn gegen den Kopf."
    "Christopher taumelt ein paar Schritte zurück, weicht jedoch dem Schlag N´Evacs reaktionsschnell aus und tritt stattdessen N´Evac die Beine weg, so dass dieser erneut auf den Rücken schlägt."
    "Hier ergreift N´Evac einen Plasmabrenner für Reparaturarbeiten, der infolge des Kampfes zu Boden gefallen war"
    "Christopher springt der speienden Plasmaflamme knapp aus dem Weg über das Geländer, rollt sich aber um dieses einmal herum, und springt dann wieder zurück mit voller Wucht gegen N´Evac, der den Plasmabrenner fallen lässt: dieser schlägt deaktiviert ein Deck tiefer auf den metallenen Boden auf."
    "Dann tauschen Christopher und N´Evac eine schnelle Folge von gezielten Faustschlägen aus, die zum Teil abgeblockt werden, zum Teil auch beim jeweils anderen sitzen."
    "Im Verlaufe ihres Kampfes umrunden die beiden auf der erhöhten Etage einmal halb den großen Hyperdrive."

    "Inmitten der Apokalypse erreichen Nakamura und Reagan mit dem Rest ihres Außenteams das Shuttle, das sie zwischen den Felsen in der Talsenke gelandet hatten. Immer wieder schlagen große Felsbrocken neben ihnen ein und werden riesige Erdwälle aus dem Boden aufgeschichtet; die Unmengen an aufgewirbeltem Staub in der Luft sorgen durch Reibung für die Entstehung vereinzelter Gewitter! Sie schließen das Außenschott und starten die Triebwerke."

    reg "Wir müssen irgendwie durch die atmosphärischen Turbulenzen hindurch manövrieren!"
    nak "Eine Alternative haben wir ja nicht!"
    reg "Alle festhalten – es ist noch nicht überstanden!"
    nak "Ich versuche einen direkten Senkrechtstart, sobald wir vom Boden abgehoben haben – die Sensoren sind sowieso hier unten blind!"

    "Das Shuttle hebt ab, indem weitere Trümmer knapp neben ihm einschlagen: gerade hat das Shuttle die Talsenke verlassen, da wird diese vollständig durch einen weiteren, sich plötzlich erhebenden Erdwall zermalmt; das Shuttle taucht, senkrecht nach oben startend, in die von Gewitterblitzen durchzuckten Staubwolken ein und wird immer wieder von heftigen Turbulenzen durchgeschüttelt."
    "Nakamura und Reagan steht der Schweiß auf der Stirn, indem sie krampfhaft um die Kontrolle des Shuttles kämpfen."
    "Auf der dunklen Kommandobrücke der S´Epazit blickt der Flugkontrolloffizier von seinen Anzeigen auf."

    of1 "Captain, nach unseren Berechnungen erfolgt die temporale Implosion im Hyperdrive der Darwin in diesen Sekunden."

    "Captain An´Jhot blickt wie gebannt auf den großen Bildschirm, der die Erde im Vollbild zeigt: da blitzt es für einen Moment in der Ebene von Salisbury hell gleißend auf, und eine Schockwelle aus purer Energie breitet sich von dort aus."
    "N´Evac hat Christopher soeben in den Würgegriff genommen und stemmt ihn hoch, als Christopher N´Evac mit beiden Händen fest in die Seiten schlägt und sich somit wieder befreit."
    "Sofort versetzt Christopher N´Evac einen kräftigen Kinnhaken."

    "Das Shuttle mit dem übrigen Außenteam hat die Erdatmosphäre gerade verlassen, da wird es von der energetischen Schockwelle eingeholt und hart getroffen, infolgedessen es unkontrolliert aus dem Orbit geschleudert wird."

    "Chief Solano ist es soeben gelungen, die Panzerabschottung zum Bereich des Maschinendecks mit dem Hyperdrive wieder zu öffnen: zusammen mit dem eingetroffenen Sicherheitstrupp eilt Solano zum Fuße des großen Hyperdrives."
    "Weiter oben sehen sie Captain Thomas und Colonel N´Evac gegeneinander kämpfen."
    "Gerade rammt N´Evac Christopher in vollem Lauf in Richtung des Geländers, um ihn darüber zu werfen: Christopher prallt mit dem Rücken schmerzhaft gegen das Geländer."
    "Doch dadurch erneut von Wut erfüllt, verpasst Christopher N´Evac gleich drei Kinnhaken unmittelbar nacheinander, die diesen ein paar Schritte zurück taumeln lassen."
    "Als N´Evac, jetzt selbst schnaubend vor Wut, zu einem brutalen Schlag mit beiden Armen gleichzeitig gegen Christopher ansetzt, duckt sich Christopher reaktionsschnell, blockt N´Evacs Schlag ab, fasst ihn jetzt selbst brutal am Hals und wirft N´Evac durch dessen eigenen Schwung, unter vollem Kraftaufwand brüllend, über sich und das Geländer hinweg."
    "N´Evac schlägt brutal auf dem untersten Deck unweit vor Solano und dem Sicherheitsteam auf: Solano und Thomas wechseln einen kurzen Blick miteinander."

    "Auf der Brücke der Phoenix geht soeben ein von Störungen durchzogener Notruf von Lieutenant Commander Reagan aus dem Shuttle ein."

    reg "Phoenix!"
    reg "..."
    reg "keine Kontrolle"
    reg "..."
    reg "..."
    reg "Steuerung funktionsunfähig"
    reg "..."
    reg "in wenigen Sekunden mit Ihnen kollidieren!"

    "Commander Stratter blickt gebannt auf, sodass sich ihrer und Lieutenant Mitchels Blick treffen: „Auf Aufprall vorbereiten!“"

    mit "Achtung, Kollision steht bevor!"

    "An Bord des Shuttles kann Nakamura im letzten Moment noch ein Zusatzaggregat für die Steuerdüsen reaktivieren, als ein Teil der Notversorgung wieder anspricht."
    "In Außenansicht driftet das sich langsam überschlagende Shuttle seitlich gegen die Phoenix und rammt diese dabei im Vorbeistreifen."
    "Das Maschinendeck wird von einem kräftigen Ruck durchstoßen, der das Sicherheitsteam und Solano fast von den Beinen reißt: oben klammert sich Christopher im letzten Moment am Geländer fest, bevor auch er hinüber gefallen wäre; außerdem ist ein Gasleck entstanden, sodass die Sicht jetzt erheblich beeinträchtigt wird."
    "Unten schlägt der auf dem Rücken liegende N´Evac plötzlich wieder seine Augen auf und springt mit einem Satz zurück in den Stand."
    "Er ergreift den neben ihm liegenden Plasmabrenner, der zuvor hier herunter gefallen ist, und wirft diesen mit aktivierter Plasmaflamme in den Weg des ausströmenden Gases, wodurch sogleich eine massive Flammenwand zwischen N´Evac und dem Sicherheitsteam auflodert."
    menu:
        "Verfolgen!":
            jump verfolgen
        "Laufen lassen":
            jump nichtverfolgen

label verfolgen:
    "Christopher blitzt N´Evac von der erhöhten Etage aus an und nimmt die Verfolgung auf, doch N´Evac entkommt schon in den Korridor hinaus."
    "Die Nachfolgen der bordweiten Erschütterung ausnutzend, kann N´Evac bis zum Shuttlehangar gelangen und schießt sich den Weg durch das Außenschott frei: Inmitten der explosiven Dekompression wird sein Shuttle hinaus geschleudert, wo er es schnell wieder unter Kontrolle bringt, um Kurs auf die S´Epazit zu setzen. Gleichzeitig nutzt Nakamura diese Gelegenheit, um das Shuttle nur mithilfe der Zusatzaggregate in die aufgesprengte Shuttlebucht hinein zu manövrieren."

    jump ende

label nichtverfolgen:
    "Die Nachfolgen der bordweiten Erschütterung ausnutzend, kann N´Evac bis zum Shuttlehangar gelangen und schießt sich den Weg durch das Außenschott frei: Inmitten der explosiven Dekompression wird sein Shuttle hinaus geschleudert, wo er es schnell wieder unter Kontrolle bringt, um Kurs auf die S´Epazit zu setzen. Gleichzeitig nutzt Nakamura diese Gelegenheit, um das Shuttle nur mithilfe der Zusatzaggregate in die aufgesprengte Shuttlebucht hinein zu manövrieren."

    jump ende

label ende:

    "{b}Im Hintergrund implodiert soeben die Erde in einem beängstigenden Szenario der totalen Auslöschung ins Nichts.{/b}"

    return
