<!-- Generated on: 2026-09-15 15:01:03 -->


---
title: "1.1 Sets & Numbers"
description: Sets, or collections of objects, are the basic building blocks of numbers and mathematics.
author: "Nolan Mitchell"
type: page
image: "Smithsonian.jpg"
draft: false
tags: ["sets", "set-builder-notation", "combining-sets", "union", "intersection", "empty-set", "counting", "number-systems", "natural-numbers", "integers", "rational-numbers", "irrational-numbers", "real-numbers", "number-line", "intervals", "interval-notation", "combining-intervals", "order-of-operations", "PEMDAS"]
---



{{% imgcap file="/img/chapter-1/Smithsonian_wide.jpg" title="Smithsonian Museum of Natural History, photo by Blake Patterson" source="https://www.flickr.com/photos/35448539@N00/8151668486" %}}

## Introduction
The Smithsonian in Washington, DC is one of the largest museums in the world, housing vast collections of rare and historically significant objects.  

The *Air and Space* collection, for example, holds the [1903 Wright Flyer](https://www.si.edu/object/nasm_A19610048000), the first successful airplane, and the [Apollo 11 Command Module](https://www.si.edu/object/nasm_A19700102000) from the first mission to the moon.  

Notable items in other collections include [Abraham Lincolnâ€™s top hat](https://www.si.edu/object/nmah_1199660), an original [Kermit the Frog](https://www.si.edu/object/nmah_765593) puppet, and the famous [Hope Diamond](https://www.si.edu/spotlight/hope-diamond). 

With over 200 million fossils, specimens, and treasures, these collections play a crucial role in preserving our nation's history and culture, serving as invaluable resources for researchers and scientists. 

Collections are equally vital in mathematics, although you seldom find them in museum exhibits.


## Sets
In mathematics, collections are usually called **sets**.  Sets are the foundational building blocks of modern mathematics.

To create a set, you simply need a way to decide if an object belongs in the set or not.  

One way to do that is to list everything in the set. For example, traffic lights only have three colors: red, yellow, and green. We can list these colors to form a set: $\lbrace \text{red, yellow, green} \rbrace$.  Items in a set are always written inside curly braces $\lbrace \thinspace \thinspace \rbrace$.

![the set of colors on a traffic light](/img/chapter-1/set_colors.svg#center)

Another way to represent a set is by drawing a big circle and writing each item of the set inside the circle.

![the set of colors on a traffic light](/img/chapter-1/set_colors_diagram.svg#center)

Visual diagrams like this will be helpful in later sections where we investigate relationships between sets.

## Set-Builder Notation
Sometimes it's hard to list everything in a set.  For instance, *whiskers on kittens*, *bright copper kettles* and *warm woolen mittens* might be a few of my favorite things, but listing all my favorites would be impossible.  

Fortunately, instead of listing everything in a set, we can simply describe the properties that the items share.  This is called **set-builder notation**. 

Using set-builder notation, the set of "all of my favorite things" could be written as

\[
  \left\lbrace x \thinspace \vert \thinspace x \text{ is one of my favorite things} \right\rbrace
\]

The vertical bar symbol $\vert$ means "such that" or "where".  If we put the set above into words we would read it as "the set of all $x$ where $x$ is one of my favorite things."

{{% check %}} 
1. Is $\text{Apple, Orange, Banana}$ a valid set?{{% answer %}}Almost.  While it is a list of objects, it does not have the right format.  To be written as a set it should be surrounded by curly braces.  The correct way to write it is $\lbrace \text{Apple, Orange, Banana} \rbrace$.{{% /answer %}}
1. Are $\lbrace \text{Taco, Cat, Goat, Cheese, Pizza} \rbrace$ and $\lbrace \text{Pizza, Cheese, Goat, Cat, Taco} \rbrace$ the same set?{{% answer %}}Yes, they are the same. In sets, the order of elements doesn't matter.{{% /answer %}}
1.  Describe the set $\lbrace x \thinspace \vert \thinspace x \text{ is something in your backpack} \rbrace$ in words and list a few items that might be in it.{{% answer %}}This is "the set of all $x$ where $x$ is something in your backpack".  Elements in this set could include note paper, a pencil, a calculator, etc.{{% /answer %}}
1.  Write the set of all vegetables using set-builder notation.{{% answer %}}$\lbrace x \thinspace \vert \thinspace x \text{ is a vegetable} \rbrace${{% /answer %}}
{{% /check %}}


## Combining Sets
Sets can be combined in two different ways. The first way is to group everything from both sets together into one big set.  This is called the **union** of the two sets.  In the figure below you can form the union of the two sets by moving the **<font color="blue">blue</font>** slider.

{{% geogebra ratio="20%" id_1="BqfEqUqLAGw8mOXv" id_2="s9wa8eba" id_m="gtgttdp7" aria="A set of {star, circle, hexagon, triangle} combined with a set {hexagon, triangle, moon, square} to make the set {star, circle, hexagon, triangle, moon, square}"%}}

There is a special symbol we use for unions: $\bigcup$.  If we have two sets, $A$ and $B$, then we write their union as $A \bigcup B$

\[
  A \bigcup B = \left\lbrace x \thinspace \vert \thinspace x \text{ is in } A  \text{ or }  x \text{ is in }B  \right\rbrace
\]

The second way to combine sets is to only consider items that the two sets have in common. This is called the **intersection** of the sets.

{{% geogebra ratio="20%" id_1="EXR1qIEEqgqFvoOY" id_2="f6fbnnnc" id_m="hq9xagby" aria="A set of {star, circle, hexagon, triangle} combined with a set {hexagon, triangle, moon, square} to make the set {hexagon, triangle}"%}}

The intersection of two sets also has its own symbol: $\bigcap$.

\[
  A \bigcap B = \left\lbrace x \thinspace \vert \thinspace x \text{ is in } A  \text{ and }  x \text{ is in }B\ \right\rbrace
\]

If the intersection has nothing in it we say it is *empty* and use the symbol $\varnothing$ to represent the **empty set**.

{{% check %}} Consider the following sets
\[
  \begin{align}
    A &= \lbrace \text{flour, sugar, butter, eggs, milk} \rbrace \newline
    B &= \lbrace \text{bacon, pancakes, eggs, milk} \rbrace \newline
    C &= \lbrace \text{peas, carrots, potatoes} \rbrace
    \end{align}
\]
1. List everything that would be in $A \bigcup C$. {{% answer %}}Since the union is all of the items in both sets combined, $A \bigcup C$ would contain flour, sugar, butter, eggs, milk, peas, carrots, and potatoes.</br></br>{{% /answer %}}
1. List all the elements of $A \bigcap B$. {{% answer %}}Since intersection is only the items that the two sets have in common, $A \bigcap B$ would contain just eggs and milk.</br></br>{{% /answer %}}
1. Describe $B\bigcap C$. {{% answer %}}The sets have nothing in common so their intersection is the empty set.  \[ B \bigcap C = \varnothing \] {{% /answer %}}
{{% /check %}}


## Counting
It might be hard to imagine, but people have not always had numbers. The numbers we use today are actually the result of thousands of years of innovation and invention.

Surprisingly, sets actually came before numbers. To see why this is the case, take a look at the following sets.  What do they have in common?

![a set with 3 cookies and a set with 3 kittens](/img/chapter-1/sets_of_3.png#center)

These sets are similar because they are the same size.  Even though the contents are very different, the *quantity* of items in each set is identical.  In other words, they have the same **number** of items.

It's this need to count the objects in a set that sparked the development of numbers.


##  Development of Numbers
There's little doubt that fingers were among the earliest counting tools.  In fact, in English the words *eleven* and *twelve* come from the Old English words for "one left over" and "two left over", indicating how many would be left over after counting to ten with your fingers.

Over time people invented other ways to keep track of their flocks, herds, and commodities.  They cut tally marks on sticks, made piles of pebbles, and even carved figurines to look like sheep, jars of oil, baskets of grain, and so on.{{% sidenote "tokens" %}}![tally sticks and figurines used for counting](/img/chapter-1/tally_sticks.jpg) Tally sticks and figurines from the Swiss Alpine Museum. [*Photo by Sandstein.*](https://commons.wikimedia.org/wiki/File:SAM_PC_1_-_Tally_sticks_1_-_Overview.jpg){{% /sidenote %}}

In Mesopotamia, about 10,000 years ago, Sumerians made clay tokens shaped to resemble the items they were exchanging, one token for each item.  Soon these tokens were replaced by shapes drawn on clay tablets.

Eventually special symbols, or *numerals*, were created to represent specific quantities. It was at that point, some 5000 years ago, that the first number system was born.{{% sidenote "numerals" %}}![5000 year old Sumerian tablet with indentations representing numerals](/img/chapter-1/Sumerian_tablet.png) This 5000 year-old clay tablet is one of the first artifacts in history to display numerical symbols.  It records how much beer should be paid to a particular worker for his labor. [Photo courtesy of the British Museum](http://www.britishmuseum.org/research/collection_online/collection_object_details.aspx?objectId=327218&partId=1) {{% /sidenote %}}

The Sumerian system did not look like the one we use today.  They counted using groups of 60 (which is why we have 60 minutes in an hour) and used different symbols than what we are used to.

The number system we now use worldwide originated in India and was later adopted by Arab scholars, which is why it is called the Hindu-Arabic system.

This system was introduced to Europe by Fibonacci in 1202, but it wasn't until the 15th and 16th centuries that it became dominant. Since then, Hindu-Arabic numerals have become the standard numerical representation used globally for counting, record-keeping, and mathematical calculations, having spread through international trade, scholarship, and cultural exchange.


## Natural Numbers and Integers
The numbers we are most familiar with are the counting numbers $1, 2, 3, 4, ...$.  The set of counting numbers is also known as the set of **natural numbers** and is represented by the symbol $\mathbb{N}$. In set notation we would say

\[
  \mathbb{N} = \left\lbrace 1,2,3,...\right\rbrace
\]

You might already know that adding two natural numbers always results in another natural number. For example, $3$ and $5$ are both natural numbers and so is $3+5=8$.

But what if we subtract one natural number from another, is the result always in $\mathbb{N}$?  Clearly not, since subtraction can create negative values.

The set that combines $\mathbb{N}$ with $0$ and all the negative natural numbers is called the set of **integers** and is represented by the symbol $\mathbb{Z}$.

\[
  \mathbb{Z} = \left\lbrace ...,-3,-2,-1,0,1,2,3,... \right\rbrace
\]

Notice that we can add and subtract integers as much as we like and the result is always an integer.

{{% check %}}
1. True or False:  $5$ is an integer. {{% answer %}}**True**.  It is also a natural number.{{% /answer %}}
1. True or False:  $0$ is a natural number. {{% answer %}}**False**.  It is an integer.{{% /answer %}}
1. True or False:  If you *multiply* two integers you always get another integer.  {{% answer %}}**True**.  Since multiplication is repeated addition, the answer will always be an integer.{{% /answer %}}
{{% /check %}}


## Rational Numbers
While multiplying two integers always results in another integer, division is more complicated.

If $p$ and $q$ are integers, then the fraction $\frac{p}{q}$ could be an integer, but it doesn't have to be. For instance $\frac{6}{2}=3$ is an integer, but $\frac{5}{2}$ is not.

The set that contains all the fractions, or ratios, of integers, is called the set of **rational numbers**, or $\mathbb{Q}$.

\[
  \mathbb{Q} = \left\lbrace \frac{p}{q}  \thinspace \bigg|  \thinspace {p} \text{ and } {q} \text{ are integers with } q\neq0 \right\rbrace.
\]

Since division by $0$ is not well defined, fractions with a denominator of $0$, such as $\frac{4}{0}$ and $\frac{-2}{0}$, are not included in the set of rational numbers.

It is important to note that since any integer can be written as a fraction (for example $5 = \frac{5}{1}$), the set of rational numbers includes all of the integers as well.

Fractions can be converted into decimals by dividing the top number (the numerator) by the bottom number (the denominator). When you do this one of two patterns will occur.  Either the division will end after a certain number of decimal places, such as $\frac{10}{5}=2$ and $\frac{3}{16}=0.1875$, or it will repeat forever like $\frac{1}{3}=0.\overline{3}$ and $\frac{1}{7}=0.\overline{142857}$.

The set of rational numbers is special because you can add, subtract, multiply and divide as much as you want and never end up with a different type of number---the answer is always a rational number.

{{% check %}}
1. Find three different ways to write $7$ as a rational number.  {{% answer %}}$\frac{7}{1}$, $\frac{14}{2}$, and $\frac{21}{3}$ are a few of the many possible answers.{{% /answer %}}
2. Write $1.5$ as a rational number.  {{% answer %}}To convert decimals to fractions, write the decimal over $1$ then multiply both top and bottom by $10$ for every digit to the right of decimal point.  Then simplify as needed.
\[
  \begin{align}
    1.5 &= \frac{1.5}{1} && \small \color{#5fa2ce}{\text{put the decimal over a }1} \newline \newline
    & = \frac{15}{10} && \small \color{#5fa2ce}{\text{multiply top & bottom by }10} \newline \newline
    & = \frac{3}{2} && \small \color{#5fa2ce}{\text{simplify}}
  \end{align}
\]
{{% /answer %}}
3. Write $\frac{3}{2} + \frac{5}{6}$ as a rational number.  {{% answer %}}Remember that to add fractions they must have the same denominator.  So first rewrite $\frac{3}{2}$ as $\frac{9}{6}$.  Then add and simplify.
\[\begin{align}
\frac{3}{2} + \frac{5}{6} &= \frac{9}{6} + \frac{5}{6} \newline
&= \frac{14}{6} \newline
&= \frac{7}{3}
\end{align}\]
{{% /answer %}}
4. Write $\frac{3}{2} \div \frac{5}{6}$ as a rational number.  {{% answer %}}Dividing fractions is the same as multiplying by the reciprocal.  So
\[\begin{align}
\frac{3}{2} \div \frac{5}{6} &= \frac{3}{2} \times \frac{6}{5} \newline
&= \frac{18}{10} \newline
&= \frac{9}{5}
\end{align}\]
{{% /answer %}}
{{% /check %}}


## Real Numbers
Since the rational numbers are closed under addition, subtraction, multiplication and division, it might come as a surprise that other types of numbers exist and are essential to mathematics.  The discovery of one new type of number is attributed to an associate of Pythagoras whose name was Hippasus of Metapontum.

According to legend, Hippasus was trying to measure the diagonal of a 1 by 1 square{{% sidenote "sqrt_2" %}}![a 1-by-1 square with the diagonal labeled as sqrt{2}](/img/chapter-1/sqrt_2.svg#center){{% /sidenote %}}.  He knew from the Pythagorean theorem that the answer was $\sqrt{2}$, but had been unable to find a rational number that was equal to $2$ when you square it.

Eventually he proved that $\sqrt{2}$ cannot be written as a ratio of any two integers and concluded that it must belong to a new set of **irrational numbers**.  

Some accounts say that the Pythagoreans were so shocked by Hippasus' discovery that they drowned him in the Mediterranean Sea to try and hide irrational numbers from the world.

That attempt failed, and we now know that there are actually far more irrational numbers than rational numbers.  Some irrational numbers are famous and have their own special symbols, like $\pi$, but most are written as expressions involving operations like $\sqrt{2}$.  

Irrational numbers cannot be expressed exactly as fractions or finite decimals since their decimal expansions never end or repeat.  In many cases we use a calculator to approximate irrational numbers by rounding to a specified number decimal places.  For example, $\sqrt{2}\approx 1.4142$ rounded to $4$ decimal places.

The union of the sets of rational and irrational numbers is called the set of **real numbers**, $\mathbb{R}$.  In other words, the set of real numbers includes every type of number we've discussed so far.

For example, $-0.5$, $\sqrt{2}$, $\frac{7}{3}$, $-0.248$, and  $8.\overline{261}$ are all real numbers.

![A diagram showing the classification of real numbers (â„) into rational and irrational numbers. Rational numbers (â„š) are defined as all numbers that can be written as p/q, where p and q are integers and q â‰  0. Inside the rational numbers set, there's a smaller set of integers (â„¤ = { 0, Â±1, Â±2, Â±3, ... }) and within that, an even smaller set of natural numbers (â„• = {1, 2, 3, 4, ...}). To the right of the rational numbers is a separate box labeled "Irrational Numbers," defined as {x : x âˆ‰ â„š}. The entire diagram is enclosed in a larger box labeled "Real Numbers â„ = {x : x is rational or irrational}".
](/img/chapter-1/real_numbers.png#center)

The set of real numbers is closed under all standard operations including powers and some roots.  In fact, you can do just about anything to a real number and the result will still be a real number, as long as you do not take the square root of a negative value, something we will look into in a [later chapter](//chapter-5/5.2#imaginary-numbers), or divide by $0$.

{{% check %}}
1.  True or False:  $ 2^{3}+9.5-\frac{8}{\sqrt{2}}$ is a real number. {{% answer %}} **True**.  Since we did not divide by zero and did not take the square root of a negative, the result must be a real number.</br></br>{{% /answer %}}
2.  True or False:   $\frac{6}{81-3^4}$ is a real number.  {{% answer %}} **False**.  This is because $81-3^{4}=0$ and division by $0$ is not well defined.</br></br>{{% /answer %}}
3.  True or False:   $\sqrt{16-4(15)}$ is a real number.  {{% answer %}}**False**. Simplifying the values inside the square root gives $\sqrt{-44}$ and the square root of a negative number is **not** a real number.{{% /answer %}}
{{% /check %}}


## The Real Number Line
It is often helpful to visualize the set of real numbers with a **number line**, which is just a straight line with marks representing the location of numbers.

![A horizontal number line with tick marks and labeled integers ranging from -4 to 4.](/img/chapter-1/numberline_plain.svg#center)

Positive numbers are always on the right side of zero while negative numbers are always on the left.

Every real number has a place on the number line, and every location on a number line is assumed to correspond to a real number.  Here are a few real numbers and their relative locations on the number line.

![A number line labeled from -4 to 4 with red arrows pointing to approximate positions of several values: negative square root of 14 near -3.7, -1.6, 1/8 near 0.125, square root of 2 near 1.4, and pi near 3.14.](/img/chapter-1/numberline_real_numbers.svg#center)


## Intervals of Real Numbers
The set of all values in between two numbers is called an **interval**.  For instance, all of the numbers between $0$ and $3$ make an interval.

There are several ways to describe this interval.  One way is to use inequalities and write it as a set.

\[\lbrace x \thinspace \vert \thinspace 0<x<3  \rbrace\]

Another option is to color the interval on a number line

![A number line from -3 to 3 with an orange line segment from 0 to 3. Open circles at 0 and 3.](/img/chapter-1/interval_open_0_to_3.svg#center)

Open circles indicate that the numbers $0$ and $3$ are **not** included in the interval.

A third option is to use **interval notation**, which is a written abbreviation of the number line.  In this example the interval notation would be

\[(0 , 3)\]

Notice that this mirrors the number line by having the lowest number on the left, with parenthesis taking the place of the open circles.

Other intervals might include an end point or even extend out toward infinity.  For example, the interval of all numbers greater than or equal to $-2$ can be described in any of the following ways

* **set notation**: \[\lbrace x\vert-2\leq x<\infty  \rbrace\]
* **number line**: ![A number line from -3 to 3 with a solid orange line starting at -2 and ending just before 3. A closed circle at -2 and an arrow pointing right near 3.](/img/chapter-1/interval_closed_-2_to_infinity.svg#center)
* **interval notation**: \[[ -2\thinspace, \thinspace \infty)\]

There are a few subtleties here that deserved to be highlighted.  

First, notice that there are three ways to indicate that an endpoint is included.  In set notation, the inequality used must have an equal sign ($\leq$ or $\geq$). On a number line, the circle marking the point is filled in. And in the interval notation, the parenthesis for that point changes to a square bracket.

Second, to indicate that an interval continues out toward infinity we use an arrow pointing in the appropriate direction.  Since nothing equals infinity we must always use a parenthesis when writing that part of the interval.

{{% check %}}
1.  Sketch the interval $\lbrace x \thinspace \vert \thinspace -1< x \leq 4  \rbrace$ on a number line.{{% answer %}}</br>![](/img/chapter-1/interval_open_-1_closed_4.svg)Because of the equal sign $4$ is included but $-1$ is not, so we put an open circle at $-1$ and a closed circle at $4$.{{% /answer %}}
2.  Sketch the interval $[ 5 , 8 )$ on a number line.{{% answer %}}</br>![](/img/chapter-1/interval_closed_5_open_8.svg)Because of the square bracket we know $5$ is included but $8$ is **not**, so we put a closed circle at $5$ and an open circle at $8$.</br> {{% /answer %}}
3.  Write the following interval in both set notation and interval notation.</br></br>
![](/img/chapter-1/interval_-infinity_open_0.svg){{% answer %}}set notation: $\lbrace x \thinspace \vert \thinspace -\infty < x<0\ \rbrace$</br>interval notation: $( -\infty, 0)$   {{% /answer %}}
{{% /check %}}


## Combining Intervals
Since intervals are sets of real numbers, they can be combined using unions and intersections.

The union is the result of combining the two intervals together, while the intersection is only the part where the intervals overlap each other.  A few examples will illustrate the idea.

Suppose we have the following intervals.  What will the **union** look like?  Move the **<font color="blue">blue</font>** slider to see the union.

{{% geogebra ratio="20%" id_1="QA5vWqgFMdxjV0v5" id_2="xnsrxwts" id_m="fysebmbd" %}}

Once we've identified the union on the number line, it's much easier to write it in interval notation.

\[(-1, \infty) \bigcup  [-3,0 ) = [-3, \infty)\]

The **intersection** of the same two intervals is smaller, since it is only where they overlap.  You can explore the intersection in the figure below.

{{% geogebra ratio="20%" id_1="zFJFHgkNdUtUOqRM" id_2="gmuyj24e" id_m="bhwanhyg" %}}

Now that we can see the intersection visually, the notation follows naturally.

\[(-1, \infty) \bigcap  [-3,0 ) = (-1, 0)\]

{{% check %}}
1.  Sketch the intersection of two intervals shown below
![](/img/chapter-1/interval_open_-8_open_-2.svg) ![](/img/chapter-1/interval_closed_-6_open_2.svg) {{% answer %}}![](/img/chapter-1/interval_closed_-6_open_-2.svg)
{{% /answer %}}
2.  Find $[-2, 5) \bigcup  (3,10 ]$. {{% answer %}}$[-2, 10]${{% /answer %}}
{{% /check %}}


## Order of operations
In elementary school students are often asked to add several numbers together, such as $4 + 10 + 5 = 19$.  What is seldom discussed is the fact that we can't technically add three numbers at once.  

Addition, like the other basic operations, is a "binary" operation--it only works on two numbers at a time.  To avoid confusion, when multiple operations are needed there is a standard order that should be followed.

The order of operations we use today is sometimes remembered by the acronym P E MD AS, which stands for

1. **P**arentheses (including brackets and fraction bars)
1. **E**xponents (including roots)
1. **M**ultiplication and **D**ivision
1. **A**ddition and **S**ubtraction

 When several of these operations are combined, operations higher on the list should be dealt with before those lower on the list.  

 And if an expression has more than one operation with equal priority (like multiplication and division or addition and subtraction) then you work with them in the order they appear from left to right.  For instance, if we have $20 \div 5 \times 2$, then we start from the left and first do $20 \div 5$, which is $4$, and then multiply that by $2$, giving us $8$.

 {{% check %}}
 1. Calculate $12 - 3 + 5$ {{% answer %}}Since addition and subtraction have the same priority, we do these in the order they appear, working from left to right.  Start by subtracting $12 - 3$, which is $9$, and then add $5$ to get $14$.{{% /answer %}}
 1. Evaluate $8-7(2+1)$.  {{% answer %}}\[\begin{align} 8-7(2+1) &= 8-7(3) \newline &= 8-21 \newline &= -13 \end{align}\]{{% /answer %}}
 1. Evaluate $\frac{4+2(5)}{7}$ {{% answer %}} \[\begin{align}\frac{4+2(5)}{7} &= \frac{4+10}{7} \newline &=\frac{14}{7} \newline &=2 \end{align}\] {{% /answer %}}
 1. True or False:  $\frac{8}{4+2}=\frac{8}{4}+\frac{8}{2}$ {{% answer %}}**False**. The correct calculation is \[\frac{8}{4+2}=\frac{8}{6}=\frac{4}{3}\].{{% /answer %}}
 1. True or False:  $(2+3)^2=2^2+3^2$ {{% answer %}}**False**. The left side of the equation simplifies to $(2+3)^2=(5)^2=25$, but the other side of the equation is $(2)^2+(3)^2=4+9=13$.  <br><br>For real numbers $a$ and $b$, the distributive property gives \[(a+b)^2=a^2+2ab+b^2\].{{% /answer %}}
 {{% /check %}}
---
title: "1.2 Functions"
description: A function is any rule that matches each item in one set with exactly one item from another set, much like how each button on a soda machine is linked one specific drink.
author: "Nolan Mitchell"
type: page
image: "vending_machine.jpg"
draft: false
tags: ["functions", "definition-of-function", "domain", "range", "mapping-diagrams", "function-notation", "evaluating-functions", "function-tables", "function-graphs", "vertical-line-test", "division-by-zero", "even-roots"]
---

{{% imgcap file="/img/chapter-1/vending_machine.jpg" title="Soda Vending Machine Japan Coast, photo by slackrhackr" source="https://commons.wikimedia.org/wiki/File:Soda_Vending_Machine_Japan_Coast.jpg"%}}

## Introduction
Each button on a vending machine corresponds to a particular snack inside the machine. The item you get depends on the button you push. When you press the button for a soda the machine should give you that soda, if it is functioning properly.

In this section we'll see that mathematical functions connect things in a similar way.


## The Definition of a Function
While no single definition can capture the full extent of the function concept, it is still important to start with one.  The following definition was developed in the early 1900's and is stated in terms of sets.

{{% definition %}}
A **function** is any rule that matches each element from one set to exactly one element in another set. The set of inputs is called the **domain** of the function while the **range** is the set of all its output values.
{{% /definition %}}

Notice that this definition has three parts: (1) a set of inputs called the domain, (2) a set of outputs called the range and (3) the rule that links them together.

This is just like a vending machine where there is a set of buttons, a set of snacks, and the internal workings of the machine that link the two.

Perhaps a diagram would help illustrate this.  If $x$ is in the domain and $y$ is in the range, then we can draw the function as a mapping diagram, like the one below.

![](/img/chapter-1/arrow_diagram_function_x_y.svg#center)

Let's look at a specific example.  Suppose three friends went to a deli and each ordered a sandwich, as in the diagram below.

![](/img/chapter-1/arrow_diagram_sandwiches_1.svg#center)

Since each person is linked to just one sandwich, this *is* a function.  

In general, anytime we can match each item from one set to just one item in another set, then we have a function.

In the figure below you can change the arrangement of the arrows by moving the **<font color="blue">blue</font>** points.  Experiment until you feel confident that you can recognize what is and what is not a function.

{{% geogebra ratio="50%" id_1="UQ7ydkWqAmoFriMg" id_2="hwwhaa98" id_m="tm4yf6r7" %}} <br>

{{% check %}}
1. Does this diagram represent a function?  If so, also identify the domain and range.
![](/img/chapter-1/arrow_diagram_sandwiches_3.svg#center){{% answer %}}**YES**, this is a function.  Even though they all ordered the same thing, each person is only getting one sandwich, so it is a function.  The **domain** is the set of people and the **range** is the set of sandwiches.{{% /answer %}}
2. Does this diagram represent a function?  If so, also identify the domain and range.
![](/img/chapter-1/arrow_diagram_sandwiches_2.svg#center){{% answer %}}**NO**, this is not a function because one person, Lisa, is linked to two sandwiches.{{% /answer %}}
{{% /check %}}


## Function Notation
When there is a function relationship between $x$ and $y$ it is common practice to replace $y$ with $f(x)$ and say that $y=f(x)$.  This is known as **function notation**.

![](/img/chapter-1/arrow_diagram_function_x_f_of_x.svg#center)

When said aloud the notation $f(x)$ is read "$f$ of  $x$".  This notation reminds us that the output $f(x)$ is the result of putting the input $x$ inside of the function $f$.   

In fact, it can be helpful to think of a function as a machine that changes an object $x$ into something new $f(x)$.

![](/img/chapter-1/function_machine.svg#center)

Suppose, for example, that pressing the button $\text{B4}$ on a vending machine gives you a bag of potato chips. Using function notation we might write $f(\text{B4})=\text{potato chips}$.

With function notation the choice of letters is completely arbitrary. For example, if a function always adds $3$ it makes no difference whether we refer to it as $f(x)=x+3$ or as $g(x)=x+3$ or as $w(t)=t+3$. It is what a function does that matters, not what it is called.

{{% check %}}
{{% imgcap file="/img/chapter-1/doug-maloney-1157775-unsplash.jpg" title="Volkswagen Beetle photo by Doug Maloney on Unsplash" source="https://unsplash.com/photos/PUmAQ2sTGMY"%}}

Suppose that the function  $C$  gives you the cost in dollars of a Volkswagen Beetle based on its age $t$ in years.

1. Are the inputs dollars or years? {{% answer %}}The inputs are **years**.{{% /answer %}}
1. Are the outputs dollars or years? {{% answer %}}The outputs are **dollars**.{{% /answer %}}
1. Describe the difference in meaning between $C(50)=2000$ and $C(2000)=50$. Which one is more reasonable? {{% answer %}}In this example the inputs are always years and the outputs are always dollars.  The first equation means that the cost of a 50 year-old Beetle is 2000 dollars.  The second would mean that the cost of a 2000 year-old Beetle is just 50 dollars (which is highly unlikely).{{% /answer %}}
{{% /check %}}


## Evaluating & Solving
The process of finding the output for a particular input is called **evaluating** the function. Evaluating is sometimes confused with solving, which is understandable since they are like two sides of a coin.  To **evaluate** we start with an input and find the output.  **Solving** is the reverse process, we are given an output and must find the input.

Perhaps seeing this in the context of our vending machine analogy will help.  Evaluating is like choosing a button on the vending machine (the input) and getting a snack (the output). Solving, on the other hand, is like knowing the snack you want and figuring out which button to press to get it.

Consider the function shown in the table below.

| $x$ | $y=f(x)$ |
| ----- | ----- |
| A2 | chocolate bar |
| A3 | bubble gum |
| B4 | potato chips |
| C1 | root beer |
| C2 | granola bar |
| D3 | pretzels |

To evaluate $f(A2)$ we simply find the value of $y$ when $x=A2$.  From the table it appears that $f(A2)=\text{chocolate bar}$.

To solve $f(x)=\text{root beer}$, however, we scan the table in the opposite direction, looking for an $x$ that creates $\text{root beer}$ as an output.  The solution is $x=C1$.

If a function is defined by an equation, such as $f(x)=2 x^2 - 6 x$, then we evaluate it by replacing every $x$ with the given input value.  To find $f(10)$, we insert $10$ everywhere we see an $x$ and simplify, if possible.

\[
  \begin{align}
    f(10) &= 2(10)^2-6(10) \newline
    &= 200-60 \newline
    &= 140
  \end{align}
\]

We now know that $f(10)=140$.

A function can be evaluated even if we do not get a numerical result.  Evaluating $f(x^{2})$ or $f(t+2)$ would mean substituting each $x$ with the expression $x^{2}$ or $t+2$.

{{% check %}}
1. Evaluate $f(2)$ if $f(x)=x-3$. {{% answer %}}$f(2)=(2)-3=-1${{% /answer %}}
1. If $g(x)=x^{2}+6x$, what is $g(ðŸ˜€)$? {{% answer %}}$g(ðŸ˜€)=(ðŸ˜€)^2+6(ðŸ˜€)${{% /answer %}}
1. For the function shown below, what is $f(5)$? <br><br> ![](/img/chapter-1/arrow_diagram_b_inverse.svg#center){{% answer %}}$f(5)=A${{% /answer %}}
1. Using the same function diagram as above, what is the solution to $f(x)=D$? {{% answer %}}Since $f(42)=D$, the solution is $x=42$.{{% /answer %}}
{{% /check %}}


## Graphs of Functions
Because functions are so widely used, there are many different ways to represent them.  Each way to visualize a function highlights something special about the function and switching from one to another can help us see different features and discover connections that might have been hidden otherwise.   

Of primary importance is the connection between equations, tables and graphs of functions.

The **graph** of a function is the set of all points $(x, y)$ where each $y$ is found by evaluating the function's equation for a particular $x$.  In other words, for any $x$ value, $y=f(x)$.  

For instance, to graph the function $f(x)=x^{2}-3$ we randomly choose a handful of values for $x$ and evaluate the function for each one, creating a table of values.  

| $x$ | $f(x)=x^{2}-3$ | $(x,y)$ |
| ----- | ----- | ----- |
|  $-2$ | $(-2)^2-3 = 1$ | $(-2, 1)$ |
| $-1$ | $(-1)^2-3 =  -2$ | $(-1, -2)$ |
| $0$ | $(0)^2-3 = -3$ | $(0, -3)$ |
| $1$ | $(1)^2-3 = -2$ | $(1, -2)$ |
| $2$ | $(2)^2-3 = 1$ | $(2, 1)$ |
| $3$ | $(3)^2-3 = 6$ | $(3, 6)$ |

Then we convert those values into ordered $(x, y)$ pairs that can be plotted as points.  Connecting the points with a smooth curve gives us a graph of the function.

![](/img/chapter-1/function_graph_x2-3.svg#center)

Even though calculators and apps can graph most functions, graphing functions by hand is still an important skill to practice.

{{% check %}}
Sketch a graph of the function $f(x)=\frac{2}{3}x + 1$.  Use $-3, 0, 3$ as your $x$ values.{{% answer %}}
| $x$ | $f(x)=\frac{2}{3}x + 1$ | $(x,y)$ |
| ----- | ----- | ----- |
|  $-3$ | $\frac{2}{3}(-3) + 1=-1$ | $(-3, -1)$ |
| $0$ | $\frac{2}{3}(0) + 1$ | $(0, 1)$ |
| $3$ | $\frac{2}{3}(3) + 1$ | $(3, 3)$ |

![](/img/chapter-1/function_graph_2_over_3_x+1.svg#center){{% /answer %}}
{{% /check %}}


## Evaluate Functions Using Graphs
When a function is defined by a graph we evaluate the function by reading off the $y$ coordinate that matches the given $x$ value.  

In the figure below you can move the **<font color="blue">INPUT</font>** $x$ value which will change the **<font color="red">OUTPUT</font>** $y$ value.  

{{% geogebra ratio="53.33%" id_1="7vUTOXYoQLp7HDaD" id_2="lQTU2l1r" id_m="lQTU2l1r" %}}

To evaluate $f(5)$, for example, move the **<font color="blue">INPUT</font>** to $x=5$ and read off the corresponding **<font color="red">OUTPUT</font>** on the $y$-axis.  In this case, $f(5)=4$.  

So to use a graph to find a function's output, just find where your input value meets the graph. The height of that point is your answer.

Solving reverses the process-we find $x$ when given a specific $y$.  As an example, to solve $f(x)=4$ for $x$ you move the  **INPUT** until the **OUTPUT** equals $4$.  Then you record the **INPUT**.  Here there are multiple values for $x$ that work: $x=1.7$, $x=4$, and $x=11.7$ all appear to give outputs of $4$ and would be valid solutions to $f(x)=4$.

{{% check %}}
![](/img/chapter-1/evaluate_function_graph.svg#center)
1.  Use the graph above to evaluate $f(2)$.{{% answer %}}When $x=2$ the matching $y$ value on the graph is $y=1$, so $f(2)=1$.
![](/img/chapter-1/evaluate_function_graph_answer.svg#center){{% /answer %}}
1.  Use the graph above to evaluate $f(x)=3$.{{% answer %}}When $y=3$ the matching $x$ value on the graph is $x=-2$, so the solution to $f(x)=3$ is $x=-2$.
![](/img/chapter-1/solve_function_graph_answer.svg#center){{% /answer %}}
{{% /check %}}

## The Vertical Line Test
It is important to remember that not every relationship or rule defines a function.  The key is that each input corresponds to just one output.  This applies to graphs as well.

In order for a graph to be a function each $x$ can only correspond to one $y$.  This means that no two points on the graph can share the same $x$-coordinate.   

A quick way to test this is to imagine drawing vertical lines across it. If any line hits the graph more than once, it's not a function. For obvious reasons, this is called the **vertical line test**.

In each of the figures below there is a **<font color="blue">blue</font>** vertical line.  Apply the vertical line test to each graph by moving the vertical line across the graph.

{{% geogebra ratio="50%" id_1="NaLzd8wzExszZzM4" id_2="dhf2es4y" id_m="r9g6gyym" %}}

The vertical line test is very useful, but we must make sure we can see the entire graph.

{{% check %}}
1.  Does the equation $y=2x-3$ define $y$ as a function of $x$?   {{% answer %}}Yes, each $x$ will create exactly one $y$ value.  And if we graph $y=2x-3$ it clearly passes the vertical line test.<br>![](/img/chapter-1/function_graph_VLT_Quick_Check_1.svg#center){{% /answer %}}
1.  If $x+2y=4$, is $y$ a function of $x$?   {{% answer %}}Yes.  Rewriting the equation as $y=-1/2 x +2$ we see that each $x$ has exactly one corresponding $y$ value and the graph passes the vertical line test.<br>![](/img/chapter-1/function_graph_VLT_Quick_Check_2.svg#center){{% /answer %}}
1.  Use a graph to decide if the equation $x^2+y^2=3$ defines $y$ as a function of $x$. {{% answer %}}No, the graph  of $x^2+y^2=3$ is a circle, which would not pass the vertical line test.
<br>![](/img/chapter-1/function_graph_VLT_Quick_Check_3.svg#center)<br>
To graph $x^2+y^2=3$ on a calculator you would need to solve for $y$, which results in two equations.  The top half of the circle is $y=\sqrt{3-x^2}$ and the bottom half is $y=-\sqrt{3-x^2}$.  Looking at just one half might lead you to incorrectly assume that the equation is a function.{{% /answer %}}
{{% /check %}}


## Domain of a Function
Every time we identify a function we should also determine its domain.  Recall that the domain is like the list of buttons on a vending machine: it's all the possible input choices you have.

When a function is defined by a table, a diagram or a set of points, then we can list each individual item in the domain, like we did in the sandwich and vending machine examples earlier.

When a function is defined by an equation, the domain is every real number that produces a real number output.  

For instance, if $f(x)=\sqrt{x} $ then the domain is any real number greater than or equal to zero, since square roots of negative values are not real numbers.  This can be written as an interval $[0,\infty)$ or with set-builder notation $\lbrace x \vert  x \ge 0 \rbrace $.

Similarly, the domain of $g(x)=\frac{1}{x}$ is every real number except zero, since division by zero is undefined.  Writing this as an interval is a bit tricky since we have to use a union:  $(-\infty,0)  \bigcup  (0,\infty)$.  With set-builder notation we simply say which $x$ values cannot be used: $ \lbrace x \vert  x \neq 0 \rbrace $.

As this example shows, it is often easiest to say what is not in the domain.  Specifically, we must always eliminate from the domain any numbers that result in division by zero and even roots of negative numbers.


{{% check %}}
1.  Explain why the domain of $f(x)=\frac{1}{x^2-9}$ is $ \lbrace x \vert x \neq \pm 3 \rbrace $. {{% answer %}}The denominator cannot equal zero, so $x$ cannot be $3$ or $-3$. Using interval notation the domain is $(-\infty,-3) \bigcup (-3, 3) \bigcup (3,\infty)$.  With set-builder notation we can write that a bit more compactly as { $ x  \vert  x\neq \pm 3 $ }.{{% /answer %}}
1.  What is the domain of $g(x)=\sqrt{x-5}$? {{% answer %}}To avoid taking the root of a negative number, $x-5 \geq 0$, or $x \geq 5$.  Using interval notation the domain is $[5, \infty)$.  With set builder-notation it is $\lbrace x \vert  x \geq 5 \rbrace$.{{% /answer %}}
1.  Find the domain of $h(x)=\sqrt[3]{x}$. {{% answer %}}The cube root is not an even root, so the domain is all real numbers.{{% /answer %}}
{{% /check %}}


## Looking Ahead
Until we gain familiarity with several different types of functions, it will be difficult to determine the range of a function by inspecting its equation.  We will have more success if we work with its graph instead.  

Graphs are also one of the best ways to determine the domain of a function.  In fact, we can learn a lot about a function from looking at its graph.  This will be the focus of the next section.
---
title: "1.3 Graphs of Functions"
description: Just like roller coasters, functions can go up and down and have peaks and valleys.
author: "Nolan Mitchell"
type: page
image: "coaster.jpg"
draft: false
tags: ["graphing-with-technology", "increasing", "decreasing", "constant", "growth", "decay", "maximums-and-minimums", "local-maximum", "local-minimum", "global-maximum", "global-minimum", "extrema", "optimization", "intercepts", "x-intercepts", "y-intercepts", "real-zeros", "concavity", "concave-up", "concave-down", "asymptotes", "vertical-asymptote", "horizontal-asymptote", "end-behavior", "complete-graphs", "domain-from-graphs", "range-from-graphs", "library-functions", "identity-function", "square-function", "square-root-function", "cube-function", "cube-root-function", "reciprocal-function", "parabola"]
---

{{% imgcap file="/img/chapter-1/roller_coaster.jpg" title="Roller coaster photo by dlohner on Pixabay" source="https://pixabay.com/en/roller-coaster-amusement-park-3100041/"%}}

## Intro
If you've ever ridden a roller coaster you know how it feels to crawl up a hill and rocket down the other side. You also know how your stomach floats at the top and sinks at the bottom. It would be a very boring ride if the track never changed direction. The twists and turns, peaks and valleys make a roller coaster exciting and give it character.

The same can be said for functions: they wouldn't be interesting (or very useful) if they didn't change.

In this section you will learn to recognize features of a function by looking at a graph, in much the same way that you could pick out the loops and dips of a roller coaster from a photograph.


## Graphing Functions with Technology
When we first encounter a new function we will generally want to see its graph.  The equation will also be an essential tool, but lots of information can be gleaned from a quick look at the graph.

In the previous section we showed how the equation of a function can be used to create a table of values that can be plotted to create a graph.  While knowing how to do that by hand is a useful skill, the technology available today makes exploring graphs of functions much simpler.

Between a graphing calculator, apps on your phone, and dedicated websites like [Desmos.com](https://www.desmos.com/calculator) or [Geogebra.org](https://www.geogebra.org/classic), we will assume that you are able to use technology to draw a graph of a function.  

This section will help you read the graph of function and identify the features you see.


## Increasing, Decreasing and Constant
When we read the shape of a function's graph, we always read from left to right, just like we read words in a sentence. For instance, a function **increases** if its graph goes up as we move from left to right and **decreases** if it goes down. These behaviors are also referred to as growth and decay, respectively. If the graph is flat then the function is **constant** on that interval; it does not grow or decay.

Consider the following graph.

![](/img/chapter-1/increasing_decreasing.svg#center)

This function is increasing on the interval $(a,b)$, constant on $(b,c)$, decreasing over the interval $(c,d)$ and increasing again on $(d,e)$.

{{% check %}}
Determine the regions where the graph below is increasing, decreasing or constant.

![](/img/chapter-1/increasing_decreasing_c.svg#center) {{% answer %}}The graph is constant on $A$, increasing on $B$, and decreasing on $C$.{{% /answer %}}
{{% /check %}}


## Maximums and Minimums
Any point where a function changes from increasing to decreasing is known as a **local maximum**.  On a graph it looks something like this.

![](/img/chapter-1/local_max.svg#center)

If $f$ has a local maximum at $x=a$, then $f(a)$ is greater than any other function value in its immediate neighborhood, to the left or right.

If it turns out that $f(a)$ is the largest value of the function over its entire domain, then $f(a)$ is called a **global maximum**

Likewise, the point where a function changes from decreasing to increasing is called a **local minimum**.   

![](/img/chapter-1/local_min.svg#center)

If $f$ has a local minimum at $x=b$, then $f(b)$ is less than any other function values in the immediate neighborhood.

If it happens that $f(b)$ is the lowest value over the entire domain of the function, then $f(b)$ is called a **global minimum**.

Maximum and minimum points are important in many real life applications. For instance, we might want to minimize cost, or maximize fuel efficiency, or minimize waste.

The process of finding exact maximum and minimum values is called *optimization* and is properly studied in calculus. For our needs, however, a visual inspection of the graph will usually be accurate enough. When more precision is needed, the `maximum` and `minimum` commands found on most graphing utilities can be used.

{{% check %}}  
Use the graph below to answer the questions that follow.

![](/img/chapter-1/max-min_quick_check.svg#center)

1. At which $x$ value does the function obtain a local maximum? What is value of the local maximum?{{% answer %}}The local maximum occurs at $x=0$.  The value of the local maximum is $f(0)= 2$.
{{% /answer %}}
1. At which $x$ value does the function obtain a local minimum? What is value of the local minimum?{{% answer %}} The local minimum occurs at $x=2$.  The value of the local minimum is $f(2)= 0$.
{{% /answer %}}
1. At which $x$ value does the function obtain a global minimum? What is value of the global minimum?{{% answer %}}The global minimum occurs at $x=-3$.  The value of the global minimum is $f(-3)= -4$.
{{% /answer %}}
{{% /check %}}


## Intercepts
In addition to maximum and minimum points, we should also look for points where the graph intersects the axes. The point where the graph crosses the y-axis is called the **y-intercept**.  An **x-intercept** is a point where the graph intersects the x-axis.

![](/img/chapter-1/intercepts.svg#center)

Both of these concepts should be familiar to you from earlier algebra courses. The only new thing to be aware of is that x-intercepts will sometimes be called **real zeros**.  This is because those x-values are real numbers that make the function equal to zero.

{{% check %}}
Decide if the following statements are True or False.

1. True or False:  The x-coordinate of a y-intercept is $0$. {{% answer %}}True.{{% /answer %}}
1. True or False:  The y-coordinate of an x-intercept is $0$.{{% answer %}}True.{{% /answer %}}
1. True or False:  A function can have several y-intercepts.{{% answer %}}False.  A graph that has multiple y-intercepts, like this example,  ![](/img/chapter-1/intercepts_quick_check_answer_1.svg)<br> will not pass the vertical line test and cannot be a function.{{% /answer %}}
1. True or False:  A function can have several x-intercepts.{{% answer %}}True.  A function can have many x-intercepts. This function, for instance, has four x-intercepts.  ![](/img/chapter-1/intercepts_quick_check_answer_2.svg){{% /answer %}}
1. True or False:  A "real zero" is the same thing as an x-intercept.{{% answer %}}True.  That is a new vocabulary term.{{% /answer %}}
{{% /check %}}


## Concavity
Another important feature of a graph is its curvature, also known as its concavity. If a graph bends up, as if to form the side of a cup, then we say it is **concave up** on that interval. If the graph bends down, like a frown, then it is **concave down**. If the graph is straight then it does not bend and does not have any concavity.

![](/img/chapter-1/concavity_details.svg#center)

Note that concavity does not tell us if a graph is increasing or decreasing.  Instead, it gives us information about how quickly, or slowly, that change is happening.  

For instance, a function that is both increasing and concave down will see its rate of growth slow down.  But the growth rate of an increasing, concave up function will speed up.  Rates of change will be studied in detail [in a later section](../1.6/#concavity-and-rates-of-change).

{{% check %}}
1. Identify the regions where the following graph is concave up and concave down.
![](/img/chapter-1/concavity_prob_b.svg#center){{% answer %}}
![](/img/chapter-1/concavity_prob_b_answer.svg#center)
{{% /answer %}}
{{% /check %}}


## Asymptotes
Sometimes a function increases (or decreases) without bound toward infinity as it approaches a particular $x$ value. When this happens we say the function has a **vertical asymptote** at that $x$ value.  In this example there is a vertical asymptote at $x=-1$.

![](/img/chapter-1/vertical_asymptote.svg#center)

Formally, the vertical line $x=c$ is a vertical asymptote of a function if $f(x)$ approaches either positive or negative infinity as $x$ gets near to $c$.  This is sometimes written $f(x)\rightarrow\pm \infty$ as $x \rightarrow c$.

We will use dotted vertical lines to indicate vertical asymptotes. Very few graphing utilities will draw asymptotes. You will have to infer their locations from the shape of the graph.

It is also possible for a function to eventually level off to the left or to the right.  When this happens we say the function has a **horizontal asymptote**. In the example below, the function has a horizontal asymptote at $y=3$.

![](/img/chapter-1/horizontal_asymptote.svg#center)

Technically speaking, the horizontal line $y=k$ is a horizontal asymptote of a function  if $f(x)\rightarrow k$ as $x \rightarrow \pm \infty$.

Horizontal asymptotes describe a type of end behavior of a function.  The **end behavior** of a function is how the function changes as $x$ approaches positive infinity or negative infinity. When looking for end behaviors, it doesn't matter how the function behaves in any local neighborhood, it only matters what happens far out at the ends. We will see functions with various combinations of increasing, decreasing and leveling off end behaviors.

Since a function can only have two end behaviors (one as $x \rightarrow \infty$ and another as $x \rightarrow -\infty$), a function can only have, at most, two horizontal asymptotes. There is no such limit on the number of vertical asymptotes.

{{% check %}}
Try to identify each of the following behaviors. Click the arrows to check your answers.

![](/img/chapter-1/identify_behaviors.svg#center)

1. <details><summary>y-intercept</summary>This function has a y-intercept at $y=2$.</details>
1. <details><summary>x-intercepts</summary>There are three x-intercepts:  $x=-1$, $x=3$, and $x=5$</details>
1. <details><summary>Maximums</summary>There is a global maximum at $(2, 4)$ and a local maximum at $(6, 2)$.</details>
1. <details><summary>Minimums</summary>There is a local minimum at $(4, -2)$, but the function does not have a global minimum.</details>
1. <details><summary>Vertical Asymptotes</summary>There appears to be a vertical asymptote at $x=-2$</details>
1. <details><summary>Horizontal Asymptotes</summary>The function seems to level off around $y=1$ as $x \rightarrow \infty$, so that is a horizontal asymptote.</details>
<details>
  <summary>See all</summary>
  <img src="/img/chapter-1/identify_behaviors_answers.svg" alt="Identify Behaviors Answers">
</details>

{{% /check %}}


## Complete Graphs
A graph that indicates all the important features of a function is called a **complete graph**.  If a function has any intercepts, asymptotes, maximums and/or minimums, then those should be visible on a complete graph.

Creating a complete graph can be a difficult adventure. Very few, if any, graphing programs will automatically give you a complete graph.  However, they all have commands for zooming in and out and changing the viewing window.

As you learn more about different types of functions, you will be able to reduce the amount of guess work by recognizing how elements of the equation affect the shape of the graph.  For now, however, you will want to experiment with the different zoom and window commands available.


## Determine Domain and Range from a Graph
A complete graph can help us identify the domain and range of a function.  Since each point on the graph has an $x$ and a $y=f(x)$ coordinate, the domain and range are the spread of the $x$ and $y$ values, respectively.  

For instance, a complete graph of $f(x)=x^{2}-3$ is shown below.

![](/img/chapter-1/graph_domain_range_x2-3.svg#center)

Since the graph continues to expand in the x-direction, its **<font color="red">domain</font>** is the set of all real numbers $\color{red}{ \lbrace x \thinspace \vert \thinspace  x \text{ is in } \mathbb{R} \rbrace }$ or the interval $\color{red}{(-\infty, \infty)}$.  The $\color{blue}{y}$ values start at $\color{blue}{y=-3}$ and continue upward, so the **<font color="blue">range</font>** is the set $\color{blue}{\lbrace y \thinspace \vert \thinspace y \geq -3 \rbrace}$ or the interval $\color{blue}{[-3, \infty)}$.

{{% check %}}
1.  Determine the domain and range of the function shown below.  Assume the graph is a complete graph.
![](/img/chapter-1/graph_domain_range_e.svg#center) {{% answer %}}The domain is all real numbers.
The range is $(-\infty, 5]$, also written as $\lbrace y \thinspace \vert \thinspace y \leq 5 \rbrace$.{{% /answer %}}
{{% /check %}}

Let's look at another example. Suppose the following is a complete graph of a function.

![](/img/chapter-1/graph_domain_range_a.svg#center)

You might recall that solid dots are always considered part of the graph.  Hollow dots, on the other hand, are used to indicate points that are not part of the graph. Here the **<font color="red">domain</font>** is the interval $\color{red}{(-2,  2 ]}$ and the **<font color="blue">range</font>** is $\color{blue}{(-2, 4 ]}$.{{% sidenote "domain_range_1" %}}In set notation the **<font color="red">domain</font>** is $\color{red}{ \lbrace x \thinspace \vert \thinspace -2 < x \leq 2 \rbrace }$ and the **<font color="blue">range</font>** is $\color{blue}{\lbrace y \thinspace \vert \thinspace -2 < y \leq 4 \rbrace}$ {{% /sidenote %}}


{{% check %}}
1.  Determine the domain and range of the function shown below.  Assume the graph is a complete graph.
![](/img/chapter-1/graph_domain_range_d.svg#center) {{% answer %}}The domain is $(-3, 2]$, or $\lbrace x \thinspace \vert \thinspace -3 < x \leq 2 \rbrace$. <br>  
The range is $[-3, 5]$, or $\lbrace y \thinspace \vert \thinspace -3 \leq y \leq 5 \rbrace$.{{% /answer %}}
{{% /check %}}

If the graph has asymptotes then the domain and range might require the union of several intervals.  In this case, the vertical asymptotes indicate that the values $x=-1$ and $x=1$ are not in the domain.  

![](/img/chapter-1/graph_domain_range_f.svg#center)

The **<font color="red">domain</font>** is split into three intervals that we union together:  $\color{red}{(-\infty, -1) \bigcup (-1, 1) \bigcup (1, \infty)}$.  The horizontal asymptote  doesn't impact the range, since the center section rises above the asymptote, so our **<font color="blue">range</font>** is $\color{blue}{(-\infty, 4]}$.


## Graphs of Basic Functions
Below you will be introduced to six basic functions that you should learn by heart.  Use the provided graphs to look for important behaviors.  Click the link below each graph to check your answers or refer to this [downloadable summary](/img/chapter-1/Six_Basic_Functions.pdf).  

### The Identity Function
The identity function $f(x)=x$ is special because the output is always the same as the input, for example $f(5)=5$ or $f(87)=87$.  Its graph is the diagonal line through the origin with a slope of $1$.
![](/img/chapter-1/library_identity.svg#center)
<details><summary>Identity Function Properties</summary>

* **Domain and Range:** Both the domain and range include all real numbers.
* **Intercepts:** Since this function crosses at the origin, both the y-intercept and the x-intercept are at the point $(0, 0)$.
* **Increasing, Decreasing, Constant:** The identity function is increasing over its entire domain.  It never decreases or becomes constant.
* **Maximums and Minimums:** There are no maximums or minimums.
* **Asymptotes:** There are no vertical or horizontal asymptotes.</details>  
<br>


### The Square Function
The square function $f(x)=x^2$ returns the square of every input, for example $f(3)=3^2=9$.  Its graph is a parabola touching the origin.

With negative inputs it is best to include parenthesis like this $f(-2)=(-2)^2=4$ to get the correct values.  
![](/img/chapter-1/library_square.svg#center)
<details><summary>Square Function Properties</summary>
The graph of the square function is a *parabola*.

* **Domain and Range:** The domain is all real numbers.  The range is the interval $[0, \infty)$.
* **Intercepts:** The y-intercept is $y=0$.  The x-intercept is $x=0$.  Both occur at the same point, the origin $(0, 0)$.
* **Increasing, Decreasing, Constant:** The function is decreasing on $(-\infty, 0)$ and increasing over the interval $(0, \infty)$.  It is not constant anywhere.
* **Maximums and Minimums:** There are no maximums, but there is a global minimum at $(0, 0)$.
* **Asymptotes:** There are no vertical asymptotes and no horizontal asymptotes.</details>  
<br>


### The Square Root Function
The principal square root function $f(x)=\sqrt{x}$ evaluates the square root of non-negative inputs only, it is not defined for negative values.  

Most calculators have a dedicated button for computing square roots.  Its graph starts at the origin.
![](/img/chapter-1/library_square_root.svg#center)
<details><summary>Square Root Function Properties</summary>

* **Domain and Range:** The domain is $\lbrace x \ \vert \ x \geq 0 \rbrace$.  The range is $\lbrace y \ \vert \ y \geq 0 \rbrace$.
* **Intercepts:** Since this function starts at the origin, the y-intercept and the x-intercept are at the same point, $(0, 0)$.
* **Increasing, Decreasing, Constant:** The function is increasing over its entire domain.  It is never decreasing or constant.
* **Maximums and Minimums:** There are no maximums, but $(0, 0)$ is a global minimum.
* **Asymptotes:** There are no vertical or horizontal asymptotes.</details>  
<br>


### The Cube Function
The cube function $f(x)=x^3$ produces the cube of any input, which is simply that number multiplied by itself three times.  For instance, $f(2)=2^3=8$ since $2 \times 2 \times 2=8$.

Most calculators do not have a dedicated button for the cube function, instead you must enter something like **`2^3`** to cube $2$.
![](/img/chapter-1/library_cube.svg#center)

<details><summary>Cube Function Properties</summary>

* **Domain and Range:** Both the domain and range include all real numbers.
* **Intercepts:** This function crosses at the origin, so both the y-intercept and the x-intercept are at the point $(0, 0)$.
* **Increasing, Decreasing, Constant:** The function is increasing over its entire domain.  It is never decreasing or constant.
* **Maximums and Minimums:** There are no maximums or minimums.
* **Asymptotes:** There are no vertical or horizontal asymptotes.</details>  
<br>


### The Cube Root Function
Many calculators have a command somewhere that will evaluate the cube root function $f(x)=\sqrt[3]{x}$ but it might be hard to find.  

It is often easier to use the rule of exponents $\sqrt[3]{x}=x^{1/3}$ to evaluate cube roots.  For example **`125^(1/3)`** would give the cube root of $125$.
![](/img/chapter-1/library_cube_root.svg#center)

<details><summary>Cube Root Function Properties</summary>

* **Domain and Range:** Both the domain and range include all real numbers.
* **Intercepts:** Since this function crosses at the origin, the y-intercept and the x-intercept are both $0$.
* **Increasing, Decreasing, Constant:** The function is increasing over its entire domain.  It is never decreasing or constant.
* **Maximums and Minimums:** There are no maximums or minimums.
* **Asymptotes:** There are no vertical or horizontal asymptotes.</details>  
<br>


### The Reciprocal Function
The reciprocal function $f(x)=\frac{1}{x}$ takes any number (except $0$) as an input and returns the reciprocal of that number. The easiest way to remember what a reciprocal is, is to see a few examples.  

* The reciprocal of $\frac{3}{2}$ is $\frac{2}{3}$.  
* The reciprocal of $5$ is $\frac{1}{5}$.
* The reciprocal of $\frac{-6}{7}$ is $\frac{-7}{6}$.

You might recall that $\frac{1}{x}=x^{-1}$ is a rule of exponents.  Because of that, many calculators have a button labeled $x^{-1}$ which will compute the reciprocal of a number.
![](/img/chapter-1/library_reciprocal.svg#center)

<details><summary>Reciprocal Function Properties</summary>

* **Domain and Range:** The domain is all real numbers except $0$, since division by $0$ is undefined.  The range is also all real numbers except for $0$.
* **Intercepts:** This function does not have any intercepts.
* **Increasing, Decreasing, Constant:** The reciprocal function is increasing on $(-\infty,0)$ and decreasing on $(0,\infty)$.
* **Maximums and Minimums:** There are no maximums or minimums.
* **Asymptotes:** The y-axis is a vertical asymptote.  The x-axis is a horizontal asymptote.</details>
<br>

## Looking Ahead
These six basic functions form a library that we will use to explore several different topics.  Since they are building blocks for more complicated ideas, you will be expected to memorize their basic properties.  This [downloadable summary](/img/chapter-1/Six_Basic_Functions.pdf) will help your study.
---
title: "1.4 Transformations of Functions"
description: "When making ice cream, chefs often start with a basic recipe and then add in special ingredients.  In a very similar way, we can take basic functions and transform them into new functions by adding constants into the mix."
author: "Nolan Mitchell"
type: page
image: "ice-cream-ice-cream-flavors-fruits-2202605.jpg"
draft: false
tags: ["transformations", "vertical-shifts", "horizontal-shifts", "vertical-stretches", "horizontal-stretches", "vertical-reflections", "horizontal-reflections", "stretch", "compression", "even-symmetry", "reflection-across-y-axis", "odd-symmetry", "reflection-around-origin", "verifying-symmetry-algebraically", "inside-changes", "outside-changes"]
---

{{% imgcap file="/img/chapter-1/ice-cream-ice-cream-flavors-fruits-2202605.jpg" title="Ice cream cones photo by silviarita on Pixabay" source="https://pixabay.com/en/ice-cream-ice-cream-flavors-fruits-2202605/"%}}

## Introduction
When making ice cream, chefs often start with a basic recipe and then add in different amounts of special ingredients, like macadamia nuts or dark chocolate or berries. Experienced chefs know the effect that each addition will have before they even taste the finished product.

In a very similar way, we can take basic functions and transform them into new functions by mixing in constants.  As you gain experience you will be able to predict the behavior of a transformed function without graphing it.  You will also learn to construct the equation for a function given its graph.

Given a generic function $f$ and any constant number $\color{blue}{c}$, there are four ways to combine them to form a new function.  We could

| 1. |Add $\color{blue}{c}$ to the function value $f(x)$. |  $f(x)+\color{blue}{c}$ |
| ----- | ----- | ----- |
| 2. |Add $\color{blue}{c}$ to the input value $x$.|  $f(x+\color{blue}{c})$ |
| 3. |Multiply $f(x)$ by $\color{blue}{c}$.| $\color{blue}{c} \thinspace  f(x)$ |
| 4. |Multiply $x$ by $\color{blue}{c}$. | $f(\color{blue}{c} \thinspace x)$ |

We will use interactive figures to explore each of these combinations.  Pay special attention to how both the graph and the equation change as you apply the transformation.  It may even help to keep track of one or two points and compare their locations before and after the transformation.


## Vertical Shifts
The first transformation we want to look at is adding a constant $\color{blue}{c}$ to the output of the function, $f(x)$.

In this figure you can change the value of $\color{blue}{c}$. The graph of the original function $\color{black}{f(x)}$ is shown in $\color{black}{black}$.  The transformed function $\color{red}{f(x)}  \color{blue}{+ c}$ will be shown in $\color{red}{red}$.

How would you describe the relationship between the two graphs?

{{% geogebra ratio="50%" id_1="54RjPl1XZOn2p1CE" id_2="Y5TzgBaP" id_m="Y5TzgBaP" %}}

The result of adding a constant to a function is that the graph moves up or down $\color{blue}{c}$ spaces.

More formally, if $\color{red}{f}$ is any function and $\color{blue}{c}$ is any constant, then the graph $\color{red}{f(x)}  \color{blue}{+ c}$ is a **vertical shift** of the function $f$.  The graph of $\color{red}{f(x)}  \color{blue}{+ c}$ can be found by adding $\color{blue}{c}$ to every y-value of the original graph.  We can summarize this by saying

* If $\color{blue}{c>0}$, then $\color{red}{f(x)} \color{blue}{+ c}$ is found by shifting the graph of $f$ up $\color{blue}{c}$ spaces.
* If $\color{blue}{c<0}$, then $\color{red}{f(x)} \color{blue}{+ c}$ is found by shifting the graph of $f$ down $\color{blue}{c}$ spaces.


{{% check %}}
1. How is the graph of $y=\sqrt{x}+10$ different from the graph of $f(x)=\sqrt{x}$ ? {{% answer %}}The graph of $y=\sqrt{x}+10$ has the same shape as the graph of $f(x)=\sqrt{x}$, except that it has been shifted up $10$ spaces.{{% /answer %}}
1. What function would have the same shape as $f(x)=x^{2}$ but shifted $6$ spaces up?{{% answer %}}$f(x)+6 = x^{2}+6${{% /answer %}}
{{% /check %}}


## Horizontal Shifts
Another way to transform a function is to add a constant $\color{blue}{c}$ to the input $x$. Use the figure to observe what happens to $\color{red}{f(x }\color{blue}{+ c} \color{red}{)}$ as the value of $\color{blue}{c}$ changes.

Pay special attention to the sign of $\color{blue}{c}$.  Which direction is the transformation when $\color{blue}{c}$ is positive?

{{% geogebra ratio="33.33%" id_1="yzTEP1RsXxkbsT26" id_2="YJUZlyHJ" id_m="YJUZlyHJ" %}}
</br>
You have just seen that the graph of $\color{red}{f(x } \color{blue}{+ c}\color{red}{)}$ is a <strong>horizontal shift</strong> of the function $f$.  The graph of $\color{red}{f(x } \color{blue}{+ c}\color{red}{)}$  can be found by subtracting $\color{blue}{c}$ from every x-value of the original graph.  In other words,

* If $\color{blue}{c>0}$, then $\color{red}{f(x} \color{blue}{+ c}\color{red}{)}$ is found by shifting $f$ to the left $\color{blue}{c}$ spaces.
* If $\color{blue}{c<0}$, then $\color{red}{f(x } \color{blue}{+ c}\color{red}{)}$ is found by shifting $f$ to the right $\color{blue}{c}$ spaces.

Horizontal shifts are somewhat counter intuitive, and you will want to refer back to this chart often as you work through the exercises.

Vertical and horizontal shifts do not change the shape of the graph, only its location.  Our next few transformations, however, will alter the shape of the graph.

{{% check %}}
Suppose the function $P(h)$ gives your weekly pay based on the number of hours worked.

![](/img/chapter-1/translate_pay.svg#center)

1.  Describe what the graph of $P(h+10)$ would look like, and what it would mean. {{% answer %}}$P(h+10)$ is a shift left 10 spaces.  It corresponds to getting paid for 10 extra hours of work. <br>![](/img/chapter-1/translate_pay_answer_plus.svg#center)<br> If you worked 15 hours, for example, then you would be paid for 25 hours of work.{{% /answer %}}  
1.  Describe what the graph of $P(h-10)$ would look like, and what it would mean. {{% answer %}}$P(h-10)$ is a shift right 10 spaces. It would represent being paid for 10 fewer hours. <br>![](/img/chapter-1/translate_pay_answer_minus.svg#center)<br> For instance, if you worked for 40 hours, you would only be paid for 30.{{% /answer %}}
1. What function would have the same shape as $f(x)=x^{2}$ but shifted $4$ spaces horizontally to the left?{{% answer %}}$f(x+4) = (x+4)^2${{% /answer %}}
{{% /check %}}


## Vertical Stretches
The two previous transformations involved addition and resulted in a shift.  Using the figure below, you can discover the effect of multiplying a function by a positive constant $\color{blue}{c}$.  As you change the value of $\color{blue}{c}$ , the graph of  $\color{blue}{c}\color{red}{ f(x)}$ will change as well.  How would you describe this change?

{{% geogebra ratio="50%" id_1="F1Ew7ZyIA2OY7Kty" id_2="HJhxc4Lx" id_m="HJhxc4Lx" %}}

Hopefully you noticed that multiplying a function by a constant $\color{blue}{c}$ stretches the graph up and down.

In other words, if $\color{red}{f}$ is any function and $\color{blue}{c}$ is any constant, then the graph of  $\color{blue}{c}\color{red}{ f(x)}$ is a **vertical stretch** of the original function $\color{red}{f}$. The graph of $\color{blue}{c}\color{red}{ f(x)}$ can be found by multiplying each y-value of the original graph by $\color{blue}{c}$.  

If $\color{blue}{0<c<1}$, then the graph $\color{blue}{c}\color{red}{f(x)}$ is sometimes called a vertical *compression* of the graph of $\color{red}{f}$.  We will use the word stretch for both situations, with the understanding that the graph is always scaled by a factor of $\color{blue}{c}$.

{{% check %}}
1. Suppose $(2, 5)$ is a point on the graph of the function $\color{red}{f}$.  What does the transformation  $\color{blue}{4}\color{red}{f(x)}$ do to that point? {{% answer %}}The transformation multiplies the y-value by a factor of $\color{blue}{4}$ transforming the point $(2, 5)$ into $(2, 20)$.{{% /answer %}}
1. Suppose $(3, 8)$ is a point on the graph of the function $\color{red}{g}$.  What does the transformation  $\color{blue}{0.5}\color{red}{g(x)}$ do to that point? {{% answer %}}The transformation multiplies the y-value by a factor of $\color{blue}{0.5}$, transforming the point $(3, 8)$ into $(3, 4)$.{{% /answer %}}
1. What function would look like $f(x)=x^{2}$ but stretched vertically by a factor of $5$?{{% answer %}}$5f(x) = 5 x^{2}${{% /answer %}}
{{% /check %}}


## Horizontal Stretches
A function can be stretched horizontally by multiplying the input $x$ by some constant $\color{blue}{c}$. Use the following interactive figure to observe how the shape of the graph changes for different values of  $\color{blue}{c}$.

How much wider is the function when $\color{blue}{c = 2}$ as compared to when $\color{blue}{c = 0.5}$?

{{% geogebra ratio="33.33%" id_1="fzaGIdMEjf6Fclnv" id_2="ZPBnPTlS" id_m="ZPBnPTlS" %}}
<br>
This <strong>horizontal stretch</strong> is one of the most counter-intuitive transformations you will encounter.  You should have seen that the graph got wider when $\color{blue}{c}$ was small, and narrower when $\color{blue}{c}$ was large.

When we encounter a transformation of the form $\color{red}{f (} \color{blue}{c}\thinspace \color{red}{x)}$,  its graph can be found by dividing each x-value of the original graph by $\color{blue}{c}$.  

* If $\color{blue}{c>1}$, then the resulting graph is *compressed* horizontally.
* If $\color{blue}{0<c<1}$, then the resulting graph is *stretched* horizontally.

In either case, the x-values are always scaled by a factor of $\color{blue}{1/c}$.

{{% check %}}
1. Suppose that the graph of the function $f (x)$ below describes the path of an average drive by PGA professional Stewart Cink using his current golf club.<br>
![](/img/chapter-1/golf_drive.gif#center) Imagine that a new club has been developed that will transform $f(x)$ into $f(2 x)$.  What would this new club do to the distance of his drive? {{% answer %}}$f(2 x)$ is a horizontal stretch with $c=2$.  Since $c=2>1$, this will actually compress the graph horizontally, cutting the distance in half. <br> ![](/img/chapter-1/golf_drive_answer.gif)<br>  If the goal was to double the distance, the transformation would need to be $f\left(\frac{1}{2}x\right)$.{{% /answer %}}
1. What function would look like $f(x)=x^{2}$ but horizontally stretched by a factor of $3$? {{% answer %}}$f\left(\frac{x}{3}\right) = \left(\frac{x}{3}\right)^2${{% /answer %}}
{{% /check %}}

## Vertical and Horizontal Reflections
The last category of transformations we will study are the reflections.  The graph of $-f(x)$ is a **vertical reflection** of the function $f$ across the x-axis.  In a vertical reflection all of the y-coordinates change signs from positive to negative or vice versa.

{{% geogebra ratio="50%" id_1="ncdiPmvbZyEYCXgS" id_2="ae4EaVFq" id_m="ae4EaVFq" %}}

The graph of $f(-x)$ is a **horizontal reflection** of $f$ across the y-axis.  With horizontal reflections the x-coordinates change signs.

{{% geogebra ratio="50%" id_1="lTM0WJ1IbOmHhKiv" id_2="xQwb021E" id_m="xQwb021E" %}}

Notice that these transformations follow the pattern of inside/outside changes we've seen before.  Putting the negative sign *outside* the function causes a vertical reflection, while a negative *inside* the function produces a horizontal reflection.

{{% check %}}
1. Find the equation of a function whose graph looks similar to $f(x)=\sqrt{x}+3$, except reflected across the x-axis. {{% answer %}}$y=-\sqrt{x}-3$.{{% /answer %}}
2. Find the equation of a function whose graph looks similar to $f(x)=\frac{1}{x-2}$, except reflected across the y-axis. {{% answer %}}$y=\frac{1}{-x-2}$.{{% /answer %}}
{{% /check %}}


## Identifying Transformations
The six transformations we have discussed so far are summarized below.

| **Transformation** | **Description** | **Coordinate Change** |
|-----|-----|-----|
| $f(x)\color{blue}{+c}$ | Vertical Shift | $(x, y) \rightarrow (x \thinspace  , \thinspace y+\color{blue}{c})$ |
| $f(x\color{blue}{+c})$ | Horizontal Shift | $(x, y) \rightarrow (x-\color{blue}{c}  \thinspace  , \thinspace y)$ |
| $\color{blue}{c} \thinspace  f(x)$ | Vertical Stretch | $(x, y) \rightarrow (x  \thinspace  , \thinspace \color{blue}{c} \thinspace y)$ |
| $f(\color{blue}{c} \thinspace x)$ | Horizontal Stretch | $(x, y) \rightarrow \left(\frac{x}{\color{blue}{c}}  \thinspace  , \thinspace y\right)$ |
| $\color{blue}{-}f(x)$ | Vertical Reflection | $(x, y) \rightarrow (x  \thinspace  , \thinspace \color{blue}{-}y)$ |
| $f(\color{blue}{-}x)$ | Horizontal Reflection | $(x, y) \rightarrow (\color{blue}{-}x  \thinspace  , \thinspace y)$ |

Notice that the location of the constant indicates whether the transformation is vertical or horizontal.  Changes *outside* the function alter the y-coordinate and result in vertical transformations, while changes *inside* the function impact the x-coordinate and cause horizontal transformations.

Furthermore, you can determine if the transformation is a shift or a stretch by looking at the operation. Shifts are addition, stretches are multiplication.  Horizontal transformations always behave in a counter intuitive way, so you will want to be extra careful with them.

{{% check %}}
What is the difference between $2f(x)$, $ f(2x)$ and $ f(x)+2$ ? {{% answer %}}$2f(x)$ means to multiply each $f(x)$ value by $2$, resulting in a vertical stretch by a factor of $2$.</br></br> $f(2x)$ means to use $2 x$ as the input to the function $f$.  The result is a  horizontal compression by a factor of $1/2$. </br></br>$f(x)+2$ means we add $2$ to each $f(x)$ value, which shifts the graph vertically $2$ spaces.</br>{{% /answer %}}
{{% /check %}}



## Symmetry
Combining a horizontal reflection with a vertical reflection creates a **reflection around the origin**.

The interactive figure below allows you to compare the horizontal reflection of a point across the y-axis with a reflection around the origin.  Choose the reflection(s) you want to see and move the **<font color="blue">blue pont</font>**.  As you do so, the location of the points will be traced, creating an image that has symmetry.  Experiment with this for a while before continuing.

{{% geogebra ratio="33.33%" id_1="pCwpjVUJCY0aQfEe" id_2="iHmotfOF" id_m="iHmotfOF" %}}


## Even and Odd Symmetry
When reflecting a graph, two interesting things happen sometimes.  The first is that a horizontal reflection across the y-axis might  produce the same exact graph as the original function.  Symbolically, $f(-x)=f(x)$.  When this happens we say that the function has **even symmetry**, or is symmetric across the y-axis.   The figure below illustrates the concept.

{{% geogebra ratio="33.33%" id_1="gVgUDdts61aFd2vt" id_2="mSp9DhKO" id_m="mSp9DhKO" %}}

The other interesting thing that can happen with reflections is that a horizontal reflection and a vertical reflection might have the same result, that is $f(-x)=-f(x)$.  When this happens the function has **odd symmetry** and is symmetric around the origin.  Visually, a 180-degree rotation around the origin produces the same exact image.  This is illustrated in the following interactive figure.

{{% geogebra ratio="33.33%" id_1="IplJTS1bHxXgKrvp" id_2="DpMbG1ID" id_m="DpMbG1ID" %}}

{{% check %}}
Describe the symmetry of the following graphs.

1. &nbsp; ![](/img/chapter-1/symmetry_check_a.png#center){{% answer %}}Odd symmetry{{% /answer %}}
1. &nbsp; ![](/img/chapter-1/symmetry_check_d.png#center){{% answer %}}Even symmetry{{% /answer %}}
1. &nbsp; ![](/img/chapter-1/symmetry_check_c.png#center){{% answer %}}Odd symmetry{{% /answer %}}
1. &nbsp; ![](/img/chapter-1/symmetry_check_b.png#center){{% answer %}}This graph does not have even or odd symmetry.  Had it been centered along the y-axis, then it would have had even symmetry.{{% /answer %}}
1. &nbsp; ![](/img/chapter-1/symmetry_check_e.png#center){{% answer %}}This graph does not have even or odd symmetry.  If it were centered at the origin, then it would have had odd symmetry.{{% /answer %}}
{{% /check %}}

## Verifying Symmetry Algebraically
While visual identification of symmetry is quick and easy, our eyes can sometimes be deceived.  If a function is defined by an equation, then it is best to verify symmetry algebraically.  If a function is even, then we should be able to demonstrate that the equations for $f(-x)$ and $f(x)$ are the same.  If it has odd symmetry, then the equations for $f(-x)$ and $-f(x)$ should be identical.

![](/img/chapter-1/symmetry_check_algebraic.png#center)

Consider the graph of $f(x)=x^3+0.01$, which appears to have odd symmetry.  Checking the equations we find that

\[
  f(-x) = (-x)^3+0.01 = -x^3+0.01
\]

while

\[
  -f(x) = -(x^3+0.01) = -x^3-0.01
\]

Since the two equations are not the same,  $f(x)=x^3+0.01$ does not have odd symmetry.  

A second look at the equation explains why this is the case.  Notice that $f(x)=x^3+0.01$ is nothing more than the cube function shifted $0.01$ units up.  It's graph

![](/img/chapter-1/symmetry_check_algebraic_graph.png#center)

does not go through the origin, rather it has a y-intercept at $(0, 0.01)$.  It is this small shift that causes the function to lose its odd symmetry.

Let's look at one more example.  The graph of $f(x)=x^{2}-1$ looks like it has even symmetry.  

![](/img/chapter-1/symmetry_check_algebraic_graph_2.png#center)

To check this algebraically, we need to compare the equation for $f(-x)$ with the equation for $f(x)$.  If the two match, then it really does have even symmetry.  Otherwise, it does not.

Replacing $x$ with $-x$ we find that

\[
  f(-x) = (-x)^2-1 = x^{2}-1
\]

which is exactly the same equation as $f(x)$.  Since $f(-x)=f(x)$, we can confidently conclude that $f(x)=x^{2}-1$ has even symmetry.  


## Looking Ahead
In future chapters, we will find transformations included in the standard forms of several function models.  Being able to predict the effects of a shift or stretch will often simplify calculations and may give insight into easier techniques for solving equations.

Transformations will be helpful when we model data in Chapter 6.  If a data set looks like a line, for example, then we can apply shifts and stretches to the identity function $f(x)=x$ until we find a combination that fits the shape of the data.
---
title: "1.5 Inverse Functions"
description: "A process that brings you back to where you started is called an inverse.  It works just like a return flight on an airplane."
author: "Nolan Mitchell"
type: page
image: "Tahiti.jpg"
draft: false
tags: ["inverse-functions", "inverse-operations", "addition-subtraction", "multiplication-division", "powers-roots", "even-powers", "odd-powers", "definition-of-inverse", "one-to-one", "horizontal-line-test", "finding-inverses", "tables-diagrams", "graphing-inverses", "reflecting-across-y-equals-x", "inverses-of-basic-functions", "restricted-domain", "shoes-and-socks-method"]
---

{{% imgcap file="/img/chapter-1/Tahiti.jpg" title="Bora Bora, Tahiti photo by Julius Silver on Pexels" source="https://www.pexels.com/photo/cottages-in-the-middle-of-beach-753626/"%}}

## Introduction
Imagine that you flew to Tahiti for a vacation.  After spending some time enjoying the white sandy beaches and crystal clear water, you *might* want to return home.  To get back home you would need to find a return flight.

In mathematics, a process that brings you back to where you started is called an **inverse**.  

In this section you will learn to recognize when a function has an inverse and how to find it.


## Inverse Operations
Many real life processes have inverses while others do not.  For instance, if you put on your shoes and socks you can easily take them off, but once you boil an egg there's no way to make it raw again.

You are, no doubt, already familiar with some **inverse operations** in mathematics.  Adding and subtracting are inverse operations, for instance.  If you add $6$, and then subtract $6$, you end up right back where you started, having completed a round trip.  

![](/img/chapter-1/inverse_add_6.svg#center)

Multiplication and division are also inverse operations.  As an example, multiplying by $-3$ and dividing by $-3$ are inverse operations.

![](/img/chapter-1/inverse_multiply_neg_3.svg#center)

The only exception is $0$.  Multiplying by $0$ cannot be undone with division, since division by $0$ is not well defined.

There are other operations that sometimes have inverses and sometimes do not.  Powers and roots are prime examples. When working with positive numbers, powers and roots are always inverses.  Here are a few powers of $2$ and the corresponding roots, for instance.  

![](/img/chapter-1/inverse_square_2.svg#center)

![](/img/chapter-1/inverse_cube_2.svg#center)

![](/img/chapter-1/inverse_4th_power_2.svg#center)

It gets more complicated when working with negative numbers, however.  Consider the following powers and roots of $ -5$.

![](/img/chapter-1/inverse_square_neg_5.svg#center)

![](/img/chapter-1/inverse_cube_neg_5.svg#center)

![](/img/chapter-1/inverse_4th_power_neg_5.svg#center)

This time, taking an even power followed by an even root did not produce a round trip.  This indicates that even powers and roots are not always inverse operations.  Even powers and roots are inverses only when working with non-negative numbers.

The following table summarizes the basic inverse operations.

![](/img/chapter-1/inverse_operations.svg#center)

{{% check %}}
1.  What is the inverse of multiplying by $-4$?{{% answer %}} Dividing by $-4$.{{% /answer %}}
1.  What is the inverse of a power of $3$?{{% answer %}} The 3rd root $\sqrt[3]{\thinspace \cdot \thinspace}$, which is also the $\frac{1}{3}$ power. {{% /answer %}}
{{% /check %}}


## Definition of an Inverse Function
If a function has an inverse, then the inverse function should return each output back to its input, just like a return airline flight.  {{% definition %}} The <strong>inverse</strong> of a function $f$ is a function $f^{-1}$ with the property that whenever $f(a)=b$, it always follows that $f^{-1}(b)=a$.

![](/img/chapter-1/inverse_function_diagram.svg#center)
{{% /definition %}}
Note that the outputs of the original function become the inputs of the inverse function.  As a consequence, the domain of $f$ is the range of $f^{-1}$, and the range of $f$ is the domain of $f^{-1}$.

This new notation can be a bit confusing.  The symbol $f^{-1}$ is used to indicate the "inverse of $f $ ".  Even though the $-1$ looks like an exponent it is not:  $f^{-1}$ does **not** mean $\frac{1}{f}$.  

{{% check %}}
1.  Suppose the function $f$ has an inverse and that $f(3)=6$. What do you know about $f^{-1}(6)$?  {{% answer %}}$f^{-1}(6)=3${{% /answer %}}
1.  Suppose the domain of $f$ is $D= \lbrace 1, 2, 3, 4 \rbrace$ and that its range is $R= \lbrace 5, 6, 7, 8 \rbrace$.  What are the domain and range of $f^{-1}$?  {{% answer %}}The domain and range trade places.  The domain of the inverse function is the set $D = \lbrace 5, 6, 7, 8 \rbrace$ and its range is $R = \lbrace 1, 2, 3, 4 \rbrace$.{{% /answer %}}
{{% /check %}}


## Identify Invertible Functions
Let's look at two functions defined by diagrams and see if they have inverse functions.  

This first function matches Josie, Ahani, and Mary with their favorite fruit.

![](/img/chapter-1/arrow_diagram_e.svg#center)

Notice that it is easy to match each fruit back to the person who likes it by reversing the diagram for $f$.  This means that $f$ has an inverse function.  

The situation is different with the second function which pairs the same people with their Italian dream car.

![](/img/chapter-1/arrow_diagram_f.svg#center)

Since both Josie and Ahani prefer Ferrari, we are unable to map Ferrari back to a single person.  Thus, according to our definition, $g$ does not have an inverse.

These examples illustrate the general situation.  Functions only have inverses if each output comes from just one input.  In other words, different inputs always generate different outputs.  The only way for $f(x_1) = f(x_2)$ is for $x_1 = x_2$.  Functions with this property are called **one-to-one** functions.  Only one-to-one functions have inverses.

When a function is defined by a diagram, you can determine if it is one-to-one by inspecting each input-output pair.  If two or more different inputs are paired with the same output, then the function is not one-to-one and does not have an inverse.  This technique can also be used when the function is defined by a table or a list of points.

{{% check %}}
1. Does this diagram represent a function that is one-to-one?
![](/img/chapter-1/arrow_diagram_b.svg#center){{% answer %}}Yes, it is one-to-one.  Each output is created by a different input.{{% /answer %}}
2. Does this diagram represent a function that is one-to-one?
![](/img/chapter-1/arrow_diagram_d.svg#center){{% answer %}}No, it is not one-to-one since salad was chosen by Ann and Chris.{{% /answer %}}
3. Is the function in this table one-to-one?
![](/img/chapter-1/function_table_b.svg#center){{% answer %}}No, it is not one-to-one.  Several outputs are created by more than one input.  For instance, $2$ and $3$ both create the same output of $6$. {{% /answer %}}
4. Are these ordered pairs a one-to-one function?
\[
  f(x) = \left\lbrace \thinspace (\color{red}{2}, \color{blue}{3}), \thinspace(\color{red}{5}, \color{blue}{1}), \thinspace(\color{red}{0}, \color{blue}{-9}) \thinspace \right\rbrace
\] {{% answer %}}Yes, this is one-to-one.{{% /answer %}}
{{% /check %}}


## The Horizontal Line Test
Since different inputs to a one-to-one function always create different outputs, no two points on the graph of a one-to-one function can have the same y-coordinate.  

A quick way to test this is to draw (or imagine drawing) several horizontal lines through the graph.  If the function is one-to-one, then no horizontal line will cross the graph more than once.  This test is called the **horizontal line test** and works exactly like the vertical line test, except in the horizontal direction.{{% sidenote "HLT" %}}One-to-one *functions* must pass both the vertical line test (to be a function) and the horizontal line test (so that it is one-to-one).{{% /sidenote %}}

In each of the figures below there is a **<font color="blue">blue</font>** horizontal line.  Apply the horizontal line test to each function by moving the horizontal line up and down graph.

<iframe scrolling="no" src="https://www.geogebra.org/material/iframe/id/GlrFXVKI/width/250/height/340/border/fafafa/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/false/at/auto" width="250px" height="340px" style="border:0px;"></iframe>

<iframe scrolling="no" src="https://geogebra.org/material/iframe/id/AKIuJidM/width/250/height/340/border/fafafa/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/false/at/auto" width="250px" height="340px" style="border:0px;"></iframe>

{{% check %}}
1.  Is this function one-to-one?
![](/img/chapter-1/HLT_a1.svg#center){{% answer %}}No, it does not pass the horizontal line test, so it is not one-to-one.
![](/img/chapter-1/HLT_a.svg#center){{% /answer %}}
1.  Does this function have an inverse?
![](/img/chapter-1/HLT_c1.svg#center){{% answer %}}Yes, this passes the horizontal line test, so is one-to-one and must have an inverse.![](/img/chapter-1/HLT_c.svg#center){{% /answer %}}
{{% /check %}}


## Use Tables or Diagrams to Find Inverses
Consider again the function that matched Jill, Alicia and Mary with their favorite fruit.  Since it is a one-to-one function, it must have an inverse function.  We can construct the inverse function $f^{-1}$ by reversing the diagram for $f$.

![](/img/chapter-1/arrow_diagram_e.svg#center)

![](/img/chapter-1/arrow_diagram_e_inverse.svg#center)  

In general, if a one-to-one function $f$ is defined by a diagram, a table or a list of ordered pairs, then the inverse function $f^{-1}$ is formed by reversing all the ordered pairs.

{{% check %}}
Find the inverses of the following one-to-one functions.

1. Find the inverse of the one-to-one function given in this diagram.
![](/img/chapter-1/arrow_diagram_b_plain.svg#center){{% answer %}}![](/img/chapter-1/arrow_diagram_b_inverse_plain.svg#center){{% /answer %}}
1. Find the inverse of the function given by this table.
![](/img/chapter-1/function_table_a.svg#center){{% answer %}}![](/img/chapter-1/function_table_a_inverse.svg#center){{% /answer %}}
1. Find the inverse of the function below.
\[
  f(x) = \left\lbrace \thinspace (\color{red}{2}, \color{blue}{3}), \thinspace(\color{red}{5}, \color{blue}{1}), \thinspace(\color{red}{0}, \color{blue}{-9}) \thinspace \right\rbrace
\] {{% answer %}}
\[
  f^{-1}(x) = \left\lbrace \thinspace (\color{blue}{3},\color{red}{2}), \thinspace(\color{blue}{1},\color{red}{5}), \thinspace(\color{blue}{-9},\color{red}{0}) \thinspace \right\rbrace
\] {{% /answer %}}
{{% /check %}}


## Graph the Inverse of a Function
This idea of reversing the ordered pairs to find the inverse can be used to graph inverse functions, even if we don't know their equations.  We can do this by identifying a point $(\color{red}{x}, \color{blue}{y})$ on the graph of $f$ and reversing the coordinates.  The new point $(\color{blue}{y}, \color{red}{x})$ will be on the graph of $f^{-1}$.  

Use the interactive figure below to explore this relationship.  As you move the blue point $\color{blue}{(x, y)}$ on $f$ the inverse point $\color{black}{(y, x)}$ on $f^{-1}$ will be plotted.

{{% geogebra ratio="50%" id_1="2FNukWMoESxNIawO" id_2="ahZnh6T9" id_m="ahZnh6T9" %}}

As you might have noticed, reversing the ordered pairs has the same effect as reflecting the graph across the line $y=x$.  In fact, a quick way to graph an inverse by hand is to locate a few points on the graph of $f$ and reflect them.


## Inverses of Basic Functions
When a function is defined by a single operation, finding the inverse is as simple as finding the inverse operation, if it exists.  This is the case with several of our six basic functions.

### Cube & Cube Root
For instance, since the cube and cube root are opposite operations, the cube and cube root functions are inverses of each other.

![](/img/chapter-1/library_cube.svg#center) ![](/img/chapter-1/library_cube_root.svg#center)

Notice that both functions pass the horizontal line test.

### Square & Square Root
The square function, on the other hand, does not pass the horizontal line test, so it cannot have an inverse.  

![](/img/chapter-1/library_square.svg#center)

At the same time, it certainly would be useful to think of the square and square root functions as inverses.  Perhaps there is a way to work around this?

The solution is to remember that the square and square root are inverse operations only when working with non-negative numbers.  If we restrict the domain and only work with $f(x)=x^{2}$ when $x \geq 0$, then we will have a pair of inverse functions.

![](/img/chapter-1/library_square_restricted.svg#center) ![](/img/chapter-1/library_square_root.svg#center)

{{% check %}}
1. What is the inverse of the identity function $f(x)=x$?
![](/img/chapter-1/library_identity.svg#center){{% answer %}}The identity function does not perform an operation, the output is exactly the same as the input.  As a result, the identity function is its own inverse, $f^{-1}(x)=f(x)=x$.{{% /answer %}}
1. What is the inverse of the reciprocal function$f(x)=\frac{1}{x}$?
![](/img/chapter-1/library_reciprocal.svg#center){{% answer %}}Since the opposite of a reciprocal is a reciprocal, the reciprocal function is also its own inverse: $f^{-1}(x)=f(x)=\frac{1}{x}$.{{% /answer %}}
{{% /check %}}


## Use the Shoes and Socks Method to Find Inverses
You have learned that if a one-to-one function is defined by a diagram, table, or graph, then its inverse can be found by reversing the ordered pairs.  If the function is defined by a single operation, then the inverse is the function that performs the opposite operation.

When functions include several operations there are two methods for finding the inverse, if it exists.  In [Chapter 4](/chapter-4/4.4#learn-the-switch-and-solve-method) you will learn a **switch and solve** method based on the idea of reversing the ordered pairs of a function.

Right now, however, the focus is on a simpler **shoes and socks** method.  This method gets its name from the obvious place.  When getting dressed you put on your socks before putting on your shoes.  To take them off you must reverse the order:  first remove your shoes and then take off your socks.

A great illustration of this method comes from the classic television program *Mr. Rogers' Neighborhood*.{{% marnote %}}![](/img/chapter-1/Mr-Rogers-stamp.jpg) The U.S. Postal Service honored Fred Rogers (1928â€“2003) with a Forever stamp on the 50th anniversary of *Mister Rogers' Neighborhood* in March, 2018.{{% /marnote %}}  At the start of each episode, the late Fred Rogers would walk in singing the song "Won't You Be My Neighbor?"  As he sang he would

1.  Take off his jacket
1.  Put on a sweater
1.  Take off his shoes
1.  Put on sneakers

At the end of each episode he would invert the process and

1. Take off the sneakers
1. Put on his shoes
1. Take off the sweater
1. Put on his jacket

Notice that the two lists contain the inverse actions *in the reverse order*.  That is the key!  If we can identify the order in which a function performs its operations, we should be able to construct its inverse by doing the inverse operations in the reverse order.

As an example, consider the function $f(x)=3x-2$.  Following the standard order of operations, this function first multiplies each input by $3$ and then subtracts $2$.  

The inverse function must do the inverse operations in the reverse order: add $2$ and then divide by $3$.

Now that we have identified the operations that the inverse should do, we construct the equation for $f^{-1}$ by applying each of those operations, in the order listed, to a variable.  The steps are as follows:

|1.| Start with a variable | $x$ |
| ----- | ----- | ----- |
|2.| Add $2$ | \[x+2\] |
|3.| Divide by $3$ | \[\frac{x+2}{3}\] |
|4.| Write as a function | \[f^{-1}(x)=\frac{x+2}{3}\] |

We should also check that $f$ and $f^{-1}$ have the round trip property we have seen earlier.  To do this pick any random number, see where $f$ takes that number, and then check to see if $f^{-1}$ will bring it back.  For instance, if $x=7$ then $f(\color{red}{7})=\color{blue}{19}$ and $f^{-1}(\color{blue}{19})=\color{red}{7}$

![](/img/chapter-1/inverse_equation_a.svg#center)

so the round trip property appears to hold.  It would be good to test this with a few more random values just to make sure.  In [Chapter 4](/chapter-4/4.4#verify-inverse-functions) we will discuss a way to formally verify that it works for any number.

{{% check %}}
Find the inverse of the function $f(x)=\frac{x+1}{4}$. {{% answer %}}The function adds $1$ and then divides by $4$, so the inverse must first multiply by $4$ and then subtract $1$.  The equation would be $f^{-1}(x)=4x-1$.{{% /answer %}}
{{% /check %}}

Now let's use the shoes-and-socks method to find the inverse of $f(x) = 2x^3 + 4$.  We begin by identifying the operations performed by the function, and then invert the list to find the operations of the inverse function.

|| **Operations Performed by the Function** || **Operations Performed by the Inverse** |
| ----- | ----- | ----- | ----- |
| 1.  | Cube | 1. | Subtract $4$ |
| 2. | Multiply by $2$ | 2. | Divide by $2$ |
| 3. | Add $4$ | 3. | Cube root |

Now that we know what the inverse function does, we construct its equation as follows:

|Start with a variable: | $x$ |
| ----- | ----- |
|Subtract $4$: | \[x-4\] |
|Divide by $2$: | \[\frac{x-4}{2}\] |
|Cube root: | $$\sqrt[3]{\frac{x-4}{2}}$$ |
|Write as a function: | $$f^{-1}(x)=\sqrt[3]{\frac{x-4}{2}}$$ |

It's also a good idea to check the round trip property with at least one value, let's see what happens when $x=2$.

![](/img/chapter-1/inverse_equation_b.svg#center)

{{% check %}}
Find the inverse of the function $f(x)=\sqrt[5]{6x+1}$. {{% answer %}}\[f^{-1}(x)=\frac{x^5-1}{6}\] {{% /answer %}}
{{% /check %}}


Let's look at one last example of the shoes-socks method and find the inverse of $f(x) = (x+1)^2$.  We'll list the operations performed by the function and then list what the inverse function should do, just as we have done earlier.

|| **Operations Performed by the Function** || **Operations Performed by the Inverse** |
| ----- | ----- | ----- | ----- |
|  1.  |Add $1$ |  1.  |Square root |
| 2. |Square | 2. |Subtract $1$ |

Then we write the equation for $f^{-1}$.

|Start with a variable: | $x$ |
| ----- | ----- |
|Apply square root: | \[\sqrt{x}\] |
|Subtract $1$: | \[\sqrt{x}-1\] |
|Write as a function: | \[f^{-1}(x)=\sqrt{x}-1\] |

But when we check the round trip property we see that some values, such as $x=-5$, don't work.

![](/img/chapter-1/inverse_equation_c.svg#center)

This is because we have made a critical oversight.  A [graph](/img/chapter-1/graph_(x+1)2.png) of $f(x) = (x+1)^2$ shows that it is *not* a one-to-one function, so it cannot have an inverse unless we **restrict the domain**.  To do this we require the input of the square to be greater than or equal to zero.  In this case, we need $x+1 \geq 0$, which is the same thing as saying $x \geq -1$.  Only when we restrict the domain of $f(x)$ to $x \geq -1$ will the two functions be inverses.  We'll need to keep an eye out for this any time a function, or its potential inverse, includes an even power.


## Interpreting Inverse Functions
Earlier in this section we found that the domain and range of $f$ become the range and domain, respectively, of the inverse function $f^{-1}$.  Not only do the domain and range trade places, but their units of measure do as well.  Keeping track of those units makes it much easier to understand the significance of an inverse function.

For instance, the amount of time $T$ that it takes you to drive to work in minutes is a function of how fast you drive in miles per hour.  In theory, if you know your average speed $S$, then you can predict how long the trip will take.

The inverse function, if it exists, would turn speed into a function that depends on the time.  With the inverse function, knowing the duration of the trip allows you to calculate the average speed. Symbolically, if $T=f(S)$, then $S=f^{-1}(T)$.

With this understanding, the distinction between $f(45)$ and $f^{-1}(45)$ is much more clear.  In this example, $f(45)$ would be the time it takes to drive to work if the average speed is $45$ mph.  On the other hand, $f^{-1}(45)$ would be the speed required so that the trip takes $45$ minutes.

{{% check %}}
The temperature of a potato depends on how long it has been in the oven.  In other words, the temperature in degrees Fahrenheit is a function of time in minutes.

1.  Explain the significance of the inverse function in this instance. {{% answer %}}The inverse function turns time into a function of the temperature.  Given a particular temperature, the inverse function would tell how long the potato has been in the oven.{{% /answer %}}
1.  Describe the difference in meaning between  $f(60)$  and  $f^{-1}(60)$ in this example. {{% answer %}}$f(60)$ is the temperature of the potato after 60 minutes in the oven, while $f^{-1}(60)$ is the time it takes for the potato to reach a temperature of 60 degrees Fahrenheit.{{% /answer %}}
{{% /check %}}


## Looking Ahead
In this section we have seen how to identify when a function has an inverse and discussed techniques for finding and interpreting the inverse.  We have also hinted at the fact that an equation only has a unique solution if the underlying function is one-to-one.  

In the following chapters, every time we learn about a new function we will also check to see if it is one-to-one or not.  If it is, then we will also look for its inverse.  If not, then we will consider restricting its domain and focusing on a smaller piece of the function that does have an inverse.
---
title: "1.6 Measuring How Functions Change"
description: "Where you are headed is often more important than where you are at the moment.  Compare the path taken by Enron with that of Apple."
author: "Nolan Mitchell"
type: page
image: "ipod-1428164_1280.jpg"
draft: false
tags: ["measuring-change", "length-of-interval", "intervals", "delta-notation", "total-change", "percent-change", "relative-change", "average-rate-of-change", "slope", "secant-line", "concavity-and-rates", "rates-that-change", "difference-quotient", "calculus-preview"]
---

{{% imgcap file="/img/chapter-1/ipod-1428164_1280.jpg" title="iPod photo by mikefoster on Pixabay" source="https://pixabay.com/photo-1428164/"%}}

## Introduction
When the stock market opened on Monday, October 22, 2001, stock in Enron (a large Fortune-500 energy company) was trading for about $20 per share.  

At the same time stock in Apple (the electronics manufacturer) could also be purchased for $20.

Without additional information, it would be natural to assume that the state of both companies was the same.  In reality, however, they were headed in opposite directions.

Later that day, the federal government announced they were investigating Enron for accounting irregularities.  Within weeks the company declared bankruptcy and several Enron executives were sent to prison for fraud and conspiracy.

Apple, on the other hand, had an important announcement of their own.  The next day, on October 23, 2001, Apple CEO Steve Jobs unveiled the very first iPod.  It was an iconic success that revolutionized the consumer electronics industry and helped establish Apple as one of the most innovative technology companies in the world.

As we've seen earlier, functions, just like stocks, can increase and decrease in value. Our goal in this section is to develop tools that allow us to measure, compare and categorize functions based on how they change.



## Intervals
In this section we will look at how much a function changes ([total change](#total-change)), how large that change is relative to the starting value ([percent change](#percent-change)), and how quickly that change happens ([average rate of change](#average-rate-of-change)).

But before we can do any of those calculations we have to specify which [interval](../1.1#intervals-of-real-numbers) we are inspecting.  It's important to note that these intervals are subsets of the domain, so they are x-values.  For instance, the interval $[5,9]$ is all real numbers from $x=5$ to $x=9$.

In addition to identifying a specific interval, we might also need to measure how long it is.  The length of an interval from $x=a$ to $x=b$ is given by

| \[\Delta x = b-a\] |
| --- |

The Greek letter "delta" ($\Delta$) is used throughout math and science to indicate change.  So writing $\Delta x$ means "the change in the x-values" and is the length of the interval $[a, b]$.


{{% check %}}
1. Can you write the interval of numbers between $x=-4$ and $x=3$ as $[3,-4]$ ? {{% answer %}}No, interval notation should indicate where the numbers are relative to each other on the number line, so the lowest number should always come first.  The proper way to write this is $[-4,3]${{% /answer %}}
1.  What is the length of the interval $[-2, 5]$? {{% answer %}}\[ \Delta x = 5-(-2) = 7\]  {{% /answer %}}
1.  What is the change in the x-values from $x=4$ to $x=10$? {{% answer %}}\[\begin{align} \Delta x &= 10-4 \newline &= 6 \end{align}\]  {{% /answer %}}
{{% /check %}}


## Total Change
The amount that a function has increased or decreased on an interval is called the **total change** on that interval.  Since this is the change in the y-values, we will often use the shorthand notation $\Delta y$ to represent total change.

To calculate the total change of a function on an interval $[a, b]$ we simply subtract the starting value $f(a)$ from the ending value $f(b)$.

| \[\Delta y = f(b)-f(a)\] |
| --- |

Notice that the total change does not care about what happens in the middle of the interval, it is only the starting and ending values that matter.

Both $\Delta y$ and $\Delta x$ are illustrated in the diagram below.

![](/img/chapter-1/deltaY_deltaX.svg#center)

{{% check %}}
Use the graph of $f(x)$ to answer the questions below.
![](/img/chapter-1/total_change_question_graph.svg#center)


1.  Find $\Delta y$ on the interval $[3, 6]$. {{% answer %}}\[\begin{align} f(b)-f(a)&=f(6)-f(3) \newline &= 4-(-4) \newline &= 8 \end{align}\]  {{% /answer %}}
{{% /check %}}
1.  Find $\Delta y$ on the interval $[-1,  3]$. {{% answer %}}\[\begin{align} f(b)-f(a)&=f(3)-f(-1)\newline &=-4-0 \newline &=-4 \end{align}\]  {{% /answer %}}


## Percent Change
Suppose you're planning a vacation to Hawaii and find that the price of airplane tickets has increased from $\\$400$ to $\\$410$.  While you might be a bit annoyed, a $\\$10$ increase is unlikely to make you cancel your trip.

However, if your favorite cafÃ© raised the price of a cup of coffee from $\\$4$ to $\\$14$, that $\\$10$ increase would almost certainly make you reconsider visiting that cafÃ© ever again.

These two situations feel so different, even though the total increase is $\\$10$ in both cases, because total change doesn't look at the increase in cost relative to the starting price.

To measure the relative change all we need to do is divide the total change by the original value.  This is often called **percent change** and is given by 

|  \[\text{percent change} = \frac{f(b)-f(a)}{f(a)} \] |
| --- |

This formula gives us a decimal which we then interpret as a percentage.  A value such as $0.12$, for instance, should be taken to mean $12\\%$. Additionally, negative values are typically labeled as "decreasing" percentages, so that a value like $-0.08$ would be written as an $8\\% \text{decrease}$.

In the case of the airplane tickets, the total change is $\\$10$ and the original price is $\\$400$, so the percent change is $\frac{\\$10}{\\$400}=0.025$ or $2.5\\%$.

On the other hand, the percent change for the coffee is $\frac{\\$10}{\\$4}=2.5$ which is a relative increase of $250\\%$.

As these examples illustrate, percent change can vary significantly even when the total change is the same. This is why relative change is a useful measure in many real-world scenarios.


{{% check %}}
1.  Suppose the number of scholarships given by a university increased from 125 to 180.  What is the percent change? {{% answer %}}\[ \begin{align}\frac{f(b)-f(a)}{f(a)} \thinspace &= \thinspace \frac{180-125}{125} \newline \thinspace &= \thinspace \frac{55}{125} \newline \thinspace &= \thinspace 0.44\end{align}\] which we interpret as a $44\text{%}$ increase.{{% /answer %}}
1.  The cost per person of sharing a \\$30 pizza between $x$ people is given by the function $f(x) = \frac{30}{x}$.  Find the percent change between sharing the pizza between 3 people instead of 2. {{% answer %}}\[ \begin{align}\frac{f(b)-f(a)}{f(a)} &= \frac{f(3)-f(2)}{f(2)} \newline &= \frac{\frac{30}{3}-\frac{30}{2}}{\frac{30}{2}} \newline &= \frac{10-15}{15} \newline &= \frac{-5}{15} \newline &\approx -0.333 \end{align}\] which we interpret as roughly a $33.3\text{%}$ decrease.{{% /answer %}}
{{% /check %}}


## Average Rate of Change
While percent change helps you see the relative increase or decrease in values, it does not indicate how quickly the change is happening.  

If we think back to our coffee example, imagine if the price increased from $\\$4$ to $\\$14$ over a period of $10$ years rather than overnight, that would be a much less dramatic change.

To measure how rapidly a function changes, we need to average the total change over the length of the interval.  

You are probably already familiar with the basic process of finding averages.  For instance, if you drove a distance of 100 miles in 2 hours then your average speed would be $\frac{100 \text{ miles}}{2 \text{ hours}} = 50 \text{ miles per hour}$. Your actual speed may have varied during the trip but, on average, it was 50 miles per hour.

Similarly, to find the average change of a function, we divide the total change in the function values $\Delta y$ by the corresponding change $\Delta x$ in the input values.

|  \[ \frac{\Delta y}{\Delta x}  = \frac{f(b)-f(a)}{b-a}\]   |
| --- |

Since $\frac{\Delta y}{\Delta x}$ is a ratio, it is called the **average *rate* of change** of a function.  This value describes what will happen to $f(x)$, on average, every time $x$ increases by $1$.

To see how this works let's find the average rate of change of $f(x) = \sqrt{x}$ on the interval $[9, 100]$.  Using the formula above:

\[ \begin{align}
\frac{\Delta y}{\Delta x} &= \frac{\sqrt{100} - \sqrt{9}} {100 - 9} \newline
&= \frac{10-3}{91} \newline
&= \frac{7}{91} \newline
&\approx 0.077
\end{align}\]  

This tells us that from $x=9$ to $x=100$ the function $f(x)=\sqrt x$ increases, on average, by $0.077$ units every time $x$ increases by $1$ unit.

It's useful to know that unless a function is linear, the average rate of change will vary depending on the interval $[a, b]$ chosen.

{{% check %}}
Calculate the average rate of change of $f(x)=\sqrt x$ over the interval $[0,16]$.  {{% answer %}}
\[\begin{align}\frac{\Delta y}{\Delta x} &= \frac{\sqrt{16}-\sqrt{0}}{16-0} \newline &= \frac{4-0}{16} \newline &= \frac{1}{4} \end{align}\]  {{% /answer %}}
{{% /check %}}


## Finding Average Rate of Change Graphically
If the average rate of change formula looks somewhat familiar, there's a good reason for that.  It is nothing more than the classic *slope* formula $m=\frac{y_2-y_1}{x_2-x_1}$ converted to function notation.

The line connecting the points $(a, f(a))$ and $(b, f(b))$ is called a secant line.  

![](/img/chapter-1/secant.svg#center)

When a function is defined by a graph, the average rate of change can always be calculated by finding the slope of the secant line.

{{% check %}}
![](/img/chapter-1/AROC_function_graph.svg#center)

1. Use the graph above to find $\frac{\Delta y}{\Delta x}$ on the interval $[-1,  3]$.{{% answer %}} 
![](/img/chapter-1/AROC_function_graph_answer1.svg#center)
\[\begin{align} \frac{\Delta y}{\Delta x} &= \frac{f(3)-f(-1)}{3-(-1)} \newline &= \frac{2-0}{4} \newline &= \frac{1}{2}\end{align}\]
{{% /answer %}}
1. From the graph, what is $\frac{\Delta y}{\Delta x}$ on the interval $[0, 2]$?{{% answer %}}
![](/img/chapter-1/AROC_function_graph_answer2.svg#center)
\[\begin{align}\frac{\Delta y}{\Delta x} &= \frac{f(2)-f(0)}{2-0} \newline &= \frac{0-1}{2} \newline &= \frac{-1}{2}\end{align}\]

{{% /answer %}}
{{% /check %}}


## Concavity and Rates that Change
When walking, cycling, or driving, you've no doubt sped up, slowed down or maintained a constant speed.  In other words, you've changed your rate of speed. 

Since speed itself is a rate of change, by accelerating (speeding up) or decelerating (slowing down) you are actually changing this rate of change.

Graphically, changes in rates of change are evident when a curve becomes steeper or less steep over an interval.  This connects to the concept of [concavity](../1.3#concavity) which we encountered earlier.

It's important to recognize that this is independent of whether a function is increasing or decreasing.

For instance, an increasing function could grow in three different ways: at a constant rate, at an increasing rate, or at a decreasing rate.  All three options are shown below.  

![](/img/chapter-1/increasing_3.svg#center)

Similarly, functions can decrease at constant, increasing, and decreasing rates.

![](/img/chapter-1/decreasing_3.svg#center)

While analyzing changing rate of change is a topic best studied in calculus, it's not too difficult to recognize situations where rates change or to spot the concavity of a graph.


{{% check %}}
For each of the scenarios below, decide if the rate of change would be increasing, decreasing or constant.
1.  The temperature of a turkey as it roasts in an oven. {{% answer %}}The temperature of the turkey increases at a decreasing rate.  It heats up quickly at first but then warms more slowly as the turkey's temperature approaches the oven's temperature.{{% /answer %}}
1.  The world record in the 100 meter dash over time. {{% answer %}}The world record in the 100-meter dash is decreasing at a decreasing rate. Each new world record is lower than the previous one, but the reductions become smaller and smaller.{{% /answer %}}
1.  The distance traveled by a car on cruise control on a straight highway.  {{% answer %}}The distance traveled is increasing at a constant rate (speed). Since the car is on cruise control its speed is held constant. {{% /answer %}}
1.  The altitude of a space ship as it accelerates away from Earth.  {{% answer %}}Altitude would increase at an increasing rate (speed).  As it gets further from Earth there is less gravity and air resistance resulting in a faster and faster increase in altitude. {{% /answer %}}
1.  The height of a ball dropped off a cliff as it accelerates toward the ground. {{% answer %}}The height decreases at an increasing rate (speed).  Because of the acceleration of gravity, the ball falls faster and faster.{{% /answer %}}
{{% /check %}}


## Difference Quotients
The formulas we have used so far show what happens on a specific interval.  Now we'll introduce a tool that allows us to examine the behavior of a function on any interval, using a more general approach.

The tool that does this is called the **difference quotient**.  The difference quotient $D(x)$ is a function that lets us calculate the average rate of change on a generic interval from $x$ to $x+h$, where $h$ is any positive number.

![](/img/chapter-1/difference_quotient.svg#center)

To see how the difference quotient comes from the average rate of change formula, we substitute $\color{red}{x}$ for $\color{red}{a}$ and $\color{blue}{x+h}$ for $\color{blue}{b}$.  

\[
\begin{align}
\frac{f(\color{blue}{b})-f(\color{red}{a})}{\color{blue}{b}-\color{red}{a}} &= \frac{f(\color{blue}{x+h})-f(\color{red}{x})}{\color{blue}{(x+h)}-\color{red}{x}} \newline \newline
          &= \frac{f(x+h)-f(x)}{h}
\end{align}
\]  

The behavior of $D(x)$ is connected to how the function $f(x)$ changes in two important ways.  First, whether the function is strictly increasing, decreasing or constant on an interval impacts the sign of $D(x)$.

* If $f(x)$ is increasing on an interval, then the difference quotient $D(x)$ is positive on that same interval.
* If $f(x)$ is decreasing on an interval, then the difference quotient $D(x)$ will be negative on that interval.
* If $f(x)$ is constant over an interval, then the difference quotient $D(x)$ is $0$ over that interval.

Secondly, the concavity of the function tells us if $D(x)$ itself is increasing, decreasing or constant.  That is to say,

* If $f(x)$ is concave up on an interval, then $D(x)$ increases over that interval.
* If $f(x)$ is concave down on an interval, then $D(x)$ decreases on that interval.
* On any interval where $f(x)$ is a straight line, $D(x)$ will be constant.

Let's examine a few simple examples.  The function $f(x)=3x+2$ is an increasing linear function, so we expect the difference quotient to be a positive constant value, and it is.

![](/img/chapter-1/difference_quotient_3x+2.svg#center)

It is interesting to note that the value of the difference quotient is exactly the same as the value of the slope of the line.

For our final example, we'll look at the square function $f(x)=x^{2}$.  We know that this function is concave up over its entire domain of all real numbers, so we expect its difference quotient will always be increasing. 

![](/img/chapter-1/difference_quotient_x_squared.svg)

Notice that no matter what value $h$ happens to be, $D(x)$ is always increasing since it is a linear function with a slope of $2$.


## Looking Ahead
Exploring how functions change is a fascinating topic and is foundational to calculus.  Not only will calculus teach you more about efficiently computing *average* rates of change, you will also learn to use the difference quotient to calculate *instantaneous* rates change, leading to the powerful concept of a **derivative**.

But for now, it is enough to know that functions with similar behaviors have similar difference quotients, allowing us to group them together into different families that we will encounter in the next chapters.
---
title: "2.1 Power Functions"
description: "A mathematician, like a painter or a poet, is a maker of patterns. If his patterns are more permanent than theirs, it is because they are made with ideas. - G.H. Hardy"
author: "Nolan Mitchell"
type: page
image: "art-artist-brush-102127.jpg"
draft: false
tags: ["power-functions", "exponents", "rules-of-exponents", "negative-exponents", "fractional-exponents", "roots", "symmetry-of-power-functions", "graphing-power-functions", "inverses-of-power-functions", "difference-quotient-of-power-functions"]
---

{{% imgcap file="/img/chapter-2/art-artist-brush-102127.jpg" title="Photo by Daian Gan from Pexels" source="https://www.pexels.com/photo/brush-painting-color-paint-102127/" %}}

## Introduction
Part of the enjoyment of art comes from its patterns of sound and color and motion.  

Patterns are also an essential part of mathematics.  The British mathematician G. H. Hardy once said that *"A mathematician, like a painter or a poet, is a maker of patterns.   If his patterns are more permanent than theirs, it is because they are made with ideas"*.

In this section, we will find an underlying structure that unifies the [six basic functions from Chapter 1](../../chapter-1/1.3#graphs-of-basic-functions) and opens up a new category of functions for our use.


## Power Functions
When working with a group of functions, the first pattern we look for is any similarity in the form, or equation, of the functions.  Once we have identified a pattern, we can create new functions by changing the parameters of that basic equation.  

For instance, these three functions

\begin{align}
    \text{identity function} && f(x) &= x = x^1 \newline
    \text{square function} && f(x) &= x^{2} \newline
    \text{cube function} && f(x) &= x^3 \newline
\end{align}

are all written in the form $f(x)=x^{p}$, where $p$ is the power of the variable $x$.  New functions can be made by taking that basic format and changing the power $p$.  Since the power is the important parameter of the equation, we will call these *power* functions.

In general, a **power function** is any function that can be written as $f(x)=x^{p}$, where $p$ is a constant.  Notice that the variable must be raised to a fixed power.  That power can be positive or negative, a whole number, a fraction or a decimal, but it cannot be a variable.  As an example, $g(x)=3^{x}$ has a variable exponent, so it cannot be a power function even though it looks somewhat similar.

{{% check %}}
Decide if the following are power functions or not.  If it is, identify the value of the power $p$.

1. $f(x)=x^{-2}${{% answer %}}Yes, it is a power function with $p=-2${{% /answer %}}
1. $f(x)=2^{x}${{% answer %}}No, since the variable $x$ is in the exponent, this is not a power function.  Functions like this are exponential functions and will be studied in Chapter 3.{{% /answer %}}
1. $f(x)=x^{1.68}${{% answer %}}Yes, this is a power function with $p=1.68${{% /answer %}}
{{% /check %}}


## Use Rules of Exponents to Identify Power Functions
We now know that the identity, square and cube are all power functions, but what about the other basic functions from Chapter 1?  At first glance, these functions

$$
\begin{align}
    \text{reciprocal function} && f(x) &= \frac{1}{x} \newline
    \text{square root function} && f(x) &= \sqrt{x} \newline
    \text{cube root function} && f(x) &= \sqrt[3]{x}
\end{align}
$$

 do not appear to be power functions since they are not written in the form $f(x)=x^{p}$.

However, any function that *can* be written as $f(x)=x^{ p}$ is a power function, even if it is often written in a different format.  A brief review of a few rules of exponents will show that these three functions are indeed power functions.

### Negative Powers
You might recall the rule $\frac{1}{x}=x^{-1}$.  This tells us that the *reciprocal function* $f(x) = \frac{1}{x}$  is the same as the power function $f(x) =  x^{-1}$.  The general rule of exponents at work here is

\begin{equation}
  \frac{1}{x^{n}}=x^{-n}
\end{equation}

This rule can be used to convert any reciprocal-type function into a power function.  For instance, $f(x)=\frac{1}{x^{5}}$ can be rewritten in the standard power function format as $f(x)=x^{-5}$.

{{% check %}}
Rewrite the following functions in the standard power function form.

1. $f(x)=\frac{1}{x^{2}}${{% answer %}}$f(x)=x^{-2}${{% /answer %}}
1. $f(x)=\frac{1}{x^{4.11}}${{% answer %}}$f(x)=x^{-4.11}${{% /answer %}}
{{% /check %}}

### Roots
Another rule of exponents allows us to rewrite roots as fractional powers.  Specifically,

$$
  \sqrt[m]{x}  =  x^{1/m}
$$

From this we see that the *square root* function $f(x)=\sqrt{x}$ and the *cube root* function $f(x)=\sqrt[3]{x}$ can be written as power functions where the powers are $1/2$ and $1/3$, respectively.

\begin{equation}
  f(x)=\sqrt{{x}}  =  x^{1/2}
\end{equation}

and

$$
  f(x) = \sqrt[3]{x}  =  x^{1/3}
$$

Other roots can be rewritten as power functions in the same way.  For instance, $f(x)=\sqrt[8]{x}   =  x^{1/8}$.

{{% check %}}
Rewrite the following functions in the standard power function form.

1. $f(x)=\sqrt[5]{x}${{% answer %}}$f(x)=x^{1/5}${{% /answer %}}
1. $f(x)=\sqrt[4]{x}${{% answer %}}$f(x)=x^{1/4}${{% /answer %}}
{{% /check %}}

### Fractional Powers
The family of power functions also includes roots of powers, such as $f(x)=\sqrt[m]{x^{n}}$ , or powers of roots like $f(x)=(\sqrt[m]{x})^{n}$, which happen to be the same thing.  These can be rewritten as power functions where the power is a rational number, or fraction, of the form $p=n/m$, such as $-3/8$ or $2/5$.  

$$
  \sqrt[m]{ x^n }  =  \left(\sqrt[m]{x}\right)^{n}  =  x^{n/m}
$$

Since all three forms are equivalent, you may be asked to convert one into the others.  The power function $f(x)  = x^{2/5 }$, for instance, can also be written as  $f(x) =  \sqrt[5]{x^{2}}$ or as $f(x) =  (\sqrt[5]{x})^2$.
{{% check %}}
Rewrite the following functions in the other two formats.

1. $f(x)=\sqrt{ x^3 }$ {{% answer %}}$f(x)=x^{3/2} =  (\sqrt{ x } )^{3}${{% /answer %}}
1. $f(x)=(\sqrt[4]{x})^{7}$ {{% answer %}}$f(x)=x^{7/4}  =  \sqrt[4]{ x^{7}  }${{% /answer %}}
1. $f(x)=x^{2/9}$ {{% answer %}}$f(x)=\sqrt[9]{ x^{2}} =  (\sqrt[9]{ x } )^{2}${{% /answer %}}
{{% /check %}}


## Evaluating Power functions
When using a calculator to evaluate and graph power functions, we need to be careful to wrap $x$ and/or $p$ in parentheses anytime either one is anything other than a whole number. For example, if $f(x)=x^{2/5}$ then to evaluate $f(-3/8)$  parentheses should be put around both $-3/8$ and around the power $2/5$.

| **Correct evaluation of $(-3/8)^{2/5}$** | **Incorrect evaluation of $(-3/8)^{2/5}$** |
| --- | --- |
| `(-3/8)^(2/5) = 0.675480019` | `-3/8^2/5 = -0.009375` |

We should also keep in mind that many power functions are not defined when $x<0$, and that if the power is negative then $0$ is not in the domain.  Expressions involving either of these will produce an error message on your calculator.

{{% check %}}
Use a calculator to find the following values of the function $f(x) =  x^{-1/2}$.

1. $f(4)$  {{% answer %}}$0.5${{% /answer %}}
1. $f(-6.1)$ {{% answer %}}Undefined{{% /answer %}}
1. $f(0)$  {{% answer %}}Undefined{{% /answer %}}
{{% /check %}}


## Graphs of Power Functions
While technology can be used to graph power functions, you can often create a "good enough" sketch within seconds just by examining the equation.  The shape of the graph of a power function $f(x)=x^{ p}$ is controlled by the value of the power $p$.  In this interactive figure you can use the **<font color="blue">blue</font>** slider to change $p$.   

Since many powers are undefined when $x< 0$, we will focus on the first quadrant for now.   As you change $p$, look for patterns or similarities between the different graphs.  In particular, try to group the graphs into *three* distinct shapes.

{{% geogebra ratio="40%" id_1="dgA6tdTPklWA1ewn" id_2="FyjpfmvA" id_m="FyjpfmvA" %}}

As you may have noticed, all power functions pass through the point $(1,\ 1)$, though they do so in three different ways depending on the power $p$.  The three behavior patterns are separated from one another by $p=0$ (when we get the horizontal line $y=1$) and $p=1$ (when we get the identity function $y=x$).

![](/img/chapter-2/powers_all_3.svg#center)

In Chapter 1 you learned how to identify several characteristics of a function by reading its graph.  Since understanding the properties of these three shapes will impact your ability to use power functions effectively, our next goal is to analyze each of these shapes individually.   

### Case 1: $\color{red}{p<0}$
Let's start with the case where the power is negative, that is $p<0$.  Notice that this graph resembles the right side of the [reciprocal function](//chapter-1/1.3#the-reciprocal-function).  

![](/img/chapter-2/power_a.svg#center)

Looking at the graph we see that it drops sharply along the y-axis and levels off toward the positive x-axis, as you move from left to right.  In mathematical terms, the graph is both decreasing and concave up on the interval $(0, \infty)$, with a vertical asymptote at $x=0$ (the y-axis) and a horizontal asymptote at $y=0$ (the x-axis).  

Because of the asymptotes, the graph never reaches a minimum or a maximum value.  Based on the shape of the graph, it would be reasonable to use this type of power function to represent quantities that decay as $x$ increases.

### Case 2: $\color{green}{0<p<1}$
If the power is small, that is $0<p<1$, then the graph of the power function $f(x)=x^{p}$ is increasing and concave down over the interval $(0, \infty)$.   Note that this shape resembles the [square root function](//chapter-1/1.3#the-square-root-function).  

![](/img/chapter-2/power_b.svg#center)

The graph has a minimum value at $(0, 0)$, but does not have a maximum or any asymptotes.  Since the graph is concave down, the rate of increase is decreasing, suggesting that this type of power function might model quantities whose growth is slowing down.


### Case 3: $\color{blue}{p>1}$
When $p>1$, the power function $f(x)=x^{p}$ increases and is concave up on the interval $(0, \infty)$.   This graph resembles the right side of the [square function](//chapter-1/1.3#the-square-function).  

![](/img/chapter-2/power_c.svg#center)

There is a minimum value at the origin $(0, 0)$, but no maximums or asymptotes.  These functions will be useful when modeling quantities that grow faster and faster.  Lastly, note that this graph, along with the two previous ones, is one-to-one and must have an inverse.  


## Symmetry of Power Functions
So far, we have restricted our attention to power functions with $x \geq 0$ because many powers are not defined when $x<0$.   

In particular, if the power is a reduced fraction $p =\color{blue}{n}/\color{green}{m}$ and the denominator $\color{green}{m}$ is even, then the function is not defined when $x<0$. The reason for this is that fractional powers with even denominators are even roots, and even roots of negatives are not real numbers.

However, if the denominator $\color{green}{m}$ is odd then the function is defined for negative values of $x$. You can explore this in the interactive figure below.

{{% geogebra ratio="40%" id_1="nkn0x5386gxHgm4s" id_2="lUgvcybm" id_m="lUgvcybm" %}}

Notice for an odd denominator $\color{green}{m}$, the function exhibits even symmetry when the numerator $\color{blue}{n}$ is even and odd symmetry when the numerator $\color{blue}{n}$ is odd.

So a quick look at the power helps us know where the function is defined and what type of symmetry it has.

{{% check %}}
Which of the following are defined when $x<0$?

1. $f(x) =  x^{7/5}$ {{% answer %}}Yes, since the denominator $5$ is odd, this function is defined when $x<0$.{{% /answer %}}
1. $f(x) =  x^{-3/2}$ {{% answer %}}No, since the denominator $2$ is even, this function is not defined for $x<0$.{{% /answer %}}
1. $f(x) =  x^{8/4}$ {{% answer %}}Yes, since the power $8/4$ simplifies to $2/1$, the denominator is $1$ and the function is defined when $x<0$.{{% /answer %}}

Describe the symmetry, if any, of each function without referring to a graph.

1. $f(x) =  x^{5/3}$ {{% answer %}}This function has odd symmetry.{{% /answer %}}
1. $f(x) =  x^{-6/5}$ {{% answer %}}This function has even symmetry.{{% /answer %}}
1. $f(x) =  x^{3/4}$ {{% answer %}}Since the denominator is not an odd number, this function is not defined for $x<0$, so it does not have any symmetry.{{% /answer %}}
{{% /check %}}


## Use Symmetry to Graph Power Functions
Knowing how the values of $\color{blue}{n}$ and $\color{green}{m}$ impact the symmetry of $f(x)=x^{p}$ with $p = \color{blue}{n} / \color{green}{m}$ also allows us to quickly sketch the graph of a power function.   

Consider, for instance, $f(x) =  x^{\color{blue}{2}/\color{green}{3}}$.  The power $p =\color{blue}{2}/\color{green}{3}$ is between $0$ and $1$, so the graph of this function looks similar to the basic shape for $0<p<1$, which resembles the square root function.  The denominator $\color{green}{3}$ is an odd number, which tells us that this function has a left side.  And since the numerator $\color{blue}{2}$ is even, we should reflect the right side across the y-axis to create a graph with even symmetry.  Thus, the graph of $f(x) =  x^{2/3}$ looks something like this:

![](/img/chapter-2/power_2_3.svg#center)

If the numerator had been odd, such as $f(x) =  x^{5/3}$ then we would have reflected around the origin instead, ending up with this rough sketch:

![](/img/chapter-2/power_5_3.svg#center)

Notice that the shape of the right side of $f(x) =  x^{5/3}$ is similar to the right side of the square function, since $5/3>1$.

In summary, to sketch the graph of a power function with a rational exponent, first choose the basic shape that matches the power $p$.  

![](/img/chapter-2/power_functions.svg#center)

Then use the symmetry rules to draw the other half of the graph, if it exists.

* If the denominator $\color{green}{m}$ is odd, then the function also exists when $x<0$ so it has a left side.
* When $\color{green}{m}$ is odd, the function has even symmetry if $\color{blue}{n}$ is even and odd symmetry if $\color{blue}{n}$ is odd.  

{{% check %}}
1.  Make rough sketch of the function $f(x)=x^{8/3}$. {{% answer %}}![](/img/chapter-2/power_check_c.svg){{% /answer %}}
1.  Make a sketch of the function $f(x)=x^{-3/5}$. {{% answer %}}![](/img/chapter-2/power_check_b.svg){{% /answer %}}
1.  Draw a graph of the function $f(x)=x^{-2/7}$. {{% answer %}}![](/img/chapter-2/power_check_a.svg){{% /answer %}}
{{% /check %}}


## Inverses of Power Functions
Finding the inverse of a power function is a very straightforward process.  As an illustration, consider the cube function $f(x) =  x^{3}$ and its inverse, the cube root function $f^{-1}(x) =  \sqrt[3]{x}$.

Since the cube root can be written as the one-third power $x^{1/3}$, the inverse of $f(x)=x^{3}$ is the power function $f^{-1}(x)=x^{1/3}$.  

Notice that the two powers are *reciprocals* of each other, that is the key.

In general, the inverse of any power function is the power function whose power is the reciprocal of the other.  

![](/img/chapter-1/reciprocal_power.png#center)

That is to say, given some power function $f(x)=x^{p}$, then its inverse is always $f^{-1}(x)=x^{1/p}$, assuming $p\neq 0$.

Of course, if the function is not one-to-one (like in the case of $f(x)=x^2$), then we should restrict ourselves to a portion of the domain (usually $x \geq 0$) where the function is one-to-one.

{{% check %}}
Find the inverse of the following power functions.

1. $f(x) =  x^5$ {{% answer %}}$f^{-1}(x) =  x^{1/5}${{% /answer %}}
1. $f(x) =  x^{7/4}$ {{% answer %}}$f^{-1}(x) =  x^{4/7}${{% /answer %}}
1. $f(x) =  x^{-3/5}$ {{% answer %}}$f^{-1}(x) =  x^{-5/3}${{% /answer %}}
1. $f(x) =  x^{2.3}$ {{% answer %}}$f^{-1}(x) =  x^{1/2.3}${{% /answer %}}
{{% /check %}}


## How Power Functions Change
Our last task for this section is to see if we can find any patterns in the way power functions change.  

You will recall that the difference quotient $D(x)$ is a function that lets us calculate the average rate of change on a generic interval $[x, x+h]$, where $h$ is any positive number.  The difference quotient of a function is given by

\begin{equation}
  D(x)=\frac{f(x+h)-f(x)}{h}
\end{equation}

Below are the difference quotients for the power functions $f(x)=x^2$ and $f(x)=x^3$.

| **Function** | **Difference quotient $D(x)$** | **Power function similar to $D(x)$** |
| ----- | ----- | ----- |
| $x^{2}$ | $2\color{black}{\boldsymbol{x}}+h$</br>[(see steps)](/img/chapter-1/difference_quotient_x_squared.svg) | $\color{black}{\boldsymbol{x^1}}$ |
| $x^3$ | $3\color{black}{\boldsymbol{x^2}}+3xh+h^2$</br>[(see steps)](/img/chapter-1/difference_quotient_x_cubed.svg) | $\color{black}{\boldsymbol{x^{2}}}$ |

*Click the link under each difference quotient to see the steps required to arrive at the equation.*

Notice that the difference quotient of each power function is similar to the next smaller power function.  In general, the difference quotient of $f(x)=x^p$ will involve the power function $f(x)=x^{p-1}$ for any $p\neq0$.  This is a fact that is verified in the first term of calculus.  


## Looking Ahead
In this section we discovered that the basic library functions could all be written in an identical algebraic form.  We then used that common form to create a new category of functions, whose properties we explored.   This is a process that will be repeated in later chapters as well.  We'll start with functions we understand and then create new functions that have slightly different algebraic forms and investigate their properties.

An understanding of the properties and behaviors of functions is essential when working with applications, which is where we will head next.
---
title: "2.2 Applications of Power Functions"
description: "I deduced that the forces which keep the planets in their orbs must be reciprocally as the squares of their distances from the centers about which they revolve. -Isaac Newton"
author: "Nolan Mitchell"
type: page
image: "Apollo_15_trimmed.jpg"
draft: false
tags: ["power-function-applications", "standard-power-function-model", "scaling-factor", "hull-speed", "pendulums", "period", "falling-bodies", "galileo", "apollo-15", "direct-variation", "inverse-variation", "variation", "proportionality", "constant-of-variation", "keplers-third-law", "stopping-distance", "newtons-law-of-gravity", "combining-variation"]
---

{{% imgcap file="/img/chapter-2/Apollo_15_trimmed.png" title="Apollo 15" source="https://spaceflight.nasa.gov/gallery/images/apollo/apollo15/html/as15-88-11866.html" %}}


## Introduction
In 1687 Isaac Newton published *Principia*, one of the most important books in the history of science. {{% sidenote "note about braces" %}} ![](/img/chapter-2/Prinicipia-title.png)<br> A rare first edition copy of *Principia* sold at auction for $3.7 million in 2016.{{% /sidenote %}} In *Principia* Newton formulated his three laws of motion, expanded Kepler's work on planetary orbits, laid the foundations for classical mechanics and, for the first time ever, gave a mathematical description of gravity.

Newton wrote that the gravitational force between two objects is *"proportional to the product of their masses and inversely proportional to the square of the distance between them"*.

In this section we'll spend time trying to figure out what Newton meant by that and uncover a few other applications of power functions along the way.  


## The Standard Power Function Model
Most power function applications require us to scale the basic form $f(x)=x^{p}$ by a factor of $k$.  The resulting equation

\[
  f(x) =  k x^{p}
\]

is called the **standard power function model**.  

To understand how $k$ impacts the model let's focus on the effect it has on a single point.

{{% geogebra ratio="33.33%" id_1="7EOvipXoNUqjGren" id_2="enm1qAJj" id_m="enm1qAJj" %}}

This causes a vertical scaling of the graph by a factor of $k$ so that any power functions of the form $f(x)=k x^{p}$ will pass through the point$(1, k)$.

In many cases the scaling factor $k$ is composed of more than one constant. For instance, the volume of a sphere is a function of the radius and is given by $V=\frac{4}{3} \pi r^{3}$. Here the constant $k$ includes both the fraction $\frac{4}{3}$ and $\pi$, that is $k=\frac{4}{3} \pi$.

{{% check %}}
Identify the scaling factor $k$ for each of the power functions listed below.

1. $f(x)=52(10)^{6}  x^{-2}$ {{% answer %}}$k=52(10)^{6}${{% /answer %}}
1. $f(x)=\frac{1}{\sqrt{2 \pi}} x^{0.84}$ {{% answer %}}$k=\frac{1}{\sqrt{2 \pi}}${{% /answer %}}
1. $f(x)=\frac{x^{1/2}}{364}$ {{% answer %}}$k=\frac{1}{364}${{% /answer %}}
{{% /check %}}


## Applications of Power Functions
Frequently we will find that the only difference between applications is the value of the scaling constant $k$ and, of course, the context. The next three examples illustrate this fact. All three are completely different applications, yet each one is modeled by $f(x)=kx^{1/2}$ for differing values of $k$.

The goal here is not to master the applications, but simply to become familiar with the terminology and maybe even begin to appreciate the usefulness of power functions.  All you will be asked to do at this point is evaluate the functions.


### Tugboats
{{% imgcap file="/img/chapter-2/6566018279_2e151a187c_o.jpg" title="Photo by James Abbot on Flickr" source="https://flic.kr/p/b1dytH" %}}

Light, fast boats are often designed to skim, or *plane*, across the surface of the water.  However, when a large, heavy boat moves it must push the water out of its way.  This creates a wave at the bow (front) of the boat.  As it tries to go faster and faster the wave gets bigger and bigger.{{% sidenote "tug" %}}<iframe src="https://www.youtube.com/embed/1Tj4xvAp_8I?start=166&mute=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe>{{% /sidenote %}}  

When the length of this wave matches the length of the boat, then the boat has reached its *hull speed* $V$, which is generally considered to be the fastest it can go.  The hull speed of a large ship doesn't depend at all on the size of its motor(s) or how heavy it is.  Hull speed is only a function of the ship's length and is given by

\[
  V=1.34 L^{1/2}
\]

where $V$ is the hull speed in knots and $L$ is the length of the boat at the water line in feet.

One surprising aspect of this model is that it not only works for large boats, but for waterfowl like ducks and geese since they make bow waves too.{{% sidenote "duck" %}}![](/img/chapter-2/mallard-3820927_1280.jpg)<br>[Photo by Capri23auto from Pixabay](https://pixabay.com/images/id-3820927/){{% /sidenote %}}  If a duck has a length of 1.25 feet at the water line, then its predicted top speed swimming is

\[
  V=1.34(1.25)^{1/2}\approx 1.5 \text{knots}
\]

{{% check %}}
The Crowley Marine Invader class tugboat *Hunter* has won the Seattle Maritime Festival's tugboat race every year that it has competed since 1995.  If the *Hunter* is 136 feet long at the water line, what is its hull speed? {{% answer %}}$V=1.34(136)^{1/2}\approx15.63 $knots{{% /answer %}}
{{% /check %}}


### Pendulums
A pendulum is an object that swings from a fixed point.  A playground swing and a grandfather clock are two examples of pendulums.  In one tower of the Oregon Convention Center, the 900 pound *Principia* pendulum hangs from a 70 foot long cable as it swings.{{% sidenote "pendulum" %}}<iframe width="100%" src="https://www.youtube.com/embed/6oYvffE6iGY?mute=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>{{% /sidenote %}}   

Surprisingly, the amount of time that it takes a pendulum to swing back and forth once (called its period) doesn't depend at all on how heavy it is.  The period of a pendulum depends only on the length of the cable and is given by

\[
  P=1.11 \thinspace L^{1/2}
\]

where $P$ is the period in seconds and $L$ is the length of the pendulum in feet.  

{{% marnote "clocks" %}}![](/img/chapter-2/clocks.jpg)[Photo by Lisa Brideau on Flickr](https://www.flickr.com/photos/lisabrideau/40606329161/){{% /marnote %}}
Pendulums in grandfather clocks are often 39 inches long.  Since 39 inches is 3.25 feet, this gives them a period of

\[
  P=1.11\thinspace  (3.25)^{1/2}\approx 2.00 \text{ seconds}
\]

If the entire period is 2 seconds, then each swing to the left or to the right lasts almost exactly 1 second, just what a clockmaker would want.

{{% check %}}
Suppose the swings at a local park are 12 feet long.  How long will it take to swing back and forth once? {{% answer %}}$P=1.11 (12)^{1/2}\approx 3.85$ seconds.{{% /answer %}}
{{% /check %}}


### Falling Bodies
{{% imgcap file="/img/chapter-2/pisa-1247452_1280.jpg" title="Photo by Monika Neumann on Pixabay" source="https://pixabay.com/images/id-1247452/" %}}
Italian scientist Galileo Galilei is reported to have dropped two spheres of different masses from the top of the Leaning Tower of Pisa and observed that both hit the ground at the same time.  He concluded that the time it takes an object to fall is independent of its mass.  In other words,  if air resistance is removed, a light object, like a feather, will fall just as fast as a heavy object, like a hammer.  

On Earth, the time it takes an object to fall, ignoring air resistance, is given by

\[
  t=0.25 d^{1/2}
\]

where $t$ is time in seconds and $d$ is the distance in feet.  This was famously verified on the Moon by the astronauts of Apollo 15 in 1971, who captured the event on video.{{% sidenote "galileo" %}}<iframe width="100%" src="https://www.youtube.com/embed//4mTsrRZEMwA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>{{% /sidenote %}}

In 1930, Chicago Cubs' baseball player Gabby Hartnett caught a baseball that had been dropped 800 feet out of a blimp before a pre-season game in Los Angeles.  Ignoring air resistance, the ball would have fallen for
\[
  t=0.25(800)^{1/2}\approx 7 \text{ seconds}
\]

According to reports, the blimp tossed out another ball which he caught as well.  The baseball reached a top speed of about 95 miles per hour.

{{% check %}}
Suppose you drop a 10 pound bowling ball off the top of a 36 foot building.  Ignoring the effects of air resistance, how long will it take to reach the ground? {{% answer %}}Since falling time is independent of mass, we ignore the fact that this is a 10 pound ball and focus only on the distance.  From the equation above, $t=0.25(36)^{1/2}=1.5$ seconds.{{% /answer %}}
{{% /check %}}


## Direct Variation
Many applications, especially in science and engineering, are expressed in the language of variation.  Our focus here is on the vocabulary and converting between verbal and symbolic descriptions.  Solving equations is left for the next section.  

Two quantities $x$ and $y$ are said to **vary directly**{{% sidenote "variation" %}}Variation is sometimes called **proportionality**.  The phrase "$y$ **varies directly** with $x$" means the same as "$y$ is **directly proportional** to $x$".{{% /sidenote %}} if $y$ is a constant *multiple* of $x$.  Algebraically this means that

\[
  y =  k \thinspace x
\]

for any constant $k$.  

In a variation problem the number $k$ is called the **constant of variation**.  Whenever $x$ increases by $1$ then $y$ will increase by $k$.  

While we normally think of $x$ and $y$ as single variables, they could also be algebraic expressions.  For instance, Kepler's third law describes a directly proportional relationship between a square and a cube.  It states that the square of the time it takes a planet to orbit the Sun (called its period) varies directly with the cube of its distance from the Sun.  The equation is $P^2 =  k \thinspace D^{3}$.

In this case the two quantities that are proportional are $P^2$ and $D^{3}$.  

Of particular interest to us are equations of the form $y =  k \thinspace x^{p}$, where $y$ varies directly with the $p$-th power of $x$.  Note that this is nothing more than our standard power function model with a different name.  

Recall, for instance, that the volume of a sphere is given by the power function $V=\frac{4}{3} \pi r^{3}$ where $r$ is the radius.  Using the terminology of variation, we can also say that volume is proportional to the cube of the radius, with a constant of variation of $\frac{4}{3} \pi$.

{{% check %}}
Describe each of the following power functions using the terminology of proportionality and identify the constant of proportionality.

1. $y =  5 x^{3/4}$ {{% answer %}}$y$ is proportional to $x^{3/4}$ with a constant of proportionality of $5$.{{% /answer %}}
1. $y=13.71 \sqrt{x}$ {{% answer %}}$y$ is directly proportional to the square root of $x$ (or to the $1/2$ power).  The constant of proportionality is $13.71${{% /answer %}}
{{% /check %}}


## Inverse Variation
When $y =  k x^{p}$ and the power is negative, there is another phrase that is used to describe the relationship between $x$ and $y$.  If

\[
  y =  k \thinspace x^{-n}  =  k \frac{1}{x^{n}} , n>0
\]

then $y$ varies **inversely** with $x^n$.  Notice that being inversely proportional to $x^n$ is the same as being directly proportional to $x^{-n}=\frac{1}{x^{n}}$.  For example, if  $y =  4 x^{-3}$, then $y$ is inversely proportional to $x^{3}$.  

If two quantities vary inversely, then one increases when the other decreases, and vice versa.  This is in contrast to direct variation where both quantities increase, or decrease, at the same time.  

Two quick examples should illustrate the difference.  When cooking rice, the amount of water needed is *directly* proportional to the amount of rice.  If you want to cook more rice, you'll need more water. However, the time it takes to drive a car around a race track is *inversely* proportional to the speed of the car.  The faster the car travels, the less time it will take to do a lap.

{{% check %}}
Decide if the quantities listed are directly or inversely proportional to one another.

1. The number of people working and the time it takes to dig a ditch. {{% answer %}}You would expect the time to decrease as the number of workers increases, so these would be *inversely* proportional.{{% /answer %}}
1. The amount of yarn needed to knit a sweater and the size of the sweater. {{% answer %}}The two quantities are *directly* proportional, since a larger sweater will need more yarn.{{% /answer %}}
1. The number of air conditioners sold and the daily high temperature. {{% answer %}}When temperatures increase, there is more demand for air conditioners, so the two are *directly* proportional.{{% /answer %}}
1. The fuel efficiency of a car and the speed it is traveling. {{% answer %}}Driving fast causes poor gas mileage, so fuel efficiency and speed are *inversely* proportional.{{% /answer %}}
{{% /check %}}


### Boyle's Law
One example of inverse variation is Boyle's Law.  According to Boyle's Law, if the temperature of a gas in a sealed container is held constant, then the volume of the gas is inversely proportional to the pressure applied.  Algebraically this means that

\[
  P=k \thinspace V^{-1}
\]

where $P$ is pressure, $V$ is volume, and the constant $k$ depends on the initial condition of the gas.

To see why this might be useful, suppose that a medical syringe contains $0.1$ cubic centimeter of air when it is closed and that $k=0.103$ kilogram-centimeters.  Then the pressure in the syringe is

\[
  P=0.103(0.1)^{-1}=1.03 \text{ kilograms per square centimeter}
\]

If the plunger of the syringe is pulled back, increasing the volume to $5.0$ cubic centimeters, then the pressure drops to

\[
  P=0.103(5.0)^{-1}=0.0206 \text{ kilograms per square centimeter}
\]

It is this drop in pressure that causes the suction needed to draw a sample of blood.


## Combining Direct and Inverse Variation
Direct and inverse variation are frequently combined together.  Here we will examine a few examples and translate the descriptions into equations.


### Stopping Distance
{{% imgcap file="/img/chapter-2/street-2369616_1280.jpg" title="Photo by Hannes215 on Pixabay" source="https://pixabay.com/images/id-2369616/" %}}

Physics shows that the stopping distance $d$ of a car is directly proportional to the square of its speed $v$ and inversely proportional to the friction $\mu$ between the tires and the road. If $v$ is measured in miles per hour and $d$ in feet, then 

\[
  d =  \frac{0.0334 v^2 }{\mu}
\]

It is interesting to note that the size and weight of the vehicle are not part of the equation.   More importantly, from a safety standpoint, is the fact that doubling the speed $v$ results in a quadrupling of the stopping distance $d$.

Suppose you are driving $60$ mph down a snowy road and suddenly slam on the brakes.  When will you come to a complete stop?  We now know the equation, but before we can use it we need the friction coefficient $\mu$.  Finding the exact value of the friction coefficient is difficult, but traffic engineers have calculated approximate values for different surfaces. {{% sidenote "stopping" %}}![](/img/chapter-2/friction_coefficients.svg){{% /sidenote %}}

In this case we will use $\mu =  0.2$, since the car is on snow. Substituting these values into our equation gives a stopping distance of

\[
  d =  \frac{0.0334(60)^{2}}{0.2}  \approx 601 \text{ feet}
\]

So if you were traveling at 60mph down a snow covered road, it would take about 601 feet for your car to stop once you had applied the brakes.

{{% check %}}
Suppose you were driving under the same conditions at a much safer speed of $30$ mph.  What would the stopping distance be? {{% answer %}}With $\mu=0.2$ and $v=30$ mph, we have \[ d =  \frac{0.0334(30)^2}{0.2}  \approx  150.3 \text{ feet} \] {{% /answer %}}
{{% /check %}}


### Newton's Universal Law of Gravity
As a final example let's now turn our attention to Newton's law of gravity.  Isaac Newton discovered that the force of gravity $F$ between two objects, like the Sun and the Earth, is proportional to the product of their two masses, $m_1$ and $m_2$, and inversely proportional to the square of the distance $d$ between them.  

![](/img/chapter-2/gravity.svg#center)

In equation format, we have

\[
  F =  k \frac{m_1 m_2 }{d^{2}}
\]

As a random fact, the units of $F$ are called "Newtons", in his honor.  One Newton is roughly equal to the weight of an apple, about 1/4 of a pound.

{{% check %}}
Write an equation that matches each situation described below.

1. The intensity of a sound is inversely proportional to the square of the distance. {{% answer %}}$I =  k \frac{1}{d^{2}}$. Your choice of letters may vary, but the form of the equation should be the same.{{% /answer %}}
1. The thrust of a propeller is proportional to the square of the speed with which it rotates times the 4th power of its diameter. {{% answer %}}$T =  k s^{2} d^{4}$.  Your choice of letters may vary, but the form of the equation should be the same.{{% /answer %}}
{{% /check %}}


## Finding the Constant of Variation
Occasionally, it will be necessary to find the constant of variation.  Whether dealing with direct or inverse variation, the process is basically the same:  insert two known values into the equation and solve for $k$.

For instance, if $y$ varies directly with $x$ and $y=72$ when $x=12$, then we can find $k$ by solving $72=k\cdot12$ by dividing both sides by $12$ to get $k=6$. With this in hand, other values of $y$ can be calculated using the direct variation equation $y=6x$. 

As another example, suppose $y$ varies inversely with $x$ and that $y=3$ when $x=14$. Then $3=\frac{k}{14}$ and, after multiplying by $14$, we find that $k=42$.  So the inverse relationship between $x$ and $y$ is $y=\frac{42}{x}$.  

{{% check %}}
It seems reasonable that the amount of paint needed to paint a wall is directly proportional to the surface area of the wall, since a larger wall requires more paint.  If it takes $5$ quarts to paint $600$ square feet, what is the constant of variation?{{% answer %}}If we let $y$ be the number of quarts of paint and $x$ be the square footage of the wall, then $y=kx$ since they are directly proportional.  

Substituting $y=5$ and $x=600$ we can solve $5=k\cdot 600$ to get $k=\frac{1}{120}$.{{% /answer %}}
{{% /check %}}


## Looking Ahead
In this section we were given equations that represented real life scenarios and were able to evaluate them.  In the next section we will solve these equations for different parameters, and in the section after that we will create our own models.
---
title: "2.3 Equations Involving Power Functions"
description: "To the skydiver, flying in a plane is akin to swimming in a boat; they live for the wind whipping past as they plummet toward the earth during free fall. -Ray Bangs & Chris Becker"
author: "Nolan Mitchell"
type: page
image: "skydive.jpg"
draft: false
tags: ["solving-power-equations", "variation", "proportionality", "isolating-variables", "reciprocal-powers", "terminal-velocity", "skydiving", "drag-force", "friction-coefficient", "solving-for-parameters", "formulas", "real-world-applications"]
---

{{% imgcap file="/img/chapter-2/skydive.jpg" title="Photo from the US Air Force on Flickr" source="https://flic.kr/p/cecNKQ"%}}

## Introduction
Do skydivers fall at a constant speed or do they go faster and faster the longer they fall?  Is there anything they can do to control their speed or is it completely out of their hands?

After we spend a moment outlining the basic solving process for power functions, we will return to these questions.


## Techniques for Solving Power Equations
Since most equations involving power functions will be of the form $y =  k x^{p}$, the steps for solving all of them are essentially the same. First we  make sure that $x^{p}$ is isolated.  Once that has been done, we can solve for $x$ by taking the reciprocal power $1/p$ of both sides of the equation.  In general it would look like this:

\[
	\begin{align}
		y &=   k x^{p} \newline
		\frac{y}{k} &=   x^{p} && \text{Divide both sides by }k \newline
		x &=   \left( \frac{y}{k} \right)^{1/p} && \text{Apply the } 1/p \text{ power to both sides}
	\end{align}
\]

Thus, the solution to $y =  k x^{p}$ is given by $x =   \left( \frac{y}{k} \right)^{1/p}$.  This assumes, of course, that $p \neq 0$.  

Also keep in mind that if $\frac{y}{k}<0$, then $x =   \left( \frac{y}{k} \right)^{1/p}$ may not be a real number and the equation would have "no real number solutions".  

Let's consider one concrete example.  Suppose we need to solve $80 =  5 x^{2}$.  The solving steps will be to first divide by $5$ and then apply the $1/2$ power.

\[
	\begin{align}
		80 &= 5 x^{2} \newline
		16 &= x^{2} && \text{Divide both sides by 5.}\newline
		x &= \pm (16)^{1/2} && \text{Apply the 1/2 power to both sides.} \newline
		x &= \pm 4 && \text{Simplify.}
	\end{align}
\]

In this case there are two $x$ values that solve the equation.  Anytime $p$ is even we might have multiple solutions.  And while only positive solutions have significance for many applications, we should not dismiss negative solutions without good cause.  

{{% check %}}
Use the process above to solve the following equations for $x$, if possible.  Do not simplify your answers.

1. $5 =  7 x^{3}$ {{% answer %}}$x =  \left(\frac{5}{7}\right)^{1/3}${{% /answer %}}
1. $36 =  -6 \thinspace x^{4/5}$ {{% answer %}}$x =  \left(\frac{36}{-6}\right)^{5/4}$ which is not a real number, so this equation has no real number solutions.{{% /answer %}}
{{% /check %}}


## Stopping distance
{{% imgcap file="/img/chapter-2/Police_measure_skidmarks.jpg" title="photo by KOMUnews" source="https://flic.kr/p/yHJev9" %}}

When reconstructing accident scenes, police officers rely on a number of tools, including measuring the length of any skid marks made by the tires.  With that distance, and an assessment of the road conditions, they can approximate the speed of the vehicle.  

So how do they do it? In the prior section we saw how to calculate the stopping distance $d$ using the formula

\[
	d =  \frac{0.0334 v^{2}}{\mu}
\]

where $v$ is the speed of the car in miles per hour and $\mu$ is the friction coefficient of the road surface.

When police need to find the speed of a car that was involved in an accident they measure the distance of the skid marks, make an observation of the road conditions, and solve this equation for $v$.  

Suppose a police investigator finds $286$ foot long skid marks along a snowy road.  How fast was the car going?  To answer this question we insert the known value for $d$ and the estimated $\mu$ from the table {{% sidenote "stopping" %}}![](/img/chapter-2/friction_coefficients.svg){{% /sidenote %}} and solve for $v$.   The result is

\[
	\begin{align}
		286 &=   \frac{0.0334 v^{2}}{0.2} \newline
		1712.575 &=   v^{2} && \text{Divide both sides by } \frac{0.0334}{0.2}=0.167 \newline
		v &=   (1712.575)^{1/2} && \text{Apply the } 1/2 \text{ power to both sides} \newline
		v &\approx\ 41.38 && \text{Evaluate}
	\end{align}
\]

The officer can safely conclude that the car was going around 41.3 miles per hour.

{{% check %}}
If 180 foot long skid marks are found on wet concrete, what was the speed of the car? {{% answer %}}With $d=180$ feet and $\mu=0.6$, we have
\[
	\begin{align}
		180 &=   \frac{0.0334 v^{2}}{0.6} \newline
		3233.53 &=   v^{2} && \text{Divide both sides by } \frac{0.0334}{0.6}=0.05567 \newline
		v &=   (3233.53)^{1/2} && \text{Apply the } 1/2 \text{ power to both sides} \newline
		v &\approx 56.86 && \text{Evaluate}
	\end{align}
\]
So $v \approx 56.86$ mph.
{{% /answer %}}
{{% /check %}}

It is easy to see that the police might need to repeat this process on a regular basis.  To simplify the work needed, it makes sense to create a formula by solving the equation for $v$ without inserting values for $d$ and $\mu$.  Assuming $v>0$, the result is

\[
	\begin{align}
		d &=  \frac{0.0334 v^{2}}{\mu} \newline
		\mu d &= 0.0334 v^2 && \text{Multiply both sides by } \mu \newline
		\frac{\mu d}{0.0334} &=  v^2 && \text{Divide both sides by } 0.0334 \newline
		v &=  \left(\frac{\mu d}{0.0334}\right)^{1/2} && \text{Apply the } 1/2 \text{ power to both sides}
	\end{align}
\]

This formula will give the same results as solving, but is more efficient and less prone to error.  In general, when a calculation needs to be repeated frequently, it's best to find a formula rather than repeating the solving process over and over.

{{% check %}}
Use the formula above find the speed of a car that left 180 foot long skid marks on wet concrete, which has a friction coefficient of $\mu=0.6$.  How do your results compare with the QUICK CHECK above? {{% answer %}}With $d=180$ feet and $\mu=0.6$, we have $v=\left(\frac{(0.6) \cdot (180)}{0.0334}\right)^{1/2} \approx 56.86$ which is the same result obtained by solving in the prior QUICK CHECK.{{% /answer %}}
{{% /check %}}


## Terminal Velocity
{{% imgcap file="/img/chapter-2/skydive.jpg" title="Skydiving photo from the US Air Force on Flickr" source="https://flic.kr/p/cecNKQ"%}}

The force of aerodynamic drag $D$ acting on a skydiver is directly proportional to four parameters: the square of the velocity $v$, the density of air $\rho$, the drag coefficient $C$, and the amount of surface area $A$ that is facing the ground, with a constant of proportionality of $1/2$.  Translating the statement above, we obtain the equation

\[
	D =  \frac{1}{2} C \rho A v^2
\]

From this information, is it possible to find a formula for velocity?


Solving for $v$ gives the following formula:

\[
	v =  \left(\frac{2 D}{ \rho C A}\right)^{1/2} =  \sqrt{\frac{2D}{\rho C A}}
\]

Of the four values ($D$, $\rho$, $C$ and $A$)  that determine velocity, a skydiver has little control over $D$ and $\rho$.  The drag force $D$ can never be greater than the skydiver's weight, otherwise they would float instead of fall, and the density of air $\rho$ at lower altitudes is fairly consistent at about $1.1  kg/m^{3}$.

A skydiver can, however, alter their shape which will affect both surface area $A$ and the drag coefficient $C$. {{%marnote "drag_coefficient"%}}![](/img/chapter-2/drag_coefficient.svg#center){{% /marnote %}}   

For example, suppose a skydiver weighing $734$ Newtons (about 165 lbs) goes into a head-first dive.  How fast might they fall?

In this instance we know $D=734$ and $\rho=1.1$, but we'll have to make some assumptions for $A$ and $C$.

Assuming a stable head down position, a surface area of about $A=0.3 \thinspace m^{2}$ is reasonable, and let's choose a value for $C$ that is a little lower than that of a cylinder, say $C=0.7$.  

With these values in place, we can evaluate $v$.

\[
	v =  \sqrt{\frac{2D}{\rho C A}} =  \sqrt{\frac{(2)(734)}{(1.1)(0.7)(0.3)}} \approx\ 79.7 \thinspace m/s
\]

Our model predicts that the maximum speed (sometimes called *terminal velocity*) of this skydiver in a stable head-first dive is $79.7 \thinspace  m/s$, or around $178 \thinspace mph$.

{{% check %}}
Imagine that our skydiver changes to a flat position so that their surface area is $A=0.6  m^{2}$ and $C$ increases to $1.0$.  What is the maximum speed under these conditions?
{{% answer %}}With $A=0.6$, $C=1.0$ and $D$ and $\rho$ as before, velocity is calculated as \[ v =   \sqrt{\frac{(2)(734)}{(1.1)(1.0)(0.6)}} \approx 47.16 \thinspace m/s \]
which is approximately $105.5 \thinspace mph$.
{{% /answer %}}
{{% /check %}}


## Find the Inverse of a Power Function
The steps we have gone through to solve equations are essentially the same steps needed to find the inverse of a power function.  Recall that the inverse of a basic power function $f(x)=x^{p}$ is the power function $f^{-1}(x)=x^{1/p}$ whose power is the reciprocal of the other.

![](/img/chapter-2/reciprocal_power.svg#center)

Of course, this assumes $p \neq 0$ and that we have restricted the domain if $f(x)=x^{p}$ is not one-to-one, such as in the case of $f(x)=x^{2}$.  Finding the inverse of a standard power function model of the form $f(x) =  k x^{p}$ will require the use of the *shoes and socks* method, since it contains two operations.

To find the inverse of $f(x) =  3 x^{1/5}$, for example, we focus on identifying the operations performed by the function and then invert the list to find the operations of the inverse function.

|| **Operations Performed by the Function** || **Operations Performed by the Inverse** |
| --- | --- | --- | --- |
| 1. | Apply the $1/5$ power | 1. |Divide by $3$ |
| 2. | Multiply by $3$ | 2. | Apply the $5/1$ power |

Now that we know what the inverse function does, we construct its equation as follows:

|Start with a variable: | $x$ |
| --- | --- |
| Divide by $3$: | $x/3$ |
| Apply the $5$th power: | $(x/3)^{5}$ |
| Write as a function: | $f^{-1}(x) =  (\frac{x}{3})^{5}$ |

Notice that the inverse function does the opposite operations in the reverse order, which should always be the case.

{{% check %}}
Find the inverse of the following power functions.

1. $f(x) =  2 x^{3}$ {{% answer %}}$f^{-1}(x) =  \left(\frac{x}{2}\right)^{1/3}${{% /answer %}}
1. $f(x) =  \frac{x^{2/5}}{13},  x \geq 0$ {{% answer %}}$f^{-1}(x) =  (13x)^{5/2}${{% /answer %}}
{{% /check %}}


### Hull Speed
{{% imgcap file="/img/chapter-2/6566018279_2e151a187c_o.jpg" title="Photo by James Abbot on Flickr" source="https://flic.kr/p/b1dytH" %}}

One of the applications in [Section 2.2](../2.2#tugboats) allowed us to find the hull speed of a boat using the function

\[
	V = 1.34 L^{1/2}
\]

where $V$ is the hull speed in knots and $L$ is the length of the boat in feet at the water line.  Since $V$ is a function of $L$, the inverse function, if it exists, will make $L$ a function of $V$.  That is to say, if $V=f(L)$, then $L=f^{-1}(V)$.  This means that $f^{-1}$, if we can find it, could be used to figure out how long a boat needs to be in order to achieve a particular hull speed.  

To find the inverse of $V=f(L) = 1.34 L^{1/2}$ we begin by recognizing that this function first uses the $1/2$ power and then multiplies by $1.34$.  The inverse must do the opposite operations in the reverse order: first dividing by $1.34$ and then applying the $2/1=2$ power.  

Now that we know what the inverse function does, we construct its equation as follows:

|Start with a variable: | $V$ |
| --- | --- |
| Divide by $1.34$: | $\frac{V}{1.34}$ |
| Apply the $2$ power: | $\left(\frac{V}{1.34}\right)^{2}$ |
| Write as a function: | $L=f^{-1}(V) =  \left(\frac{V}{1.34}\right)^{2}$ |

Lastly, to ensure that $f^{-1}$ is one-to-one itself we should add the condition that $V\geq0$.    

How might this new function get used?  Suppose the Navy needs to design a new aircraft carrier with a hull speed of at least $V= 33$ knots.  By evaluating $L=f^{-1}(33)$ the engineers could quickly know that the boat should be at least 606.48 feet long.  

Note that the same answer can be found by inserting $V=33$ into the original function and *solving* for $L$.  In other words, evaluating the inverse function is essentially the same as solving the original function.

{{% check %}}
Suppose you want to build a canoe that will have a hull speed of $V = 5$  knots.  How long should it be? {{% answer %}}Using the inverse function we have \[ L=f^{-1}(5)\approx(5/1.34)^{2}\approx 14 \]  The canoe should be at least 14 feet in length at the water line in order to have a hull speed of $5$ knots.{{% /answer %}}
{{% /check %}}


### Dial-up Internet
Let's consider one last example of a power function model and the importance of its inverse.  Due to the increasing availability of high-speed internet, the number of subscribers to AOL's dial-up internet service has been decreasing.{{% sidenote "dial-up"%}}A 2013 study by the Pew Research Center reported that 3% of Americans still use dial-up connections, primarily in rural areas.  Thatâ€™s more than 9.4 million people.{{% /sidenote %}}

![](/img/chapter-2/aol.svg#center)

The number of AOL subscribers (in millions) can be approximated by the power function $S =  f(t) =  16.32 t^{-0.84}$
where $t$ is time in years since 2005.  What is the inverse of this function, and what significance might it have?  

Using the techniques discussed earlier, the inverse function is

\[
	t =  f^{-1}(S) =  \left(\frac{S}{16.32}\right)^{1/-0.84}
\]

This function is useful because it allows us to approximate the time, in years since 2005, when AOL will have $S$ million subscriptions.  

Many companies sell off divisions of their business when that part of the company shrinks.  Suppose, for instance, that AOL plans to sell off their dial-up service once the number of subscribers drops to 1,000,000.  To find out when that would happen we evaluate the inverse function when $S=1$.

\[
	f^{-1}(1) =  \left(\frac{1}{16.32}\right)^{1/-0.84}\ \approx\ 27.78
\]

This suggests that AOL would continue to offer dial-up internet for about 28 years, until the year 2033.  Of course, this assumes that our original model for the number of AOL subscriptions will continue to hold, which is never a sure thing.


## Looking Ahead
In the next section we will discuss how to take data, like the AOL data, and create power function models that fit the data closely.  Those models can then be used to predict important future behavior.
---
title: "3.1 Exponential Functions"
description: 
author: "Nolan Mitchell"
type: page
image: "nci-vol-2230-300.jpg"
draft: false
tags: ["exponential-functions", "exponential-growth", "exponential-decay", "going-viral", "nuclear-reactions", "cell-division", "growth-factor", "decay-factor", "base", "linear-vs-exponential", "evaluating-exponentials", "percent-change", "growth-rate", "difference-quotient-of-exponential-functions", "the-number-e", "eulers-number", "constant-percent-change"]
---

## Introduction
Exponential functions have a type of growth that we have not studied yet, but you have probably seen it before.  Perhaps the best place to start is with an example.  

The images below illustrate three different real world examples of exponential growth.  All three are exactly the same, just in a different context.  

| ![](/img/chapter-3/viral_e.gif)  | ![](/img/chapter-3/nuclear_explosion.gif)| ![](/img/chapter-3/cell_growth_PNNL.gif)|
| --- | --- | --- |
| [Going Viral](../3.1#going-viral) | [Nuclear Reactions](../3.1#nuclear-reactions) | [Cell Division](../3.1#cell-division) |

## Exponential Growth
### Going Viral
![](/img/chapter-3/social.gif#center)

The videos and games on social media sites like YouTube and Facebook can often "go viral" when they experience a rapid increase in popularity.  
Imagine, for instance, that you share a video with two friends and each of them shares it with two new friends.  If that process continues then the number of new people viewing the video would follow the pattern:

\[
  1,  2,  4,  8,  16,  32,  64, \dotsc
\]

Notice that these numbers are doubling.  One doubles to get two, two doubles to get four, four doubles to get eight, and so on.  This type of increase is one example of **exponential growth**.

If the numbers were to consistently triple, for example $1, 3, 9, 27, \dotsc$, or quadruple like $1,\thinspace 4,\thinspace 16,\thinspace 64,\thinspace \dotsc$, that would also be considered exponential growth.


### Nuclear Reactions
![](/img/chapter-3/chain_reaction.png#center)
A nuclear reaction begins when a small particle, called a neutron, crashes into an atom and splits it in half.  When that atom splits it releases more neutrons.  Those neutrons crash into other atoms and cause them to split as well.  

If each atom that splits causes two more atoms to split, then the number of reactions would follow the pattern:

\[
  1,  2,  4,  8,  16,  32,  64, \dotsc
\]

Notice that these numbers are doubling.  One doubles to get two, two doubles to get four, four doubles to get eight, and so on.  This type of increase is one example of **exponential growth**.

If the numbers were to consistently triple, for example $1, 3, 9, 27, \dotsc$ or quadruple like $1,\thinspace 4,\thinspace 16,\thinspace 64,\thinspace \dotsc$, that would also be considered exponential growth.


### Cell Division
![](/img/chapter-3/cell_division.png#center)
All living cells reproduce by cell division.  Once a cell matures, it then splits into two new cells.  These new cells can also split once they mature.  

The number of cells would follow the pattern:

\[
  1,  2,  4,  8,  16,  32,  64, \dotsc
\]

Notice that these numbers are doubling.  One doubles to get two, two doubles to get four, four doubles to get eight, and so on.  This type of increase is one example of **exponential growth**.  

If the numbers were to consistently triple for example $1, 3, 9, 27, \dotsc$, or quadruple like $1,\thinspace 4,\thinspace 16,\thinspace 64,\thinspace \dotsc$, that would also be considered exponential growth.


## Exponential Decay
![](/img/chapter-3/World_Cup_Bracket_Large.gif#center)

In the 2010 FIFA World Cup, teams from 16 countries competed for the world championship of men's soccer.  

In each round, the losing teams were eliminated from the tournament while the winners advanced to the next round.  This process continued until there was only one undefeated champion:  the Spanish national team.   The number of teams in each round followed the pattern:

\[
  16,  8, 4, 2, 1
\]

Notice that these numbers are always halving.  One-half of sixteen is eight, one-half of eight is four, and so on.  This type of  decrease is an example of **exponential decay**.  

If each number was always one-third or one-fifth of the previous number (for example $27, 9, 3, 1\thinspace$ or $\thinspace250, 50, 10, 2$) then that would also be considered exponential decay.  


## Linear vs. Exponential
These examples show us that exponential growth is special because each new value is a *multiple* of the previous one.  Contrast this with linear growth where each new value is the previous value *plus* a constant.  

![](/img/chapter-3/linear_vs_exponential_growth_table.svg#center)

With linear growth, the number you add to move from one value to the next is called the *slope* and is usually represented by the letter $m$.  In exponential growth, the number we multiply by to move from one value to the next is called the **growth factor**.  We will use the letter $b$ to represent the growth factor.

{{% check %}}
1.  Are the values $5,\thinspace 10,\thinspace 15,\thinspace 20, ...$ growing linearly or exponentially? {{% answer %}}Each new value is the previous one *plus* $5$, so this is linear growth.{{% /answer %}}
2.  Are the values $5,\thinspace 25,\thinspace 125,\thinspace 625, ...$ growing linearly or exponentially? {{% answer %}}Each new value is the previous one *times* $5$, so this is exponential growth.{{% /answer %}}
1.  Suppose a list of numbers grows exponentially with a growth factor of $b=3$.  How would you find the next value in the list? {{% answer %}}Each new number would be $3$ times the prior one.{{% /answer %}}
{{% /check %}}

Recall that the only difference between linear growth and linear decay is the sign of the slope.  If $m$ is positive, the line increases, or grows.  But if $m$ is negative, the line decreases, or decays.

In a similar way, the only difference between exponential growth and exponential decay is the value of the growth factor $b$.  Growth occurs when $b$ is large, whereas the function decays if $b$ is small.  Specifically, any growth factor $0<b<1$ will result in exponential decay.

![](/img/chapter-3/linear_vs_exponential__decay_table.svg#center)

If we know for certain that $0<b<1$, then we call $b$ a **decay factor**.  If no value of $b$ is specified, then we will use the term *growth factor* in a generic sense that could include the possibility of growth or decay.

{{% check %}}
Decide if the following tables display exponential growth or decay.  Then state the value of the growth factor.

|  $90$  | $30$ | $10$ | $\frac{10}{3}$ | $\frac{10}{9}$ |
| --- | --- | --- | --- | --- |
{{% answer %}}Each new value is the previous one *multiplied* by $\frac{1}{3}$, so this is exponential decay with a growth factor of $b=\frac{1}{3}$.{{% /answer %}}

|  $\frac{7}{16}$  | $\frac{7}{4}$ | $7$ | $28$ | $112$ |
| --- | --- | --- | --- | --- |
{{% answer %}}Each new value is the previous value *times* $4$, so this is exponential growth with $b=4$.{{% /answer %}}
{{% /check %}}


## Identify Characteristics of Exponential Functions
Now that we can identify exponential growth, it's time to derive the basic equation for an exponential function.

Our first growth examples in this section followed the pattern $1, 2, 4, 8, 16, 32, 64,\dotsc$ where the growth factor is $b=2$ and each new value is twice the previous value.  If we recall that $1=2^0$, then a clear pattern emerges.

![](/img/chapter-3/exponential_growth_2.svg#center)

Using function notation we might write this as $f(x) = 2^{x}$, which is nothing more than the growth factor $b=2$ raised to the power of $x$.  This gives us a clue for how the basic equation of an exponential function should look.

All exponential functions, whether they represent growth or decay, have the same basic form.  The basic form for an exponential function is

\[
  f(x) = b^{x}
\]

The **base** of the function is the growth factor $b$, which can be any positive number.  

We should be careful not to confuse an exponential function $f(x)=b^{x}$ with a power function $f(x)=x^{p}$.  Even though their equations look similar, they are completely different types of functions.  The key difference is that an exponential function has a variable $x$ in the exponent, whereas the exponent of a power function is a fixed constant.

{{% check %}}  
Are any of the following exponential functions?  If so, identify the base $b$ and decide if the function grows or decays as $x$ increases.

1. $f(x)=3^{x}$ {{% answer %}}Yes, this is an exponential function with $b=3$.  Since $b>1$ the function will grow as $x$ increases.{{% /answer %}}
1. $h(t)=t^{2}$ {{% answer %}}No, the variable needs to be in the exponent.  This is actually a power function.{{% /answer %}}
1. $g(x)=(1/5)^{x}$ {{% answer %}}Yes, this is an exponential function with $b=1/5$.  Since $0<b<1$ the value of the function will decay as $x$ increases.{{% /answer %}}
1. $Q(x)=x^{0.2}$ {{% answer %}}No, this is not an exponential function.  It is actually a power function.{{% /answer %}}
1. $P(t)=(-2)^t$ {{% answer %}}No, this is not an exponential function.  The base of an exponential function must be positive.{{% /answer %}}
{{% /check %}}

The shape of the graph of an exponential function is controlled entirely by the value of the base $b$.  In the following figure you can change the value of the base $b$ by moving the **<font color="blue">blue</font>** slider.  As you do so, pay attention to the shape of the graph.  

{{% geogebra ratio="40%" id_1="JHZ4o4QcfJtuK37Y" id_2="t1KIn8Z3" id_m="t1KIn8Z3" %}}

You should specifically check for each of the following behaviors, which were introduced in [Chapter 1](//chapter-1/1.3).

<details><summary>Behaviors</summary>

* Domain includes all $x$ values; the Range is $y>0$.
* All exponential functions have the same **y-intercept** of $y=1$. There are no **x-intercepts** since exponential functions never cross the x-axis.
* If $b > 1$ the function is always **increasing** and represents **exponential growth**.  Larger values of $b$ produce faster growth.  If $0 < b < 1$ the function is always **decreasing** and indicates **exponential decay**.  The decay is greatest when $b$ is close to $0$.  When $b=1$ the function is **constant** and is usually not considered exponential.
* Exponential functions are either always increasing or always decreasing.  They do not have any maximums or minimums.
* Exponential functions are always concave up.
* The x-axis is a horizontal asymptote, but there are no vertical asymptotes.
* Exponential functions do not have odd or even symmetry.
* All exponential functions are one-to-one.  This means that every exponential function must have an inverse, which will be called a **logarithm.**
</details>


## Evaluate Exponential Functions
When we want to evaluate an exponential function we can often take advantage of the rules of exponents.  For instance, if $f(x)=2^{x}$ then

\[
  f(-3/2) =  2^{-3/2} =  \frac{1}{\sqrt{2^{3}}} =  \frac{1}{2\sqrt{2}}
\]

This is an *exact* expression for $f(-3/2)$.  Sometimes it may make sense to use a calculator to find an *approximate* decimal value instead.  In this case, $f(-3/2) \approx 0.3536$.

{{% check %}}
Give exact values for the following.  Use the rules of exponents as needed.

1. $3^{-2}${{% answer %}}$\frac{1}{3^2}=1/9${{% /answer %}}
1. $5^{1/2}${{% answer %}}$\sqrt{5}$ {{% /answer %}}
1. $2^{0}${{% answer %}}$1${{% /answer %}}

Use a calculator to approximate the following:

1. $\left(\frac{1}{2}\right)^{1.6}$ {{% answer %}}![](/img/chapter-3/eval_exp_2.gif){{% /answer %}}
1. $1.5^{\pi}$ {{% answer %}}![](/img/chapter-3/eval_exp_4.gif){{% /answer %}}
1. $\left(1+\frac{0.8}{12}\right)^{(12 \cdot 7)}$ {{% answer %}}![](/img/chapter-3/eval_exp_5.gif){{% /answer %}}
{{% /check %}}


## How Exponential Functions Change
We said earlier that exponential functions $f(x)=b^{x}$ are special because each time $x$ increases by $1$ the value of the function is multiplied by a factor of $b$.  In other words, if $f$ is an exponential function, then

\[
  f(x+1)=b \cdot f(x)
\]

You'll recall that this pattern was the key to identifying exponential growth and decay.

![](/img/chapter-3/exponential_growth_vs_decay_table.svg#center)

This simple property, $f(x+1)=b \cdot f(x)$, is unique to exponential functions and causes them to change in a way that is different than any other type of function.

Consider, for example, the percent change of an exponential function $f$ over the interval $[x,\thinspace x+1]$.

|  Percent change  | \[ \frac{f(x+1)-f(x)}{f(x)} \] | *Percent change formula.* |
| --- | --- | --- |
||\[\frac{b \cdot f(x)-f(x)}{f(x)}\] | *Apply the property $f(x+1)=b \cdot f(x)$.* |
||\[b-1\] | *Cancel the $f(x)$.* |

Since $b$ is constant, $b-1$ is also constant.  This means that the percent change from one value to the next is always constant.  Having a constant percent change is one of the features that distinguishes exponential functions from all other functions.

{{% check %}}
1.  The percent changes for two functions, $f$ and $g$, are shown below.  
![](/img/chapter-3/percent_change_quick_check_b.png)
![](/img/chapter-3/percent_change_quick_check_a.png)<br>
Which one is an exponential function? {{% answer %}}The first function $f$ is exponential because its percent change is constant.  The second function $g$ is likely a power function, since its percent change is decreasing.
{{% /answer %}}
{{% /check %}}


For any exponential function $f(x)=b^{x}$ with a *growth factor* of $b$, the expression $b-1$ is called the **growth rate** of the function and is designated by the letter $r$.  For instance, if $f(x)=1.08^{x}$, where $b=1.08$, then the growth rate is $r=0.08$.

To see why the growth rate is important, let's take a look at the total change of a basic exponential function over the interval $[x, \thinspace x+1]$.

| $\Delta y$| $= f(x+1)-f(x)$ | Total change formula. |
| --- | --- | --- |
||$=b \cdot f(x)-f(x)$ | Apply the property $f(x+1)=b \cdot f(x)$. |
||$=f(x) (b-1)$ | Factor out $f(x)$. |
||$=r \cdot f(x)$ | Substitute $r=b-1$. |

This result indicates that the difference between $f(x)$ and $f(x+1)$ is $r \cdot f(x)$.  In other words, to move from one value to the next you add $r$ times the current function value.  

For instance, if $b=1.08$, then $f(x+1)=f(x) + .08f(x)$, meaning that every time $x$ increases by $1$, the function increases by $8\text{%}$.

{{% check %}}
1.  Suppose $f(x)=1.26^{x}$.  Identify both the growth factor $b$ and the growth rate $r$. {{% answer %}}The growth factor is the base $b=1.26$.  The growth rate is $r=0.26$, meaning that every time $x$ increases by $1$ the function increases by $26\text{%}$.{{% /answer %}}
{{% /check %}}


## Difference Quotients of Exponential Functions
The difference quotient of an exponential function $f(x)=b^{x}$ can be simplified as follows:   

| $D(x)$|$=  \frac{f(x+h)-f(x)}{h}$ | Difference quotient formula. |
| --- | --- | --- |
||$=  \frac{b^{x+h}-b^{x}}{h}$ | Insert $f(x+h)=b^{x+h}$ and $f(x)=b^x$. |
||$=  \frac{b^{x} b^{h}-b^{x}}{h}$  | Rewrite $b^{x+h}$ as $ b^{x} b^{h}$. |
|| $=  b^{x} \left( \frac{b^{h}-1}{h} \right)$ | Factor out $b^{x}$. |

Since $b$ and $h$ are constants, the expression $\frac{b^{h}-1}{h}$ is also a constant.  This means that the difference quotient of any exponential function is always proportional to the function itself.

This is certainly different from what we observed with power functions.  The difference quotient of a power function is related to a power function with a lower degree, not to the function itself.  For instance $x^{3}$ grows at a rate involving $x^{2}$.  Only exponential functions grow at rates proportional to themselves.

Let's consider a specific example.  If $f(x)=10^{x}$ then the difference quotient is

| $D(x)$|$=  b^{x} \left( \frac{b^{h}-1}{h} \right)$ | Use the result from above. |
| --- | --- | --- |
||$=  10^{x} \left( \frac{10^{h}-1}{h} \right)$ | Insert the growth factor $b=10$. |

This shows that no matter which $h>0$ we choose, $D(x)$ will always be a multiple of the original function $f(x)=10^{x}$.  For instance, choosing $h=1$ gives

\[
  D(x) = \left( \frac{10^{1}-1}{1} \right) 10^{x} = 9 \cdot 10^{x}
\]


{{% check %}}
1.  What is the difference quotient of $f(x)=3^{x}$. {{% answer %}}Inserting $b=3$ into the formula above we see that $D(x)=\left(\frac{3^{h}-1}{h}\right) 3^{x}${{% /answer %}}
1.  Evaluate with the difference quotient of $f(x)=3^{x}$ with $h=2$. {{% answer %}}If $h=2$ then $D(x)=\left(\frac{3^{2}-1}{2}\right) 3^{x}=4 \cdot 3^{x}$ </br></br>In other words, the difference quotient is the original function times $4$.{{% /answer %}}
{{% /check %}}


## The Number **e**
Since every exponential function is proportional to its difference quotient, it's possible that there are special cases where the function and the difference quotient are identical. To pinpoint when this might happen, let's reexamine the equation for the difference quotient of $f(x)=b^{x}$.

\[
  D(x) =  \frac{b^{h}-1}{h} b^{x}
\]

Notice that if  $\frac{b^{h}-1}{h}=1$, then $D(x)=b^{x}=f(x)$.    In other words, if we can find values of $b$ and $h$ that make $\frac{b^{h}-1}{h}=1$, then the difference quotient will equal the function.   

Although there are many combinations of $b$ and $h$ that make $\frac{b^{h}-1}{h}=1$, the most important one arises when $h$ is chosen to be a very small, positive number.  In the interactive figure below, we have fixed $h = 0.001$.  Use the slider to adjust the value of $b$ until you find one where $\color{red}{D(x)}=f(x)$.

{{% geogebra ratio="40%" id_1="rCXAt1yGSjNNjcdr" id_2="hl5o7xc8" id_m="hl5o7xc8" %}}

Which value of $b$ works? From the figure it appears that choosing $b$ somewhere around $2.718$ does the trick.   

The true value is an irrational number known as $e$.   Since $e$ is an irrational number, $2.718$ is just an approximation of  it, much like $3.14$ is an approximation of $\pi$.  Before we can find more precise approximations of $e$, we need to define exactly what $e$ is.

The number $e$ was discovered by a Swiss mathematician, Jacob Bernoulli, as he studied interest on loans, an application we will look at in the next section. The name $e$ was given by another Swiss mathematician, Leonard Euler.  

While there are many ways to define $e$, we choose to say that $e$ is the number which causes $\frac{b^h-1}{h}=1$ as $h \rightarrow 0$.  Solving this equation for $b$ will give us a variation of the formula Bernoulli used to discover $e$.

| $\frac{b^h-1}{h} = 1$ | Original equation. |
| --- | --- |
| $b^h-1 = h$ | Multiply both sides by $h$. |
| $b^h = 1+h$ | Add $1$ to both sides. |
| $b = (1+h)^{1/h}$ | Take the $1/h$ power. |

As $h>0$ approaches zero, this expression approaches the number $e$.  That is to say,

\[
  (1+h)^{1/h} \rightarrow e \thinspace \text{  as  } \thinspace h \rightarrow 0
\]

which is equivalent to one of the definitions Euler used.

The fact that $(1+h)^{1/h} \rightarrow e$ as $h \rightarrow 0$ allows us to find more precise approximations of $e$ by simply making $h$ closer to $0$.  

| $h$  | $(1+h)^{1/h}$ |
| --- | --- |
|  $0.01$ |  $2.70481$ |
|  $0.0001$ | $2.71815$ |
|  $0.000001$ |  $2.71828$ |
|  $0.00000001$ | $2.71828$ |

Euler once approximated $e$ out to 18 decimal places as  $2.718281828459045235$, all *by hand*.   You do not need to memorize several digits of $e$, but remembering that $e \approx 2.718$ will give you a good approximation for making rough calculations.  

Today $e$ is considered one of the most important numbers in mathematics and science.   It is used so frequently, that the exponential function with a base of $e$ is often called *the* exponential function, as though no other bases mattered.  You will find that your calculator has a button dedicated to evaluating $e^{x}$ for any real number $x$.  

{{% check %}}
Find the $e^{x}$ button on your calculator and use it to evaluate the following:

1. $e^{2}$ {{% answer %}}![](/img/chapter-3/eval_e_1.gif){{% /answer %}}
1. $e^{-3.4}$ {{% answer %}}![](/img/chapter-3/eval_e_2.gif){{% /answer %}}    
1. $60 e^{-.035(15)}$ {{% answer %}}![](/img/chapter-3/eval_e_3.gif){{% /answer %}}
1. Does $f(x)=e^{x}$ represent exponential growth or decay?  What about $f(x)=e^{-x}$? {{% answer %}}Since $e>1$, it follows that $f(x)=e^{x}$ is an exponential growth function.  However, $0<1/e<1$, so $f(x)=e^{-x}=(1/e)^{x}$ is an exponential decay function.{{% /answer %}}
{{% /check %}}

## Looking Ahead
In the next section we will see several applications of exponential functions, and many of those will involve using the number $e$ as the base of an exponential function.  
---
title: "3.2 Exponential Models and Applications"
description:
author: "Nolan Mitchell"
type: page
image: "hot_cocoa.jpg"
draft: false
tags: ["exponential-models", "growth-factor", "growth-rate", "initial-value", "standard-exponential-model", "half-life", "doubling-time", "periodic-compound-interest", "continuous-compound-interest", "continuous-growth", "unlimited-growth", "newtons-law-of-cooling", "logistic-growth", "carrying-capacity", "moores-law", "tulipmania", "compound-interest", "the-number-e"]
---

{{% imgcap file="/img/chapter-3/hot_cocoa.jpg" title="Hot cocoa photo by Rawpixels on Unsplash" source="https://unsplash.com/photos/UbMl1U1KvvA" %}}

## Introduction

Imagine that you have a delicious mug of creamy, homemade hot cocoa that is, unfortunately, much too hot to drink.  How long should you leave it on your kitchen counter so that it cools but doesn't lose all of its comforting warmth?  

We're not ready to answer that question yet, but it should not surprise you that it has to do with exponential functions!  In this section, we will develop variations of the basic exponential function that are used in applications as varied as radiation therapy, population growth and, of course, the cooling of hot cocoa.

But before we discuss these specific examples, we must first learn how to interpret the base of an exponential function and incorporate a few standard transformations.


## Growth Factor and Growth Rate
You learned in the previous section that the base $b$ of an exponential function $f(x)=b^{x}$ is a growth factor.  For instance,  if $f(x)=1.08^{x}$, then the *growth factor* is $b=1.08$, meaning the function is multiplied by $1.08$ every time $x$ increases by $1$.  

We can also say that each new value of $f(x)=1.08^{x}$ is $8 \text{%}$ larger than the current one.  This second interpretation focuses on the *growth rate* $r=b-1$ rather than the growth factor $b$.  

In real world applications the growth rate is given much more frequently than the growth factor.  For instance, businesses commonly report that sales are up by $3 \text{%}$ or down by $5 \text{%}$, instead of announcing growth factors of $1.03$ or $0.95$.

For this reason, it is often useful to make the substitution $b = 1+r$ and write exponential functions in the form

\[
  f(x)=(1+r)^{x}
\]

Note that growth occurs when $r>0$ and decay occurs if $ -1<r<0$.

{{% check %}}
1.  Suppose $f(x)=2.6^{x}$.  Identify both the growth factor and the growth rate.  {{% answer %}}The growth factor is the base $b=2.6$.  The growth rate is $r=1.6$, meaning that  every time $x$ increases by $1$ the function increases by $160\text{%}$.{{% /answer %}}
1.  Write an exponential function that has a growth rate of  $0.25$.  {{% answer %}}$f(x)=(1+0.25)^{x}$  or $f(x)=1.25^{x}$.{{% /answer %}}
1.  Find an exponential function that decreases by $50\text{%}$ every time $x$ increases by $1$.  {{% answer %}}With $r=-0.5$ we must have $b=-0.5+1=0.5$ and $f(x)=0.5^{x}$.{{% /answer %}}
{{% /check %}}


## Initial Value
Another way to change the basic exponential function $f(x)=b^{x}$ is to apply a vertical stretch.  You might recall that a vertical stretch is caused by multiplying the function by some constant $a$, which has the effect of multiplying each y-value by $a$.  Use the figure below to explore the how exponential functions respond to vertical stretches. Make a note of your observations before continuing.

{{% geogebra ratio="40%" id_1="aMSg0ulYcZkY4Re8" id_2="ZfNEAkbh" id_m="ZfNEAkbh" %}}

You should have noticed that multiplying an exponential function $f(x)=b^{x}$ by a constant $a$ causes the y-intercept to change from $(0, 1)$ to $(0, a)$.  For instance, if $a=4$, then the y-intercept will be $(0, 4)$.  

![](/img/chapter-3/exponential_vertical_stretch.png#center)

This is actually a consequence of the rule of exponents that says $b^{0}=1$, so $f(0)=a \cdot b^{0} = a$ for any valid base.  

{{% check %}}
*Without graphing*, identify the y-intercept of the function $f(x)=59(0.86)^{x}$. {{% answer %}}The y-intercept is $(0, 59)$.{{% /answer %}}
{{% /check %}}

## The Standard Exponential Model
By including a vertical stretch with the exponential form $f(x)=(1+r)^{x}$, we obtain a more general function

\[
  f(x)=a(1+r)^{x}
\]

that starts with an initial value of $a$ and grows (or decays) at a constant rate $r$. We will call this equation the **standard exponential model**.  All other exponential functions are variations of this equation.

{{% check %}}
Write the equation for an exponential function with an initial value of $31$ that grows at a rate of $25 \text{%}$.  {{% answer %}}Using $a=31$ and $r=0.25$, the function is $f(x)=31(1+0.25)^{x}$ or $f(x)=31(1.25)^{x}$.{{% /answer %}}
{{% /check %}}

Let's revisit an earlier example.  In the final stage of the 2010 FIFA World Cup, 16 teams competed for the world championship.  After each round, one-half of the teams were eliminated and eventually Spain emerged as the champion.

![](/img/chapter-3/Spain_World_Cup_2.gif#center)

We now have the tools needed to model this scenario with the standard exponential model $f(x)=a(1+r)^{x}$.  

Since the final stage of the World Cup starts with 16 teams, we know that $a=16$.  And if $50\text{%}$ the teams are eliminated after each round, then $r=-0.5$ and the function

\[
  f(x)=16 (1-0.5)^{x}=16(0.5)^{x}
\]

models the number of teams left after $x$ rounds have been played.

{{% check %}}
1.  Write the equation of an exponential function that starts at $8$ and increases at a rate of $10\text{%}$. {{% answer %}}With $a=8$ and $r=0.1$, the function is $f(x)=8(1+0.1)^{x}=8(1.1)^{x}$.{{% /answer %}}
1.  Write the equation of an exponential function that starts at $8$ and decreases at a rate of $10\text{%}$. {{% answer %}}With $a=8$ and $r=-0.1$, the function is $f(x)=8(1-0.1)^{x}=8(0.9)^{x}$.{{% /answer %}}
{{% /check %}}

## Half-Life
Our first variation of the standard model will enable us to work with applications that involve half lives and doubling times.  

The **half-life** of a function is the amount of time needed for the value to be reduced by half.  Every exponential decay function has a half-life.  

![](/img/chapter-3/half_life.svg#center)

For instance, the exponential decay function in this graph models the value of a sports car.  The initial value of \\$60,000 is cut in half every 3 years, so we would say it has a half-life of 3 years.

To make the standard model fit this situation we must stretch the $50\text{%}$ decay out over a three-year period.  In other words, we must stretch the function horizontally by a factor of $3$.  So we can model the value of this car with the function

\[
  f(x)=60000(1-0.5)^{x/3}
\]

where $a=60000$ is the initial value and $r=-0.5$ is the growth rate.

{{% check %}}
Create an exponential function that starts at $10$ and is cut in half every time $x$ increases by $4$. {{% answer %}}$f(x)=10(1-0.5)^{x/4}$  or $f(x)=10(1/2)^{x/4}$ {{% /answer %}}
{{% /check %}}


## Doubling Time
On the other hand, the **doubling time** of a function is the amount of time needed for the value to double.  Every exponential growth function has a doubling time.

![](/img/chapter-3/doubling_time.svg#center)

Consider, for example, the value of a collectible toy car like the one shown in this graph.  We say that the value of this toy car has a doubling time of 5 years, since its value doubles every 5 years.

To make the standard model fit this situation we must stretch the $100\text{%}$ growth out over a five-year period.  In other words, we need to stretch the function horizontally by a factor of $5$.  This means we can model the value of this toy car with the function

\[
  f(x)=2(1+1.00)^{x/5}
\]

where $a=2$ is the initial value and $r=1.00$ is the growth rate.

{{% check %}}
Create an exponential function that starts at 10 and doubles every time $x$ increases by 4.  
{{% answer %}}$f(x)=10(1+1.00)^{x/4}$ or $f(x)=10(2)^{x/4}${{% /answer%}}
{{% /check %}}


## Recognize Doubling Time and half-life Models
Let's generalize these last two examples.  If an initial quantity $a$ grows exponentially at a rate of $r$ every time $x$ increases by $c$, then that growth can be modeled by an exponential function of the form

\[
  f(x)=a (1+r)^{x/c}
\]

For instance, the function $f(x)=18(1+0.64)^{x/7}$ could model an initial quantity of $18$ that increases by $64\text{%}$ every time $x$ increases by $7$.

{{% check %}}
1.  Write the equation for an exponential function that starts at $20$ and increases by $87\text{%}$ every time $x$ increases by $3$.  {{% answer %}}$f(x)=20(1+0.87)^{x/3}$ or $f(x)=20(1.87)^{x/3}$.{{% /answer %}}
1.  Write the equation for an exponential function that starts at $30$ and decreases by $52\text{%}$ every time $x$ increases by $2$. {{% answer %}}$f(x)=30(1-0.52)^{x/2}$ or $f(x)=30(0.48)^{x/2}$.{{% /answer %}}
{{% /check %}}

This new form $f(x)=a (1+r)^{x/c}$ gives us greater flexibility when modeling realistic scenarios.  Of particular interest is the case when $r=1$, which gives us the **doubling time model**,  and the case where $r=-1/2$, which is called the **half-life model**.

| **Doubling Time Model** | **Half-Life Model** |
| --- | --- |
| $f(x)=a(2)^{x/c}$ | $f(x)=a\left(\frac{1}{2}\right)^{x/c}$ |

{{% check %}}
Identify the half-life of the function $g(t) = 9.2\left(\frac{1}{2}\right)^{t/1.4}$.   Assume $t$ is measured in hours. {{% answer %}}The half-life is $1.4$ hours.{{% /answer %}}
{{% /check %}}

![](/img/chapter-3/Intel_C4004.jpg#center)

As an example, when technology innovator, Intel, produced its first microprocessor in 1971, it contained 2300 transistors.  Intel's founder, Gordon Moore, predicted that the number of transistors on a computer chip would double *every two years*.  His prediction is known as *Moore's law* and can be modeled by

\[
  f(x)=2300(2)^{x/2}
\]

where $x$ is the number of years since 1971.  

In 2011, Intel's *Sandy Bridge* processor had more than 2.2 billion transistors.  How does this compare with Moore's prediction for 2011?  Since 2011 is 40 years after 1971, we evaluate the above function with $x=40$

| Calculator Evaluation of $f(40) = 2300(2)^{40/2}$ |
| --- |
| `2300*2^(40/2) = 2411724800` |

which is very close to the actual value.  When evaluating expressions like this on a calculator, make sure to include parenthesis around the exponent.

{{% check %}}
Intel released the first *Pentium* processor in 1993.  According to Moore's law, how many transistors should it have had? {{% answer %}}1993 is 22 years after 1971.  Using $x=22$ we have
\[ f(22)=2300(2)^{22/2}=4,710,400 \]
On a calculator you should enter </br>&nbsp; `2300*2^(22/2) = 4710400`
</br>The first *Pentium* actually had 3.1 million transistors, somewhat less than what was predicted. {{% /answer %}}
{{% /check %}}


## Periodic Compound Interest
Another variation of the standard model $f(x)=a(1+r)^{x}$ arises from applications in banking and finance.  

An essential concept of investing is taught in the classic movie *Mary Poppins*.  In one scene, Mr. Dawes tries to convince young Michael{{% sidenote "tuppence" %}}![](/img/chapter-3/tuppence.gif#center){{% /sidenote %}} to invest his tuppence (two pennies) in the bank with the following words of wisdom:

*If you invest your tuppence, wisely in the bank <br>
Safe and sound <br>
Soon that tuppence, safely invested in the bank, <br>
Will compound.*

Interest is **compounded** when it is added to the initial account balance, or **principal**.  Once that interest has been added to the principal it starts earning interest as well, compounding the effect.

In the financial world, it is common for interest to be compounded periodically throughout the year, sometimes on a monthly, weekly or even a daily basis.

If interest is compounded $n$ times a year, only a fraction $\frac{r}{n}$ of the annual interest is earned during each of those periods.  If there are $n$ interest periods per year, the number of periods in $t$ years would be $n \cdot t$. With this in mind, we modify the standard exponential model to create a function for working with **periodic compound interest**.

\[
  A(t) = P\left(1 + \frac{r}{n}\right)^{n \cdot t}
\]

where

* $A(t)$  is the account balance after t years
* $P$  is the principal (initial balance)
* $r$  is the annual interest rate (written as a decimal)
* $n$  is the number of compounding periods per year (ie. 12 for monthly, 52 for weekly, 365 for daily, etc.)
* $t$  is time in years

For example, if \\$3000 is invested at 6% compounded monthly for 8 years, the account balance would be

\[
  A(8) =  3000\left(1+\frac{0.06}{12}\right)^{12 \cdot 8}\approx 4842.43
\]

When using a calculator, remember to include parenthesis around the exponent.

{{% check %}}
What is the account balance after 10 years if \\$8500 is invested at 3% compounded weekly?  {{% answer %}}$A(10)=8500\left(1+\frac{0.03}{52}\right)^{52 \cdot 10}\approx  11472.81$ dollars.{{% /answer %}}
{{% /check %}}


## Continuous Compound Interest
It is logical to wonder what might happen if we were to increase the number of compounding periods $n$ over the course of a year.  Let's investigate.  

Suppose you invest $\\$25,000$ at $5\text{%}$ interest for one year.  Using $P=25000$, $r=0.05$ and $t=1$, the accompanying table shows the account balance $A$ for ever increasing values of $n$.

| $n$ | $A(1)=25000 \left(1+\frac{0.05}{n}\right)^{n \cdot1}$ |
| --- | --- |
| 1 | \\$26,250.00 |
| 12 | \\$26,279.05 |
| 52 | \\$26,281.15 |
| 365 | \\$26,281.69 |
| 1,000 | \\$26,281.74 |
| 10,000 | \\$26,281.77 |
| 100,000 | \\$26,281.78 |
| 1,000,000 | \\$26,281.78 |

The table suggests that more frequent compounding does not produce unlimited growth over the course of a year.  For instance, compounding interest 365 times a year (every day) gives a balance of \\$26,281.69, which is only very slightly better than compounding just 12 times a year (every month).

It also appears that no matter how many times we compound interest, the balance never gets above \\$26,281.78.

To explain why more frequent compounding does not produce unlimited wealth, consider what happens to the equation $A(t)=P\left(1+\frac{r}{n}\right)^{n t}$ as $n
\rightarrow \infty$.  If $n$ gets larger, then $\frac{r}{n} \rightarrow 0$.  

In the past we've used the letter $h$ for quantities that get close to zero.  We will follow that convention and make the substitution $h= \frac{r}{n}$.  Note that this implies $n=\frac{r}{h}$.  With these changes we rewrite $A(t)$ as follows:

| $A(t) =P\left(1+\frac{r}{n}\right)^{n t}$ | *Start with the periodic compound interest function.* |
| --- | --- |
| $A(t) = P(1+h)^{\left(\frac{r}{h} \right)t}$ | *Substitute $h= \frac{r}{n}$ and $n = \frac{r}{h}$.* |
| $A(t) = P(1+h)^{\left(\frac{1}{h}\right) r t}$ | *Rewrite $\left(\frac{r}{h}\right) t$ as $\left(\frac{1}{h}\right) r t$.* |
| $ = P\big[(1+h)^{\frac{1}{h}}\big]^{ r t}$ | *Rewrite using the rule of exponents $x^{m n} = (x^m)^{n}$.* |

The expression in brackets $[(1+h)^{1/h}]$ might remind you of something from the previous section.  If $h \rightarrow 0$ then $(1+h)^{1/h} \rightarrow e \approx 2.71828$.  This is the reason for the limit.  Compounding interest more and more frequently makes the base closer and closer to $e$.  The resulting function

\[
  A(t)=P e^{r  \thinspace  t}
\]

is known as the **continuous compound interest formula** and is widely used in finance, business and economics.


## Work with Continuous Growth
{{% imgcap file="/img/chapter-3/nci-vol-2230-300.jpg" title="Photo from the National Cancer Institute" source="https://visualsonline.cancer.gov/retrieve.cfm?imageid=2230&dpi=300&fileformat=jpg" %}}

Aside from compound interest, there are many other quantities that change continuously.  For instance, the number of bacteria in a petri dish does not increase suddenly at the end of a day, week or month.  Rather the population increases continuously at a rate that is proportional to the size of population.  

Similarly, the amount of carbon-14 in an object decays continuously.

When used in different settings such as these, the $A(t)=P e^{ r t}$  formula is often referred to as "continuous growth".  

In general, we will say a quantity that experiences **continuous exponential growth** (or decay) can be modeled by a function of the form

\[
  f(t)=a e^{ k t}
\]

where $a$ is the initial quantity when $x=0$ and $k$ is the continuous rate of growth.

The continuous exponential growth function is often written with different letters to match specific application.  You will need to be able to recognize continuous growth regardless of how the function is written.  For example,

\[
\begin{align}
Q(x) &= Q_0 e^{ k x} \newline
n(t) &= n_0 e^{ r t} \newline
y &= C e^{ r x}
\end{align}
\]

are all continuous growth models.

{{% check %}}
1.  What are the distinguishing features of continuous exponential growth?  {{% answer %}}The base of the exponential function is $e$ and the growth rate is in the exponent along with the variable.{{% /answer %}}
1.  What is the continuous rate of growth (or decay) of the function $f(x)=36e^{-0.03 x}$ ? {{% answer %}}The rate is $k=-0.03$, which indicates a continuous decay of 3%.{{% /answer %}}
{{% /check %}}

## Unlimited Growth
In general, exponential growth cannot be sustained unless there are unlimited resources.   For this reason it is sometimes called **unlimited growth**.  A historic example of this is "tulipmania".

![](/img/chapter-3/tulip_price_index.png#center)

During the 1630's, Holland was crazy for tulips and their value skyrocketed exponentially.  At one point, tulip prices were as much as 20-times higher than they had been just months before.  Some economists estimate that half of all the money in the Dutch economy was wrapped up in the tulip market.  Such a huge exponential rate of growth was not sustainable and soon the tulip market crashed, bankrupting many Dutch citizens.

In the next few examples we look at situations where, instead of exploding, the growth is limited and eventually levels off.  Surprisingly, exponential functions are at the center of those applications as well.


## Newton's Law of Cooling
{{% imgcap file="/img/chapter-3/pexels-photo-905847.jpeg" title="Photo by Eneida Nieves from Pexels" source="https://www.pexels.com/photo/baked-pizza-on-pizza-peel-in-oven-905847/"%}}

Suppose you put a pizza in a 450&deg;F oven.  The temperature of the pizza will increase, but in a limited way since it will never exceed the temperature of the oven.  Isaac Newton studied situations like this and discovered a law that modeled the heating or cooling of an object.  

**Newton's law of cooling** says that rate of temperature change in an object is proportional to the temperature difference between the object and its surroundings.  Based on this, Newton found that the temperature of an object at time $t$ is given by  

\[
  T(t) = S + (T_{0} - S)e^{-k  \thinspace t}
\]

where $S$ is the temperature of the surroundings (or the temperature of the oven, in this case) $T_{0}$ is the initial temperature of the object (or the original temperature of the pizza), and $ k $ is a positive constant that depends on the nature of the object.  

This function models cooling when $T_0 > S $ and heating if $T_0 < S$.  

![](/img/chapter-3/newtons_law.svg#center)

In either case, $y = S$ is a horizontal asymptote.  Also notice that the resulting curves are nothing more than exponential functions that have been reflected and/or shifted vertically.

Let's consider a cooling example.  Suppose you put a 160&deg;F hot cup of cocoa on the counter in a 70&deg;F kitchen.  The cocoa will cool according to Newton's law of cooling as it approaches room temperature.   

{{% imgcap file="/img/chapter-3/hot_cocoa.jpg" title="Hot cocoa photo by Rawpixels on Unsplash" source="https://unsplash.com/photos/UbMl1U1KvvA" %}}

Assuming $k=0.08$, what will be the temperature of the cocoa in 20 minutes?

\[
\begin{align}
T(t) &= S+(T_0-S)e^{-k  \thinspace  t} \newline
&=70 + (160-70)e^{-0.08 \cdot 20} \newline
&=70 + 90e^{-1.6} \newline
&\approx 88.17
\end{align}
\]

We conclude that after 20 minutes the temperature of the cocoa is roughly 88&deg;F.


## Logistic Growth
Our final variation of the standard exponential model has its roots in population growth.

Imagine that a small number of trout are introduced into a large lake.  When the population is small, the amount of food and resources available appears unlimited, and the population grows exponentially.  But as the population increases, resources become more scarce and the growth levels off.

In 1838, Belgian mathematician Pierre-Francois Verhulst created a function that has this very behavior.  His function, now called the **logistic function**, assumes growth is proportional to both the current population size and the available resources.  The equation and graph of a logistic function are given below.  The values $a$, $b$ and $c$ are constants.

![](/img/chapter-3/logistic.svg#center)

The number $c$ is a horizontal asymptote of the function and is often called the **carrying capacity**.  In the trout example, it would represent the maximum number of trout that the lake can support.

{{% check %}}
Suppose the population of trout in a particular mountain lake is modeled by the logistic equation $f(x)=\frac{20000}{1+39e^{-0.2x}}$ where $x$ is the number of years since the lake was first stocked.

1.  Calculate the initial trout population.  {{% answer %}}At time $x=0$ the equation suggests that there were $f(0)=500$ trout.{{% /answer %}}
1.  What is the carrying capacity, or maximum number of trout the lake can support?  {{% answer %}}Since $c=20000$, the carrying capacity is $20000$ trout.{{% /answer %}}
1.  Determine the trout population $10$ years after the lake was stocked.  {{% answer %}}$f(10) = \frac{20000}{1+39 e^{-0.2*10}}\approx 3186$ trout.{{% /answer %}}
{{% /check %}}

## Looking Ahead
In this section we have used transformations to create a wide variety of exponential models.  

| **[Standard model](../3.2#the-standard-exponential-model)** | $f(x)=a(1+r)^{x}$ |
| --- | --- |
| **[half-life](../3.2#half-life)** | $f(x)=a\left(\frac{1}{2}\right)^{x/c}$ |
| **[Doubling Time](../3.2#doubling-time)** | $f(x)=a(2)^{x/c}$ |
| **[Compound Interest](../3.2#periodic-compound-interest)** | $A(t)=P\left(1+\frac{r}{n}\right)^{n \thinspace t}$ |
| **[Continuous Growth](../3.2#work-with-continuous-growth)** | $f(x)=a e^{k\thinspace x}$ |
| **[Newton's Law of Cooling](../3.2#newtons-law-of-cooling)** | $T(t)=S+(T_0-S)e^{-k \thinspace t}$ |
| **[Logistic](../3.2#logistic-growth)** | $f(x)=\frac{c}{1+ae^{-b \thinspace x}}$ |

We will return to these models later when we solve exponential equations.  The main tool for solving exponential equations is called the *logarithm*, and it just happens to be the focus of the next section.
---
title: "3.3 Logarithmic Functions"
description:
author: "Nolan Mitchell"
type: page
image: "371919441_51f06c8fb9_b.jpg"
draft: false
tags: ["logarithmic-functions", "definition-of-logarithms", "inverse-of-exponential", "common-logarithm", "natural-logarithm", "converting-exponential-logarithmic", "evaluating-logarithms", "graphing-logarithms", "logarithmic-scales", "product-rule", "quotient-rule", "power-rule", "properties-of-logarithms", "slide-rules", "tables-of-logarithms", "john-napier", "hp-35-calculator", "difference-quotient-logarithms"]
---

{{% imgcap file="/img/chapter-3/371919441_51f06c8fb9_b.jpg" title="Photo by john allspaw" source="https://flic.kr/p/ySbGa" %}}

## Introduction
Up until the invention of scientific calculators{{% sidenote "HP-35" %}}![HP-35 scientific calculator](/img/chapter-3/4368541979_ec395ea1eb_o.jpg)The HP-35 was the first handheld scientific calculator.  Developed by Hewlett-Packard, it went on sale in 1972 for $395.  [Photo by Julian Bucknall](https://flic.kr/p/7E2Vki){{% /sidenote %}} in the 1970's, people relied on 300-year-old mechanical calculators called "slide rules".

Slide rules use the properties of exponents to simplify calculations.  For example, multiplication turns into addition and division becomes subtraction.

To build a slide rule you need a function that can extract exponents.  Such functions are called *logarithmic* functions and just happen to be the inverses of exponential functions.  In this section we will study logarithms and even learn how to use a simple slide rule.


##  Definition of Logarithms
We learned in a [previous chapter](//chapter-1/1.4) that every one-to-one function has an inverse.  Since the exponential function $b^{x}$ (where $b>0$ and $b\neq1$) is one-to-one, it must have an inverse.

The inverse of the exponential with base $b$ is called the **logarithm** with base $b$ and is written $\log_b (x)$.

![](/img/chapter-3/inverse_exp_log.svg#center)

As with exponential functions, the base $b$ must be a positive number not equal to $1$.

In other words, as long as the base is the same, the functions $b^{x}$ and $\log_b(x)$ are inverses of each other.  

<table>
  <tr>
    <th>Function</th><th>Inverse</th>
  </tr>
  <tr>
    <td>$f(x) =  3^{x}$</td><td>{{% answer %}}$f^{-1}(x) = \log_{3}(x)${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$g(x) =  \log_{4} (x)$</td><td>{{% answer %}}$g^{-1}(x) = 4^{x}${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$h(t)  =  2^t$</td><td>{{% answer %}}$h^{-1}(t) = \log_2(t)${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$q(x) =  \log_{10}(x)$</td><td>{{% answer %}}$q^{-1}(x) = 10^{x}${{% /answer %}}</td>
  </tr>
</table>

{{% check %}}
1. What is the inverse of $f(x) =  7^{x}$? {{% answer %}}$f^{-1}(x) = \log_{7}(x)${{% /answer %}}
1. What is the inverse of $g(x) =  \log_{13} (x)$?  {{% answer %}}$g^{-1}(x) = 13^{x}${{% /answer %}}
{{% /check %}}

## Convert Between Exponential and Logarithmic Equations
Whenever a function has an inverse, we know that $f(x) = y$ if and only if $f^{-1}(y) = x$.   In the present context, this inverse relationship means that $y = b^{x}$ is equivalent to $\log_{b}(y) = x$.

This gives us the ability to rewrite exponential equations as logarithmic equations and/or convert logarithmic equations into exponential equations.{{% sidenote "convert exp to log" %}}To convert between exponential and logarithmic equations it is easiest to first identify the base and then remember that the logarithm equals the  exponent.{{% /sidenote %}}

![](/img/chapter-3/rewrite_exp_log.svg#center)

For example,  the exponential equation $9=3^{2}$ is equivalent to logarithmic equation $\log_{3}(9) = 2$.  

Going the other direction, $\log_{10}(1000)=3$ means the same thing as $1000=10^{3}$.  Here are a few more examples.

<table>
  <tr>
    <th> </th><th>Exponential Equation</th><th>Logarithmic Equation</th>
  </tr>
  <tr>
    <td>a.</td><td>$5^{3}=125$ </td><td>{{% answer %}}$\log_{5}125=3${{% /answer %}}</td>
    </tr>
  <tr>
    <td>b.</td><td>$9^{2}=81$</td><td>{{% answer %}}$\log_{9}81=2${{% /answer %}}</td>
  </tr>
  <tr>
    <td>c.</td><td>$3^{y}=4$</td><td>{{% answer %}}$y=\log_{3}4${{% /answer %}}</td>
  </tr>
  <tr>
    <td>d.</td><td>{{% answer %}}$2^4=16${{% /answer %}}</td><td>$\log_2(16)=4$</td>
  </tr>
  <tr>
    <td>e.</td><td>{{% answer %}}$3^{3}=27${{% /answer %}}</td><td>$\log_3(27)=3$</td>
  </tr>
  <tr>
    <td>f.</td><td>{{% answer %}}$10^5=x${{% /answer %}}</td><td>$\log_{10}(x)=5$</td>
  </tr>
</table>

{{% check %}}
1.  Write a logarithmic equation that is equivalent to $2^{4}=16$.
{{% answer %}}$\log_{2}16=4${{% /answer %}}
1.  Write an exponential equation that is equivalent to $\log_{7}49=2$.
{{% answer %}}$7^2=49${{% /answer %}}
{{% /check %}}


## Evaluate Logarithms
The inverse relationship

\[
  y=b^{x} \Longleftrightarrow \log_{b}(y) = x
\]

can also be used to evaluate logarithms by rewriting known exponential values. To illustrate this point, let's compute a few values of $\log_{2}(x)$ by looking at known values of $2^{x}$.

<table>
  <tr>
    <td>$y=2^{x}  \Longleftrightarrow  \log_{2}(y)=$</td><td>$x$</td>
  </tr>
  <tr>
    <td>$1=2^{0}  \Longleftrightarrow  \log_{2}(1)=$</td><td>{{% answer %}}$0${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$2=2^{1}  \Longleftrightarrow  \log_{2}(2)=$</td><td>{{% answer %}}$1${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$4=2^{2}  \Longleftrightarrow  \log_{2}(4)=$</td><td>{{% answer %}}$2${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$8=2^{3}  \Longleftrightarrow  \log_{2}(8)=$</td><td>{{% answer %}}$3${{% /answer %}}</td>
  </tr>
</table>

Notice that in each instance the logarithm is the exponent.  For example, $\log_{2}(8)=3$ because $3$ is the exponent that makes $2^{x}=8$.  

Of course, logarithmic functions can also be evaluated on a calculator.  Starting with the [HP-35](/img/chapter-3/HP-35_large.jpg) in 1972, two different logarithms have been built into every handheld scientific and graphing calculator: the **common log** and the **natural log**.{{% sidenote "calculator log and ln" %}}The buttons for $\log$ and $\ln$ on different calculators are shown below. ![](/img/chapter-3/calculator_log_and_ln.png)  {{% /sidenote %}}

The common logarithm has a base of $10$.  It is written as $\log$ (lowercase LOG).  The natural logarithm has
a base of $e$.  It is written as $\ln$ (lowercase LN).

{{% check %}}
1.  Use a calculator to evaluate $\log 1000$. {{% answer %}}$\log 1000 = 3$ <br> This is the exponent you would have to put on $10$ to generate $1000$.  You can check your answer by seeing if $10^{3} = 1000$.{{% /answer %}}
2.  Use a calculator to evaluate $\ln 1000$.{{% answer %}}$\ln 1000 \approx 6.90776$ <br>  This is the exponent you would have to put on $e$ to generate $1000$.  You can check your answer by seeing if $e^{6.90776} \approx 1000${{% /answer %}}
{{% /check %}}

## Graph Logarithmic Functions
We can also use the inverse function relationship to sketch graphs of logarithmic functions.  Remember, with inverse function if the point $(x,y)$ is on the graph of $f$ then the point $(y,x)$ is on the graph of $f^{-1}$.

Use the figure below to help you graph $\log_2(x)$.  As you move the **<font  color="blue">blue</font>** point, the pencil will plot its inverse (in **black**).  

{{% geogebra ratio="50%" id_1="TMQcNvcShckVTBRM" id_2="NqdtIjsk" id_m="NqdtIjsk" %}}

You may want to verify that each of the following points is on the appropriate graph.

| **Point on** $f(x)=2^{x}$ | **Point on** $f^{-1}(x)=\log_{2}(x)$ |
| ----- | ----- |
| $(0,1)$ | $(1,0)$ |
| $(1,2)$ | $(2,1)$ |
| $(2,4)$ | $(4,2)$ |
| $(3,8)$ | $(8,3)$ |

Like exponential functions, the shape of the graph of a logarithmic function is controlled entirely by the value of the base $b$.  Each base will have its own, slightly different graph. Use the following interactive figure to change the value of $b$ and analyze the behavior of the function.  

{{% geogebra ratio="33.333%" id_1="mdoZbTnv0jseqoJk" id_2="u2R6RhFZ" id_m="u2R6RhFZ" %}}

Specifically, look for any of the 9 basic function properties.  Click each property to check your observations.
<details><summary>Domain and Range</summary>Domain includes all $x>0$, the Range is all real numbers.</details>
<details><summary>y-intercept</summary>Logarithmic functions never cross the y-axis, so there are no y-intercepts.</details>
<details><summary>x-intercepts</summary>All logarithmic functions have the same x-intercept of $x=1$.</details>
<details><summary>Increasing, Decreasing, Constant</summary>
If $b>1$ the function is always increasing and represents logarithmic growth.  Larger values of $b$ produce slower growth. </br></br>
If $0 < b < 1$ the function is always decreasing and indicates logarithmic decay.  The decay is greatest when $b$ is close to $1$.</br></br>
The function does not exist when $b \leq 0$ or if $b=1$. </details>
<details><summary>Maximums & Minimums</summary>Since logarithmic functions are constantly increasing or decreasing they do not have any maximums or minimums.</details>
<details><summary>Concavity</summary>Concavity depends on the base.  If $b>1$ the graph is concave down.  If $0 < b < 1$ it will be concave up. </details>
<details><summary>Asymptotes</summary>No horizontal asymptotes exist, but the y-axis is a vertical asymptote.</details>
<details><summary>Symmetry</summary>Logarithmic functions do not have odd or even symmetry.</details>
<details><summary>1:1</summary>Yes, all logarithmic functions are 1:1.  The inverse function would be the exponential function with the same base.</details>


## Understand How Logarithmic Functions Change
Every time we define a new function, we need to investigate the way it changes.   Let's start by looking at the average rate of change $\frac{\Delta y}{\Delta x}$ over several intervals.  

For convenience, we will use the common logarithm $\log(x)$ and, to simplify the calculations, we will choose intervals $[a, b]$ that have a width of $\Delta x=1$.  

|Interval | $\frac{\Delta y}{\Delta x} =\frac{f(b)-f(a)}{b-a}=\frac{\log(b)-\log(a)}{b-a}$ |
| --- | --- |
| $[0.001, 1.001]$ | $\frac{\Delta y}{\Delta x}=\frac{\log (1.001)-\log (0.001)}{1.001-0.001}=3.000$ |
| $[1, 2]$ | $\frac{\Delta y}{\Delta x}=\frac{\log 2-\log 1}{2-1}=0.301$ |
| $[2, 3]$ | $\frac{\Delta y}{\Delta x}=\frac{\log 3-\log 2}{3-2}=0.176$ |
| $[3, 4]$ | $\frac{\Delta y}{\Delta x}=\frac{\log 4-\log 3}{4-3}=0.125$ |
| $[50, 51]$ | $\frac{\Delta y}{\Delta x}=\frac{\log 51-\log 50}{51-50}=0.009$ |
| $[100, 101]$ | $\frac{\Delta y}{\Delta x}=\frac{\log 101-\log 100}{101-100}=0.004$ |

What do these values for $\frac{\Delta y}{\Delta x}$ in the table tell us about the common logarithm function?  It appears that $\log(x)$ changes more when $x$ is small than it does when $x$ is large.  In other words, the values of $\log(x)$ are further apart when $x$ is small, and closer together when $x$ is large.  The difference quotient will help us understand why this happens.


## Difference Quotient of Logarithmic Functions
In earlier chapters we saw that the difference quotient of a function, given by $D(x)=\frac{f(x+h)-f(x)}{h}$, is a function that describes how $f$ changes on any interval of length $h>0$.

Unlike power functions and exponential functions, it is very difficult to simplify the difference quotient of a logarithmic function by hand, so we will not attempt that.

However, since $D(x)$ is itself a function, we can take a look at its graph and see if it has any interesting properties.

In the figure below, the graphs of $f(x)=\log_{b}(x)$ and its difference quotient $D(x)$ are shown in <span style="font-weight: bold;color:black;">black</span> and in <span style="font-weight:bold;color:red">red</span>, respectively.   

We have fixed $h=0.001$, but the value of the base $b$ can change, allowing us to view the difference quotient for several different logarithms.  Use the <span style="font-weight:bold;color:blue">blue</span> slider to change the value of $b$ and see if you recognize $D(x)$ as one of the basic functions from [Chapter 1](//chapter-1/1.3#the-reciprocal-function).

{{% geogebra ratio="33.333%" id_1="jsCkMkF0S57kJ8oP" id_2="XWcmkpYg" id_m="XWcmkpYg" %}}

No matter which base is chosen, the graph of $D(x)$ always looks like the reciprocal function $1/x$.  And the fact that $1/x$ is large when $x$ is small but small when $x$ is large confirms our earlier observation that logarithmic functions change rapidly when $x$ is small but that the rate slows down as $x$ increases.  


## Logarithmic Scales
When we plot values for $\log (x)$ on a number line it quickly becomes apparent that they are not evenly spaced.  The smaller values are spread out while the larger values are more compressed.

![](/img/chapter-3/log_scale_a.svg#center)

If we use the logarithms as increments and relabel the axis we end up with something called a **logarithmic scale**.

![](/img/chapter-3/log_scale_b.svg#center)

Logarithmic scales have several applications, some of which will be covered in the next section.  For now, we will use it like a ruler to measure lengths.  In the process, we hope to uncover at least one property of logarithms.


## Product Rule for Logarithms
We now turn our attention to some rather useful properties that deal with combining logarithms through addition and subtraction.  Rather than deriving these properties by rewriting rules of exponents, we will attempt to discover some of them by using the logarithmic scale in this interactive figure.  Keep in mind that since *logarithms are exponents*, we cannot expect the normal rules of addition to work.  

{{% geogebra ratio="45%" id_1="6MkXEHnjxFtTorWV" id_2="iLAuEp1a" id_m="iLAuEp1a" %}}

Start by adding two logarithms.  For instance, find $\log(3) + \log(5)$ by putting both $\log(3) $ and $\log(5)$  end-to-end on the log scale.  Is the answer $\log(8)$ ?    Experiment with other combinations to see if there is a pattern for addition.

Then move on to expressions like $\log(9) - \log(3)$.  Since you are not given a bar for $\log(9)$ you might have to find multiple bars that add up to $\log(9)$ before you subtract $\log(3)$ away from them.

Use a calculator to check your work and make a note of your results before continuing.

Let's look closely at what you might have found from the interactive figure.  This is what it would look like if you placed $\log(3) $ and $\log(5)$  end-to-end on the log scale.

![](/img/chapter-3/log3_plus_log5.png#center)

Notice that the resulting bar lines up with $15$ on the log scale.  We learn from this that $\log(3)+\log(5)=\log(15)$ or,  in other words,

\[
  \log(3)+\log(5)=\log(3 \cdot 5)
\]

If you try this with other values you will find that it is always true.  The pattern is

\[
  \log(x)+\log(y)=\log(x \cdot y)
\]

and is called the **product rule**.

{{% check %}}
1.   Verify the product rule $\log(x)+\log(y)=\log(x \cdot y)$ by evaluating both $\log(18)+\log(2)$ and $\log(18 \cdot 2)$ on your calculator.{{% answer %}}![](/img/chapter-3/log18_plus_log2.gif#center){{% /answer %}}
{{% /check %}}


## Quotient Rule for Logarithms
Since addition always tells us something about subtraction, let's take another look at $\log(3) + \log(5)$.  
![](/img/chapter-3/log3_plus_log5.png#center)
We know that $\log(3)+\log(5)=\log(15)$, but what if we were to remove the $\log(5)$ from the figure above?  The only thing left would be $\log(3)$.   In other words, $\log(15)-\log(5)=\log(3)$.
Since $\frac{15}{5}=3$ the pattern for subtraction is
$\log(x)-\log(y)=\log\left(\frac{x}{y}\right)$
which is known as the **quotient rule**.

{{% check %}}
1.   Verify the pattern $\log(x)-\log(y)=\log\left(\frac{x}{y}\right)$ by evaluating both $\log(27)-\log(13)$ and $\log\left(\frac{27}{13}\right)$ on your calculator.{{% answer %}}![](/img/chapter-3/log27_minus_log13.gif#center){{% /answer %}}
{{% /check %}}


## Power Rule for Logarithms
One of the most useful logarithm properties is called the **power rule**.  Consider what happens when you add $\log(3)$ with another $\log(3)$.

![](/img/chapter-3/power_rule.png#center)

Clearly $\log(3)+\log(3)=\log(9)$.  And since $9=3^2$, this result can also be given as $\log(3)+\log(3)=\log(3^2)$.

But it is also proper to write $\log(3)+\log(3)=2 \cdot \log(3)$, just as we might write $5+5=2*5$.

Putting the two together we see that $\log(3^2)=2 \cdot \log(3)$.   The general pattern is

\[
  \log x^{p}=p \cdot \log(x)
\]

and will be used extensively throughout the rest of this chapter.


## Properties of Logarithms
The properties we discovered are valid for all logarithms, no matter which base is used.  We have listed them below in their general form.  You are encouraged to use a calculator to check the given examples.

| **Identity** | **Formula** | **Example** |
| --- | --- | --- |
| **Product Rule** | \[ \log_b (x \cdot  y) = \log_b (x) + \log_b (y) \] | \[ \ln(20) =  \ln(4) + \ln(5) \] |
| **Quotient Rule** | \[ \log_b \left(\frac{x}{y}\right) =  \log_b (x) - \log_b (y) \] | \[ \ln\left(\frac{10}{2}\right) =  \ln(10) - \ln(2) \] |
| **Power Rule** | \[ \log_b x^{p} =  p \log_b (x) \] | \[ \ln(2^{3}) =  3\ln(2) \] |

{{% check %}}
1. Use the **product rule** to rewrite $\log(7)+\log(3)${{% answer %}}$\log(7)+\log(3)=\log(7 \cdot 3)=\log(21)${{% /answer %}}
1. Use the **quotient rule** to rewrite $\ln(8)-\ln(4)${{% answer %}}$\ln(8)-\ln(4)=\ln\left(\frac{8}{4}\right)=\ln(2)${{% /answer %}}
1. Use the **power rule** to rewrite $\log(3^{x})${{% answer %}}$\log(3^{x})=x*\log(3)${{% /answer %}}
{{% /check %}}

## Logarithms Throughout History
### Tables of Logarithms
When [John Napier](http://upload.wikimedia.org/wikipedia/commons/4/4b/John_Napier_%28Neper%29.jpg) discovered logarithms in 1614, he realized that with these logarithm rules, every operation could be converted to a simpler one.   

The product rule changes multiplication into addition; the quotient rule turns division into subtraction; and the power rule replaces powers with multiplication.

The only tool needed to use these simplifications is a table of logarithmic values.  

To illustrate how to use a table of logarithms, we'll examine a very simple case.  Suppose we wanted to multiply $2$ and $3$.  Rather than doing the multiplication, we look up the two logarithms in the table and calculate their sum:  $\log(2) + \log(3) = 0.301 + 0.477 = 0.778$.

![](/img/chapter-3/log_table.png#center)

Next, we scan through the table until we find $0.778$.  Lastly, we read the table backward to find the $x$ next to $0.778$.  This value, $x = 6$ is the answer to our multiplication problem!

What we just did was a product rule: $\log(2)+\log(3)=\log(2 \cdot 3)$.  And while our example was overly simple, the time saved when working with large numbers is tremendous since adding large numbers by hand is much faster than multiplying them.

{{% check %}}
Explain how you could use the above table and the properties of logarithms to evaluate the following:

1. $4\times2$ {{% answer %}}Using the product rule, $\log(4)+\log(2)=0.602+0.301=0.903$.  From the table we see that $0.903=\log(8)$ so the answer is $4*2=8$.{{% /answer %}}
1. $10\div2$ {{% answer %}}Using the quotient rule, $\log(10)-\log(2)=1.000-0.301=0.699$.  From the table we see that $0.699=\log(5)$ so the answer is $10/2=5$.{{% /answer %}}
1. $3^2$ {{% answer %}}Using the power rule we know $\log(3^2)=2 \cdot \log(3)$.  So we find $\log(3)=0.477$ on the table and double it: $2 \cdot 0.477=0.954$.  Next we look for $0.954$ and read it backward to get $x=9$ as our answer.{{% /answer %}}
{{% /check %}}


### Slide Rules
{{% imgcap file="/img/chapter-3/371919441_51f06c8fb9_b.jpg" title="Photo by john allspaw" source="https://flic.kr/p/ySbGa" %}}

The rules of logarithms sped up calculations even more after the invention of slide rules.  

Slide rules look similar to regular rulers except that the markings are not evenly spaced.  Instead, the distances are proportional to the logarithms of the marked values. In essence, a slide rule is just two logarithmic scales, one placed on top of the other so they can slide back and forth.

Let's see how this works.  Suppose you wanted to multiply $2 \cdot 3$.  The first step is to slide the top scale to the right until the $1$ is above the $2$.  Next move the hairline so that it is over the $3$ on the top scale.  The answer, $6$, will be directly below on the lower scale.

{{% geogebra ratio="33.333%" id_1="5znJBOupbxSj7YbQ" id_2="xHcwR0N3" id_m="xHcwR0N3" %}}

Sliding the upper scale is a physical way to add logarithms and use the product rule.  And while it may not be as precise as a table, it is very quick.  Notice that no extra work is needed to calculate other multiples of $2$ because  all the numbers on the top scale are now lined up with their multiples on bottom scale.

## Looking Ahead
Modern calculators and computers have rendered both logarithm tables and slide rules obsolete.  

However, the properties of logarithms that were developed in this section are valuable tools for solving exponential equations.

We will also return to logarithmic scales, but with a slight twist, at the end of the next section.
---
title: "3.4 Logarithmic Models and Applications"
description:
author: "Nolan Mitchell"
type: page
image: "headphones.jpg"
draft: false
tags: ["logarithmic-models", "logarithmic-scales", "decibel-scale", "sound-intensity", "stellar-magnitude-scale", "apparent-magnitude", "ph-scale", "acidity", "hydrogen-ions", "richter-scale", "earthquakes", "seismograph", "solving-exponential-equations", "cancellation-properties", "change-of-base-formula", "bell-telephone-laboratories", "charles-richter"]
---

{{% imgcap file="/img/chapter-3/headphones.jpg" title="Photo by Matthieu A on Unsplash" source="https://unsplash.com/photos/bXjqPckmLD8" %}}

## Introduction
The human senses are capable of perceiving a wide range of stimuli.  Our sense of hearing, for example, picks up both faint whispers and highly amplified music.

One reason for this is the fact that your ears don't perceive the actual intensity of sound, rather they respond approximately to logarithm of the sound intensity.  For example, if you increase the intensity of a sound 10 times, it will only sound about twice as loud.

In this section we will discuss several applications of logarithms including the decibel scale, which is used to measure the intensity of sound.


## Logarithmic Scales
When measuring quantities that vary greatly, like sound intensity, it's often convenient to work with logarithmic scales.  As we saw earlier, one of the nice features of logarithmic functions is that they expand small values and condense larger ones.  Observe, for instance, the values of $\log(x)$ given in this table.

| $x$ | $\log(x)$ |
| ----- | ----- |
| 0.001 | -3 |
| 0.01 | -2 |
| 0.1 | -1 |
| 1 | 0 |
| 10 | 1 |
| 100 | 2 |
| 1000 | 3 |

Even though each $x$ value increases by a factor of 10, the $\log x$ values only increase by $1$.  By using a logarithmic scale we can view a large range of data values without having to use enormous numbers.

Because of the convenience of a 10-fold increase, most logarithmic scales use $\log$ rather than $\ln$.  This is true of the pH scale, the Richter scale, the stellar magnitude scale and the decibel scale, which we will examine next.


## The Decibel Scale
{{% imgcap file="/img/chapter-3/headphones.jpg" title="Photo by Matthieu A on Unsplash" source="https://unsplash.com/photos/bXjqPckmLD8" %}}
Sounds that cause unbearable pain are about *10 trillion times* more intense than the faintest sounds that can be heard.  With such a wide range, using the actual values is not very convenient.  

Realizing this, engineers at Bell Telephone Laboratories developed the decibel {{% sidenote "decibel" %}}A decibel is one tenth (deci-) of a <b>bel</b>, a unit named after Alexander Graham Bell, and is abbreviated as dB.{{% /sidenote %}} scale in the 1920's to rank the intensity of sounds with respect to the lowest sound level a listener can detect, called the *threshold of hearing*.

To find the decibel level (in dB) of a sound we use the formula

\[
  D = 10\log\left(\frac{I}{I_0}\right)
\]

where $I$ is the intensity of the sound being ranked and $I_0$ is the threshold of hearing, both measured in watts per square meter.  And while hearing ability varies from person to person, it is generally accepted that $I_0=10^{-12}$ watts per square meter.  

As an example, the sound of a typical household vacuum cleaner has an intensity of $10^{-4}$ watts per square meter.  On the decibel scale this would measure
\[
\begin{align}
D &= 10 \log \left( \frac{10^{-4}}{10^{-12}}\right) \newline
&= 10 \log \left(10^8\right) \newline
&= 10 \times 8 \newline
&= 80 \text{ dB}
\end{align}
\]

A few other decibel levels are given below for comparison.

| decibel level | Intensity in watts/m<sup>2</sup> |  |
| :---: | :---: | :--- |
|  $0\text{ dB}$  | $0.000000000001$ | Threshold of Hearing |
| $20\text{ dB}$  | $0.0000000001$ | Whisper |
| $60\text{ dB}$  | $0.000001$  | Normal Conversation |
| $70\text{ dB}$  | $0.00001$  | Busy Street Traffic |
| $90\text{ dB}$  | $0.001$  | Hairdryer |
| $110\text{ dB}$ | $0.1$  | Front Rows of a Rock Concert |
| $130\text{ dB}$ | $10$   | Threshold of Pain |
| $140\text{ dB}$ | $100$   | Instant Perforation of the Eardrum |

{{% check %}}
Some of the quietest dishwashers on the market produce only about $4 \times 10^{-8}$ watts per square meter of sound.  Where would that rank on the decibel scale? {{% answer %}}\[
\begin{align}
D &= 10 \log \left( \frac{4 \times 10^{-8}}{10^{-12}}\right) \newline
&= 10 \log (40000) \newline
&= 10 \times 4.602 \newline
&= 46 \text{ dB}
\end{align}
\]{{% /answer %}}
{{% /check %}}

## The Stellar Magnitude Scale
{{% imgcap file="/img/chapter-3/denis-degioanni-9wH624ALFQA-unsplash.jpg" title="Photo by Denis Degioanni on Unsplash" source="https://https://unsplash.com/photos/9wH624ALFQA" %}}

One of the oldest logarithmic scales is the one used for measuring the brightness of stars.  The human eye responds to changes in brightness in a logarithmic way, so when the ancient Greeks categorized stars by how bright they appeared to the naked eye, they unknowingly created a logarithmic scale.

In 1856, British astronomer Norman Pogson created the following equation for the apparent magnitude $m$ of a star to closely match those more ancient classifications.

\[
  m=-2.5  \log \left(\frac{F}{F_{0}}\right)
\]

In this formula $F$ is the observed flux (ie. brightness) of a star and $F_0$ is a reference flux in the same color.  Flux is usually given in watts per square meter.  Modern astronomers typically use the star Vega as the reference for an apparent magnitude of zero ($m=0$), making it's flux the baseline: $F_0=2.8\times10^{-8}$  watts/m<sup>2</sup> for visible light.

Suppose, for instance, that we wanted to find the apparent magnitude of the Sun, which has a flux of $1340$ watts/m<sup>2</sup>.

\[
  m=-2.5  \log \left( \frac{1340}{2.8\times10^{-8}}\right)\approx-26.7
\]

This number might seem low at first, but remember that the apparent magnitude scale puts the brightest objects low on the scale and the weakest objects at the top.  

{{% check %}}
1.  Sirius is the brightest star in the night sky.  The flux of Sirius is $F=1.1\times10^{-7}$ watts/m<sup>2</sup>.  What is the apparent magnitude of Sirius?   {{% answer %}}\[
\begin{align}
m &= -2.5 \log \left( \frac{1.1 \times 10^{-7}}{2.8\times10^{-8}}\right) \newline
&\approx -1.4856
\end{align}
\]{{% /answer %}}
1.  The full Moon is the brightest object in the night sky.  When full, it's flux is about $0.004$ watts/m<sup>2</sup>.  What is the apparent magnitude of a full moon?   {{% answer %}}\[
\begin{align}
m &= -2.5 \log \left( \frac{0.004}{2.8\times10^{-8}}\right) \newline
&\approx -12.8873
\end{align}
\]{{% /answer %}}
{{% /check %}}


## The pH Scale
In chemistry, the acidity of a substance is measured on a logarithmic scaled called the **pH scale**.  {{% marnote "pH scale" %}}Typical pH values of common substances. ![](/img/chapter-3/PH_Scale.svg){{% /marnote %}}  

To calculate pH we use the formula

\[
  pH=\log \left(\frac{1}{[H^+]}\right)=-\log{[H^+]}
\]

where $[H^+]$ is the concentration of hydrogen ions, measured in moles per liter, found in the substance.  

For example, household bleach has a hydrogen ion concentration of $2.512 \times 10^{-13}$ moles per liter, whereas the concentration in milk is nearly a million times greater at $1.995 \times 10^{-7}$ moles per liter.  Their rankings on the pH scale are

\[
  pH_\text{bleach}=-\log(2.512 \times 10^{-13})\approx12.6
\]

\[
  pH_\text{milk}=-\log(1.995 \times 10^{-7})\approx6.7
\]

{{% check %}}
Lime juice has a hydrogen ion concentration of $[H^+]=0.00631$ moles per liter.  Where does lime juice rank on the pH scale?    {{% answer %}}\[
\begin{align}
pH_\text{lime juice} &= -\log(0.00631) \newline
&\approx2.2
\end{align}
\]{{% /answer %}}
{{% /check %}}


## The Richter Scale
In the early 1930's, Charles Richter was attempting to measure the strength of earthquakes in California.  He soon came to the conclusion that the range between the largest and smallest earthquakes was "unmanageably large".  

At that point a colleague suggested he plot the amplitudes logarithmically.  Even though Richter felt that "logarithmic plots are a device of the devil", he gave them a try and soon "I saw that I could now rank the earthquakes one above the other. ... This set of logarithmic differences thus became the numbers on a new instrumental scale." (See <i>Earthquake Information Bulletin, Volume 12, Issue 1, 1980.</i>)

On the Richter scale the magnitude $R$ of an earthquake is given by {{% marnote "earthquake list" %}}![](/img/chapter-3/Earthquake_list.svg#center){{% /marnote %}}

\[
  R=\log\left(\frac{I}{I_0}\right)
\]

where $I$ is the earthquake's reading on a [seismograph](/img/chapter-3/seismograph.jpg), an instrument used to measure the motion of an earthquake.  

Richter arbitrarily chose $I_0$ to be an earthquake whose reading shows a 0.001 millimeter movement on a seismograph that is 100km away from the center of the earthquake.  Due to the logarithmic basis of the scale, each whole number increase in magnitude represents a tenfold increase in the intensity of the quake.

{{% check %}}
The 1906 earthquake in San Francisco would have had a seismographic reading of 7643 millimeters 100km from the epicenter.  Determine its magnitude on the Richter scale. {{% answer %}}\[
\begin{align}
  R&= \log \left(\frac{7643}{0.001}\right) \newline
  &\approx 6.88
\end{align}
\]{{% /answer %}}
{{% /check %}}


## Solve Exponential Equations
Another major use of logarithms is found in solving exponential equations.  Here we aim to explain the basic principles at work.  A  number of detailed examples and techniques will be discussed [Section 3.5](../3.5).  

Because logarithms and exponentials are inverses of each other, the following cancellation properties hold:

\[
  \log_b(b^{x})=x \text{  for all   } x
\]

and  

\[
  b^{\log_b(x)}=x  \text{  for  } x>0
\]

These properties imply that taking a logarithm and exponentiation are *inverse operations*, as long as the bases are the same.

For example, applying the base $10$ logarithm is the opposite of applying the base $10$ exponential.  Thus, an expression like $\log_{10}(10^{\pi})$ simplifies to $\pi$, because the log cancels the exponential.

{{% check %}}
1. What is the opposite of applying the base $3$ logarithm to an equation? {{% answer %}}Exponentiating with a base of $3$.{{% /answer %}}
1. What is the opposite of exponentiating with a base of $4$? {{% answer %}}Taking the base $4$ logarithm.{{% /answer %}}
1. Use a cancellation property to simplify $2^{\log_2(13)}$. {{% answer %}}$13${{% /answer %}}
1. Use a cancellation property to simplify $\log_6(6^{81})$. {{% answer %}}$81${{% /answer %}}
{{% /check %}}


One way to solve an exponential equation is to apply a logarithm with the same base to both sides, so that we can apply the cancellation properties.

For instance, to solve $3^{x}=100$, we can take the base-3 logarithm of both sides and simplify.

| $3^{x} =100$ ||
| ----- | ----- |
| $\log_3(3^{x}) = \log_3(100)$ | *Apply $\log_3$ to both sides.* |
| $x = \log_3(100)$ | *Use the cancellation property.* |

The only difficulty with this method is that we do not have a convenient way to approximate $\log_3(100)$.  It would be nice if we could rewrite this value using either the common or natural logarithms, for then we could use the `LOG` or `LN` buttons on a calculator.

Whenever we encounter an exponential equation such as $3^{x}=100$, we should always consider *taking the natural logarithm $ln$ of both sides*.  Since logarithms are one-to-one, taking the natural logarithm of both sides does not change the solution.  It does however, allow us to reformat the equation using the power rule.  After using the power rule, the equation will be much simpler to solve.  

To illustrate how this is done, we will solve the exponential equation $3^{x}=100$ for $x$.

| $3^{x} =100$ ||
| ----- | ----- |
| $\ln(3^{x}) = \ln(100)$ |*Apply $\ln$ to both sides.*  |
| $x \cdot \ln(3) = \ln(100)$ |*Use the power rule.*  |
| $x = \frac{\ln(100)}{\ln(3)}$ |*Divide both sides by $\ln(3)$.* |
| $x \approx 4.1918$ |*Use* `LN` *button to obtain a decimal approximation.* |

We chose $\ln$ simply because most calculators have a `LN` button.  Had we used a $\log$ or any other logarithm for that matter, the answer would have been the same.   

{{% check %}}
1.  Use your calculator to verify that `log(100)/log(3)` gives the same value as `ln(100)/ln(3)`.  Does this mean that $\log$ and $\ln$ are the same thing? {{% answer %}}**NO**.  The base of $\log$ is $10$ while the base of $\ln$ is $e$, so they are not the same function.  However, since all logarithms share the same properties (such as the power rule), either one can be used to solve an exponential equation.{{% /answer %}}
{{% /check %}}


## Change of Base Formula
We have just solved the equation $3^{x}=100$ three different ways.  One answer was $x=\log_3(100)$, another was  $x=\frac{\ln(100)}{\ln(3)}$, and in the last **QUICK CHECK** we saw that $x=\frac{\log(100)}{\log(3)}$ is also a solution.  How do we reconcile these three solutions?

Since all exponential functions are one-to-one, the equation $3^{x}=100$ can only have one solution, and we are forced to conclude that *all three are equal*:  

\[
  \log_3(100)= \frac{\ln 100}{\ln 3}=\frac{\log 100}{\log3}
\]  

What we have discovered is a way to evaluate $\log_{3} 100$ by utilizing either $\ln$ or $\log$.  

In practice, we can evaluate a logarithm with any base by rewriting it as an expression involving $\ln$ or $\log$.  

\[
  \log_{b}(x)=\frac{\log(x)}{\log(b)}
\]   

or

\[
  \log_{b}(x)=\frac{\ln(x)}{\ln(b)}
\]

We use $\log$ or $\ln$ simply because calculators have `LOG` and `LN` buttons.  In theory, any other logarithm $\log_{a}$ could be used:

\[
  \log_{b}(x)=\frac{\log_a(x)}{\log_a(b)}
\]

which is called the generic **change of base formula**.  It allows us to convert from one base to any other base.

{{% check %}}
1. Use the change of base formula to approximate $\log_7(13)$. {{% answer %}}$\log_7(13)=\frac{\ln(13)}{\ln(7)} \approx 1.318${{% /answer %}}
1. Use the change of base formula to approximate $\log_4(68)$. {{% answer %}}$\log_4(68)=\frac{\ln(68)}{\ln(4)} \approx 3.0437${{% /answer %}}
{{% /check %}}
---
title: "3.5 Exponential and Logarithmic Equations"
description:
author: "Nolan Mitchell"
type: page
image: "ken-treloar-pFoA5Pphb-Q-unsplash.jpg"
draft: false
tags: ["solving-exponential-equations", "solving-logarithmic-equations", "isolate-exponential", "one-to-one-property", "rewrite-as-logarithm", "take-logarithm-both-sides", "power-rule", "inverse-property", "half-life-applications", "iodine-123", "doubling-time", "continuous-compound-interest", "carbon-dating", "radioactive-decay", "piltdown-man", "nuclear-stockpile", "population-growth", "exponentiating", "finding-inverses", "change-of-base", "google-stock"]
---

{{% imgcap file="/img/chapter-3/ken-treloar-pFoA5Pphb-Q-unsplash.jpg" title="Photo by Ken Treloar on Unsplash" source="https://unsplash.com/photos/pFoA5Pphb-Q" %}}

## Introduction
Since exponential and logarithmic functions arise in many applications, it is essential to be able to manipulate and solve equations involving them.  As an example of the type of problems we might encounter, consider the following situation.

A patient who is undergoing diagnostic imaging for thyroid cancer typically swallows a capsule containing the radioactive isotope Iodine-123 shortly before being placed inside a scanner.  The scanner detects radiation from the Iodine-123 and constructs a 3D image of the area being scanned, which is used by doctors to plan treatment options.  

One of the main advantages of using Iodine-123 is that it has a relatively short half-life of approximately 13.2 hours.  This means that within 13.2 hours, one-half of the Iodine-123 will be gone.

If a patient is given 400 microcuries of Iodine-123, how long will it take for the radiation level to drop to a negligible 10 microcuries?

To answer this question, we need to be able to solve the exponential half-life equation

\[
  10=400\left(\frac{1}{2}\right)^{t/13.2}
\]

In this section, we will learn techniques for solving equations like this, where the variable is in the exponent, as well as equations involving logarithms. Once we have established the basic techniques, we can return and solve questions like this one.


## Techniques for Solving Exponential Equations
There are three main techniques for solving exponential equations.  But before solving any exponential equation we should first isolate the exponential expression.

### First Step: Isolate the Exponential
When working with more complicated exponential equations it is often necessary to perform some algebraic simplifications first in order to isolate the exponential expression.  

As an example, let's examine the equation $500(1.2)^{x}=3000$.  Here the exponential expression $(1.2)^{x}$ has been multiplied by $500$.  If we divide both sides of the equation by $500$, then we will have isolated $1.2^{x}$.

\[
\begin{align}
500(1.2)^{x} &= 3000 \newline
1.2^{x} &= 6 &&  \small \color{#5fa2ce} {\text{Divide by } 500} \newline
\end{align}
\]

At this point we can choose an appropriate solving technique from the choices discussed below.  But this initial step of isolating the exponential is always an essential first step.

{{% check %}}
1. What must be done to isolate the exponential in the equation $2^{x}+6=54$?{{% answer %}}Subtracting $6$ from both sides will isolate the exponential.{{% /answer %}}
1. What must be done to isolate the exponential in the equation $4(3)^{x}=324$ ?{{% answer %}}Dividing both sides by $4$ will isolate the exponential.{{% /answer %}}
{{% /check %}}


### Solving Method 1: The One-to-One Property of Exponentials
One technique for solving an exponential equation is to take advantage of the fact that all exponential functions are one-to-one.  This means that

\[
  b^N=b^M \text{ if and only if }N=M
\]

So if we can express both sides of an equation as powers of the same base, then the one-to-one property tells us that the solution can be found by comparing the exponents.

For example, suppose we want to solve $7^{x+3}=49$.  We can do so by writing both sides as powers of $7$ and equating the exponents.

\[
\begin{align}
7^{x+3} &= 49 \newline
7^{x+3} &= 7^2 && \small \color{#5fa2ce}{{\text{Rewrite }} 49=7^2} \newline
x+3 &= 2 && \small \color{#5fa2ce}{\text {One-to-one property of exponentials}} \newline
x &= -1 && \small \color{#5fa2ce}{-3 \text{ from both sides}}
\end{align}
\]

Notice that this method only works when both sides can be written easily as powers of the same base.  If the equation had been just slightly different, say $7^{x+3}=50$, we would not have been able to solve it easily with this technique.

{{% check %}}
Solve the exponential equation $2^{x-1}=8$ by relating the bases.    {{% answer %}}
\[
\begin{align}
2^{x-1} &= 8 \newline
2^{x-1} &= 2^{3} && \small \color{#5fa2ce}{\text{rewrite } 8=2^{3}} \newline
x-1 &=3 && \small \color{#5fa2ce}{\text{since exponentials are one-to-one}} \newline
x &= 4  && \small \color{#5fa2ce}{+1 \text{ to both sides}}
\end{align}
\]
{{% /answer %}}
{{% /check %}}


### Solving Method 2:  Rewrite as a Logarithmic Equation
Another useful technique is to rewrite an exponential equation as an equivalent logarithmic equation using the definition of a logarithm.

\[
  b^{x}=y \Longleftrightarrow \log_{b}(y) = x
\]

For instance, if we start with the equation $3^{x}=10$ then rewriting it as a logarithm gives us the solution $x = \log_3{10}$, which could be evaluated using the change of base formula.{{% sidenote "Change of Base"%}}\[ \log_b(x)=\frac{\log(x)}{\log(b)}=\frac{\ln(x)}{\ln(b)} \]{{% /sidenote %}}  The complete process would look like this:

\[
\begin{align}
3^{x} &= 10 \newline
x &= \log_3(10) && \small \color{#5fa2ce}{\text{Rewrite as a log equation}} \newline
x &= \frac{\ln(10)}{\ln(3)} && \small \color{#5fa2ce}{\text{Change of base formula}} \newline
x & \approx 2.0959 && \small \color{#5fa2ce}{\text{Evaluate}} \newline
\end{align}
\]

We could have used $\log$ for the change of base formula and still arrived at the correct answer, but $\ln$ will be our default choice.

{{% check %}}
How would you solve $5^{x}=200$ for $x$?    {{% answer %}}
\[
\begin{align}
5^{x} &= 200 \newline
x &= \log_5(200) && \small \color{#5fa2ce}{\text{Rewrite as a log equation}} \newline
x &= \frac{\ln(200)}{\ln(5)} && \small \color{#5fa2ce}{\text{Change of base formula}} \newline
x & \approx 3.292 && \small \color{#5fa2ce}{\text{Evaluate}} \newline
\end{align}
\]
{{% /answer %}}
{{% /check %}}


### Solving Method #3: Take the Logarithm of Both Sides
Perhaps the most useful technique for solving an exponential equation is to take the logarithm of both sides.   

For example, suppose we start with $3^{x}=10$ and take the natural log of both sides.
\[
\begin{align}
3^{x} &= 10 \newline
\ln\left(3^{x}\right) &= \ln(10)  && \small \color{#5fa2ce}{\text{Apply } \ln \text{to both sides}}
\end{align}
\]

While this might seem worse than the original equation, it is actually better because we can now apply the power rule for logarithms{{% sidenote "Power Rule"%}}\[ \log_b x^{p} =  p \log_b (x) \]{{% /sidenote %}} and bring the $x$ out of the exponent.

\[
\begin{align}
\ln\left(3^{x}\right) &= \ln(10) \newline
x \cdot \ln(3) &= \ln(10) && \small \color{#5fa2ce}{\text{Power rule for logs}}
\end{align}
\]

The final step is to divide both sides by the number $\ln(3)$.

\[
\begin{align}
x \cdot \ln(3) &= \ln(10)  \newline
x  &= \frac{\ln(10)}{\ln(3)} && \small \color{#5fa2ce} {\text{Divide by } \ln(3)} \newline
x  &\approx 2.0959 && \small \color{#5fa2ce} {\text{Evaluate}}
\end{align}
\]

Notice that the last two lines are exactly the same as when we solved this earlier with the change of base formula.  One of the nice features of this technique is that the change of base formula is built in, so you do not need to memorize it.

{{% check %}}
Solve the same equation $3^{x}=10$ using $\log$ instead of $\ln$.  Verify that your decimal approximation is identical to the one found above.   {{% answer %}}
\[
\begin{align}
3^{x} &= 10 \newline
\log\left(3^{x}\right) &= \log(10)  && \small \color{#5fa2ce}{\text{Apply } \log} \newline
x \cdot \log(3) &= \log(10) && \small \color{#5fa2ce}{\text{Power rule for logs}} \newline
x  &= \frac{\log(10)}{\log(3)} && \small \color{#5fa2ce} {\text{Divide by } \log(3)} \newline
x  &\approx 2.0959 && \small \color{#5fa2ce} {\text{Evaluate}}
\end{align}
\]
{{% /answer %}}
{{% /check %}}

This method has an extra benefit if the base of the exponential in the equation is $e$.

If we start with the equation $e^{2x}=17$, as an example, then when taking the natural log of both sides we are able to use the inverse property of logs{{% sidenote "Inverse Logs"%}}\[ \log_b\left(b^x\right)=x \]{{% /sidenote %}} rather than the power rule.  

\[
\begin{align}
e^{2x} &= 17 \newline
\ln\left(e^{2x}\right) &= \ln 17 && \small \color{#5fa2ce}{\text{Apply } \ln} \newline
2x &= \ln 17 && \small \color{#5fa2ce} {\text{Inverse property of logs}} \newline
x &= \frac{\ln 17}{2} && \small \color{#5fa2ce} {\text{Divide by }2} \newline
x &\approx 1.4166 && \small \color{#5fa2ce} {\text{Evaluate}}
\end{align}
\]

Notice how this simplifies the solving process, with the logarithm undoing the exponential.

## Solve Applications Involving Exponential Equations
### Half-Life
{{% imgcap file="/img/chapter-3/ken-treloar-pFoA5Pphb-Q-unsplash.jpg" title="Photo by Ken Treloar on Unsplash" source="https://unsplash.com/photos/pFoA5Pphb-Q" %}}

Now that we have established the basic techniques for solving exponential equations, let's return to the section opener.

We want to know how long it will take for the radiation level to drop to 10 microcuries given an initial dose of 400 microcuries of Iodine-123.  Since we know that the half-life of Iodine-123 is 13.2 hours, we will use the half-life formula to write our equation:

\[
  10=400\left(\frac{1}{2}\right)^{t/13.2}
\]

Our task is to solve this equation for $t$.  The first step is to isolate the exponential.

\[
\begin{align}
10 &= 400\left(\frac{1}{2}\right)^{t/13.2} \newline
\frac{10}{400}  &=  \left(\frac{1}{2}\right)^{t/13.2} &&  \small \color{#5fa2ce} {\text{Divide by } 400} \newline
\end{align}
\]

Now we have to decide which method to use to solve the equation. Since it is not obvious how to write both sides as powers of $\frac{1}{2}$, and converting it to a logarithm equation looks like it would be messy, let's take the natural logarithm of both sides.

\[
\begin{align}
\frac{10}{400}  &=  \left(\frac{1}{2}\right)^{t/13.2} \newline
\ln \left(\frac{10}{400} \right) &= \ln \left(\frac{1}{2}\right)^{t/13.2} && \small \color{#5fa2ce} {\text{Apply } \ln} \newline
\ln \left(\frac{10}{400} \right) &= \frac{t}{13.2} \ln \left(\frac{1}{2}\right) && \small \color{#5fa2ce} {\text{Power rule for logs}} \newline
\frac{\ln \left(\frac{10}{400}\right)}{\ln \left(\frac{1}{2}\right)} &= \frac{t}{13.2} && \small \color{#5fa2ce} {\text{Divide by } \ln\left(\frac{1}{2}\right)} \newline
t &= 13.2 \frac{\ln \left(\frac{10}{400}\right)}{\ln \left(\frac{1}{2}\right)} && \small \color{#5fa2ce} {\text{Multiply by } 13.2} \newline
t &\approx 70.249 && \small \color{#5fa2ce} {\text{Evaluate}}
\end{align}
\]

This means that it will take 70.249 hours (roughly 3 days) for the radiation level to drop from 400 to 10 microcuries.


### Doubling Time
![](http://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/US_%245000_1934_Federal_Reserve_Note.jpg/1024px-US_%245000_1934_Federal_Reserve_Note.jpg)

When solving real life problems, we usually will not be given the equation directly.  When this happens, we must construct it from the information available and our knowledge of appropriate models.

For instance, suppose you have invested \\$5000 in an account earning 2% interest compounded continuously.  How long will it take for your investment to double?

Since this question involves continuously compounded interest, we should use the continuous growth model $A(t)=P e^{r t}$.  

{{% check %}}
Based on the information given, what are the values for $P$, $r$ and $A(t)$?  {{% answer %}}The initial deposit is 5000 dollars, so $P=5000$.  The rate is given as 2%, so $r=0.02$.  The balance of the account should be double the initial deposit, so $A(t)=10000$.  Substituting those values into $A(t)=P e^{r t}$ will let us solve for the time it takes for the investment to double.{{% /answer %}}
{{% /check %}}

Making the substitutions $P=5000$ and $r=0.02$ we see that the account balance for any $t$ is given by $A(t)=5000e^{0.02 t}$.  We need to find $t$ so that $A(t)=10000$.

\[
\begin{align}
10000 &= 5000 e^{0.02 t} \newline
2 &= e^{0.02 t} && \small \color{#5fa2ce} {\text{Divide both sides by } 5000} \newline
\ln(2) &= \ln(e^{0.02 t}) && \small \color{#5fa2ce} {\text{Apply } \ln \text{ to both sides}} \newline
\ln(2) &= 0.02 t && \small \color{#5fa2ce} {\text{Use the inverse relationship } \ln(e^{x})=x} \newline
\frac{\ln(2)}{0.02} &= t && \small \color{#5fa2ce} {\text{Divide both sides by } 0.02} \newline
t &\approx 34.657 && \small \color{#5fa2ce} {\text{Decimal approximation}} \newline
\end{align}
\]

We have found that it will take close to 35 years for the investment to double if it earns 2% continuously.  

{{% check %}}
Rework the problem above assuming the initial deposit is just $70$ dollars.  What is the doubling time?  What does this tell you about doubling times in general?{{% answer %}}Once we divide by $70$, this is exactly the same as the problem above and has the same solution. </br>
| $140 =70 e^{0.02 t}$ | |
| --- | --- |
| $2 =e^{0.02 t}$ |*Divide both sides by $70$ to isolate the exponential.* |
</br> This shows that doubling time depends entirely on the rate, not on the size of the initial investment.{{% /answer %}}
{{% /check %}}


### Stock Price for Google
<!-- prettier-ignore -->
Let's consider a similar example.  When Google went public in 2004 you could buy a share of stock for \\$85 .  

![](/img/chapter-3/Google_2015_logo.svg#center)
<!-- prettier-ignore -->
Just 2 years later, Google stock was trading at \\$387 per share.  Assuming the price increased exponentially, what was the continuous rate of growth?

In this case, we will also use $A(t)=P e^{r t}$.  We know $P=85$, $t=2$ and want to find $r$ so that $A(2)=387$.

| $387 = 85 e^{r(2)}$ |  |
| --- | --- |
| $\frac{387}{85} =e^{2 r}$ | *Divide both sides by $85$ to isolate the exponential.* |
| $\ln\left(\frac{387}{85}\right) = \ln\left(e^{2 r}\right)$ | *Apply the natural log $\ln$ to both sides.* |
| $\ln\left(\frac{387}{85}\right) = 2 r$ | *Use the inverse relationship $\ln(e^{x})=x$.* |
| $\frac{\ln\left(\frac{387}{85}\right)}{2} = r$ |  *Divide both sides by $2$.* |
| $r \approx 0.7579$ | *Use a calculator to find a decimal approximation.* |

This means that over the 2-year period from 2004 to 2006, Google's stock increased at a continuous rate of 75.79%.  

Notice that while the numbers were different, the process of solving this equation was exactly the same as in the previous example. The only difference being that we were solving for $r$ instead of $t$.


### Radioactive Decay
![](/img/chapter-3/piltdown.gif#center)

In 1912, men working in an English quarry discovered what appeared to be a prehistoric human skull.  Piltdown Man, as the fossil was known, seemed to be a clear indication that the human species had originated in England and was considered by many to be the "missing link" in the history of human evolution.  But was it really?

The age of fossils is often determined by a process called *carbon dating*.  Plants absorb small amounts of the radioactive isotope carbon-14 from the atmosphere.  People and animals collect carbon-14 when they eat plants and other animals.  Once they die, however, the amount of carbon-14 begins to decay exponentially with a half-life of about 5730 years.  By comparing the amount of carbon-14 in a fossil with the amount that would have been been present when it was alive we can estimate the fossil's age.

Suppose that you were able to get a small fragment of the bone and extract $9.7 \times 10^{-15}$ grams of carbon-14 out of it.  If there would have been $1.05 \times 10^{-14}$ grams present when Piltdown Man was alive, how old is this fossil?

To solve this we will use the half-life formula $f(t) = a \left(\frac{1}{2}\right)^{t/c}$.

{{% check %}}
Use the information above to write the equation that we must solve.  Keep in mind that $a$ is the initial value, $c$ is the half-life, and $f(t)$ is the amount after some period of time.   {{% answer %}}Taking $a = 1.05 \times 10^{-14}$, $c = 5730$ and $f(t) = 9.7 \times 10^{-15}$, the equation that must be solved is
\[9.7 \times 10^{-15} = 1.05 \times 10^{-14}\left(\frac{1}{2}\right)^{t/5730}\]{{% /answer %}}
{{% /check %}}

To determine the actual age of the Piltdown skull, we must use the half-life formula with $a=1.05 \times 10^{-14}$, $c = 5730$ and $f(t) = 9.7 \times 10^{-15}$.  Our task is to solve for $t$.

| $9.7 \times 10^{-15} = 1.05 \times 10^{-14}\left(\frac{1}{2}\right)^{t/5730}$ | |
| --- | --- |
| $0.9238 = \left(\frac{1}{2}\right)^{t/5730}$ | *Divide both sides by $1.05 \times 10^{-14}$ to isolate the exponential.* |
| $\ln(0.9238) = \ln \left(\left(\frac{1}{2}\right)^{t/5730}\right)$ | *Apply the natural log $\ln$ to both sides.* |
| $\ln(0.9238) = \frac{t}{5730} \ln \left(\frac{1}{2}\right)$ | *Use the power rule for logarithms.* |
| $\frac{\ln(0.9238)}{\ln\left(\frac{1}{2}\right)} = \frac{t}{5730}$ | *Divide both sides by $\ln\left(\frac{1}{2}\right)$.* |
| $t = 5730 \frac{\ln(0.9238)}{\ln\left(\frac{1}{2}\right)}$ | *Multiply both sides by $5730$.* |
| $t \approx 655.21$ | *Use a calculator to find a decimal approximation.* |

As this result suggests, Piltdown Man was an elaborate forgery.  Someone had cleverly stained and carved the bones to look old, though this fact was not discovered for more than 40 years.  And while the perpetrator has never been determined, there are several suspects, including Sir Arthur Conan Doyle (author of Sherlock Holmes) who lived nearby.  In any case, Piltdown Man remains one of the greatest unsolved scientific hoaxes of all time.


### Nuclear Stockpile
{{% imgcap file="/img/chapter-3/B831_bomb.jpg" title="Photo by Paul Shambroom" source="https://paulshambroom.com/nuke" %}}

During the 1950's, the number of active nuclear warheads in the U.S. arsenal doubled every 2.27 years. If there were 369 nuclear warheads in 1950, when did the U.S. stockpile exceed 30,000?

As we are given the doubling time, it makes sense to use the function $f(t)=a(2)^{t/c}$ with $a=369$, $c = 2.27$ and to try and find a $t$ so that $f(t)=30000$.

| $30000 =369(2)^{t/2.27}$ | |
| --- | --- |
| $\frac{30000}{369} = 2^{t/2.27}$ | *Divide both sides by $369$ to isolate the exponential.* |
| $\ln\left(\frac{30000}{369}\right) = \ln\left(2^{t/2.27}\right)$ | *Apply the natural log $\ln$ to both sides.* |
| $\ln\left(\frac{30000}{369}\right) = \frac{t}{2.27} \ln(2)$ | *Use the power rule for logarithms.* |
| $\frac{\ln\left(\frac{30000}{369}\right)}{\ln(2)} =\frac{t}{2.27}$ | *Divide both sides by $\ln(2)$.* |
| $t = 2.27 \frac{\ln\left(\frac{30000}{369}\right)}{\ln(2)}$ | *Multiply both sides by $2.27$.* |
| $t \approx 14.40$ | *Use a calculator to find a decimal approximation.*|

So if the number of nuclear warheads since 1950 is given by $f(t)=369(2)^{t/2.27}$, then our work suggests the United States had a stockpile of more than 30,000 warheads some time in the spring of 1964.  

{{% check %}}
If nuclear arms production had continued at that rate, how many warheads would there have been in 2010?  {{% answer %}}Taking $t=60$, we have \[ f(60)=369(2)^{60/2.27} \approx 33,401,528,382 \]
which would have been enough for everyone on Earth to have about 5.  As of 2017, the official number was 3822 stockpiled warheads according to the [US Department of Energy](https://open.defense.gov/Portals/23/Documents/frddwg/2017_Tables_UNCLASS.pdf).{{% /answer %}}
{{% /check %}}


### Population Growth
{{% imgcap file="/img/chapter-3/rabbit-1436329_1280.jpg" title="Photo by Andreas Lischka from Pixabay" source="https://pixabay.com/images/id-1422882/" %}}
Suppose your neighbor starts a farm with $4$ cute little rabbits.   One hundred days later, she is tending a herd of $28$ rabbits.  Assuming exponential growth, how long until she has $500$ rabbits at her farm?

Before we can answer this question, we need to find the continuous rate of growth by solving $28=4e^{k \cdot 100}$ for $k$.

| $28 = 4e^{k \cdot 100}$ |  |
| --- | --- |
| $\frac{28}{4} = e^{100 k}$ | *Divide both sides by $4$ to isolate the exponential.* |
| $\ln 7 = \ln(e^{100 k})$ | *Apply the natural log $\ln$ to both sides.* |
| $\ln 7 = 100 k$ | *Use the inverse relationship $\ln(e^{x})=x$.* |
| $\frac{\ln 7}{100} = k$ | *Divide both sides by $100$.* |
| $k \approx 0.0195$| *Use a calculator to find a decimal approximation.* |

So the number of bunnies can be modeled by $f(t)=4e^{0.0195 \thinspace t}$.  

{{% check %}}
How can we determine when there will be 500 rabbits? {{% answer %}}We need to find $t$ so that $f(t)=500$, so we have to solve the equation $500=4e^{0.0195 \thinspace  t}$.{{% /answer %}}
{{% /check %}}

Since the number of bunnies is modeled by $f(t)=4e^{0.0195 \thinspace t}$, to figure out when the population is at 500 we should solve the equation $500 = 4e^{0.0195 \thinspace t}$ for $t$.

| $500 =4e^{0.0195 \thinspace  t}$ | |
| --- | --- |
| $\frac{500}{4} = e^{0.0195 t}$ | *Divide both sides by $4$ to isolate the exponential.* |
| $\ln 125 = \ln(e^{0.0195 t})$ | *Apply the natural log $\ln$ to both sides.* |
| $\ln 125 = 0.0195 t$ | *Use the inverse relationship $\ln(e^{x})=x$.* |
| $\frac{\ln 125}{0.0195} = t$ | *Divide both sides by $0.0195$.* |
| $t \approx 247.6$ | Use a calculator to find a decimal approximation.|

We conclude that in roughly 250 days the farmer will have 500 rabbits.

{{% check %}}
How would the equation have been different if we wanted to know when the farmer would have 2000 rabbits?
{{% answer %}}The only change would be that $f(t)=2000$.  The solving process would remain the same.{{% /answer %}}
{{% /check %}}


# Techniques for Solving Logarithmic Equations
While our primary focus has been solving exponential equations that arise from different applications, we should also discuss solving logarithmic equations.

Just as with exponential equations, it's usually best to try and simplify the equation first.

### Use Log Properties
If an equation contains multiple logarithms, we should start by using log properties to condense those into a single logarithm, if possible.

For instance, the left side of the equation $\log(x+39)-\log(4x) = 1$ could be condensed using the quotient rule.

\[
\begin{align}
\log(x+39)-\log(4x) &= 1 \newline
\log\left(\frac{x+39}{4x}\right) &= 1 && \small \color{#5fa2ce}{\text{Quotient rule for logs}}
\end{align}
\]

At this point we can choose an appropriate solving technique from the choices discussed below.  But this initial step of trying to condense multiple logarithms is always something we should look for first.

{{% check %}}
1. Use the product property to write the left side of the equation $\ln 8 + \ln x = 7$ as a single logarithm.  {{% answer %}}$\ln(8x)=7${{% /answer %}}
1.  Which log property could you use to simplify the equation $\log(x^{3})=12$? {{% answer %}}The power rule would make the equation $3\log(x)=12$ which becomes the much simpler equation $\log(x)=4${{% /answer %}}
{{% /check %}}


### Solving Method 1: The One-to-One Property of Logarithms
Since logarithms are one-to-one functions, if we know that two logs with the same base are equal then their inputs must also be equal.

\[
  \log_b(N) = \log_b(M) \text{ if and only if } N=M
\]

In other words, as long as both sides are written as single logarithms with the same base, then the logarithms themselves can be ignored.

For example, solving the equation $\log_2(x^{2}+1) = \log_2(26)$ is equivalent to solving $x^{2}+1 = 26$ as we see below.

\[
\begin{align}
\log_2(x^{2}+1) &= \log_2(26) \newline
x^{2}+1 &= 26 && \small \color{#5fa2ce}{\text{One-to-One Property}} \newline
x^{2} &= 25 && \small \color{#5fa2ce}{\text{Subtract } 1} \newline
x &= \pm 5 && \small \color{#5fa2ce}{\text{Square root both sides}}
\end{align}
\]


{{% check %}}
1. Solve the equation $\log_5(x-3) = \log_5(9)$. {{% answer %}}Using the logarithm property of equality, we only need to solve $x-3=9$.  The solution is $x=12$.{{% /answer %}}
1. Solve the equation $\ln\sqrt{x} = \ln(4)$. {{% answer %}}Using the logarithm property of equality, we only need to solve $\sqrt{x} = 4$.  The solution is $x=16$.{{% /answer %}}
{{% /check %}}


### Solving Method 2: Rewrite as an Exponential Equation
Another solving technique is to isolate the logarithmic expression and rewrite the equation as an equivalent exponential using the definition of a logarithm.

\[
  b^{x}=y \Longleftrightarrow \log_{b}(y) = x
\]

Consider the equation $4 \log_3(x-2) = 16$.  If we divide both sides by $4$ then the logarithm will be isolated and we can solve by rewriting it as an exponential equation.

\[
\begin{align}
4 \log_3(x-2) &= 16 \newline
\log_3(x-2) &= 4 && \small \color{#5fa2ce}{\text{Divide by } 4} \newline
3^{4} &= x-2 && \small \color{#5fa2ce}{\text{Rewrite as an exponential equation}} \newline
81+2 &= x && \small \color{#5fa2ce}{\text{Add }2} \newline
x &= 83 && \small \color{#5fa2ce}{\text{Simplify}}
\end{align}
\]

This is useful anytime the equation can be written as a single logarithm, even if it doesn't start out that way.

{{% check %}}
What should be done to isolate the logarithm in the equation $6+\log(2x)=9$?
{{% answer %}}Subtracting $6$ from both sides will isolate the logarithm.  It can then be solved using the technique above.
\[
\begin{align}
6+\log(2x) &= 9 \newline
\log(2x) &= 3 && \small \color{#5fa2ce}{\text{Subtract } 6} \newline
10^{3} &= 2 x && \small \color{#5fa2ce}{\text{Rewrite as an exponential equation}} \newline
\frac{1000}{2} &= x && \small \color{#5fa2ce}{\text{Divide by }2} \newline
x &= 500 && \small \color{#5fa2ce}{\text{Simplify}}
\end{align}
\]
{{% /answer %}}
{{% /check %}}


### Solving Method 3: Exponentiate Both Sides
Our final method is to exponentiate both sides of the equation using the base of the logarithm.  

To *exponentiate* both sides of an equation means to turn each side into an exponent of the base $b$.  Once that has been done we can take advantage of the inverse property between logs and exponentials.{{% sidenote "Inverse Exp"%}}\[ b^{\log_b x} = x \]{{% /sidenote %}}

We will illustrate the process using the equation $\log_2 x= 6$.

\[
  \begin{align}
    \log_2 x &= 6 \newline
    2^{\log_{2} x} &= 2^{6}  && \small \color{#5fa2ce}{\text{Exponentiate base } 2} \newline
    x &= 2^{6} && \small \color{#5fa2ce}{\text{Inverse property}} \newline
    x &= 64 && \small \color{#5fa2ce}{\text{Evaluate}}
  \end{align}
\]

 Earlier we would have solved this by rewriting it as the exponential equation $x=2^6$ and simplifying to see that $x=64$, and rewriting is probably the preferred method.  We introduce the idea of exponentiation here to reemphasize the inverse relationship between exponentials and logarithms.  Not only are they inverse functions, but it can sometimes be useful to think of exponentiation and taking the logarithm as inverse operations.  Exponentiating can then be viewed as just another operation we can use when we solve equations by reversing the order of operations.

{{% check %}}
Exponentiate both sides of the equation $\ln(x) = 4$.  Simplify if possible.  {{% answer %}}The base of the natural logarithm is $e$, so we will place both sides of the equation into the exponent of an $e$.  $e^{\ln(x)} = e^{4}$ But $e$ and $\ln$ are inverses, so this simplifies to $x=e^4$ which is the same answer we would get by converting $\ln(x) = 4$ to an exponential equation. {{% /answer %}}
{{% /check %}}



## Find Inverses
As we learned earlier, we can find an inverse by listing the operations performed by the function and doing the *opposite operations in the reverse order*.  Viewing exponentiation and logarithms as opposite operations allows us to find the inverses of more complicated exponential and logarithmic functions.  

For instance, the function $f(x)=5(3)^{x+2}$ does three things to each input value.  It adds $2$, then exponentiates with a base of $3$, and lastly multiplies by $5$.  It's inverse should divide by $5$, then apply the base $3$ logarithm, and finally subtract $2$.  We summarize this in the table below.

| | **Operations Done by the Function** || **Operations Done by the Inverse** |
| --- | --- | --- | --- |
|  1.  | Add $2$ |  1.  | Divide by $5$ |
| 2. | Exponentiate with a base of $3$ | 2. | Apply the base $3$ logarithm |
| 3. | Multiply by $5$ | 3. | Subtract $2$|

Now we take the operations listed and build the inverse function $f^{-1}$ as follows:

| 1. | Start with a variable: | $x$ |
| --- | --- | --- |
| 2. | Divide by $5$: | $\frac{x}{5}$ |
| 3. | Apply the base $3$ logarithm: | $\log_3\left(\frac{x}{5}\right)$ |
| 4. | Subtract $2$ : | $\log_3\left(\frac{x}{5}\right)-2$ |
| 5. | Write as a function: | $f^{-1}(x)=\log_3\left(\frac{x}{5}\right)-2$ |


{{% check %}}
Identify the order of operations of the function $f(x)=500(2)^{x/27}$.  Then find the inverse function $f^{\thinspace-1}$.  {{% answer %}}This function **(1)** divides by 27, then **(2)** exponentiates with a base of 2, and **(3)** multiplies by 500.  The inverse should **(1)** divide by 500, **(2)** apply the base 2 logarithm, and **(3)** multiply by 27.  The equation is
$f^{-1}(x)=27*\log_2\left(\frac{x}{500}\right)$. {{% /answer %}}
{{% /check %}}


Let's look at another example.  This time we will find the inverse of $g(t)=\log_2(3 t-7)$.  Start by listing the operations of the function in the proper order and then list which operations its inverse should do.

|| **Operations Done by the Function** || **Operations Done by the Inverse** |
| --- | --- | --- | --- |
|  1.  | Multiply by $3$ |  1.  | Apply the base $2$ exponential |
| 2. | Subtract $7$ | 2. | Add $7$ |
| 3. | Apply the base$2$ logarithm | 3. | Divide by $3$ |

Once we know the inverse operations and their order we can build up the inverse function.

| 1. | Start with a variable: | $t$ |
| --- | --- | --- |
| 2. | Apply the base $2$ exponential: | $2^t$ |
| 3. | Add $7$: | $2^t+7$ |
| 4. | Divide by $3$: | $\frac{2^t+7}{3}$ |
| 5. | Write as a function: | $g^{-1}(t)=\frac{2^t+7}{3}$ |


## Looking Ahead
The key idea from this section is that since exponential and logarithmic functions are inverses functions, we can also use them as inverse operations to solve equations and applications.
---
title: "4.1 Addition and Subtraction of Functions"
description:
author: "Nolan Mitchell"
type: page
image: "smartphone.jpg"
draft: false
tags: ["combining-functions", "function-addition", "function-subtraction", "adding-functions-graphically", "domain-of-combined-functions", "equations-of-combined-functions", "symmetry-of-combined-functions", "profit-and-revenue", "catenary-curves", "gateway-arch", "polynomials", "polynomial-terms", "degree", "leading-coefficient", "constant-term", "graphs-of-polynomials"]
---

{{% imgcap file="/img/chapter-4/smartphone.jpg" title="Photo by Pexels" source="https://pixabay.com/photo-1283938/" %}}

## Introduction
Not too long ago, mobile phones were only used for making phone calls, nothing else was possible.  Today's smart phones, however, combine the functionality of several different devices into one convenient package.

In a similar way, mathematical functions can be combined together to create new functions.  In this section we will focus on combining two or more functions through the algebraic operations of addition and subtraction.


## Combining Functions by Addition
We begin by summing the outputs of two functions. This is done with normal addition since the outputs of a function are real numbers.  For instance, if $\color{red}{f(}1\color{red}{) = -5}$ and $\color{blue}{g(}1\color{blue}{) = 19}$, then

\[
  \color{red}{f(}1\color{red}{)} + \color{blue}{g(}1\color{blue}{)} = \color{red}{-5} + \color{blue}{19} =  14
\]

In the table below, use the given values of $\color{red}{f(}x\color{red}{)}$ and $\color{blue}{g(}x\color{blue}{)}$ to find values for $(f+g)(x)$.

<table>
  <tr>
    <th>$x$</th><th>$\color{red}{f(}x\color{red}{)}$</th><th>$\color{blue}{g(}x\color{blue}{)}$</th><th>$\color{red}{f(}x\color{red}{)} + \color{blue}{g(}x\color{blue}{)}$</th>
  </tr>
  <tr>
    <td>$1$</td><td>$\color{red}{-5}$</td><td>$\color{blue}{19}$</td><td>$\color{red}{-5} + \color{blue}{19}=14$</td>
  </tr>
  <tr>
    <td>$2$</td><td>$\color{red}{13}$</td><td>$\color{blue}{-7}$</td><td>{{% answer %}}$\color{red}{13}  \color{blue}{-7}=6${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$3$</td><td>$\color{red}{21}$</td><td>$\color{blue}{4}$</td><td>{{% answer %}}$\color{red}{21} + \color{blue}{4}=25${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$4$</td><td>$\color{red}{8}$</td><td>$\color{blue}{0}$</td><td>{{% answer %}}$\color{red}{8} + \color{blue}{0}=8${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$5$</td><td>$\color{red}{-2}$</td><td>$\color{blue}{32}$</td><td>{{% answer %}}$\color{red}{-2} + \color{blue}{32}=30${{% /answer %}}</td>
  </tr>
</table>

Taking a closer look at these results you might notice that each $\color{black}{x}$ creates a single $\color{red}{f(}x\color{red}{)} + \color{blue}{g(}x\color{blue}{)}$ value.

![](/img/chapter-4/function_addition.svg#center)

In other words, the values of  $\color{red}{f(}x\color{red}{)} + \color{blue}{g(}x\color{blue}{)}$  are a function of $\color{black}{x}$.  This is only natural since $\color{red}{f}$ and $\color{blue}{g}$ are both functions of $\color{black}{x}$.  


## Adding Functions Graphically
Now let's take a look at what happens when you add the outputs of two functions graphically.

As you change $x$ in the interactive figure below the value of $\color{red}{f(}x\color{red}{)} + \color{blue}{g(}x\color{blue}{)}$ will be recorded, forming a new graph.  Is this new graph a function?  Does it look familiar?  Make a note of your observations before continuing.

{{% geogebra ratio="50%" id_1="eWfigb1Jo0IzflDg" id_2="dPa7vBG3" id_m="dPa7vBG3" %}}

There are two things you should notice about the resulting graph (shown here in **<font color="gray">gray</font>**).  

![](/img/chapter-4/function_addition_graph.svg#center)

First, it passes the vertical line test, which confirms our earlier conclusion that $\color{red}{f} + \color{blue}{g}$ is a new function of $x$.  To emphasize this, from now on we will use the following notation

\[
  (f+g)(x) =   f(x) + g(x)
\]

when referring to the sum of two functions.

Second, the graph of $(f+g)(x)$ retains some of the properties of both $f(x)$ and $g(x)$.  It has dips and bumps like $g(x)$, but it also has the upward trend of $f(x)$.  

Adding two functions always creates a new function that blends together the behaviors of the two original functions.


## The Domain of $(f+g)(x)$
Let's now suppose that both $f(x)$ and $g(x)$ are undefined over some regions, as in the figure below.  How does this affect $(f+g)(x)$ ?

{{% geogebra ratio="50%" id_1="mrpyHNh1nQAPSDPy" id_2="FOsUyxCc" id_m="FOsUyxCc" %}}

In working with the interactive figure above you probably realized that $(f+g)(x)$ is only defined if both $f(x)$ and $g(x)$ are defined.  If either is undefined, then $(f+g)(x)$ is undefined as well.

![](/img/chapter-4/function_addition_domain.svg#center)

In this particular example, $f$ is defined on the intervals $[1, 5]$ and $[6, 8]$ while $g$ is defined on $[1,2]$ and $[3,8]$.  The function $f+g$ is only defined in the regions where those intervals overlap.

The domain of $f+g$ is always the intersection of the domain of $f$ and the domain of $g$.

{{% check %}}
1.  Suppose the domain of $f$ is {1, 2, 3, 4, 5} and the domain of $g$ is {2, 4, 6, 8, 10}.  What is the domain of  $f+g$? {{% answer %}}The domain of  $f+g$ is {2, 4}, since those are the only values that are found in both the domain of $f$ and the domain of $g$.{{% /answer %}}

2.  If the domains of the functions $p$ and $q$ are $x<2$ and $x\geq-10$, respectively, what is the domain of $p+q$? {{% answer %}}The domain consists of the $x$ that are in both domains.  In this case, only $-10\leq x < 2$ are allowable. {{% /answer %}}
{{% /check %}}


## Equations of $(f+g)(x)$
If the functions $f$ and $g$ are defined by equations, then the combined function $f+g$ is the sum of those two equations.  Of course, this rule only makes sense when $f$ and $g$ are both defined.

As an example, consider the two functions $f(x)=\sqrt{x}$ and $g(x)=2x$.  The equation for their sum is

\[
  (f+g)(x)=\sqrt{x} + 2x
\]

Since the square root is not defined for negative values, the domain of $f+g$ must be $x\geq0$.  

With an equation we evaluate $f+g$ by simply replacing $x$ with the appropriate value.   

If we want to evaluate $(f+g)(9)$ for the function above, for example, we replace $x$ with $9$ and simplify.

\[
\begin{align}
(f+g)(9) &= \sqrt{9} + 2(9) \newline
&= 3+18 \newline
&= 21
\end{align}
\]

On the other hand, we cannot evaluate $(f+g)(-4)$ since $x=-4$ is not in the domain of this particular function.

{{% check %}}
Suppose $f(x)=x^{3}$ and $g(x)=\frac{1}{x}$.

1.  Find the equation for $f+g$.   {{% answer %}}\[(f+g)(x)=f(x)+g(x)=x^{3}+\frac{1}{x}\].{{% /answer %}}
1.  What is the domain of the function $f+g$?  {{% answer %}}The domain is all real numbers except for $x=0$ since $f(x)=x^{3}$ is defined for all real numbers but $g(x)=\frac{1}{x}$ is undefined when $x=0$. {{% /answer %}}
1.  What is the value of $(f+g)(2)$?  {{% answer %}}\[(f+g)(2)=(2)^{3}+\frac{1}{2}=8+\frac{1}{2}=8.5\]{{% /answer %}}
{{% /check %}}


## Combining Functions by Subtraction
Up to this point we have focused on adding functions.  Predictably, subtracting functions yields similar results.

Below values for two functions $\color{red}{f(}x\color{red}{)}$ and $\color{blue}{g(}x\color{blue}{)}$ are given.  Use subtraction to complete the table values for $(f-g)(x)$.

<table>
<tr>
  <td>$x$</td><td>$\color{red}{f(}x\color{red}{)}$</td><td>$\color{blue}{g(}x\color{blue}{)}$</td><td>$\color{red}{f(}x\color{red}{)} - \color{blue}{g(}x\color{blue}{)}$</td>
</tr>
<tr>
  <td>$1$</td><td>$\color{red}{2}$</td><td>$\color{blue}{8}$</td><td>$\color{red}{2} - \color{blue}{8}=-6$</td>
</tr>
<tr>
  <td>$2$</td><td>$\color{red}{29}$</td><td>$\color{blue}{-1}$</td><td>{{% answer %}}$\color{red}{29} - \color{blue}{-1}=30${{% /answer %}}</td>
</tr>
<tr>
  <td>$3$</td><td>$\color{red}{13}$</td><td>$\color{blue}{-22}$</td><td>{{% answer %}}$\color{red}{13} - \color{blue}{-22}=35${{% /answer %}}</td>
</tr>
<tr>
  <td>$4$</td><td>$\color{red}{-1}$</td><td>$\color{blue}{9}$</td><td>{{% answer %}}$\color{red}{-1} - \color{blue}{9}=-10${{% /answer %}}</td>
</tr>
<tr>
  <td>$5$</td><td>$\color{red}{0}$</td><td>$\color{blue}{7}$</td><td>{{% answer %}}$\color{red}{0} - \color{blue}{7}=-7${{% /answer %}}</td>
</tr>
</table>

As with addition, the essential observation here is that if $f$ and $g$ are both functions of $x$, then their difference  $f - g$ is also a function of $x$.   Furthermore, $(f-g)(x)$ is evaluated by

\[
  (f-g)(x)=f(x)-g(x)
\]

and its domain is the intersection of the domains of $f$ and $g$.

Take, for instance,  the functions $f(x)=\frac{1}{x+6}$ and $g(x)=x+1$.  Their difference is the new function

\[
\begin{align}
(f-g)(x) &=\frac{1}{x+6}-(x+1) \newline
&=\frac{1}{x+6}-x-1
\end{align}
\]

Since the domain of $f(x)=\frac{1}{x+6}$ does not include $x=-6$, we cannot include $x=-6$ in the domain of $(f-g)(x)$.

{{% check %}}
Suppose $f(x)=\log(x)$, which has a domain of $x>0$, and $g(x)=x^{3}$, which is defined for all real numbers.

1. Determine the equation for $(f-g)(x)$ and its domain.    {{% answer %}}$(f-g)(x)=\log(x)-x^{3}$.  The domain is all $x>0$.{{% /answer %}}
1. Evaluate $(f-g)(2)$   {{% answer %}}$(f-g)(2)=\log(2) - 8\approx-7.7${{% /answer %}}
1. Evaluate $(f-g)(-2)$   {{% answer %}}This is not defined, since $-2$ is not in the domain.{{% /answer %}}
{{% /check %}}


## Symmetry
As we saw earlier, the function $f+g$ blends together the behaviors of $f$ and $g$.  However, since $f$  and $g$ can have very different maximums, minimums, intercepts, etc., predicting the exact behavior of $f+g$ is difficult.

One behavior that we can usually predict is the symmetry of $f+g$.   If $f$ and $g$ are both even functions (ie. symmetric across the y-axis), then so is $f+g$.  Likewise, if $f$ and $g$ are odd functions (ie. symmetric around the origin), then $f+g$ is also an odd function.

You may wish to verify this with the interactive figure below.  The graphs of two even functions $\color{red}{f(x)=3-x^2}$ and $\color{blue}{g(x)=x^{2/3}}$ are shown.  Changing $x$ and/or pressing **Play** will draw the graph of $f+g$.  

You are free to enter any equations you want for $\color{red}{f}$ and $\color{blue}{g}$.  You might want to also try two odd functions, like $x^{3}$ and $x^{1/3}$, or some other combinations before continuing.

{{% geogebra ratio="40%" id_1="FDg45LeJ67WEWpql" id_2="ghdHeX19" id_m="ghdHeX19" %}}

The same symmetry rules apply for $f-g$.  If $f$ and $g$ are both even functions (ie. symmetric across the y-axis), then so is $f-g$.  Likewise, if $f$ and $g$ are odd functions (ie. symmetric around the origin), then $f-g$ is also odd.

{{% check %}}
Without graphing, decide if the following functions have even or odd symmetry.

1. $f(x)=  x^{4} - x^{2}$ {{% answer %}}Since both $x^{4}$ and $x^{2}$ are even, this function will have even symmetry.{{% /answer %}}
1. $g(x)=x^{3} + \ln(x)$ {{% answer %}}$x^{3}$ is odd but $\ln (x)$ is neither even nor odd, so this function does not have any symmetry.{{% /answer %}}
1. $h(x)=x + \frac{1}{x}$ {{% answer %}}Since both $x$ and $\frac{1}{x}$ are odd, this function is also odd.{{% /answer %}}
{{% /check %}}


## Applications
It is impossible to cover every possible application of adding and subtracting functions, but we'll look at a few just to illustrate the variety.


### Calculating Profit and Deductions
{{% imgcap file="/img/chapter-4/hanh-nguyen-j6DH45Bflho-unsplash.jpg" title="Photo by Hanh Nguyen on Unsplash" source="https://unsplash.com/photos/j6DH45Bflho" %}}

Imagine that one day you brought a homemade cupcake to work and a friend offered to buy it from you for $\\$2.50$.  If the ingredients cost $\\$1.00$, then you earned a profit of $\\$1.50$.

Recognizing that made-from-scratch-daily cupcakes could be a commercial success, you throw caution to the wind and open your own bakery.

After several days and nights of baking, you discover that the ingredient cost for $x$ cupcakes is given by the function $\color{#E69F00}{C(x)=0.65 x + \frac{0.85}{x}}$.  And since you are charging $\\$2.50$ per cupcake, your revenue is given by $\color{#56B4E9}{R(x)=2.5x}$.

Your *profit* is the difference of these two functions.  That is to say, $P(x)=(\color{#56B4E9}{R} - \color{#E69F00}{C})(x)$.

{{% check %}}
What is the profit if you sell 500 cupcakes?   {{% answer %}}
\[
  \begin{align}
    P(500) &=(\color{#56B4E9}{R} - \color{#E69F00}{C})(500) \newline
    &=\color{#56B4E9}{R(500)} - \color{#E69F00}{C(500)} \newline
    &=\color{#56B4E9}{1250} - \color{#E69F00}{325} \newline
    &=925
  \end{align}
\]
So the profit on 500 cupcakes would be \\$925.
{{% /answer %}}
{{% /check %}}

Now that you are running a business and earning a profit, you need to calculate how much of your weekly profits $P$ should be sent to the federal government for income tax and Social Security.  Since different income levels pay different tax rates, federal income tax is a piecewise function.  Let's assume that

\[
  \color{#009E73}{T(P)=\begin{cases}
    0 &  \$0\leq P \leq \$42 \newline
    0.1(P-42) & \$42 \leq P \leq \$214 \newline
    17.2+0.15(P-214) & \$214 \leq P \leq \$739 \newline
    95.95+0.25(P-739) & \$739 \leq P \leq \$1732
  \end{cases} }
\]

for single taxpayers.  

The Social Security deduction is fixed percent so it is a simpler function.  We'll say that for self-employed individuals it is $\color{#CC79A7}{S(P)=0.153P}$, or $15.3\%$ of your weekly profit.

If your weekly profit was $P=600$ dollars, then your total federal deductions are

\[
  \begin{align}
    \color{#009E73}{T(600)}+\color{#CC79A7}{S(600)} &= \color{#009E73}{17.2+0.15(600-214)}+\color{#CC79A7}{0.153(600)} \newline
    &= \color{#009E73}{75.1}+\color{#CC79A7}{91.80} \newline
    &= \$166.90
  \end{align}
\]

{{% check %}}
Suppose your weekly profit doubles from $P=600$ to $P=1200$.  How much are your new federal deductions? {{% answer %}}\[
\begin{align}
\color{#009E73}{T(1200)}+\color{#CC79A7}{S(1200)} &= \color{#009E73}{95.95+0.25(1200-739)}+\color{#CC79A7}{0.153(1200)} \newline
&= \color{#009E73}{211.20}+\color{#CC79A7}{183.60} \newline
&= \$394.80
\end{align}
\]{{% /answer %}}
{{% /check %}}


### Catenary Curves
Another useful, but less taxing, application comes from adding an exponential growth function, like $f(x)=e^{x}$, with an exponential decay function such as $g(x)=e^{-x}$.  What would the graph of such a function look like?

The figure below lets you discover the answer.  Change $x$ and watch as the graph of $(f+g)(x)$ is drawn.  How would you describe its shape?

{{% geogebra ratio="40%" id_1="R4L82gzS2s0kfcDA" id_2="e6hPPmqS" id_m="e6hPPmqS" %}}

While this shape looks like a parabola, it is actually a different curve known as a **catenary**.   

![](/img/chapter-4/catenary.svg#center)

A catenary is the shape formed by any chain hanging freely under its own weight whose ends are held in place.  If you have ever held a necklace or a string loosely between your hands, then you have made a catenary curve.

Upside down, or "inverted" catenary curves are frequently used in the construction of bridges and arches because of the way they distribute the load.  The Gateway Arch{{% sidenote "Gateway Arch"%}}![](/img/chapter-4/e785a7052f4e4d7c9d86259df9edc062Original.jpg)Photo by [Cecil W. Stoughton](https://npgallery.nps.gov/AssetDetail/e785a7052f4e4d7c9d86259df9edc062){{% /sidenote %}} in St. Louis, Missouri is a famous example of an inverted catenary arch.


## Polynomials
Perhaps the most important consequence of adding and subtracting functions is the creation of a new category of functions known as polynomials.

A **polynomial** is a function that can be written as a sum or difference of power functions whose powers are non-negative integers such as $0, 1, 2, 3, \dotsc$.  

For example, the polynomial $p(x)=\color{red}{5x^{3}}+\color{black}{7x^{2}}\color{orange}{-4x}+\color{green}{8}$ is a sum of the four power functions $\color{red}{5x^{3}}$, &nbsp; $\color{black}{7x^{2}}$, &nbsp; $\color{orange}{-4x}$ &nbsp; and &nbsp; $\color{green}{8}$.

Each power function is called a **term** of the polynomial.  The highest power is called the **degree** of the polynomial, and the coefficient of that term is called the **leading coefficient**.  The term without an $x$ is referred to as the **constant term**.

![](/img/chapter-5/polynomial_terms.svg#center)

Polynomials cannot contain terms like $x^{5/2}$ or $x^{1.28}$ or $x^{-3}$,  since the powers $5/2$ and $1.28$ are not integers and $-3$ is negative.  Neither can a polynomial include any exponential or logarithmic terms like $2^{x}$, $e^{x}$ and $\ln x$.

{{% check %}}
Decide if the following are polynomials or not.  If it not, explain why not.  If it is a polynomial, state its degree.

1. $f(x)=x^{2}+1$  {{% answer %}}Yes, this is a polynomial.  The degree is $2$.{{% /answer %}}
1. $g(x)=2^{x}+3^{x}-7$  {{% answer %}}No, this is not a polynomial because $2^{x}$ and $3^{x}$ are exponential functions.{{% /answer %}}
1. $h(x)=4x^{3.5}+2x^{-3/4}+6x$  {{% answer %}}No, this is not a polynomial because the powers $3.5$ and $-3/4$ are not non-negative integers.{{% /answer %}}
1. $p(x)=x^{12}-x^{5}+9x-23$  {{% answer %}}Yes, this is a $12-"th"$ degree polynomial.{{% /answer %}}
1. $q(x)=(x+3)^{2}$  {{% answer %}}Yes, since this can be written as $q(x)=x^{2}+6x+9$, it is a polynomial.  The degree is $2$.{{% /answer %}}
1. $r(x)=\frac{1}{x-5}$  {{% answer %}}No, this is not a polynomial because it cannot be written as a sum of non-negative integer powers of $x$.{{% /answer %}}
1. $s(x)=\sqrt{x+4}$  {{% answer %}}No, this is not a polynomial because it cannot be written as a sum of non-negative integer powers of $x$.{{% /answer %}}
{{% /check %}}


## Graphs of Polynomials
The graphs of polynomials are very reminiscent of roller coasters. We will explore their graphs in greater detail in [Chapter 5](//chapter-5/5.1). For now, use the interactive figure below to familiarize yourself with some of the possible shapes. You are free to show or hide the individual power functions and to change their coefficients.

{{% geogebra ratio="50%" id_1="67U7cvounRV85WCc" id_2="IzqmS4xo" id_m="IzqmS4xo" %}}

## Looking Ahead
In this section we have seen how combining a few simple functions through the operations of function addition and subtraction can create new functions that display a wide variety of behaviors.  

Polynomial functions, in particular, are prized for both the simplicity of their equations and the complexity of their behavior.  That duality makes them attractive models for data and processes that change from increasing to decreasing multiple times.

Since we've just covered function addition and subtraction, you can probably guess what is coming next:  multiplication and division.
---
title: "4.2 Multiplication and Division of Functions"
description:
author: "Nolan Mitchell"
type: page
image: "storm-surge-3735936_1280.jpg"
draft: false
tags: ["function-multiplication", "function-division", "domain-of-product", "multiplying-power-functions", "multiplying-exponentials", "multiplying-polynomials", "surge-functions", "storm-surge", "hurricane-katrina", "quotient-of-functions", "rational-functions", "simplifying-rational-functions", "cancellation", "polynomial-long-division", "synthetic-division", "divisor-quotient-remainder", "domain-of-combined-functions", "equations-of-combined-functions", "symmetry-of-combined-functions"]
---


{{% imgcap file="/img/chapter-4/storm-surge-3735936_1280.jpg" title="Photo by Jerry Coli from Pixabay " source="https://pixabay.com/images/id-3735936/"%}}

## Introduction
The strong winds of large tropical storms, like hurricane Katrina or super storm Sandy, can push sea water toward the shore causing severe flooding.  These "storm surges" are often a greater threat to life and property than the hurricane itself.  The surge after Katrina reached 28 feet above flood level.

In this section we will see a simplified model for storm surges that results from multiplying a power function by an exponential decay function.


## Combining Functions by Multiplication
In the last section we saw that if $f$ and $g$ are both functions, then we can form new functions by taking their sum $f+g$ or their difference $f-g$.  The *product* of two functions $fg$ is also a function and can be evaluated using the rule

\[
  (fg)(x)=f(x)g(x)
\]

In the table below, use the given values of $\color{red}{f(}x\color{red}{)}$ and $\color{blue}{g(}x\color{blue}{)}$ to find values for $(fg)(x)$.

<table>
  <tr>
    <td>$x$</td><td>$\color{red}{f(}x\color{red}{)}$</td><td>$\color{blue}{g(}x\color{blue}{)}$</td><td>$(fg)(x)=\color{red}{f(}x\color{red}{)}\color{blue}{g(}x\color{blue}{)}$</td>
  </tr>
  <tr>
    <td>$1$</td><td>$\color{red}{4}$</td><td>$\color{blue}{9}$</td><td>$\color{red}{(4)}\color{blue}{(9)}=36$</td>
  </tr>
  <tr>
    <td>$2$</td><td>$\color{red}{3}$</td><td>$\color{blue}{-5}$</td><td>{{% answer %}}$\color{red}{(3)}\color{blue}{(-5)}=-15${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$3$</td><td>$\color{red}{1}$</td><td>$\color{blue}{14}$</td><td>{{% answer %}}$\color{red}{(1)}\color{blue}{(14)}=14${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$4$</td><td>$\color{red}{-8}$</td><td>$\color{blue}{-3}$</td><td>{{% answer %}}$\color{red}{(-8)}\color{blue}{(-3)}=24${{% /answer %}}</td>
  </tr>
  <tr>
    <td>$5$</td><td>$\color{red}{-32}$</td><td>$\color{blue}{0}$</td><td>{{% answer %}}$\color{red}{(-32)}\color{blue}{(0)}=0${{% /answer %}}</td>
  </tr>
</table>

Notice that each $x$ creates only one $(fg)(x)$ value, which means that multiplying two functions always creates a new function.

## The Domain of $(fg)(x)$
As with the sum and difference, the domain of $fg$ is the intersection of the domains of $f$ and $g$.

For example, if $f(x)=\ln(x)$ and $g(x)=4-x^{2}$, then

\[
  \begin{align}
    (fg)(x) &= \ln(x)(4-x^{2}) \newline
    &= 4\ln(x)-x^{2}\ln(x)
  \end{align}
\]

Since $f(x)=\ln(x)$ is only defined for positive values of $x$, the product $f g$ is only defined for $x>0$ as well.

{{% check %}}
1. Suppose $f(x)=\sqrt{x+4}$ and $g(x)=\frac{1}{x}$.  Find the equation for $f g$ and state its domain. {{% answer %}}\[ (f g)(x)=f(x)g(x)=\sqrt{x+4} \frac{1}{x}=\frac{\sqrt{x+4}}{x} \].
The domain of $f(x)=\sqrt{x+4}$ is all numbers greater than or equal to $-4$.  The domain of $g$ is anything except $0$.  So the domain of $fg$ is all real numbers greater than or equal to $-4$, except for $0$.  In interval notation, it would be $[-4, 0) \bigcup (0,\infty)$.{{% /answer %}}
1. If the domain of $f$ is $[-10, 6)$ and the domain of $g$ is $(4, 9]$, what is the domain of $fg$? {{% answer %}}$[-10, 6) \cap (4, 9] = (4, 6)$ so the domain of $fg$ is $(4, 6)$.  In other words, only the numbers between 4 and 6.{{% /answer %}}
{{% /check %}}


## Simplifying $(fg)(x)$
Sometimes we can tell what type of function the product $f g$ will be by recognizing what type of function $f$ and $g$ are.

### When $f$ and $g$ are Power Functions
Suppose you take two power functions, like $\color{red}{f(x)=x^{1.3}}$ and $\color{blue}{g(x)=x^{2.5}}$.  Their product is also a power function

\[
  \begin{align}
    (f g)(x) &= \color{red}{x^{1.3}}\color{blue}{x^{2.5}} \newline
    &= x^{3.8}
  \end{align}
\]

### When $f$ and $g$ are Exponential Functions
A similar thing holds if $f$ and $g$ are both exponential functions.  As an example, consider $\color{red}{f(x)=2^{x}}$ and $\color{blue}{g(x)=3^{x}}$.  The equation for $f g$ is

\[
  \begin{align}
    (f g)(x) &= \color{red}{2^{x}}\color{blue}{3^{x}} \newline
    &= 6^{x}
  \end{align}
\]

which is also an exponential function.  

### When $f$ and $g$ are Polynomials
Lastly, the product of two polynomials is still a polynomial.  Using $\color{red}{f(x)=3x+1}$ and $\color{blue}{g(x)=x+4}$, for instance, gives

\[
  \begin{align}
    (f g)(x) &= \color{red}{(3x+1)}\color{blue}{(x+4)} \newline
    &= 3x^{2}+13x+4
  \end{align}
\]


## Graphs of $(fg)(x)$
We can also gain some insight into the graph of $(fg)(x)$ by inspecting the graphs of $f(x)$ and $g(x)$.

Of particular interest is the fact that $(fg)(x)$ inherits the x-intercepts from both $f(x)$ and $g(x)$.  

This can be explored in the interactive figure below.  The $\color{red}{f(x)=4-x^{2}}$ and $\color{blue}{\ln(x)}$ are shown, though you can change either one.

{{% geogebra ratio="40%" id_1="7088gRlSnR7MzxmG" id_2="ccAPEyMG" id_m="ccAPEyMG" %}}

It's worth noting that the product $fg$ only exists for $x>0$ since the domain of the logarithm is $x>0$.


## Applications
At the start of this section we mentioned the storm surge following a tropical storm like a hurricane.  It's now time that we looked at this shape and tried to find a function with a similar graph.

The chart below from the United States Geological Survey shows the storm surge for Hurricane Rita in 2005.  Notice how the water level (in blue) increases quickly, and then recedes at a slower rate.

![](https://pubs.usgs.gov/ds/2006/220/images/LA9b.gif)

One way to create a function that grows quickly and then decays is to multiply an increasing power function by an exponential decay function.

In the figure below, the graphs of $f(x)=10x^{2}$ and $g(x)=e^{-x}$ are shown.  The graph of $(fg)(x)=10x^{2}e^{-x}$ will be drawn as you change the value of $x$.

{{% geogebra ratio="40%" id_1="GZumI2j14Zzb1bPr" id_2="AfMnn6k3" id_m="AfMnn6k3" %}}

As you have just seen, the graph of the function $f(x)=10x^{2}e^{-x}$ is similar in some ways to storm surge flooding.  In fact, functions of this type, where an increasing power function is multiplied by an exponential decay function, are often called *surge* functions.  All **surge functions** have the form

\[
  f(x)=ax^{p}e^{-b x}
\]

where $p>0$ and $b>0$.  The rapid rise, or surge, is caused by the power function and the eventual decay is due to the exponential function.

Surge functions can be found in a number of areas.  For instance, the level of [glucose](/img/chapter-4/surge_data_2.png) in your blood, the [electrical current](/img/chapter-4/surge_data_3.png) in a toy car, the number of [Tweets](/img/chapter-4/surge_data_4.png) about a world news event, or even the number of people trying to figure out how to watch the [Superbowl](/img/chapter-4/surge_data_5.png) online can display surge-like behavior.

Unfortunately, fitting a surge function to real data is beyond the scope of this book, but its existence should illustrate the utility of creating new functions by multiplication.  Division of functions is also useful, and that is where we turn our attention next.


## Combining Functions by Division
Since we have worked with addition, subtraction and multiplication of functions, it should come as no surprise that dividing one function by another creates a new function.  The **quotient** of two functions $f$ and $g$ is defined as

\[
  \left(\frac{f}{g}\right)(x)=\frac{f(x)}{g(x)}
\]

provided that $g(x) \neq 0$.


## Simplifying $\left(\frac{f}{g}\right)(x)$
If $f$ and $g$ are either both power functions or both exponential functions then the rules of exponents allow us to simplify their quotients.

You might recall that

\[
  \frac{x^m}{x^n}=x^{m-n}
\]

where $m$ and $n$ are any real numbers and $x \neq 0$.  In the present context, this shows that the quotient of any two power functions is just another power function, and that $x=0$ must be excluded from the domain of $x^{m-n}$.

Another rule of exponents states that

\[
  \frac{a^x}{b^x}=\left(\frac{a}{b}\right)^{x}
\]

where $a$ and $b$ are any positive real numbers.  This rule shows that the quotient of any two exponential functions is still an exponential function.  And since $a$ and $b$ are positive, there are no restrictions on the domain of $\left(\frac{a}{b}\right)^{x}$.

{{% check %}}
1. If $f(x)=x^{2}$ and $g(x)=x^5$, find the equation for $\left(\frac{f}{g}\right)(x)$. {{% answer %}}\[ \left(\frac{f}{g}\right)(x) = \frac{x^2}{x^5} = x^{2-5} = x^{-3} \]{{% /answer %}}
1. If $f(x)=2^{x}$ and $g(x)=5^{x}$, find the equation for $\left(\frac{f}{g}\right)(x)$ {{% answer %}}\[ \left(\frac{f}{g}\right)(x) = \frac{2^{x}}{5^{x}} = \left(\frac{2}{5}\right)^{x} \]{{% /answer %}}
{{% /check %}}


## Rational Functions
As we have just seen, division of power functions and division of exponential functions is simply an application of the rules of exponents.  

In those cases division does not generate a new category of function--the quotient of two power functions is just another power function and the quotient of two exponentials is another exponential function.  

However, dividing one polynomial by another polynomial does create a new family of functions, known as **rational functions**.  A rational function is any function that can be written in the form

\[
  f(x)=\frac{n(x)}{d(x)}
\]

where $n(x)$ and $d(x)$ are both polynomials and $d(x)\neq0$.

{{% check %}}
Which of the following are rational functions?

1. $f(x)=\frac{x^{2}+1}{x-3}$  {{% answer %}}Yes, this is a rational function.{{% /answer %}}
1. $g(x)=\frac{2^x+3}{3^x-7}$  {{% answer %}}No, this is not a rational function because $2^x+3$ and $3^x-7$ are not polynomials.{{% /answer %}}
1. $h(x)=6x^{2}+2x$  {{% answer %}}Yes, every polynomial is a rational function where the denominator is $d(x)=1$.{{% /answer %}}
1. $p(x)=\frac{2}{x^5-9x^{2}-3}$  {{% answer %}}Yes, this is a rational function.{{% /answer %}}
{{% /check %}}


## Graphs of Rational Functions
The graphs of rational functions can have very interesting and complex behaviors.  The graphs below should give you an idea of the variety we might encounter.

![](/img/chapter-4/rational_functions_graphs.svg#center)

In [Chapter 5](//chapter-5/5.5) we will examine the properties of rational functions.  One tool that will help us do that is being able to simplify the equation by cancelling common terms, if possible, or by polynomial division.


## Simplifying Rational Functions by Cancellation
Sometimes it is possible to simplify a rational function by canceling common factors.  Whenever we cancel factors, we should keep in mind the domain of the original rational function.

For instance, the rational function $f(x)=\frac{x^{2}-3x}{x}$ can be simplified by canceling the $x$ that all terms have in common.

\[
  \begin{align}
    f(x) &= \frac{x^{2}-3x}{x} \newline
    &= \frac{x^{2}}{x} - \frac{3x}{x} \newline
    &= x-3
  \end{align}
\]

But we must remember to specify that this only holds for $x \neq 0$, since $0$ is not included in the domain of $f(x)=\frac{x^{2}-3x}{x}$.  The proper way to write it is

\[
  f(x)=\frac{x^{2}-3x}{x}=x-3, \thinspace x \neq 0
\]

Without the condition that $x \neq 0$, this would be a false statement.

{{% check %}}
1. What is the domain of the rational function $f(x)=\frac{(x-3)(x-4)}{x-3}$? {{% answer %}}$x \neq 3${{% /answer %}}
1. Simplify the rational function $f(x)=\frac{(x-3)(x-4)}{x-3}$. {{% answer %}}This simplifies to \[ f(x)=x-4, x \neq 3 \]  The $x \neq 3$ restriction is necessary.{{% /answer %}}
1. Simplify the rational function $f(x)=\frac{x^{2}+3x+2}{x+2}$ by first factoring the numerator. {{% answer %}}\[\begin{align}f(x)&=\frac{x^{2}+3x+2}{x+2} \newline &=\frac{(x+1)(x+2)}{x+2} \newline &= x+1, \thinspace x \neq -2 \end{align} \]{{% /answer %}}
{{% /check %}}


## Simplify Rational Functions by Long Division
When no common factors can be found, a rational function can be simplified by division, but only if the polynomial in the numerator has a degree that is higher than or equal to the degree of the denominator.

For instance, $f(x)=\frac{x^{2}-3x}{x-1}$ and $f(x)=\frac{x^4-6x}{x^4+8}$ can be simplified by division while $g(x)=\frac{2x+4}{x^{3}-5}$ cannot.

{{% check %}}
1.  Can we use division to simplify $f(x)=\frac{7x^5-2x^{3}+11}{x^{2}+3x-1}$? {{% answer %}}Yes, the degree in the numerator is $5$, which is higher than the denominator's degree of $2$.  So polynomial division could be used.{{% /answer %}}
1.  Can we use division to simplify $f(x)=\frac{x^{2}+1}{x^{4}+3x-1}$? {{% answer %}}No, the degree in the numerator is $2$, which is lower than the denominator's degree of $4$.  So polynomial division cannot be used.{{% /answer %}}
{{% /check %}}


You'll recall that dividing one whole number by a whole number *divisor* results in a *quotient* and a *remainder*.  As an example,

\[
  \frac{15}{7} = 2 + \frac{1}{7}
\]

where $7$ is the divisor, $2$ is the quotient and $1$ is the remainder.

Polynomial division follows the identical pattern:

\[
  \frac{n(x)}{d(x)}=q(x)+\frac{r(x)}{d(x)}
\]

We refer to the function $d(x)$ as the **divisor**, $q(x)$ as the **quotient** and $r(x)$ as the **remainder**.  

{{% check %}}
Suppose $\frac{3x^{2}+1}{x-2}=3x+6+\frac{13}{x-2}$.  Identify the divisor, quotient and remainder.
{{% answer %}}The divisor is $d(x)=x-2$.  The quotient is $q(x)=3x+6$.  The remainder is $r(x)=13$.{{% /answer %}}
{{% /check %}}

The traditional method for dividing one polynomial by another is called **polynomial long division**, and works much like long division of numbers.  The figure below will walk you through the algorithm for dividing $3x^{2}+5x-2$ by $x+1$.  Use the controls in the lower left corner to start or pause the process or skip directly to any step.

{{% geogebra ratio="50%" id_1="CoF2ZmtzTw1P1KwH" id_2="kBIVwuSv" id_m="kBIVwuSv" %}}

After performing the division we need to identify the divisor $d(x)$, the quotient $q(x)$ and the remainder $r(x)$.

![](/img/chapter-4/long_division.png#center)

Now we can simplify $\frac{3x^{2}+5x-2}{x+1}$ using the $\frac{n(x)}{d(x)}=q(x)+\frac{r(x)}{d(x)}$ pattern.  The final result is

![](/img/chapter-4/polynomial_long_division_1b.png#center)

Now that you have seen an example, let's walk through another division problem together.  This time we will divide $4x^{2}-5$ by $x+2$.   

1. Write the problem as a long division. {{% answer %}}![](/img/chapter-4/long_division_QC_1a.png){{% /answer %}}
2. What multiplies $x$ to create $4x^{2}$? {{% answer %}}$4x${{% /answer %}}
3. Perform the first step of the division. {{% answer %}}![](/img/chapter-4/long_division_QC_1b.png){{% /answer %}}
4. What is the next number that should go above the division symbol? {{% answer %}}It needs to be a $-8$.{{% /answer %}}
5. Perform the rest of the division. {{% answer %}}![](/img/chapter-4/long_division_QC_1c.png){{% /answer %}}
6. Now identify the quotient and remainder. {{% answer %}}![](/img/chapter-4/long_division_QC_1d.png){{% /answer %}}


## Synthetic Division
When the divisor is simple, something of the form $x-c$, such as $x-3$ or $x-5$, then the long division process can be greatly simplified.  This simplified division process is called **synthetic division**.  Synthetic division is simpler because we only work with the number $c$ from the divisor and the coefficients of the numerator.  

For instance, if the divisor is $x-6$ then $c=6$, if the divisor is $x+8$ then $c=-8$.

If the numerator is $7x^{3}+5x-9$ then we work with the coefficients $7, 0, 5, -9$, including a $0$ for any term that is missing.

{{% check %}}
1.  What is $c$ if the divisor is $x+4$?   {{% answer %}}$c=-4${{% /answer %}}
2.  Can we use synthetic division if the divisor is $x^{2}-5$?   {{% answer %}}No, the divisor must be of the form $x-c$ for some constant $c$.  {{% /answer %}}
3.  What are the coefficients of $-2x^5 + x^{3} - 7x+5$?   {{% answer %}}$-2,0,1,0,-7,5${{% /answer %}}
{{% /check %}}


Whereas the long division algorithm required multiplication and then subtraction, with synthetic division we multiply and then add.

Earlier we used long division to divide $3x^{2}+5x-2$ by $x+1$.  Here we perform the same calculation with synthetic division.   Use the controls in the lower left corner to start or pause the process or skip directly to any step.

{{% geogebra ratio="33.333%" id_1="XtFvoYTcImPMucDB" id_2="kNm8cmKM" id_m="kNm8cmKM" %}}

After identifying the divisor $d(x)$, quotient $q(x)$ and remainder $r(x)$.

![](/img/chapter-4/synthetic_division.png#center)

we can rewrite $\frac{3x^{2}+5x-2}{x+1}$ as

![](/img/chapter-4/long_division_1a.png#center)

using the $\frac{n(x)}{d(x)}=q(x)+\frac{r(x)}{d(x)}$ pattern.

Next we will divide $2x^{3}+7x^{2}-2x-12$ by $x+3$.   Fill in the steps as prompted below.  

1. What are the coefficients of the numerator? {{% answer %}}![](/img/chapter-4/synthetic_QCe.png){{% /answer %}}
2. What is $c$? {{% answer %}}![](/img/chapter-4/synthetic_QCd.png){{% /answer %}}
3. Write as a synthetic division. {{% answer %}}![](/img/chapter-4/synthetic_QCa.png){{% /answer %}}
4. Complete the synthetic division. {{% answer %}}![](/img/chapter-4/synthetic_QCb.png){{% /answer %}}
5. Identify the quotient and remainder. {{% answer %}}![](/img/chapter-4/synthetic_QCc.png){{% /answer %}}
6. Use the quotient and remainder to simplify  $\frac{2x^{3}+7x^{2}-2x-12}{x+3}$. {{% answer %}}![](/img/chapter-4/synthetic_QCf.png){{% /answer %}}


## Looking Ahead
We now know how to combine functions using the four basic operations of addition, subtraction, multiplication and division.  We've also seen how complicated behaviors, like those of polynomial and rational functions, can arise by combining simple functions.

We will return to polynomial and rational functions in the [following chapter](/chapter-5/), but first we must investigate [another way to combine functions](../4.3).
---
title: "4.3 Composition of Functions"
description:
author: "Nolan Mitchell"
type: page
image: "washing-machine-2668472_1280.jpg"
draft: false
tags: ["composition-of-functions", "composition-notation", "laundry-analogy", "order-of-composition", "non-commutative", "evaluating-composite-functions", "domain-of-composition", "composition-with-tables", "equation-of-composition", "graphing-composite-functions", "nested-functions", "function-of-a-function"]
---

{{% imgcap file="/img/chapter-4/washing-machine-2668472_1280.jpg" title="Image by Steve Buissinne from Pixabay" source="https://pixabay.com/images/id-2668472/"%}}

## Introduction
Washing laundry usually involves two machines: a washer and a dryer.  Once the wash cycle is over you have to transfer the load over to the dryer.  

What does this have to do with math?  Well, there is a new way to combine functions called **composition**.  Composition is completely different than addition, subtraction, multiplication or division of functions.  Fortunately, the concept behind composition is almost exactly the same as washing laundry.


## Composition of Functions
Let's diagram the laundry experience.  You start by putting a load of dirty clothes and linens into a washing machine.  When the washing cycle is over your laundry is not only clean, but wet as well.  To remedy this you transfer the clean, wet clothes into the dryer and turn it on.  Eventually you have what you wanted:  clean and dry clothes.

![](/img/chapter-4/composition_laundry.svg)

If we overlay the laundry diagram with function notation you can begin to see what function composition is.

![](/img/chapter-4/composition_laundry_notation.svg)

When we take the output of one function (like clean, wet laundry from the washing machine) and input it into another function (like the dryer), the result (clean, dry laundry) is a **composition** of the two functions.

Suppose, for instance, that $\color{blue}{g}$ adds 2 to any number,  and that $\color{red}{f}$ multiplies any input by 10.  In other words, $\color{blue}{g(x)=x+2}$ and $\color{red}{f(x)=10x}$.

If we insert $x = 4$ into $\color{blue}{g}$ then $\color{blue}{6}$ comes out.  Now take $\color{blue}{6}$ and use it as the input to $\color{red}{f}$.

![](/img/chapter-4/composition_laundry_values.svg)

The result is the composition $\color{red}{f(}\color{blue}{g(}4\color{blue}{)}\color{red}{)}=60$.

{{% check %}}
Suppose the example above had started with $x = 1$ instead.  What would be the result of the composition?  {{% answer %}}Putting $x =1$ into $\color{blue}{g}$ gives $\color{blue}{g(}1\color{blue}{)}=\color{blue}{3}$.  Putting $\color{blue}{3}$ into $\color{red}{f}$  produces  $\color{red}{f(}\color{blue}{3}\color{red}{)}=\color{red}{30}$.  So $\color{red}{f(}\color{blue}{g(}1\color{blue}{)}\color{red}{)}=30$ is the result of the composition.{{% /answer %}}
{{% /check %}}


## Understand Composition of Functions
{{% imgcap file="/img/chapter-4/hanh-nguyen-j6DH45Bflho-unsplash.jpg" title="Photo by Hanh Nguyen on Unsplash" source="https://unsplash.com/photos/j6DH45Bflho" %}}

We encountered composition [earlier in this chapter](//chapter-4/4.1#calculating-profit-and-deductions), though we did not call it composition at the time.

Recall that the Social Security deduction for someone who is self-employed was given by the function $S(P)=0.153P$, where $P$ are the profits earned.

But the profit depends on how many items are sold.  In the cupcake example, for instance, $P(x)=1.85x -\frac{0.85}{x}$ where $x$ is the number of cupcakes sold.

If you sold $1000$ cupcakes you would need to first calculate $P(1000)$ before using that value as the input to $S(P)$ to find the Social Security deduction.  This is composition since you are using the output of one function as the input to a second function.

{{% check %}}
Using the functions above, find the Social Security deduction on the profits from selling $1000$ cupcakes. {{% answer %}}First find \[P(1000)=1.85(1000) - \frac{0.85}{1000}\approx\$1850\]
Then evaluate \[S(1850)=0.153(1850)=\$283.05\]
{{% /answer %}}
{{% /check %}}


## Composition Notation
Since composition is a new way of combining functions, it needs its own symbol.  The symbol for composition is a small open circle $\circ$ .  If $\color{red}{f}$ and $\color{blue}{g}$ are functions, the composition of $\color{red}{f}$ with $\color{blue}{g}$ is the function given by

\[(f \circ g)(x)=\color{red}{f(}\color{blue}{g(}x\color{blue}{)}\color{red}{)}\]

For example, using $\color{red}{f(x)=2x^{3}}$ and $\color{blue}{g(x)=\frac{x+3}{2}}$ as our two functions, we can find $(f \circ g)(1)$ as follows:

![](/img/chapter-4/composition_eval_b.svg#center)

Notice that the output of the $\color{blue}{g}$ function was used as the input of the $\color{red}{f}$ function.

{{% check %}}
Using the same functions as above, find $(f \circ g)(7)$.   {{% answer %}}
\[
\begin{align}
(f \circ g)(7) &= f(g(7) \newline
&=f\left(\frac{7+3}{2}\right) \newline
&=f(5) \newline
&=2(5)^3 \newline
&=250
\end{align}
\]
{{% /answer %}}
{{% /check %}}


## Order of Composition
You are probably aware that some operations, like addition and multiplication, are *commutative*, meaning they can be done in any order.

With other operations, like subtraction and division, the order makes a big difference in the result.  

This begs the question: Is the operation of composition commutative?  Can we compose functions in any order we like, or is the order important?

Our laundry analogy suggests that composition may not be commutative, since drying clothes before washing them is not the same as first washing and then drying.

But the analogy is merely a suggestion.  To get real evidence we need to look at some functions and compare $(f \circ g)(x)$ with $(g \circ f)(x)$.

Let's choose two simple functions to work with $\color{red}{f(x)=x+4}$ and $\color{blue}{g(x)=x^2}$.

First we compute $(f \circ g)(5)$ and we'll compare that value with $(g \circ f)(5)$.

![](/img/chapter-4/composition_eval_a.svg#center)

If we compare this with $(g \circ f)(5)$

![](/img/chapter-4/composition_eval_a_reverse.svg#center)

it becomes clear that $(f \circ g)(5)$ and $(g \circ f)(5)$ are not the same.  In general, composition is *not* a commutative operation, and we will need to pay close attention to the order of the functions.


## Evaluate Composite Functions
Now that we know order is important, we should look at a few more examples.  This time $\color{red}{f}$ and $\color{blue}{g}$ are defined by the tables below.

![](/img/chapter-4/composition_table.svg#center)

To evaluate $(g \circ f)(1)$, for example, we first use the table to find $f(1) = 2$, and then find $g(2) = -1$.  Thus, $(g \circ f)(1) = -1$.  

Contrast this with $(f \circ g)(1)=f(g(1))=f(3)$ which is undefined.

{{% check %}}
Use the table above to evaluate the following, if possible.

1. $(f \circ g)(2)$ {{% answer %}}$f(g(2))=f(-1)=-13$ {{% /answer %}}
1. $(g \circ f)(0)$ {{% answer %}}$g(f(0))=g(1)=3$ {{% /answer %}}
1. $(f \circ g)(1)$ {{% answer %}}$f(g(1))=f(3)=\text{undefined}$ {{% /answer %}}
1. $(g \circ f)(2)$ {{% answer %}}$g(f(2))=g(7)=\text{undefined}$ {{% /answer %}}
1. $(g \circ g)(5)$ {{% answer %}}$g(g(5))=g(2)=-1$ {{% /answer %}}
{{% /check %}}


## The Domain of Composite Functions
Let's consider another analogy for composition.  Imagine you wanted to fly from Portland, Oregon to Tahiti.  Since there is no direct service from Portland to Tahiti, you would need to fly somewhere else first and then find a connecting flight.  For instance, you might fly to Hawaii first and then on to Tahiti.

![](/img/chapter-4/composition_tahiti.png#center)

If we regard each flight as a function, then the entire trip could be viewed as a composition of functions.  This analogy gives us two useful insights.  

First, in order for composition to work, there must be some location, like Hawaii, where the range of the first function intersects the domain of the second function.  Otherwise, the composition is undefined, as you discovered previously.

Second, it's possible to create a single new function that has the same actions as the composition of the two separate functions.  This new function would be similar to a direct flight from Portland to Tahiti.

Consider the two functions $\color{red}{f}$ and $\color{blue}{g}$ defined by the arrow diagrams below.  

![](/img/chapter-4/composition_arrow_diagram_1.svg#center)

Since the range of $\color{blue}{g}$ intersects the domain of $\color{red}{f}$ only at $10$, the domain of $h=f \circ g$ can only be the single number $2$, there's no way to use $1$ as an input to $h = f \circ g$ because $5$ is not in the domain of $\color{red}{f}$.

![](/img/chapter-4/composition_arrow_diagram_2.svg#center)

And just as a direct flight from Portland to Tahiti would not stop in Hawaii, the composed function $h=f \circ g$ maps $2$ directly to $13$ without stopping at $10$.


## Composition with Tables
If we return to the functions $\color{red}{f}$ and $\color{blue}{g}$ as defined in the tables below,

![](/img/chapter-4/composition_table.svg#center)

we should be able to compute values of $h(x)=(f \circ g)(x)$.

![](/img/chapter-4/composition_table_b.svg#center)

Since $x = 1$ and $x = 3$ are not valid inputs to
$h(x)=(f \circ g)(x)$ we conclude that the domain is the set $ \lbrace 2,4,5 \rbrace $.

Notice again that the domain of $h=f \circ g$ is always a subset of the domain of $\color{blue}{g}$.


{{% check %}}
Using the same function tables as above, what is the domain of $(g \circ f)(x)$?   {{% answer %}}The domain of $(g \circ f)(x)$ is the set {-2,0,1}.{{% /answer %}}
{{% /check %}}


## Equation of $f \circ g$
When $\color{red}{f}$ and $\color{blue}{g}$ are defined by equations, we find the equation for $h=f \circ g$ by composing the two equations rather than working with individual values.

For instance, if $\color{red}{f(x)=3x^2-x+2}$ and $\color{blue}{g(x)=2^x}$ then

![](/img/chapter-4/composition_eval_4.svg#center)

The benefit of having an equation for $h=f \circ g$ is that it allows you to evaluate the composition more efficiently.  You need only deal with one function instead of two.

{{% check %}}
Using the same functions as above, verify that $(f \circ g)(1)$ gives the same value as $h(1)$.   {{% answer %}}
\[ \begin{align}
    (f \circ g)(1)&=f(g(1)) \newline
    &=f(2^1) \newline
    &=f(2) \newline
    &=3(2)^2-2+2 \newline
    &=12
\end{align}\]
\[ \begin{align}
    h(1)&=3(4)^1-2^1+2 \newline
    & =12
\end{align}\]
{{% /answer %}}
{{% /check %}}

Finding an equation for $h=f \circ g$ also helps us determine its domain.

Take, for example, $f(x)=\ln(x)$ and $g(x)=x-4$.  The composed equation is $h(x)=(f \circ g)(x)=\ln(x-4)$.  

Since the natural logarithm can only take in positive numbers, the domain of $h=f \circ g$ can only include $x$ values for which $x-4>0$.  Therefore, the domain of $h=f \circ g$ must be $x>4$.

Notice that this domain of $x>4$ is a subset of the domain of $g$, which is all real numbers.  Assuming $h=f \circ g$ exits, its domain is always either the entire domain of $g$ or a subset of it.

{{% check %}}
1.  If $f(x)=\sqrt{x}$ and $g(x)=8-x^{3}$, find the equation for $h(x)=(f \circ g)(x)$ and state its domain.   {{% answer %}}$h(x)=(f \circ g)(x)=\sqrt{8-x^{3}}$. Since only positive numbers, or zero, have real square roots, we need $8-x^{3}\geq0$, or $x\leq2$.  So while the domain of $g$ is all real numbers, the domain of $h=f \circ g$ is $x \leq 2$.{{% /answer %}}
1.  If $f(x)=e^{x}$ and $g(x)=1/x$, find the equation for $h(x)=(f \circ g)(x)$and state its domain.   {{% answer %}}$h(x)=(f \circ g)(x)=e^{1/x}$.  Any real number can be inserted into the exponential function, so it does not impose any extra restrictions on the domain of $h=f \circ g$.  We conclude that the domain of $h=f \circ g$ is the same as the domain of $g$, which is $x \neq 0$. {{% /answer %}}
{{% /check %}}


## Graph Composite Functions
The graphs of composite functions can display a wide range of behaviors.  In the figure below you can let $\color{red}{f}$ and $\color{blue}{g}$ be any functions you want.  The graph of $h=f \circ g$ will be drawn as you change $x$ or press **Play**.

Consider putting a polynomial like $g(x)=2x^{2}-x^4$ inside of an exponential function $f(x)=e^{x}$.  Or, as in the example below, compose two functions that are vertical reflections of each other.  The goal here is just to have fun making graphs, so try as many as you like before continuing.


{{% geogebra ratio="50%" id_1="QNrmk8lmdIInXZ3s" id_2="Kbg4KOk8" id_m="Kbg4KOk8" %}}

Determining the exact shape of the graph of a composite function $h=f \circ g$ by examining the equations and/or graphs of $f$ and $g$ is a complicated process.  Generally, it will be best to find the equation for $h=f \circ g$ and then use a computer or graphing calculator to analyze its behavior.

For instance, if $f(x)=e^{-x}$ and $g(x)=x^{2}$ then $h(x)=(f \circ g)(x)=e^{-x^{2}}$ and it can be graphed as follows.  

![](/img/chapter-4/composition_calculator.svg)

With the graph it is easier to analyze the behavior of the function.  For instance, it is now clear that the function $h$ has a maximum of $h(x)=1$ at $x=0$.  We could also discuss asymptotes and regions where the function is increasing or decreasing as well as domain and range.

{{% check %}}
Using the graph above, or a graph on your own calculator, discuss domain, range, asymptotes, etc. of $h(x)=(f \circ g)(x)=e^{-x^{2}}$.

{{% answer %}}

* The domain appears to be all real numbers.
* The range looks to be $(0,1]$.
* The x-axis appears to be a horizontal asymptote.
* The function is increasing on the interval $(-\infty, 0)$ and decreasing on the interval $(0, \infty)$
{{% /answer %}}
{{% /check %}}


## Looking Ahead
We now have five different ways to combine functions, addition, subtraction, multiplication, division and composition.  Combining two functions with any of these operations always produces a new function.

Many of these combined functions are generally not one-to-one.  They do not pass a horizontal line test and do not have inverses unless the domain is restricted.  In the next section we will discuss how to find inverses of these more complicated functions.

We will also see how composition can be used to prove that two functions are inverses of each other.
---
title: "4.4 Inverses of Combined Functions"
description:
author: "Nolan Mitchell"
type: page
image: "small-3871893_1280.jpg"
draft: false
tags: ["finding-inverses", "shoes-and-socks-method", "switch-and-solve-method", "graphing-inverses", "reflecting-across-y-equals-x", "inverses-of-exponentials", "inverses-of-linear-functions", "inverses-of-power-functions", "inverses-of-combined-functions", "verifying-inverses", "round-trip-properties", "composition-to-verify", "applications-of-inverses", "domain-and-range-of-inverses"]
---

{{% imgcap file="/img/chapter-4/small-3871893_1280.jpg" title="Image by Vinson Tan from Pixabay " source="https://pixabay.com/images/id-3871893/"%}}

## Introduction
In the 1980's Hasbro changed the toy world by introducing a line of robot action figures known as *Transformers*.  What made each Transformer special was that if you bent the legs, twisted the torso, and folded the arms, the robot would change into something else, like a car or an airplane.  Undoing each of those steps in the reverse order would change it back into a robot again.

Converting a Transformer is very similar to the shoes-and-socks method of finding an inverse function that we introduced in [Section 1.5](//chapter-1/1.5).  Unfortunately, that technique seldom works on combined functions.  In this section we develop a new procedure that can be applied to any function.

## Review the Shoes and Socks Method
Let's review the shoes-and-socks method for finding an inverse.  We'll use $f(x)=\frac{x^{3}+1}{5}$ as an example.  The first step in the process was to identify the operations performed by the function, following the standard order of operations.  The next step was to list the inverse operations in the reverse order.

|| Operations Performed by the Function || Operations Performed by the Inverse |
| --- | --- | --- | --- |
| 1. | Cube |  1.  | Multiply by $5$ |
| 2. | Add $1$ | 2. | Subtract $1$ |
| 3. | Divide by $5$ | 3. | Cube root |

Since the list on the right describes exactly what the inverse function does, we use it to build the equation for $f^{-1}$.  This is the final step.

\begin{align}
\small \color{#5fa2ce}{\text{Start with an $x$:}} &&& x \newline
\small \color{#5fa2ce}{\text{Multiply by $5$:}} &&& 5x \newline
\small \color{#5fa2ce}{\text{Subtract $1$:}} &&& 5x - 1 \newline
\small \color{#5fa2ce}{\text{Cube root:}} &&& \sqrt[3]{5x-1} \newline
\small \color{#5fa2ce}{\text{Write as a function:}} && f^{-1}(x) &= \sqrt[3]{5x-1}  
\end{align}


{{% check %}}
Use this shoes-and-socks method to find the inverse of $g(x)=2x-7$. {{% answer %}}$g^{-1}(x)=\frac{x+7}{2}${{% /answer %}}
{{% /check %}}


## Review Graphing Inverses
Now consider a function such as $f(x)=\frac{x-5}{x-4}$ where $x$ appears more than once in the equation.  Since we cannot determine what happens to $x$ first, we cannot establish an order of operations and cannot use the shoes-and-socks method, despite the fact that this function is indeed one-to-one.

We can, however, find the graph of $f^{-1}(x)$ by reflecting points on the graph of $f(x)$ around the line $y=x$, as in the figure below (move the <font color="blue">blue</font> slider to see the reflection).

{{% geogebra ratio="50%" id_1="cQPv8NFYS7hVyGck" id_2="izzOv7Yo" id_m="izzOv7Yo" %}}

Notice that each point $\color{red}{(x, y)}$ on the graph of $f$ turns into the point $\color{black}{(y, x)}$ on the graph of the inverse.  This may not seem like a significant fact, but it is the key to a new algebraic method for finding the equations of inverses.


## Learn the Switch and Solve Method
We have seen that if $(x, y)$ is a point on the graph of a one-to-one function $f$, then the point $(y, x)$ is on the graph of $f^{-1}$.  The significance of this is that switching $x$ and $y$ in the equation of a one-to-one function creates an implicit equation for its inverse.  All that remains is to solve that equation for $y$ so that we can write it with function notation.   For obvious reasons, this will be called the **switch-and-solve** method.

The **switch-and-solve** method can be broken down into a four-step process.

$$
  \begin{align}
    \text{Step 1:} &&& \small \color{#5fa2ce}{\text{Replace $f(x)$ with $y$}} \newline
    \text{Step 2:} &&& \small \color{#5fa2ce}{\text{Switch $x$ and $y$}} \newline
    \text{Step 3:} &&& \small \color{#5fa2ce}{\text{Solve for $y$}} \newline
    \text{Step 4:} &&& \small \color{#5fa2ce}{\text{Replace $y$ with $f^{-1}(x)$}}
    \end{align}
$$

We will illustrate this process by returning to the same function $f(x)=\frac{x^{3}+1}{5}$ that we used earlier with the shoes-and-socks method.

**$\text{Step 1: } \small \color{#5fa2ce}{\text{ Replace $f(x)$ with $y$. }}$**  
To find the inverse using the switch-and-solve method we start by rewriting the function as an equation with $y$ in place of $f(x)$.  

$$
  y=\frac{x^{3}+1}{5}
$$

**$\text{Step 2: } \small \color{#5fa2ce}{\text{ Switch $x$ and $y$. }}$**  
Then we turn every $x$ into a $y$ and vice versa.

$$
  x = \frac{y^{3}+1}{5}
$$

**$\text{Step 3: } \small \color{#5fa2ce}{\text{ Solve for $y$. }}$**  
The next step is to solve this equation for $y$.

$$
  \begin{align}
    5x &= y^{3}+1 && \small \color{#5fa2ce}{\text{Multiply both sides by $5$}} \newline
    5x-1 &= y^{3} && \small \color{#5fa2ce}{\text{Subtract $1$ from both sides}} \newline
    \sqrt[3]{5x-1} &= y && \small \color{#5fa2ce}{\text{Take the cube root}}
  \end{align}
$$

**$\text{Step 4: } \small \color{#5fa2ce}{\text{ Replace $y$ with $f^{-1}(x)$. }}$**<br>
Lastly we rewrite this equation using inverse function notation.

$$
  f^{-1}(x) = \sqrt[3]{5x-1}
$$

Notice that this is the same answer we obtained earlier with the shoes-and-socks method and that the steps needed to solve for $y$ are exactly the steps listed in the shoes-and-socks method.


## Use the Switch and Solve Method
Since there are several solving techniques that may arise when doing the switch-and-solve method, we will explore a few more examples before looking at functions with more than one $x$.

### Example 1
Here we will find the inverse of $f(x)=e^x-2$.  Since this is an exponential function, after we switch variables we should expect the solving process to involve the natural logarithm.

$$
  \begin{align}
    f(x) &= e^x-2 && \small \color{#5fa2ce}{\text{Original function}} \newline
    y &= e^x-2 && \small \color{#5fa2ce}{\text{Replace $f(x)$ with $y$}} \newline
    x &= e^y-2 && \small \color{#5fa2ce}{\text{Swap $x$ and $y$}} \newline
    x + 2 &= e^y && \small \color{#5fa2ce}{\text{Add $2$}} \newline
    \ln(x+2) &=  \ln\left(e^y\right) && \small \color{#5fa2ce}{\text{Apply $\ln$ to both sides}} \newline
    \ln(x+2) &= y && \small \color{#5fa2ce}{\text{Simplify}} \newline
    f^{-1}(x) &= \ln(x+2) && \small \color{#5fa2ce}{\text{Replace $y$ with $f^{-1}(x)$}}
  \end{align}
$$

We now know that the inverse of $f(x)=e^x-2$ is $f^{-1}(x)=\ln(x+2)$.

### Example 2
In this next example we will use the switch-and-solve method to find the inverse of $f(x)=-5x+8$.  The solving steps do not involve anything beyond basic inverse operations.  Please try each step on your own and then check your answer.

$\text{Step 1: } \small \color{#5fa2ce}{\text{ Replace $f(x)$ with $y$. }}$ {{% answer %}}$$y=-5x+8$${{% /answer %}}

$\text{Step 2: } \small \color{#5fa2ce}{\text{ Switch $x$ and $y$. }}$ {{% answer %}}$$x=-5y+8$${{% /answer %}}

$\text{Step 3: } \small \color{#5fa2ce}{\text{ Solve for $y$. }}$ {{% answer %}}  \begin{align} x&=-5y+8 \newline
x-8 &= -5y && \small \color{#5fa2ce} {\text{subtract 8}} \newline
\frac{x-8}{-5}&=y && \small \color{#5fa2ce} {\text{divide by -5}}\end{align}{{% /answer %}}

$\text{Step 4: } \small \color{#5fa2ce}{\text{ Replace $y$ with $f^{-1}(x)$. }}$ {{% answer %}}$$f^{-1}(x)=\frac{x-8}{-5}$${{% /answer %}}


### Example 3
Now let's look at a power function $f(x)=x^{2/3}+6$ and restrict its domain $x\leq0$ so that it is one-to-one.  The steps below outline the complete process for finding the equation for $f^{-1}$.

$$
  \begin{align}
    f(x) &= x^{2/3}+6 && \small \color{#5fa2ce} {\text{Original function}} \newline
    y &= x^{2/3}+6 && \small \color{#5fa2ce} {\text{Replace $f(x)$ with $y$}} \newline
    x &= y^{2/3}+6 && \small \color{#5fa2ce} {\text{Switch $x$ and $y$}} \newline
    x-6 &= y^{2/3} && \small \color{#5fa2ce} {\text{Subtract $6$}} \newline
    (x-6)^{3} &= y^{2} && \small \color{#5fa2ce} {\text{Apply the 3rd power}} \newline
    \pm\sqrt{(x-6)^{3}} &= y && \small \color{#5fa2ce} {\text{Apply the square root}} \newline
    y &= \pm(x-6)^{3/2} && \small \color{#5fa2ce} {\text{Rewrite}} \newline
  \end{align}
$$

We now face a choice, should we pick $(x-6)^{3/2}$ or $-(x-6)^{3/2}$ as the inverse?  

Since the inputs and outputs of a function and its inverse should switch places, comparing the domain and range of our original function against these two options should point us to the correct choice.

Both of our options have a domain of $x\geq6$, matching the range of $f$, but only $-(x-6)^{3/2}$ has a range that matches the domain of $f$, making it the correct choice for $f^{-1}$.

Another way to see this is to look at the graphs.  The graphs of $f$ and $f^{-1}$ must be symmetric across the line $y=x$.  In this case, our function has a y-intercept at $(0,6)$, so the inverse must have an x-intercept at $(6,0)$.

![](/img/chapter-4/inverse_x_pow_2_3+6.svg#center)

The takeaway is that whenever the equation for $f^{-1}$ is not one-to-one, as it was in this example, we need to look closely at the graph of the function and its domain and range to help us choose the correct inverse.

{{% check %}}
1.  Suppose the *domain* of a one-to-one function $f$ is known to be $[3, 18]$.  What is the *range* of $f^{-1}$? {{% answer %}}The range of $f^{-1}$ would have to be $[3,18]$.{{% /answer %}}
1.  Suppose the point $(-2,5)$ is on the graph of a one-to-one function. Which point must be on the graph of the inverse function? {{% answer %}}The point $(5,-2)$ must be on the graph of the inverse.{{% /answer %}}
{{% /check %}}


## Inverses of Combined Functions
Let's return to the function $f(x)=\frac{x-5}{x-4}$ which we graphed earlier.  Since $x$ occurs more than once, the switch-and-solve method is the best way to find the inverse.   Here are all of the steps.

$$
  \begin{align}
    f(x) &= \frac{x-5}{x-4} && \small \color{#5fa2ce} {\text{Original function}} \newline
    y &= \frac{x-5}{x-4} && \small \color{#5fa2ce} {\text{Replace $f(x)$ with $y$}} \newline
    x &= \frac{y-5}{y-4} && \small \color{#5fa2ce} {\text{Switch $x$ and $y$}} \newline
    x(y-4) &= y-5 && \small \color{#5fa2ce} {\text{Multiply by $y-4$}} \newline
    xy-4x &= y-5 && \small \color{#5fa2ce} {\text{Distribute $x$}} \newline
    xy-4x -y &= -5 && \small \color{#5fa2ce} {\text{Subtract $y$}} \newline
    xy-y &= 4x-5 && \small \color{#5fa2ce} {\text{Add $4x$}} \newline
    y(x-1) &= 4x-5 && \small \color{#5fa2ce} {\text{Factor out $y$}} \newline
    y &= \frac{4x-5}{x-1} && \small \color{#5fa2ce} {\text{Divide by $x-1$}} \newline
    f^{-1}(x) &= \frac{4x-5}{x-1} && \small \color{#5fa2ce}{\text{Replace $y$ with $f^{-1}(x)$}}
  \end{align}
$$

Using function notation, we can now say that $f^{-1}=\frac{4x-5}{x-1}$ is the inverse of $f(x)=\frac{x-5}{x-4}$.

As you can see, finding a formula for an inverse function can be very difficult.  In fact, sometimes it is impossible.  For example, to find the inverse of $f(x)=xe^{x}$, $x\geq0$ we would need to solve $x=ye^y$ for $y$.

$$
  \begin{align}
    x &= ye^y && \small \color{#5fa2ce} {\text{Original equation}} \newline
    \frac{x}{y} &= e^y && \small \color{#5fa2ce} {\text{Divide by } y} \newline
    \ln\left(\frac{x}{y}\right) &= y && \small \color{#5fa2ce} {\text{Apply the natural logarithm}}
  \end{align}
$$

By removing the exponential we've freed up one $y$, but the other $y$ is now stuck inside of the logarithm.  If we were to free the $y$ inside of the logarithm, then the other $y$ would be trapped back in an exponential.  It's a loop we could never get out of.


## Verify Inverse Functions
![](/img/chapter-1/tahiti_flight.png#center)
You'll remember that in [Section 1.5](//chapter-1/1.5) we introduced the idea that a function combined with its inverse should act like a round trip airplane flight, bringing you back to where you started.  Now that we understand composition, we can state this rule more precisely.

Given a one-to-one function $f$ and its inverse $f^{-1}$, the following round trip properties hold

$$
  (f \circ f^{-1})(x)=f(f^{-1}(x))=x
$$

for all the $x$ in the domain of $f^{-1}$ and

$$
  (f^{-1} \circ f)(x)=f^{-1}(f(x))=x
$$

for all the $x$ in the domain of $f$.  In other words, a function and its inverse should cancel each other, no matter which way they are composed together.

These properties are only true for inverse functions.  As a consequence, they can be used to verify that two functions are inverses.

Earlier, in [Example 2](./#example-2), we found that the inverse of $\color{red}{f(x)=-5x+8}$  was $\color{blue}{f^{-1}(x)=\frac{x-8}{-5}}$.  Let's use the round trip properties to verify that these are indeed inverses.  

First we'll check to see that $(f \circ f^{-1})(x) = x$.

$$
  \begin{align}
    (f \circ f^{-1})(x) &= \color{red}{f \left( \color{blue}{f^{-1}(x)} \right) } &&  \small \color{#5fa2ce} {\text{Definition of composition}} \newline
    &= \color{red}{f \left( \color{blue}{\frac{x-8}{-5}} \right) } &&  \small \color{#5fa2ce} {\text{Use equation for } f^{-1}(x)} \newline
    &= \color{red}{-5 \left( \color{blue}{\frac{x-8}{-5}} \right) +8} &&  \small \color{#5fa2ce} {\text{Use equation for } f(x)} \newline
    &= \color{red}{ \left( \color{blue}{x-8} \right) +8} &&  \small \color{#5fa2ce} {\text{Multiplication and division cancel}} \newline
    &= x &&  \small \color{#5fa2ce} {\text{Simplify}}
  \end{align}
$$

We also need to check composition in the other direction to see if $(f^{-1} \circ f)(x) = x$.

$$
  \begin{align}
    (f^{-1} \circ f)(x) &= \color{blue}{f^{-1} \left( \color{red}{f(x)} \right) } &&  \small \color{#5fa2ce} {\text{Definition of composition}} \newline
    &= \color{blue}{f^{-1} \left( \color{red}{-5x + 8} \right) } &&  \small \color{#5fa2ce} {\text{Use equation for } f(x)} \newline
    &= \color{blue}{\frac{\color{red}{(-5x + 8)} -8}{-5}} &&  \small \color{#5fa2ce} {\text{Use equation for } f^{-1}(x)} \newline
    &= \color{blue}{\frac{\color{red}{-5x}}{-5}} &&  \small \color{#5fa2ce} {\text{Cancel +8 and -8}} \newline
    &= x &&  \small \color{#5fa2ce} {\text{Simplify}}
  \end{align}
$$

Since both round trip properties hold, we have verified that these two functions are truly inverses of each other.

{{% check %}}
Are the functions $\color{red}{f(x)=\frac{x}{2}+3}$ and $\color{blue}{g(x)=2x-3}$ inverses?  Use the round trip properties to justify your answer. {{% answer %}}No, these are not inverses.  $$(f \circ g)(x)=\color{red}{ \frac{ \color{blue}{2x-3}}{2} + 3 } = x + \frac{3}{2}$$ and $$(g \circ f)(x) = \color{blue}{2\left(\color{red}{\frac{x}{2}+3}\right)-3}=x+3$$  Neither of these equal $x$, so the functions cannot be inverses.{{% /answer %}}
{{% /check %}}


## Applications of Inverses
{{% imgcap file="/img/chapter-1/LMGould.jpg" title="Photo by Bob DeValentino of the NSF" source="https://photolibrary.usap.gov/#1-1" %}}
One of the main jobs of the ship L.M. Gould  is to pick up containers of food and supplies from Punta Arenas, Chile, and deliver them to the scientists working at Palmer Station in Antarctica.

Suppose the amount of food, in pounds, that the station has on hand $x$ days after being re-supplied is given by $f(x)=11200-200x$.  The inverse of this function is

$$
  \begin{align}
    f(x) &= 11200-200x && \small \color{#5fa2ce} {\text{Original function}} \newline
    y &= 11200-200x && \small \color{#5fa2ce} {\text{Replace $f(x)$ with $y$}} \newline
    x &= 11200-200y && \small \color{#5fa2ce} {\text{Switch $x$ and $y$}} \newline
    y &= \frac{x - 11200}{-200} && \small \color{#5fa2ce} {\text{Solve for $y$}} \newline
    f^{-1}(x) &= \frac{x - 11200}{-200} && \small \color{#5fa2ce}{\text{Replace $y$ with $f^{-1}(x)$}}
  \end{align}
$$

But how should we interpret the inverse, what would it mean in this situation?  Our new switch-and-solve method not only gives the equation for the inverse, but can also help us see the context of the inverse as well.  

The key is to recognize that the inputs and outputs are trading places.  If the original function computes pounds of food based on the number of days since the supply ship arrived, then the inverse would allow the scientists to calculate how long it has been since the ship last visited by measuring the amount of food available.

{{% check %}}
Evaluate $f^{-1}(1000)$ and describe what it would mean to the scientists in Antarctica. {{% answer %}}
$$f^{-1}(1000) = \frac{1000-11200}{-200} = 51$$
This means that when the scientists have $1000$ pounds of food left, they will know that the supply ship came 51 days ago.
{{% /answer %}}
{{% /check %}}


## Looking Ahead
In this chapter we've seen how to make new, more complicated functions by combining simple functions through the operations of function addition, subtraction, multiplication, division and composition.

We have also seen that as the functions become more complicated, their inverses, if they exist, are difficult or even impossible to find.

In the [next chapter](/chapter-5/) we will focus on the properties of polynomial and rational functions.  Since their equations involve several terms and are not in general one-to-one, we will not spend time finding their inverses.
---
title: "5.1 Graphs of Polynomials"
description:
author: "Nolan Mitchell"
type: page
image: "al-jabr.jpg"
draft: false
tags: ["graphs-of-polynomials", "standard-form", "polynomial-terms", "degree", "leading-coefficient", "constant-term", "end-behavior", "even-degree", "odd-degree", "positive-leading-coefficient", "negative-leading-coefficient", "turning-points", "minimum-degree-from-graph", "y-intercept", "real-zeros", "x-intercepts", "factor-theorem", "multiple-zeros", "multiplicity", "determining-polynomial-from-graph", "imaginary-zeros", "al-khwarizmi"]
---

{{% imgcap file="/img/chapter-5/al-jabr.jpg" title="Statue of Al-KhwÄrizmÄ« in his birth town Khiva, Uzbekistan. Photo by Yunuskhuja Tuygunkhujaev on Wikipedia" source="https://en.wikipedia.org/wiki/Muhammad_ibn_Musa_al-Khwarizmi#/media/File:Khiva.jpg" %}}

## Introduction
Polynomials have intrigued mathematicians for centuries.  Ancient Egyptian, Babylonian, and Greek mathematicians all studied simple polynomials.

The Chinese are known to have worked with cubics in the early 7th century, at the same time mathematicians in India were busy creating the [quadratic formula](/img/chapter-5/quadratic_formula.svg).

Two centuries later the Persian mathematician al-KhwÄrizmÄ« introduced the world to â€œal-jabrâ€, or â€œalgebraâ€, as a process for solving polynomial equations.

During the Renaissance polynomials spread throughout western Europe and contests were held to see who could solve the hardest polynomial problem.  

As we explore the properties and behaviors of polynomial functions in this chapter you might begin to see why they have been able to hold the attention of great minds throughout history.


## Standard Form of a Polynomial
One attractive feature of polynomial functions is the simplicity of their equations.  In [Chapter 4](//chapter-4/4.1#polynomials) you learned that polynomials are sums of power functions with non-negative integer powers.  

For example, the polynomial $p(x)=5x^{3}+7x^{2}-4x+8$ is a sum of the four power functions $5x^{3}$, &nbsp; $7x^{2}$, &nbsp; $-4x$ &nbsp; and &nbsp; $8$.

Each power function is called a **term** of the polynomial.  The highest power is called the **degree** of the polynomial, and the coefficient of that term is called the **leading coefficient**.  The term without an $x$ is referred to as the **constant term**.

![](/img/chapter-5/polynomial_terms.svg#center)

It is standard to write a polynomial so that the powers are in descending order.

{{% check %}}
1.  Rewrite the polynomial $p(x)=6x-4x^{2}+15$ in standard form, with the powers in descending order.  Then identify the degree, leading coefficient and constant term. {{% answer %}}In standard form the polynomial is $p(x)=-4x^{2}+6x+15$.  Degree is $2$, the leading coefficient is $-4$ and the constant term is $15$.{{% /answer %}}
{{% /check %}}


## End Behavior of Polynomials
It's important to be able to identify the degree and leading coefficient of a polynomial because they influence the overall shape of its graph.

### Even vs Odd Degrees
Since degrees of polynomials are always whole numbers, the degree must either be an even number or an odd number. The ends of polynomials with even degrees behave differently than those with odd degrees.  

To investigate this, random polynomials with different degrees are shown in the figure below.  As you switch from one to another, try to decide how even degree polynomials are different from odd degree polynomials.  In particular, pay attention to the <font color="red">end behavior</font> of the graphs.

{{% geogebra ratio="40%" id_1="dijK8osMnd0mJq4S" id_2="kcvhpeer" id_m="d5gxgxxc" %}}

When a polynomial has an even degree, both ends of its graph will point in the same direction and it will look somewhat similar to a parabola.  When the degree is odd, however, one end will go up while the other goes down, just like a line.  

{{% check %}}
1.  Without graphing, describe the end behavior of $p(x)=2x^5-3x^2+4$  Do the ends of the graph both point in the same direction or do they point in opposite directions? {{% answer %}}The degree is $5$, which is an odd number, so the ends of the graph will point in opposite directions.{{% /answer %}}
1.  Without graphing, describe the end behavior of $p(x)=x^4+2x-7$  Do the ends of the graph both point in the same direction or do they point in opposite directions? {{% answer %}}The degree is $4$, which is an even number, so the ends of the graph will both point in the same direction.{{% /answer %}}
{{% /check %}}

### Positive vs Negative Leading Coefficients
The leading coefficient of a polynomial can change the direction of the graph, depending on if it is positive or negative.  In this figure you can change the sign of the leading coefficient for several polynomials.  

{{% geogebra ratio="40%" id_1="OmmHWEiVVwMnQmRB" id_2="sayexky8" id_m="umnevpzw" %}}

If the degree is even then the graph mimics the behavior of a parabola, with both ends pointing up when the leading coefficient is positive and down when it is negative.

If the degree is odd then the graph behaves like a line, pointing up to the right when the leading coefficient is positive and pointing down when the leading coefficient is negative.  This mirrors the behavior of a line with positive or negative slope.

{{% check %}}
1. Without graphing, describe the end behavior of $p(x)=-2x^6-3x^5+9$. {{% answer %}}The degree is $6$, which is an even number and the leading coefficient is negative.  So both ends of this polynomial will point down.{{% /answer %}}
1. Without graphing, describe the end behavior of $p(x)=-3x^5+x^4-7x^{3}+5x-6$. {{% answer %}}Since the degree is an odd number, and the leading coefficient is negative, the left end of the graph will point up while the right end points down.{{% /answer %}}   
{{% /check %}}


Since the end behavior of a polynomial depends only on the degree and the leading coefficient, in the long run its graph will look like the graph of its leading term.

In this figure you can zoom out on the graphs of $\color{red}{p(x)=\frac{1}{2}x^4-2x^{2}+x+1}$ and $\color{black}{f(x)=\frac{1}{2}x^4}$.

{{% geogebra ratio="40%" id_1="qcCwgLkxu1fSPGfm" id_2="vsnxmmcg" id_m="wxpddg2b" %}}

We can see that the graph of $\color{red}{p(x)=\frac{1}{2}x^4-2x^{2}+x+1}$ is nearly identical to the graph of the power function $\color{black}{f(x)=\frac{1}{2}x^4}$ as we zoom out, even though they are very different for small values of $x$.

In general, any polynomial will eventually behave like the power function $ax^n$, where $a$ is the leading coefficient and $n$ is the degree of the polynomial.


### Determine Degree & Leading Coefficient from a Graph
Knowing how the end behavior is connected to the degree and leading coefficient allows us draw conclusions about the equation of a polynomial simply by observing its graph.  Specifically, we know that

* If both ends point in the same direction, then the degree is even.
* If one end is up while the other is down, then the degree is odd.
* If the right end points up, then the leading coefficient is positive.
* If the right end points down, then the leading coefficient is negative.

{{% check %}}
For each graph, decide if the degree of the polynomial is even or odd.  Also state whether the leading coefficient is positive or negative.

1.  &nbsp;![](/img/chapter-5/poly_graph_QC1.svg#center) {{% answer %}}Since both ends of the graph point up, this polynomial must have an even degree and a positive leading coefficient.{{% /answer %}}
1.  &nbsp;![](/img/chapter-5/poly_graph_QC2.svg#center) {{% answer %}}Since the right end points up but the left side points down, this has an odd degree with a positive leading coefficient.{{% /answer %}}
1.  &nbsp;![](/img/chapter-5/poly_graph_QC3.svg#center) {{% answer %}}Odd degree.  Negative leading coefficient.{{% /answer %}}
1.  &nbsp;![](/img/chapter-5/poly_graph_QC4.svg#center) {{% answer %}}Even degree.  Negative leading coefficient.{{% /answer %}}
{{% /check %}}


## Turning Points
Another thing that makes polynomials useful is their ability to change direction.  The point where a polynomial changes from increasing to decreasing, or vice versa, is known as a **turning point**.  Turning points are always local maximums or local minimums.

![](/img/chapter-5/poly_turns_a.svg#center)

The number of turning points is related to the degree of the polynomial.  Look again at the graphs above. Can you spot a connection between the degree and the number of turns?

From the graphs it would seem that the number of turns is always one less than the degree, since the 2nd degree polynomial had 1 turn, the 3rd degree had 2 turns, and the 4th degree had 3 turning points.

Unfortunately, that's not always true.  Take a look at the three graphs below.

![](/img/chapter-5/poly_turns_b.svg#center)

All three are 5th degree polynomials but each graph has a different number of turns.  It seems that a 5th degree polynomial can have 4 turns, but it could also have less than 4.

A good way to describe this is to say that the *maximum* number of turning points is always one less than the degree.

{{% check %}}
1. How many turns can a 6th degree polynomial have? {{% answer %}}Since the degree is 6, it can have at most 5 turning points.{{% /answer %}}
1. How many turns can a 3rd degree polynomial have? {{% answer %}}Since the degree is 3, it can have at most 2 turning points.{{% /answer %}}
{{% /check %}}


## Find the Minimum Degree from a Graph
Since we can find the maximum number of turns by looking at the equation, we should also be able to do the reverse:  find the minimum degree by looking at the graph.  This is done by counting the number of turns and adding 1.

As an example, consider the following polynomial.

![](/img/chapter-5/poly_turns_7.svg#center)

Since the graph has 3 turning points, the degree of the polynomial must be *at least* 4.  The degree could be higher, but it must be *at least* 4.

We actually know a little more than that.  Since both ends point in the same direction, the degree must be even.  So the actual degree could be any *even* degree of 4 or higher.  It cannot, for instance, be a 5th degree polynomial.

{{% check %}}
State the number of turning points and the minimum degree of each graph.

1. &nbsp; ![](/img/chapter-5/poly_turns_8.svg#center) {{% answer %}}There are 4 turning points, so the degree must be at least 5.{{% /answer %}}
1. &nbsp; ![](/img/chapter-5/poly_turns_9.svg#center) {{% answer %}}The degree is at least 7, since there are 6 turning points.{{% /answer %}}
1. &nbsp; ![](/img/chapter-5/poly_turns_10.svg#center) {{% answer %}}Only one turning point, so the degree must be at least 2.{{% /answer %}}
{{% /check %}}


## Constant Term
The behaviors we have investigated so far were connected to the degree and the leading coefficient of the polynomial.  Next we will look at how the constant term affects a polynomial's graph.

In the interactive figure below you can adjust the value of the constant term in a 3rd degree polynomial.  Look for a connection between the constant term and the graph.  Make a note of your observations before continuing.

{{% geogebra ratio="40%" id_1="JjYN8PiVptUupCYe" id_2="s33ajp8m" id_m="mmu4fvmg" %}}

You should have found that the constant term of a polynomial is the value of y-intercept of the graph.  The reason for this is simple.

Recall that the y-intercept of any function occurs when $x=0$.  Replacing $x$ with $0$ will eliminate every term containing a power of $x$, leaving just the constant term.

Take $p(x)=-4x^7+6x^4-18x^{2}+9$ as an example.  If we evaluate $p(0)$ we find

\[p(0)=-4(0)^7+6(0)^4-18(0)^2+9=9\]

which verifies that the y-intercept is $y=9$, exactly the same value as the constant term.

{{% check %}}
1.  What is the value of the y-intercept of the polynomial $p(x)=-5x^{2}+9x-4$? {{% answer %}}Since the constant term is $-4$, the y-intercept is $y=-4$.{{% /answer %}}
{{% /check %}}


## Real Zeros of Polynomials
While it is easy to see the y-intercept from the standard equation of a polynomial, finding the x-intercepts is much more challenging.  

However, if the polynomial has been factored{{% sidenote "factoring" %}}Factoring is the process of breaking a polynomial into simpler pieces which, when multiplied together, are the same as the original polynomial.  For instance, $(x+2)(x+3)$ is the factored form of $x^{2}+5x+6$.{{% /sidenote %}}, then finding the x-intercepts is simple.

### The Factor Theorem
In the interactive figure below, you can change the location of the x-intercepts.  As you do so, pay attention to how the factored equation changes.  

{{% geogebra ratio="50%" id_1="OnJrwBBvCMm6r0oN" id_2="EyHYBvpj" id_m="EyHYBvpj" %}}

You probably noticed that there is a factor for each x-intercept.  The reason for this is that x-intercepts are real number solutions to $p(x)=0$.  And if $(x-c)$ is a factor, then $x=c$ will cause the entire function to equal zero.  In fact, x-intercepts are often called **real zeros** for this very reason.

In general, $p(c)=0$ if and only if $(x-c)$ is a factor of the polynomial.  In other words, knowing that $(x-c)$ is a factor tells us that $x=c$ is a zero. The reverse is also true.  If $x=c$ is a zero then $(x-c)$ is a factor.  This is known as the **factor theorem**.  

With the factor theorem we can quickly find the x-intercepts of any factored polynomial.  For instance, if $p(x)=(x-3)(x+6)(x+15)$, then the x-intercepts are $x=3$, $x=-6$, and $x=-15$.

{{% check %}}
1. What are the x-intercepts of $p(x)=(x-2)(x+4)(x-1)$? {{% answer %}}The x-intercepts are the real zeros $x=2$, $x=-4$ and $x=1$.{{% /answer %}}
1. Find the x-intercepts of $p(x)=(x)(x-7)(x+3)$. {{% answer %}}The x-intercepts are the real zeros $x=0$, $x=7$ and $x=-3$.{{% /answer %}}
{{% /check %}}


### Multiple Zeros
Consider a polynomial such as $f(x)=(x-2)(x-2)$.  The factor theorem tells us that this polynomial has real zeros at $x=2$ and $x=2$.  But what does it mean for a polynomial to have two zeros with the same value?  Can it have more than one x-intercept at $x=2$?

The figure below will help answer this question.  You are free to move the real zeros (**<font color="blue">blue points</font>**) anywhere you want. Look for a change in the shape of the graph and a corresponding change in the equation when multiple zeros are put in the same spot.

{{% geogebra ratio="45%" id_1="CdxLlYEgwcn28D5r" id_2="jupSjhUq" id_m="jupSjhUq" %}}

Putting multiple zeros in the same spot creates a factor of the form $(x-c)^m$ where the power $m$ corresponds to the number of zeros.  If the multiplicity of the zero is odd, then the graph crosses the x-axis.  If the multiplicity is even, then the graph does not cross the x-axis but instead just touches it and then bounces off.  

{{% check %}}
Identify the zeros of the polynomial and state whether their multiplicities are even or odd.
![](/img/chapter-5/multiple_zero_qc1.svg#center)
{{% answer %}}
* The zero at $x=-2$ has an odd multiplicity.
* The zero at $x=0$ has an even multiplicity.
* The zero at $x=3$ has an odd multiplicity.
{{% /answer %}}
{{% /check %}}


## Determine Polynomial Functions from a Graph
We have now arrived at a point where we can create an equation for a polynomial simply by analyzing its graph.  To see how this might work, let's start with this graph.

![](/img/chapter-5/find_poly_equation_1.svg#center)

Since the graph has just one turn and both ends point upward, we expect the equation to be at least a 2nd degree polynomial with a positive leading coefficient.  It should also have a constant term of $-2$, since the y-intercept is at $(0, -2)$.

In addition, the zeros at $x=-2$ and $x=1$ tell us that $(x+2)$ and $(x-1)$ must be factors.  This suggests that the equation might be $p(x)=(x+2)(x-1)=x^{2}+x-2$.

This equation meets all of the expectations we had above;  it is a 2nd degree polynomial with a positive leading coefficient and the y-intercept is at $-2$.  Graphing this equation on a calculator
![](/img/chapter-5/poly_calculator_1.png#center)
shows that it does have the right shape.

{{% check %}}
Find an equation for a polynomial that has zeros at $x=5$ and $x=-1$. {{% answer %}}The polynomial $p(x)=a(x-5)(x+1)$ would work for any leading coefficient $a$.{{% /answer %}}  
{{% /check %}}

Let's try a few more examples, starting with the graph below.  

![](/img/chapter-5/find_poly_equation_2.svg#center)

We can see 2 turning points which suggests that the degree is at least 3.  We also know that the leading coefficient is negative and the y-intercept is $(0, 2)$.

The graph has real zeros at $x=-1$, $x=-2$ and $x=3$, which means $(x+1)$, $(x+2)$ and $(x-3)$ must be factors, so one possible equation is

\[p(x) = (x + 1) (x + 2) (x - 3)\]

To see if this is a good fit we'll expand the equation and check its leading coefficient and y-intercept.

\[
\begin{align}
p(x) &= (x + 1) (x + 2) (x - 3) && \newline
 &= (x+1)(x^{2}-3x+2x-6) && \text{multiply} (x+2)(x-3) \newline
 &= (x+1)(x^{2}-x-6) && \text{combine} -3x+2x \newline
 &= (x^{3}-x^{2}-6x+x^{2}-x-6) && \text{distribute} (x+1) \newline
 &= x^{3}-7x-6 && \text{simplify}
\end{align}
\]

The leading coefficient is positive and, since the constant term is $-6$, this function has a y-intercept at $(0, -6)$.  Since neither of these matches our graph, we'll need to find a way to change both without altering the real zeros.

We can change both the leading coefficient and the y-intercept if we multiply it by a constant $a$, making the equation $p(x)=a(x^{3}-7x-6)$.  Remember, multiplying a function by a constant vertically stretches and/or flips the graph, it doesn't change the x-intercepts or zeros.  

Since we want to have a y-intercept of $2$, the trick will be to find $a$ when $\color{red}{p(0)=2}$.

\[
\begin{align}
p(x) &= a(x^{3}-7x-6) && \newline
p(0) &= a((0)^3-7(0)-6) && \text{replace each } x \text{ with } 0 \newline
p(0) &= -6a && \text{simplify} \newline
\color{red}{2} &= -6a && \text{since } \color{red}{p(0)=2} \newline
-\frac{1}{3} &= a && \text{divide by } -6
\end{align}
\]

This gives us $p(x)=-\frac{1}{3}(x^{3}-7x-6)=-\frac{1}{3}x^{3}+\frac{7}{3}x+2$, which has all the properties (zeros, degree, leading coefficient, and y-intercept) of the graph we were trying to match.  Plotting this new equation on a calculator

![](/img/chapter-5/poly_calculator_2.png#center)

shows that it is, indeed, a good fit.

{{% check %}}
1.  Find the equation for a polynomial with zeros at $x=2$ and $x=-4$ and a y-intercept of $(0, 16)$.
![](/img/chapter-5/poly_equation_qc_1.svg#center) {{% answer %}}The function is \[p(x)=\color{red}{-2}\color{blue}{(x-2)}\color{green}{(x+4)}\] To find this first note that the zeros $\color{blue}{x=2}$ and $\color{green}{x=-4}$ give the factors $\color{blue}{(x-2)}\color{green}{(x+4)}$.  <br><br> For $\color{red}{a}$ remember that the y-intercept is $(0, 16)$ so $p(0)=16$.  The steps for solving for $\color{red}{a}$ follow
\[
\begin{align}
p(x) &= a(x-2)(x+4) \newline
p(0) &= a(0-2)(0+4) \newline
16 &=-8a \newline
\color{red}{-2 } & \color{red}{ = a}
\end{align}
\]
{{% /answer %}}
{{% /check %}}


As our final example consider this graph.

![](/img/chapter-5/find_poly_equation_3.svg#center)

This graph appears to have a single zero at $x=0$, a multiple zero with even multiplicity at $x=-1$, and a multiple zero with odd multiplicity at $x=2$.  

When faced with graphs that have multiple zeros we will choose the lowest power possible unless directed otherwise.  Thus we start with the equation

\[ p(x)=a(x)(x+1)^2(x-2)^3 \]

To find $a$ we need another point on the graph.  Note that the point $(1, 2)$ is on the graph, so $p(1)=2$ which will help us solve for $a$.

\[
\begin{align}
p(x) &= a(x)(x+1)^2(x-2)^3 \newline
p(1) &= a(1)(1+1)^2(1-2)^3 && \text{Replace each } x \text{ with } 1 \newline
2 &= -4a && \text{since } p(1)=2 \newline
-\frac{1}{2} &= a && \text{divide by }-4
\end{align}
\]


Using $a=-\frac{1}{2}$ we arrive at the equation $p(x)=-\frac{1}{2}(x+1)^2(x)(x-2)^3$.  Checking this on a graphing calculator

![](/img/chapter-5/poly_calculator_3.png#center)

shows that we have found a good match.

{{% check %}}
1.   Find an equation for the polynomial shown below.
![](/img/chapter-5/poly_equation_qc_2.svg#center)
{{% answer %}}$p(x) = \frac{1}{4}(x + 2)^2(x - 1)$ fits nicely.{{% /answer %}}
{{% /check %}}


## Looking Ahead
We should point out that this process of finding the factored equation of a polynomial from a graph only works if the number of real zeros equals the degree.

As a case in point, look at the graph below.

![](/img/chapter-5/find_poly_equation_4.svg#center)

There is only one real zero, $x=-2$, implying that the equation only has one factor $(x+2)$ and is the first degree polynomial $p(x)=x+2$.  

But we can clearly see 2 turning points!  Since a first degree polynomial cannot have 2 turning points, there must be more to this polynomial than meets the eye.

What we can't see are the zeros that are imaginary numbers.  While real zeros can be picked out as the x-intercepts, these **imaginary zeros** cannot be seen on a regular graph.  In the next section we will discuss ways to visualize and find imaginary zeros.
---
title: "5.2 Zeros & Polynomial Equations"
description:
author: "Nolan Mitchell"
type: page
image: "duel.jpg"
draft: false
tags: ["zeros-of-polynomials", "fundamental-theorem-of-algebra", "galois-theory", "evariste-galois", "niels-henrik-abel", "carl-friedrich-gauss", "rational-zeros-theorem", "finding-possible-zeros", "verifying-zeros", "finding-rational-zeros", "finding-real-zeros", "finding-complex-zeros", "imaginary-zeros", "fundamental-theorem-of-algebra", "synthetic-division", "quadratic-formula", "cubic-formula", "quartic-formula", "factoring-polynomials"]
---

{{% imgcap file="/img/chapter-5/duel.jpg" title="Drawing by Bauce and Rouget" source="https://commons.wikimedia.org/wiki/File:Duel_pistolet.JPG" %}}

## Introduction
As the smoke cleared on the morning of May 30, 1832, young Ã‰variste Galois lay mortally wounded on the ground, having been shot in the stomach.  Though only 20 years old, Galois had earned a reputation not only as a brilliant mathematician, but also as a reckless political activist who had threatened the life of the French king and been arrested for carrying loaded weapons during a protest in Paris.  

No one knows for sure why Galois was involved the duel.  Some say that he was defending the honor of a young lady or that he was the victim of a government conspiracy.  All we know is that he feared for his life and spent the night before the duel writing farewell letters to close friends.

In one of those letters Galois famously described a new mathematical theory that revealed the hidden framework of polynomials.


## Zeros of Polynomials
In the last section we saw that x-intercepts are real number solutions to the polynomial equation $p(x)=0$ and that they are simple to find if the polynomial has been factored.{{% sidenote "factor theorem"%}}The **factor theorem** told us that $x=c$ is an x-intercept if and only if $(x-c)$ is a factor{{% /sidenote %}}  If the polynomial isn't factored, then solving $p(x)=0$ can be challenging.  

Throughout history efforts have been made to find formulas that will produce the zeros of polynomials. The Indian mathematician Brahmagupta is generally credited as being the first to publish a description of the [quadratic formula](/img/chapter-5/quadratic_formula.svg) in 628 AD, though the roots of the solution go back thousands of years.  The quadratic formula gives the two zeros of any 2nd degree polynomial.

In the 1500's, NiccolÃ² Tartaglia, one of the most gifted mathematicians in Italy, found a general process for solving all cubic equations.  Within a few years a fellow Italian by the name of Lodovico Ferrari found a way to find the zeros of all 4th degree polynomials.

The work of Tartaglia and Ferrari showed there are always 3 solutions to every 3rd degree polynomial and 4 solutions to every 4th degree polynomial.  Following that pattern, it would be reasonable to expect that a polynomial with a degree of $n$ always has $n$ zeros.

If you made that assumption, you'd be in good company.  In 1799, Carl Friedrich Gauss, arguably the greatest mathematician in history, proved that result as a consequence of his **Fundamental Theorem of Algebra**.

While the proof is very complicated and beyond the scope of this text, what the Fundamental Theorem of Algebra says is actually very simple.  In essence, Gauss showed that a polynomial whose degree is $n$ will always have exactly $n$ zeros.  Some of the zeros might involve imaginary numbers, some may be repeated, but there will always be $n$ zeros total.

For instance, since  $p(x)=2x^4-3x+8$ is a $4th$ degree polynomial, we know that it has exactly $4$ zeros.

{{% check %}}
1. How many total zeros does $p(x)=-3x^6+x^{2}-9x$ have? {{% answer %}}It is a 6th degree polynomial, so it must have 6 zeros.{{% /answer %}}
1. How many total zeros does $p(x)=5x^{3}-4$ have? {{% answer %}}It is a 3rd degree polynomial, so it must have 3 zeros.{{% /answer %}}
{{% /check %}}


## Galois Theory
Gauss showed that for a polynomial of degree $n$ there will always be $n$ solutions to the equation $p(x)=0$.  He did not, however, come up with a formula to find all of those solutions.  And there's a very good reason he didn't.

In the early 1800's, Galois' notes and letters, together with the work of his equally tragic contemporary Niels Henrik Abel{{% sidenote "Abel"%}}Abel was a young Norwegian mathematician struggling to find steady income so he could marry his fiancÃ©e.  He died, unwed, at the age of 26 from tuberculosis.  Two days later a letter arrived offering a post at the University of Berlin.{{% /sidenote %}}, showed that it is impossible to find a general algebraic formula (ie. a formula involving only addition, subtraction, multiplication, division, powers and roots) for the zeros of a polynomial if the degree is higher than 4.

In other words, we cannot count on using a formula to find the zeros of a polynomial if its degree is higher than 4.  In fact, since the formulas for the [cubic](/img/chapter-5/cubic_formula.svg) and [quartic](/img/chapter-5/quartic_formula.svg) are impractical, the only polynomial formula you'll likely need to remember is the [quadratic formula](/img/chapter-5/quadratic_formula.svg).

Instead of using complicated formulas, we will use a combination of graphical, algebraic, and numerical methods to find the zeros of polynomials.  And since graphs help us estimate the number and location of any real zeros as well as the number of imaginary zeros, it is preferable to study the graph of a polynomial first.


## Finding Possible Zeros
Since the real zeros of a polynomial correspond to the x-intercepts of its graph, we can sometimes identify them just by looking.

For instance, the graph of $p(x)=x^5-5x^{3}+4x$, shown here, appears to have x-intercepts at $x=-2$, $x=-1$, $x=0$, $x=1$ and $x=2$.

![](/img/chapter-5/poly_graph_5_integer_zeros.svg#center)

But what if a graph isn't available or if the graph is difficult to read?  For example, the cubic polynomial $p(x)=3x^{3}+8x^{2}+3x-2$ appears to have zeros when $x=-2$ and $x=-1$, but the location of the third zero is not clear.

![](/img/chapter-5/poly_graph_1_rational_2_integer_zeros.svg#center)

It might be $\frac{1}{4}$ or $\frac{1}{3}$ or maybe it's some irrational number like $\sqrt{\frac{1}{8}}$.  We simply can't tell just by looking. 

Luckily, there is a nice tool called the **rational zeros theorem** that allows us to make a list of numbers that *might* be zeros.  Take a look at the table below and see if you can spot the (color-coded) pattern yourself.

![](/img/chapter-5/rational_zeros_table.svg#center)

Notice that the *<font color="red">numerators</font>* of each zero are factors of the *<font color="red">constant term</font>* and the *<font color="blue">denominators</font>* are factors of the *<font color="blue">leading coefficient</font>*.  

If a polynomial with integer coefficients has a rational zero, then the **rational zeros theorem** says this pattern will always occur.  Which means we can use that pattern to reverse engineer a list of fractions that *might* be zeros.  

Let's test this and find all the fractions that might be zeros of $p(x)=\color{blue}{3}x^{3}+8x^{2}+3x\color{red}{-2}$.

The constant term is $\color{red}{-2}$, which can be divided evenly by $\color{red}{\pm 1, \thinspace \pm 2}$, so those are its factors.

The factors of the leading coefficient $\color{blue}{3}$ are $\color{blue}{\pm 1, \thinspace \pm 3}$.

Putting those together, our list of fractions that might be zeros is 

\[ \pm \frac{\color{red}{1}}{\color{blue}{1}}, \thinspace  \pm \frac{\color{red}{2}}{\color{blue}{1}},  \pm \frac{\color{red}{1}}{\color{blue}{3}}, \thinspace  \pm \frac{\color{red}{2}}{\color{blue}{3}} \]

Notice that the two zeros we spotted from the graph, $x=-2$ and $x=-1$, are in this list.  If our missing third zero is a fraction, then the rational zeros theorem guarantees that it is in this list.  The theorem **does not** however, guarantee that the missing zero is a fraction.

{{% check %}}
Consider the polynomial $p(x)=\color{blue}{5}x^2+3x+\color{red}{6}$.

1. List all the factors of the constant term $\color{red}{6}$. {{% answer %}}$\color{red}{6}$ can be divided evenly by $\color{red}{\pm 1, \thinspace \pm 2, \thinspace \pm 3, \thinspace \pm 6}$ , so those are its factors.{{% /answer %}}
1. List all the factors of the leading coefficient $\color{blue}{5}$. {{% answer %}}$\color{blue}{5}$ can be divided evenly by $\color{blue}{\pm 1, \thinspace \pm 5}$ , so those are its factors.{{% /answer %}}
1. List all the fractions with numerators that are factors of $\color{red}{6}$ and denominators that are factors of $\color{blue}{5}$. {{% answer %}}There are sixteen combinations.
\[ \pm \frac{\color{red}{1}}{\color{blue}{1}}, \thinspace  \pm \frac{\color{red}{2}}{\color{blue}{1}}, \thinspace \pm \frac{\color{red}{3}}{\color{blue}{1}}, \thinspace \pm \frac{\color{red}{6}}{\color{blue}{1}} \]
and
\[ \pm \frac{\color{red}{1}}{\color{blue}{5}}, \thinspace  \pm \frac{\color{red}{2}}{\color{blue}{5}}, \thinspace \pm \frac{\color{red}{3}}{\color{blue}{5}}, \thinspace \pm \frac{\color{red}{6}}{\color{blue}{5}} \]
{{% /answer %}}
{{% /check %}}


## Verifying Zeros

You'll recall that the real zeros of a polynomial are real numbers that are solutions to the equation $p(x)=0$.  Graphically they correspond to the x-intercepts of its graph.

For instance, the graph of $p(x)=x^5-5x^{3}+4x$, shown here, appears to have x-intercepts at $x=-2$, $x=-1$, $x=0$, $x=1$ and $x=2$.

![](/img/chapter-5/poly_graph_5_integer_zeros.svg#center)

But how do we know if these really are the zeros?  Maybe the true values are slightly different.  To verify that those values really are zeros we must check to see if $p(x)=0$ for each one.  With $x=-2$, for example,

\[ \begin{align}
p(-2) &= (-2)^5-5(-2)^3+4(-2) \newline
&=-32+40-8 \newline
&=0
\end{align}
\]

so we can be confident that $x=-2$ truly is a zero.

{{% check %}}
1.  Verify that $x=-1$, $x=0$, $x=1$ and $x=2$ are each zeros of $p(x)=x^5-5x^{3}+4x$. {{% answer %}}
\[
\begin{align}
p(-1)&=(-1)^5-5(-1)^3+4(-1) \newline
&=-1+5-4 \newline
&=0 \newline \newline
p(0)&=(0)^5-5(0)^3+4(0) \newline
&=0-0+0 \newline
&=0 \newline \newline
p(1)&=(1)^5-5(1)^3+4(1) \newline
&=1-5+4 \newline
&=0 \newline \newline
p(2)&=(2)^5-5(2)^3+4(2) \newline
&=32-40+8 \newline
&=0
\end{align}
\]
{{% /answer %}}
{{% /check %}}


## Finding Rational Zeros of a Polynomial

### Rational Zeros Example 1
Let's return to the polynomial  $p(x)=\color{blue}{3}x^{3}+8x^{2}+3x\color{red}{-2}$ and see how the rational zeros theorem helps us identify its zeros.  Since the leading coefficient is $\color{blue}{3}$ and the constant term is $\color{red}{-2}$, we know that the numerators and denominators of possible rational zeros must be

![](/img/chapter-5/rational_zeros_1_num_den.png#center)

This means that all rational zeros of $p(x)=\color{blue}{3}x^{3}+8x^{2}+3x\color{red}{-2}$  can be found in the following list.

![](/img/chapter-5/rational_zeros_1.png#center)

We can see from the graph that $-1$ and $-2$ are zeros, and both appear in this list.  

![](/img/chapter-5/poly_graph_1_rational_2_integer_zeros_color.svg#center)

Judging from the graph, if the third zero is a rational number then it is either $\frac{\color{red}{1}}{\color{blue}{3}}$ or $\frac{\color{red}{2}}{\color{blue}{3}}$.  

To see if either of these are the zeros we put the into the function and see if the result is zero.  We'll start with $\frac{\color{red}{1}}{\color{blue}{3}}$.

\[
  \begin{align}
    p\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)&=3\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)^{3}+8\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)^2+3\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)-2 \newline
    &=3\left(\frac{1}{27}\right)+8\left(\frac{1}{9}\right)+1-2 \newline
    &= \frac{3}{27}+\frac{8}{9}-1 \newline
    &= \frac{1}{9} + \frac{8}{9}-1 \newline
    &= \frac{9}{9} - 1 \newline
    &= 1 - 1 \newline
    &= 0
  \end{align}
\]

Since $p\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)=0$ we know that $\frac{\color{red}{1}}{\color{blue}{3}}$ is the third zero of the polynomial.  There's no need to check $\frac{\color{red}{2}}{\color{blue}{3}}$ because this polynomial only has three zeros.

### Rational Zeros Example 2
Let's use a graph and the rational zeros theorem to see if $p(x)=\color{blue}{6}x^2+7x\color{red}{-5}$ has any rational zeros.  

With a leading coefficient of $\color{blue}{6}$ and a constant term of $\color{red}{-5}$, we know that all rational zeros, if there are any, must be in the following list.

![](/img/chapter-5//rational_zeros_3.png#center)

With the help of the graph we can narrow this list down to $\frac{ \color{red}{1} } { \color{blue}{2} }$, $\frac{\color{red}{1}}{\color{blue}{3}}$ and $\frac{\color{red}{-5}}{\color{blue}{3}}$, since the other values are not near the x-intercepts.

![](/img/chapter-5/poly_graph_2_rational_zeros_color.svg#center)

Now we need to check each one, beginning with $x=\frac{\color{red}{1}}{\color{blue}{2}}$.

\[
  \begin{align}
    p\left(\frac{\color{red}{1}}{\color{blue}{2}}\right) &= 6\left(\frac{\color{red}{1}}{\color{blue}{2}}\right)^2+7\left(\frac{\color{red}{1}}{\color{blue}{2}}\right)-5 \newline
    &=\frac{6}{4}+\frac{7}{2}-5 \newline
    &=0
  \end{align}
\]

We've found one zero!  Let's keep going and check $x=\frac{\color{red}{1}}{\color{blue}{3}}$.

\[
  \begin{align}
    p\left(\frac{\color{red}{1}}{\color{blue}{3}}\right) &= 6\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)^2+7\left(\frac{\color{red}{1}}{\color{blue}{3}}\right)-5 \newline
    &=\frac{6}{9}+\frac{7}{3}-5 \newline
    &=-2
  \end{align}
\]

Since this is not $0$, we move on to our last option, $x=\frac{\color{red}{-5}}{\color{blue}{3}}$.

\[
  \begin{align}
    p\left(\frac{\color{red}{-5}}{\color{blue}{3}}\right) &= 6\left(\frac{\color{red}{-5}}{\color{blue}{3}}\right)^2+7\left(\frac{\color{red}{-5}}{\color{blue}{3}}\right)-5 \newline
    &=\frac{150}{9}-\frac{35}{3}-5 \newline
    &=0
  \end{align}
\]

From this it's clear that $\frac{ \color{red}{1} } { \color{blue}{2} }$ and $\frac{\color{red}{-5}}{\color{blue}{3}}$ are both zeros of our polynomial.  And since the Fundamental Theorem of Algebra says that a second degree polynomial has exactly two zeros, we know we have found all of the solutions.

## Finding Real Zeros of a Polynomial

### Real Zeros Example 1
There are two other tools we have at our disposal that we shouldn't forget about.  For example, the possible rational zeros of $p(x)=\color{blue}{1}x^2-\color{red}{3}$ are

\[ \pm \frac{\color{red}{1}}{\color{blue}{1}}, \thinspace \pm \frac{\color{red}{3}}{\color{blue}{1}} \]

but the graph does not have x-intercepts at $\pm 1$ or at $\pm 3$.

![](/img/chapter-5/poly_graph_2_irrational.svg#center)

It's important to remember that the Rational Zeros Theorem only gives us a list of rational numbers that *might* be zeros.  If none of them work then the zeros are not fractions.  

In this case the two zeros are irrational numbers and can be found with the Quadratic Formula.

\[
  \begin{align}
    x &= \frac{-b\pm\sqrt{b^2-4ac}}{2a} \newline
    &= \frac{-(0)\pm\sqrt{(0)^2-4(\color{blue}{1})(\color{red}{-3})}}{2\color{blue}{(1)}} \newline
    &= \frac{\pm\sqrt{12}}{2} \newline
    &= \frac{\pm2\sqrt{3}}{2} \newline
    &= \pm \sqrt{3} \newline
  \end{align}
\]

So the first tool we shouldn't forget about is the Quadratic Formula.

### Real Zeros Example 2
The second tool that is often helpful is synthetic division.  Consider, for instance the polynomial $p(x)=\color{blue}{6}x^3+7x^2-16x\color{red}{-12}$.  The list of possible rational zeros is huge.

\[ \pm \frac{\color{red}{1}}{\color{blue}{1}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{1}},\thinspace \pm \frac{\color{red}{3}}{\color{blue}{1}},\thinspace  \pm \frac{\color{red}{4}}{\color{blue}{1}},\thinspace\pm \frac{\color{red}{6}}{\color{blue}{1}},\thinspace \pm \frac{\color{red}{12}}{\color{blue}{1}} \]

\[ \pm \frac{\color{red}{1}}{\color{blue}{2}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{2}},\thinspace \pm \frac{\color{red}{3}}{\color{blue}{2}},\thinspace \pm \frac{\color{red}{4}}{\color{blue}{2}},\thinspace \pm \frac{\color{red}{6}}{\color{blue}{2}},\thinspace \pm \frac{\color{red}{12}}{\color{blue}{2}} \]

\[ \pm \frac{\color{red}{1}}{\color{blue}{3}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{3}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{4}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{6}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{12}}{\color{blue}{3}} \]

\[ \pm \frac{\color{red}{1}}{\color{blue}{6}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{6}},\thinspace \pm \frac{\color{red}{3}}{\color{blue}{6}},\thinspace \pm \frac{\color{red}{4}}{\color{blue}{6}},\thinspace \pm \frac{\color{red}{6}}{\color{blue}{6}},\thinspace \pm \frac{\color{red}{12}}{\color{blue}{6}} \]

By eliminating duplicate values like $\frac{\color{red}{1}}{\color{blue}{1}}$ and $\frac{\color{red}{2}}{\color{blue}{2}}$ and looking at the graph

![](/img/chapter-5/poly_graph_1_integer_2_rational.svg#center)

we can trim this list down significantly, but there are still five numbers to check (listed here in numerical order).

\[ \frac{\color{red}{-2}}{\color{blue}{1}}, \thinspace \frac{\color{red}{-2}}{\color{blue}{3}}, \thinspace \frac{\color{red}{-1}}{\color{blue}{2}}, \thinspace \frac{\color{red}{-1}}{\color{blue}{3}}, \thinspace \frac{\color{red}{3}}{\color{blue}{2}}\]

Earlier we plugged the values into the polynomial to check each one.  While that always works, synthetic division can also be used.  To show how this works we'll pick $\frac{\color{red}{-2}}{\color{blue}{1}}=-2$ out of our list and do synthetic division.  

![](/img/chapter-5/synthetic_2_a.svg#center)

Since the remainder is $0$ we know that $\left(x-\frac{\color{red}{-2}}{\color{blue}{1}}\right)$ is a factor of the polynomial, which also means that $\frac{\color{red}{-2}}{\color{blue}{1}}$ is a zero.

Anytime we do synthetic division and end with a remainder of $0$ then we have found a zero of the polynomial.

Additionally, any other real zeros must be inside the quotient $6x^2-5x-6$ and could be found by the quadratic formula.  But since our list of rational zeros was so small, it may be preferable to check the remaining three numbers by synthetic division before resorting to the quadratic formula.  

Starting with $\frac{\color{red}{-2}}{\color{blue}{3}}$, the synthetic division tells us that it is a zero.

![](/img/chapter-5/synthetic_2_b.svg#center)

Since $\frac{\color{red}{-2}}{\color{blue}{3}}$ is a zero, there's no need to check $\frac{\color{red}{-1}}{\color{blue}{2}}$ and $\frac{\color{red}{-1}}{\color{blue}{3}}$, but we should still look at $\frac{\color{red}{3}}{\color{blue}{2}}$.

![](/img/chapter-5/synthetic_2_c.svg#center)

We conclude that the three zeros of our polynomial are $-2$, $\thinspace \frac{\color{red}{-2}}{\color{blue}{3}} \thinspace$ and $\thinspace \frac{\color{red}{3}}{\color{blue}{2}}$.


## Finding Complex Zeros of a Polynomial

### Complex Zeros Example 1
The process we have developed can also find imaginary zeros.  This time we'll examine $p(x)=\color{blue}{3} x^{3}-14 x^{2}+23 x\color{red}{-10}$.  

This is a third degree polynomial so it must have three zeros.  We can tell right away from the graph that it only has one real zero, so there must be two that are imaginary.

![](/img/chapter-5/poly_graph_1_rational_2_imaginary.svg#center)

If that real zero is a rational number, then we can find it using the Rational Zeros Theorem by examining the list of fractions that might be zeros.

\[ \pm \frac{\color{red}{1}}{\color{blue}{1}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{1}},\thinspace \pm \frac{\color{red}{5}}{\color{blue}{1}},\thinspace \pm \frac{\color{red}{10}}{\color{blue}{1}}\]

\[ \pm \frac{\color{red}{1}}{\color{blue}{3}}, \thinspace \pm \frac{\color{red}{2}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{5}}{\color{blue}{3}},\thinspace \pm \frac{\color{red}{10}}{\color{blue}{3}}\]

Out of that list $\frac{\color{red}{2}}{\color{blue}{3}}$ appears to be our best choice, so we'll use synthetic division to check it.

![](/img/chapter-5/synthetic_3.svg#center)

Because the remainder is $0$ we know for sure that $\frac{\color{red}{2}}{\color{blue}{3}}$ is a zero.  

That takes care of our one real zero, but what about the two that are imaginary?  Those are inside the quotient $3x^{2}-12x+15$ and we'll get them with the quadratic formula.

\[
  \begin{align}
    x &= \frac{-b\pm\sqrt{b^2-4ac}}{2a} \newline
    &= \frac{-(-12)\pm\sqrt{(-12)^2-4(3)(15)}}{2(3)} \newline
    &= \frac{12 \pm\sqrt{-36}}{6} \newline
    &= \frac{12 \pm 6i}{6} \newline
    &= 2 \pm i \newline
  \end{align}
\]

The two imaginary zeros are $2+i$ and $2-i$ and we have now found all three of the complex zeros of our polynomial.

### Complex Zeros Example 2
Our final example $p(x)=x^4 + x^3 - x^2 + x -2$ is a fourth degree polynomial with a very short list of possible rational zeros.  The choices are $\pm 1$ and $\pm 2$ and a graph quickly shows us that $-2$ and $1$ are the likely candidates.

![](/img/chapter-5/poly_graph_2_integer_2_imaginary.svg#center)

As before we'll check one of these by synthetic division, starting with $-2$.

![](/img/chapter-5/synthetic_4_a.svg#center)

This tells us that $-2$ is a zero, but we still have three more to find.  The key is to remember that all the other zeros must be in the quotient $x^3-x^2+x-1$.  So now we focus on the quotient and repeat the process.

If $x^3-x^2+x-1$ has a rational zero then it is in our original list, so let's try $1$.

![](/img/chapter-5/synthetic_4_b.svg#center)

Since the remainder is zero, we know $1$ is a zero of the polynomial.  The final two zeros must be inside this new quotient $x^2+1$ and we'll use the quadratic formula to get them out.

\[
  \begin{align}
    x &= \frac{-b\pm\sqrt{b^2-4ac}}{2a} \newline
    &= \frac{-(0)\pm\sqrt{(0)^2-4(1)(1)}}{2(1)} \newline
    &= \frac{\pm\sqrt{-4}}{2} \newline
    &= \frac{\pm 2i}{2} \newline
    &= \pm i \newline
  \end{align}
\]

We add these two imaginary numbers to our list and can finally say that the four complex zeros of $p(x)=x^4 + x^3 - x^2 + x -2$ are $-2, \thinspace 1, \thinspace -i, \thinspace$ and $\thinspace i$.


## Summary
Let's take a moment to summarize the process that we have developed.  Given a polynomial, we can attempt to find its complex (real and imaginary) zeros by working through the following steps.

1. Use the Rational Zeros Theorem to list all possible fractions that might be zeros.  
1. Trim down that list by looking at a graph and eliminating any values that are not reasonably close to the x-intercepts.
1. Check the remaining values either by testing if $p(x)=0$ or by performing synthetic division and seeing if the remainder is zero.
1. Repeat the process for the other zeros or, if the quotient is a 2nd degree polynomial, apply the quadratic formula.

## Looking Ahead
While the process outlined here will work for all the exercises in the homework, it is far from being a universal method that will work for every polynomial.  For most problems, in fact, it is not possible to find exact zeros, so we have to find approximations.  There is even an entire field of modern math (numerical analysis) dedicated to, among other things, constructing algorithms for finding zeros of equations.  And many practical applications in physics, chemistry, engineering, etc. rely on those computational methods.

In the next section we get a brief glimpse of a few ways polynomials end up being used in the real world.
---
title: "5.3 Applications of Polynomials"
description:
author: "Nolan Mitchell"
type: page
image: "generalife-3111770_1280.jpg"
draft: false
tags: ["applications-of-polynomials", "projectile-motion", "parabolas", "galileo", "vertex-of-parabola", "finding-vertex", "maximum-height", "pumpkin-chuckin", "solving-quadratic-equations", "quadratic-formula", "cliff-diving", "alhambra-palace", "generalife-gardens"]
---

{{% imgcap file="/img/chapter-5/generalife-3111770_1280x720.jpg" title="Photo by granadandyou from Pixabay " source="https://pixabay.com/images/id-3111770/" %}}

## Introduction
Located in the foothills of the Sierra Nevada mountains in the Andalusia region of Spain, the Alhambra palace is a world heritage site from the 13th century.  Among its most photographed features today are the water fountains in the Generalife gardens.  

The water that flows out of these fountains follows a curved path through the air.  But it's not just any random curve, it is a parabola!  

## Projectile Motion
It was Galileo who proved that any object launched into the air will follow the path of a parabola.{{% sidenote "Galileo"%}}Drawings from [Galileo's notebook](https://www.mpiwg-berlin.mpg.de/Galileo_Prototype/HTML/F116_V/F116_V.HTM) showing results of his free fall experiments, dating from about 1609. ![Folio 116v from Galileo's notebook](/img/chapter-5/Galileo_Notebook_C116_V.jpg){{% /sidenote %}}  This could be water tossed into the air by a fountain or a ball thrown by a child, they all take on the same characteristic arc.

Physicists have studied this for hundreds of years and have discovered several equations that model the motion of projectiles.  In particular, the vertical height of a projectile (in meters) can be written as a function of time

\[ h(t) = -4.9 t^{2} + v_0 t + h_0 \]

where $v_0$ is vertical velocity (in meters per second), $h_0$ is the initial height (in meters) and $t$ is the time (in seconds).

{{% check %}}
{{% imgcap file="/img/chapter-5/16333686542_ca8b5866fc_b_flipped.jpg" title="Photo by Petri DamstÃ©n on Flickr" source="https://flic.kr/p/qTmpXd" %}} Suppose the skier in this photo leaves the jump with a vertical velocity of $2$ meters per second from an initial height of $70$ meters.  Write a function that models their height, assuming the jump follows projectile motion. {{% answer %}}Using $v=2$ and $h=70$ the function would be
\[ h(t)=-4.9t^{2}+2t+70 \]
{{% /answer %}}
{{% /check %}}

## Finding the Vertex of a Parabola
One place where projectile motion is used is in the sport of pumpkin chuckin', where teams build slingshots, catapults or air cannons (like the one below) to throw pumpkins as far as possible.

{{% imgcap file="/img/chapter-5/14421974334_a9a983284b_b_flipped.jpg" title="Photos by Clark on Flickr" source="https://flic.kr/p/nYqovU" %}}

If pumpkins leave the barrel of this air cannon 6.4 meters above the ground with a vertical velocity of 170 meters per second, then the height at any time is given by

\[ h(t) = -4.9 t^{2} + 170 t + 6.4 \]

Our model gives the height at any time, so only questions involving height and time are fair game.{{% sidenote "Pumpkin"%}}The obvious question of how far the cannon can shoot a pumpkin is, unfortunately, not one we can solve with this function.  <br><br>Distance depends on the launch angle and you have to use trigonometry to find it.  But to give you some idea, the current world record is well over one mile!{{% /sidenote %}}  The two that come to mind are determining when the pumpkin will come back down and hit the ground and finding its maximum height.

Graphing our function will give us a better idea of where to look for the answers.

![](/img/chapter-5/projectile_graph_pumpkin.svg#center)

The pumpkin will come back down and hit the ground when the height is $0$, which means we need to find the zeros of the function.  All that needs to be done is to solve $0= -4.9 t^{2} + 170 t + 6.4$ using the quadratic formula like we've done before.

\[
  \begin{align}
    t &= \frac{-b\pm\sqrt{b^2-4ac}}{2a} \newline
    &= \frac{-(170)\pm\sqrt{(170)^2-4(-4.9)(6.4)}}{(2)(-4.9)} \newline
    &= \frac{-170\pm\sqrt{29025.44}}{-9.8} \newline
    &= -0.0376 \small \text{ and } \normalsize 34.731 \small \text{ seconds} \newline
  \end{align}
\]

Of the two values the only one that makes physical sense is $t=34.731$ seconds, which also matches the value in our graph.

The maximum height occurs at the peak of the graph which, for a parabola, is called the **vertex**.  Due to symmetry, the vertex always occurs halfway between the two x-intercepts.  In other words, if $x_1$ and $x_2$ are the two x-intercepts, then the x-coordinate of the vertex is $x_v=\frac{x_1+x_2}{2}$.

For our particular pumpkin cannon function $h(t) = -4.9 t^{2} + 170 t + 6.4 $ which had x-intercepts of $-0.0376$ and $34.731$, the x-coordinate of the vertex is

\[
  \begin{align}
    x_v & =\frac{x_1+x_2}{2} \newline
    &= \frac{-0.0376 + 34.731}{2} \newline
    &= 17.347
  \end{align}
\]

So our maximum height occurs $17.347$ seconds after launch.  

To figure out what that height is, we put this time into the function

\[
  \begin{align}
    h(t) &= -4.9 t^{2} + 170 t + 6.4 \newline
    h(17.347) &= -4.9(17.347)^{2} + 170(17.347) + 6.4 \newline
    &= 1480.9 \small \text{ meters}
  \end{align}
\]

and find that the maximum height is $1480.9$ meters.

Using the x-intercepts to find the vertex always works, but there is a faster method.  

If your function is quadratic polynomial written as $f(x)=ax^2+bx+c$, then the x-coordinate of the vertex is always $x_v=\frac{-b}{2a}$ and the y-coordinate is $y_v=f(x_v)$.

Let's go back to the pumpkin function $h(t) = -4.9 t^{2} + 170 t + 6.4$ and see how this works.

The x-coordinate of the vertex is found by computing

\[
  \begin{align}
    x_v &=\frac{-b}{2a} \newline
    &= \frac{-170}{(2)(-4.9)} \newline
    &= 17.347
  \end{align}
\]

which is the same value as before, but we did not need to go through the quadratic formula to find the two zeros and locate the halfway point between them.

Getting the y-coordinate of the vertex is exactly the same as before, we just evaluate the function when $x=17.347$.

\[
  \begin{align}
    y_v &= f(x_v) \newline
    &= f(17.347) \newline
    &= -4.9(17.347)^{2} + 170(17.347) + 6.4 \newline
    &= 1480.9 \small \text{ meters}
  \end{align}
\]

This technique for finding the vertex works on any quadratic function, not just with projectile motion.  One thing to keep in mind, however, is that the vertex is *not always* a maximum.  Depending on the shape of the parabola it could be a minimum.  

{{% check %}}
{{% imgcap file="/img/chapter-5/9764584931_cab334ff9a_b.jpg" title="Photo by Jeremy Taylor on Flickr" source="https://flic.kr/p/fSS3UB" %}} Suppose the motorcyclist in this photo leaves the ramp with a vertical velocity of 14 meters per second from an initial height of 2 meters.  Write a function that models their height, assuming the jump follows projectile motion.  Then find their maximum height by locating the vertex of your function. {{% answer %}} Using $v=14$ and $h=2$ the function would be
\[ h(t)=-4.9t^{2}+14t+2 \]
The x-coordinate of the vertex is
\[
\begin{align}
x_v &=\frac{-b}{2a} \newline
&= \frac{-(14)}{(2)(-4.9)} \newline
&= 1.43 \small \text{ seconds}
\end{align}
\]
and the y-coordinate of the vertex is
\[
\begin{align}
y_v &= f(x_v) \newline
&= f(1.43) \newline
&= -4.9(1.43)^2+14(1.43)+2 \newline
&= 12 \small \text{ meters}
\end{align}
\]
So the motorcycle reaches a maximum height of 12 meters 1.429 seconds after leaving the ramp.
{{% /answer %}}
{{% /check %}}


## Solving Quadratic Equations
{{% imgcap file="/img/chapter-1/cliff_dive.jpg" title="Saltos Red Bull en Bilbao 2015 by jamoral, on Flickr" source="https://www.flickr.com/photos/jamoral/21713225096/"%}}
Cliff diving is potentially a very dangerous sport.  One maneuver that makes it a bit safer is called a *barani*.{{% sidenote "barani" %}}<iframe width="100%" height="100%" src="https://www.youtube.com/embed/tx2ZgKYS-Yc?start=11" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>{{% /sidenote %}}  

The barani is a gymnastics move that combines a half somersault with a half twist.  Performing a barani gives the diver time to see the water and control their landing so that they hit the water feet first.  

Assuming a professional cliff diver can jump up with a vertical velocity of $3$ meters per second, then the projectile motion function

\[ h(t)=-4.9 t^{2} + 3t + 27 \]

gives us their height above the water $t$ seconds after diving off the $27$ meter platform.

If a diver can complete a barani about 5 meters above the surface of the water, then the chance of a safe dive is very high.  How much time does that give them to do their flips and twists?

To answer this we have to find $t$ so that $h(t)=5$.  Setting up the equation we find that

\[
  \begin{align}
    h(t) &= 5 && \small \color{#5fa2ce}{\text{Original equation}} \newline
    -4.9 t^{2} + 3t + 27 &= 5 && \small \color{#5fa2ce}{\text{Insert equation for $h(t)$}} \newline
    -4.9 t^{2} + 3t + 22 &= 0 && \small \color{#5fa2ce}{\text{Subtract $5$}}
  \end{align}
\]

which is another situation for the quadratic formula.

\[
  \begin{align}
    t &= \frac{-(3)\pm\sqrt{(3)^2-4(-4.9)(22)}}{2(-4.9)} && \small \color{#5fa2ce}{\text{Apply Quadratic Formula}} \newline
    t &= \frac{-3\pm\sqrt{440.2}}{-9.8} && \small \color{#5fa2ce}{\text{Simplify}} \newline
    t &= -1.84 \small \text{ and } \normalsize 2.45 \small \text{ seconds } && \small \color{#5fa2ce}{\text{Evaluate}}
  \end{align}
\]

Clearly $t=-1.84$ seconds can't be our answer, so it must be that the diver has $2.45$ seconds to do their dive and complete the barani.

{{% check %}}
Assuming the diver completes their barani after $2.45$ seconds, how much longer will it take before they hit the water? {{% answer %}}This question is asking us to find the zeros, or x-intercepts of our function $h(t)=-4.9 t^{2} + 3t + 27$ which, as we've done before, can be found through the quadratic formula.
\[
\begin{align}
t &= \frac{-(3)\pm\sqrt{(3)^2-4(-4.9)(27)}}{2(-4.9)} && \small \color{#5fa2ce}{\text{Apply Quadratic Formula}} \newline
t &= \frac{-3\pm\sqrt{538.2}}{-9.8} && \small \color{#5fa2ce}{\text{Simplify}} \newline
t &= -2.06 \small \text{ and } \normalsize 2.67 \small \text{ seconds } && \small \color{#5fa2ce}{\text{Evaluate}}
\end{align}
\]
The diver hits the water at $t=2.67$ seconds, which is $2.67-2.45=0.22$ seconds after completing the barani.{{% /answer %}}
{{% /check %}}
---
title: "5.4 Rational Functions"
description:
author: "Nolan Mitchell"
type: page
image: "erik-mclean-oPWGhqBPNI0-unsplash.jpg"
draft: false
tags: ["rational-functions", "zeros-of-rational-functions", "vertical-asymptotes", "horizontal-asymptotes", "removable-discontinuities", "holes-in-graphs", "undefined-division-by-zero", "numerator-zeros", "denominator-zeros", "degree-comparison", "leading-coefficient-ratio", "end-behavior-rational-functions"]
---

{{% imgcap file="/img/chapter-5/erik-mclean-oPWGhqBPNI0-unsplash.jpg" title="Photo by Erik Mclean on Unsplash" source="https://unsplash.com/photos/oPWGhqBPNI0" %}}

## Introduction
Some observable characteristics, such as eye and hair color, are controlled by genes that pass from parent to child.  It's not unusual for a trait to skip generations and appear to pop up out of nowhere.  For instance, two people who don't have red hair can have redheaded children, or someone might have blue eyes even if both parents have brown eyes.

Since rational functions are built with polynomials, they inherit some of the same behaviors as their "parents", the polynomials.  But rational functions also have several properties that polynomials do not have.


## Rational Functions
In [Chapter 4](/chapter-4/4.2/#rational-functions) we saw that dividing two polynomials $n$ and $d$ resulted in a new type of function called a *rational function*.

\[ r(x)=\frac{n(x)}{d(x)} \]

The graphs of rational functions have some of the most complicated behavior we have seen so far.

![](/img/chapter-4/rational_functions_graphs.svg#center)

As you can see from these examples, rational functions often have x-intercepts, a property they share with polynomials, but they can also have [vertical and horizontal asymptotes](/chapter-1/1.3/#asymptotes), two things polynomials never have.  There is even an entirely new behavior that we have not seen before that seems to pop up almost out of nowhere.

## Zeros
Rational functions inherit their zero behavior from the polynomial in the numerator.  You can explore this in the figure below.  Look carefully at the link between the location of the zero and the factors in the numerator.

{{% geogebra ratio="40%" id_1="zigao44ostIFLpfy" id_2="tk5488nc" id_m="hrgyn3qw" %}}

{{% check %}}
1. How can you find the x-intercepts of a rational function by looking at its equation? {{% answer %}}If $(x-c)$ is a factor of the numerator, then the function has an x-intercept at $x=c$. The zeros of the polynomial in the numerator cause the zeros of the rational function.{{% /answer %}}
{{% /check %}}


## Vertical Asymptotes
The vertical asymptotes of a rational function are caused by the polynomial in the denominator.  In the figure below you can move the vertical asymptotes (indicated by the dotted lines).  Look for a connection between the location of the vertical asymptotes and the factors in the denominator.

{{% geogebra ratio="65%" id_1="68P3xw4hSKGeNNe4" id_2="pcxugr4b" id_m="ssgbhywx" %}}


{{% check %}}
1. How can you tell if a rational function has a vertical asymptote, just by looking at its equation? {{% answer %}}If $(x-c)$ is a factor of the denominator and not a factor of the numerator then the function has a vertical asymptote at $x=c$. The zeros of the polynomial in the denominator cause the vertical asymptotes of the rational function.{{% /answer %}}
{{% /check %}}

## Removable Discontinuities
So far we've determined that zeros in the numerator cause x-intercepts while zeros in the denominator cause vertical asymptotes.  But what would happen if there was a zero in both at the same place?

Or to ask the question another way, what is $\frac{0}{0}$?  One thought is that it should equal $1$, since a number divided by itself is $1$.  Another argument is that it should be $0$, since $0$ divided by any number is $0$.

But if we look back at what division means it gets even more complicated.  Remember that $a \div b = x$ means $a = b \times x$.

Then $0 \div 0 = x$ would mean $0 = 0 \times x$, but that's true for every number!  Since there's no single well defined way to say what $0 \div 0$ equals, we leave it *undefined*.  

So whenever we have a rational function that has matching factors in the numerator and denominator, the graph is undefined at that point and there is a hole or break in the graph.  The official term is "*removable discontinuity*".

In the figure below you can change the locations of the zero, the vertical asymptote, and the hole.

{{% geogebra ratio="65%" id_1="xPIL41W5dZKruUnz" id_2="mhChyVxw" id_m="ntYzprQz" %}}


{{% check %}}
1. Identify all of the x-intercepts, vertical asymptotes and holes of the rational function \[r(x)=\frac{(x-5)(x+3)(x-1)}{(x-2)(x-7)(x-1)}\] {{% answer %}}There are x-intercepts at $x=5, x=-3$, vertical asymptotes at $x=2, x=7$ and a hole at $x=1$. {{% /answer %}}
1. Write an equation for a rational function that has a zero at $x=2$, a vertical asymptote at $x=11$, and a hole at $x=4$. {{% answer %}}\[r(x)=\frac{(x-2)(x-4)}{(x-11)(x-4)}\]
{{% /answer %}}
{{% /check %}}


## Horizontal Asymptotes
In addition to x-intercepts, vertical asymptotes and holes, rational functions often have horizontal asymptotes.

Recall that a horizontal asymptote is a long-term behavior, describing how the function levels off as $x \rightarrow \pm \infty$.  Since the long-term behavior of a polynomial is controlled by the degree and leading coefficient, we should focus our attention on the degree and leading coefficients of the polynomials that make up a rational function.

In this first figure both polynomials have the same degree.  Adjust the leading coefficients and see how that impacts the location of the horizontal asymptote.

{{% geogebra ratio="65%" id_1="pe7TUPcu5aPtBhgT" id_2="at9thts5" id_m="u76wmebr" %}}

As you've just seen, if the degrees match then you can simplify the leading coefficients to find the horizontal asymptote.

But what if the degrees do not match?  In this figure you can alter the degree of each polynomial.  

{{% geogebra ratio="65%" id_1="zxRWUiBDisUD0ALZ" id_2="pdxmcuxv" id_m="prrwdbcz" %}}

If the degree of the numerator is larger, then no horizontal asymptote exists. However, if the degree of the denominator is larger, the horizontal asymptote is automatically at $y = 0$ (i.e. the x-axis).

{{% check %}}
1. What is the horizontal asymptote of this rational function? \[ r(x)=\frac{10x^3+4}{2x^3-8x^2} \] {{% answer %}}Since the degrees match, the horizontal asymptote is $y=\frac{10}{2}=5$.
{{% /answer %}}
1. What is the horizontal asymptote of this rational function? \[ r(x)=\frac{5x-2}{3x^2+97x+13} \] {{% answer %}}Since the degree on the bottom is larger, the horizontal asymptote is $y=0$.
{{% /answer %}}
1. What is the horizontal asymptote of this rational function? \[ r(x)=\frac{x^{6974}+1}{x^{3827}-4x} \] {{% answer %}}Since the degree in the numerator is larger, there is no horizontal asymptote.
{{% /answer %}}
{{% /check %}}
---
title: "6.1 Concepts of Modeling"
description: "Every spring, hundreds of people come to the Great Plains region of the United States in an attempt to get as close as possible to one of natureâ€™s most violent events: a tornado. "
author: "Nolan Mitchell"
type: page
image: "tornado.jpg"
draft: false
tags: ["mathematical-modeling", "modeling-process", "scatterplots", "interpolation", "extrapolation", "tornado-data", "independent-variables", "dependent-variables", "aligning-data", "scaling-data", "modeling-with-transformations", "slope-intercept-form", "point-slope-form", "vertex-form", "piecewise-defined-functions"]
---

{{% imgcap file="/img/chapter-6/nikolas-noonan-682177-unsplash.jpg" title="Tornado photo by Nikolas Noonan on Unsplash" source="https://unsplash.com/photos/fQM8cbGY6iQ"%}}


## Introduction
Every spring, hundreds of people come to the Great Plains region of the United States in an attempt to get as close as possible to one of nature's most violent events:  a tornado.  While some go to "Tornado Alley" just for the thrill, most professional storm chasers have a different goal.  What they want is data: scientific measurements that can only be found inside real tornadoes.

Scientists and university researchers, like those at NOAA's National Severe Storms Laboratory, hope to use that data to create mathematical models that will help them understand the inner workings of tornadoes and how they form.


## The Modeling Process
When we speak of creating a **mathematical model**, what exactly are we talking about?  

A model is a simplified representation of a real world object.  Mathematical models are found in nearly every field of study and are useful when it is not feasible, economical, practical, or safe to work with the real item.  

To construct a model, we begin with a set of data points and a description of the scenario and then try to find an equation of a function that closely aligns with our observations and what we know about the situation.

Once a model has been created, we can use the rules of mathematics to discover things about its mathematical behavior. The insights gained from these analyses can, in turn, be used to make predictions and gain understanding about how the real-world object might behave.

![](/img/chapter-6/modeling_diagram.svg#center)

Through continued observations and adjustments, the model can be refined to more accurately represent the real-world phenomenon it is intended to simulate.

While our models will never be perfect, there is a good chance that they might be accurate enough to be genuinely useful.  Renowned physicist Eugene Wigner referred to the predictive nature of mathematics, especially in the natural sciences, as the *"unreasonable effectiveness of mathematics."*  This theme will be prevalent throughout this chapter.



## Scatterplots
Many physical laws, like the law of gravity, were discovered by gathering data and looking for patterns.  One of our primary tools for visualizing data is the **scatterplot**.  A scatterplot is nothing more than pairs of data plotted as points on a grid.  

For instance, researchers from Purdue University analyzed 1285 tornadoes in Indiana from 1950 to 2012.{{% sidenote "tornado citation" %}}See the paper by Olivia Kellner and Dev Niyogi in the [American Meteorological Society's Earth Interactions journal, volume 18 no. 10 (2014).](https://doi.org/10.1175/2013EI000548.1){{% /sidenote %}}  One set of data compared the number of tornadoes observed at different hours of the day.  The scatterplot below illustrates this data.

![](/img/chapter-6/tornado_time.svg#center)

The scatterplot reveals a distinct pattern, suggesting that most tornadoes form late in the afternoon.  This is a well-known result that follows from the fact that, by mid-afternoon, the sun has sufficiently heated the ground and atmosphere enough to produce thunderstorms.

Notice that there is a subtle but important difference between the data (black dots) and the model (the red curve).  The model allows us to make predictions for values that were not recorded.  For instance, no data point corresponds to 10:15am, but using the model we can say the number is likely to be around 20 tornadoes. 


## Interpolation and Extrapolation
Models can be used to make estimations in two different ways. Making a prediction outside of a data set is called **extrapolation**.  Estimating a value that is in between known values is **interpolation**.

For instance, if we knew the number of tornadoes in 1900 and in 2000, predicting how many will occur in 2050 would be an extrapolation since that value lies beyond the known data. Extrapolation assumes that an existing trend will continue unchanged into the future, which is not always guaranteed.

On the other hand, estimating the number of tornadoes in the year 1950 would be interpolation since 1950 falls between the known values.

{{% check %}}
Suppose that we know the price of a movie ticket in 2000 and also the price in 2010, but no other years.  Decide if the following would be examples of interpolation or extrapolation.

1. Predicting what the cost of a movie ticket will be in 2050. {{% answer %}}Extrapolation because 2050 is outside of the known data.{{% /answer %}}
1. Estimating what the cost of a movie ticket was in 2005. {{% answer %}}Interpolation since 2005 is in between known values.{{% /answer %}}
1. Estimating what the cost of a movie ticket was in 1920. {{% answer %}}Extrapolation.  1920 is outside of the data set.{{% /answer %}}
{{% /check %}}


## Another Tornado Data Set
Let's take a look at another set of tornado data, showing how closely tornadoes occur to populated areas.

{{% geogebra ratio="50%" id_1="6XcJvVUnACwrTb4z" id_2="mrcsehab" id_m="j64zgw6h" %}}

This scatterplot reveals a strong linear trend, indicating that the percentage of observed tornadoes increases as one moves further away from the city or town center. The equation $y=\color{blue}{2.84}x+\color{green}{0.14}$ serves a good model for the data.  

If we use our model to extrapolate back to a distance of $0$ kilometers it suggests that there is a $0\\%$ chance of seeing a tornado, which might lead to the assumption that people in cities are safer than those in rural areas. That conclusion, however, needs to be approached with caution since many other factors may come into play.

Contrary to what one might think, tornadoes are not diverted by structures or buildings.  They have been known to hit large cities, pass over rivers, climb hills and cross canyons.  

Research even suggests that slower winds and hotter air in urban areas can actually *increase* the tornado-genesis process.  According to NOAA's tornado safety guidelines, the safest place is in a [fortified tornado shelter.](https://www.spc.noaa.gov/faq/tornado/#Safety "NOAA's tornado safety guidelines")

This example serves as a valuable lesson that even when data displays an apparent pattern, it is crucial to take time to investigate and consider other underlying factors before we make predictions or draw conclusions from our model.


## Independent and Dependent Variables
In all of the tornado data sets we've seen, it was up to the researchers to decide which variable was independent and which was dependent.  

Whenever we work with a raw set of data, it will be up to us to do the same thing and determine which quantity is the independent and which one is dependent. 

The **independent variable** is the parameter that changes or controls the other variable, and it is often plotted on the x-axis of a graph. 

On the other hand, the **dependent variable** is the outcome or response that is measured or observed as the independent variable changes, and it is typically plotted on the y-axis of a graph.

Often, certain variables are naturally independent or dependent based on our knowledge of the situation. For example, suppose researchers collect data on the dosage of a medication given to patients and their corresponding blood pressure measurements.  Since researchers control the dosage, it would be considered the independent variable.  Blood pressure, on the other hand, is expected to change in response to the dosage level, so it should be the dependent variable.

{{% check %}}
1. In an experiment, data is collected on the amount of sunlight and the harvest yield of a tomato plant.  Which variable would be considered dependent?  {{% answer %}}We would expect the yield to be dependent on the amount of sunlight.{{% /answer %}}
1. If the speed of a rocket is your dependent variable, what kinds of things might be reasonable independent variables? {{% answer %}}Anything that influences the speed could be a reasonable choice:  time since launch; weight of the rocket; amount of fuel; size of the payload; etc. {{% /answer %}}
1. In 1662, scientist Robert Boyle investigated the relationship between pressure and volume in a gas.  Which variable do you think he used as the independent one? {{% answer %}}This is a harder one.  Boyle discovered that pressure and volume are inversely proportional to each other so, in theory, either one could be independent.  In practice, Boyle, found it easier to change the pressure rather than change the volume, so pressure was his independent variable. {{% /answer %}}
{{% /check %}}


## Aligning and Scaling Data
To make the data more manageable and relatable, we often use aligning and scaling techniques.

**Aligning** the data involves shifting the independent variable to a more convenient starting point. **Scaling** the data allows us to convert the units of the dependent variable to a more practical scale.  

Let's look at an example where both of these might be helpful.  The table below shows the total number of mobile game downloads on iOS and Android from 2015 to 2022.  

| Year | Downloads |
|------|---------------|
| 2015 |      24,300,000,000     |
| 2016 |      27,900,000,000     |
| 2017 |      34,700,000,000     |
| 2018 |     38,400,000,000     |
| 2019 |     42,100,000,000     |
| 2020 |     56,200,000,000     |
| 2021 |     55,300,000,000     |
| 2022 |     55,600,000,000     |

Since 2015 is a convenient starting point, we can align this data by converting the time to "years since 2015". This is done by subtracting 2015 from each year, resulting in the aligned years 0, 1, 2, ..., 7.

Next, we might want to scale the number of downloads so that 1 on the graph represents "1 billion downloads". We can do this by dividing each value by 1,000,000,000.  

After aligning and scaling our data table has the same information but with more manageable values.  Notice how the labels of each column have been updated to reflect those changes.

| Year Since 2015 | Billions of Downloads |
|--------------|---------------------------|
|      0       |          24.3             |
|      1       |          27.9             |
|      2       |          34.7             |
|      3       |          38.4             |
|      4       |          42.1             |
|      5       |          56.2             |
|      6       |          55.3             |
|      7       |          55.6             |

Not only is the aligned and scaled data easier to read, it is also much easier to graph in a scatterplot.

![](/img/chapter-6/game_download_scatterplot.svg#center)

{{% check %}}
1. Suppose you have data on housing prices from 1956 through 1974.  What would be a convenient starting point and how would you align your data?  {{% answer %}}Several answers are possible, but perhaps the best one would be to use 1950 as the starting year and subtract 1950 from each given year.{{% /answer %}}
1. Suppose you were looking at data involving the national debt, which was $31,419,689,421,557.90 at the end of 2022.  How might you scale the data to make it more manageable? {{% answer %}}Dividing by 1,000,000,000,000 (1-trillion) would give $31.42 trillion which would be easier to work with. {{% /answer %}}
{{% /check %}}


## Modeling with Transformations
You might have noticed that the mobile game data above roughly has the shape of a line.  If we find that a set of data has a shape similar to one of our basic functions, then transformations can be used to shift and stretch that function to make align with the data.  

Let's start by looking at a few transformed functions that you might have seen in prior algebra classes.

### Slope-Intercept Form of a Line
To begin, we take the identity function $f(x)=x$ and stretch it vertically by a factor of $\color{blue}{m}$ and shift it vertically $\color{green}{b}$ units.  The resulting equation, $y=\color{blue}{m}x+\color{green}{b}$, is known as the **slope-intercept** form for a line, where $\color{blue}{m}$ is the slope and $\color{green}{b}$ is the y-intercept.  The figure below will let you experiment with this equation.

{{% geogebra ratio="50%" id_1="Wr52bKrzTkGnlmob" id_2="hBQsE4O1" id_m="hBQsE4O1" %}}
</br>

### Point-Slope Form of a Line
Another transformed version of the identity function is $y=\color{blue}{m}(x-\color{brown}{x_1})+\color{green}{y_1}$.  

This new equation involves a horizontal shift $\color{brown}{x_1}$ spaces, a vertical stretch by $\color{blue}{m}$, and a vertical shift $\color{green}{y_1}$ units.  

The result is a line that passes through the point $(\color{brown}{x_1}, \color{green}{y_1})$ and has a slope of $\color{blue}{m}$.  We refer to this equation as the **point-slope** form of a line.  Feel free to experiment with this equation using the figure below.

{{% geogebra ratio="50%" id_1="kDqggaOWaZNpd7Ni" id_2="PdeIue6n" id_m="PdeIue6n" %}}
</br>

### Vertex Form of a Quadratic
Lastly, consider $y=\color{blue}{a}(x-\color{brown}{h})^2+\color{green}{k}$, which is a transformed version of the square function.  

The horizontal and vertical shifts move the vertex to the point $(\color{brown}{h}, \color{green}{k})$ while the vertical stretch by a factor of $\color{blue}{a}$ influences the concavity of the graph.  

This equation is often referred to as the **vertex form** of a quadratic function.  You can identify the three transformations in the figure below.

{{% geogebra ratio="50%" id_1="BBDfruwxgd3VVqyG" id_2="uTrJWh1K" id_m="uTrJWh1K" %}}

{{% check %}}
1. Write the equation of a line with a slope of $2$ and a y-intercept of $3$.  {{% answer %}}Using the slope-intercept form, $m=2$ and $b=3$ so the equation would be $y=2x+3$.{{% /answer %}}
1. Write the equation for a line passing through the point $(3, 5)$ that has a slope of $4$. {{% answer %}}With the point-slope form the equation would be $y=4(x-3)+5$.  If desired, this could be converted to the slope-intercept form as $y=4x -7$.{{% /answer %}}
1. Write the equation for any quadratic function with a vertex at $(2, -1)$. {{% answer %}}Using the vertex-form, your equation should look similar to $y=a(x-2)^2-1$.  Since $a$ was not specified, any nonzero value will work.{{% /answer %}}
{{% /check %}}


##  Example: Apple Prices
To demonstrate how all this works together, let's use the following raw data from the U.S. Department of Agriculture.

![](/img/chapter-6/apple_data_raw.png#center)

### Step 1: Choosing Variables
With this data, it seems reasonable that the year is independent and the price is dependent.  

### Step 2: Aligning and Scaling Data
To avoid a graph that spans $2009$ units, we choose to align the years by converting them to "years since 2000".  This is done by subtracting $2000$ from each year.  

And we might want to convert the price to "*dollars* per pound" rather than *cents* per pound.  To do this we'll change the scale of the prices by dividing each price by $100$.  

The result of aligning the years and scaling the prices is shown below.

![](/img/chapter-6/apple_data_aligned.png#center)

### Step 3: Using a Scatterplot to Choose a Function
Now that we have aligned and scaled the apple data, let's examine the scatterplot and compare its shape with the shapes of the six basic functions that we know.  

![](/img/chapter-6/apple_data_graph.svg#center)

Does the data look like the identity function or the square function? Perhaps it looks like the reciprocal or the cube root function?

Since this data appears linear, we should be able to model it with a transformed version of the identity function $f(x)=x$.  For simplicity, we will use the slope-intercept form of a line $y = \color{blue}{m} x + \color{green}{b}$ but the point-slope form could be used as well.

### Step 4:  Using Transformations to Fit the Function to the Data
All that remains is to find values of $\color{red}{m}$ and $\color{green}{b}$ that make the model fit the data as closely as possible.

In the figure below, you are free to change both the slope $\color{red}{m}$ and the y-intercept $\color{green}{b}$ until you find a line that fits the data.  Make a note of your equation before continuing.

{{% geogebra ratio="50%" id_1="XNmissvYwqQV8RC8" id_2="m9XFVxlH" id_m="m9XFVxlH" %}}

You may have had trouble finding just one line that fit well.  In fact, good arguments could be made for several lines.  However, the line that is as close as possible to each point is the line $\color{blue}{y} = \color{red}{0.04}x + \color{green}{0.86}$.

Where did this equation come from, and how do we know it is the best?  Well, that's a great question that would take a few weeks in a statistics course to explain fully.  For now, it's enough to know that most graphing utilities have programs that fit equations to data.  That process is called *least squares regression* and we will look at it later in this chapter.  

### Step 5: Constructing the Model
Now that we have an equation, $\color{blue}{y} = \color{red}{0.04}x + \color{green}{0.86}$, it's time to turn that into an actual model.

A model is not just an equation or function, it also includes a description of the variables and their units of measure.  Without an accurate description, the function itself is meaningless since there would be no way to relate it to the real world.

Since our independent variable is time in years since $2000$, we take the liberty of using $t$ in place of $\color{blue}{x}$.  

Similarly, using $p$ instead of $\color{blue}{y}$ will help us remember that the dependent variable represents the price of apples.  We are now ready to write our model.

> According to data provided by the U.S. Department of Agriculture, the price $p$ of apples per pound in dollars can be modeled by the function
> \[ p(t) = 0.04t + 0.86 \]
> where $t$ is the time in years since 2000.

### Step 6:  Using the Model to Make Predictions
We can use this model to estimate the price of apples in any year we want.  For example, to predict the price of a pound of apples in the year 2030 we simply evaluate the function for $t=30$ (remember, $t$ is years *since* 2000.)

\[
  p(30) = 0.04(30) + 0.86 = 2.06
\]

Thus, our model predicts the average price of a pound of apples will be $2.06 in the year 2030.  How accurate is that?  We'll have to wait and see.


## Modeling with Piecewise-Defined Functions
{{% imgcap file="/img/chapter-6/pompidou_1.jpg" title="Photo by Yann Caradec on Flickr" source="https://www.flickr.com/photos/la_bretagne_a_paris/5995530090"%}}

The Pompidou Center in Paris has an amazing escalator. Designed by Italian architect Renzo Piano and British designer Richard Rogers, the 6 story escalator is encased in a glass tube and attached to the outside of the building!

The Pompidou escalator is not a single straight line, but rather several small lines pieced together.  It's an example of a new type of function which we'll call **piecewise-defined** functions.  For instance, to model the Pompidou escalator we shift and stretch several pieces of the identity function and connect them together with horizontal line segments.

![](/img/chapter-6/pompidou_model.gif)

**Piecewise-defined** functions, such as this, give us a lot more flexibility when creating models.  No longer are we required to find a single function; we are now free to construct models in multiple pieces.

When writing piecewise functions, we list the equations for each piece and then specify where each is used.  Consider, for example, the path a bounding ball.  

![https://people.rit.edu/andpph/photofile-misc/stroboscope/bouncing-ball-7791m.jpg](/img/chapter-6/piecewise_bounce.gif#center)

Each bounce is an individual parabola, with its own equation, and its own limited domain.  The piecewise function for this particular ball is

\[ f(x)=\begin{cases}
      -(x+2)(x-2) & \text{if } & 0 \leq x \leq 2 \newline
      -1.2(x-2)(x-5) & \text{if } & 2 <  x \leq 5 \newline
      -1.8(x-5)(x-7) & \text{if } & 5 < x \leq 7
   \end{cases}
\]

To find a value such as $f(4)$, we first compare our x-value $4$ with the three inequalities.  Since $4$ would fit in $2<x \leq 5$, we must use the second equation.  Thus, $f(4)=-1.2(4-2)(4-5) =2.4$.

{{% check %}}
Use the piecewise function above to evaluate the following:

1. $f(0)${{% answer %}}$-(0+2)(0-2) = 4${{% /answer %}}
1. $f(2)${{% answer %}}$-(2+2)(2-2)=0${{% /answer %}}
1. $f(6)${{% answer %}}$-1.8(6-5)(6-7)=1.8${{% /answer %}}
{{% /check %}}


## Looking Ahead
In the final two sections of this book, we will approach mathematical modeling from two different perspectives.  

In [6.2](//chapter-6/6.2) we will have limited data and will need to find a suitable model based on descriptions of the situation and our knowledge of how linear, power, and exponential functions behave.

In the [last section](//chapter-6/6.3) we will explore the practical application of using graphing utilities to create scatterplots and find functions that best fit the data.

Throughout it all, remember that while models are powerful tools, they are not infallible. Careful consideration of underlying factors is crucial for drawing meaningful insights and making accurate predictions.
---
title: "6.2 Algebraic Methods for Modeling"
description: "Mercury levels in large fish like tuna can be over a million times higher than the surrounding waters."
author: "Nolan Mitchell"
type: page
image: "sushi-373588_1280.jpg"
draft: false
tags: ["algebraic-modeling", "identifying-functions-from-descriptions", "linear-functions-constant-rates", "power-functions-proportional", "exponential-functions-constant-percentages", "writing-linear-functions", "writing-exponential-functions", "find-function-from-two-points", "slope-formula", "converting-exponential-models", "continuous-biological-decay", "biological-half-life"]
---

{{% imgcap file="/img/chapter-6/sushi-373588_1280.jpg" title="Image by Design n Print from Pixabay" source="https://pixabay.com/images/id-373588/" %}}


## Introduction
Many people are concerned about the amount of mercury they ingest by eating certain species of large fish like shark, swordfish, and tuna.  Mercury levels in large fish can be over a million times higher than that found in the surrounding waters, posing a possible health risk.

An accurate mathematical model could help people understand those concerns and make informed decisions.  Fortunately, the elimination of substances like mercury from the body are known to have *biological half-lives*, and we know that half-lives can be modeled with exponential functions.  

In this section we will point out key words and phrases, like "half-life", that indicate a scenario might be modeled by a particular type of function.  We'll also cover algebraic methods for finding those equations.


## Identifying Functions from Descriptions
### Linear Functions: Constant Rates
When we studied how functions change in [Chapter 1](/chapter-1/1.6), we saw that the average rate of change formula was nothing more than the slope formula rewritten with function notation.  

Since the slope of a line remains consistent throughout, the key to identifying a linear function is to spot a constant rate of change.

It helps to remember that a **rate** is ratio of two quantities.  Such rates are often described using the word *per* (miles *per* gallon, servings *per* package, dollars *per* hour, feet *per* second) or something equivalent (two tickets *for each* person, ten-thousand steps *every* day, etc.).  

Whatever that constant rate of change is, it will be the slope of the linear function.

### Power Functions:  Proportional Changes
Back in [Chapter 2](/chapter-2/2.2) when we introduced the ideas of direct and inverse proportionality, all the examples explicitly stated the type of proportionality.  Without specific guidance like that, we'll need to look for other clues.

Specifically, if two quantities increase or decrease together, then they might vary directly.  On the other hand, if one goes up while the other goes down, then they could vary inversely.

While those behaviors don't exclusively belong to power functions, they do indicate that a power function should be considered.

### Exponential Functions:  Constant Percentages
As we saw in [Chapter 3](/chapter-3/3.2) exponential functions often appear in scenarios involving growth or decay that follows a multiplicative pattern. 

A distinguishing feature of exponential functions is that they involve a constant **percentage change** over equal intervals.  Almost without exception, if a constant percent change is mentioned within a certain time frame, then the scenario is likely exponential in nature.

{{% check %}}
Identify the type of function (linear, power, or exponential) that would likely be the best model for each scenario.

1. A bacteria culture doubles every $8$ hours.{{% answer %}}The keyword "doubles" implies exponential growth.  Since doubling means growing constantly at 100%, this is exponential{{% /answer %}}
1. The cost of an Uber ride increases $\\$2$ per mile.{{% answer %}}The cost increases at a constant rate of $2 each mile, so this is linear{{% /answer %}}
1. The slower you drive the longer it takes to arrive at your destination.{{% answer %}}This is likely an inversely proportional relationship, so a power function is probably the best model.{{% /answer %}}
1. The more horsepower a car has the faster it accelerates. {{% answer %}}This sounds like a directly proportional relationship, so a power function is probably best.{{% /answer %}}
1. A job offers $3\\%$ raises every year.{{% answer %}}This scenario has a constant percent increase of 3%, so it is exponential{{% /answer %}}
1. A person spends $\\$4$ each day on a bus pass.{{% answer %}}$4 each day is a constant rate of change, so this is linear.{{% /answer %}}
{{% /check %}}

## Writing Functions from Descriptions
Once we've chosen a function model that seems to fit the description, the next task is to write the equation of that function.  

If a starting value is given, then the equations for linear and exponential functions can generally be written without much trouble.  Power functions will require two known values, so we'll delay looking at them for a moment.

### Writing Linear Functions
As we saw in the previous section, the **slope-intercept** form of a linear function is $y=mx+b$, where $m$ is the slope and $b$ is the y-intercept.

To pull the slope and y-intercept out of a description, look for the following:
- The slope $m$ is the constant rate of change of the function.
- The y-intercept $b$ is a starting value, which is the value of $y$ when $x = 0$.

For instance, suppose a gym has an initial sign-up fee of $\\$50$ and monthly membership fee of $\\$20$.  In this scenario, the initial sign-up fee is the y-intercept and the monthly fee is the slope.  Using $m=20$ and $b=50$ the equation of the linear function is:
\[ y = 20x + 50 \]
This linear function allows us to calculate the total cost of the gym membership based on the number of months ($x$).


### Writing Exponential Functions
In [Chapter 3](//chapter-3/3.2) we learned that the general form of an exponential function is $y = ab^x$, where $a$ is the initial value (or starting amount) and $b$ is the base (growth/decay factor).  

So, much like a linear function, we only need two parameters to write the equation of an exponential function.  To extract these from a description, look for the following:
- The initial value $a$ is the value of $y$ when $x = 0$. It represents the starting point of the exponential growth or decay.
- The base $b$ is the factor by which $y$ changes for each unit change in $x$. If $b > 1$, it represents exponential growth; if $0 < b < 1$, it represents exponential decay.  If a percentage rate $r$ is given then the base is $b=1+r$ for growth and $b=1-r$ for decay.  If the change takes $c$ units to occur, then $x$ should be divided by $c$, which is how we obtained the half-life and doubling-time equations.

As a simple example, suppose an aspiring social influencer has $400$ followers and expects that number to grow by $3\\%$ every month.  Then $y=400(1.03)^x$ allows us the calculate how many followers they have after $x$ months.

{{% check %}}
1. Suppose a different gym has a $\\$75$ initial fee and $\\$10$ monthly dues.  Write an equation for the total cost. {{% answer %}} $y=10x+75$ where $x$ is months.{{% /answer %}}
1. Suppose the aspiring social influencer above realizes their number of followers increases by $3\\%$ every $2$ months. Write an equation for the number of followers they have after $x$ months.{{% answer %}}$y=400(1.03)^{x/2}$ where $x$ is months. {{% /answer %}}
{{% /check %}}


## Creating Functions from Two Points
In many cases we may have to determine the parameters of a function from two pairs of data.  This can apply to any of the three types of functions we're looking at in this section.

### Find a Linear Function from Two Points
The first step in finding a linear function through two points is to use the slope formula 
\[m=\frac{y_2-y_1}{x_2-x_1}\] 

Once we have the slope in hand we can finish the process with either the point-slope form or the slope-intercept form.  Many people prefer the slope-intercept form since it is more familiar, but the point-slope form is actually easier to work with.  We'll do the same example both ways and you can decide for yourself.

For our example, let's use the points $(2,5)$ as $(x_1,y_1)$ and $(6,-1)$ as $(x_2,y_2)$.  We'll start with the slope

\[
  \begin{align}
  m &= \frac{y_2-y_1}{x_2-x_1} && \small \color{#5fa2ce} {\text{slope formula}} \newline
  &= \frac{-1 - 5}{6-2} && \small \color{#5fa2ce} {\text{insert coordinates of the two points}} \newline
  &= \frac{-6}{4} && \small \color{#5fa2ce} {\text{evaluate the subtractions}} \newline
  &= -\frac{3}{2} && \small \color{#5fa2ce} {\text{reduce the fraction}} \newline
  \end{align}
\] 

To finish this with the slope-intercept form we need to find the y-intercept $b$.  This is done by taking putting the coordinates of either point into the equation and solving for $b$.  We will use $(2,5)$ and, of course, $m = \frac{-3}{2}$.

\[
  \begin{align}
    y &= m x  + b && \small \color{#5fa2ce} {\text{slope-intercept form}} \newline
    5 &= -\frac{3}{2}(2)+b && \small \color{#5fa2ce} {\text{insert the slope and the coordinates of the point}} \newline
    5 &= -3+b && \small \color{#5fa2ce} {\text{simplify}} \newline
    8 &= b && \small \color{#5fa2ce} {\text{add $3$ to both sides}}
  \end{align}
\]

We now have $y=-\frac{3}{2}x+8$ as our linear model in the slope-intercept form.

Since the point-slope form only requires the coordinates of a point and the slope, we can get the equation just by substituting.  Here we will also use $(2,5)$ and $m = \frac{-3}{2}$.

\[
  \begin{align}
    y &= m(x-x_1)  + y_1 && \small \color{#5fa2ce} {\text{point-slope form}} \newline
    y &= -\frac{3}{2}(x-2)+5 && \small \color{#5fa2ce} {\text{insert the slope and the coordinates of the point}}
  \end{align}
\]

We now have $y=-\frac{3}{2}(x-2)+5$ as our linear model in the point-slope form.  It is important to point out that these are the same exact equation, just in different formats.  This can be seen clearly if we start with point-slope form, distribute the slope and simplify.

\[
  \begin{align}
    y &= -\frac{3}{2}(x-2)+5 && \small \color{#5fa2ce} {\text{point-slope form}} \newline
    y &= \left(-\frac{3}{2}\cdot x\right)-\left(-\frac{3}{2}\cdot 2\right) + 5 && \small \color{#5fa2ce} {\text{distribute the slope}} \newline
    y &= -\frac{3}{2}x + 3 + 5 && \small \color{#5fa2ce} {\text{simplify the multiplication}} \newline
    y &= -\frac{3}{2}x + 8 && \small \color{#5fa2ce} {\text{simplify the addition}}
  \end{align}
\]

The end result is the same slope-intercept form we found earlier.  This process can always be used to find a line through any two points, provided both points have different $x$-coordinates.  If the points have the same $x$-coordinate then we cannot create a linear function since those points would not pass the vertical line test.

### Find a Power Function from Two Points
Suppose we are asked to find a standard power function through the points $(6, 10)$ and $(2, 5)$.  Since power functions are not lines, we cannot use the slope formula and must employ different techniques.

One thing that will help is remembering that each point has an $x$ and a $y=f(x)$ coordinate. Substituting those values into the standard power function equation $f(x)=kx^p$ will give us a pair of equations to work with.

![](/img/chapter-6/substitution_power.svg#center)

 Since there are two unknown values, $k$ and $p$, we need to eliminate one of them in order to solve for the other.  Notice that if we form a ratio of our equations then $k$'s will cancel.  That's our first step.

\[
\begin{align}
\frac{10}{5} &= \frac{k (6)^{p}}{k (2)^{p}} && \small \color{#5fa2ce}{\text{Form a ratio of the two equations.}} \\newline
\frac{10}{5} &= \frac{6^{p}}{2^{p}} && \small \color{#5fa2ce}{\text{Cancel $k$'s.}} \\newline
\frac{10}{5} &= \left(\frac{6}{2}\right)^p && \small \color{#5fa2ce}{\text{Use the rule $\frac{a^x}{b^x}=\left(\frac{a}{b}\right)^{x}$.}} \\newline
2 & = 3^p && \small \color{#5fa2ce}{\text{Reduce the fractions.}}
\end{align}
\]

With $k$ out of the way momentarily, we can focus on finding $p$.  Since $p$ is in the exponent, we'll need to use logarithms to find it.

\[
\begin{align}
\ln(2) &= \ln \left(3^{p}\right) && \small \color{#5fa2ce}{\text{Apply a logarithm to both sides.}} \\newline
\ln(2) &= p \cdot \ln (3) && \small \color{#5fa2ce}{\text{Use the power rule for logarithms.}} \\newline
\frac{\ln(2)}{\ln(3)} &= p && \small \color{#5fa2ce}{\text{Divide to isolate $p$.}} \\newline
p &\approx 0.6309 && \small \color{#5fa2ce}{\text{Decimal approximation.}}
\end{align}
\]

By putting $p=0.6309$ back into either of our original two equations we'll be able to determine $k$.

\[
\begin{align}
10 &= k (6)^{p} && \small \color{#5fa2ce}{\text{Choose one of the original equations.}} \\newline
10 &= k (6)^{0.6309} && \small \color{#5fa2ce}{\text{Substitute $p=0.6309$}} \\newline
10 &= k \cdot 3.097 && \small \color{#5fa2ce}{\text{Evaluate the power.}} \\newline
\frac{10}{3.097} &= k && \small \color{#5fa2ce}{\text{Divide both sides by $3.097$}} \\newline
k &= 3.229 && \small \color{#5fa2ce}{\text{Evaluate the division.}}
\end{align}
\]

With both $k$ and $p$ in hand, we can now write the equation for our power function. 

\[
  f(x)=3.229x^{0.6309}
\]

Keep in mind that, since power functions generally exist only when $x \gt 0$, we should check that both $x$-coordinates are positive before starting this process.  Additionally, since logarithms were involved in our solving process, the two $y$-coordinates should be non-zero and have the same sign.  For the most part, expect to find power functions only when both points are in the first quadrant.


### Find an Exponential Function from Two Points
Suppose we are asked to find an exponential function that passes through the points $(1, 12)$ and $(3, 27)$, how is that done?  The process begins the same way it did with a power function--inserting the coordinates into the standard exponential function $f(x)=a \thinspace b^{x}$ to make two equations. 

![](/img/chapter-6/substitution_exponential.svg#center)

Forming a ratio of the two equations worked before, so let's try that again.  We'll put the equation with the larger numbers on top, which should help us reduce fractions along the way.

\[
\begin{align}
\frac{27}{12} &= \frac{ a  \thinspace  b^{3}}{a  \thinspace  b^{1}} && \small \color{#5fa2ce}{\text{Form the ratio of the two equations.}} \newline
\frac{27}{12} &= \frac{b^{3}}{b^{1}} && \small \color{#5fa2ce}{\text{Cancel the $a$'s.}} \newline
\frac{27}{12} &= b^{2} && \small \color{#5fa2ce}{\text{Simplify the powers.}} \newline
\frac{9}{4} &= b^{2} && \small \color{#5fa2ce}{\text{Reduce the fraction.}} \newline
\pm \sqrt{\frac{9}{4}} &= b   && \small \color{#5fa2ce}{\text{Take $\pm \sqrt{\text{  }}$ of both sides}} \newline
\pm \frac{3}{2} &= b  && \small \color{#5fa2ce}{\text{Simplify}}
\end{align}
\]

Normally getting two answers could cause a problem, but in this case we know something extra.  We are trying to find the base of an exponential function, and the base of an exponential is never negative.  So the correct value must be $b=\frac{3}{2}$.

This is only half of the solution; we also need to know what $a$ is.  To find that, we'll substitute $b$ back into one of our equations.  As before, either one will work but we'll choose the one with the smaller values as is a bit simpler.

\[
\begin{align}
12 &= a  \thinspace  b^{1} && \small \color{#5fa2ce}{\text{Equation #1}} \newline
12 & = a \frac{3}{2} && \small \color{#5fa2ce}{\text{Substitute $b = \frac{3}{2}$}} \newline
\frac{2}{3} \cdot 12 &= a && \small \color{#5fa2ce}{\text{Multiply by $\frac{2}{3}$}} \newline
8 &= a && \small \color{#5fa2ce}{\text{Simplify}} \newline
\end{align}
\]

Now that we know the values for $a$ and $b$, we can finally say that

\[f(x)=8 \left(\frac{3}{2} \right)^{x}\]

is the exponential function that passes through the points $(1, 12)$ and $(3, 27)$.


## Convert Between Exponential Models
In the previous example we used the standard exponential model $f(x)=a \thinspace b^{x}$, where $b=1+r$, but we know from [Chapter 3](//chapter-3/3.2#looking-ahead) that there are several different exponential forms.  Why didn't we use one of those?

The answer is that we certainly could have.  The format we use doesn't really matter since its possible to switch between any of them.  In particular, the standard model $f(x)=a \thinspace b^{x}$ and the continuous growth model $f(t)=a \thinspace e^{k t}$ are equivalent (and are the most commonly used).  Here's how you convert from one to the other.

\[
  \begin{align}
   a \thinspace b^{\ x} &\Longrightarrow a \thinspace e^{\ k \  t} && \small \color{#5fa2ce}{\text{by setting $k = \ln (b)$}} \newline \newline
   a \thinspace e^{\ k \ t} &\Longrightarrow a \thinspace b^{\ x} && \small \color{#5fa2ce}{\text{by setting $b=e^{\ k}$}} \newline
  \end{align}
  \]

Either form can be used for any application.  We often make the decision based on convenience and whether its preferable to emphasize the growth factor $b$ or the continuous growth rate $k$ in a given scenario.  


{{% check %}}
1. Use the identity $b=e^{k}$ to rewrite $f(t)=2 \thinspace e^{-0.356 t}$ in the standard exponential model form $f(x)=a \thinspace b^{x}$. {{% answer %}}Since $e^{-0.356}=0.7$, the equivalent standard model is $f(x)=2(0.7)^{x}$.{{% /answer %}}
1. Use the identity $k = \ln (b)$ to rewrite $f(x)=138(1.493)^{x}$ as a continuous growth exponential function of the form $f(t)=a \thinspace e^{k  t}$. {{% answer %}}Since $\ln(1.493)=0.4$, the equivalent continuous growth model is $f(t)=138 \thinspace e^{0.4 t}$.{{% /answer %}}
{{% /check %}}


## Create Exponential Models

### Continuous Biological Decay
{{% imgcap file="/img/chapter-6/sushi-373588_1280.jpg" title="Image by Design n Print from Pixabay" source="https://pixabay.com/images/id-373588/" %}}

Let's return to the example that at the start of this section.  The Mercury that small fish eat gets collected in large predatory fish such as shark, swordfish, and tuna that live longer.{{% sidenote "fish"%}}![](/img/chapter-6/MercuryFoodChain.svg#center){{% /sidenote %}}  Mercury levels in large fish can be over a million times higher than that found in the surrounding waters.  

The U. S. Environmental Protection Agency (EPA) believes that if a person has a blood mercury level under 5.8 micrograms per liter ($\mu$g/L) then they are relatively safe and should see no adverse effects.

Suppose the Mercury level in your blood is at 15 $\mu$g/L.  If 5 days later it has only dropped to 14  $\mu$g/L, how long will it take to reach a safe level?

If we assume mercury leaves your body in a continuous fashion, then we can try to find a model of the form $f(t)=ae^{k t}$.  From the information given we can find $k$ by solving  $14=15e^{k \thinspace 5}$.

\[ \begin{align}
14 =& 15e^{k \thinspace 5} \newline
\frac{14}{15} &= e^{5 \thinspace  k} && \small \color{#5fa2ce} {\text{Divide both sides by $15$ to isolate the exponential.}} \newline
\ln\left(\frac{14}{15}\right) &= \ln\left(e^{5 k}\right) && \small \color{#5fa2ce} {\text{Apply the natural log $\ln$ to both sides.}} \newline
\ln\left(\frac{14}{15}\right) &= 5 k && \small \color{#5fa2ce} {\text{Use the inverse relationship $\ln(e^{x})=x$.}} \newline
\frac{\ln\left(\frac{14}{15}\right)}{5} &= k && \small \color{#5fa2ce} {\text{Divide both sides by $5$.}} \newline
k  &\approx  -0.0138 && \small \color{#5fa2ce} {\text{Use a calculator to find a decimal approximation.}} 
\end{align}\]

From this we see that the mercury concentration can be modeled by $f(t)=15e^{-0.0138  \thinspace  t}$.  

{{% check %}}
1. Now that we know the model is $f(t)=15e^{-0.0138 \thinspace t}$, how do we figure out the amount of time it will take to reach a safe level of  5.8$\mu$g/L?
{{% answer %}}We need to set $f(t)=5.8$ and solve the equation for $t$.{{% /answer %}}
{{% /check %}}
We know that if your blood mercury level is initially at 15 $\mu$g/L, then the mercury concentration can be modeled by the function $f(t)=15e^{-0.0138  \thinspace t}$ where $t$ is time in days.  

To find out how long it will take to reach a safe level of 5.8 $\mu$g/L, we need to find $t$ so that $f(t)=5.8$.

\[
  \begin{align}
  5.8 &=  15e^{-0.0138 \thinspace  t} \newline
\frac{5.8}{15}  &=  e^{-0.0138 \thinspace  t} && \small \color{#5fa2ce} {\text{Divide both sides by $15$ to isolate the exponential.}} \newline
\ln\left(\frac{5.8}{15}\right)  &=  \ln\left(e^{-0.0138 t}\right) && \small \color{#5fa2ce} {\text{Apply the natural log $\ln$ to both sides.}} \newline
\ln\left(\frac{5.8}{15}\right)  &=  -0.0138 t && \small \color{#5fa2ce} {\text{Use the inverse relationship $\ln(e^{x})=x$.}} \newline
\frac{\ln\left(\frac{5.8}{15}\right)}{-0.0138}  &=  t && \small \color{#5fa2ce} {\text{Divide both sides by $-0.0138$.}} \newline
t  &\approx  68.85 && \small \color{#5fa2ce} {\text{Decimal approximation.}}
\end{align}
\]

It appears that it will take roughly 69 days for the blood mercury concentration to return to a safe level.

{{% check %}}
1.  How would this process have changed if you were asked to find the biological half-life of mercury in the blood stream?
{{% answer %}}To find the half-life we would need to solve for $t$ with $f(t)=\frac{1}{2} a$ where $a$ is the initial concentration.  The solving steps would be nearly identical to what was done above.{{% /answer %}}
{{% /check %}}

### Biological Half-Life

It is very common to use the half-life model $f(x)=a\left(\frac{1}{2}\right)^{x/c}$ to describe the biological decay of substances in the body.  To change our continuous decay model for mercury into a half-life model, we must find $t$ so that $f(t)=\frac{1}{2}  a$, where $a$ is the initial concentration.

\[
  \begin{align}
\frac{1}{2} \cdot 15  &=  15 e^{-0.0138 t} && \small \color{#5fa2ce} {\text{Start with continuous decay model from above.}} \newline
\frac{1}{2}  &=  e^{-0.0138 t} && \small \color{#5fa2ce} {\text{Divide both sides by $15$ to isolate the exponential.}} \newline
\ln\left(\frac{1}{2}\right) &= \ln(e^{-0.0138 t}) && \small \color{#5fa2ce} {\text{Apply the natural log $\ln$ to both sides.}} \newline
\ln\left(\frac{1}{2}\right) &= -0.0138 t && \small \color{#5fa2ce} {\text{Use the inverse relationship $\ln(e^{x})=x$.}} \newline
\frac{\ln\left(\frac{1}{2}\right)}{-0.0138} &= t && \small \color{#5fa2ce} {\text{Divide both sides by $-0.0138$.}} \newline
t  &\approx  50.23 && \small \color{#5fa2ce} {\text{Use a calculator to find a decimal approximation.}}
\end{align}
\]

This shows that the half-life of mercury in the body is about 50 days.  By taking $c=50$, we conclude that the function

\[
  f(x)=15\left(\frac{1}{2}\right)^{x/50}
\]

is the half-life model for mercury concentration that is equivalent to our earlier continuous decay model.  Both produce the same values, they are just written in different formats.


## Looking Ahead
In our final section we will use technology to find models that fit larger sets of data rather than doing the work by hand.  Even so, the basic process will be the same as what we've done in the past two sections. 

We will always start by comparing the properties of the data with the behaviors of functions we know so that we can choose an appropriate function model that can be used to predict unknown values.

If the model predicts unreasonable values that do not make any sense, then we should try to explain how we know the result is an error and why it might have occurred.  An analysis of the errors can often lead to the construction of a more robust model. 
---
title: "6.3 Using Technology to Model Data"
description: "Throughout the vast grasslands of Nevada live herds of wild mustangs." 
author: "Nolan Mitchell"
type: page
image: "horses.jpg"
draft: false
tags: ["using-technology-for-modeling", "regression-analysis", "least-squares-regression", "keplers-third-law", "allometry", "checking-multiple-models", "standing-mile", "logarithmic-regression", "logistic-regression", "quadratic-regression", "power-regression", "polynomial-regression", "model-breakdown", "wild-mustangs", "graphing-calculator", "ti-83-ti-84"]
---

{{% imgcap file="/img/chapter-6/horses-61158_1280.jpg" title="Photo Steppinstars from Pixabay " source="https://pixabay.com/images/id-61158/"%}}


## Introduction
Throughout the vast grasslands of Nevada live herds of wild horses known as "mustangs".  The Bureau of Land Management (BLM) has been diligently monitoring the number of mustangs and the land's capacity to support them since 1971. 

A function model of that data could be used to predict the future size of the mustang herds, helping the BLM plan actions to help the herds thrive. 

In this section, we will explore the process of creating function models using large data sets and then we'll return to this scenario.  

## General Strategy
In the previous section we found functions by hand in situations where only two data points were known.  Creating a functional model from a larger dataset involves several steps including borrowing a powerful tool from statistics called *regression*.  

While this might sound intimidating, we will utilize technology to do the hard lifting, leaving us free to focus on the analysis. Here's our general strategy:

1. **Align and/or Scale the Data**: Before performing regression, consider [aligning and/or scaling](/chapter-6/6.1/#aligning-and-scaling-data) the data to make it easier to work with. If you encounter an "overflow" error when running regression in a later step, consider coming back to this step and adjusting your data to more manageable values.
2. **Make a Scatterplot of the Data**: A [scatterplot](/chapter-6/6.1/#scatterplots) will help you visually spot trends in the data points, providing insight into the relationship between the variables.
3. **Compare the Shape of the Scatterplot to Known Functions**: By comparing the scatterplot's shape to the shapes of functions we are familiar with (such as linear, exponential, or polynomial), we can get a rough idea of which function might be the best fit.
4. **Use Software to Run Regressions for Different Functions**: To find the best-fitting model more precisely, use a graphing calculator or other software to run regressions for the various functions you think match the shape of the data.
5. **Graph the Functions with the Data**: After running regressions, plot the resulting functions on the scatterplot alongside the actual data to visually assess the accuracy of each model.
6. **Investigate Potential Model Breakdowns**: We'll examine instances where the model might not accurately capture certain aspects of the data. This investigation helps in refining the model and understanding its limitations.

While a graphing calculator or other software can give you equations and values (many of which are discussed in a full class on statistics), it can't see the data.  It can, for example, find the line that fits the data best, but it can't decide if a linear model is an appropriate choice--that's up to you.  

It's also important to point out that even when we can identify patterns and show a correlation in data, that doesn't necessarily imply causation between the two variables.  For instance, we saw that time of day is connected to the number of observed tornados, but that doesn't mean the clock generates tornadoes.  Establishing causality involves carefully designed and controlled experiments, something we'll touch on in the next example.


### Example: Kepler's Third Law
{{% imgcap file="/img/chapter-6/solar-system-11111_1280.jpg" title="Image by NASA" source="https://en.wikipedia.org/wiki/File:Solar_sys8.jpg" %}}

When Johannes Kepler came up with his theory for the orbit of planets in 1618, he was only aware of six planets:  Mercury, Venus, Earth, Mars, Jupiter and Saturn.  Kepler based his theory on measurements taken years earlier by Tycho Brahe who spent his life making observations with the naked eye--he died 7 years before the telescope was invented!

Kepler struggled for 17 years to find a relationship between the time it takes a planet to orbit the Sun (called its orbital period) and its average distance from the Sun (called the semi-major axis).  Let's see if we can't do something similar in less than 17 **minutes**.  We will show instructions for using a Texas Instruments graphing calculator, but other calculators and software should have similar commands available.

The table below lists the periods and distances for the 8 major planets in our solar system.  

| **Planet** | **Distance from Sun (AU)** | **Orbital Period (Years)** |
| --- | --- | --- |
| Mercury | 0.39 | 0.24 |
| Venus | 0.72 | 0.62 |
| Earth | 1 | 1 |
| Mars | 1.52 | 1.88 |
| Jupiter | 5.20 | 11.86 |
| Saturn | 9.54 | 29.46 |
| Uranus | 19.19 | 84.07 |
| Neptune | 30.06 | 164.81 |

We start by entering the data into a calculator

![](/img/chapter-6/kepler_data.svg#center)  

and taking a look at the scatterplot.  Using `9: ZoomStat` gives a good viewing window.

![](/img/chapter-6/kepler_scatterplot.svg#center)

The scatterplot looks like it could be an increasing power function, so we run `PwrReg`

![](/img/chapter-6/kepler_equation.svg#center)

and get back the equation $y=x^{1.5}$.  Graphing this equation along with our scatterplot shows that it is a very good fit.

![](/img/chapter-6/kepler_fit.svg#center)

Kepler found this same equation over 400 years ago.  When he unveiled his findings, Kepler stated, "It is absolutely certain and exact that the proportion between the periodic times of any two planets is precisely the sesquialternate proportion of the mean distances." The term 'sesquialternate proportion' is a way of expressing the power of $3/2$ using the language of proportionality, a concept we previously explored in [Chapter 2](/chapter-2/2.2/#direct-variation).

All that remains is for us to turn this into a model by adding a description to our equation.

> The orbital period $P$ of a planet, in years, can be modeled by the equation
> \[ P =  D^{3/2} \]
> where $D$ is the distance of the planet from the Sun in astronomical units (AU).

Remember that including the units of the variables is an essential part of making a model.  If the data had been measured in days instead of years, or miles instead of astronomical units, then the equation would be different.  Understanding the units and their relevance in the model is crucial when using the model to make predictions.

{{% check %}}
Kepler discovered his third law by studying planets.  Below are the values for some objects in our solar system that are not planets.  
| **Celestial Object** | **Distance from Sun (AU)** | **Orbital Period (Years)** |
| --- | --- | --- |
| Chiron (a centaur) | 13.71 | 50.76 |
| Haley's Comet | 17.80 | 75.30 |
| Pluto (a dwarf planet) | 39.48 | 248.07 |
| Eris (a dwarf planet) | 68.01 | 560.90 |

Does Kepler's 3rd law work for these objects as well?  In other words, if you insert a value for $D$ into the equation $P =  D^{3/2}$ does the resulting value for $P$ match the table?{{% answer %}} Yes, Kepler's 3rd law works for all of these objects, not just planets.{{% /answer %}}
{{% /check %}}


### Example: Allometry
{{% imgcap file="/img/chapter-6/james-youn-IA2pNk_dyqw-unsplash.jpg" title="Photo by James Youn on Unsplash" source="https://unsplash.com/photos/IA2pNk_dyqw" %}}

In the natural sciences, many aspects of an organism's life are connected to its size. Life expectancy, brain size, gestational period, metabolic rate, just to name a few, all depend on body mass. The study of the relationship of body size to shape, anatomy, physiology and behavior is called "allometry".

For example, the accompanying table shows the weight and cruising speed of several birds.  

![](/img/chapter-6/bird_data.svg#center)

A scatterplot of the data suggests that a slowly increasing power function with $0<p<1$, which would have a shape similar to the square root function, might model the data well.  

{{% geogebra ratio="33.33%" id_1="ncguvQHLwhXvamtn" id_2="ZnU6AiQr" id_m="ZnU6AiQr" %}}
</br>

Running the `PwrReg` program gives $f(x) =  23.66 x^{0.2}$ as the best fit, confirming our initial observation that $0 < p < 1$.

We can use this function to predict the flying speed of other animals based on their weight.  For instance, the giant golden-crowned flying fox is one of the heaviest bat species, with some individuals weighing up to $3.1$ pounds.  Our model predicts that a $3.1$ pound flying fox has an optimal flying speed of $f(3.1) =  23.66 (3.1)^{0.2}=29.67 \text{ mph}$.

{{% check %}}
Check to see if this function works for an airplane like the Cessna 172 Skyhawk, which has a cruising speed of $140 \text{ mph}$ and weighs $2300 \text{ pounds}$.
{{% answer %}}This model predicts a flying speed of \[ f(2300) =  23.66 (2300)^{0.2} = 111.27 \text{ mph} \] which, surprisingly, isn't too far off the actual value of $140 \text{ mph}$.  {{% /answer %}}
{{% /check %}}


## Check Multiple Models
In the last two examples we identified the scatterplots as a power functions.  This isn't surprising, since power functions can grow quickly (when $p \gt 1$), grow slowly (when $0 \lt p \lt 1$) and decay (when $p \lt 0$).

![](/img/chapter-2/powers_all_3.svg#center)

However, it would have been better to check multiple function models.  For example, the scatterplot below looks similar to Kepler's data, but no matter which values you choose for $k$ and $p$, no power function will ever fit the curvature of the data.

{{% geogebra ratio="33.33%" id_1="LLBa2iAu6P4mcBKq" id_2="Rv4EWJmR" id_m="Rv4EWJmR" %}}

In particular, it's very easy to mistakenly identify data with exponential, logarithmic or even logistic trends as being power functions.  You can see the similarities in the three data sets below.

![](/img/chapter-6/scatterplots.svg#center)

It's always best practice to try more than one type of function model to see which fits best.


{{% check %}}
The following scatterplots have shapes similar to functions that have been discussed in earlier chapters.  Discuss which functions could fit the data well.

1. &nbsp; ![](/img/chapter-6/scatterplot_sqrt.svg#center) {{% answer %}}This data is similar to a power function with a power of $0<p<1$, such as the square root function.  This shape is also visually similar to a logarithmic function.  Both should be tested to see which is a better fit.{{% /answer %}}
1. &nbsp; ![](/img/chapter-6/scatterplot_linear.svg#center) {{% answer %}}This data has the shape of a linear function.  No other functions have this shape so it would be our best choice.{{% /answer %}}
1. &nbsp; ![](/img/chapter-6/scatterplot_reciprocal.svg#center) {{% answer %}}This data has the shape of a power function with a power of $p<0$, such as the reciprocal function.  This shape is also similar to an exponential decay function.  Both should be tested to see which is a better fit.{{% /answer %}}
1. &nbsp; ![](/img/chapter-6/scatterplot_quadratic.svg#center) {{% answer %}}This data looks similar to a quadratic function.  It could potentially be a higher degree polynomial with an even degree.{{% /answer %}}
{{% /check %}}


### Example: Standing Mile
![](/img/chapter-6/standing_mile.gif#center)

In the summer of 2005, Road and Track magazine gathered 13 cars, 1 motorcycle, and a Navy F/A-18 Hornet fighter jet for a one-mile long acceleration test at the Lemoore Naval Air Base in California.  This started a trend and "standing mile" events are now held around the country.

At this event, the first-placed Lola Champ Car (yellow car on the bottom right) crossed the finish line in just 24.2 seconds!  The following table show how long it took the Lola to reach different speeds.

| Time (sec) | Speed (mph) |
| ----- | ----- |
| 3.1 | 60 |
| 5.6 | 100 |
| 8.6 | 150 |
| 9.9 | 161.4 |
| 22 | 200 |
| 24.2 | 203.3 |

Can we find a function that fits this data?  As always, we start by creating a scatterplot.

![](/img/chapter-6/standing_mile_scatterplot.png#center)

Looking at the scatterplot helps us narrow down the list of possible models.  For instance, the data does not appear to be linear, so no attempt will be made at running `LinReg` and trying to fit a line to the data.

{{% check %}}
Of all the functions you've seen, which one(s) do you think have a shape similar to the data in this scatterplot?
{{% answer %}}Of the functions we have seen, this might match a logarithmic function, a logistic function, or even a quadratic.  In a moment we will try each of these and choose the one that appears to fit best.{{% /answer %}}
{{% /check %}}

The equations and graphs for natural log regression `LnReg`, logistic regression `Logistic`, and quadratic regression `QuadReg` are shown below.  

![](/img/chapter-6/standing_mile_regressions.png#center)

All three functions are reasonably close to all of the data points, so how do we pick the best?  We'll have to rely on our personal knowledge about how vehicles behave as they accelerate to their top speed.  We would expect the speed to rise quickly and then level off at the top speed.  The only model that has this behavior is the logistic function, so we choose it as the best fit.


### Example:  K-12 Administration
The majority of teachers in primary education (K-12) are women. However, positions in K-12 administration, such as principal or superintendent, are more frequently held by men. The following data, from Indiana's department of education, shows the percent of women in K-12 administration. {{% marnote %}}![](/img/chapter-6/woman-2773007_640.jpg) [Image by ernestoeslava on Pixabay](https://pixabay.com/images/id-2773007/){{% /marnote %}}

| Year | % of women administrators |
| ----- | ----- |
| 1990 | 18.3 |
| 1992 | 22.8 |
| 1994 | 26.7 |
| 1996 | 30.2 |
| 1998 | 32.5 |
| 2000 | 34.4 |
| 2002 | 36.3 |
| 2004 | 37.8 |
| 2006 | 39.3 |

A scatterplot of the data shows an increasing, concave down trend.

![](/img/chapter-6/educator_scatterplot.png#center)

Due to the shape, we can eliminate linear and exponential models from consideration.

{{% check %}}
Based on the shape of the data in the scatterplot, which types of functions do you think could be the best fit? {{% answer %}}The shape is similar to a logarithmic function, but it is also reminiscent of a power function with a power $0<p<1$, like the square root function.  It might also be worthwhile to see if a logistic function might fit.{{% /answer %}}
{{% /check %}}

Based on the curve of the data, it seems that we should run a logistic regression `Logistic`, a logarithmic regression `LnReg`, and a power regression `PwrReg`.  

Before running any regressions, we often align the data first.  In this case, it would seem natural to let $x$ represent years since 1990.  However, that would give us a value of $x=0$ and both logarithmic and power regression need $x$-values larger than $0$.  To adjust for that, we'll let $x$ represent years since 1989.  Now all of our $x$ values are positive.   

| Years since 1989 | % of women administrators |
| ----- | ----- |
| 1 | 18.3 |
| 3 | 22.8 |
| 5 | 26.7 |
| 7 | 30.2 |
| 9 | 32.5 |
| 11 | 34.4 |
| 13 | 36.3 |
| 15 | 37.8 |
| 17 | 39.3 |

The results of the three chosen regressions are shown below.

![](/img/chapter-6/educator_regressions.png#center)

All three models match the data fairly well.  However, the logistic function has a significant flaw.  Remember that the carrying capacity $c$ is a horizontal asymptote.  In this case, the logistic model would never allow the percent of female administrators to exceed $40.866\\%$.  

Consequently, either the logarithmic or the power models might be better predictors of future trends.


### Example: Redmond, Oregon
{{% imgcap file="/img/chapter-6/6625662063_a45070af3b_b.jpg" title="Photo of Smith Rock by Unsettler on Flickr" source="https://flic.kr/p/b6ufuP" %}}

With stunning mountain views, snowy winters, warm summers and world-class outdoor activities, Redmond is
one of the fastest growing cities in Oregon. The following table shows the population growth since 1970.

\[
  \begin{array}{|c|c|}
    \hline
    \text{Year} & \text{Population} \newline
    \hline
    1970 & 3721  \newline
    \hline
    1980 & 6452 \newline
    \hline
    1990 & 7165 \newline
    \hline
    2000 & 13481 \newline
    \hline
    2010 & 26216 \newline
    \hline
  \end{array}
\]

Before choosing a model we should plot the data and see what it looks like.  To make it easier, we will use years *since* 1970 rather than the actual year.

![](/img/chapter-6/redmond_regression_1.png#center)

The data appears to increase, slow down, and then increase again, like a polynomial function.  In general, if you notice a pattern with $n$ turns in the data you can model it effectively with an $n+1$ degree polynomial. Since the data appears to have two turns, a cubic polynomial might be a good fit.  

Running `CubicReg` on a calculator

![](/img/chapter-6/redmond_regression_2.png#center)

gives a cubic polynomial which does fit the data well, coming very close to most of the data points.

But what if we try a higher degree polynomial? Most calculators can do up to 4th degree polynomial regression `QuarticReg` and programs are available that can do polynomials with even higher degrees.  The results of running `QuarticReg` 

![](/img/chapter-6/redmond_regression_3.png#center)

show that the quartic polynomial is a perfect fit!  It hits every single point precisely.

So the 4th degree polynomial must be a better model than the 3rd degree polynomial, right?  Maybe not.

Notice that our quartic model has a negative leading coefficient.  Because of that the right side of the graph must eventually come down. Zooming out makes this easier to see.

![](/img/chapter-6/redmond_regression_4.png#center)

While the quartic model could be a good model for a few years, it is obviously a poor predictor for the population of Redmond in the distant future, especially since it eventually gives negative population values (and you can't have less than $0$ people living somewhere).  

Keeping an eye on when your model might predict unreasonable values is always important.  It's even a good idea to specify a particular domain for your model.  For instance, if the Census counts the population every 10 years, there's no reason to keep this model any longer than that.  

{{% check %}}
The equation of our cubic model for Redmond's population is
\[y=0.70x^3-23.89x^2+393.10x+3818.21\]
and the quartic model's equation is 
\[y=-0.028x^4+2.97x^3-79.38x^2+798.16x+3721\]
Use those to predict the population of Redmond in 2020.
{{% answer %}}The year 2020 corresponds to $x=50$.  Evaluating both equations gives
\[y=0.70(50)^3-23.89(50)^2+393.10(50)+3818.21=51248\]
and
\[y=-0.028(50)^4+2.97(50)^3-79.38(50)^2+798.16(50)+3721=41429\]
The actual population in 2020 was 33,274 so neither of our models produced a good prediction for 2020. In fact, from 1990 to 2010 a linear model is more accurate.{{% /answer %}}
{{% /check %}}


### Example: Wild Mustangs
{{% imgcap file="/img/chapter-6/horses-61158_1280.jpg" title="Photo Steppinstars from Pixabay " source="https://pixabay.com/images/id-61158/"%}}
We're now ready to return to the example at the start of this section.  Every year the BLM conducts aerial surveys in an effort to get an accurate count of the mustangs in Nevada.

When the number of horses exceeds a sustainable level, the BLM takes action by gathering animals from overpopulated herds and making them available to the public for adoption. 

The table below gives the total number of mustangs in Nevada from 2000 to 2011.

![](/img/chapter-6/horse_data.png)

Notice that the population decreased and then started to increase, so it seems reasonable that a quadratic function might fit the data.

Since this is our final example, we will approach this two ways.  First we will try using transformations to make a quadratic model in the vertex form like we did in [section 6.1](/chapter-6/6.1#vertex-form-of-a-quadratic).  Then we'll use regression and will show all the steps for using a Texas-Instruments TI83 or TI84 graphing calculators.  Since a quadratic function has $3$ parameters, we will not use the algebraic methods of [section 6.2](/chapter-6/6.2) since we do not have the tools for large systems of equations.

To hunt for a quadratic model in the vertex form, adjust the values of $\color{blue}{a}$, $\color{brown}{h}$ and $\color{green}{k}$ in the figure below.

{{% geogebra ratio="50%" id_1="NYMIg0eN3w5XIZtN" id_2="FdLFe4II" id_m="FdLFe4II" %}}

With data sets like this one it is hard to know which combination of transformations will make the curve fit the data the best.  It will be easier to let technology find the equation for us.

To enter the data into the calculator we press the `STAT` button and select `1: Edit`.

![](/img/chapter-6/horse_regression_1.png#center)

The data is entered into the `L1` and `L2` lists, with the independent values in `L1` and the dependent values in `L2`.

![](/img/chapter-6/horse_regression_2.png#center)

To view the scatterplot, press `2ND` and `Y=` to enter the `STAT PLOTS` menu,  then select the first plot and make sure it is turned on.

![](/img/chapter-6/horse_regression_3.png#center)

Using `9:ZoomStat` in the `ZOOM` menu gives a good viewing window for the data.

![](/img/chapter-6/horse_regression_4.png#center)

Once we have confirmed the shape of the data, we go back to the `STAT` menu and this time choose the `CALC` tab.

![](/img/chapter-6/horse_regression_5.png#center)

This reveals all of the regression models built into the calculator, letting us choose the model that we think visually matches the shape of the data.  Since this data looks like the square function, we choose `5: QuadReg`.  If the data had looked like a line then `4: LinReg(ax+b)` would have been a good choice.

After running `5: QuadReg` we are shown the equation that fits the data.

![](/img/chapter-6/horse_regression_6.png#center)

The result is given in the standard form $y = a x^{2} + b x + c$ rather than in the vertex form we used when trying to fit the data by hand.  Copying this equation into the graphing window shows that it fits the data reasonably well.

![](/img/chapter-6/horse_regression_7.png#center)

We could now use the equation $y=239.8x^2-3147.9x+24397.8$ as the basis for a model of the wild mustang population in Nevada.

It bears repeating that a mathematical model is not the same as the real object, nor does it control the behavior of the real thing.  For instance, this model might *predict* the future number of wild mustangs, but it is not a guarantee of what will happen.
