# Réseau Résiduel-Contractant Profond : un algorithme d’IA adapté aux données fortement bruitées

Le Réseau Résiduel-Contractant Profond est une version améliorée du Réseau de Neurones Résiduel Profond, qui est en fait une intégration du Réseau de Neurones Résiduel Profond, du mécanisme d'attention et de la fonction de seuillage doux.

Dans une certaine mesure, le principe de fonctionnement du Réseau Résiduel-Contractant Profond peut être interprété comme suit : il utilise le mécanisme d'attention pour identifier les caractéristiques non pertinentes et les met à zéro par le biais de la fonction de seuillage doux ; ou, en d'autres termes, il utilise le mécanisme d'attention pour identifier les caractéristiques pertinentes et les conserver, renforçant ainsi la capacité du Réseau de Neurones Profond à extraire les caractéristiques utiles à partir de signaux bruités.

**Contexte et motivations**

Premièrement, lors de la classification des échantillons, ceux-ci contiennent inévitablement une certaine forme de bruit, tel que le bruit gaussien, le bruit rose ou le bruit laplacien. Dans un sens plus large, les échantillons sont susceptibles de contenir des informations non pertinentes pour la tâche de classification en cours ; ces informations peuvent également être considérées comme du bruit. Ce bruit risque d'affecter négativement la performance de la classification. (Le seuillage doux est d'ailleurs une étape cruciale dans de nombreux algorithmes de débruitage de signal.)

Par exemple, lors d'une conversation au bord d'une route, le signal vocal peut être mêlé à des bruits parasites comme des klaxons ou des bruits de roulement. Lorsque ces signaux sonores sont traités pour la reconnaissance vocale, la performance de celle-ci est inévitablement affectée par ces bruits. Du point de vue de l'apprentissage profond, les caractéristiques correspondant à ces bruits parasites devraient être supprimées au sein du réseau de neurones profond, afin d'éviter de nuire au résultat de la reconnaissance vocale.
Deuxièmement, même au sein d'un même jeu de données, la quantité de bruit varie souvent d'un échantillon à l'autre. (Ce principe présente une analogie avec le mécanisme d'attention ; dans un jeu de données d'images, par exemple, la position de l'objet cible peut varier d'une image à l'autre. Le mécanisme d'attention est capable, pour chaque image, d'identifier la localisation de cet objet cible.)

Par exemple, lors de l'entraînement d'un classifieur de chats et de chiens, parmi cinq images étiquetées comme « chien », la première pourrait contenir à la fois un chien et une souris, la deuxième un chien et une oie, la troisième un chien et un poulet, la quatrième un chien et un âne, et la cinquième un chien et un canard. Durant l'entraînement du classifieur, nous sommes inévitablement confrontés aux interférences causées par ces objets non pertinents — la souris, l'oie, le poulet, l'âne et le canard — ce qui entraîne une baisse de la précision de la classification. Si nous parvenions à identifier ces objets non pertinents et à supprimer les caractéristiques qui leur correspondent, il serait alors possible d'améliorer la précision du classifieur de chats et de chiens.

**Références**

Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.

**BibTeX**
```bibtex
@article{Zhao2020,
  author    = {Minghang Zhao and Shisheng Zhong and Xuyun Fu and Baoping Tang and Michael Pecht},
  title     = {Deep Residual Shrinkage Networks for Fault Diagnosis},
  journal   = {IEEE Transactions on Industrial Informatics},
  year      = {2020},
  volume    = {16},
  number    = {7},
  pages     = {4681-4690},
  doi       = {10.1109/TII.2019.2942898}
}
```
