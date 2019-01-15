* À quoi sert le système d'exploitation sur un ordinateur ?
- Il met en place un régime d'oppression sur les micropuces
  informatiques.
- Il est responsable de charger le CSS dans les pages web HTML.
- Il produit le bytecode Java à partir du code source Java.
- Il recharge la pile des appels avec du courant alternatif.
- Il permet de visualiser le débogage dans un Traceback Python.
- Il détecte les erreurs de syntaxe dans un code source C.
- Il est responsable de la détection des variables Python non
  utilisées afin de prévoir leur libération.
+ Il gère les entrées/sorties et les interactions avec le monde extérieur.
+ Il propose des interfaces de haut niveau avec les ressources matériels.
+ Il cache les spécificités matériels du hardware (avec des pilotes).
+ Il permet un partage judicieux des ressources entre les utilisateurs.
+ Il permet un partage judicieux des ressources entre les différents
  programmes.
+ Il assure l'intégrité et la cohérence des données de la machine.
+ Il fait l'interface entre le matériel (hardware) et les logiciels
  applicatifs (software).


* Parmi les opérations informatiques suivantes, laquelle(lesquels)
  sollicite(nt) le système d'exploitation ?
- Changer la pile de carte mère alimentant la puce du BIOS.
- Nettoyer les circuits imprimés et les dissipateurs de chaleurs avec
  de l'air pulsé.
- Changer une touche non fonctionnelle du clavier.
- Calculer la complexité d'un algorithme de tri.
- Établir une bijection entre les nombres binaire sur 32 bits et les
  entiers positifs plus petits que 4294967296.
- Vérifier que les bases de données sont structurés en forme normale.
- Utiliser une méthode diviser pour régner.
+ Lancer l'exécution d'un programme.
+ Sauvegarder un fichier.
+ Parcourir le contenu d'un répertoire.
+ Bouger le pointeur de la souris à l'écran.
+ Éteindre le système avant une décharge complète d'une batterie
  Lithium.
+ Partager la puissance de calcul du processeur entre plusieurs
  programmes exécutés en même temps.
+ Demander de la mémoire pérenne supplémentaire dans un programme C
  (avec malloc).


* Parmi les organes matériels suivant, lequel ou lesquels sont vitaux
  pour un ordinateur (un ordinateur ne pourrait ainsi pas fonctionner
  sans un de ces organes) ?
- une souris
- un écran
- une imprimante
- un clavier
- un respirateur artificiel
- un défibrillateur
- une chaise
+ un microprocesseur central
+ de la mémoire vive
+ une carte mère


* De nos jours, les microprocesseurs contiennent dans leur coeur
- soit 2, soit 4 transistors
- une dizaine de transistors
- jamais plus de 128 transistors
- quelques centaines de transistors
+ autour d'un milliard de transistors


* Cochez les caractéristiques possédés par la mémoire vive d'un
  ordinateur
- C'est une mémoire lente en lecture.
- Cette mémoire utilise des disques magnétiques tournant à haute vitesse.
- Cette mémoire reste pérenne même si elle n'est plus sous tension.
- C'est la mémoire qu'on trouve en plus grande capacité dans un ordinateur.
- Cette mémoire à besoin d'être rembobinée avant utilisation.
+ C'est la mémoire principalement utilisé lors de la réalisation de calculs.
+ Chaque morceau ou cellule de cette mémoire est accessible directement via son adresse.
+ Les ordinateurs en comportent plusieurs GigaOctets de nos jours.
+ Cette mémoire est montée sur des barrettes amovibles clipsées sur carte mère.


* Quels sont les objectifs d'un système d'exploitation ?
- Éviter que la souris attrape des puces.
- Assurer que l'écran ne chauffe pas trop.
- Augmenter la durée de vie des cartouches d'encres en limitant l'encre utilisée.
- Augmenter les bénéfices sans revaloriser les salaires.
- Empêcher les pauvres de devenir riche.
+ Être le plus léger possible pour ne pas alourdir les tâches de calculs.
+ Faire en sorte que les données soient toujours cohérentes.
+ Virtualise les ressources et les attribue comme un chef d'orchestre.
+ Sécuriser le matériel et rattraper les erreurs non critique.
+ Permettre le partage de ses ressources.
+ Augmenter l'expérience de l'utilisateur en interagissant efficacement avec le monde extérieur.
+ Proposer des interfaces standardisés pour chaque ressource.


* Parmi les logiciels suivants, lesquels sont des systèmes d'exploitation
- Photoshop
- Powerpoint
- Excel
- PostgreSQL
- Le capitalisme
- Chrome
- Opéra
- Firefox
- Konqueror
- L'éducation nationale française
+ Unix
+ Linux
+ Mac OS X
+ Windows


* Que contient un système d'exploitation en termes logiciels ?
- Des algorithmes de traitement d'images.
- Des lecteurs de fichiers mp3.
- Des MMORPG.
- Un synthétiseur vocal.
- Le code du travail.
+ Des piles et des files pour collecter des tâches et des événements.
+ Des mémoires tampons et des buffers un peu partout.
+ Des mécanismes de gestion de la temporalité.
+ Virtualisation les mémoires pour les partager efficacement.
+ Structuration, organisation et maintenance des données pérennes.
+ Mécanisme de sécurité, de mise à jour et de diagnostique.


* Quels sont les spécificités des systèmes d'exploitation de type Unix ?
- Unix ne propose que des sessions graphiques.
- Un seul utilisateur peut se loger à la fois.
- Unix augmente les capacités des barrettes mémoires.
- Le développement d'Unix est focalisé sur le user-friendly au détriment de la robustesse.
- Unix tente de cacher les bogues pour éviter la mauvaise pub.
- Le code source de ces systèmes est ouvert.
+ Unix attribut des droits spécifiques à tous les fichiers ainsi qu'aux processus.
+ Ils sont multi-utilisateurs et multi-tâches.
+ Tout est fichier en Unix.
+ Ils sont très largement écrit avec le langage C.
+ Ils sont apparus vers 1970.
+ La philosophie d'Unix est de proposer des programmes basiques mais
  robustes pouvant se combiner très facilement.


* Quels sont les conséquences de l'idée de Von Neumann de mélanger les
  données et les programmes dans la mémoire et de les considérer sur
  un pied d'égalité ?
- Paf, ça fait des chocapics !
- Ça permet de limiter l'énergie utiliser par la RAM.
- Ça permet d'augmenter la cadence du CPU (overclocking).
- Ça limite la latence lors des chargements (lags).
+ Ça permet de faire des programme prenant en argument d'autre programme.
* Ça permet de considérer des programmes qui fabriquent d'autres programmes.
+ Ça permet une montée en puissance des fonctionnalités via des
  niveaux d'abstraction : compilateur, bibliothèque bas-niveau,
  framework évolué, application haut niveau (différent langage et
  traduction d'un niveau à un autre).


* Quelles sont les caractéristiques d'une unité arithmétique et logique ?
- Elle permet de connecter l'ordinateur à internet.
- Elle évite les fuites mémoires dans les gros programmes.
- Elle est responsable de la mise à jour du système.
- Elle facilite la portabilité des codes sources entre les systèmes.
- Elle diminue la complexité des algorithmes de tris.
+ Elle possèdent des jeux d'instructions basiques pouvant être exécutés très rapidement.
+ Elle manipule des mots machines de taille 64 bits ou plus de nos jours.
+ Elle exploite des registres et mémoires caches très proche physiquement de ces circuits.
+ Elle ne manipule que des données numériques binaires.


* Quels sont les éléments définissant l'architecture de Von Neumann
- Le processeur, la carte mère, la mémoire vive et le couple clavier/écran.
- L'unité centrale, l'écran, le clavier et la souris.
- L'unité arithmétique et logique, la mémoire vive, la mémoire morte et les entrées/sorties.
- L'unité arithmétique et logique, la mémoire, le quartz cadenceur et le bus central.
+ L'unité arithmétique et logique, l'unité de contrôle, la mémoire et les entrées/sorties.
