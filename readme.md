jeu d’échec

 * tour par tour en local
 * on lance un tournoi en 4 manches.
    * comment qu’on lance-t-il un tournoi didon ?
    * on run le programme, un menu nous est présenté:
        1. commencer le tournoi
            * 4 manches = 16 joueurs
            * une manche: l’utilisateur définira qui a gagné/perdu/match nul
        2. imprimer le rapport du tournoi
            * toutes les actions des joueurs doivent être enregistrés afin de pouvoir reprendre une partie
                * reprise de partie: affichage de la dernière action et de la prochaine action à faire
        3. ajouter un joueur
            * les joueurs doivent s’enregistrer pour démarrer un tournoi.
                * l’enregistrement se fait en CLI avec un prompt firtname/lastname/date de naissance
        4. quitter

second temps :

 * définir le nombre de manches par tournoi.
 * deux joueurs ne devraient pas se rencontrer plus d’une fois.

implpémentation :

 * les données d’enregistrement sont sauvegardées dans JSON
 * modèle MVC, en python
 * BDD

 A faire : le fichier players.json reste vide