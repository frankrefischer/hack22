Übersetzt mit www.DeepL.com/Translator (kostenlose Version)

https://core.ac.uk/download/pdf/18175413.pdf

## Räume
```csv
Name;Type;Size
Euler;lecture;70
Pascal;lecture;60
MVF21;lecture/exercise;30
MVF23;lecture/exercise;30
MVF26;lecture/exercise;36
MVF31;|lecture/exercise;42
MVF32;lecture/exercise;16
MVF33;lecture/exercise;36
MVH11;lecture/exercise;26
MVH12;lecture/exercise;38
MVF22;computer lab;90
```

## Lehrveranstaltungen
## Courses
```csv
Course code;Course groups;Size;Lectures;Exercises;Computer labs;No. of groups;Fixed
MMG720;Cadv;8;2;1;0;1;No
MMG300;CGU1;38;2;2;0;1;Yes
MVG300;CGU1;34;3;0;3;1;Yes
MMG800;CEM1, Cadv;55;4;0;0;1;No
MSG200;CGU2, CEM1;50;2;2;0;1;No
MMA511;CEM1, Cadv;13;3;0;0;1;No
MMG500;CGU2, CEM2, Cadv;28;2;2;0;2;No
MSA200;CEM2;11;2;1;0;1;No
MMA421;CEM2, Cadv;19;2;1;0;1;No
MSG830;Cothers;44;2;1;2;1;Yes
MMGF20;Cothers;29;2;2;0;1;No
MMGK11;Cothers;49;4;4;0;2;No
MMGL31;Cothers;20;4;6;2;1;No
LGMA10;Cothers;35;4;8;0;1;Yes
MMGF30;Cothers;21;3;0;0;1;Yes
```
## Problembeschreibung

### 1 Studenten
Es gibt verschiedene Gruppen von Studierenden, die je nach Studiengang und Studienjahr unterschiedliche Kurse belegen.  
Anstelle von Mengen verschiedener Gruppen von Studierenden hat das Modell Untermengen der Menge von Kursen, wobei eine Untermenge alle Kurse für eine Gruppe von Studierenden enthält.

### 2 Lehrer
Jede Lehrveranstaltung wird von einer bestimmten Lehrkraft unterrichtet, von der angenommen wird, dass sie zu jeder Tageszeit verfügbar ist.  
Die Lehrkräfte sind grundsätzlich mit den Kursen verbunden.  

### 3 Kurse
Es gibt eine bestimmte Anzahl von Kursen, die je nach Studienzeit geplant werden.  
Jeder Kurs hat eine bestimmte Anzahl von Vorlesungen, Übungen und Computerlabors während des Studienzeitraums.  
Jeder Kurs ist durch einen Kurscode gekennzeichnet und hat eine bestimmte Anzahl von Studenten, die ihn besuchen können und werden.  
Alle Kurse sind in verschiedene Kursgruppen aufgeteilt, die Kurse enthalten, die von derselben Gruppe von Studierenden belegt werden.  
Diese Gruppen sind die Kurse für die Studenten, die
- das erste Jahr des Mathematikstudiums an der Universität Göteborg
- das zweite Jahr des Mathematikstudiums an der Universität Göteborg
- das erste Jahr des Studiengangs Ingenieurmathematik und Computational Science an der Chalmers University of Technology
- und das zweite Jahr des Studiengangs Ingenieurmathematik und Computerwissenschaften an der Chalmers University of Technology
Kollisionen zwischen Kursen sind innerhalb dieser Gruppen nicht erlaubt.

Es gibt zwei weitere Gruppen: Fortgeschrittenenkurse und andere Kurse.  
Fortgeschrittenenkurse sind Kurse für Studenten, die das dritte Jahr des Mathematikstudiums an der Universität Göteborg absolvieren.  
Die Vorlesungen in diesen Kursen dürfen nicht miteinander kollidieren, wohl aber die Übungen und Computerlabors.  
Dies ist auf die große Anzahl von Kursen in dieser Gruppe zurückzuführen.  
Zu den anderen Kursen gehören verschiedene übrige Kurse, die mit allen Kursen kollidieren dürfen, außer mit ihnen selbst.    
Bei einigen wenigen Kursen sind die Übungen in kleinere Gruppen aufgeteilt.  
Außerdem werden einige Lehrveranstaltungen gemeinsam mit anderen Fachbereichen in den Räumen des Fachbereichs Mathematik angeboten.  
Diese sind festgelegt und können nicht geändert werden.  
Im tatsächlichen Stundenplan, der in Abbildung 1 zu sehen ist, gibt es einige Kurse, deren Sitzungen in Räumen stattfinden, die nicht zum Fachbereich Mathematik gehören.  
Im Modell werden diese Sitzungen in den Räumen des Fachbereichs Mathematik geplant.  

### 4 Räume
Es steht eine bestimmte Anzahl von Räumen mit unterschiedlichen Kapazitäten für Studierende zur Verfügung.  
Die Räume und ihre Kapazitäten bleiben für jeden Studienabschnitt gleich.  
Es gibt zehn Räume für Vorlesungen und acht Räume für Übungen.  
Die Übungsräume werden auch als Vorlesungsräume genutzt und sind somit in den zehn Vorlesungsräumen enthalten.  
Es gibt einige spezielle Computerräume, die für Computerlabore genutzt werden.  
In der mathematischen Formulierung wird die Vereinfachung vorgenommen, dass es nur einen großen Computerraum gibt.  
Dies wurde gemacht, weil es relativ häufig vorkommt, dass alle Computerräume für eine Laborsitzung gebucht werden.  
Nur wenige Räume sind bereits mit Kursen belegt, die nicht geändert oder verschoben werden können.  
Ansonsten sind die Räume frei und können jederzeit genutzt werden.

### 5 Constraints
Es gibt zwei Gruppen von Constraints, die berücksichtigt werden müssen: harte Constraints und weiche Constraints.  
Die Constraints wurden auf der Grundlage von Informationen formuliert, die wir von den Verantwortlichen für die Terminplanung im Fachbereich Mathematik erhalten haben.  
Die harten Constraints sind notwendig, um einen gültigen Stundenplan zu erhalten, und die weichen Constraints spiegeln die Präferenzen der Mehrheit wider.  

#### 5.1 Harte Constraints
1. Es darf nicht mehr als eine Vorlesung, eine Übung oder ein Computerlabor gleichzeitig in einem Raum stattfinden.
2. Der Stundenplan muss vollständig sein, d.h. alle Kurse müssen mit der erforderlichen Anzahl von Sitzungen pro Woche geplant werden.
3. Die Räume müssen groß genug für die Lehrveranstaltungen sein.
4. Kein Kurs darf mit sich selbst kollidieren.
5. Kollisionen zwischen Kursen der gleichen Gruppe sind nicht erlaubt, außer bei Fortgeschrittenenkursen und anderen Kursen.
6. Kollisionen zwischen Vorlesungen in Leistungskursen sind nicht erlaubt.
7. Vorlesungen, Übungen und Computerlabore müssen in ihren jeweiligen Räumen abgehalten werden.

#### 5.2 Weiche Constraints
1. Pro Tag und Kurs sollte es nicht mehr als eine Vorlesung, eine Übung und ein Computerlabor geben.
2. Der Stundenplan für die verschiedenen Gruppen von Studierenden sollte über die Woche verteilt und an jedem Tag so kompakt wie möglich sein.
3. Eine Übung in einer Lehrveranstaltung sollte unmittelbar nach einer Vorlesung in derselben Lehrveranstaltung abgehalten werden. 
4. Jede Vorlesung einer Lehrveranstaltung sollte im gleichen Raum stattfinden. Dies gilt auch für Übungen.
5. Montagmorgen und Freitagnachmittag sollten keine Sitzungen stattfinden.
6. Die Sitzungen sollten vorzugsweise zwischen 10:00 und 15:00 Uhr stattfinden.

## Erläuterung der modellierten Beschränkungen
9) Die Räume müssen mindestens so groß sein wie die Kursgröße für die Vorlesungen.
10) Die Räume müssen groß genug für die Übungen sein. Es gibt einen multiplikativen Faktor von 0,8, da in der Regel nicht alle Studierenden an den Übungen teilnehmen.
11) Die Räume müssen mindestens so groß sein wie die Kursgröße für die Computerräume.
12) Es darf nicht mehr als eine Vorlesung/Übung/Computerlabor in einem Raum zu einer bestimmten Zeit stattfinden.
13) Die Kurse in CGU1 dürfen sich nicht überschneiden.
14) Die Kurse in CGU2 dürfen nicht kollidieren.
15) Die Kurse in CEM1 dürfen nicht kollidieren.
16) Die Kurse in CEM2 dürfen nicht kollidieren.
17) Die Vorlesungen der Kurse in Cadv dürfen nicht kollidieren.
18) Die Lehrveranstaltungen in Cothers dürfen nicht mit sich selbst kollidieren.
19) Jede Lehrveranstaltung muss die geforderte Anzahl von Vorlesungen, Übungen und Computerlaboren haben.
20) Jede Lehrveranstaltung muss die geforderte Anzahl von Vorlesungen, Übungen und Computerlaboratorien haben.
21) Jede Lehrveranstaltung muss die erforderliche Anzahl von Vorlesungen, Übungen und Computerräumen aufweisen.
22) Die Vorlesungen müssen über die Woche verteilt sein, außer bei Kursen in C1.
23) Für jede Lehrveranstaltung muss jede Vorlesung im selben Raum stattfinden.
24) Für jede Lehrveranstaltung muss sich jede Übung im selben Raum befinden.
25) Für jede Lehrveranstaltung, in der die Übungen in Gruppen aufgeteilt sind, müssen die Sitzungen jeder Gruppe im selben Raum stattfinden.
26) Die Übungen müssen im Anschluss an eine Vorlesung in derselben Lehrveranstaltung oder im Zeitabschnitt 1 stattfinden.
27) Es darf nicht mehr als eine Vorlesung pro Tag und Kurs geben.
28) Es darf nicht mehr als eine Übung pro Tag und Kurs geben, außer bei Kursen in C3.
29) Es dürfen nicht mehr als zwei Übungen pro Tag für Kurse in C5 stattfinden.
30) Es darf nicht mehr als ein Computerraum pro Tag und Kurs vorhanden sein, außer bei Kursen in C4.
