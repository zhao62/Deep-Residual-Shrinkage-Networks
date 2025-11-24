# Tiefes Residual-Schrumpfungs-Netzwerk (Deep Residual Shrinkage Network): Eine Methode der künstlichen Intelligenz für stark verrauschte Daten

**Das Tiefe Residual-Schrumpfungs-Netzwerk (Deep Residual Shrinkage Network, DRSN) ist eine verbesserte Version des Tiefen Residual-Netzwerks (Deep Residual Network, ResNet). Es handelt sich im Grunde um eine Integration von ResNet, Aufmerksamkeitsmechanismen (Attention Mechanisms) und der weichen Schwellenwertfunktion (Soft Thresholding Function).**

**In gewisser Weise kann das Funktionsprinzip des Tiefen Residual-Schrumpfungs-Netzwerks so verstanden werden: Durch einen Aufmerksamkeitsmechanismus werden unwichtige Merkmale bemerkt und durch die weiche Schwellenwertfunktion auf Null gesetzt (Schrumpfung); oder anders ausgedrückt, wichtige Merkmale werden durch den Aufmerksamkeitsmechanismus bemerkt und beibehalten. Dadurch wird die Fähigkeit des tiefen neuronalen Netzwerks verstärkt, nützliche Merkmale aus verrauschten Signalen zu extrahieren.**

## 1. Forschungsmotivation
**Zunächst enthalten Datenstichproben (Samples) bei der Klassifizierung unvermeidlich ein gewisses Rauschen, wie zum Beispiel Gaußsches Rauschen, Rosa Rauschen oder Laplace-Rauschen.** Im weiteren Sinne enthalten die Stichproben wahrscheinlich Informationen, die für die aktuelle Klassifizierungsaufgabe irrelevant sind; diese Informationen können ebenfalls als Rauschen verstanden werden. Dieses Rauschen kann die Klassifizierungswirkung nachteilig beeinflussen. (Die weiche Schwellenwertsetzung ist ein entscheidender Schritt in vielen Algorithmen zur Signalentstörung).

Ein Beispiel: Bei einem Gespräch am Straßenrand können sich Autohupen und Reifengeräusche in die Sprachsignale mischen. Bei der Spracherkennung dieser Signale wird das Ergebnis unvermeidlich durch diese Hup- und Reifengeräusche beeinträchtigt. Aus der Perspektive des Deep Learning (Tiefes Lernen) sollten die Merkmale, die diesen Hup- und Reifengeräuschen entsprechen, innerhalb des tiefen neuronalen Netzwerks gelöscht werden, um negative Auswirkungen auf die Spracherkennung zu vermeiden.

**Zweitens ist der Rauschanteil oft auch innerhalb desselben Datensatzes von Stichprobe zu Stichprobe unterschiedlich.** (Dies weist Parallelen zum Aufmerksamkeitsmechanismus auf; betrachtet man beispielsweise einen Bilddatensatz, so kann die Position des Zielobjekts in jedem Bild variieren; der Aufmerksamkeitsmechanismus kann sich gezielt auf die Position des Zielobjekts in jedem einzelnen Bild fokussieren).

Beispiel: Beim Training eines Klassifikators für Katzen und Hunde könnten bei 5 Bildern mit dem Label „Hund“ folgende Situationen auftreten: Bild 1 enthält Hund und Maus, Bild 2 Hund und Gans, Bild 3 Hund und Huhn, Bild 4 Hund und Esel, Bild 5 Hund und Ente. Beim Training des Katzen-Hunde-Klassifikators werden wir unvermeidlich durch die irrelevanten Objekte (Maus, Gans, Huhn, Esel und Ente) gestört, was zu einer Verringerung der Klassifizierungsgenauigkeit führt. Wenn wir in der Lage sind, diese irrelevanten Mäuse, Gänse, Hühner, Esel und Enten zu bemerken und die ihnen entsprechenden Merkmale zu löschen, lässt sich die Genauigkeit des Klassifikators wahrscheinlich erhöhen.

## 2. Weiche Schwellenwertsetzung (Soft Thresholding)
**Die weiche Schwellenwertsetzung (Soft Thresholding) ist der Kernschritt vieler Algorithmen zur Signalentstörung. Dabei werden Merkmale, deren Absolutbetrag kleiner als ein bestimmter Schwellenwert ist, gelöscht, und Merkmale, deren Absolutbetrag größer als dieser Schwellenwert ist, werden in Richtung Null „geschrumpft“ (daher der Begriff *Schrumpfung*).** Dies kann durch folgende Formel realisiert werden:

$$
y = \begin{cases} 
x - \tau & x > \tau \\ 
0 & -\tau \le x \le \tau \\ 
x + \tau & x < -\tau 
\end{cases}
$$

Die Ableitung der Ausgabe nach der Eingabe bei der weichen Schwellenwertsetzung lautet:

$$
\frac{\partial y}{\partial x} = \begin{cases} 
1 & x > \tau \\ 
0 & -\tau \le x \le \tau \\ 
1 & x < -\tau 
\end{cases}
$$

Wie oben ersichtlich, ist die Ableitung der weichen Schwellenwertsetzung entweder 1 oder 0. Diese Eigenschaft ist identisch mit der der ReLU-Aktivierungsfunktion. Daher kann die weiche Schwellenwertsetzung auch das Risiko verringern, dass Deep-Learning-Algorithmen Probleme mit verschwindenden (Gradient Vanishing) oder explodierenden Gradienten (Gradient Exploding) bekommen.

**In der weichen Schwellenwertfunktion muss das Setzen des Schwellenwerts zwei Bedingungen erfüllen: Erstens muss der Schwellenwert positiv sein; zweitens darf der Schwellenwert nicht größer als der Maximalwert des Eingangssignals sein, da sonst die Ausgabe vollständig Null wäre.**

**Gleichzeitig sollte der Schwellenwert idealerweise eine dritte Bedingung erfüllen: Jede Stichprobe sollte, basierend auf ihrem eigenen Rauschgehalt, ihren eigenen unabhängigen Schwellenwert haben.**

Dies liegt daran, dass der Rauschgehalt vieler Stichproben oft unterschiedlich ist. Beispielsweise kommt es häufig vor, dass in demselben Datensatz Stichprobe A weniger Rauschen enthält und Stichprobe B mehr Rauschen. Wenn dann in einem Algorithmus zur Entstörung die weiche Schwellenwertsetzung angewendet wird, sollte Stichprobe A einen größeren Schwellenwert und Stichprobe B einen kleineren Schwellenwert verwenden. Obwohl diese Merkmale und Schwellenwerte in einem tiefen neuronalen Netzwerk ihre explizite physikalische Bedeutung verlieren, ist das grundlegende Prinzip ähnlich. Das heißt, jede Stichprobe sollte basierend auf ihrem eigenen Rauschgehalt über einen eigenen, unabhängigen Schwellenwert verfügen.

## 3. Aufmerksamkeitsmechanismus (Attention Mechanism)
Der Aufmerksamkeitsmechanismus ist im Bereich Computer Vision (Maschinelles Sehen) relativ leicht zu verstehen. Das visuelle System von Tieren kann schnell einen gesamten Bereich scannen, das Zielobjekt entdecken und dann die Aufmerksamkeit auf dieses Objekt konzentrieren, um mehr Details zu extrahieren und gleichzeitig irrelevante Informationen zu unterdrücken. Für Details wird auf entsprechende Literatur zum Aufmerksamkeitsmechanismus verwiesen.

Das Squeeze-and-Excitation Network (SENet) ist eine neuere Deep-Learning-Methode, die auf dem Aufmerksamkeitsmechanismus basiert. In verschiedenen Stichproben ist der Beitrag unterschiedlicher Merkmalskanäle (Feature Channels) zur Klassifizierungsaufgabe oft unterschiedlich groß. SENet verwendet ein kleines Sub-Netzwerk, um einen Satz von Gewichtungen zu erhalten, und multipliziert diese Gewichtungen dann jeweils mit den Merkmalen der einzelnen Kanäle, um die Größe der Merkmale in den Kanälen anzupassen. Dieser Prozess kann so aufgefasst werden, als ob unterschiedliche Grade an Aufmerksamkeit auf die jeweiligen Merkmalskanäle angewendet würden.

Bei diesem Ansatz hat jede Stichprobe ihren eigenen, unabhängigen Satz von Gewichtungen. Mit anderen Worten: Die Gewichtungen zweier beliebiger Stichproben sind unterschiedlich. Im SENet ist der konkrete Pfad zum Erhalt der Gewichtungen: „Globales Pooling (Global Pooling) $\rightarrow$ Fully Connected Layer (Vollständig verbundene Schicht) $\rightarrow$ ReLU-Funktion $\rightarrow$ Fully Connected Layer $\rightarrow$ Sigmoid-Funktion“.

## 4. Weiche Schwellenwertsetzung unter einem tiefen Aufmerksamkeitsmechanismus
Das Tiefe Residual-Schrumpfungs-Netzwerk (Deep Residual Shrinkage Network) greift die oben genannte Sub-Netzwerk-Struktur des SENet auf, um eine weiche Schwellenwertsetzung unter einem tiefen Aufmerksamkeitsmechanismus zu realisieren. Durch das blaue Sub-Netzwerk (in den Diagrammen der Originalarbeit) kann ein Satz von Schwellenwerten erlernt werden, um die weiche Schwellenwertsetzung auf die einzelnen Merkmalskanäle anzuwenden.

In diesem Sub-Netzwerk werden zunächst die Absolutwerte aller Merkmale der Eingabe-Merkmalskarte berechnet. Anschließend wird durch Globales Durchschnitts-Pooling (Global Average Pooling) und Mittelwertbildung ein Merkmal gewonnen, das als A bezeichnet wird. Auf einem anderen Pfad wird die Merkmalskarte nach dem Globalen Durchschnitts-Pooling in ein kleines Fully Connected Network eingegeben. Dieses Netzwerk nutzt eine Sigmoid-Funktion als letzte Schicht, um die Ausgabe auf den Bereich zwischen 0 und 1 zu normieren und so einen Koeffizienten zu erhalten, der als $\alpha$ bezeichnet wird. Der endgültige Schwellenwert lässt sich als $\alpha \times A$ ausdrücken. Der Schwellenwert ist also: eine Zahl zwischen 0 und 1 multipliziert mit dem Durchschnitt der Absolutwerte der Merkmalskarte. **Diese Methode garantiert nicht nur, dass der Schwellenwert positiv ist, sondern auch, dass er nicht zu groß wird.**

**Zudem erhalten unterschiedliche Stichproben somit unterschiedliche Schwellenwerte. Daher kann dies in gewissem Maße als ein spezieller Aufmerksamkeitsmechanismus verstanden werden: Merkmale, die für die aktuelle Aufgabe irrelevant sind, werden bemerkt; diese Merkmale werden durch zwei Faltungsschichten (Convolutional Layers) in Werte nahe 0 transformiert und anschließend durch die weiche Schwellenwertsetzung auf Null gesetzt. Oder anders gesagt: Merkmale, die für die aktuelle Aufgabe relevant sind, werden bemerkt; diese werden durch zwei Faltungsschichten in Werte fern von 0 transformiert und somit beibehalten.**

Schließlich erhält man das vollständige Tiefe Residual-Schrumpfungs-Netzwerk, indem man eine bestimmte Anzahl dieser Basismodule sowie Faltungsschichten, Batch-Normalisierung (Batch Normalization), Aktivierungsfunktionen, Globales Durchschnitts-Pooling und eine Fully-Connected-Ausgabeschicht stapelt.

## 5. Allgemeingültigkeit
Das Tiefe Residual-Schrumpfungs-Netzwerk ist faktisch eine universelle Methode zum Lernen von Merkmalen (Feature Learning). Dies liegt daran, dass in vielen Aufgaben des Feature Learning die Stichproben mehr oder weniger Rauschen sowie irrelevante Informationen enthalten. Dieses Rauschen und die irrelevanten Informationen können die Effektivität des Feature Learning beeinträchtigen. Zum Beispiel:

Bei der Bildklassifizierung: Wenn ein Bild gleichzeitig viele andere Objekte enthält, können diese Objekte als „Rauschen“ verstanden werden. Das Tiefe Residual-Schrumpfungs-Netzwerk ist möglicherweise in der Lage, mithilfe des Aufmerksamkeitsmechanismus dieses „Rauschen“ zu bemerken und dann mithilfe der weichen Schwellenwertsetzung die diesem „Rauschen“ entsprechenden Merkmale auf Null zu setzen, was die Genauigkeit der Bildklassifizierung erhöhen könnte.

Bei der Spracherkennung: In einer akustisch eher lauten Umgebung, wie zum Beispiel bei einem Gespräch am Straßenrand oder in einer Fabrikhalle, kann das Tiefe Residual-Schrumpfungs-Netzwerk vielleicht die Genauigkeit der Spracherkennung verbessern, oder zumindest einen Denkansatz liefern, wie die Genauigkeit der Spracherkennung verbessert werden kann.

## Literaturverzeichnis

Minghang Zhao, Shisheng Zhong, Xuyun Fu, Baoping Tang, Michael Pecht, Deep residual shrinkage networks for fault diagnosis, IEEE Transactions on Industrial Informatics, 2020, 16(7): 4681-4690.

[https://ieeexplore.ieee.org/document/8850096](https://ieeexplore.ieee.org/document/8850096)

## BibTeX
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

## Einfluss und Verbreitung

Die Anzahl der Zitationen dieser Arbeit auf Google Scholar hat bereits 1400 überschritten.

Laut unvollständigen Statistiken wurde das Tiefe Residual-Schrumpfungs-Netzwerk in mehr als 1000 Fachpublikationen direkt angewendet oder in verbesserter Form in zahlreichen Bereichen eingesetzt, darunter Maschinenbau, Energiewirtschaft, Computer Vision, Medizin, Sprachverarbeitung, Textanalyse, Radar, Fernerkundung und viele weitere.
