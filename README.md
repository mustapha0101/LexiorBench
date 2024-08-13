
Lexior Bench, une initiative visant à créer un benchmark pour évaluer les capacités de raisonnement juridique des grands modèles de langage (LLMs) dans le contexte spécifique du droit québécois. Inspiré par LEGALBENCH, Lexior Bench proposera une série de tâches couvrant des domaines clés du droit civil et du droit public québécois, tout en tenant compte des particularités linguistiques et culturelles du Québec. Ce benchmark a pour ambition de fournir aux chercheurs et aux professionnels du droit un outil pour mesurer l’efficacité des LLMs dans des tâches juridiques pertinentes, tout en offrant des perspectives sur l’adaptation des modèles à des contextes juridiques locaux.

---

# **Introduction**

Les récentes avancées en intelligence artificielle (IA) et en traitement automatique du langage naturel (TALN) ont permis de développer des modèles de langage capables de traiter des tâches juridiques complexes. Cependant, pour que ces modèles soient véritablement efficaces dans des contextes juridiques spécifiques, comme celui du Québec, il est nécessaire de disposer de benchmarks adaptés aux particularités locales.

C'est dans cette perspective qu'il est proposé de lancer **Lexior Bench**, une initiative dédiée à la création de benchmarks spécifiques pour l'évaluation des modèles de langage dans le domaine juridique québécois. Inspiré par LEGALBENCH, un projet collaboratif développé pour le droit américain, Lexior Bench aurait pour mission de fournir des outils d'évaluation adaptés aux spécificités du droit québécois, garantissant ainsi la pertinence et la fiabilité des modèles utilisés par les professionnels du droit au Québec.

En développant ces benchmarks locaux, Lexior Bench contribuerait non seulement à améliorer la qualité des outils d'IA disponibles pour le secteur juridique, mais aussi à renforcer la précision et l'efficacité des modèles de langage en contexte québécois. Cette initiative pourrait ainsi devenir un pilier essentiel pour l'évolution de l'intelligence artificielle appliquée au droit au Québec.


**LegalBench : Un pilier de l'évaluation des LLM dans le domaine juridique**

LEGALBENCH a pour but de tester et d’évaluer les capacités de raisonnement juridique des grands modèles de langage (LLMs). Conçu par un groupe interdisciplinaire d’experts en droit, LEGALBENCH propose 162 tâches variées, couvrant six types distincts de raisonnement juridique. Ce benchmark repose sur des cadres juridiques bien établis, permettant une évaluation précise et pertinente des capacités des LLMs. Une des forces de LEGALBENCH est son approche collaborative dans la création des tâches, où des professionnels du droit ont joué un rôle clé, garantissant que chaque tâche soit non seulement théoriquement intéressante, mais aussi pratiquement utile. Ce projet met également en lumière l’importance des stratégies d’ingénierie des prompts, explorant comment ces ajustements peuvent améliorer les performances des modèles sur des tâches spécifiques. Le document fournit une analyse empirique de 20 modèles de langage, révélant des tendances de performance et comparant les capacités de modèles populaires tels que GPT. LEGALBENCH se distingue par sa capacité à engager à la fois les développeurs et les professionnels du droit dans un dialogue commun, grâce à un vocabulaire partagé et une évaluation rigoureuse

Référence : [https://hazyresearch.stanford.edu/legalbench/](https://hazyresearch.stanford.edu/legalbench/)

# **Contexte et motivation :**

Le droit québécois, principalement basé sur le Code civil, diffère sensiblement du système de common law dominant en Amérique du Nord. Cette spécificité, combinée à l’usage prédominant du français, pose des défis uniques pour les LLMs. Lexior Bench répond à ces défis en offrant une plateforme d’évaluation adaptée, permettant de tester les capacités des modèles dans des scénarios qui reflètent la réalité du droit québécois.

# **Construction de Lexior Bench**

Lexior Bench sera élaboré en collaboration avec des experts en droit québécois et des chercheurs en IA. Ce benchmark inclura des tâches couvrant divers domaines du droit civil (comme les obligations, les contrats, et la responsabilité civile) et du droit public (y compris le droit administratif et le droit constitutionnel). Les tâches seront conçues pour tester six types de raisonnement juridique, à savoir l’identification des problèmes, le rappel des règles, l’application des règles, la conclusion des règles, l’interprétation et la compréhension rhétorique.

# **Typologie du raisonnement juridique**

Suivant l’exemple de LEGALBENCH, Lexior Bench catégorisera les tâches en fonction des types de raisonnement juridique :

1. **l’identification des problèmes**
2. **le rappel des règles**
3. **l’application des règles**
4. **la conclusion des règles**
5. **l’interprétation et la compréhension rhétorique**

Cette typologie sera essentielle pour comprendre comment les LLMs performent dans des scénarios réels et comment ils peuvent être améliorés pour répondre aux exigences du droit québécois.

# **Stratégies d’ingénierie des prompts**

Lexior Bench explorera différentes stratégies d’ingénierie des prompts pour améliorer les performances des modèles. Les résultats de ces expérimentations offriront des pistes intéressantes pour l’optimisation des LLMs dans le cadre juridique

# **Collaboration interdisciplinaire**

L’une des leçons clés de LEGALBENCH est l’importance de la collaboration entre les professionnels du droit et les experts en IA. Lexior Bench s’inscrira dans cette lignée en encourageant une participation active des juristes québécois dans la conception et l’amélioration des tâches d’évaluation, garantissant ainsi la pertinence des benchmarks pour les utilisateurs finaux.

# **Conclusion et travaux futurs**

Lexior Bench constitue une étape cruciale vers le développement d’un outil d’évaluation adapté aux spécificités du droit québécois, permettant ainsi d’améliorer l’efficacité des LLMs dans ce contexte particulier. Bien que ce projet en soit à ses débuts, il représente une avancée prometteuse pour l’intégration des technologies d’intelligence artificielle dans le domaine juridique au Québec. À l’avenir, nous prévoyons d’élargir le benchmark en ajoutant de nouvelles tâches et en affinant les modèles sur la base des retours d’expérience. Cette initiative ouvre la voie à une collaboration interdisciplinaire renforcée, avec pour objectif d’optimiser les pratiques juridiques à travers l’IA, tout en respectant les particularités locales du système juridique québécois.




# 📜 LegalBench

<div align="center">

The LegalBench project is an ongoing open science effort to collaboratively curate tasks for evaluating legal reasoning in English large language models (LLMs). The benchmark currently consists of 162 tasks gathered from 40 contributors.

[**Website**](https://hazyresearch.stanford.edu/legalbench/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Data**](https://huggingface.co/datasets/nguha/legalbench)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Paper**](https://arxiv.org/abs/2308.11462)
</div>

