# Réseau Résiduel-Contractant Profond : un algorithme d’IA adapté aux données fortement bruitées

Le Réseau Résiduel-Contractant Profond est une version améliorée du Réseau de Neurones Résiduel Profond, qui est en fait une intégration du Réseau de Neurones Résiduel Profond, du mécanisme d'attention et de la fonction de seuillage doux.

Dans une certaine mesure, le principe de fonctionnement du Réseau Résiduel-Contractant Profond peut être interprété comme suit : il utilise le mécanisme d'attention pour identifier les caractéristiques non pertinentes et les met à zéro par le biais de la fonction de seuillage doux ; ou, en d'autres termes, il utilise le mécanisme d'attention pour identifier les caractéristiques pertinentes et les conserver, renforçant ainsi la capacité du Réseau de Neurones Profond à extraire les caractéristiques utiles à partir de signaux bruités.

**1.Contexte et motivations**

Premièrement, lors de la classification des échantillons, ceux-ci contiennent inévitablement une certaine forme de bruit, tel que le bruit gaussien, le bruit rose ou le bruit laplacien. Dans un sens plus large, les échantillons sont susceptibles de contenir des informations non pertinentes pour la tâche de classification en cours ; ces informations peuvent également être considérées comme du bruit. Ce bruit risque d'affecter négativement la performance de la classification. (Le seuillage doux est d'ailleurs une étape cruciale dans de nombreux algorithmes de débruitage de signal.)

Par exemple, lors d'une conversation au bord d'une route, le signal vocal peut être mêlé à des bruits parasites comme des klaxons ou des bruits de roulement. Lorsque ces signaux sonores sont traités pour la reconnaissance vocale, la performance de celle-ci est inévitablement affectée par ces bruits. Du point de vue de l'apprentissage profond, les caractéristiques correspondant à ces bruits parasites devraient être supprimées au sein du réseau de neurones profond, afin d'éviter de nuire au résultat de la reconnaissance vocale.

Deuxièmement, même au sein d'un même jeu de données, la quantité de bruit varie souvent d'un échantillon à l'autre. (Ce principe présente une analogie avec le mécanisme d'attention ; dans un jeu de données d'images, par exemple, la position de l'objet cible peut varier d'une image à l'autre. Le mécanisme d'attention est capable, pour chaque image, d'identifier la localisation de cet objet cible.)

Par exemple, lors de l'entraînement d'un classifieur de chats et de chiens, parmi cinq images étiquetées comme « chien », la première pourrait contenir à la fois un chien et une souris, la deuxième un chien et une oie, la troisième un chien et un poulet, la quatrième un chien et un âne, et la cinquième un chien et un canard. Durant l'entraînement du classifieur, nous sommes inévitablement confrontés aux interférences causées par ces objets non pertinents — la souris, l'oie, le poulet, l'âne et le canard — ce qui entraîne une baisse de la précision de la classification. Si nous parvenions à identifier ces objets non pertinents et à supprimer les caractéristiques qui leur correspondent, il serait alors possible d'améliorer la précision du classifieur de chats et de chiens.

**2.Le seuillage doux**

Le seuillage doux, qui est une étape fondamentale de nombreux algorithmes de débruitage de signal, consiste à mettre à zéro les caractéristiques dont la valeur absolue est inférieure à un certain seuil, et à effectuer une contraction en direction de zéro sur celles dont la valeur absolue est supérieure à ce même seuil. Il peut être mis en œuvre au moyen de la formule suivante :

```math
y = \begin{cases}
x - \tau & x > \tau \\
0 & -\tau \le x \le \tau \\
x + \tau & x < -\tau
\end{cases}
```

La dérivée de la sortie du seuillage doux par rapport à l'entrée est :

```math
\frac{\partial y}{\partial x} = \begin{cases}
1 & x > \tau \\
0 & -\tau \le x \le \tau \\
1 & x < -\tau
\end{cases}
```

D'après ce qui précède, la dérivée du seuillage doux est soit 1, soit 0. Cette propriété est identique à celle de la fonction d'activation ReLU. Par conséquent, le seuillage doux peut également réduire le risque que les algorithmes d'apprentissage profond soient confrontés à la disparition du gradient et à l'explosion du gradient.

Pour la fonction de seuillage doux, la définition du seuil doit satisfaire à deux conditions : premièrement, le seuil doit être un nombre positif ; deuxièmement, il ne doit pas être supérieur à la valeur maximale du signal d'entrée, sans quoi la sortie serait entièrement nulle.

Parallèlement, il est préférable que le seuil satisfasse également à une troisième condition : chaque échantillon devrait posséder son propre seuil, défini en fonction de son niveau de bruit.

En effet, le niveau de bruit varie souvent d'un échantillon à l'autre. Il est fréquent, par exemple, que dans un même jeu de données, l'échantillon A contienne moins de bruit et l'échantillon B en contienne davantage. Dans ce cas, lors de l'application du seuillage doux au sein d'un algorithme de débruitage, l'échantillon A devrait se voir appliquer un seuil plus élevé, et l'échantillon B un seuil plus faible. Bien que dans les réseaux de neurones profonds, ces caractéristiques et seuils perdent leur signification physique explicite, le principe fondamental reste analogue. Autrement dit, chaque échantillon devrait avoir un seuil indépendant, déterminé par son propre niveau de bruit.

**3.Le mécanisme d'attention**

Le mécanisme d'attention est relativement simple à comprendre dans le domaine de la vision par ordinateur. Le système visuel des animaux peut balayer rapidement une zone entière pour y détecter un objet cible, puis focaliser son attention sur cet objet afin d'en extraire davantage de détails, tout en inhibant les informations non pertinentes. Pour plus de détails, veuillez vous référer aux publications spécialisées sur le mécanisme d'attention.

Le réseau Squeeze-and-Excitation (SENet) est une méthode d'apprentissage profond relativement récente qui relève du mécanisme d'attention. Pour différents échantillons, la contribution de chaque canal de caractéristiques à la tâche de classification est souvent inégale. SENet utilise un petit sous-réseau pour obtenir un ensemble de poids, qui sont ensuite multipliés par les caractéristiques de chaque canal respectif afin d'en moduler l'amplitude. Ce processus peut être interprété comme l'application d'une attention d'intensité variable à chaque canal de caractéristiques.

De cette manière, chaque échantillon obtient son propre ensemble de poids. En d'autres termes, les poids de deux échantillons quelconques sont différents. Dans SENet, le cheminement spécifique pour obtenir ces poids est le suivant : « Pooling global → Couche entièrement connectée → Fonction ReLU → Couche entièrement connectée → Fonction sigmoïde ».


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
