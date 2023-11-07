<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DavidScanu/My-Credit" target="_blank">
    <img src="https://avatars.githubusercontent.com/u/70485959?v=4" alt="Logo" width="120" height="120">
  </a>
  <h3>My Credit - Back-End (API)</h3>
  <h3>Développement de l'API de l'application "My Credit".</h3>
</div>
<ul>
<li><a href="https://api-isen-g4-6efab73bbf58.herokuapp.com/docs" target="_blank">API - Documentation de l'API</a></li>
<li><a href="https://my-credit-isen-group-4.streamlit.app/" target="_blank">APP - Demonstration de l'app Streamlit</a></li>
<li><a href="https://docs.google.com/presentation/d/1ok4Yt8M9RsFvn8HT-luv4DpzHH3nC9ZiAnbYC8zrWwc/edit?usp=sharing" target="_blank">Documment de formation - Kevin Duranty</a></li>
</ul>

<!-- Built With -->
### Built With

[![fastapi][fastapi-shield]][fastapi-url]


## Groupe 4
- Antoine Ancelin (Modèle)
- Charley Lebarbier (Front-end)
- David Scanu (Back-end, Tech lead)

## Améliorations possibles
- Changer l'algorithme du **modèle** (XGBoost est trop lourd pour Heroku)
- Utiliser **OneHotEncoding** pour encoder les features
- Utiliser un **pipeline** pour sauvegarder l'encoder et le scaler
- Ajouter **MLFlow**

<!-- ABOUT THE PROJECT -->
## Contexte du projet

La banque pour laquelle vous travaillez veut publier assez rapidement son POC (Proof of Concept - Preuve de concept) : Une application permettant à un utilisateur de faire une demande de crédit en ligne.

En tant que data scientist, machine learning engineer, - installer et créer un environment de développement correct :

- mettre en place un environement de développement Git/Github
- entrainer un modèle de classification binaire
- déployer l'API et le modèle dans le cloud
- déployer une application front à l'aide de streamlit

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Modalités pédagogiques

Le projet sera à réaliser en trois jours, chaque équipe est constituée de 3 développeurs, une par feature :
- FRONT (developpement de l'application front)
- BACK (développement de l'API back)
- MODEL (entrainemment du modèle).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

### Partie 1 - Configuration du projet

- ✔️ Créez des groupes de 3 personnes maximum puis répartissez vous les tâches (Front, Back, Model).
- ✔️ Désignez un tech lead qui aura à sa charge le répertoir du projet Github. → Le Tech Lead doit faire un fork du projet Github suivant → Ajouter les membres de son équipe au projet github. → Copiez le tablaeu suivant.
- ✔️ Téléchargez le logiciel Github Desktop puis clonnez en local votre projet.
- ✔️ Créez un fichier **Readme** sur chacune des branches dont vous avez la charge puis faites un commit et un push afin de vérifier la bonne configuration du projet.

### Partie 2 - Développement des features

- ✔️ **Développez le Front** : Le front de l’API sera développez avec le Framework Streamlit. → Présence d’un formulaire permettant à l’utilisateur de renseigner ses informations personnelles. → Le programme fait une requête POST à l’API. → Le programme affiche la réponse de l’accord de crédit.
- ✔️ **Concevez le modèle** : Le modèle de classification sera développez avec la bibliothèque de votre choix (Sklearn, Tensorflow, PyTorch). → Le modèle doit avoir une accuracy d’au moins 90%. → Les données passez au modèle doivent être standardisées. → Le modèle doit être sauvegardée au format pickle.
- ✔️ **Développez l’API** : L’API du sera développée avec le framework FastAPI. → Un point de terminaison predict doit être créé avec une méthode POST. → Le point de terminaison predict gère les structure de données avec la bibliothèque pydantic. → La réponse doit être sous forme d’une chaîne de caractère ou sous forme d’un json.

### Partie 3 - Développement de Tests Unitaires

- ✔️ **Testez le modèle** : → Testez la fonction qui importe les données. → Testez la fonction qui standardise les données. → Testez la fonction qui entraîne le modèle.
- ✔️ **Testez l’API** : → Testez la réponse de l’API → Testez la sortie de l’api → Testez le type de données passées en entrée.
- ✔️ Déployez vos tests unitaires et déployez votre API sur Heroku à l'aide de Github actions.
​
### Partie 4 - Monitoring de modèle avec MLFlow

- ❌ Déployez une application **MLFlow** puis déployez la sur Heroku à l'aide de Docker.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

- Antoine Ancelin
- Charley Lebarbier
- David Scanu - [@davidsca_](https://twitter.com/davidsca_) - davidscanu14@gmail.com

Project Link: [https://github.com/DavidScanu/My-Credit](https://github.com/DavidScanu/My-Credit)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Contributors -->
[contributors-shield]: https://img.shields.io/github/contributors/DavidScanu/My-Credit
[contributors-url]: https://github.com/DavidScanu/My-Credit/graphs/contributors

<!-- Forks -->
[forks-shield]: https://img.shields.io/github/forks/DavidScanu/My-Credit
[forks-url]: https://img.shields.io/github/forks/DavidScanu/My-Credit

<!-- Stars -->
[stars-shield]: https://img.shields.io/github/stars/DavidScanu/My-Credit
[stars-url]: https://img.shields.io/github/stars/DavidScanu/My-Credit

<!-- Linkedin -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/davidscanu14/

[product-screenshot]: images/screenshot.png

<!-- Next -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/

<!-- React -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/

<!-- Vue -->
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/

<!-- Angular -->
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/

<!-- Svelte -->
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/

<!-- Laravel -->
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com

<!-- Bootstrap -->
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

<!-- JQuery -->
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

<!-- Fast API -->
[fastapi-shield]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white
[fastapi-url]: https://fastapi.tiangolo.com/fr/
