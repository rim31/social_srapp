# social_srcap
test scrap social account

## sudject
Mettre en œuvre un processus automatisé pour vérifier l'état d'un compte ou d'un ensemble de comptes AC dans l'une des plateformes en ligne convenues.
Le processus sera idéalement implémenté en .NET ou en Python, et idéalement, il exposera une API REST avec l'entrée 
[hostingparty, account_id, account_handle, account_url] (au moins l'un des 3 identifiants doit être fourni) 
et output [hostingparty, account_id , account_handle, account_url, statut]. Le statut d'entrée définit si le compte est disponible ou non

## details
Le système pourrait être livré selon une approche par étapes: 
1. Implémentez une API REST comme décrit ci-dessus pour vérifier l'état de mock onlineaccount comme proof of concept
2. L'API REST peut vérifier l'état des comptes Facebook
3. L'API REST peut vérifier l'état des comptes Instagram
4. L'API REST peut vérifier l'état des sites Wordpress
5. Implémenter des mécanismes dans le processus de vérification d'état pour éviter d'être identifié comme un robot, comme utiliser plusieurs comptes pour accéder aux API ou aux applications des plateformes (avec un algorithme round-robin ou similaire, lorsque le contrôle anonyme est interdit ou augmente les chances d'être banni / bloqué), en changeant aléatoirement les étapes suivies pour vérifier l'état d'un compte, etc.
6. L'API REST peut vérifier l'état des comptes Google+
7. Implémentez un outil de ligne de commande qui, basé sur un fichier de configuration avec une liste de comptes et leur état attendu, peut évaluer si l'API REST échoue pour l'une des plates-formes. Le fichier de configuration doit contenir des comptes connus de beactive et des comptes connus pour être suspendus pour chaque plateforme.
8. L'API REST peut vérifier l'état des comptes Twitter
9. L'API REST peut vérifier l'état des comptes YouTube
10. Ajoutez la possibilité de prendre des captures d'écran des comptes dans le cadre du processus de vérification de statut. Les captures d'écran doivent être incluses dans la charge utile de l'API REST
11. L'API REST peut vérifier l'état des comptes Archive.org
12. L'API REST peut vérifier l'état des comptes Justpasteit

###sources
https://www.youtube.com/watch?v=7SWVXPYZLJM
